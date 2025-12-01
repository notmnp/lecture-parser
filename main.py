from tqdm import tqdm
import os
import sys
import glob
import shutil
import time
import base64
from openai import OpenAI
from pdf2image import convert_from_path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants - can be overridden via environment variables
PDF_DIR = os.getenv('PDF_DIR', 'PDFs')
SUMMARY_DIR = os.getenv('SUMMARY_DIR', 'Summaries')
TMP_IMG_DIR = os.getenv('TMP_IMG_DIR', 'tmp_slide_imgs')

# Groq model names and API endpoint
VISION_MODEL = os.getenv('VISION_MODEL', 'meta-llama/llama-4-scout-17b-16e-instruct')
TEXT_MODEL = os.getenv('TEXT_MODEL', 'openai/gpt-oss-20b')
API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.groq.com/openai/v1')

VISION_PROMPT = (
    "Provide a detailed, faithful summary of this lecture slide. "
    "Capture ALL content: equations, formulas, definitions, bullet points, and any written text. "
    "If the slide contains diagrams or images, describe what is shown (axes, shapes, arrows, labels, curves, intersections, etc.). "
    "Do not omit or simplify — include more detail rather than less, so no context is lost. "
    "This is not a final summary; it is a comprehensive capture of everything on the slide for later distillation."
)

TEXT_PROMPT = (
    "You are given detailed slide-by-slide summaries of a lecture. "
    "Rewrite them into *problem-solving-focused exam notes* for a student who wants to know:\n"
    "  - What formulas and definitions they must know\n"
    "  - What the main concepts and ideas are\n"
    "  - How to approach typical problems step by step\n"
    "\n"
    "Important rules:\n"
    "- THESE STUDY NOTES WILL BE SAVED AS A MARKDOWN FILE. SO USE MARKDOWN SYNTAX.\n"
    "- Use clear section headings such as:\n"
    "  - Core Formulas & Definitions\n"
    "  - Key Concepts & Intuition\n"
    "  - Problem-Solving Strategies\n"
    "  - Common Pitfalls & Checks\n"
    "- FORMATTING GUIDELINES FOR MATH: Use standard Markdown LaTeX format:\n"
    "  * For inline math, use single dollar signs: $formula$ (NOT \\(formula\\))\n"
    "  * For block math, use double dollar signs: $$formula$$ (NOT \\[formula\\])\n"
    "  * Never use escaped backslashes like \\( or \\[ for math delimiters\n"
    "  * Always check that all math expressions are properly formatted\n"
    "- DO NOT mention slides, slide numbers, or page numbers.\n"
    "- DO NOT organize content by slide.\n"
    "- For each IMPORTANT formula:\n"
    "  * Give the formula in LaTeX\n"
    "  * Explain what each symbol means\n"
    "  * State when/why you would use it (typical problem patterns)\n"
    "- For problem-solving strategies, describe:\n"
    "  * Typical cues in the question (e.g., keywords, structures)\n"
    "  * A short step-by-step approach or checklist\n"
    "  * Any common mistakes to avoid\n"
    "- Eliminate filler prose, agenda items, and purely decorative content.\n"
    "- Avoid repeating the same concept multiple times.\n"
    "- Prefer concise bullet points over long paragraphs.\n"
)

MAX_IMG_PIXELS = int(os.getenv('MAX_IMG_PIXELS', '33000000'))
MAX_IMG_SIZE_MB = int(os.getenv('MAX_IMG_SIZE_MB', '4'))

# How many slide summaries to send to the text model at once
SLIDES_PER_BATCH = int(os.getenv('SLIDES_PER_BATCH', '20'))


def load_api_key():
	"""Load and validate the Groq API key from environment variables."""
	key = os.getenv('GROQ_API_KEY')
	if not key or key == 'your_api_key_here':
		print('Error: GROQ_API_KEY not found or not configured in .env file')
		print('Please copy .env.template to .env and add your API key')
		sys.exit(1)
	return key


