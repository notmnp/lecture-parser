# MTE 220 - Module 6 - Powering Embedded Systems (annotated)

## Study Notes

# Powering Embedded Systems – Exam‑Study Notes  
*Problem‑Solving Focus*  

---  

## Core Formulas & Definitions  

| # | Formula | Symbols | Typical Use |
|---|---------|---------|-------------|
| 1 | $P = V \cdot I$ | $P$ – power (W), $V$ – voltage (V), $I$ – current (A) | Basic power balance for any device |
| 2 | $P_{\text{reg}} = (V_{\text{in}}-V_{\text{out}}) \, I_{\text{out}}$ | $V_{\text{in}}$, $V_{\text{out}}$ – regulator rails, $I_{\text{out}}$ – load | Heat loss in a linear regulator |
| 3 | $\eta_{\text{lin}} = \frac{V_{\text{out}}}{V_{\text{in}}}$ | $\eta$ – efficiency | Ideal linear regulator (ignoring internal drop) |
| 4 | $\eta = \frac{P_{\text{out}}}{P_{\text{in}}}$ | | Efficiency of any converter |
| 5 | $V_{\text{out}} = D \, V_{\text{in}}$ (buck) | $D$ – duty cycle | Output of an ideal buck converter |
| 6 | $V_{\text{out}} = \frac{V_{\text{in}}}{1-D}$ (boost) | | Output of an ideal boost converter |
| 7 | $V_{\text{out}} = \frac{D}{1-D}\,V_{\text{in}}$ (buck‑boost) | | Output of a buck‑boost |
| 8 | $V_{\text{ripple}} \approx \frac{I_{\text{load}}}{f_{\text{sw}}\;C_{\text{out}}}$ | $f_{\text{sw}}$ – switching frequency | Approx ripple on a switching regulator output |
| 9 | $V_{\text{peak}} = V_{\text{ac,rms}}\sqrt{2} - 2 V_{\text{D}}$ | $V_{\text{D}}$ – diode forward drop | Peak DC after a bridge rectifier |
|10 | $V_{\text{dc,avg}} \approx V_{\text{peak}} - \frac{I_{\text{load}}}{f_{\text{rect}}\;C_{\text{L}}}$ | $f_{\text{rect}} = 2f_{\text{ac}}$ for full‑wave | Average DC after a rectifier |
|11 | $V_{\text{rms}} = \frac{V_{\text{dc}}}{\sqrt{2}}$ (square‑wave inverter) | | RMS voltage of a 50 % duty square wave |
|12 | $V_{\text{p}}/V_{\text{s}} = N_{\text{p}}/N_{\text{s}}$ | | Transformer turns ratio |
|13 | $P_{\text{out}} = \eta\,P_{\text{in}}$ | | Power transfer efficiency of a transformer |
|14 | $I_{\text{p}} = \frac{V_{\text{s}}I_{\text{s}}}{V_{\text{p}}}$ (from power balance) | | Primary current from secondary data |
|15 | $C_{\text{out}} = \frac{I_{\text{load}}}{f_{\text{rect}}\,V_{\text{ripple}}}$ | | Capacitor needed for a target ripple |
|16 | $I_{\text{p}} = \frac{N_{\text{s}}}{N_{\text{p}}}\,I_{\text{s}}$ | | Current scaling in a transformer |

> **Unit notes**: 1 Ah = 3600 C, 1 Wh = 3600 J, 1 V = 1 J/C.

---  

## Key Concepts & Intuition  

* **Linear (LDO) regulators**  
  * Drop‑out voltage: $V_{\text{out}} \approx V_{\text{in}}-V_{\text{drop}}$  
  * Heat ≈ $(V_{\text{in}}-V_{\text{out}})I_{\text{out}}$  
  * Efficiency limited by voltage drop; best for low drop & low noise.

* **Switching regulators**  
  * Use a transistor switch (on/off) and energy storage (inductor, capacitor).  
  * Duty cycle $D$ controls $V_{\text{out}}$ (see formulas 5‑7).  
  * Ripple ∝ $I_{\text{load}}/(f_{\text{sw}}C_{\text{out}})$; higher $f_{\text{sw}}$ or larger $C_{\text{out}}$ reduces ripple.  
  * Efficiency ≥ 80 % typical; losses: conduction (MOSFET), switching (core, diode), and quiescent current.

* **DC/AC inverters**  
  * Full‑bridge or H‑bridge switches the DC polarity rapidly.  
  * Square‑wave inverter: $V_{\text{rms}} = V_{\text{dc}}/\sqrt{2}$.  
  * Frequency: $f_{\text{out}} = f_{\text{switch}}/2$ for a full‑bridge; adjust for desired AC frequency.  
  * Filter (LC) turns square wave into sine.

* **Rectifiers**  
  * Bridge (full‑wave) provides two diode drops per cycle.  
  * Ripple is inversely proportional to $C_{\text{L}}$ and rectifier frequency.  
  * Larger $C_{\text{L}}$ → lower ripple but slower transient response.

* **Transformers**  
  * Only work with AC; magnetic coupling transfers energy.  
  * Turns ratio determines voltage and current scaling.  
  * Efficiency ≈ 90–97 %; core size and material influence losses.  

---  

## Problem‑Solving Strategies  

### 1. **Choosing a Regulator Topology**

| Cue | Checklist |
|-----|-----------|
| “Low noise, low current” | Use LDO if $V_{\text{in}}-V_{\text{out}} < V_{\text{drop}}$ + small $I_{\text{out}}$ |
| “High voltage drop or high current” | Switch to buck/boost; calculate $D$ using formulas 5‑7 |
| “Need high efficiency” | Prefer buck/boost; estimate $\eta$ from datasheet |
| “Transient load” | Check surge current rating; include protection (OCP, thermal shutdown) |

