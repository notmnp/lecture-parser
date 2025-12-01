# MTE 220 - Module 2 - Opamps and Opamp Circuits (annotated)

## Study Notes

# Instrumentation Amplifiers – Problem‑Solving Study Guide  

---

## Core Formulas & Definitions  

| Formula | Meaning of Symbols | When & Why Use It |
|---------|--------------------|-------------------|
| **Differential gain of a two‑op‑amp IA**<br>$$A_d = \Bigl(1 + \frac{R_2}{R_1}\Bigr)\frac{R_4}{R_3} \;\;=\;A_1A_2$$ | • $R_1, R_2$ – resistor pair on the first op‑amp<br>• $R_3, R_4$ – resistor pair on the second op‑amp<br>• $A_1$ – first stage gain, $A_2$ – second stage gain | Use to set the overall gain of a fixed‑gain IA.  Pick $R_1$–$R_4$ so that $A_1A_2$ equals the desired $A_d$. |
| **Single‑stage gain (difference amp)**<br>$$A = 1 + \frac{R_f}{R_i}$$ | • $R_i$ – input resistor<br>• $R_f$ – feedback resistor | Use when you need only a single difference stage.  It gives a common‑mode gain of 1, so CMRR is limited by resistor matching. |
| **CMRR of a two‑stage IA**<br>$$\mathrm{CMRR}_{\text{dB}} \approx 20\log_{10}\!\Bigl(\frac{R_1}{\Delta R}\Bigr)$$ where $\Delta R$ is the mismatch between $R_1$ and $R_2$ (or $R_3$ & $R_4$) | • $\Delta R = |R_1-R_2|$ | Use to estimate how resistor tolerance or temperature drift degrades CMRR. |
| **Fixed‑gain IA with adjustable resistor**<br>$$A_d = \Bigl(1 + \frac{R_2}{R_1}\Bigr)\frac{R_G}{R_1} \quad\text{(with $R_3=R_1$, $R_4=R_G$)}$$ | • $R_G$ – user‑selectable gain resistor (often $2R_1$)<br>• $R_1, R_2$ – matched on‑chip | Use when you want a single variable gain parameter while keeping the rest matched on‑chip for CMRR. |

### Definitions  

* **$V_{\text{diff}} = V_{in+} - V_{in-}$** – differential input voltage.  
* **$V_{\text{CM}} = \dfrac{V_{in+}+V_{in-}}{2}$** – common‑mode input voltage.  
* **$A_d$** – differential (signal) gain.  
* **$A_{\text{CM}}$** – common‑mode gain (ideally zero).  
* **CMRR** – common‑mode rejection ratio, usually expressed in dB.  
* **$R_{\text{in}}$** – input resistance (ideally $\infty$ for sensor interfaces).  
* **$I_{\text{in}}$** – input bias current (ideally $0$).  

---

## Key Concepts & Intuition  

* **High Input Impedance** – Sensors often have high output resistance; the amplifier must not load the sensor. Use a first stage that draws negligible current ($R_{\text{in}}\to\infty$, $I_{\text{in}}\to0$).  
* **Resistor Matching** – CMRR depends critically on matching the resistor pairs. Even a 1 % mismatch can reduce CMRR by ~40 dB.  
* **On‑chip vs Off‑chip Resistors** – Match the majority of resistors on‑chip or using resistor arrays; leave only the gain‑setting resistor off‑chip if a variable gain is needed.  
* **Fixed‑Gain vs Variable‑Gain IA** – Fixed‑gain IAs offer the best CMRR because all resistors are matched. Variable‑gain IAs trade some CMRR for flexibility.  
* **Common‑Mode Range** – Ensure the op‑amp’s input common‑mode range includes $V_{\text{CM}}$; otherwise the IA may saturate or become non‑linear.  

---

## Problem‑Solving Strategies  

| Typical Problem | Quick Cues | Step‑by‑Step Checklist | Common Mistakes |
|-----------------|------------|------------------------|-----------------|
| **Design an IA for a low‑output sensor** | Sensor voltage < 100 µV, sensor resistance > 10 kΩ | 1. Choose op‑amp with low bias current & low offset.<br>2. Use a two‑stage IA to achieve high CMRR.<br>3. Set $R_1$ and $R_3$ on‑chip (matched).<br>4. Select $R_2$ (or $R_G$) to get desired $A_d$.<br>5. Verify $V_{\text{CM}}$ within op‑amp range. | Neglecting resistor matching; using a single difference amp. |
| **Achieve a specified gain $A_d$** | Gain target given, e.g., 50× | 1. Pick convenient $R_1$ (e.g., 10 kΩ).<br>2. Compute $R_2$ from $A_1=1+R_2/R_1$.<br>3. Choose $R_3$ = $R_1$ (match).<br>4. Compute $R_4$ from $A_2=R_4/R_3$.<br>5. Check that $A_1A_2$ ≈ target. | Wrong order of operations; rounding resistor values without considering tolerance. |
| **Estimate CMRR for a design** | Resistor tolerances known, e.g., ±0.1 % | 1. Compute mismatch $\Delta R$ for each pair.<br>2. Apply $$\mathrm{CMRR}_{\text{dB}} \approx 20\log_{10}\!\Bigl(\frac{R}{\Delta R}\Bigr).$$<br>3. Sum contributions if multiple stages. | Assuming ideal CMRR; ignoring op‑amp offset. |
| **Convert a fixed‑gain IA to variable‑gain** | Need gain adjustment while keeping CMRR high | 1. Keep $R_1$–$R_4$ on‑chip matched.<br>2. Use a single variable resistor $R_G=2R_1$ in the second stage.<br>3. Re‑calculate overall gain as $$A_d= (1+R_2/R_1) \cdot \frac{R_G}{R_1}.$$ | Forgetting to update $A_d$ when $R_G$ changes; using an off‑chip $R_G$ that mismatches $R_1$. |
| **Verify common‑mode input range** | $V_{\text{CM}}$ close to rail voltage | 1. Check op‑amp datasheet for $V_{\text{CM}}$ range.<br>2. Ensure sensor output + bias does not exceed limits.<br>3. If out of range, consider adding a bias network or a rail‑to‑rail op‑amp. | Ignoring $V_{\text{CM}}$ limits leads to clipping. |

---

## Common Pitfalls & Checks  

| Pitfall | What to Check | Quick Fix |
|---------|---------------|-----------|
| **Resistor mismatch** | Measure $R_1$ vs $R_2$, $R_3$ vs $R_4$. | Use resistor arrays; match on‑chip. |
| **Input bias current loading** | Verify op‑amp bias current vs sensor source impedance. | Use JFET or CMOS op‑amp; add bias resistor if needed. |
| **Offset voltage amplification** | Compute $V_{\text{offset}} = V_{\text{offset,opamp}} \times A_d$. | Select op‑amp with low offset; consider offset nulling. |
| **Common‑mode range exceeded** | Compute expected $V_{\text{CM}}$; compare to op‑amp spec. | Switch to rail‑to‑rail or add a bias network. |
| **Incorrect gain formula** | Ensure you use $A_1A_2$ for two‑stage IA; not just $1+R_f/R_i$. | Double‑check resistor roles; use table above. |
| **Leaving $R_G$ off‑chip** | Verify $R_G$ is matched to $R_1$ if variable. | Use precision trim or on‑chip tuning resistor. |

---

## Quick Reference Cheat Sheet  

```markdown
## Differential Gain
A_d = (1 + R2/R1) * (R4/R3)

## Fixed‑gain Variable‑resistor IA
A_d = (1 + R2/R1) * (RG/R1)   (with RG = 2R1 for high CMRR)

## Common‑mode Rejection (approx)
CMRR_dB ≈ 20 log10 (R / ΔR)

## Input Resistance
R_in ≈ ∞  (ideal for sensor input)

## Common‑mode Voltage
V_CM = (V_in+ + V_in-) / 2
```

---

### Quick Problem Walk‑through

1. **Sensor gives 30 µV/°C, R_out = 10 kΩ.**  
   *Choose IA:*  
   - Op‑amp with <10 nA bias.  
   - Fixed‑gain IA: $A_d = 1000$ → $R_2/R_1 ≈ 999$ (use $R_1$ = 10 kΩ, $R_2$ = 10 MΩ).  
   - Match $R_3=R_1$, $R_4=R_2$ on‑chip.

2. **Desired gain 50×, tolerance ±1 %**  
   - Pick $R_1 = 10 kΩ$; $R_2 = 490 kΩ$.  
   - $R_3 = 10 kΩ$; $R_4 = 500 kΩ$.  
   - Verify $A_d ≈ 50$; CMRR ≈ 20 log10(10 kΩ / 100 Ω) ≈ 80 dB.

3. **Variable gain needed (10–100×)**  
   - Use $R_G$ in range 20 kΩ–200 kΩ (fixed $R_1$=10 kΩ).  
   - $A_d = (1+R_2/R_1) * (R_G/R_1)$.  
   - Adjust $R_G$ to set gain.

---

Use this guide to quickly identify which formulas to apply, how to set the resistor values, and what to double‑check before finalizing an instrumentation‑amplifier design.

---

## Raw Slide Summaries

### Slide 1

The image presents a slide from a presentation on "Opamps and Opamp Circuits" as part of Module 2 in the MTE 220 course, titled "Sensors and Instrumentation," offered by the University of Waterloo's Faculty of Engineering.

**Title Section:**

*   **Module 2**: The title of the module is prominently displayed in large black text at the top left of the slide.
*   **Opamps and Opamp Circuits**: Below the module title, the specific topic of the slide is written in slightly smaller but still bold black text.
*   **MTE 220 - Sensors and Instrumentation**: This line provides context for the course and topic, indicating that the slide is part of a larger educational presentation focused on sensors and instrumentation.

**Institutional Information:**

*   **University of Waterloo Logo**: The logo of the University of Waterloo is displayed in the bottom-left corner. The logo features a yellow shield with a red design and a black and white chevron, accompanied by the words "UNIVERSITY OF WATERLOO" in black text. To the right of the logo, a vertical line separates it from the text "FACULTY OF ENGINEERING," which is also in black.

**Background and Image:**

*   **Background**: The background of the slide is divided into two sections. The left side has a white background, while the right side features a close-up image of a circuit board. The circuit board image is predominantly teal and black, showcasing various components and pathways.
*   **Circuit Board Image**: The right side of the slide displays a detailed image of a circuit board, which appears to be a key visual element related to the topic of opamps and opamp circuits. The image includes various components such as chips, resistors, and wiring, all depicted in shades of teal against a black background.

Overall, the slide effectively combines textual information with a relevant visual aid to introduce the topic of opamps and opamp circuits within the context of the MTE 220 course.

### Slide 2

The image presents a slide from a presentation, likely related to electronics or electrical engineering. The title of the slide is:

