# Lecture Parser

A production-ready tool that converts PDF lecture slides into structured study notes using AI vision and text models via the Groq API.

## Features

- 📄 Converts PDF slides to detailed summaries using vision AI
- 📝 Generates problem-solving-focused study notes
- 🔄 Batched processing for efficient API usage
- 📊 Progress tracking with tqdm
- 🔧 Configurable via environment variables
- ⚡ Automatic retry with exponential backoff

## Prerequisites

- Python 3.8+
- Groq API key ([Get one here](https://console.groq.com/keys))
- poppler-utils (for PDF to image conversion)

### Installing poppler

**macOS:**
```bash
brew install poppler
```

**Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**Windows:**
Download from [poppler releases](http://blog.alivate.com.au/poppler-windows/) and add to PATH.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd lecture_parsing
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
cp .env.template .env
# Edit .env and add your GROQ_API_KEY
```

## Usage

1. Place your PDF lecture files in the `PDFs/` directory

2. Run the parser:
```bash
python main.py
```

3. Find generated notes in the `Summaries/` directory

## Configuration

All configuration can be done via the `.env` file:

### Required
- `GROQ_API_KEY`: Your Groq API key

### Optional
- `VISION_MODEL`: Vision model to use (default: `meta-llama/llama-4-scout-17b-16e-instruct`)
- `TEXT_MODEL`: Text model to use (default: `openai/gpt-oss-20b`)
- `PDF_DIR`: Input directory for PDFs (default: `PDFs`)
- `SUMMARY_DIR`: Output directory for summaries (default: `Summaries`)
- `TMP_IMG_DIR`: Temporary directory for slide images (default: `tmp_slide_imgs`)
- `SLIDES_PER_BATCH`: Number of slides to process per batch (default: `20`)
- `MAX_IMG_PIXELS`: Maximum pixels per image (default: `33000000`)
- `MAX_IMG_SIZE_MB`: Maximum image file size in MB (default: `4`)

## Output Format

Each processed PDF generates a Markdown file containing:
- **Study Notes**: Problem-solving focused summary with:
  - Core formulas and definitions
  - Key concepts and intuition
  - Problem-solving strategies
  - Common pitfalls
- **Raw Slide Summaries**: Detailed summaries of each slide

## Error Handling

- Automatic retry with exponential backoff for API calls
- Individual PDF processing errors don't stop the entire batch

## Project Structure

```
lecture_parsing/
├── main.py                 # Main application
├── requirements.txt        # Python dependencies
├── .env.template          # Environment variable template
├── .env                   # Your configuration (git-ignored)
├── README.md              # This file
├── PDFs/                  # Input PDFs
└── Summaries/             # Generated notes (auto-created)
```