**Step‑by‑step**  
1. Write desired $V_{\text{in}}$, $V_{\text{out}}$, $I_{\text{out}}$.  
2. Compute drop for LDO: $\Delta V = V_{\text{in}}-V_{\text{out}}$.  
3. If $\Delta V$ < drop‑out + margin → LDO ok.  
4. Else calculate required $D$ (buck or boost) with formulas 5‑6.  
5. Verify $I_{\text{in}} = I_{\text{out}}/D$ (buck) or $I_{\text{in}} = I_{\text{out}}(1-D)$ (boost).  
6. Check component ratings and thermal limits.  

### 2. **Efficiency and Power Loss in Linear Regulator**

| Cue | Calculation |
|-----|-------------|
| “Given $V_{\text{in}}$ and $V_{\text{out}}$” | $\eta_{\text{lin}} = V_{\text{out}}/V_{\text{in}}$ |
| “Need heat dissipation” | $P_{\text{loss}} = (V_{\text{in}}-V_{\text{out}})I_{\text{out}}$ |
| “Design for a 10 W load, 5 V→3.3 V LDO” | $\eta = 3.3/5 = 0.66$ → $P_{\text{loss}} = (5-3.3)\times10 = 17$ W (unacceptable) |

**Common mistake**: Using $P_{\text{in}} = V_{\text{in}}I_{\text{out}}$ instead of the drop‑based loss formula.

### 3. **Designing a Switching Converter**

| Step | Action |
|------|--------|
| 1 | Pick topology (buck, boost, buck‑boost). |
| 2 | Compute duty cycle ($D$) using formulas 5‑7. |
| 3 | Determine $I_{\text{in}}$ (from $I_{\text{out}}$ and $D$). |
| 4 | Estimate ripple: $V_{\text{ripple}} = I_{\text{out}}/(f_{\text{sw}}C_{\text{out}})$. |
| 5 | Choose $C_{\text{out}}$ to meet ripple spec; verify $I_{\text{out}} \leq I_{\text{max}}$ of inductor. |
| 6 | Confirm efficiency from datasheet; adjust $f_{\text{sw}}$ or component choice if needed. |

**Key cue**: “Efficiency 90 %” → use $\eta = 0.90$ to find required $P_{\text{in}}$.

### 4. **Battery Runtime Estimate**

| Cue | Formula |
|-----|---------|
| “Average load current” | $C_{\text{Ah}} = I_{\text{avg}} \times t_{\text{hrs}}$ |
| “DoD = 80 %” | Required rating $C_{\text{rated}} \geq C_{\text{Ah}}/0.8$ |
| “Temperature drop 5 %/10 °C above 25 °C” | Adjust $C_{\text{Ah}}$ downward by $0.05 \times \Delta T/10$ |

### 5. **Battery Pack Configuration**

| Target | Calculation |
|--------|-------------|
| Pack voltage | $N = V_{\text{pack}}/V_{\text{cell}}$ |
| Pack energy | $E_{\text{total}} = M\,Q_{\text{cell}}\; N\,V_{\text{cell}}$ |
| Parallel cells | $M = E_{\text{desired}}/(N V_{\text{cell}}\,Q_{\text{cell}})$ |
| Current rating | $I_{\text{max}} = I_{\text{cell,max}}\times M$ |

### 6. **Transformer Design**

| Cue | Calculation |
|-----|-------------|
| “Voltage ratio” | $N_{\text{p}}/N_{\text{s}} = V_{\text{p}}/V_{\text{s}}$ |
| “Primary current” | $I_{\text{p}} = \frac{V_{\text{s}}I_{\text{s}}}{V_{\text{p}}}$ |
| “Efficiency 97 %” | Verify $P_{\text{out}} = 0.97\,P_{\text{in}}$ |
| “Core selection” | Match $N_{\text{p}}$, $N_{\text{s}}$, and $f_{\text{ac}}$ to avoid saturation (use core B-H curve). |

**Example**  
Given $V_{\text{in}}=120$ V, $V_{\text{out}}=12$ V, $I_{\text{out}}=1$ A, $\eta=0.97$ → $I_{\text{in}}=103$ mA (shown in slide 23).

### 7. **Rectifier Design**

| Parameter | Formula |
|-----------|---------|
| Peak DC | $V_{\text{peak}} = V_{\text{ac,rms}}\sqrt{2} - 2 V_{\text{D}}$ |
| Ripple | $V_{\text{ripple}} = \frac{I_{\text{load}}}{f_{\text{rect}}\,C_{\text{L}}}$ |
| Output DC | $V_{\text{dc,avg}} \approx V_{\text{peak}} - V_{\text{ripple}}/2$ (for full‑wave) |
| Cap value | $C_{\text{L}} = \frac{I_{\text{load}}}{f_{\text{rect}}\,V_{\text{ripple}}}$ |

*Remember*: Full‑wave rectifier frequency is $f_{\text{rect}} = 2f_{\text{ac}}$.

### 8. **DC/AC Inverter Basics**

| Cue | Calculation |
|-----|-------------|
| Output AC RMS (square wave) | $V_{\text{rms}} = \frac{V_{\text{dc}}}{\sqrt{2}}$ |
| Switching frequency | $f_{\text{switch}} = 2f_{\text{out}}$ (full‑bridge) |
| Filter design | $V_{\text{ripple,AC}} \approx \frac{V_{\text{dc}}}{f_{\text{switch}} C_{\text{filter}}}$ |

**Checklist**  
1. Choose $V_{\text{dc}}$ to meet desired $V_{\text{ac,rms}}$.  
2. Set $f_{\text{switch}}$ to match required AC frequency (e.g., 60 Hz → $f_{\text{switch}}=120$ Hz).  
3. Select $C_{\text{filter}}$ to keep $V_{\text{ripple,AC}}$ below spec.

---  

## Common Pitfalls & Checks  