**2.1 - Opamp and Amplifier Circuit Models**

The slide features a prominent title in large black text, centered on the page. Above the title, there is a horizontal strip showcasing a close-up image of a computer circuit board, characterized by various shades of teal and green hues. The circuit board image is set against a white background.

In the bottom-right corner of the slide, a small logo is visible, consisting of a yellow shield with a red design and a black and white chevron pattern. At the bottom center of the slide, the number "2" is displayed in small black text.

Overall, the slide appears to be an introductory slide for a section on operational amplifier (opamp) and amplifier circuit models, suggesting that the presentation will delve into the topic of electronic circuits and their modeling.

### Slide 3

The image presents a lecture slide focused on the topic of "Motivation" in the context of electronics or electrical engineering. The slide is divided into two main sections: a list of bullet points on the left and a circuit diagram on the right.

**Bullet Points:**

*   **We need to understand, predict, and mitigate what happens when real ≠ ideal**
    *   This point emphasizes the importance of understanding and addressing the differences between ideal and real-world conditions in electronic circuits.
*   **We need to understand loading, especially when we get to sensors**
    *   This point highlights the significance of understanding loading effects, particularly in the context of sensor applications.
*   **Sensor with high output resistance**
    *   This point mentions sensors with high output resistance, which can be affected by loading.
*   **Amplifier with low input resistance**
    *   This point notes amplifiers with low input resistance, which can also be impacted by loading effects.
*   **The modeling we'll do looks a lot like the Thevenin-equivalent MTE 120 material**
    *   This point indicates that the modeling approach will resemble the Thevenin-equivalent method covered in MTE 120 material.

**Circuit Diagram:**

The circuit diagram on the right side of the slide appears to be a simple amplifier circuit with input and output connections. The diagram includes:

*   **Input and Output Connections:**
    *   $V_{in}$ (input voltage)
    *   $V_{out}$ (output voltage)
*   **Resistances:**
    *   $R_{in}$ (input resistance)
    *   $R_{out}$ (output resistance)
    *   $R_L$ (load resistance)
*   **Amplifier Representation:**
    *   The amplifier is represented by a simple symbol with a gain of $A$
*   **Equations:**
    *   $V_{out} = AV_{in}$ (output voltage equation)

**Additional Elements:**

*   A logo in the bottom-right corner features a shield with a red and yellow design.
*   The background of the slide is white, with a purple and black bar at the top.
*   The slide number "3" is displayed at the bottom center.

### Slide 4

The image presents a slide from a presentation on two-port networks, featuring a white background with a purple and black border at the top. The title "Two-Port Networks" is prominently displayed in large black text.

**Key Points:**

* A circuit with two connections to the outside world
* Sometimes the two ports don't influence each other
* Sometimes they do

**Diagrams:**

The slide includes three diagrams illustrating different types of two-port networks:

1. **First Diagram:**
	* A simple two-port network with two ports labeled $V_1$ and $V_2$, and currents $I_1$ and $I_2$.
	* No additional components are shown.
2. **Second Diagram:**
	* A two-port network consisting of two resistors $R_1$ and $R_2$ in parallel.
	* The ports are labeled $V_1$ and $V_2$, with currents $I_1$ and $I_2$.
3. **Third Diagram:**
	* A two-port network featuring two resistors $R_1$ and $R_2$ in series.
	* The ports are labeled $V_1$ and $V_2$, with currents $I_1$ and $I_2$.

**Additional Elements:**

* A yellow and red crest logo is located in the bottom-right corner of the slide.
* The number "4" is centered at the bottom of the slide, likely indicating the slide number.

### Slide 5

The slide is titled "Amplifiers" and contains the following content:

**Text:**

* A two-port network
	+ Port 1: Input
	+ Port 2: Output
* Input influences output
* Output does not influence input
* A is called the "gain"
* Units of [Output Units]/[Input Units]

**Equations and Formulas:**

* None explicitly written, but the relationship between input and output is represented as Vout = AVin, where A is the gain.

**Diagrams:**

* A circuit diagram showing a two-port network with input voltage Vin, output voltage Vout, and a dependent voltage source AVin.
	+ The input port is on the left, with a voltage source Vin.
	+ The output port is on the right, with a voltage Vout.
	+ A diamond-shaped symbol represents the dependent voltage source AVin.
* A simple amplifier symbol diagram:
	+ A triangle with the gain A inside.
	+ Vin on the left and Vout on the right.

**Other Elements:**

* A logo in the bottom-right corner, which appears to be a shield with a red and yellow design.
* A page number "5" in the bottom center of the slide.
* A purple and black bar at the top of the slide.

### Slide 6

The slide presents four amplifier topologies, each with its own unique characteristics and applications.

**Title:** Four Amplifier Topologies

**Amplifier Topologies:**

### Voltage Amplifier

* Circuit diagram: A voltage amplifier with input voltage $V_{in}$ and output voltage $V_{out}$
* Open-Circuit Voltage Gain: $A_{vo} = \frac{v_{out}}{v_{in}} [\frac{V}{V}]$

### Transconductance Amplifier

* Circuit diagram: A transconductance amplifier with input voltage $V_{in}$ and output current $I_{out}$, represented as a controlled current source
* Short-Circuit Transconductance: $G_{m} = \frac{i_{out}}{v_{in}} [\frac{A}{V}]$

### Transresistance/Transimpedance Amplifier

* Circuit diagram: A transresistance/transimpedance amplifier with input current $I_{in}$ and output voltage $V_{out}$
* Open-Circuit Transresistance: $R_{m} = \frac{v_{out}}{i_{in}} [\frac{V}{A}]$
* Handwritten note: TIA

### Current Amplifier

* Circuit diagram: A current amplifier with input current $I_{in}$ and output current $I_{out}$
* Short-Circuit Current Gain: $A_{is} = \frac{i_{out}}{i_{in}} [\frac{A}{A}]$

**Additional Notes:**

* Handwritten note at the top: OTA: Operational Transconductance Amp.
* A crest logo is present in the bottom-right corner of the slide.

### Slide 7

The image presents a comprehensive overview of op-amp models, focusing on both real and ideal behavior. The title, "Opamp Models - Real and Ideal Behaviour," is prominently displayed at the top.

**Left Side: Op-Amp Circuit and Equations**

* A simple op-amp circuit diagram is shown, featuring:
	+ Input voltage Vin
	+ Output voltage Vout
	+ Power supply voltages VDD and VSS
* The equation Vout = Ao * Vin is written, where Ao represents the open-loop gain.
* Handwritten notes provide additional information:
	+ "Top voltage rail" and "Max working voltage" with examples (1.5V, 5V USB, 3.3V)
	+ "Bottom voltage rail" and "Min working voltage" with examples (GND, -5V)
	+ Ao = 1M [V/V]
	+ 1V → 1MV out and 1μV → 1V out, indicating the high gain of the op-amp

**Right Side: Voltage Transfer Curve (VTC)**

* A graph illustrates the VTC, plotting Vout against Vin.
* The graph features:
	+ A blue line representing the ideal op-amp behavior with unlimited output voltage
	+ A green line indicating the actual output voltage limits (VDD = +1.5V, VSS = -1.5V)
	+ Red annotations highlighting:
		- Open-loop and closed-loop behavior
		- Positive and negative feedback
		- Shifts due to offset error
* The graph shows that the op-amp's output voltage is limited by the power supply voltages and that the actual output voltage deviates from the ideal behavior due to various factors.

Overall, the image provides a detailed comparison of ideal and real op-amp behavior, highlighting the limitations and characteristics of op-amp models.

### Slide 8

The image presents a comprehensive overview of op-amp models, specifically focusing on equivalent circuits. The title "Opamp Models - Equivalent Circuit" is prominently displayed at the top.

**Key Components and Equations:**

* Two op-amp equivalent circuits are illustrated, each with distinct characteristics:
	+ The left circuit features:
		- Input current $I_{in} = 0$ (noted as a mostly good assumption at low frequency)
		- Input voltage $V_{in}$
		- Output voltage $V_{out} = A_0 V_{in} = A_0(V_+ - V_-)$
	+ The right circuit includes:
		- Output resistance $R_{out}$
		- Load resistance $R_L$
		- Output current $I_{out}$
		- Output voltage $V_{out} - I_{out}R_{out}$
		- The equation $V_{th}$, open-circuit voltage $V_{oc}$, and the note "Accounts for drop in $V_{out}$ due to loading ($I_{out} \neq 0$)"
* Handwritten notes at the bottom of the image mention:
	+ $I_{in} = 0$ (mostly good assumption at low frequency)
	+ As a next level of modeling, we would include $R_s$, $C_s$, and $L_s$ that represent physical effects (e.g., input capacitance)

**Visual Elements:**

* The image features two op-amp equivalent circuits, each with a triangular symbol and various components.
* The circuits are accompanied by handwritten notes and equations in blue and black ink.
* A logo is present in the bottom-right corner, consisting of a yellow shield with a red cross and a black chevron.

**Overall:**

The image provides a detailed comparison of two op-amp equivalent circuits, highlighting their differences and key characteristics. The handwritten notes and equations add context and clarify the assumptions and limitations of each model. The visual representation of the circuits and components facilitates understanding and analysis of the op-amp models.

### Slide 9

The image shows a lecture slide titled "Example: Output Loading" and features a white background with a purple and black border at the top. The slide contains the following content:

**Title and Text**

* The title "Example: Output Loading" is displayed in bold black font.
* A bullet point explains that an opamp in open-loop configuration outputs 4.00 V with no load, but the output voltage drops to 3.98 V when a 100 Ω resistor is attached. The task is to determine the opamp's R<sub>out</sub>.

**Equations and Formulas**

* V<sub>out</sub> = 4V, I<sub>out</sub> = 0
* V<sub>out</sub> = 3.98V, R<sub>L</sub> = 100 Ω
* V<sub>out</sub> = V<sub>in</sub> * R<sub>L</sub> / (R<sub>L</sub> + R<sub>out</sub>)
* 3.98 = 4 * 100 / (100 + R<sub>out</sub>)
* R<sub>out</sub> = 50 mΩ ≈ 0.5 Ω

**Diagrams**

* Two hand-drawn circuit diagrams are present:
	+ Diagram 1: A simple opamp circuit with a voltage source and a resistor labeled R<sub>out</sub>. The voltage is labeled as 4V, and the current is labeled as I<sub>out</sub> = 0.
	+ Diagram 2: A circuit with a voltage source, a resistor labeled R<sub>out</sub>, and a load resistor R<sub>L</sub> = 100 Ω. The voltage is labeled as 4V, and the output voltage is labeled as 3.98V.

**Additional Notes**