def ensure_dirs():
	"""Create required directories if they don't exist."""
	try:
		os.makedirs(PDF_DIR, exist_ok=True)
		os.makedirs(SUMMARY_DIR, exist_ok=True)
		os.makedirs(TMP_IMG_DIR, exist_ok=True)
	except Exception as e:
		print(f'Error: Failed to create directories: {e}')
		sys.exit(1)


def pdf_to_jpegs(pdf_path, out_dir):
	"""Convert PDF pages to JPEG images with size constraints."""
	try:
		images = convert_from_path(pdf_path, fmt='jpeg')
	except Exception as e:
		print(f'Error converting {pdf_path} to images: {e}')
		return []
	img_paths = []
	for idx, img in enumerate(images):
		# Check size constraints
		w, h = img.size
		pixels = w * h
		if pixels > MAX_IMG_PIXELS:
			scale = (MAX_IMG_PIXELS / pixels) ** 0.5
			new_w, new_h = int(w * scale), int(h * scale)
			img = img.resize((new_w, new_h))
		img_path = os.path.join(out_dir, f'slide_{idx+1}.jpeg')
		img.save(img_path, 'JPEG')
		# Check file size
		if os.path.getsize(img_path) > MAX_IMG_SIZE_MB * 1024 * 1024:
			print(f'Warning: Slide {idx+1} in {pdf_path} exceeds {MAX_IMG_SIZE_MB}MB after resizing, skipping.')
			os.remove(img_path)
			continue
		img_paths.append(img_path)
	return img_paths