| Pitfall | Check |
|---------|-------|
| Assuming constant battery voltage | Use discharge curve; account for sag during load peaks |
| Ignoring linear regulator drop | Compute $P_{\text{loss}}$ and verify thermal limit |
| Misreading duty‑cycle formulas | Confirm topology (buck vs boost) before applying formula |
| Overestimating efficiency of switching | Use datasheet or measured data; include quiescent current |
| Using mAh → Wh directly | Convert via $Q_{\text{cell}}$ first ($Wh = \text{mAh}\times V_{\text{cell}}/1000$) |
| Forgetting diode drops in rectifier | Include $2V_{\text{D}}$ for full‑wave |
| Mis‑setting transformer turns ratio | Double‑check $N_{\text{p}}/N_{\text{s}} = V_{\text{p}}/V_{\text{s}}$ |
| Neglecting core losses at high frequency | Verify core material rating for $f_{\text{ac}}$ |
| Under‑estimating ripple for high‑speed switching | Compute $V_{\text{ripple}}$ with actual $f_{\text{sw}}$ and $C_{\text{out}}$ |
| Selecting an LDO for $V_{\text{in}}-V_{\text{out}}\gg V_{\text{drop}}$ | Use switching regulator instead to avoid excessive heat |

---  

## Quick‑Reference Cheat Sheet  

- **Linear Regulator**: $\eta = V_{\text{out}}/V_{\text{in}}$, $P_{\text{loss}}=(V_{\text{in}}-V_{\text{out}})I_{\text{out}}$  
- **Switching Regulator**:  
  - Buck: $V_{\text{out}}=DV_{\text{in}}$  
  - Boost: $V_{\text{out}}=V_{\text{in}}/(1-D)$  
  - Ripple: $V_{\text{ripple}}\approx I_{\text{out}}/(f_{\text{sw}}C_{\text{out}})$  
- **Rectifier**: $V_{\text{peak}}=V_{\text{ac,rms}}\sqrt{2}-2V_{\text{D}}$, $C_{\text{L}}=I_{\text{load}}/(2f_{\text{ac}}\,V_{\text{ripple}})$  
- **Inverter**: $V_{\text{rms}}=V_{\text{dc}}/\sqrt{2}$, $f_{\text{switch}}=2f_{\text{ac}}$  
- **Transformer**: $V_{\text{p}}/V_{\text{s}}=N_{\text{p}}/N_{\text{s}}$, $I_{\text{p}}=V_{\text{s}}I_{\text{s}}/V_{\text{p}}$, $P_{\text{out}}=\eta P_{\text{in}}$  

Use this sheet to spot the key formulas while solving problems; then refer to the detailed strategies for a systematic approach. Good luck on the exam!

---

## Raw Slide Summaries

### Slide 1

The image is a slide from a presentation about embedded systems, specifically Module 6: Powering Embedded Systems. The slide is divided into two sections: the left side contains text, and the right side features an image of a circuit board.

* **Left Section**
	+ **Title**: "Module 6" in large black font at the top
	+ **Subtitle**: "Powering Embedded Systems" in slightly smaller black font below the title
	+ **Course Information**: "MTE 220 - Sensors and Instrumentation" in gray font below the subtitle
	+ **University Logo**: University of Waterloo Faculty of Engineering logo in the bottom-left corner
* **Right Section**
	+ **Circuit Board Image**: A close-up photograph of a teal-colored circuit board with various components and wires visible
	+ **Color Scheme**: The circuit board is predominantly teal, with some silver and black accents

The slide appears to be part of a larger presentation on embedded systems, and the image of the circuit board on the right side adds a visual element to the text on the left side.

### Slide 2

The image is a presentation slide titled "6.1 - Overview" in large, bold black font on the left side.

*   The title is positioned below a banner that spans the top of the image.
    *   The banner features a gradient that transitions from white to purple.
    *   Below the banner, there is an image of a circuit board with various components and wires.
        *   The circuit board is dark green with light blue-green lines and silver dots.
*   The background of the slide is white.
    *   In the bottom center, the number "2" is displayed in small black text.
    *   In the bottom-right corner, there is a logo featuring a shield with a red and yellow design.
        *   The logo appears to be a university or institutional emblem.

### Slide 3

The image presents a slide from a presentation about power supplies, featuring a diagram and accompanying text that explain the concept of power supplies and their functionality.

*   **Title**: The title "Power Supplies" is prominently displayed at the top of the slide in bold black font.
*   **Diagram**:
    *   A flowchart illustrates the process of converting source power into load power.
    *   The flowchart consists of three boxes: "Power Source," "Power Conditioning Circuits," and "Mechatronic System."
    *   Arrows connect these boxes, indicating the flow of power from the source to the system.
    *   The variables Vsource, Isource, fsource, Vsystem, Isystem, and fsystem are labeled along the arrows, representing voltage, current, and frequency at different stages.
*   **Text**:
    *   The first bullet point explains that power supplies convert source power into load power, with a sub-bullet point specifying that this involves converting voltage, current, and frequency as needed.
    *   The second bullet point provides an example of a USB laptop wall charger, listing its specifications:
        *   Vsource = 120 VRMS
        *   fsource = 50-60 Hz
        *   Vsystem = 5 VDC (0 Hz)
        *   Isystem = 3.0 A max
*   **Image**:
    *   A photograph of an Anker Nano II 65W charger is displayed on the right side of the slide.
    *   The charger has a sleek black design with a silver front panel featuring the "ANKER" logo.
*   **Logo**:
    *   A shield-shaped logo is located in the bottom-right corner of the slide, although its details are not clearly visible.

In summary, the slide effectively conveys the concept of power supplies and their role in converting source power into load power, using a clear diagram and concise text. The example of a USB laptop wall charger provides a practical illustration of the topic, while the image of the Anker Nano II 65W charger adds a visual element to the presentation.

### Slide 4

The image presents a slide titled "Power Sources" in bold black text at the top left, accompanied by a list of common power sources and an image of supercapacitors.

**Title and List**

* The title "Power Sources" is displayed prominently.
* A bullet point labeled "Common Power Sources:" is followed by a sublist of eight items:
	+ Batteries: Rechargeable or disposable cells (DC)
	+ Supercapacitors (DC)
	+ Solar Panels (DC)
	+ Fuel Cells: Electrochemical devices (DC)
	+ External Power Supply (DC or AC)
	+ Mains Power (power from the local grid, typically 110 V or 220 V AC)
	+ Energy Harvesting (e.g., RF, piezoelectric, thermal)
	+ Capacitive/Inductive Power Transfer (wireless power transfer)