* A note in green handwriting at the bottom of the slide reads: "*Trick away: Amplifier loading problems are Thevenin/Norton in disguise."
* A small logo featuring a yellow and red shield with a black design is located in the bottom-right corner of the slide.

### Slide 10

The slide is titled "Amplifier Circuit Models" and contains the following content:

**Title and Bullet Points:**

* The title is in large black text at the top of the slide.
* Two bullet points are listed below the title:
	+ "Summarizes the terminal behaviour of an amplifier circuit in a simplified model"
	+ "Makes it straightforward to deal with connecting many amp stages"

**Circuit Diagrams:**

* Three circuit diagrams are shown in the top half of the slide, connected by red arrows:
	1. The first diagram shows a simple inverting amplifier circuit with:
		- Input voltage $V_{in}$
		- Resistors $R_1$ and $R_2$
		- Output voltage $V_{out}$
		- An op-amp symbol
	2. The second diagram shows the same circuit with the op-amp symbol replaced by a triangle
	3. The third diagram shows a simplified model of the amplifier circuit with:
		- Input voltage $V_{in}$
		- Input resistance $R_{in}$
		- Output resistance $R_{out}$
		- A voltage-controlled voltage source with gain $A_{v0}V_{in}$
		- Output voltage $V_{out}$
* A handwritten note in red and blue text next to the third diagram reads:
	+ "'open-circuit voltage gain'"
	+ "$e.g. -\frac{R_2}{R_1}, 1 + \frac{R_2}{R_1}$, etc."

**Additional Diagrams:**

* A series of four identical circuit diagrams are shown in the bottom half of the slide, representing multiple amplifier stages connected together.

**Footer:**

* The number "10" is centered at the bottom of the slide.
* A logo is located in the bottom-right corner, featuring a yellow shield with a red dragon and a black and white chevron.

### Slide 11

The slide presents a detailed analysis of amplifier circuit models, focusing on finding equivalent model values such as $R_{in}$, $A_{vo}$, and $R_{out}$. 

**Title and Bullet Points**

* The title of the slide is **Amplifier Circuit Models**.
* A bullet point reads: "Find equivalent model values: $R_{in}$, $A_{vo}$. What about $R_{out}$?"

**Equations and Formulas**

The following equations and formulas are presented:

* $R_{in} = \frac{V_{in}}{I_{in}}$
* $I_{in} = \frac{V_{in} - V_{-}}{R_{1}} = \frac{V_{in}}{R_{1}}$
* $\therefore R_{in} = \frac{V_{in}}{(V_{in}/R_{1})} = R_{1}$
* $A_{vo} = -\frac{R_{f}}{R_{i}}$ (closed-loop gain)
* $R_{out} = \frac{\Delta V_{out}}{\Delta I_{out}} = 0\Omega$ (CLNF)

**Circuit Diagram**

The circuit diagram depicts an amplifier with the following components:

* $R_{1}$ and $R_{2}$ resistors
* An op-amp with a triangle symbol
* Input voltage $V_{in}$ and output voltage $V_{out}$
* A "Virtual Ground" label

The diagram includes various annotations, such as:

* $I_{in}$ and $V_{in}$ labels
* Arrows indicating the direction of current flow
* A "Virtual Ground" label
* $\Delta I_{out}$ and $\Delta V_{out}$ labels

**Additional Text and URL**

* The text "If we apply a load current, $\Delta I_{out}$, how much does $V_{out}$ change by? $\Delta V_{out} = \frac{0}{\Delta I_{out}} = 0\Omega$" is written in red and blue ink.
* A URL is provided at the bottom left corner: https://everycircuit.com/circuit/6302906743259136

### Slide 12

The image presents a comprehensive overview of nonideal op-amp parameters, featuring a white background with a purple gradient at the top. The title "Nonideal Opamp Parameters" is prominently displayed in bold black text.

**Circuit Diagrams and Equations**

The slide includes two circuit diagrams:

*   **Open-Loop Differential Gain**: This diagram illustrates the open-loop differential gain of an op-amp, accompanied by equations that describe its behavior. The diagram shows a differential amplifier with input voltages V+ and V-, and output voltage Vo. The equations provided are:
    *   Ao = Adiff = Vo / Vin = Vo / (V+ - V-)
    *   Ideally, Vo = Ao (V+ - V-) = Ao (Vcm - Vcm) = 0
    *   But, Vo is a function of Vcm
    *   Acm = Vo / Vcm, Many orders of magnitude smaller than Adiff
*   **Common Mode Gain**: This diagram depicts the common-mode gain of an op-amp, along with a brief description of its characteristics.

**Table of Parameters**

A table is presented, listing various parameters related to op-amps, including:

| Parameter | Typical range | Ideal values |
| :-------- | :------------ | :----------- |
| Open-loop gain, A | 100k to 10M [V/V] | ∞ [V/V] |
| Input resistance, Ri | 100k to 10T Ω | ∞ Ω |
| Output resistance, Ro | 0.1 to 100 Ω | 0 Ω |
| Supply voltage, VDD | 1 to 24 V | ∞ V |

**DC Offset, Slew Rate, and Gain Bandwidth Product**

The slide also covers three key concepts:

*   **DC Offset**: A diagram illustrates the DC offset of an op-amp, with handwritten notes explaining its significance. The notes state that if you apply V+ = V- = 0V, you should get Vo = 0V. However, due to manufacturing randomness, Vos ≠ "Input-Referred offset voltage." The notes also provide an equation: Vo = Ao (V+ - V- - Vos) ~ μV.
*   **Slew Rate**: A graph shows the slew rate of an op-amp, with a brief description of its characteristics. The notes explain that the slew rate represents how fast the output can change in response to a step input.
*   **Gain Bandwidth Product**: A graph illustrates the gain-bandwidth product of an op-amp, with handwritten notes providing additional information. The notes state that GBWP = Ao \* f0 = A1 \* f1, and that there is a tradeoff between gain and higher frequencies.

Overall, the image provides a detailed overview of nonideal op-amp parameters, including circuit diagrams, equations, tables, and graphs. The handwritten notes add context and explanations to the diagrams and graphs, making the image a valuable resource for understanding op-amp behavior.

### Slide 13

The slide is titled "Amplifier Models Summary" and provides a detailed overview of amplifier models, including their representation, analysis, and application.

**Title and Introduction**

* The title "Amplifier Models Summary" is prominently displayed at the top of the slide in bold black text.

**Amplifier Representation**

* The slide shows two equivalent representations of an amplifier:
	+ One with input resistance $R_{in}$, output resistance $R_{out}$, and gain $A_{vo}$:
		- Input: $V_{in}$, $R_{in}$
		- Output: $V_{out}$, $R_{out}$, $A_{vo}V_{in}$
	+ Another with a sensor output:
		- Input: $V_{sensor}$, $R_{out}$
		- Output: $V_{out}$

**Thevenin-Type Problems**

* The slide explains that there are two Thevenin-type problems:
	1. Finding $R_{TH}$ and $V_{in}$:
		- $R_{TH} = R_{in} = \frac{V_{in}}{I_{in}}$
		- $I_{in}$
		- $V_{in}$
	2. Finding $R_{out}$ and $V_{out}$:
		- $R_{out} = R_{TH}$
		- $V_{out} = A_{vo}V_{in}$

**Analysis and Application**

* The slide notes that understanding amplifier models helps us analyze what happens when we connect a signal chain together.
* It highlights that there are two types of Thevenin-type problems:
	+ Type 1: Finding $R_{TH}$ and $V_{in}$
	+ Type 2: Finding $R_{out}$ and $V_{out}$
* The slide provides a step-by-step approach to solving these problems:
	+ Set $V_{in} = 0$, $A_{vo}V_{in} = 0V$
	+ Recall that a $0V$ source is like a short circuit
	+ Apply $\Delta I_{out}$, measure $\Delta V_{out}$, or vice versa

**Equations and Formulas**

* The slide includes several equations and formulas, including:
	+ $R_{TH} = R_{in} = \frac{V_{in}}{I_{in}}$
	+ $R_{out} = R_{TH}$

**Diagrams and Images**

* The slide features two hand-drawn diagrams:
	+ A simple amplifier circuit with input resistance, output resistance, and gain
	+ A sensor output circuit with output resistance and voltage

Overall, the slide provides a comprehensive summary of amplifier models, including their representation, analysis, and application. It highlights the importance of understanding amplifier models in signal chain analysis and provides a step-by-step approach to solving Thevenin-type problems.

### Slide 14

The slide is titled "2.2 – Comparators and Schmitt Triggers".

* The title is in large, bold, black text, centered on the slide.
* The slide has a white background.
* At the top of the slide, there is a purple and black bar.
* Below the bar, there is a photograph of a computer circuit board with various components, including:
	+ Teal-colored lines and pathways
	+ Small silver dots and circles
	+ Various shapes and patterns
* In the bottom-right corner of the slide, there is a small logo that appears to be a shield with a red and yellow design.
* In the bottom-center of the slide, there is the number "14" in small black text. 

There are no equations, formulas, definitions, or bullet points on this slide.

### Slide 15

The image presents a comprehensive overview of comparators, a crucial component in electronic circuits. The content is organized into two main sections: a detailed explanation on the left and a visual representation on the right.

**Detailed Explanation:**

*   **Open-loop configuration**
    *   $V_{DD}, V_{+}: 3.3V, 5V, etc.$
*   **$V_{out} = \begin{cases}V_{DD}, & V_{+} > V_{-} \\ V_{SS}, & V_{+} < V_{-}\end{cases}$, i.e. it "hits the rails"**
    *   Digital output ('1': $V_{DD}, V_{+} < V_{-}$; '0': $0V, GUND$)
*   Useful to compare two analog signals and give a digital output
*   E.g.: A digital system with a **light sensor**
    *   '0' = $0 V$, '1' = $5 V$ **output (Arduino)**
    *   Light sensor output voltage exceeds $2 V$ during the day
*   Make 'daytime' and 'nighttime' detectors

**Visual Representation:**

The visual representation consists of two graphs and two circuit diagrams.

*   **Top Graph: "Daytime Detector"**
    *   The graph shows the output voltage ($V_{out}$) versus the input voltage ($V_{in}$) for a non-inverting comparator.
    *   The x-axis represents $V_{in}$, ranging from 0 to 5 volts.
    *   The y-axis represents $V_{out}$, ranging from 0 to 5 volts.
    *   The graph indicates that when $V_{in} < V_{ref}$ (2V), $V_{out}$ is 0V, and when $V_{in} > V_{ref}$, $V_{out}$ is 5V.
*   **Bottom Graph: "Night-time Detector"**
    *   The graph shows the output voltage ($V_{out}$) versus the input voltage ($V_{in}$) for an inverting comparator.
    *   The x-axis represents $V_{in}$, ranging from 0 to 5 volts.
    *   The y-axis represents $V_{out}$, ranging from 0 to 5 volts.
    *   The graph indicates that when $V_{in} < V_{ref}$ (2V), $V_{out}$ is 5V, and when $V_{in} > V_{ref}$, $V_{out}$ is 0V.