def call_groq_vision(client, img_path, retries=3):
	"""Call Groq vision API to summarize a slide image."""
	with open(img_path, 'rb') as f:
		img_bytes = f.read()
	img_b64 = base64.b64encode(img_bytes).decode()
	for attempt in range(retries):
		try:
			response = client.chat.completions.create(
				model=VISION_MODEL,
				messages=[{
					"role": "user",
					"content": [
						{"type": "text", "text": VISION_PROMPT},
						{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
					]
				}]
			)
			return response.choices[0].message.content.strip()
		except Exception as e:
			print(f'Warning: Vision API call failed (attempt {attempt+1}/{retries}): {e}')
			if attempt < retries - 1:
				time.sleep(2 ** attempt)  # Exponential backoff
	print(f'Error: Vision API failed after {retries} attempts for {img_path}')
	return '[Vision API failed]'


def batch_slide_summaries(slide_summaries, batch_size=SLIDES_PER_BATCH):
    """Yield successive batches of slide summaries of size at most batch_size."""
    for i in range(0, len(slide_summaries), batch_size):
        yield slide_summaries[i:i + batch_size]


def call_groq_text(client, prompt, retries=3):
	"""Call Groq text API to generate or refine notes."""
	for attempt in range(retries):
		try:
			response = client.chat.completions.create(
				model=TEXT_MODEL,
				messages=[{
					"role": "user",
					"content": prompt
				}]
			)
			return response.choices[0].message.content.strip()
		except Exception as e:
			print(f'Warning: Text API call failed (attempt {attempt+1}/{retries}): {e}')
			if attempt < retries - 1:
				time.sleep(2 ** attempt)  # Exponential backoff
	print(f'Error: Text API failed after {retries} attempts')
	return '[Text API failed]'


def refine_notes_with_batch(client, current_notes, batch_summaries):
	"""Refine notes with a batch of slide summaries.
	
	Args:
		current_notes: Existing notes (str) or None for first batch
		batch_summaries: List of slide summaries to integrate
		
	Returns:
		Updated notes as string
	"""
	batch_block = '\n'.join(batch_summaries)

	if current_notes is None:
		# First batch: create notes from scratch
		prompt = (
			TEXT_PROMPT
			+ "\n\nHere are detailed slide summaries from a lecture:\n\n"
			+ batch_block
			+ "\n\nProduce well-structured Markdown exam notes that are focused on problem solving:\n"
			"- Highlight the essential formulas, definitions, and main ideas.\n"
			"- Explain when and how to use each formula in typical problems.\n"
			"- Include short step-by-step strategies or checklists for common problem types.\n"
			"- Avoid unnecessary repetition."
		)
	else:
		# Subsequent batches: update existing notes with new material
		prompt = (
			TEXT_PROMPT
			+ "\n\nHere are the current draft study notes:\n\n"
			+ current_notes
			+ "\n\nHere are additional detailed slide summaries from later slides:\n\n"
			+ batch_block
			+ "\n\nUpdate and improve the notes with a focus on problem solving:\n"
			"- Integrate any genuinely new formulas, concepts, or problem patterns.\n"
			"- Add or refine step-by-step strategies where the new slides provide more detail.\n"
			"- Remove redundancy and keep the structure clear and easy to scan.\n"
			"- Do NOT just repeat the same idea multiple times."
		)

	updated_notes = call_groq_text(client, prompt)
	return updated_notes


def rolling_batched_summarize(client, slide_summaries, batch_size=SLIDES_PER_BATCH, lecture_name=""):
    """Generate final lecture notes using batched processing.
    
    Args:
        slide_summaries: List of slide summaries from vision API
        batch_size: Number of slides to process per batch
        lecture_name: Name of the lecture for progress display
        
    Returns:
        Final lecture notes as a single string
    """
    notes = None
    batches = list(batch_slide_summaries(slide_summaries, batch_size=batch_size))

    desc = f"{lecture_name} (Text Summarization)" if lecture_name else "Text Summarization"
    with tqdm(total=len(batches), desc=desc, unit="batch") as pbar:
        for batch_idx, batch in enumerate(batches, start=1):
            pbar.set_postfix_str(f"Batch {batch_idx}")
            notes = refine_notes_with_batch(client, notes, batch)
            pbar.update(1)

    return notes


def process_pdf(pdf_path, client):
	"""Process a single PDF file into lecture notes."""
	lecture_name = os.path.splitext(os.path.basename(pdf_path))[0]
	img_dir = TMP_IMG_DIR
	img_paths = pdf_to_jpegs(pdf_path, img_dir)
	if not img_paths:
		print(f'Warning: No valid slides found in {pdf_path}')
		return
	slide_summaries = []

	# Vision phase
	with tqdm(total=len(img_paths), desc=f"{lecture_name} (Slide Summarization)", unit="slide") as pbar:
		for idx, img_path in enumerate(img_paths):
			pbar.set_description(f"{lecture_name} (Slide {idx+1} Summarization)")
			summary = call_groq_vision(client, img_path)
			slide_summaries.append(f'Slide {idx+1}: {summary}')
			pbar.set_postfix_str(f"Slide {idx+1}")
			pbar.update(1)

	# Batched rolling text summarization (with tqdm)
	lecture_notes = rolling_batched_summarize(
		client,
		slide_summaries,
		batch_size=SLIDES_PER_BATCH,
		lecture_name=lecture_name
	)

	# Write output
	out_path = os.path.join(SUMMARY_DIR, f'{lecture_name}.md')
	with open(out_path, 'w', encoding='utf-8') as f:
		f.write(f'# {lecture_name}\n\n')
		f.write('## Study Notes\n\n')
		f.write(lecture_notes + '\n\n')
		f.write('---\n\n')
		f.write('## Raw Slide Summaries\n\n')
		for idx, summary in enumerate(slide_summaries):
			f.write(f'### Slide {idx+1}\n\n')
			f.write(summary.replace(f'Slide {idx+1}: ', '') + '\n\n')
	print(f'Output written to {out_path}')

	# Clean up images
	for img_path in img_paths:
		try:
			os.remove(img_path)
		except Exception:
			pass

def main():
	"""Main entry point for the lecture parser."""
	ensure_dirs()
	api_key = load_api_key()
	client = OpenAI(base_url=API_BASE_URL, api_key=api_key)
	
	pdfs = glob.glob(os.path.join(PDF_DIR, '*.pdf'))
	if not pdfs:
		print(f'No PDF files found in {PDF_DIR}/')
		return
	
	for pdf_path in pdfs:
		process_pdf(pdf_path, client)
	
	# Clean up tmp dir
	try:
		if os.path.exists(TMP_IMG_DIR):
			shutil.rmtree(TMP_IMG_DIR)
	except Exception:
		pass

if __name__ == '__main__':
	main()