**Image of Supercapacitors**

* To the right of the list, an image showcases five black cylindrical supercapacitors with white and blue text, arranged in two rows.
* The top row features three supercapacitors with the text "SkelCap supercapacitor" on them.
* The bottom row displays two supercapacitors, one with the text "skeleton" and the other with "SCX5000 skeleton".

**Footer**

* In the bottom-right corner, a logo is visible, although its details are not discernible.
* The number "4" is centered at the bottom of the slide.

**Background and Border**

* The background of the slide is white.
* A purple gradient border runs along the top edge, transitioning from light to dark.

### Slide 5

The image is a slide from a presentation about battery basics. 

*   The top of the image has a banner with a circuit board design, featuring:
    *   A black background
    *   Teal-colored circuitry and silver dots
    *   A purple-to-white gradient at the bottom edge
*   Below the banner, the title "6.2 - Battery Basics" is displayed in large black text.
*   At the bottom center of the image, the number "5" is shown in small black text, likely indicating the slide number.
*   In the bottom-right corner, there is a logo consisting of:
    *   A yellow shield
    *   A red design on the shield
    *   A black and white "V" shape on the shield

The background of the image is white.

### Slide 6

The image presents a slide titled "Battery Basics" that provides an overview of electrochemical cells, including their types, characteristics, and applications.

*   **Electrochemical cell**
    *   Voltage determined by chemistry, Vcell, not size (AAA vs. D)
    *   Two types: Non-rechargeable & Rechargeable
*   **Non-rechargeable ("Primary"):**
    *   E.g., Typical alkaline battery Vcell = ~1.5 V
*   **Rechargeable ("Secondary"):**
    *   E.g., Lithium-Ion (LiIon), Lithium Polymer (LiPo), Nickle Metal Hydride (NiMH), Nickle Cadmium (NiCd)
    *   Widely varying Vcell and behaviour
    *   Cell voltage drops as battery energy is used up
    *   See https://www.epectec.com/batteries/chemistry/ for great info
*   **Battery comparison**
    *   A visual representation of different battery sizes, including AAA, AA, C, D, and PP3, is provided to illustrate the varying sizes of batteries.
*   **Circuit symbol for a battery**
    *   A diagram shows the circuit symbol for a battery, which is represented by two parallel lines with a positive terminal marked "+" and a negative terminal marked "-".

In summary, the slide provides a comprehensive introduction to battery basics, covering the fundamental principles of electrochemical cells, the differences between non-rechargeable and rechargeable batteries, and examples of various battery types. The visual aids, including the comparison of different battery sizes and the circuit symbol for a battery, enhance the understanding of the concepts presented.

### Slide 7

The image presents a slide from a presentation about battery capacity, featuring a white background with black text and a purple gradient at the top. The title "Battery Capacity" is prominently displayed in bold, black font.

*   **Title and Bullet Points**
    *   The title "Battery Capacity" is centered at the top of the slide.
    *   Four bullet points provide information about battery capacity:
        *   Capacity = total amount of energized charge available = Ccell
        *   Different than capacitance of a capacitor!
        *   Units of milliamp-hours (mA·h) or amp-hours (A·h)
        *   Handy units: How long a battery can provide a given amount of current charged to battery voltage
*   **Example and Calculation**
    *   An example is given: Energizer Max AA battery has Ccell = 2500 mAh.
    *   A calculation is performed to determine how long the battery can power a 20 mA LED circuit:
        *   Capacity = Current x time, C = I·t
        *   t1 = C/I1 = 2500 mA·h / 20 mA = 125 h
        *   t2 = C/I2 = 2500 mA·h / 2000 mA = 1 h 15 m
*   **Diagram and URL**
    *   A diagram on the right side of the slide illustrates a simple circuit with a 1.5V battery, a resistor, and an LED.
    *   The URL "https://data.energizer.com/pdfs/e91 max na.pdf" is provided at the bottom of the slide.
*   **Footer and Page Number**
    *   The page number "7" is displayed at the bottom center of the slide.
    *   A logo is visible in the bottom-right corner.

In summary, the slide provides an overview of battery capacity, including its definition, units, and a practical example using an Energizer Max AA battery. The calculation demonstrates how to determine the battery's lifespan based on its capacity and the current drawn by a circuit.

### Slide 8

The image presents a slide titled "Battery Capacity" that discusses the concept of battery capacity, its units, and how to calculate the total usable electrical energy stored in a battery.

*   The title is prominently displayed at the top of the slide.
*   Below the title, there are several bullet points that provide detailed information about battery capacity:
    *   **Capacity is a proxy for Qcell, the total charge that can be delivered at Vcell**
        *   1 mA × h = 10^-3 C/s × 60 s/min × 60 min/h = 3.6 C
        *   1 mAh = 3.6 C, and Qcell = 3.6Ccell (capacity in mAh)
        *   1 Ah = 3.6 kC, and Qcell = 3600Ccell (capacity in Ah)
        *   E.g., What is Qcell for the Energizer Max AA? 2500mA·h × 3.6 = 9 kC
    *   **Total usable electrical energy stored in a battery, Ecell = QcellVcell**
        *   Alternative units: Ecell = CcellVcell = [A × h] × [V] = [V × A × h] = [W × h] or mWh
        *   E.g., How much energy is stored in the Energizer Max AA battery given Vcell = 1.5 V?
            *   E = QV = 9k[C] × 1.5[J/C] = 13.5 kJ ← Is that "a lot"?
            *   Stop a heart with 400J. Car wreck = 960 kJ. Time is the missing factor.
*   The slide also includes some handwritten notes in red and blue ink, which appear to be additional explanations or examples related to the topic.
*   At the bottom of the slide, there is a URL link to a PDF document from Energizer, which likely provides more information about the Energizer Max AA battery.
*   In the bottom-right corner, there is a logo that appears to be a shield with a crest or emblem on it.