*   **Circuit Diagrams:**
    *   The top circuit diagram represents a non-inverting comparator with $V_{ref} = 2V$.
    *   The bottom circuit diagram represents an inverting comparator with $V_{ref} = 2V$.

In summary, the image provides a detailed explanation of comparators, including their open-loop configuration, digital output, and applications in digital systems. The visual representation illustrates the behavior of non-inverting and inverting comparators, highlighting their use in daytime and nighttime detectors.

### Slide 16

The image presents a slide from a presentation on the problem with comparators, focusing on a house heating system. The title "Problem with Comparators" is prominently displayed at the top.

**Main Points:**

* **Consider a house with a furnace and thermostat set to 20 °C**
	+ This point introduces the context of the problem, which involves a simple heating system.
* **Heating Strategy #1: Furnace ON when T<sub>house</sub> < 20 °C**
	+ This strategy outlines the basic approach to controlling the furnace based on the house temperature.
* A graph illustrating the furnace's on/off state and the house temperature over time
	+ The graph shows the furnace turning on and off in a rapid, repetitive pattern as the house temperature fluctuates around the setpoint of 20 °C.
	+ The furnace is represented by a red line, and the house temperature is represented by a green line.
	+ The graph's axes are labeled: "Furnace" (y-axis) with "ON" and "OFF" labels, and "t" (x-axis) representing time.
* A diagram showing the relationship between the house temperature and the furnace's on/off state
	+ This diagram illustrates the comparator's output as a function of the house temperature.
	+ The diagram shows that when the house temperature is below 20 °C, the furnace is ON; otherwise, it is OFF.
* A circuit diagram of a temperature sensor and comparator
	+ The circuit consists of a temperature sensor, a voltage output, and a comparator.
	+ The temperature sensor output is connected to the inverting input of the comparator, and the reference voltage (V<sub>ref</sub>) is connected to the non-inverting input.
	+ The comparator's output is labeled as V<sub>out</sub>.
* **Not a great strategy: Output exhibits "short cycling", "output bounce", "chatter"**
	+ This point highlights the drawbacks of the simple heating strategy, including short cycling, output bounce, and chatter.

**Summary:**

The slide discusses a basic heating strategy for a house with a furnace and thermostat set to 20 °C. The strategy turns the furnace on when the house temperature falls below 20 °C. However, this approach leads to problems such as short cycling, output bounce, and chatter, making it not a great strategy. The slide includes graphs and diagrams to illustrate the issues with this approach.

### Slide 17

The image presents a comprehensive overview of the concept of hysteresis, specifically in the context of heating strategies. The title "Hysteresis" is prominently displayed at the top left, accompanied by two bullet points that provide a concise definition and explanation of the concept.

**Definition and Explanation:**

*   **Heating Strategy #2: Apply a range to slightly over-heat and over-cool**
*   **Called hysteresis: Output depends on inputs and current state (output)**

The slide features four graphs that illustrate the hysteresis concept in a heating system. The graphs are arranged in two rows, with two graphs on the top and two on the bottom.

**Top Graphs:**

*   The top-right graph displays a line graph with temperature on the y-axis and time on the x-axis. The graph shows a red line representing the system's output (ON/OFF) and a green line representing the temperature. The graph also includes a dashed red line indicating the comparator with hysteresis.
*   The top-left graph is not explicitly labeled but appears to show a similar relationship between temperature and time.

**Bottom Graphs:**

*   The bottom-left graph consists of three sub-graphs, each showing the relationship between temperature and time. The sub-graphs are labeled:
    1.  **House cools to 19°C**
    2.  **Furnace turns on and heats to 21°C**
    3.  **Furnace turns off and cools to 19°C**
*   The bottom-right graph displays a hysteresis loop, illustrating the relationship between the system's output (ON/OFF) and the temperature. The graph is labeled **4) Complete heating cycle curve**.

The slide also includes a logo in the bottom-right corner, which appears to be a university or institutional logo.

Overall, the image provides a clear and concise explanation of the concept of hysteresis in the context of heating strategies, along with visual aids to help illustrate the concept.

### Slide 18

The image presents a slide from a lecture on adding hysteresis to a comparator, featuring a white background with black text and purple and black bars at the top.

**Title:** "Adding Hysteresis to a Comparator"

**Bullet Points:**

* Need to move transition point by ±ΔV depending on current state
* Recall that output always flips when V+ > V−
* Consider non-inverting comparator (V+ = Vin, V− = Vref)
	+ Move transition point right by ΔV, apply Vin − ΔV or Vref + ΔV
	+ Move transition point left by ΔV, apply Vin + ΔV or Vref − ΔV
	+ Choose whichever is most convenient to implement
* Same concept for inverting comparator, but opposite implementation

**Handwritten Notes:**

* 100m dash:
	+ Changing Vref is like moving the finish line
	+ Change Vin is like moving the start line

**Circuit Diagram:**

A simple comparator circuit diagram is displayed in the top-right corner, consisting of:

* Vin (input voltage)
* Vref (reference voltage)
* Vout (output voltage)
* A triangle-shaped op-amp symbol

**Transfer Function Graphs:**

Two transfer function graphs are shown, each with:

* Vin (input voltage) on the x-axis
* Vout (output voltage) on the y-axis
* A vertical dotted line indicating the reference voltage (Vref)
* A horizontal arrow pointing to the right, labeled ΔV
* A square-shaped hysteresis loop with a blue outline

The graphs illustrate the effect of adding hysteresis to a comparator, with the top graph showing a non-inverting comparator and the bottom graph showing an inverting comparator. The handwritten notes and bullet points provide additional context and explanations for the concepts presented.

### Slide 19

The slide is titled "Inverting Schmitt Trigger" and features a detailed explanation of the concept.

**Circuit Diagram**

On the left side of the slide, a circuit diagram is shown, which includes:

* A voltage source labeled "+5 V"
* Resistors R1, R2, and R3
* An op-amp with input Vin and Vref, and output Vout
* The output Vout is shown to be equal to either 0 V or 5 V

**Equations and Formulas**

Several equations and formulas are written around the circuit diagram:

* Vref = 5 * R2 / (R1 + R2) = 2.5 V (written in red)
* Two cases are considered:
	+ Case I: Vout = 0 V
		- Vref0 = 5 * R2 * R3 / (R1 * R3 + R2 * (R1 + R3)) = 1.67 V
	+ Case II: Vout = 5 V
		- Vref1 = 5 * R2 / (R1 + R2) * R3 / (R3 + R2) = 3.33 V

**Graph**

On the right side of the slide, a graph is shown with the following features:

* The x-axis is labeled "Vin" and ranges from 0 to 5
* The y-axis is labeled "Vout" and ranges from 0 to 5
* A hysteresis loop is shown, with two curves:
	+ A red curve corresponding to the case without R3 (R1 = R2 = 10 kΩ)
	+ A blue curve corresponding to the case with R3 = 10 kΩ
* The graph shows the output "sticking" to one extreme or the other

**Bullet Points**

Two bullet points are listed on the right side of the slide:

* A comparator with positive feedback
* Makes the output 'stick' to one extreme or the other

**Additional Text**

The slide also includes some additional text:

* "Ignoring R3 leaves a comparator with Vref = 5 * R2 / (R1 + R2) = 2.5 V" (written in red)
* "sweep Vin up, then down" (written in blue)

### Slide 20

The image presents a detailed lecture slide on the topic of "Inverting Schmitt Trigger Example." The slide is divided into two main sections, with the left side featuring a mathematical derivation and the right side displaying a circuit diagram and a graph.

**Main Points:**

* **Title and Description:**
	+ Title: "Inverting Schmitt Trigger Example"
	+ Description: Design the Schmitt trigger circuit in a) to achieve the transition points shown in b). The current through any resistor should not exceed 1 mA.
* **Mathematical Derivation:**
	+ Clue (constraint) to help choose actual resistor values: 3.3V across 3.3kΩ is 1mA. So, choose R3 = 10kΩ as a starting point.
	+ Equations:
		- 1.2 = 3.3 × R2/(R1 + R2)
		- 2.1 = 3.3 × R2/(R1 || R3 + R2)
	+ Solution:
		- R1 = R2 = 7.5kΩ
		- R3 = 10kΩ
* **Circuit Diagram:**
	+ A simple inverting Schmitt trigger circuit with:
		- +3.3V power supply
		- R1, R2, and R3 resistors
		- Op-amp with Vin, Vout, and ground connections
* **Graph:**
	+ A hysteresis loop graph showing:
		- Vout vs. Vin
		- Two transition points: Vref0 (1.2V) and Vref1 (2.1V)

**Summary:**

The slide provides a step-by-step example of designing an inverting Schmitt trigger circuit to achieve specific transition points. The derivation involves choosing resistor values that satisfy the constraint of not exceeding 1 mA current through any resistor. The solution yields R1 = R2 = 7.5kΩ and R3 = 10kΩ. The circuit diagram and graph illustrate the implementation and behavior of the Schmitt trigger circuit.

### Slide 21

The image presents a detailed lecture slide on the topic of a Non-Inverting Schmitt Trigger. The slide is divided into several sections, each providing valuable information about the circuit.

**Title and Circuit Diagram**

* The title "Non-Inverting Schmitt Trigger" is prominently displayed at the top of the slide.
* A circuit diagram is provided, showing the configuration of the Non-Inverting Schmitt Trigger:
	+ The circuit consists of an op-amp with resistors $R_i$ and $R_f$ connected to the inverting input.
	+ The non-inverting input is connected to $V_{ref}$.
	+ The output is labeled as $V_{out}$.

**Equations**

* The slide provides several equations that describe the behavior of the Non-Inverting Schmitt Trigger:
	+ $V_{1\to0} = (1 + \frac{R_i}{R_f})V_{ref} - (\frac{R_i}{R_f})V_{DD}$
	+ $V_{0\to1} = (1 + \frac{R_i}{R_f})V_{ref}$
	+ $\frac{R_i}{R_f} = \frac{V_{0\to1}-V_{1\to0}}{V_{DD}}$
	+ $V_{ref} = \frac{V_{0\to1}}{(\frac{V_{0\to1}-V_{1\to0}}{V_{DD}})+1} = \frac{V_{0\to1}}{\frac{R_i}{R_f}+1}$

**Handwritten Notes**

* Blue handwritten notes on the slide provide additional insights:
	+ "This time, opamp modifies $V_{in}$ to drag it up or down depending on $V_{out}$. $V_{in}$ forming a voltage divider to '0' or '1' (VDD), so $V_{in}$ must work extra hard to exceed $V_{ref}$."
	+ A link to a circuit simulation: "https://everycircuit.com/circuit/5871898185170944"

**Bullet Points**

* Two bullet points are listed on the right-hand side of the slide:
	+ "Output 'drags' $V_+$ up or down (instead of $V_{ref}$)"
	+ "Exercise: Derive transition points using basic opamp assumptions"

**Graph**

* A graph is displayed on the right-hand side of the slide, showing the relationship between $V_{in}$ and $V_{out}$:
	+ The x-axis represents $V_{in}$, ranging from 0 to $V_{DD}$ (5V).
	+ The y-axis represents $V_{out}$, ranging from 0 to $V_{DD}$ (5V).
	+ The graph shows a hysteresis loop with two transition points: $V_{1\to0}$ and $V_{0\to1}$, which are labeled as 2V and 3V, respectively.
	+ Red annotations on the graph indicate the values of $\frac{R_i}{R_f} = \frac{3-2}{5} = \frac{1}{5}$ and $V_{ref} = 2.5V$.

**Additional Information**

* The slide number "21" is displayed at the bottom center of the slide.
* A logo is present in the bottom-right corner of the slide, featuring a yellow and red crest.

### Slide 22

The image presents a slide titled "Analog to Digital Threshold Detection" and features a comprehensive overview of the process. The slide is divided into two main sections: a list of bullet points on the left and two diagrams on the right.

**Bullet Points:**

*   To check if an analog signal is above a certain threshold
    *   Connect directly to GPIO? No!
    *   Unwise to hold digital inputs between 'o' and '1' for extended periods
    *   Can cause short circuit current within the IC
*   Use a comparator opamp circuit
    *   Be sure that expected analog voltage range can be tolerated by opamp inputs
    *   Could use Schmitt Trigger if needed

**Diagrams:**

*   The top-right diagram illustrates a comparator circuit with the following components:
    *   A voltage source labeled "VDD = 3V"
    *   A 20kΩ resistor connected to the positive terminal of the comparator
    *   A 10kΩ resistor connected to the negative terminal of the comparator
    *   A capacitor labeled "CLEAN DIGITAL SIGNAL"
    *   A waveform diagram showing a clean digital signal
*   The bottom-right diagram displays a graph with the following features:
    *   The x-axis labeled "t" (time)
    *   The y-axis labeled "Vout" and "Vin"
    *   A waveform showing the input voltage (Vin) and output voltage (Vout) over time
    *   A dotted line indicating the reference voltage (Vref)

**Additional Elements:**

*   A logo in the bottom-right corner featuring a shield with a red and yellow design
*   The number "22" centered at the bottom of the slide

Overall, the slide provides a clear and concise explanation of the analog-to-digital threshold detection process, including the importance of using a comparator opamp circuit and the potential risks of connecting directly to GPIO. The diagrams effectively illustrate the concepts discussed in the bullet points, making it easier for viewers to understand the material.

### Slide 23

The slide is titled "2.3 – Single-Ended and Differential Signalling".

* The title is written in large, bold black text and centered on the slide.
* The background of the slide is white.
* At the top of the slide, there is a purple and gray gradient bar.
* Below the gradient bar, there is a photograph of a computer circuit board with various components and wiring.
* The circuit board image is teal and black with silver dots and lines.
* In the bottom-right corner of the slide, there is a small logo that appears to be a shield with a red and yellow design.
* In the bottom-center of the slide, there is the number "23" in small black text. 

There are no equations, formulas, definitions, or bullet points on this slide. The slide appears to be an introductory slide for a section on single-ended and differential signalling.

### Slide 24

The image presents a slide from a presentation on electrical engineering, specifically focusing on single-ended and differential ports. The title "Single-Ended and Differential" is prominently displayed at the top.

**Key Points:**

* **Ports can be single-ended or differential**
* **Single-Ended:** Voltages are ground-reference (difference from ground)
* **Differential:** Voltage differences are explicitly provided

**Circuit Diagrams:**

The slide features two circuit diagrams, each with a triangle representing an amplifier. The diagrams are divided into two sections by a dotted line.

**Left Diagram (Single-Ended):**

* Input: $V_{in}$
* Output: $V_{out}$
* Ground symbol: $\stackrel{\perp}{\text{ }}$

**Right Diagram (Differential):**

* Input: $V_{in}$
* Output: $V_{out}$
* Two inputs: $+$ and $-$

**Additional Information:**

* The slide number "24" is displayed at the bottom center.
* A logo featuring a shield with a black and yellow design is located in the bottom-right corner.

Overall, the slide provides a clear and concise explanation of single-ended and differential ports, along with accompanying circuit diagrams to illustrate the concepts.

### Slide 25

The image presents a detailed lecture slide on "Signal Reference Voltage - Opamp," which appears to be part of an educational presentation on electronics or circuit analysis. The slide is divided into sections, each containing specific information and visual aids to illustrate key concepts.

*   **Title and Introduction**
    *   The title "Signal Reference Voltage - Opamp" is prominently displayed at the top of the slide.
    *   A brief introduction explains that single-ended signals are not always ground referenced, providing examples and considerations for signal referencing.
*   **Equations and Formulas**
    *   The slide presents several equations and formulas related to signal processing and op-amp circuits:
        *   "New Input": \(V_{in} - V_{ref}\)
        *   Gain is still \(-R_f/R_i\)
        *   Output = Gain \(\times\) New Input + Offset \(= (-2 V/V) \times (V_{in} - 2V) + 2V\)
    *   These equations are handwritten in blue ink, suggesting they were added during the lecture for emphasis or illustration.
*   **Circuit Diagram**
    *   A circuit diagram is shown in the upper right corner of the slide, depicting an op-amp configuration with resistors and input/output voltages labeled.
    *   The diagram illustrates how the op-amp is used to process the input signal with respect to a reference voltage.
*   **Graph**
    *   A graph is presented below the circuit diagram, displaying three sinusoidal waveforms over time.
    *   The graph has a title and axis labels, but the exact details are not specified; however, it appears to show the relationship between input and output signals in terms of voltage and time.
*   **Additional Notes and URL**
    *   A URL is provided at the bottom of the slide: https://everycircuit.com/circuit/4658452617756672
    *   This URL likely links to a simulation or interactive model of the circuit discussed in the slide.

In summary, the slide provides a comprehensive overview of signal reference voltage in the context of op-amp circuits, including key concepts, equations, and visual aids such as a circuit diagram and graph. The content is detailed and appears to be designed for educational purposes, likely as part of a lecture on electronics or circuit analysis.

### Slide 26

The image presents a comprehensive overview of signal reference voltage, featuring three distinct circuit diagrams and accompanying equations. The title "Signal Reference Voltage" is prominently displayed in bold black text at the top left corner.

**Circuit Diagrams:**

*   **Inverting Circuit:** The first circuit diagram illustrates an inverting configuration, comprising:
    *   Input voltage (Vin)
    *   Input resistor (Ri)
    *   Feedback resistor (Rf)
    *   Reference voltage (Vref)
    *   Output voltage (Vout)
*   **Non-Inverting Circuit:** The second circuit diagram depicts a non-inverting configuration, consisting of:
    *   Input voltage (Vin)
    *   Input resistor (Ri)
    *   Feedback resistor (Rf)
    *   Reference voltage (Vref)
    *   Output voltage (Vout)
*   **Difference Circuit:** The third circuit diagram shows a difference configuration, featuring:
    *   Two input voltages (Vin+ and Vin-)
    *   Two input resistors (Ri)
    *   Two feedback resistors (Rf)
    *   Reference voltage (Vref)
    *   Output voltage (Vout)

**Equations:**

*   **Inverting Circuit:** Vout = Gain × New Input + offset = -Rf/Ri(Vin - Vref) + Vref
*   **Non-Inverting Circuit:** Vout = Gain × New Input + offset = (1 + Rf/Ri)(Vin - Vref) + Vref
*   **Difference Circuit:** Vout = Gain × New Input + offset
    *   Gain = Rf/Ri
    *   "Old" Input = Vin+ - Vin-
    *   New "Input" = (Vin+ - Vref) - (Vin- - Vref) = Vin+ - Vin-

**Additional Notes:**

*   A question is posed in blue handwriting: "Could you use a difference amp w/ offset to create a level-shifter circuit?"
*   A possible solution is provided in red handwriting: Vout = Vin + Vref
*   A condition is specified: Set A=1 (Rf=Ri), Vin- = 0V
*   A link to an online circuit simulator is provided: https://everycircuit.com/circuit/4659204841013248

**Footer:**

*   The number "26" is displayed in small black text at the bottom center of the image.
*   A logo featuring a yellow shield with a red and black design is situated in the bottom-right corner.

### Slide 27

The slide is titled "Capacitive Coupling - Premise" and contains the following content:

**Text:**

* Change the DC offset of a signal with a simple method
* We pass an AC signal $v_{AC}(t)$ between circuits with different DC voltages using a coupling capacitor
* Capacitor blocks DC (looks like open circuit)
* Capacitor lets AC through (looks like short circuit)

**Circuit Diagram:**

* The circuit consists of:
	+ A coupling capacitor labeled "C"
	+ Two voltage sources: $V_{DD}$, $V_{DC1}$, and $v_{ac}(t)$
	+ Two resistors: $R_{G1}$ and $R_{G2}$
	+ The capacitor is connected between $v_{ac}(t)$ and $V_{DC2} + v_{ac}(t)$
	+ $R_{G1}$ is connected between $V_{DD}$ and $V_{DC2} + v_{ac}(t)$
	+ $R_{G2}$ is connected between $V_{DC2} + v_{ac}(t)$ and ground
* The coupling capacitor is labeled with an arrow pointing to it, and the text "coupling capacitor" is written above it

**Graph:**

* The graph shows two sinusoidal waveforms:
	+ One waveform has a DC offset of $V_{DC2}$ (blue dashed line) and oscillates around it (green curve)
	+ The other waveform has a DC offset of $V_{DC1}$ (red line) and oscillates around it (green curve)
* The x-axis is labeled "t" and the y-axis is labeled "V"
* The graph shows the AC signal $v_{AC}(t)$ being passed through the coupling capacitor, with the DC offset changed from $V_{DC1}$ to $V_{DC2}$

**Additional Elements:**

* A URL is provided at the bottom left of the slide: https://everycircuit.com/circuit/658744784846848480
* A slide number is displayed at the bottom center of the slide: 27
* A logo is present in the bottom right corner of the slide, but its details are not specified.

### Slide 28

The slide is titled "Capacitive Coupling - DC Equivalent Circuit" and contains the following content:

**Bullet Points:**

* Consider DC only:
* $v_{\mathrm{AC}}(t)=0$, and $0 \mathrm{~V}$ source looks like short circuit
* Capacitor looks like open circuit