In summary, the slide provides a comprehensive overview of battery capacity, including its definition, units, and how to calculate the total usable electrical energy stored in a battery. The slide also includes examples and handwritten notes to help illustrate the concepts being discussed.

### Slide 9

The image is a slide from a presentation about battery packs, featuring a white background with a purple gradient banner at the top. The title "Battery Packs" is prominently displayed in bold black text on the left side of the slide.

**Visual Elements:**

* A diagram on the left side illustrates the concept of combining battery cells in series and parallel to increase available energy.
* The diagram consists of two parts:
	+ Top: A vertical stack of three battery cells connected in series, with a bracket indicating the total voltage (Vtotal) equal to N times the voltage of a single cell (Vcell).
	+ Bottom: A parallel connection of multiple battery cells, with a bracket showing the total capacitance (Ctotal) equal to M times the capacitance of a single cell (Ccell).

**Text Content:**

* Four bullet points on the right side of the slide provide additional information:
	+ "Combine battery cells in series and parallel to increase the available energy"
	+ "N cells in series gives higher voltage: Vtotal = NVcell"
	+ "Qtotal = Qcell and Ctotal = Ccell remain the same"
	+ "M cells in parallel achieves more charge: Qtotal = MQcell and Ctotal = MCcell"
	+ "Vtotal = Vcell remains the same"
	+ "Apply both approaches together to achieve Etotal = (MQcell)(NVcell)"
	+ "But with the added cost, weight, and size"

**Additional Elements:**

* A handwritten note in blue ink at the top-right corner reads "Single Cell".
* A URL at the bottom of the slide links to a webpage on Digikey's website, specifically https://www.digikey.ca/en/products/filter/battery-packs/89.
* A small logo in the bottom-right corner features a shield with a red and yellow design, accompanied by a black and white crest.

Overall, the slide effectively conveys the concept of combining battery cells to increase available energy, providing a clear and concise visual representation and accompanying text.

### Slide 10

The image presents a slide titled "State of Charge" with a white background, black text, and red accents. The title is prominently displayed at the top left.

**Title and Bullet Points**

*   "State of Charge" in bold black font
*   Five bullet points:
    *   "Battery voltage drops as it delivers charge (not linearly)"
    *   "Reality: Capacity and voltage are complicated functions of how the battery is used"
        *   Sub-bullet point: "Discharge current, temperature, battery age, number of prior recharge cycles, depth of discharge"
    *   "State of Charge (SoC) is like a gas tank indicator: 0% is empty, and 100% is full"
        *   Sub-bullet points:
            *   "SoC = 1 when battery has performed no work"
            *   "SoC = 0 when it has delivered E_total work"
    *   "V vs. SoC = Discharge Curve"
        *   Sub-bullet points:
            *   "Every chemistry has a different discharge curve"
            *   "E.g., 12-cell Nickle-Metal-Hydride (NiMH) battery pack"

**Graph**

A graph is situated on the right side of the slide, featuring:

*   A red curve representing the discharge curve
*   X-axis labeled "State of Charge (%)"
*   Y-axis labeled "Battery Pack Voltage (V)"
*   A fuel gauge icon above the graph, displaying a red needle pointing to "E" (empty)

**Additional Elements**

*   A logo in the bottom-right corner, consisting of a yellow shield with a red and black design
*   A small number "10" at the bottom center of the slide
*   A purple and black border at the top of the slide

This detailed description captures all the content present on the slide, including text, graphs, and images.

### Slide 11

The image presents a slide from a presentation on rechargeable batteries, featuring a white background with black text and red handwritten notes. The title "Rechargeable Batteries" is prominently displayed at the top.

*   **Title and Main Points**
    *   The title "Rechargeable Batteries" is centered at the top of the slide.
    *   Four main points are listed below the title, each with sub-bullets providing additional information.
*   **First Main Point: Recharge a Battery**
    *   The first main point discusses recharging a battery by pushing current into it at a controlled rate, denoted as $I_r$.
    *   A diagram illustrates the process, showing the flow of current into the battery.
*   **Second Main Point: Higher $I_r$**
    *   The second main point explains that higher $I_r$ values result in faster charging but can cause batteries to overheat, become permanently damaged, or significantly reduce their capacity.
    *   No specific statistics are provided for this point.
*   **Third Main Point: Recharging Currents**
    *   The third main point defines recharging currents in terms of the battery capacity as $I_r = P \times C_{total}$.
    *   An example is given, where $P = 0.1 [h^{-1}]$ and $C_{total} = 2.1$ Ah for a NiMH battery, resulting in $I_r = 0.21$ A = 210 mA.
*   **Fourth Main Point: Higher $I_r$ with Sensing**
    *   The fourth main point mentions that higher $I_r$ is possible with voltage, current, and temperature sensing.
    *   A handwritten note in red ink suggests that $I_r$ usually drops as you approach full charge, and "Trickle charging" is written below it.
*   **Additional Handwritten Notes**
    *   Several handwritten notes are scattered throughout the slide, including "P=0.01" and "usually drop as you approach full charge."
    *   These notes appear to be related to the topic of rechargeable batteries and may have been added by the presenter or a student.

In summary, the slide provides an overview of rechargeable batteries, discussing how to recharge them, the effects of higher recharging currents, and the importance of sensing voltage, current, and temperature. The slide includes diagrams, equations, and examples to illustrate these concepts, as well as handwritten notes that add additional context and insights.

### Slide 12

The image presents a comprehensive overview of Lithium Polymer (LiPo) batteries, covering their advantages, disadvantages, charging requirements, safety precautions, and applications. The slide is divided into sections, each providing detailed information on a specific aspect of LiPo batteries.

*   **Advantages**
    *   High energy density
    *   Lightweight and thin
    *   Flexible shapes
*   **Disadvantages**
    *   Expensive
    *   Safety concerns (fire/explosion risk)
    *   Faster degradation over time