**Equations:**

* $\mathrm{V}_{\mathrm{DC} 2}=V_{\mathrm{DD}} \frac{R_{\mathrm{G} 2}}{R_{\mathrm{G} 1}+R_{\mathrm{G} 2}}$

**Circuit Diagrams:**

There are two circuit diagrams on the slide. The left diagram shows a circuit with the following components:

* A capacitor $C$ 
* A voltage source $v_{\mathrm{ac}}(t)$ 
* A voltage source $\mathrm{V}_{\mathrm{DC} 1}$
* A voltage source $\mathrm{V}_{\mathrm{DC} 2}+v_{\mathrm{ac}}(t)$
* A voltage source $\mathrm{V}_{\mathrm{DD}}$
* Resistors $R_{\mathrm{G} 1}$ and $R_{\mathrm{G} 2}$

The right diagram shows a simplified circuit with the following components:

* A voltage source $\mathrm{V}_{\mathrm{DC} 1}$
* A voltage source $\mathrm{V}_{\mathrm{DD}}$
* Resistors $R_{\mathrm{G} 1}$ and $R_{\mathrm{G} 2}$

**Arrows and Labels:**

* An arrow points from the left circuit diagram to the right circuit diagram, labeled "DC only".

**Other Content:**

* The number "28" is displayed at the bottom of the slide.
* A logo is present in the bottom-right corner of the slide, but its details are not specified.

### Slide 29

The slide presents information on capacitive coupling and AC equivalent circuits. The main points are:

* **Title**: Capacitive Coupling - AC Equivalent Circuit

**Key Points:**

* Consider AC only:
	+ $V_{DC1} = 0$, $V_{DD} = 0$, and 0 V source looks like short circuit
	+ $V_{DD}$ looks like short to ground $\rightarrow R_{G1}$ and $R_{G2}$ appear in parallel

**Circuit Diagrams:**

There are three circuit diagrams shown:

1. The initial circuit diagram:
	* The circuit consists of:
		- A voltage source $v_{ac}(t)$
		- A capacitor $C$
		- Two resistors $R_{G1}$ and $R_{G2}$
		- Two DC voltage sources $V_{DC1}$ and $V_{DC2}$
	* The voltage source $v_{ac}(t)$ is in series with $V_{DC1}$
	* The capacitor $C$ is in series with $R_{G1}$ and $R_{G2}$ is connected to ground
2. The AC equivalent circuit:
	* The circuit consists of:
		- A voltage source $v_{ac1}(t)$
		- A capacitor impedance $Z_C$
		- Two resistors $R_{G1}$ and $R_{G2}$
	* The voltage source $v_{ac1}(t)$ is in series with $Z_C$ and $R_{G2}$ is connected to ground
3. The small-signal model:
	* The circuit consists of:
		- A voltage source $v_{ac1}(t)$
		- A capacitor impedance $Z_C$
		- A resistor $R_{G1}||R_{G2}$
	* The voltage source $v_{ac1}(t)$ is in series with $Z_C$ and $R_{G1}||R_{G2}$

**Resulting Circuit:**
The resulting circuit is called a small-signal model.

**Additional Information:**

* The slide number is 29.
* A logo is present in the bottom-right corner.

### Slide 30

The image presents a comprehensive overview of noise in single-ended signals, featuring a detailed explanation and accompanying diagrams.

**Title:** "Noise in Single-Ended Signals"

**Bullet Points:**

* Single-ended signal (ground-referenced), $V_s$
* Picks up noise, $V_n$
* Receiver amplifies signal (wanted) and noise (unwanted)

**Equations:**

* $V_{in} = V_s + V_n$
* $V_{out} = A \cdot V_{in} = A(V_s + V_n) = AV_s + AV_n$

**Diagram 1: Circuit Representation**

* A simple circuit diagram illustrating the concept of noise in single-ended signals
* The diagram shows a signal source ($V_s$) connected to a receiver through a wire, with noise ($V_n$) coupled into the signal path

**Diagram 2: Signal and Noise Waveforms**

* A set of four waveform diagrams displaying:
	+ $V_s$ (black): a clean sinusoidal signal
	+ $V_n$ (red): a noisy signal
	+ $V_{in}$ (blue): the input signal with noise
	+ $V_{out}$ (green): the output signal with amplified noise

**Handwritten Notes:**

* A handwritten note in the bottom-right corner reads: "Can't 'reject' the noise. Filtering could help, maybe not."

**Additional Elements:**

* A logo in the bottom-right corner features a yellow and red shield with a black design
* The background of the slide is white, with a purple and black border at the top

### Slide 31

The slide presents information on differential signalling, a method of transmitting signals. 

**Title:** 
Differential Signalling

**Bullet Points:**
* Instead of sending a signal as a single time-varying voltage (V<sub>s</sub>), you can split it into a positive and negative part:

**Diagram 1:**
The first diagram shows a sinusoidal signal V<sub>s</sub> being split into two signals: +V<sub>s</sub>/2 and -V<sub>s</sub>/2. 
The left side shows a single sinusoidal signal V<sub>s</sub> with a dotted line representing its average voltage. 
On the right side, two sinusoidal signals are shown in red and blue, with the same frequency and amplitude but opposite phases. 
The two signals have arrows indicating their peak-to-peak amplitudes.

* Subtract signals to restore V<sub>s</sub>
* Signal common mode voltage doesn't matter (with low A<sub>CM</sub>...)
* Other benefit - less signal voltage swing

**Diagram 2:**
The second diagram shows a differential amplifier with two inputs: V<sub>CM</sub> + V<sub>s</sub>/2 and V<sub>CM</sub> - V<sub>s</sub>/2, where V<sub>CM</sub> is the common-mode voltage. 
The output of the amplifier is A(V<sub>+</sub> - V<sub>-</sub>) = A[(V<sub>cm</sub> + 1/2 V<sub>s</sub>) - (V<sub>CM</sub> - 1/2 V<sub>s</sub>)] = A * V<sub>s</sub>. 

**Number at the Bottom:** 
The number 31 is shown at the bottom center of the slide. 

**Logo:**
A logo is present in the bottom-right corner of the slide, featuring a yellow shield with a red design.

### Slide 32

The slide is titled "Noise in Differential Signals" and contains the following information:

**Bullet Points:**

* If + and – signal conductors are close together, then they mostly get the same noise
* Noise is common mode
* Receiver cancels common mode

**Circuit Diagram:**

The circuit diagram shows a differential signal source with the following components:

* A differential signal source with $V_s/2$ and $-V_s/2$ inputs
* A common-mode voltage source $V_{CM}$
* A noise voltage source $V_n$
* A differential amplifier or receiver

The diagram shows the following labels and annotations:

* $V_+$ and $V_-$ are the voltages at the positive and negative inputs of the receiver, respectively
* $V_{CM}$ is the common-mode voltage
* $V_n$ is the noise voltage
* $V_s/2$ and $-V_s/2$ are the differential signal source voltages

**Equations:**

The following equations are written on the slide:

* $V_+ = V_{CM} + V_n + \frac{V_s}{2}$
* $V_- = V_{CM} + V_n - \frac{V_s}{2}$
* $V_+ - V_- = V_s$

**Cable Illustration:**

There is an illustration of a cable with multiple colored wires, including blue, orange, green, brown, and white.

**Additional Annotations:**

* "DC offset" is written in green handwriting next to the $V_{CM}$ voltage source
* "Differential Signal Source" is written in green handwriting above the differential signal source
* The number "32" is written in small black text at the bottom of the slide.

### Slide 33

The slide, titled "Common and Differential Modes Defined," presents a comprehensive overview of the concepts of common and differential modes in electrical engineering. The slide is divided into several sections, each providing detailed information on the topic.

**Graphs and Diagrams:**

*   Two graphs are displayed on the slide:
    *   The left graph shows a sinusoidal waveform with a DC offset, representing the total common mode signal. The waveform has a peak amplitude of approximately 1 V and a DC offset of 1 V. A horizontal blue line is plotted at y=2, and a red, wavy line is plotted around the x-axis.
    *   The right graph shows two waveforms, one in blue and the other in red, representing the differential signal. The waveforms have a peak amplitude of approximately 2 V and are out of phase with each other.
*   A circuit diagram is also provided, illustrating the definition of common and differential modes. The circuit consists of a voltage source, a differential amplifier, and two resistors. The voltage source is represented by $V_{CM} + v_{cm}$ and $v_{diff}/2$. The differential amplifier has two inputs, $V_{in+}$ and $V_{in-}$, and the output is represented by $v_{diff}$.

**Equations and Formulas:**

*   The slide provides several equations and formulas that define the common and differential modes:
    *   Total common mode signal: $v_{CM} = V_{CM} + v_{cm}$
    *   DC common mode (DC offset): $V_{CM} = 2V$
    *   AC common mode (noise): $v_{cm} = 50 \cos(2\pi \times 17.3 \times t) mV$
    *   Differential signal: $v_{diff} = \cos(2\pi \times 1 \times t) V$
    *   Relationship between common and differential modes: $v_{CM} = \frac{V_{+} + V_{-}}{2}$ and $v_{diff} = V_{+} - V_{-}$
    *   Relationship between $V_{+}$, $V_{-}$, $v_{CM}$, and $v_{diff}$: $V_{+} = v_{CM} + \frac{v_{diff}}{2}$ and $V_{-} = v_{CM} - \frac{v_{diff}}{2}$

**Definitions:**

*   The slide provides definitions for the following terms:
    *   Common mode: The common mode signal is the average of the two input signals, $V_{+}$ and $V_{-}$.
    *   Differential mode: The differential mode signal is the difference between the two input signals, $V_{+}$ and $V_{-}$.

**Summary:**

In summary, the slide provides a detailed explanation of the concepts of common and differential modes in electrical engineering. The graphs and diagrams illustrate the definitions of these modes, while the equations and formulas provide a mathematical representation of the relationships between the common and differential modes. The definitions section provides a clear understanding of the terminology used in the context of common and differential modes. Overall, the slide presents a comprehensive overview of the topic, making it a valuable resource for students and professionals in the field of electrical engineering.

### Slide 34

The image presents a detailed lecture slide on "Common and Differential Mode Gains" in the context of electronics, specifically focusing on operational amplifiers (op-amps) and their gain characteristics.

**Title and Layout**

* The title, "Common and Differential Mode Gains," is prominently displayed at the top of the slide in bold black text.
* The slide features a white background with a purple and black bar at the top, providing a clean and visually appealing layout.

**Circuit Diagram**

* A circuit diagram is situated on the left side of the slide, illustrating a differential amplifier configuration.
* The diagram includes:
	+ A voltage source labeled "VCM" (common-mode voltage) connected to the inverting and non-inverting inputs of the op-amp through resistors.
	+ A differential voltage source labeled "v_diff" connected between the inverting and non-inverting inputs.
	+ The op-amp symbol with its output labeled "Vout".
	+ Various labels and annotations, such as "v_CM (noise)", "V_in+", "V_in-", and "v_diff/2".

**Mathematical Equations**

* A series of mathematical equations are presented on the right side of the slide, describing the relationship between the input and output voltages of the differential amplifier.
* The equations are:
	+ Vout = A+ \* Vin+ - A- \* Vin-
	+ = A+ \* (v_diff/2 + VCM) - A- \* (-v_diff/2 + VCM)
	+ = ((A+ + A-)/2) \* v_diff + ((A+ - A-)/2) \* VCM
	+ = A_diff \* v_diff + A_CM \* VCM
* These equations demonstrate how the output voltage is a function of both the differential and common-mode input voltages.

**Additional Text and Handwritten Notes**

* The slide includes additional text and handwritten notes, providing further clarification and insights:
	+ "The gains can be expressed as a function of Vin+ and Vin-".
	+ "Or as a function of v_diff and VCM. They're mathematically equivalent."
	+ Handwritten notes at the bottom of the slide: "OR: A+ = A_diff + A_CM/2, A- = A_diff - A_CM/2".

**Footer**

* The slide features a small logo or crest in the bottom-right corner, which appears to be a university or institutional emblem.
* The number "34" is displayed at the bottom center of the slide, likely indicating the slide number.

### Slide 35

The slide, titled "Differential Outputs," presents a comprehensive overview of differential output configurations. 

**Title and URL**
The title, "Differential Outputs," is prominently displayed in bold black text at the top left of the slide. Adjacent to the title is a URL: https://www.ti.com/lit/an/sloa099/sloa099.pdf.

**Circuit Diagrams**
The slide features two circuit diagrams:

1. **Differential Input and Differential Output (Diff in, diff out)**
   - The left diagram illustrates a differential input and differential output configuration.
   - It consists of:
     - Two input voltage sources: $V_{in+}$ and $V_{in-}$.
     - Two input resistors: $R_g$ (one for each input).
     - A feedback resistor: $R_f$.
     - An operational amplifier (op-amp) with a triangle symbol.
     - Output voltages: $V_{out+}$ and $V_{out-}$.

2. **Single-Ended Input and Differential Output (Single in, diff out)**
   - The right diagram shows a single-ended input and differential output configuration.
   - It comprises:
     - A single input voltage source: $V_{in}$.
     - Two input resistors: $R_g$.
     - A feedback resistor: $R_f$.
     - An operational amplifier (op-amp) with a triangle symbol.
     - Output voltages: $V_{out-}$ and $V_{out+}$.

**Additional Elements**
- In the top-right corner, there is a small diagram of an MCP6D11 component with the text "Output off set → $V_{OCM}$" and an arrow pointing to it.
- Handwritten notes below the diagrams read: "Diff in, diff out" and "Single in, diff out."
- A logo is present in the bottom-right corner, but its details are not specified.
- The slide number "35" is displayed at the bottom center.

### Slide 36

The image presents a detailed lecture slide on calculating differential and common-mode gain, featuring a comprehensive overview of the topic.

**Title**
The title, "Calculating Differential and Common-Mode Gain," is prominently displayed in bold black text at the top of the slide.

**Main Content**
The main content is divided into two sections:

**Left Section**

* A bullet point lists the steps to determine $A_{diff} = V_{out}/V_{diff}$ with $V_{CM} = 0$:
	+ $V_{out} = A_+ V_{in+} - A_- V_{in-}$ (Derive $V_{out}$, rearrange)
	+ CLNF: Find $V_+, Eq'n$ for $V_-, set V_- = V_+$
* A circuit diagram is provided, illustrating the components and connections:
	+ The circuit consists of:
		- $V_{in-}$ and $V_{in+}$ as input voltages
		- A $1 k\Omega$ resistor connected to $V_{in-}$
		- A $10.1 k\Omega$ resistor connected to $V_{out}$
		- A $1 k\Omega$ resistor connected to $V_{in+}$
		- A $10 k\Omega$ resistor connected to ground
	+ The circuit also includes a green waveform symbol representing $V_{diff}$
* Four numbered equations are written in blue, red, and green ink:
	1. $V_+ = V_{in+} \cdot \frac{10}{10+1} = \frac{10}{11} V_{int}$
	2. $V_{in-} - V_- = \frac{V_- - V_{out}}{10.1}$
	3. $V_- = V_+$
	4. $V_{out} = \frac{111}{11} \cdot V_{in+} - \frac{101}{10} \cdot V_{in-}$

**Right Section**

* A vertical line separates the left section from the right section, which contains additional equations and notes:
	+ $con \: use \: (4) \: with \: V_{int} = V_{cm} + \frac{V_{diff}}{2}$ and $V_{int} = V_{cm} - \frac{V_{diff}}{2}$
	+ $\Rightarrow A_{diff} = \frac{V_{out}}{V_{diff}} = 10.0955 [V/V]$
	+ $Rearrange$
	+ $A_{diff} = \frac{A_+ + A_-}{2}$

**Additional Elements**

* A URL is provided at the bottom-left corner: https://everycircuit.com/circuit/6105864674738176
* A small logo featuring a shield with a red and yellow design is located at the bottom-right corner.

### Slide 37

The image presents a detailed example of a common-mode gain calculation for a differential amplifier circuit.

*   The title of the slide is "Example Continued" and it appears to be part of a lecture on differential amplifiers.
*   The main objective is to determine the common-mode gain (ACM) of the amplifier, defined as ACM = Vout / VCM with Vdiff = 0.

**Equations:**

*   Vout = (11/11) * Vin+ - (10/10) * Vin-
*   ACM = A+ - A- = (11/11) - (10/10) = -9.0909 [mV/V]

**Circuit Diagram:**

*   The circuit consists of:
    *   A differential amplifier with two input voltages, Vin+ and Vin-.
    *   Two resistors, 1 kΩ and 10 kΩ, connected in series between Vin+ and the non-inverting input of the op-amp.
    *   A 10 kΩ resistor connected between the inverting input of the op-amp and the output Vout.
    *   A 1 kΩ resistor connected between Vin- and the inverting input of the op-amp.

**Handwritten Notes:**

*   The handwritten notes appear to be working through the calculation of the common-mode gain.
*   The notes show the derivation of the output voltage equation and the calculation of the common-mode gain.

**Other Elements:**

*   The slide number "37" is displayed at the bottom center of the image.
*   A logo is present in the bottom-right corner of the image, but its details are not clear.

In summary, the image provides a detailed example of how to calculate the common-mode gain of a differential amplifier circuit, including the relevant equations and a circuit diagram.

### Slide 38

The image displays a lecture slide titled "Common-Mode Rejection Ratio." 

**Title and Content**

* The title is in bold black text at the top of the slide.
* The slide contains the following bullet points:
  * CMRR = How well amplifier eliminates unwanted common-mode noise compared to the wanted differential gain:
  * Usually in dB
  * Rejection Ratio = (gain you want) / (gain you don’t want)
  * Common-mode gain arises from imbalances in the circuit
    * Design weaknesses
    * Manufacturing tolerances

**Equations and Formulas**

* The slide includes the following equations and formulas:
  * CMRR = A_diff / A_CM
  * A_dB = 20 log10 (|A|)
  * CMRR_dB = |A_diff| / |A_CM| dB = A_diff,dB - A_CM,dB

**Example and Calculations**

* The slide provides an example with the following calculations:
  * A_diff = 10.0955 [V/V] = 20.083 dB
  * A_CM = -9.09091 [mV/V] = -40.828 dB = -0.00909091 [V/V]
  * CMRR = |A_diff| / |A_CM| = 1.1105K [V/V] / [V/V]
  * CMRR_dB = |A_diff| / |A_CM| dB = A_diff,dB - A_CM,dB = 60.911 dB ≈ 61 dB

**Additional Information**

* The slide number "38" is displayed at the bottom center of the slide.
* A logo is present in the bottom-right corner of the slide. 

Overall, the slide provides a detailed explanation of the Common-Mode Rejection Ratio (CMRR), its definition, and its calculation, along with an example and relevant equations and formulas.

### Slide 39

The slide, titled "Application to Input Resistance," presents a comprehensive overview of the input resistance in the context of a difference amplifier. The content is organized into two main bullet points, accompanied by two circuit diagrams and several equations.

**Main Points:**

* $v_{\mathrm{CM}}$ and $v_{\mathrm{diff}}$ experience different input resistances
* Calculate the common- and differential-mode input resistance of a difference amplifier

**Circuit Diagrams:**

The slide features two circuit diagrams:

1. **Common-Mode Input Resistance Circuit:**
	* The circuit consists of:
		+ $R_1$, $R_2$, $R_3$, and $R_4$ resistors
		+ An op-amp with $V_{\mathrm{out}}$ output
		+ A voltage source $v_{\mathrm{CM}}$ with a positive terminal connected to the inverting input of the op-amp and a negative terminal connected to ground
		+ A current $i_{\mathrm{CM}}$ flowing through $R_3$ and $R_1$
	* The common-mode input resistance $R_{\mathrm{CM}}$ is given by:
		+ $R_{\mathrm{CM}} = v_{\mathrm{CM}}/i_{\mathrm{CM}}$
		+ $R_{\mathrm{CM}} = \frac{R_3 + R_4}{1 + R_3/R_4} = R_3 + R_4 \frac{R_4}{R_3}$
2. **Differential-Mode Input Resistance Circuit:**
	* The circuit consists of:
		+ $R_1$, $R_2$, $R_3$, and $R_4$ resistors
		+ An op-amp with $V_{\mathrm{out}}$ output
		+ A voltage source $v_{\mathrm{diff}}$ with a positive terminal connected to the non-inverting input of the op-amp and a negative terminal connected to ground
		+ A current $i_{\mathrm{diff}}$ flowing through $R_1$ and $R_3$
	* The differential-mode input resistance $R_{\mathrm{diff}}$ is given by:
		+ $R_{\mathrm{diff}} = v_{\mathrm{diff}}/i_{\mathrm{diff}}$
		+ $R_{\mathrm{diff}} = R_1 + R_3$

**Additional Circuit:**

A third circuit diagram shows a difference amplifier with:

* $R_1$, $R_2$, $R_3$, and $R_4$ resistors
* $V_{\mathrm{in}-}$ and $V_{\mathrm{in+}}$ inputs
* $V_{\mathrm{out}}$ output

The slide provides a detailed analysis of the input resistance in the context of a difference amplifier, highlighting the differences between common-mode and differential-mode input resistances.

### Slide 40

The image presents a slide from a presentation on instrumentation amplifiers, featuring a title and a background image of a circuit board.