*   **Charging Requirements**
    *   Special chargers needed (current, voltage, and temperature monitoring)
    *   Balanced charging to ensure cell equality
    *   Voltage monitoring (> 4.2 V max per cell → thermal runaway)
*   **Safety Precautions**
    *   Handle carefully to avoid damage
    *   Store partially charged (3.7 - 3.8 V per cell prevents degradation)
    *   Do not discharge below 3.0 V per cell (irreversible damage → possible safety issues)
*   **Applications**
    *   Drones, RC vehicles, portable electronics
    *   High-performance consumer electronics

The slide also includes a graph that compares the energy density of different battery types, including LiPo batteries. The graph shows that LiPo batteries have a high energy density compared to other battery types.

*   **Graph: Energy Density Comparison**
    *   The graph displays the energy density of various battery types, including LiPo, Li-Ion, NiMH, NiCD, AGM, Gel, and Flooded batteries.
    *   The x-axis represents the energy density in Wh/kg, ranging from 0 to 250.
    *   The y-axis represents the energy density in Wh/l, ranging from 0 to 700.
    *   The graph shows that LiPo batteries have a high energy density, both in terms of weight and volume, making them suitable for applications where space and weight are limited.

In summary, the slide provides a detailed overview of LiPo batteries, highlighting their advantages, disadvantages, charging requirements, safety precautions, and applications. The graph compares the energy density of LiPo batteries with other battery types, demonstrating their high energy density and suitability for various applications.

### Slide 13

The image presents a slide titled "Batteries: Summary" in bold black text, providing an overview of the key aspects of batteries. The slide is divided into three sections, each focusing on a different aspect of batteries.

*   **Single Cell:**
    *   The section begins with a diagram illustrating a single cell, represented by a simple circuit symbol.
    *   The voltage (Vcell) is dependent on the cell's chemistry and state of charge (SoC).
    *   The capacity (Ccell) increases with the physical size of the cell and serves as a proxy for the charge (Qcell).
    *   Two equations are provided to calculate the energy stored in the cell:
        *   Ecell = Qcell \* Vcell [J] or Ecell = Ccell \* Vcell [Wh]
*   **Battery Pack:**
    *   A diagram showing a battery pack, comprising multiple cells connected in series and/or parallel, is presented.
    *   The total voltage (Vtotal) is calculated by multiplying the number of cells in series (N) by the voltage of each cell (Vcell).
    *   The total capacity (Ctotal) is determined by multiplying the number of cells in parallel (M) by the capacity of each cell (Ccell).
    *   The total energy (Etotal) is calculated using the formula: Etotal = Qtotal \* Vtotal = M \* N \* Qcell \* Vcell.
*   **State of Charge (SoC):**
    *   The state of charge is defined as a value between 0 (empty) and 1 (full).
    *   The voltage versus SoC curve, also known as the "discharge curve," is dependent on the chemistry of the battery.
    *   The recharge rate is influenced by the power (P) and total capacity (Ctotal), as well as the chemistry of the battery.

In summary, the slide provides a concise overview of the fundamental principles governing batteries, including the characteristics of single cells, battery packs, and the state of charge. The equations and diagrams presented offer a clear understanding of the relationships between voltage, capacity, energy, and other key parameters.

### Slide 14

The image is a slide from a presentation, titled "6.3 - Power Conditioning Circuits." The title is prominently displayed in large black text at the bottom left of the slide.

*   **Top Section:**
    *   The top section features a banner with a gradient that transitions from black to purple.
    *   Below the banner, there is an image of a circuit board with various components and wires.
*   **Main Content:**
    *   The main content area is blank, except for the title and a small number "14" centered at the bottom.
*   **Bottom Right Corner:**
    *   In the bottom right corner, there is a logo featuring a shield with a red and yellow design.
*   **Background:**
    *   The background of the slide is white.

Overall, the slide appears to be part of a larger presentation on power conditioning circuits, and the image of the circuit board at the top suggests that the topic may be related to electronics or electrical engineering.

### Slide 15

The image presents a slide titled "Overview" that appears to be part of a presentation on power conditioning circuits. The content is organized into three main sections: a diagram, a list of bullet points, and a footer.

**Diagram:**
The diagram illustrates the flow of power from a source to a mechatronic system, with a power conditioning circuit in between. The components are represented by boxes, and the flow of power is indicated by arrows. The diagram shows the following:

*   Power Source
*   Power Conditioning Circuits
*   Mechatronic System

The arrows between the components are labeled with variables such as Vsource, Isource, Vsystem, Isystem, fsource, and fsystem.

**Bullet Points:**
The slide lists three key points related to power conditioning circuits:

1.  **Power Conditioning Aim:** The primary goal of power conditioning is to convert power at one voltage, current, and frequency to another as efficiently as possible, up to a certain maximum power.
2.  **Efficiency Formula:** The efficiency of the power conditioning circuit is defined by the formula: η = Psystem / Psource = Pout / Pin = VsystemIsystem / VsourceIsource.
3.  **Circuit Categorization:** Power conditioning circuits can be broadly categorized based on their input/output characteristics, specifically whether they operate with AC or DC.

**Footer:**
The footer contains the number "15" in the center, indicating that this is likely the 15th slide in the presentation. In the bottom-right corner, there is a logo featuring a shield with a red and yellow design, accompanied by a black and white chevron pattern. The background of the slide is white, with a purple gradient bar at the top.

### Slide 16

The image displays a presentation slide with the title "Overview" and a discussion about the efficiency of a DC/DC board-mount module.

**Title and Content**

* The title "Overview" is prominently displayed in large black text at the top left of the slide.
* Below the title, a bullet point reads, "Example: How efficient is this DC/DC board-mount module."
* Two sub-bullet points provide specific values:
	+ Vsource = 72 VDC, Isource = 0.93 A
	+ Vsystem = 3.3 VDC, Isystem = 20 A

**Calculations**