*   The title is prominently displayed in large black text at the bottom left of the slide.
    *   **Title:** "2.4 - Instrumentation Amplifiers"
*   A background image of a circuit board is visible at the top of the slide.
    *   **Image Description:** The circuit board features various components, including:
        *   Teal-colored lines and pathways
        *   Small silver dots and circles
        *   A purple and black bar running across the top
    *   **Image Size:** The image spans the entire width of the slide, with a height of approximately one-quarter of the slide's total height.
*   A logo is located in the bottom-right corner of the slide.
    *   **Logo Description:** The logo consists of a yellow shield with a red dragon and a black and white chevron.
    *   **Logo Size:** The logo is relatively small compared to the rest of the slide.
*   A page number is displayed at the bottom center of the slide.
    *   **Page Number:** 40

In summary, the image shows a slide from a presentation on instrumentation amplifiers, featuring a title, a background image of a circuit board, a logo, and a page number. The title is prominently displayed, while the background image and logo provide additional visual interest. The page number indicates that this is the 40th slide in the presentation.

### Slide 41

The slide is titled "Instrumentation Amplifiers – Motivation" and features a white background with a purple and black border at the top.

**Bullet Points:**

* Some sensors cannot provide reasonable current
	+ Thermocouple produces ~40 μV/°C @ R<sub>out</sub> = ~10 kΩ
	+ Pressure sensor produces ~10 mV @ R<sub>out</sub> = ~100 kΩ

**Handwritten Notes:**

* Problem 1) Amplifiers may require input current (not op-amp, but surrounding circuit)
	→ Want amp config. that doesn't load at input :: R<sub>in</sub> → ∞, O.C., I<sub>in</sub> → 0
* Problem 2) Amp resistor mismatch leads to high A<sub>CM</sub> (poor CMRR)
	→ Want very well-matched R<sub>s</sub>

**Circuit Diagrams:**

Two circuit diagrams are shown side-by-side, each with the following components:

* A voltage source (V<sub>in+</sub> and V<sub>in-</sub>)
* Two resistors (R<sub>i</sub> and R<sub>f</sub>)
* An op-amp
* A ground connection

The left circuit diagram has the following labels:

* I<sub>in</sub> ≠ 0 (with a red arrow pointing to the input)
* V<sub>in</sub>
* V<sub>out</sub>

The right circuit diagram has the same components and labels, but with the input voltage sources labeled as V<sub>in+</sub> and V<sub>in-</sub>.

**Logo:**

A logo is located in the bottom-right corner of the slide, featuring a yellow shield with a black and red design.

Overall, the slide appears to be discussing the motivation behind using instrumentation amplifiers, specifically the need to address issues with sensor output currents and amplifier input loading. The handwritten notes highlight two problems: the need for an amplifier configuration that does not load the input, and the importance of well-matched resistors to achieve high common-mode rejection ratio (CMRR).

### Slide 42

The image presents a slide from a presentation on electronics, specifically focusing on the topic of "Fix Input Resistance." The slide features a white background with a purple and black bar at the top.

**Title and Bullet Point**

* The title "Fix Input Resistance" is displayed in bold black text at the top left of the slide.
* A bullet point below the title reads: "Start by using a stage that does not require input current (very high Rin):"

**Circuit Diagrams**

* Two circuit diagrams are presented side by side, each enclosed in a blue dotted rectangle.
* The top diagram shows:
	+ A voltage source labeled "Vin" connected to the positive terminal of an operational amplifier (op-amp).
	+ The negative terminal of the op-amp is connected to ground through a resistor labeled "R1."
	+ The output of the op-amp is connected to the negative terminal through a resistor labeled "R2."
* The bottom diagram is identical to the top one, but with the input voltage labeled "Vin+" and the output taken from the op-amp.

**Equations and Text**

* To the right of the circuit diagrams, handwritten notes in blue ink state:
	+ "R1 and R2 can be very well-matched using resistor arrays or creating the circuit on-chip."
* Below this, handwritten notes in red ink read:
	+ "Solves the input current problem."
* At the bottom left of the slide, an equation is written in blue ink:
	+ A1 = 1 + R2/R1

**Additional Elements**

* In the bottom-right corner of the slide, a small logo featuring a yellow shield with a red dragon and a black and white chevron is visible.
* The number "42" is centered at the bottom of the slide.

### Slide 43

The slide is titled "Apply Gain to Differential Signal" and contains the following content:

**Bullet Point:**
* Send that to a difference amplifier

**Circuit Diagram:**
The slide features a circuit diagram with two op-amps, resistors, and input and output voltage labels. The diagram is divided into two sections: 
- The left section shows an op-amp with $V_{in-}$ and $V_{in+}$ inputs, and resistors $R_1$ and $R_2$. 
- The right section shows another op-amp with $V_{out}$ output and resistors $R_3$ and $R_4$. 
The two sections are outlined with dotted blue and green lines, respectively.

**Equations:**
The following equations are written on the slide:

- $A_1 = (1 + \frac{R_2}{R_1})$
- $A_2 = \frac{R_4}{R_3}$
- $= A_1 A_2 = (1+\frac{R_2}{R_1})(\frac{R_4}{R_3})$

**Handwritten Text:**
The slide includes handwritten text in black, blue, and red ink:

- We can put the whole circuit on-chip. $R_1$ through $R_4$ very well-matched.
- Result is a fixed gain Instrumentation Amplifier (IA).
- To make user-configurable gain, leave $R_1$ off-chip.

**Other Elements:**
The slide features a logo in the bottom-right corner, which appears to be a shield with a red and yellow design. The slide number "43" is displayed in the center at the bottom.

### Slide 44

The image presents a detailed slide on improving Common-Mode Rejection Ratio (CMRR) in electronic circuits, specifically focusing on operational amplifier (op-amp) configurations. The title "Improve CMRR" is prominently displayed at the top.

**Key Points:**

* **Objective:** The primary goal is to enhance CMRR by adjusting resistor values.
* **Approach:** Keep all resistors fixed except for one user-specified gain resistor, $R_G = 2R_1$.

**Circuit Diagram:**

The slide features a circuit diagram with two op-amps, various resistors ($R_1$, $R_2$, $R_3$, $R_4$, and $R_G$), and input voltages ($V_{in+}$ and $V_{in-}$). The diagram is annotated with notes and equations, including:

* $R_G = 2R_1$
* $V_{in-} - V_{in+}$ (differential input)
* $\frac{V_{in+} + V_{in-}}{2}$ (common-mode input)

**Handwritten Notes:**

Several handwritten notes are scattered throughout the slide:

* "Now only one resistor sets the gain for both $V_{in+}$ and $V_{in-}$. $\therefore A_{CM}$ should stay very low."
* "$V_{in-}$ acts like virtual ground."
* "$R_G = 2R_1$"

**Equations and Formulas:**

No specific equations or formulas are explicitly written on the slide, but the relationship between $R_G$ and $R_1$ is highlighted.

**Visual Elements:**

The circuit diagram is the primary visual element, showcasing the op-amp configuration and resistor network. The diagram is divided into two sections, with the left side labeled "CLMF" and the right side showing the output voltage ($V_{out}$).

**Overall:**

The slide provides a detailed explanation of how to improve CMRR in op-amp circuits by adjusting the gain resistor $R_G$. The circuit diagram and handwritten notes offer a clear understanding of the approach and its implications on common-mode rejection.

### Slide 45

The slide is titled **Called an Instrumentation Amplifier** and contains the following information:

**Bullet Points:**
* Package it all on an IC so that the resistors and transistors are low power and very well matched
* Convenient, high-performance analog interface IC

**Circuit Diagrams:**

The slide features two circuit diagrams. 

1. The left diagram shows a more detailed circuitry of an instrumentation amplifier, which consists of:
	* Two input voltages labeled as $V_{in-}$ and $V_{in+}$
	* Four resistors labeled as $R_2$, $R_3$, $R_4$, and $R_G$
	* Two operational amplifiers
	* The output voltage is labeled as $V_{out}$
2. The right diagram shows a simplified representation of an instrumentation amplifier, which consists of:
	* A single block representing the instrumentation amplifier
	* Two input voltages labeled as $V_{in-}$ and $V_{in+}$
	* A resistor labeled as $R_G$
	* A reference voltage labeled as $V_{REF}$
	* The output voltage is labeled as $V_{out}$

**Equation/Formula:** 
There are no equations or formulas on this slide.

**Other Content:**
The slide has a white background with a black and purple bar at the top. The number "45" is centered at the bottom of the slide. In the bottom-right corner, there is a logo that appears to be a shield with a red and yellow design.

### Slide 46

The image presents a slide from a presentation on the topic of "Many Different Types of IAs" (Instrumentation Amplifiers). The slide features three main bullet points and three circuit diagrams.

* **Many Different Types of IAs**
	+ The title of the slide is in large black text at the top.
* **Bullet Points:**
	+ Different architectures
	+ Different means of setting gain
	+ Do what the datasheet says!
* **Circuit Diagrams:**
	+ Three black and white circuit diagrams are displayed on the right side of the slide, showcasing different types of instrumentation amplifiers. 
	+ The top-left diagram shows a circuit with various components, including resistors, capacitors, and operational amplifiers.
	+ The top-right diagram depicts a more complex circuit with multiple operational amplifiers, resistors, and capacitors.
	+ The bottom-right diagram illustrates another circuit configuration with operational amplifiers, resistors, and capacitors.
* **Link and Logo:**
	+ A link to a PDF document is provided at the bottom of the slide: https://www.analog.com/media/en/training-seminars/design-handbooks/designers-guide-instrument-amps-complete.pdf
	+ A logo for the University of Cambridge is displayed in the bottom-right corner of the slide.
* **Slide Number:**
	+ The slide number "46" is centered at the bottom of the slide.

In summary, the slide provides an overview of the diversity of instrumentation amplifier types, highlighting their different architectures, gain-setting methods, and the importance of following datasheet instructions. The accompanying circuit diagrams illustrate various configurations, and a link to a comprehensive guide is provided for further information.

### Slide 47

The slide contains a simple graphic and text. 

* The top of the slide has a thick black line, followed by a gradient purple bar that transitions from light purple on the left to dark purple on the right.
* In the top-left corner, there is bold black text that reads "Thanks!".
* In the bottom-right corner, there is a small shield-shaped logo with a yellow background and a red design. 
* The shield has a black and white chevron in the middle.
* In the center of the slide, there is a simple black line drawing of a right hand with the thumb up. 
* The hand is making a "thumbs-up" gesture, and there is a long straight arrow extending from the tip of the thumb up and to the right.
* There is also a curved arrow extending from the index finger.
* At the bottom center of the slide, there is the number "47" in small black text.
* The background of the slide is white.