* The efficiency of the module is calculated using the formula: η = Pout / Pin
* Pout is calculated as 3.3 x 20 = 66 W
* Pin is calculated as 72 x 0.93
* The efficiency is then calculated as (3.3 x 20) / (72 x 0.93) = 98.6%

**Image and URL**

* To the right of the calculations, an image of a green circuit board with various components is displayed.
* At the bottom of the slide, a URL is provided: https://www.digikey.ca/en/products/detail/flex-power-modules/PIM4710PDA/10287667

**Footer and Logo**

* The slide number "16" is displayed at the bottom center.
* A logo is visible in the bottom-right corner, although its details are not clear.

### Slide 17

The image presents a slide titled "Power Conditioning Circuits: Figures of Merit" in large black text at the top, set against a white background. The title is accompanied by a purple gradient bar above it.

Below the title, two columns of bullet points outline various figures of merit for power conditioning circuits:

**Left Column:**

* Efficiency
* Output Voltage Accuracy
	+ How close Vout matches specification
* Load Regulation
	+ Stability of Vout with changes in Iout
* Line Regulation
	+ Stability of Vout with changes in Vin
* Ripple and Noise
	+ Sometimes referred to as how "clean" a supply is
* Transient Response
	+ How fast Vout can respond to step change in Iout
* Mechanical: Size, Weight, Form Factor, Thermal

**Right Column:**

* Protection Features:
	+ Overvoltage protection (OVP)
	+ Overcurrent protection (OCP)
	+ Short-circuit protection (SCP)
	+ Thermal protection
* Power Factor Correction (PFC)
	+ Ensure that Vin and Iin are in-phase
* Level of Integration
	+ Module vs. Regulator vs. Controller
* Reliability
	+ Mean Time Between Failures (MTBF) quantifies average time between failures

At the bottom center of the slide, the number "17" is displayed, indicating that this is likely the 17th slide in a presentation. In the bottom-right corner, a logo featuring a shield with a red and yellow design is visible.

Overall, the slide provides a comprehensive overview of the key performance metrics for power conditioning circuits, highlighting their importance in ensuring reliable and efficient operation.

### Slide 18

The image displays a slide from a presentation about DC/DC converters, titled "DC/DC: Overview" in bold black text at the top left. 

*   The title is followed by a bullet point that reads, "Converting from one DC voltage to another is accomplished with linear or switching voltage regulators."
*   Below this, there is a handwritten note in blue ink that defines "LDO" as "Low-Dropout."
*   A table comparing linear and switching voltage regulators is presented, with the following columns:
    *   Type
    *   Function
    *   Efficiency
    *   Waste Heat
    *   Complexity
    *   Size
    *   Cost
    *   Ripple/Noise
*   The table has two rows, one for linear regulators and one for switching regulators, with the corresponding characteristics listed in each column.
*   At the bottom of the slide, there is a URL link to an article on DigiKey's website, titled "Understanding the Advantages and Disadvantages of Linear Regulators."
*   In the bottom-right corner, there is a logo featuring a shield with a red and yellow design.

The background of the slide is white, with a purple gradient bar at the top.

### Slide 19

The image presents a slide from a presentation on DC/DC converters, specifically focusing on linear regulators. The title "DC/DC: Linear Regulators" is prominently displayed in large black text at the top left of the slide.

**Key Points and Diagrams:**

*   Four bullet points provide key information about linear regulators:
    *   Often called "LDO": Low Drop-Out
    *   Higher DC voltage in, lower DC voltage out
    *   Uses negative feedback to check Vout against desired Vref
    *   E.g., what is the max efficiency of this linear regulator?
*   Three diagrams illustrate the concept:
    1.  A simple circuit diagram showing Vin, Vout, and GND, with a voltage drop of 1.7V between Vin and Vout.
    2.  A simplified representation of a linear regulator, highlighting the input and output voltages and currents.
    3.  A more detailed circuit diagram of a linear regulator, including a bandgap reference circuit and various components.

**Mathematical Equations and Formulas:**

*   The efficiency of the linear regulator is calculated using the formula: η = Pout / Pin = (Vout \* Iout) / (Vin \* Iin) = 3.3 / 5 = 66%
*   The power dissipated by the regulator is given by: PReg = Vdropout x I = 1.7V x Iout

**Notations and Annotations:**

*   Various notations and annotations are scattered throughout the slide, including:
    *   Red handwriting for equations and annotations
    *   Blue handwriting for additional comments
    *   Green annotations on the circuit diagrams
    *   A small logo in the bottom-right corner, featuring a shield with a red and yellow design.

Overall, the slide provides a concise overview of linear regulators, including their characteristics, operation, and efficiency.

### Slide 20

The image presents a slide titled "DC/DC: Switching Regulators" in bold black text, accompanied by two diagrams illustrating the concept of DC/DC switching regulators.

**Title and Bullet Points**

* The title is followed by two bullet points:
	+ "Uses a controlled switch to that is either fully on or fully off"
	+ "Can be configured as buck (shown), boost, or inverting depending on circuit"

**Diagrams**

The slide features two diagrams:

1. **Left Diagram**
	* A simple circuit diagram showing a voltage source (+5V), a switch, and an output voltage (+3.3V) with a capacitor and inductor.
	* The diagram is labeled with the following components:
		- Vin
		- SWout
		- GND
2. **Right Diagram**
	* A more complex circuit diagram illustrating the operation of a switching regulator.
	* The diagram includes various components such as resistors, capacitors, inductors, and a comparator.
	* The diagram is annotated with handwritten notes and labels, including:
		- "Controlling a switching duty cycle instead of transistor gate voltage"
		- "A: 1 closed, 2 open"
		- "B: 1 open, 2 closed"

**Additional Elements**

* A logo is visible in the bottom-right corner of the slide.
* The background of the slide is white, with a purple gradient bar at the top.

Overall, the slide provides a clear and concise overview of DC/DC switching regulators, including their basic principles and configurations. The diagrams effectively illustrate the concepts, making it easier for viewers to understand the material.

### Slide 21

The image presents a slide from a presentation on DC/AC power inverters, featuring a clear and concise layout. The title "DC/AC: Power Inverter" is prominently displayed at the top, followed by a bullet point that reads, "Use switching to reverse DC polarity across load." 

**Key Components:**

*   **Circuit Diagrams:** Two circuit diagrams are illustrated, showcasing the conversion of DC power to AC power.
*   **Handwritten Notes:** Handwritten notes in blue ink provide additional information and explanations.
*   **Logo:** A logo is situated in the bottom-right corner, indicating the source or affiliation of the presentation.

**Detailed Description:**

*   **Title and Bullet Point:**
    *   The title "DC/AC: Power Inverter" is centered at the top of the slide.
    *   A single bullet point below the title states, "Use switching to reverse DC polarity across load."
*   **Circuit Diagrams:**
    *   The left diagram illustrates a bridge circuit with a DC voltage source, switches, and a load resistor (R_L).
    *   The right diagram depicts a simple DC/AC inverter circuit using a transformer to boost the output voltage.
*   **Handwritten Notes:**
    *   The notes on the left side of the slide explain that the circuit creates an AC square wave, which can be filtered into a sine wave.
    *   The notes also highlight the ability to pre-boost the DC voltage to achieve a higher AC voltage, citing an example where 170V DC is converted to 178V AC square wave.
    *   The notes on the right side of the slide mention the use of a transformer to boost the output voltage.
*   **Logo:**
    *   A logo is positioned in the bottom-right corner of the slide, featuring a shield with a red and black design.

**Summary:**

The slide effectively communicates the fundamental concept of DC/AC power inverters, using clear diagrams and concise handwritten notes to illustrate the process of converting DC power to AC power.

### Slide 22

The image presents a slide titled "AC/DC: Rectifier Circuits" in bold, black font at the top. The title is accompanied by a purple and pink gradient bar above it.

Below the title, four bullet points outline key aspects of rectifier circuits:

*   Use four-diode bridge rectifier
*   May be preceded by a transformer to drop the line voltage
*   Bigger "bulk decoupling" C_L reduces V_r ripple voltage
*   Many four-pin through-hole and surface-mount packages

To the right of the bullet points, a circuit diagram illustrates the components involved in the rectifier circuit. The diagram includes:

*   A voltage source labeled "V_ac"
*   Four diodes arranged in a diamond configuration
*   A capacitor labeled "C_L" connected across the output
*   A resistor labeled "R_L" connected in parallel with the capacitor
*   A voltage output labeled "+ V_L" and "- V_L"

Below the bullet points, three images depict different types of rectifier packages:

*   Two small, black, rectangular packages with four pins each
*   A larger, black, rectangular package with four pins and a heat sink

At the bottom center of the slide, a graph displays the relationship between V_ac and V_L over time. The graph features:

*   A green sine wave representing V_ac
*   A blue waveform representing V_L
*   A red line indicating the ripple voltage V_r

The x-axis is labeled "22", while the y-axis is unlabeled. The background of the slide is white, with a logo in the bottom-right corner featuring a shield with a red and yellow design.

### Slide 23

The lecture slide is titled "AC/AC: Transformers." The slide contains information about the principle of transformers, including the following key points:

*   **Principle:**
    *   $I_{in} \rightarrow$ coupled magnetic flux $\Phi \rightarrow I_{out}$
    *   $V_{in}/V_{out} = N_{in}/N_{out}$ (ratio of coil turns)
    *   $P_{out} = \eta P_{in}$
*   **Only works for AC**
*   **Example:** 
    *   E.g., What is $I_{in}$ if $V_{in} = 120 V_{RMS}$, $V_{out} = 12 V_{RMS}$, $I_{out} = 1 A_{RMS}$, $\eta = 97\%$?
        *   $\eta = \frac{V_{out}I_{out}}{V_{in}I_{in}} \therefore I_{in} = \frac{12 \times 1}{120 \times 0.97} = 103 mA_{RMS}$

**Diagram:**

The slide features a diagram of a transformer, which includes:

*   A gray rectangular core with a primary winding and a secondary winding
*   The primary winding has $N_P$ turns and is labeled with a red coil and the text "Primary current" and "Primary voltage $V_P$"
*   The secondary winding has $N_S$ turns and is labeled with a blue coil and the text "Secondary current" and "Secondary voltage $V_S$"
*   A green dashed line represents the magnetic flux $\Phi$ through the core
*   The diagram is accompanied by a simple circuit diagram showing the input voltage $V_{in}$ and output voltage $V_{out}$

**Additional Information:**

*   A handwritten note at the bottom of the slide states, "Electromechanical doorbells have one of these."
*   The slide number "23" is displayed below the handwritten note.
*   A logo is present in the bottom-right corner of the slide, featuring a shield with a red and yellow design and a checkered pattern.

### Slide 24

The image is a slide from a presentation, likely used to conclude or thank the audience. The slide features a simple yet distinctive design.

*   **Title and Header**
    *   At the top of the slide, there is a header section with a gradient color scheme transitioning from black to purple.
    *   The title "Thanks!" is prominently displayed in bold, black font on the left side of the slide.
*   **Central Image**
    *   A large, hand-drawn illustration of a thumbs-up gesture is centered on the slide.
    *   The thumb is drawn in black and is accompanied by an arrow pointing upwards and to the right, symbolizing approval or appreciation.
    *   The illustration is simple and stylized, adding a touch of informality to the slide.
*   **Footer and Logo**
    *   At the bottom of the slide, the number "24" is displayed in small black text, indicating that this is the 24th slide in the presentation.
    *   On the bottom-right corner, a logo is visible, featuring a shield with a red and yellow design. The logo appears to be associated with the University of Cambridge, as suggested by the crest-like design.
*   **Background**
    *   The background of the slide is white, providing a clean and neutral backdrop for the content.

In summary, the slide is a concluding slide that expresses gratitude to the audience, featuring a stylized thumbs-up illustration and a logo that may represent the University of Cambridge.

