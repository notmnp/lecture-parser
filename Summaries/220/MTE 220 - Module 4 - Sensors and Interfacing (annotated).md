# MTE 220 - Module 4 - Sensors and Interfacing (annotated)

## Study Notes

# Sensors & Instrumentation – Problem‑Solving Cheat‑Sheet  

> Exam‑ready reference: core formulas, concepts, and step‑by‑step tactics for active and passive sensors.

---

## Core Formulas & Definitions  

| # | Formula | Symbols | When to Use |
|---|---------|---------|-------------|
| 1 | **Full‑scale / Span** | $x_{\text{range}} = x_{\max}-x_{\min}$ | Usable range of a sensor or ADC. |
| 2 | **Resolution** | $Q_{\text{sensor}} = \dfrac{x_{\text{range}}}{2^n}$ | Smallest detectable change at the sensor output. |
| 3 | **ADC LSB** | $Q_{\text{ADC}} = \dfrac{V_{\max}-V_{\min}}{2^n}$ | Voltage increment per ADC step. |
| 4 | **DAC Output** | $V_{\text{out}} = V_{\min} + \dfrac{D}{2^N-1}\,(V_{\max}-V_{\min})$ | Convert $N$‑bit word $D$ to analog voltage. |
| 5 | **PWM Duty Cycle** | $DC = \dfrac{t_{\text{high}}}{t_{\text{high}}+t_{\text{low}}}$ | Fraction of one period that the signal is high. |
| 6 | **PWM Average** | $V_{\text{avg}} = DC \times V_{\text{high}}$ | Mean voltage after low‑pass filtering. |
| 7 | **RC Time Constant** | $\tau = RC$ | First‑order integrator or low‑pass filter. |
| 8 | **Rise / Fall Time** | $t_{10-90}\approx 2.2\,\tau$ | Step response of a first‑order system. |
| 9 | **Maximum Switch Frequency** | $f_{\max} = \dfrac{1}{4.4\,\tau}$ | Minimum period for a reliable rise–fall cycle. |
|10 | **Low‑pass Cut‑off** | $f_c = \dfrac{1}{2\pi RC}$ | –3 dB point of a single‑pole filter. |
|11 | **Voltage Divider** | $V_{\text{out}} = V_{\text{in}}\dfrac{R_2}{R_1+R_2}$ | Passive level shifting. |
|12 | **MOSFET Level Shift (N‑FET)** | $V_{\text{out}}\approx V_{\text{rail}}\;(g_{\text{high}}),\;V_{\text{out}}\approx0\;(g_{\text{low}})$ | Inverted logic with pull‑up resistor. |
|13 | **Hall Voltage** | $V_H = \dfrac{B\,I\,l}{n\,q\,A}$ | $B$ magnetic flux density, $I$ current, $l$ length, $A$ cross‑section, $n$ carrier density, $q$ charge. |
|14 | **Electromagnetic Induction** | $V = -N\,\dfrac{d\Phi_B}{dt}$, $\Phi_B = B\,A$ | Voltage induced by changing magnetic flux. |
|15 | **Seebeck Voltage** | $V = S\,\Delta T$ | $S$ Seebeck coefficient, $\Delta T$ temperature difference. |
|16 | **Peltier Heat** | $\dot Q = \Pi\,I$ | $\Pi$ Peltier coefficient, $I$ current. |
|17 | **Thomson Heat** | $\dot Q = \tau\,I\,\dfrac{dT}{dx}$ | $\tau$ Thomson coefficient, $dT/dx$ temperature gradient. |
|18 | **Piezoelectric Voltage** | $V = d_{33}\,F/A$ or $Q = d_{33}\,F$ | $d_{33}$ piezoelectric coefficient, $F$ applied force, $A$ electrode area. |
|19 | **Photoelectric Threshold** | $h\nu \ge \phi$ | $h$ Planck constant, $\nu$ photon frequency, $\phi$ work function. |
|20 | **Photovoltaic Open‑Circuit Voltage** | $V_{\text{oc}} = \dfrac{kT}{q}\ln\!\left(\dfrac{I_{\text{ph}}}{I_0}+1\right)$ | $I_{\text{ph}}$ light‑generated current, $I_0$ saturation current. |
|21 | **Capacitance (Parallel‑Plate)** | $C = \varepsilon_0\,\varepsilon_r\,\dfrac{A}{d}$ | $A$ area, $d$ spacing. |
|22 | **Inductance** | $L = \mu_0\,\mu_r\,\dfrac{N^2A}{d}$ | $N$ turns, $A$ core area, $d$ core length. |
|23 | **Capacitive Impedance** | $Z_c = \dfrac{1}{j\omega C}$ | Frequency‑dependent impedance of a capacitor. |
|24 | **Inductive Resonant Frequency** | $f_{\text{res}} = \dfrac{1}{2\pi\sqrt{LC}}$ | Resonance of an $L$–$C$ circuit. |
|25 | **Bridge Δv** | $\Delta v = V_s\!\left(\dfrac{R_x}{R_2+R_x}-\dfrac{R_3}{R_1+R_3}\right)$ | Differential output of an unbalanced Wheatstone bridge. |
|26 | **Balanced Bridge** | $R_x = \dfrac{R_2}{R_1}\,R_3$ | Condition for $\Delta v=0$. |

---

## Key Concepts & Intuition  

- **Active vs. Passive Sensors**  
  - *Passive*: Sensor changes a physical property (R, C, L) that is sensed by external circuitry (e.g., thermistor, capacitive humidity sensor).  
  - *Active*: Sensor *generates* a measurable electrical signal (e.g., Hall element, photo‑diode, piezoelectric transducer) by coupling the sensed physical quantity to an electric domain.

- **Signal Conditioning**  
  - Choose a divider or bridge that linearises the sensor response over the expected range.  
  - Match source impedance to the next stage (e.g., op‑amp input, ADC input) to avoid loading.

- **Resolution vs. Accuracy**  
  - **Resolution**: smallest step the converter can distinguish (LSB).  
  - **Accuracy**: closeness of measurement to the true value, limited by sensor tolerance, offset, and calibration.

- **Bandwidth & Filtering**  
  - RC filters must satisfy $f_c \ll$ PWM frequency but $f_c$ > signal bandwidth to suppress ripple.  
  - $f_{\max}=1/(4.4\tau)$ guarantees the RC network can follow the switching transitions.

- **Quantization & Noise**  
  - ADC/DAC quantization error ≤ ½ LSB.  
  - Additive noise (thermal, flicker) can dominate if the signal is smaller than the LSB.

- **Hall Effect**  
  - Transverse voltage $V_H$ is proportional to $B$ and the driving current $I$.  
  - Sign of $V_H$ indicates polarity of $B$.

- **Electromagnetic Induction**  
  - Time‑varying flux $\Phi_B$ induces an EMF proportional to its rate of change.  
  - Number of turns $N$ scales the induced voltage.

- **Thermoelectric Effects**  
  - Seebeck: $V$ proportional to temperature difference.  
  - Peltier & Thomson: heat transport by current.

- **Piezoelectric Effect**  
  - Mechanical stress ↔ electric charge (or voltage).  
  - Used for force/strain sensors and actuators.

- **Photoelectric & Photovoltaic**  
  - Photon energy must exceed material work function to liberate electrons.  
  - Photovoltaics convert light energy to electrical energy; open‑circuit voltage depends logarithmically on photocurrent.

---

## Problem‑Solving Strategies  

| Sensor Type | Typical Cues | Step‑by‑Step Checklist | Common Mistakes |
|-------------|--------------|------------------------|-----------------|
| **Hall Sensor** | “Hall voltage”, “magnetic field measurement”, “B‑field sensor” | 1. Identify $I$, $l$, $A$, $n$ (from datasheet). 2. Compute $V_H$ via $V_H = B I l/(n q A)$. 3. If $V_H$ measured, rearrange to find $B$. 4. Check polarity sign. | Ignoring carrier density $n$ or using wrong unit for $l$ (cm vs m). |
| **Electromagnetic Induction** | “Induced emf”, “changing magnetic flux”, “inductor with AC” | 1. Find $N$, $B$, $A$, $\nu$ (or $dB/dt$). 2. Compute $\Phi_B = B A$. 3. Compute $V = -N\,d\Phi_B/dt$. | Using $V = N\,\Phi_B$ instead of derivative; forgetting the minus sign. |
| **Seebeck (Temperature Sensing)** | “Thermocouple”, “temperature from voltage”, “Seebeck coefficient” | 1. Know $S$ (V/K) for the material pair. 2. Measure $V$. 3. Compute $\Delta T = V/S$. 4. Add reference temperature if needed. | Using $S$ in mV/°C without unit conversion. |
| **Peltier** | “Thermoelectric cooler”, “heat pumped”, “Peltier coefficient” | 1. Get $\Pi$ (W/A). 2. Measure or set current $I$. 3. Compute heat $\dot Q = \Pi I$. | Ignoring Joule heating and Thomson effect in real designs. |
| **Piezoelectric** | “Force sensor”, “strain gauge”, “piezo voltage” | 1. Identify $d_{33}$, $A$, or $F$. 2. Use $V = d_{33} F / A$ (or $Q = d_{33}F$). 3. Convert charge to voltage via capacitor if needed. | Forgetting electrode area or mixing units of force and charge. |
| **Photoelectric** | “Photon detection”, “work function”, “photo‑diode” | 1. Check photon energy $h\nu$. 2. Compare to work function $\phi$. 3. If $h\nu\ge\phi$, electrons ejected; compute kinetic energy $E_k = h\nu - \phi$. | Using $E = hc/\lambda$ without converting to joules; ignoring quantum efficiency. |
| **Photovoltaic** | “Solar cell output”, “photocurrent”, “open‑circuit voltage” | 1. Know $I_{\text{ph}}$, $I_0$, $T$. 2. Use $V_{\text{oc}} = (kT/q)\ln(I_{\text{ph}}/I_0+1)$. 3. Plot or calculate I–V curve if needed. | Assuming linear I–V; ignoring series resistance and shunt paths. |
| **Capacitive Sensor** | “Humidity sensor”, “distance sensor”, “variable capacitance” | 1. Calculate $C$ from geometry or calibration curve. 2. Compute impedance $Z_c = 1/(j\omega C)$. 3. If used in a bridge, apply bridge equations. | Treating $C$ as resistive; neglecting dielectric loss. |
| **Inductive Sensor** | “Proximity sensor”, “resonant frequency shift” | 1. Compute $f_{\text{res}} = 1/(2\pi\sqrt{LC})$. 2. After change in $L$, recalc $f_{\text{res}}$. 3. Relate Δf to ΔL. | Ignoring parasitic capacitance; assuming linear change in $L$. |
| **RC Filter Design** | “Filter bandwidth”, “rise time”, “PWM filtering” | 1. Desired $t_{10-90}$ → compute $\tau = t/2.2$. 2. Pick $R$ or $C$ to satisfy $RC=\tau$. 3. Verify $f_c=1/(2\pi RC)$. | Using $RC=5\tau$; not checking load impedance. |
| **Voltage Divider** | “Level shift”, “output voltage” | 1. Set ratio $R_2/(R_1+R_2)=V_{\text{out}}/V_{\text{in}}$. 2. Select convenient resistor values (high to reduce current draw, low to lower output impedance). 3. Verify input source can drive the divider. | Choosing too small resistors (high current) or too large (high impedance loading). |
| **MOSFET Level Shift** | “Logic level translation”, “inverted output” | 1. N‑FET with gate threshold $V_{GS(th)}<$ low logic level. 2. Pull‑up resistor to high logic rail. 3. Output follows inverted logic with low impedance. | Assuming MOSFET conducts when gate is low; forgetting pull‑up. |
| **Wheatstone Bridge** | “Strain gauge”, “resistance change”, “ΔR measurement” | 1. Balance bridge: $R_x = (R_2/R_1) R_3$ for zero output. 2. After change, compute $\Delta v$ with bridge equation. 3. Solve for new $R_x$ or strain. | Mixing $R_2$ and $R_3$ signs; ignoring temperature compensation. |

---

## Common Pitfalls & Checks  

| Pitfall | Why It Happens | Fix |
|---------|----------------|-----|
| **Unit mismatches** | Mixing volts, millivolts, kilohms, etc. | Convert all to SI before calculation. |
| **Sign conventions** | Confusing polarity of Hall voltage or induced EMF. | Draw the direction of magnetic field and current; remember $V=-d\Phi/dt$. |
| **Neglecting series resistance** | Assuming ideal capacitors or inductors; real components have $R_s$. | Add $R_s$ in series when computing impedance. |
| **Using $2^n$ instead of $2^n-1$** | Off‑by‑one in ADC resolution. | Use $2^n-1$ intervals for LSB. |
| **Ignoring temperature effects** | Sensor parameters change with $T$ (e.g., $S$ of thermocouple). | Calibrate at operating temperature or include compensation. |
| **Over‑loading a divider** | Low resistor values draw excessive current. | Choose $R_1,R_2$ > 10 kΩ unless low impedance required. |
| **Assuming linearity of non‑linear sensors** | e.g., piezoelectric voltage vs. stress is linear only over limited range. | Verify linear region from datasheet; use polynomial fit otherwise. |
| **Not accounting for hysteresis** | Sensors like strain gauges or thermocouples show different forward/reverse curves. | Measure both directions; calculate hysteresis $H$. |
| **Using static formula for dynamic conditions** | E.g., using static $V_H$ for rapidly changing fields. | Check bandwidth and add filtering if necessary. |
| **Ignoring quantum efficiency in photo‑sensors** | Underestimating output signal. | Use QE factor from datasheet in calculations. |
| **Assuming infinite input impedance for ADC** | ADC may have source impedance limit. | Keep $R_{\text{source}}\le 10\,\text{k}\Omega$ or use a buffer. |

---

## Quick Reference Checklist  

1. **Identify the sensor type** (Hall, thermocouple, piezoelectric, etc.).  
2. **Pick the core formula(s)** from the table above.  
3. **Insert all known values** – always check units.  
4. **Compute intermediate parameters** (LSB, $\tau$, $V_H$, $f_{\text{res}}$).  
5. **Verify constraints** (bandwidth, current draw, input impedance).  
6. **Validate the result** – sanity check against expected ranges.  
7. **Document assumptions** (ideal component, linearity, calibration).  

Use this sheet to scan the key steps for each typical question. Master the formulas, understand the intuition, and practice applying the strategies to avoid the common pitfalls.

---

## Raw Slide Summaries

### Slide 1

The slide is titled "Module 4: Sensors and Interfacing" and appears to be from a lecture on sensors and instrumentation. 

**Title and Course Information**

* The title **Module 4** is written in large black text at the top left of the slide.
* Below the title, **Sensors and Interfacing** is written in slightly smaller black text.
* The course information **MTE 220 - Sensors and Instrumentation** is written in gray text below the module title.

**University Logo and Faculty Information**

* In the bottom-left corner, there is a logo for the **University of Waterloo**, which features a yellow shield with a red crest and a black and white chevron.
* To the right of the logo, the text **FACULTY OF ENGINEERING** is written in small black text, aligned vertically with the logo.

**Image**

* On the right side of the slide, there is a close-up image of a **circuit board**.
* The circuit board has a dark background with **teal-colored circuitry** and various components such as **silver dots** ( possibly solder balls or vias), **teal lines** ( possibly copper wiring), and **circular pads** (possibly for mounting components).
* The image appears to be a high-quality photograph of a printed circuit board (PCB), showcasing its intricate design and layout.

**Border and Background**

* The slide has a **black border** at the top and bottom.
* A **purple and black gradient** runs along the top border.
* The background of the slide is **white** on the left side and **circuit board image** on the right side.

### Slide 2

The slide is titled "4.1 - Sensor Characteristics" and features a white background with a purple and black bar at the top. The top of the slide has an image of a computer circuit board with teal-colored lines and silver dots.

*   The title of the slide is **4.1 - Sensor Characteristics**.
*   The slide number is **2**, located at the bottom center of the slide.
*   There is a logo in the bottom-right corner, which appears to be a shield with a red and yellow design.
*   The background of the slide is predominantly white, with a black and purple bar at the top.
*   The top of the slide features an image of a computer circuit board with:
    *   Teal-colored lines
    *   Silver dots
    *   Various shapes and patterns

There are no equations, formulas, definitions, bullet points, or diagrams on this slide.

### Slide 3

The slide is titled "Premise" and has a white background with a purple and black border at the top. The main content is in black text.

* The title "Premise" is written in large, bold font.
* Below the title, there are four bullet points:
  * Transducers are devices that convert energy from one domain, $x$, to another, $y$.
  * E.g. a piezoelectric material has a voltage difference between its surfaces proportional to a given strain.
  * Transducers can be sensors or actuators (and indicators).
  * Sensors produce signals that represent measured physical values
  * Actuators and indicators produce some action based on an applied signal.

Below the bullet points, there is a simple diagram of a sensor with the following labels:
* "Sensor" is written above the diagram.
* "Input $x$" is written to the left of the diagram, connected to it by a line.
* "Output $y$" is written to the right of the diagram, connected to it by a line.

The diagram shows a simple cylindrical shape with a line extending from each side, representing the input and output. The number "3" is centered at the bottom of the slide.

There is a logo in the bottom-right corner of the slide, which appears to be a shield with a red and yellow design. 

Overall, the slide provides a brief introduction to the concept of transducers, including their definition, examples, and types.

### Slide 4

The slide is titled "Sensor Range" and features a diagram of a sensor with an input and output. The main content of the slide is as follows:

**Bullet Points:**

* **Input Range**: 
  - Range of input values that creates useful output values
  - Input Range = $x_{max} - x_{min}$, or $(x_{min}, x_{max})$

* **Output Range**: 
  - Range of output values corresponding to the full range of input values
  - Output Range = $y_{max} - y_{min}$, or $(y_{min}, y_{max})$

* **Common Input Types**: 
  - Temp, humidity, electric field, magnetic, position, speed, acceleration

* **Common Output Types**: 
  - force, strain, angle, torque, light intensity, light color, voltage, current, chemical concentrations, frequency

**Additional Written Text:**
- Voltage, current, resistance, capacitance, inductance, digital: serial (I2C, SPI), parallel, pulse characteristics, freq., etc.

**Diagram:**
The diagram shows a graph with the following features:
- The x-axis is labeled "Input $(x)$" and has two points marked: $x_{min}$ and $x_{max}$.
- The y-axis is labeled "Output $(y)$" and has two points marked: $y_{min}$ and $y_{max}$.
- A red curve starts at $(x_{min}, y_{min})$ and increases to $(x_{max}, y_{max})$.
- A blue vertical line is drawn at $x_{max}$.
- A black arrow points to the curve from the top of the y-axis.
- The background of the graph has a grid pattern with dotted lines.

### Slide 5

The slide is titled "Transfer Function" and contains the following content:

**Bullet Points:**

* Often taken to mean "output as a function of input"
* whereas "transfer function" usually means LTI (linear time-invariant) in ME 253, 351, 360, 494

**Equations and Formulas:**

* Units are $\left[\frac{Output \: state}{Input \: state}\right]$, e.g. $\left[\frac{V}{kPa}\right]$, $\left[\frac{Hz}{N}\right]$

**Examples:**

* Eg: Resistive Pressure Sensor: $A=10\left[\frac{\mu S}{kPa}\right]$, Means $+10\mu S$ for every $+1 kPa$
* often nonlinear, often has DC offset. Both complicate design process.
* Eg, made-up, more realistic sensor TF $R_{out}(P_{kPa})= 10 \times P_{kPa} + 0.02 \times P^2_{kPa} + 7 [k\Omega]$
* Can also include frequency or time domain effects (eg model RC delay, frequency of operation via LPF, etc.)

**Graph:**

The graph is a plot of output (V) versus input (x) in units of [kPa]. The x-axis ranges from 0 to 10 [kPa], and the y-axis ranges from 0 to 100. There are two curves on the graph: a blue curve and a red curve. The blue curve is a straight line with a slope of $10[\frac{\mu S}{kPa}]$. The red curve is a nonlinear curve that increases rapidly at first and then levels off.

**Additional Notes:**

* The graph has a grid pattern with dotted lines, and the axes are labeled.
* There is a logo in the bottom-right corner of the slide, which appears to be a shield with a red and yellow design.

### Slide 6

The image presents a slide from a presentation on accuracy, featuring a white background with a purple and black border at the top. The title "Accuracy" is prominently displayed in large black text.

**Equations and Formulas:**

*   $Eg: x$ is known to be exactly $10 mm$ 
*   $x_M = 10.1 mm$, 
*   $\therefore$ Measurement Error $=-0.1 mm$
*   Measurement Error = Actual Value - Measured Value

**Definitions:**

*   **Accuracy:** How close a measured value is to the actual value
*   **Measurement accuracy:** Measurement error guaranteed by the manufacturer

**Bullet Points:**

*   Accuracy: 
    *   Quantifies the measurement error
    *   Measurement Error = Actual Value - Measured Value
*   Measurement accuracy: 
    *   Measurement error guaranteed by the manufacturer
    *   Actual Value is within Measured Value $\pm$ Measurement Accuracy
*   Actual measurement error should not exceed the manufacturer-specified measurement accuracy
    *   Say MFG said measurement accuracy was $\pm 0.2 mm$. Any measurement from $9.8 mm$ to $10.2 mm$ is "in spec"
*   System accuracy considers all the individual sensor and system errors to determine an overall accuracy
    *   $Eg:$ Terrible sensor $+$ high-quality $ADC \rightarrow$ Bad system accuracy.
    *   Some errors add, others are root-sum-squared

**Additional Text:**

*   "Ground Truth" is underlined and written in red handwriting.
*   The number "6" is displayed at the bottom center of the slide.
*   A logo is located in the bottom-right corner, featuring a yellow shield with a black and red design.

Overall, the slide provides a clear and concise explanation of accuracy, measurement error, and system accuracy, along with relevant equations and definitions.

### Slide 7

The slide discusses the concept of accuracy in measurement, specifically how it is expressed and calculated. 

**Title and Subtitle**
The title of the slide is "Accuracy" in bold black text. 

**Table Description**
The slide features a table with a purple header and three columns: 
- **Measurement Accuracy Type**
- **E.g.: -90° to +90° angle sensor**
- **Resulting Measurement Accuracy**

The table has four rows:
- **% of full-scale input**: 
  - ±0.5% full-scale
  - ±0.45° at all angles
- **% of instrument span**: 
  - ±0.5% instrument span
  - ±0.7° at all angles
- **% of present measured value**: 
  - ±0.5% measured value
  - Eg: 45°, ± 0.225°
- **Absolute worst-case**: 
  - ±0.1°
  - ± 0.1° at all angles

**Diagram Description**
A diagram is located at the bottom left of the slide, illustrating the concepts of "zero-scale", "full-scale", and "instrument span". 
- The diagram shows a semicircle with a blue line representing the measured value, a red line representing the instrument span, and a dotted line indicating the full-scale input. 
- The "zero-scale" is labeled at -90°, and the "full-scale" is labeled at +90°, with the instrument span equal to 180°. 
- The diagram also includes handwritten notes explaining that the terminology applies to both input and output.

**Additional Notes**
Handwritten notes are scattered throughout the slide, providing additional explanations and examples. 
- A note explains that the terminology applies to both input and output. 
- An example is given for the "% of present measured value" row, where a measurement of 45° has an accuracy of ± 0.225°.

### Slide 8

The image presents a slide from a presentation on sensitivity, likely in the context of engineering or a related field. The slide is titled "Sensitivity" and features a white background with black text.

**Title and Definition**

* The title "Sensitivity" is prominently displayed in large, bold black font at the top of the slide.
* Below the title, four bullet points provide a definition and explanation of sensitivity:
	+ The measure of a change in output to a change in input
	+ Like the gain of a transfer function
	+ E.g., speed sensor $V_{out} = 100 \left[\frac{mV}{km/h}\right] \times Speed_{km/h} + 2 V$
	+ High sensitivity is often desirable but costly

**Equation and Handwritten Notes**

* The equation for the speed sensor is accompanied by handwritten notes in red ink, which read:
	+ Sensitivity, slope of output vs. input curve at operating point

**Visual Elements**

* A purple and black bar runs across the top of the slide, adding a pop of color to the design.
* A small logo featuring a yellow shield with a red dragon and a black and white chevron is located in the bottom-right corner of the slide.
* The number "8" is centered at the bottom of the slide, likely indicating the slide number.

Overall, the slide provides a clear and concise explanation of sensitivity, along with a relevant example and visual elements to support the content.

### Slide 9

The slide is titled "Hysteresis" and features a white background with a purple and black border at the top. The main content is divided into two sections: a list of bullet points on the left and a graph on the right.

**Bullet Points:**

* "History"
* Different behaviour:
	+ Whether increasing or decreasing
	+ The previous state of the system
* Usually undesirable in sensors
	+ Complicates measurement and control systems

The bullet points are written in black text, while the handwritten notes are in blue ink.

**Graph:**

The graph is a plot of output (y) versus input (x). It features two curves:

* A blue curve that increases as the input increases
* A red curve that decreases as the input decreases

The curves intersect at several points, forming a hysteresis loop. The graph has a black border with a grid pattern, and the axes are labeled:

* Output (y) on the y-axis
* Input (x) on the x-axis

Both axes have arrowheads at the ends, indicating that they extend beyond the visible range. The graph appears to be a representation of the hysteresis phenomenon, showing how the output depends on the history of the input.

**Additional Elements:**

* A small logo in the bottom-right corner, which appears to be a shield with a red and yellow design
* The number "9" in small black text at the bottom center of the slide, likely indicating the slide number.

### Slide 10

The slide is titled "Reproducibility" and contains the following content:

**Definition and Procedure:**

* Quantifies the change in measured values as an input is repeatedly applied
* Procedure:
	+ Begin at same initial value every time
	+ Traverse to measurement state
	+ Measure Sample Vout
	+ Repeat 1000s of times

**Example:**

* Speed sensor with A = 100 [mV/(km/h)]
* Speed = 10.00 km/h
* Vout (ideal) = 1.000 V

**Handwritten Notes:**

* A blue handwritten note provides an example of a set of measured values:
	+ Vout1 = 1.012 V
	+ Vout2 = 1.607 V
	+ Vout3 = 0.996 V
	+ ...
* The note also mentions that from this set of measured values, statistics like mean and standard deviation (variance) can be obtained.

**Sources of Error:**

* A red handwritten note on the right side of the slide lists sources of error as:
	+ Random processes and fluctuations in operating conditions
	+ Electrical noise
	+ Temperature (Temp.)
	+ Vcc fluctuations
	+ etc.

**Slide Number and Logo:**

* The slide number "10" is displayed at the bottom center of the slide.
* A logo is present in the bottom-right corner, featuring a yellow shield with a red and black design.

### Slide 11

The slide is titled "Resolution" and contains the following content:

**Title:** Resolution

**Bullet Points:**

* The minimum detectable change in input $x$
* Analog:
	+ Minimum measurable change in input value
	+ Often expressed as % of full-scale value
* Digital:
	+ Change in input required to cause a 1-bit change in output (LSB)

**Equations and Formulas:**

* $\frac{Input\ Range}{\#\ of\ digital\ states} = \frac{90-0 [^{\circ}]}{2^{12} [states]} = 21.77\ milli-degrees/state \rightarrow "per\ LSB"$

**Handwritten Notes:**

* Eg. 0 to 1mm linear position sensor with "0.1% resolution". What is the smallest change in displacement that you can reliably measure?
	+ $0.001 \times 1mm = 1\mu m$. $Q = 1\mu m$
* Eg: Digital angle sensor module w/ $0^{\circ}$ to $90^{\circ}$ input range and a 12-bit output. What's the smallest measurable change in angle?

**Diagram/ Image:** 
There are no diagrams or images on this slide.

**Other Content:**

* A logo in the bottom-right corner featuring a shield with a red and yellow design.
* A small number "11" in the bottom-center of the slide, possibly indicating the slide number. 
* A purple and black border at the top of the slide.

### Slide 12

The slide is titled "Linearity" and features a white background with a purple and black border at the top. The main content is divided into two sections: a bullet point list on the left and a graph on the right.

**Bullet Point List:**

* The straightness of a sensor's input-output relationship compared to a perfectly straight line
	+ Measure how closely the actual response matches a straight line
	+ Equation: y = mx + b
		- y: output
		- m: sensitivity
		- x: input
		- b: offset
	+ Usually expressed as % of full scale OR "bits of nonlinearity" at output

**Graph:**

The graph is a plot of output (y) versus input (x) and features:

* A blue line labeled "Best Fit Straight Line (BFSL)"
* A red line labeled "Actual Response"
* A vertical gray dotted line indicating the maximum nonlinearity
* A horizontal black arrow pointing upward on the y-axis
* A horizontal black arrow pointing to the right on the x-axis
* Gridlines with gray dotted lines

The graph illustrates the relationship between the actual response of a sensor and its best-fit straight line, highlighting the concept of linearity and nonlinearity.

### Slide 13

The slide is titled "Sensor Step Response" and features a graph with a white background and a black, purple, and pink border at the top. The graph displays three curves: 

*   A red square wave representing the "Sensor Input" 
*   A blue curve labeled "First-Order Response"
*   A green curve labeled "Second-Order Response"

The x-axis is labeled "t" and the y-axis is labeled "x, y". 

The slide also includes handwritten notes in blue and green ink. The blue ink notes read:

*   "First-Order: There's a time constant, $\tau$, just like in RC/RL circuits. Determines how fast the sensor can respond to step changes in input. often expressed as $10\% \to 90\%$ rise time. $(2.2\tau)$ or as $63\%$ $(1\tau)$."

The green ink notes read:

*   "Second-Order: Oscillations are possible. called 'ringing'. Usually, adding damping (b, friction, damper) will eliminate. Ringing can lead to instability in feedback. (MTE 351, MTE 360, MTE 484)."

There is also a diagram at the bottom of the slide showing the flow of $x(t)$ into a "Sensor" and out as $y(t)$. The slide number "13" is centered at the bottom, and a logo is in the bottom-right corner.

### Slide 14

The image presents a lecture slide focused on sensor characteristics, specifically addressing problems related to a linear position sensor and an 8-bit Analog-to-Digital Converter (ADC). The slide is divided into four main bullet points, each detailing a different aspect of the sensor and ADC's performance.

*   **Linear Position Sensor Characteristics**
    *   The linear position sensor has a transfer function of $20 [mV/mm]$ and an output range of $0$ to $1.5 V$.
    *   The instrument span is calculated as $x_{max} - x_{min} = \frac{(1.5-0)[V]}{20[mV/mm]} = 75mm$.
*   **8-bit ADC Resolution**
    *   An 8-bit ADC has an input voltage range from $0$ to $3.3 V$.
    *   The resolution of the ADC is given by $Resolution (Q_{ADC}) = \frac{(3.3-0)}{2^8} = 12.89 mV$.
*   **Minimum Displacement Discernible by ADC and Sensor**
    *   If the ADC was sampling the above linear sensor, the minimum displacement it can discern is calculated as follows:
        *   $12.89 mV \leftarrow 1 LSB$
        *   $\frac{12.89 mV}{20 [mV/mm]} = 0.6445 mm$ or $644.5 \mu m$
*   **Limiting Device for Overall Measurement Accuracy**
    *   If the linear sensor has a resolution of $0.5 mm$, we need to determine which device (sensor or ADC) is limiting the overall measurement accuracy.
    *   The resolution of the sensor is $Q_{sensor} = 0.5 mm = 10 mV$, and the resolution of the ADC is $Q_{ADC} = 0.6445 mm = 12.89 mV$.
    *   Since $Q_{ADC} > Q_{sensor}$, the ADC is limiting the resolution.

In summary, the slide provides detailed calculations and explanations for understanding the characteristics of a linear position sensor and an 8-bit ADC, including their resolutions and how they impact the overall measurement accuracy.

### Slide 15

The slide is titled "4.2 – Sensor Interfacing" and has a white background with black text. 

* The title is in large, bold font on the left side of the slide.
* A small logo is located in the bottom-right corner of the slide. The logo features a yellow shield with a red design and a black and white chevron.
* The number "15" is centered at the bottom of the slide in small font.
* At the top of the slide, there is a purple and black bar.
* Below the bar, there is a picture of a computer circuit board with various components, including:
	+ Teal-colored lines and pathways
	+ Small circles and dots
	+ Silver dots arranged in rows
* The circuit board image spans the width of the slide and has a gradient effect, with the color fading to white at the bottom.

### Slide 16

The image presents a comprehensive overview of the Wheatstone Bridge, a fundamental concept in electrical engineering. The slide is titled "Wheatstone Bridge - Premise" and features a detailed diagram of the bridge circuit.

**Main Points:**

* **Calculate an unknown resistance Rx using known resistances R1-R3**
	+ The Wheatstone Bridge is used to measure an unknown resistance Rx by using three known resistances R1, R2, and R3.
* **All the other resistors will undergo the same variation due to operating conditions**
	+ The bridge circuit is designed to minimize the effects of operating condition variations on the measurement.
* **Creates a differential signal**
	+ The Wheatstone Bridge produces a differential signal, which is the difference between the voltages at points a and b.
* **One resistor can be variable (potentiometer, "pot") for calibration**
	+ One of the resistors, often R3, can be made variable to facilitate calibration of the bridge.
* **Often R3 for symmetry**
	+ For symmetry, R3 is often used as the variable resistor.

**Diagram:**

The diagram shows the Wheatstone Bridge circuit, which consists of:

* A voltage source Vs
* Resistors R1, R2, R3, and Rx
* Points a and b, which are connected to a differential amplifier or meter

The diagram also shows the equation for the differential signal:

Δv = vb - va = Vs * (Rx / (R2 + Rx)) - Vs * (R3 / (R1 + R3))

**Handwritten Note:**

A handwritten note at the bottom of the slide reads:

"Note: You can buy 'chip resistor arrays' with very well-matched resistors."

**Summary:**

In summary, the Wheatstone Bridge is a circuit used to measure an unknown resistance Rx using three known resistances R1, R2, and R3. The bridge produces a differential signal, which can be calibrated using a variable resistor, often R3. The circuit is designed to minimize the effects of operating condition variations on the measurement. The diagram shows the Wheatstone Bridge circuit, and the equation for the differential signal is provided. Additionally, a handwritten note suggests that chip resistor arrays with well-matched resistors can be purchased.

### Slide 17

The image presents a detailed lecture slide on the Wheatstone Bridge in voltage mode, featuring a comprehensive overview of the concept.

**Title and Main Content**

* The title, "Wheatstone Bridge - Voltage Mode," is prominently displayed in bold black text at the top of the slide.
* Below the title, two main bullet points outline the strategies for using the Wheatstone Bridge:
	+ **Two strategies for use**
		- **a. Vary R3 until Δv = 0, then**
			+ The equation for Rx is provided: Rx = (R2/R1) * R3
		- **b. Set R3 so that Δv = 0 under known calibration point, then use Δv to calculate resulting Rx while in operation**
			+ The equation for Rx is provided: Rx = R2 * (∆v/vs + R3/(R1+R3)) / (1 - (∆v/vs + R3/(R1+R3)))
			+ A handwritten note in blue ink reads: "I derived this from the two voltage dividers"

**Circuit Diagram and Graph**

* A circuit diagram is situated to the right of the main content, illustrating the Wheatstone Bridge configuration with the following components:
	+ A voltage source (vs)
	+ Resistors R1, R2, R3, and Rx
	+ A voltmeter measuring Δv
* Below the circuit diagram, a graph displays the relationship between Δv (in volts) and Rx (in kilohms), with the following characteristics:
	+ The x-axis represents Rx (in kilohms), ranging from 0 to 100
	+ The y-axis represents Δv (in volts), ranging from -2 to 2
	+ A red curve illustrates the non-linear relationship between Δv and Rx

**Additional Information**

* A bullet point at the bottom of the slide mentions that sometimes method 'b' will use a lookup table in software to get from Δv back to a physical parameter.
* The slide number "17" is centered at the bottom.
* In the bottom-right corner, a logo features a yellow shield with a red and black design, accompanied by the equations:
	+ R1 = R2 = R3 = 10 kΩ
	+ vs = 5 V

### Slide 18

The image presents a detailed example of a Wheatstone Bridge in voltage mode, with the title "Wheatstone Bridge - Voltage Mode Example" prominently displayed at the top.

**Problem Statement:**
The problem states that $v_x$ is measured to be $9 V$. The task is to determine $R_x$, as well as the values of $v_{x+}$ and $v_{x-}$.

**Equations and Calculations:**

*   $v_x = v_{x+} - v_{x-}$
*   $v_{x+} = 45 \frac{20}{5+20} = 36 V$
*   $\therefore v_{x-} = 36 - 9 = 27 V$
*   $v_{x-} = 45 \frac{R_x}{60+R_x} = 27$
*   $\therefore R_x = 90 k\Omega$

**Circuit Diagram:**
The circuit diagram is situated on the right side of the image and consists of:

*   A $45 V$ voltage source
*   A $5 k\Omega$ resistor
*   A $20 k\Omega$ resistor
*   A $60 k\Omega$ resistor
*   An unknown resistor $R_x$
*   The output voltage $v_x$ is labeled, with $v_{x+}$ and $v_{x-}$ marked as $36 V$ and $27 V$, respectively

**Additional Information:**

*   A link to a related circuit simulation is provided at the bottom left: https://everycircuit.com/circuit/4961377777221632
*   The page number "18" is displayed at the bottom center
*   A logo is present in the bottom-right corner

### Slide 19

The image presents a detailed lecture slide on the Wheatstone Bridge in Current Mode. The title, "Wheatstone Bridge - Current Mode," is prominently displayed at the top.

**Key Points:**

* Alternatively, we can determine $R_x$ by measuring $I_{out}$
* Good for low values of $R_x$
* Ammeter "looks like" a short circuit

**Circuit Diagram:**

The circuit diagram features a Wheatstone bridge configuration with the following components:

* $R_1$
* $R_2$
* $R_3$
* $R_x$

The diagram shows the following currents:

* $I_{in}$ (input current)
* $I_{out}$ (output current)
* $I_1$, $I_2$, $I_3$, and $I_x$ (branch currents)

**Equations:**

The slide provides several equations:

* $I's$ via current division:
	+ $I_1 = I_{in} \cdot \frac{R_2}{R_1+R_2}$, $I_2 = I_{in} \cdot \frac{R_1}{R_1+R_2}$
	+ $I_3 = I_{in} \cdot \frac{R_x}{R_3+R_x}$, $I_x = I_{in} \cdot \frac{R_3}{R_3+R_x}$
* KCL (Kirchhoff's Current Law) gives:
	+ $I_{out} = I_1 - I_2$ or $I_x - I_3$
	+ $\frac{1}{2}(I_1-I_2+I_x-I_3)$

**Additional Information:**

The slide number "19" is displayed at the bottom center, and a logo is present in the bottom-right corner.

### Slide 20

The slide presents a detailed analysis of a Wheatstone Bridge in current mode, focusing on determining the output current $I_{out}$ as a function of the unknown resistance $R_x$. 

**Title and Bullet Point:**
- The title of the slide is "Wheatstone Bridge - Current Mode Example."
- A bullet point reads: "Determine $I_{out}$ as a function of $R_x$."

**Circuit Diagram:**
The circuit diagram depicts a Wheatstone Bridge configuration with the following components:
- A current source of $1$ mA.
- Four resistors arranged in a diamond configuration:
  - The top resistor is $1\,\Omega$.
  - The bottom left resistor is $1\,\Omega$.
  - The bottom right resistor is $R_x$.
  - The left resistor (connected to the current source and the bottom left resistor) is $1\,\Omega$.
- The output current $I_{out}$ is shown.

**Equations:**
The following equations are provided:
1. $I_{out} = I_x - I_1$
2. $I_{out} = I_{in} \left(\frac{R_3}{R_3 + R_x} - \frac{R_1}{R_1+R_2}\right)$
3. Substituting given values:
   - $I_{out} = 1\,\text{mA} \cdot \left(\frac{1}{1+R_x} - \frac{1}{1+1}\right)$
   - $I_{out} = 1\,\text{mA} \cdot \left(\frac{1}{1+R_x} - 0.5\right)$
4. Solving for $R_x$:
   - $R_x = \frac{1\,\text{m}}{I_{out} + 0.5\,\text{m}} - 1$

**Additional Information:**
- A link to a circuit simulation is provided at the bottom left: https://everycircuit.com/circuit/4553458426445824.
- The slide number is $20$, located at the bottom center.
- A university crest or logo is present at the bottom right.

### Slide 21

The slide is titled "Rise Time" and features a white background with a purple and black bar at the top.

**Text Content:**

* The title "Rise Time" is displayed in large black text.
* Three bullet points:
	+ How fast a signal transitions from one value to another is often measured with the rise-time or fall-time
	+ Time to get from 10% to 90% of the transition
	+ Or vice versa
* An equation: $t_{rise} = t_{fall} \cong 2.2\tau$

**Graph:**

* A graph with a white background and black axes, featuring:
	+ A blue curve that starts at 0 and increases to a maximum value
	+ A red curve that starts at a maximum value and decreases to 0
	+ Both curves intersect at 10% and 90% of the transition
	+ The x-axis is labeled "t" and the y-axis is labeled "$V_{DD}$"
	+ The graph shows the rise and fall times, with $t_r = t_f = 2.2\tau$
	+ Green annotations on the graph: $0'$ and $V_{DD}$

**Table:**

* A table with four columns and three rows:
	+ Columns: $t[s]$, $\tau[\tau]$, $\exp\left(-\frac{t}{\tau}\right)$, and $1 - \exp\left(-\frac{t}{\tau}\right)$
	+ Rows:
		- $0.105 s$, $0.105 \tau$, $0.90$, $0.10$
		- $2.303 s$, $2.303 \tau$, $0.10$, $0.90$

**Additional Content:**

* A handwritten note at the bottom: $t_f \\ t_r \\ 2.303 \tau - 0.105 \tau \cong 2.2 \tau$
* A logo in the bottom-right corner featuring a yellow shield with a red and black design
* The number "21" in small black text at the bottom-center of the slide.

### Slide 22

The image presents a slide from a lecture on electronics, specifically focusing on the concept of fall time in a circuit. The slide is titled "Fall Time Example" and features a combination of text, equations, and a circuit diagram.

*   **Title and Problem Statement**
    *   The title "Fall Time Example" is prominently displayed at the top of the slide.
    *   The problem statement reads: "The fall time was measured to be 2.6 ms. What is the value of C?"
*   **Equations and Calculations**
    *   The equation for fall time is given as $t_f = 2.6 ms = 2.2 \tau$.
    *   The relationship between $\tau$ and $RC$ is stated as $\tau = RC$.
    *   Substituting $\tau$ into the equation for fall time yields $t_f = 2.2 RC$.
    *   The equation for capacitance $C$ is derived as $C = \frac{t_f}{2.2R}$.
    *   Given that $t_f = 2.6 ms$ and $R = 10 k\Omega$, the value of $C$ is calculated as:
        *   $C = \frac{2.6 m}{2.2 \times 10k} k \rightarrow m$
        *   $C = 0.118 \mu F = 118 nF$
*   **Circuit Diagram**
    *   A simple circuit diagram is shown, consisting of:
        *   A voltage source $V(t)$
        *   A capacitor $C$
        *   A resistor $10 k\Omega$
        *   The components are connected in series, with the capacitor and resistor forming an $RC$ circuit.
*   **Additional Information**
    *   The slide number "22" is displayed at the bottom center.
    *   A logo featuring a shield with a red and yellow design is located in the bottom-right corner.

In summary, the slide provides a clear and concise example of how to calculate the value of capacitance $C$ in an $RC$ circuit given the fall time and resistance. The equations and calculations are neatly presented, making it easy to follow along and understand the solution.

### Slide 23

The slide is titled "Rise and Fall Times in Digital Systems" and features two graphs, equations, and a circuit diagram.

**Graph 1 (left):**

* The graph shows a plot of voltage (v) versus time (t) with a red outline.
* The y-axis is labeled with "10%" and "90%" and has an arrow pointing upwards labeled "v".
* The x-axis has an arrow pointing to the right labeled "t".
* The graph displays two curves, one rising and one falling, with the following points marked:
	+ 10% and 90% on the y-axis.
	+ $t_r$ (rise time) and $t_f$ (fall time) on the x-axis.
* The equations written below the graph are:
	+ $T_{min} = t_r + t_f = (2.2 + 2.2) \tau = 4.4\tau$
	+ $f_{max} = \frac{1}{T_{min}}$
* A question is written above the graph in blue ink: "What's the max digital freq.?"

**Graph 2 (right):**

* The graph shows a plot of voltage versus time with multiple curves.
* The y-axis is labeled with "10%" and "90%" and has an arrow pointing upwards labeled "$V_{DD}$".
* The x-axis has an arrow pointing to the right labeled "t".
* The graph displays three curves with different rise and fall times, with the following labels:
	+ $\tau < \tau < \tau$ (three tau symbols)
* The curves represent different cases of rise and fall times.

**Equations:**

* $R=0.3\Omega$, $C=128pF$
* $f_{max} = \frac{1}{T_{min}} = \frac{1}{4.4RC} = \frac{1}{4.4 \times 0.3 \times 128p} = 5.92 GHz$

**Circuit Diagram:**

* The circuit diagram shows a simple RC circuit with the following components:
	+ A digital output from an Arduino board
	+ A resistor (0.3 $\Omega$) representing circuit board copper resistance
	+ A capacitor (128 pF)
	+ A transistor IC (MCH6660-TL-W)

**Additional Text:**

* A URL is provided at the bottom left: "https://everycircuit.com/circuit/5485295604727808"
* A number "23" is displayed at the bottom center.
* A logo is present at the bottom right.

### Slide 24

The image presents a comprehensive overview of Pulse Width Modulation (PWM) basics, featuring a graph and accompanying equations.

**Title:** "PWM: Basics"

**Graph:**

*   The graph displays two pulse width modulation waveforms with different duty cycles.
*   The x-axis represents time ($t$), and the y-axis represents voltage ($V(t)$).
*   The graph shows two pulses:
    *   A blue pulse with a 33% duty cycle
    *   A red pulse with a 50% duty cycle
*   The graph also labels several key parameters:
    *   $V_+$: The peak voltage of the pulses
    *   $t_h$: The high time or pulse width
    *   $t_l$: The low time
    *   $T_{PRF}$: The pulse repetition period, which is the time between the start of one pulse and the start of the next pulse

**Equations:**

*   **PRF (Pulse Repetition Frequency)**
    *   $PRF \equiv Pulse\ Repetition\ Frequency$
    *   $Square\ wave \Leftrightarrow f_{PRF} = \frac{1}{T_{PRF}}$
*   **DC (Duty Cycle)**
    *   $DC \equiv Duty\ Cycle = \%\ of\ time\ high$
    *   $= \frac{t_h}{T_{PRF}} = \frac{t_h}{t_h + t_l}$
*   **Average Value**
    *   $Can\ use\ LPF\ to\ keep\ average\ value:$
    *   $Value = DC \times V_+$

In summary, the image provides a detailed explanation of PWM basics, including the definition of PRF and duty cycle, as well as the calculation of the average value using a low-pass filter (LPF). The graph illustrates two PWM waveforms with different duty cycles, and the equations provide a mathematical representation of the concepts.

### Slide 25

The image presents a slide from a presentation on Pulse Width Modulation (PWM) and its applications. The title, "PWM: Use Cases," is prominently displayed in bold black text at the top left of the slide.

**Key Points:**

* **Cheap and dirty way to get from digital to analog**
	+ PWM output through low-pass filter
* **Far more efficient to drive transistors fully-on/fully-off (digital) instead of partly on (analog)**
	+ But very noisy - high frequency switching
* **Can encode information in PWM parameters, like duty cycle**
	+ *See ultrasound Lab*

**Circuit Diagram:**

A hand-drawn circuit diagram is situated on the right side of the slide, illustrating a PWM signal being filtered through a low-pass filter (LPF) to produce an analog output. The diagram consists of:

* A PWM signal source
* A resistor (R)
* A capacitor (C)
* An output voltage (Vout)

The diagram also includes various notes and equations, including:

* **Digital MOSFET**
	+ P = V.I = 0
* **Analog MOSFET**
	+ P = V.I ≠ 0

**Additional Notes:**

The slide features additional handwritten notes and equations, including:

* **PWM** (in blue)
* **LPF** (in red)
* **G-PIO** (in black)
* **Vout** (in blue)

The background of the slide is white, with a purple and black border at the top. A logo for the University of Cambridge is displayed in the bottom-right corner. The slide number, "25," is centered at the bottom of the slide.

### Slide 26

The image presents a comprehensive overview of PWM (Pulse Width Modulation) practical considerations, focusing on the fundamental trade-off between response time to change in duty cycle and the amount of ripple. The content is divided into two main sections: a graph illustrating the relationship between frequency and voltage, and a discussion on the practical implications of LPF (Low Pass Filter) in PWM applications.

**Graph Section:**

*   The graph on the left side of the image displays the relationship between frequency (f) and voltage (V). It features several key points:
    *   **DC + V_s**: The DC voltage plus the voltage source.
    *   **f_LPF**: The frequency of the Low Pass Filter.
    *   **2f_LPF**: Twice the frequency of the Low Pass Filter.
    *   **3f_LPF**: Three times the frequency of the Low Pass Filter.
    *   **Ripple**: The fluctuations in voltage.
*   The graph shows how the voltage changes with frequency, with the Low Pass Filter (LPF) represented by a green line. The LPF is used to smooth out the voltage fluctuations.

**Practical Considerations Section:**

*   The right side of the image features a graph showing the output voltage (V_out) over time (t) for a PWM signal with a 50% duty cycle and a 90% duty cycle. The graph highlights the response time to change in duty cycle and the amount of ripple.
*   The handwritten notes on the image discuss the trade-off between response time and ripple:
    *   **Fundamental Trade-off:** Response time to change in duty cycle vs. amount of ripple.
*   The notes also provide examples of situations where an LPF is not explicitly necessary:
    *   **Eg1) LED lighting:** You are the LPF.
    *   **Eg2) Motor control:** Motor inertia is the LPF.

**Additional Information:**

*   A URL is provided at the bottom of the image: https://everycircuit.com/circuit/6534191478734848
*   The image includes a logo in the bottom-right corner, which appears to be a shield with a red and yellow design.

In summary, the image provides a detailed explanation of the practical considerations of PWM, including the fundamental trade-off between response time and ripple, and the role of LPF in smoothing out voltage fluctuations. The examples provided illustrate situations where an LPF may not be necessary, such as in LED lighting and motor control applications.

### Slide 27

The image presents a comprehensive overview of Analog-to-Digital Converters (ADCs) and Digital-to-Analog Converters (DACs), which are crucial components in the field of electronics and computer science. The slide is divided into two main sections, each focusing on one of these converter types.

**ADCs and DACs**

*   **ADC (Analog to Digital Converter)**
    *   Definition: Analog to Digital Converter
    *   Function: Takes $V_{in}$ and quantizes it into N bits from $V_{ref-}$ to $V_{ref+}$
    *   Diagram: The diagram shows the ADC process, where $V_{in}$ is converted into digital form $D_{0..(N-1)}$. The reference voltages $V_{ref-}$ and $V_{ref+}$ are used for conversion.
    *   Resolution (Q) Formula: $Q = \frac{V_{ref+} - V_{ref-}}{2^N}$ [in Volts per Least Significant Bit (LSB)]
*   **DAC (Digital to Analog Converter)**
    *   Definition: Digital to Analog Converter
    *   Function: Takes N bits in and generates a $V_{out}$ linearly spaced between $V_{ref-}$ and $V_{ref+}$
    *   Diagram: The diagram illustrates the DAC process, where digital input $D_{0..(N-1)}$ is converted into an analog output $V_{out}$. The reference voltages $V_{ref+}$ and $V_{ref-}$ are used for conversion.

**Additional Notes**

*   The slide also mentions that the same idea applies in reverse, referring to Data Acquisition (DAQ) systems.
*   An example is provided: Analog $\rightarrow$ DAQ $\rightarrow$ PC, highlighting the role of DAQs in analog-to-digital conversion for computer processing.

In summary, the slide provides a detailed comparison of ADCs and DACs, including their definitions, functions, and diagrams. It also touches upon the concept of resolution in ADCs and the application of these converters in data acquisition systems.

### Slide 28

The slide, titled "Voltage Translation Interfacing (Digital to Digital)," presents a comprehensive overview of voltage translation interfacing in digital systems. The slide is divided into two main sections: a graphical representation of voltage levels and a list of bullet points explaining the concept.

**Graphical Representation:**

The graphical representation consists of five vertical bar graphs, each representing a different voltage level:

*   5-V TTL
*   5-V CMOS
*   3.3-VLVTTL
*   2.5-V CMOS
*   1.8-V CMOS

Each graph displays the following voltage levels:

*   **Vcc**: The supply voltage, represented by the top of each graph.
*   **VOH (Output High Voltage)**: The minimum voltage required for a logic high output.
*   **VIH (Input High Voltage)**: The minimum voltage required for a logic high input.
*   **Vt (Threshold Voltage)**: The voltage threshold for logic high and low.
*   **VIL (Input Low Voltage)**: The maximum voltage allowed for a logic low input.
*   **VOL (Output Low Voltage)**: The maximum voltage allowed for a logic low output.
*   **GND (Ground)**: The reference voltage, represented by the bottom of each graph.

The graphs are color-coded, with red indicating the output voltage and blue indicating the input voltage. Green squiggly lines represent the noise margin.

**Key Observations:**

*   The 5-V CMOS graph has a handwritten note indicating that it is "unacceptable" due to the low noise margin.
*   The graphs show that different voltage levels have different noise margins and voltage thresholds.

**Bullet Points:**

The slide includes two bullet points that provide additional information:

*   **Many sensor modules use digital interfacing, but with different voltage levels**: This point highlights the challenge of interfacing sensor modules with different voltage levels.
*   **E.g. Typical MCU = 3.3 V, Arduino = 5 V, 2.5 V and 1.8 V also common**: This point provides examples of common voltage levels used in microcontrollers (MCUs) and Arduino boards.

In summary, the slide provides a detailed graphical representation of voltage levels in digital systems and explains the challenges of voltage translation interfacing. The bullet points highlight the importance of considering voltage levels when interfacing sensor modules and provide examples of common voltage levels used in MCUs and Arduino boards.

### Slide 29

The image shows a lecture slide about voltage translation interfacing, specifically focusing on step-down voltage translation. The title of the slide is "Voltage Translation Interfacing: Step-Down".

*   The main points are:
    *   One direction step-down: Use voltage divider
        *   Note: GPIO inputs appear as capacitors. Forms RC time constant with divider resistors.

The circuit diagram shows:

*   A 5V input on the left side, which is connected to a 47 kΩ resistor.
*   The 47 kΩ resistor is connected to a 91 kΩ resistor, which is grounded.
*   The voltage output is taken from the connection between the two resistors and is labeled as 3.3V.
*   The circuit is connected to an Arduino output on the left and an STM32 input on the right.

The slide number is 29, and there is a logo in the bottom-right corner that appears to be a shield with a red and yellow design.

The handwritten notes on the slide are written in red and blue ink. The red notes read: "Note: GPIO inputs appear as capacitors. Forms RC time constant w/ divider resistors." The blue notes read: "Arduino Output" and "STM32 Input".

### Slide 30

The image presents a detailed lecture slide on "Voltage Translation Interfacing: Step-Up" with a focus on using MOSFETs for voltage level shifting. The slide is divided into sections, each providing specific information and diagrams to illustrate the concepts.

*   **Title and Bullet Points:**
    *   The title "Voltage Translation Interfacing: Step-Up" is prominently displayed at the top of the slide.
    *   A bullet point explains that a one-direction step-up can be achieved using a MOSFET with a pull-up resistor, noting signal inversion.
    *   A recall from Lab 1 highlights that a MOSFET works like a voltage-controlled switch.
    *   A note on signal inversion indicates that the signal gets digitally inverted, with 0 to 3.3V becoming 5V to 0V.

*   **Circuit Diagram:**
    *   A circuit diagram illustrates the use of an N-FET (N-type Field-Effect Transistor) with a pull-up resistor.
    *   The diagram shows:
        *   A 5.0V supply voltage
        *   A 100 kΩ pull-up resistor
        *   An N-FET connected to the output node ('O')
        *   A signal input ('I') with a 51 MΩ resistance
        *   A voltage source with 3.3V and 0V labels
    *   The diagram demonstrates how the pull-up resistor provides a default value of 5V to the output node ('O').

*   **Notes and Equations:**
    *   A note explains that the fall time is fast due to the NMOS being ON with very low resistance.
    *   Another note mentions that the rise time can be slow, depending on the pull-up resistance (Rpu).
    *   No specific equations are presented, but the diagram and text imply the relationship between the input signal, MOSFET operation, and output voltage.

*   **Additional Information:**
    *   The slide includes a logo in the bottom-right corner, indicating the University of Oxford.
    *   The number "30" is displayed at the bottom center of the slide, likely indicating the slide number.

In summary, the slide provides a comprehensive overview of using MOSFETs with pull-up resistors for voltage level shifting, specifically for step-up applications. It covers the basic principles, circuit diagrams, and notes on signal inversion and timing characteristics.

### Slide 31

The image presents a lecture slide focused on designing a PWM (Pulse Width Modulation) circuit driven by a 0 to 3.3 V digital output. The goal is to create a precision reference voltage from 0 to 12 V using an NMOS and RC filtering.

**Problem Statement:**

* Design a PWM circuit driven by a 0 to 3.3 V digital output that uses an NMOS and RC filtering to create a precision reference voltage from 0 to 12 V.
* Assume that you have a +12 V rail and an op-amp available for buffering.
* The response time to a change in duty cycle should not exceed 100 ms.

**Equations and Formulas:**

* $5 \tau \approx 100 \, \text{ms}$
* $5 \tau = 5RC$

**Circuit Diagram:**

The circuit diagram is hand-drawn and consists of:

* A PWM source connected to an NMOS transistor
* The NMOS transistor connected to a +12 V rail through a resistor $R_{pu} = 100k\Omega$
* The NMOS transistor connected to a resistor $R$ and a capacitor $C$ in series
* The output voltage $V_{out}$ is taken across the capacitor $C$

**Notes and Comments:**

* Changing and discharging have different time constants due to loading:
	+ Changing: $(R_{pu}+R)C$
	+ Discharging: $RC$
* Use a buffer or active filter to fix $\tau$

**Waveforms:**

The slide includes two waveforms:

* A PWM waveform with a duty cycle labeled as % DC
* A plot of $V_{out}$ versus time, showing the response to a change in duty cycle

**Additional Information:**

* A link to an EveryCircuit simulation: https://everycircuit.com/circuit/4681685731639296

### Slide 32

The slide is titled "Voltage Translation Interfacing: Bi-Directional" and features a white background with a purple and black border at the top.

**Title and Border**
- The title is in large, bold black text at the top of the slide.
- A purple and black border runs along the top of the slide.

**Bullet Points**
- Two bullet points are listed:
  - "Use MOSFET as shown"
  - "Use level-shifter IC"

**Circuit Diagram**
- A circuit diagram is shown to the right of the bullet points.
- The diagram consists of:
  - A circle with a MOSFET symbol inside, labeled "N-CHANNEL MOSFET (small signal)".
  - The MOSFET has three terminals labeled:
    - S (source)
    - D (drain)
    - G (gate)
  - Two 10K Ohm resistors are connected to the circuit, one on each side of the MOSFET.
  - Two arrows point to the left and right of the circuit, indicating bi-directional voltage translation.
  - The labels "LU" and "HU" are shown on either side of the circuit, with arrows pointing up.

**Image of Level-Shifter IC**
- A small image of a red circuit board with various components is shown below the circuit diagram.
- The board has several labels, including:
  - "HV1", "HV2", "HV3" (high voltage)
  - "LV1", "LV2", "LV3" (low voltage)
  - "GND" (ground)

**Footer**
- The number "32" is displayed at the bottom center of the slide.
- A small logo featuring a shield with a black and yellow design is located in the bottom-right corner.

### Slide 33

The slide is titled "4.3 – Passive Sensors and Techniques" and features a prominent image of a computer circuit board at the top. The circuit board image spans the width of the slide and showcases various shades of teal, with a purple and black gradient bar running across the top.

**Key Elements:**

* **Title:** "4.3 – Passive Sensors and Techniques" in large, bold black text
* **Slide Number:** "33" in small black text at the bottom center of the slide
* **Logo:** A small yellow shield logo with a red dragon and a black and white chevron is located in the bottom-right corner
* **Background:** White background

**Summary:** The slide appears to be part of a presentation on passive sensors and techniques, likely in the context of computer science or engineering. The circuit board image at the top adds a visual element to the slide, while the title and slide number provide context and organization. The logo suggests that the presentation may be affiliated with a specific institution or organization. Overall, the slide provides a clear and concise introduction to the topic of passive sensors and techniques.

### Slide 34

The slide is titled "Passive vs. Active Sensors" and compares the two types of sensors.

**Passive Sensors**

* The input is denoted as $x$ and the output is denoted as $y(f(x))$, with a function $f(x)$ in between.
* A physical value, $x$, changes a passive property of the device, $f(x)$. Examples of passive properties include:
  - Resistance
  - Capacitance
  - Inductance
  - Other passive properties: 
    - Dimensions 
    - Density 
    - Colour 
    - Temp. 
    - Mass 
    - Inertia 
    - etc.
* Requires conversion to voltage or current signal, $y$.
* A passive sensor module can include integrated signal conditioning.

**Active Sensors**

* The input is denoted as $x$ and the output is denoted as $y(x)$.
* A physical effect creates an output signal voltage or current, $y$, directly from a physical value, $x$.
* A physics principle couples $x$ and $y$. 
* Examples:
  - Piezoelectric material relates mechanical strain and voltage.
* May require external power to function (e.g., phototransistor).

### Slide 35

The image presents a comprehensive overview of passive sensor principles, focusing on the physical parameters that influence resistance (R), inductance (L), and capacitance (C). The title "Passive Sensor Principles" is prominently displayed at the top.

**Equations and Formulas:**

*   $R = \rho \frac{L}{A}$
*   $C = \varepsilon_0 \varepsilon_r \frac{A}{d}$
*   $L = \mu_0 \mu_r \frac{N^2A}{d}$

**Definitions:**

*   $\rho = resistivity$
*   $\varepsilon_0 = \text{Permitivity of Free Space}$
*   $\varepsilon_r = \text{Relative Permitivity} (>1)$
*   $\mu_0 = \text{Permeability of Free Space}$
*   $\mu_r = \text{Relative Permeability} (>1)$

**Diagrams and Descriptions:**

*   **Cylindrical Resistor:**
    *   A cylindrical object with a blue gradient, labeled as $R = \rho \frac{L}{A}$.
    *   The diagram illustrates the relationship between resistance, resistivity, length, and area.
*   **Potentiometer:**
    *   A hand-drawn diagram with a blue circle and a green line, accompanied by notes on how $L$ changes based on shaft angle.
    *   Described as a "Passive angle to resistance sensor" and an example of a strain gauge.
*   **Capacitor:**
    *   A hand-drawn diagram with a blue outline, red curved lines, and green text.
    *   Labeled as an example of an "Electret Microphone" with notes on how $d$ changes with applied sound and capacitance.
*   **Inductor:**
    *   A cylindrical object with blue lines and a gray core, labeled with parameters such as length ($l$), cross-sectional area ($A$), and number of turns ($N$).
    *   Described as primarily used in LVDT (high-precision position measuring) and proximity detection, specifically in Linear Variable Differential Transformers.

**Additional Notes:**

*   The slide number "35" is displayed at the bottom center.
*   A logo featuring a yellow and red shield is located in the bottom-right corner.

### Slide 36

The image presents a comprehensive overview of resistive sensing techniques, featuring two primary circuit configurations: Voltage Divider and Current Divider, alongside Bridge Circuit. The slide is divided into two main sections, each detailing a specific circuit type with its corresponding notes.

**Voltage Divider Circuit**

*   **Circuit Diagram:** The voltage divider circuit consists of two resistors (R1 and R2) connected in series, with an input voltage (Vin) applied across the combination. The output voltage (Vout) is taken across one of the resistors (R2).
*   **Notes:**
    *   Simple
    *   Low cost
    *   Good when Rx is large (i.e., Iox is low)
    *   Ix changes with Rx
    *   Nonlinear Vout to Rx
    *   Single-ended output
    *   Poor choice if Rx is low

**Current Divider Circuit**

*   **Circuit Diagram:** The current divider circuit comprises two resistors (R1 and R2) connected in parallel, with an input current (Iin) flowing into the node. The output current (Iout) is taken through one of the resistors (R2).
*   **Notes:**
    *   Simple
    *   Low cost
    *   Good when Rx is low (controlling Iin directly)
    *   Nonlinear Iout to Rx
    *   Single-ended
    *   Constant current source requires work
    *   Poor choice if Rx is large (requires too much V)

**Bridge Circuit**

*   **Circuit Diagram:** The bridge circuit consists of four resistors (R1, R2, R3, and R4) arranged in a diamond configuration, with an input voltage (Vin) applied across two opposite corners. The output voltage (Vout) is taken across the remaining two corners.
*   **Notes:**
    *   Wheatstone bridge benefits
    *   Select V or I configuration depending on magnitude of Rx
    *   More components (cost)
    *   Requires differential receiver

**Additional Information**

*   A footnote at the bottom of the slide clarifies that Rx represents the resistance being sensed.
*   An additional note suggests using a transimpedance amplifier (TIA) to take Iin and produce Vout.

In summary, the image provides a detailed comparison of voltage divider, current divider, and bridge circuits used in resistive sensing techniques, highlighting their characteristics, advantages, and limitations.

### Slide 37

The image presents a comprehensive overview of capacitive sensing techniques, featuring a white background with a purple gradient at the top. The title "Capacitive Sensing Techniques" is prominently displayed in bold black text.

**Main Points:**

* **Approaches to measuring C:**
	+ Oscillator-based
	+ Charge-based
	+ Wheatstone bridge (AC)
* **Equations and Formulas:**
	+ Q = CV
	+ C = ε/d
	+ Zc = 1/(jωC) = 1/(j2πfC)
* **Diagrams and Illustrations:**
	+ A hand approaching a grounded plate with a capacitor symbol
	+ A stack of colored plates (red, green, blue) with a sensor and shield
	+ A 3D illustration of a material between two plates
	+ A circuit diagram with resistors, capacitors, and voltage sources
* **Handwritten Notes:**
	+ Green handwriting: "Not certain", "usually force or 1/c or 1/d", "As finger approaches"
	+ Blue handwriting: "Reflect fringe cap. decreasing d", "Can determine how much of a material is stacked between two plates", "Er ↑ as material is added", "like phasor version of resistive Wheatstone bridge"

**Summary:**

The image provides a detailed explanation of capacitive sensing techniques, including approaches to measuring capacitance, equations, and diagrams. The handwritten notes add additional context and insights, highlighting the relationship between capacitance and material properties. Overall, the image presents a comprehensive overview of capacitive sensing techniques, making it a valuable resource for those interested in understanding this topic.

### Slide 38

The slide is titled "Inductive Sensing Techniques" and features a white background with a purple and black border at the top.

**Bullet Points:**

* Inductors are active sensors if sensing a changing magnetic field (Faraday's Law)
* Passive sensing:
* Inductance to Digital Converter IC (LDC) does the heavy lifting
* Senses change in LC resonant frequency

**Equations and Formulas:**

* $f_{ox} \propto \frac{1}{\sqrt{LC}}$ (written in blue handwriting)

**Graph:**

A graph is displayed on the left side of the slide, showing:
* The x-axis labeled "Frequency (MHz)" ranging from 1 to 100
* The y-axis labeled "Gain (dB)" ranging from 20 to 100
* Two curves are plotted: one red and one green
* A purple box with text: "Material interrupts magnetic field, lowers L, increases resonant frequency"

**Diagrams:**

Two diagrams are shown on the right side of the slide:
* **Axial Sensing:** A gray rectangular prism with a green base, featuring an orange spiral pattern. A red arrow points to the top of the prism, indicating a change in distance (Δ μr).
* **Event Counting:** A gear with a red arrow, placed on a green base with an orange spiral pattern.

**Additional Elements:**

* A URL is provided at the bottom of the slide: https://www.ti.com/lit/an/snoa954d/snoa954d.pdf
* A logo is displayed in the bottom-right corner, featuring a yellow shield with a red dragon and a black and white chevron.

### Slide 39

The image presents a detailed lecture slide focused on the problem of a capacitive sensor and Wheatstone bridge. The slide is divided into several sections, each providing specific information about the circuit and the calculations involved.

**Title and Circuit Diagram**

*   The title "Problem: Capacitive Sensor and Wheatstone Bridge" is prominently displayed at the top of the slide.
*   A circuit diagram is provided, illustrating the configuration of the capacitive sensor and Wheatstone bridge. The diagram includes various components such as resistors (R1, R2, RG), capacitors (C1, Cx), and voltage sources (Vin, Vout).

**Equations and Formulas**

*   The slide includes several equations and formulas related to the circuit, including:
    *   $C_x = 160 + 0.34(RH-5) [pF]$
    *   $Z_{Cx} = \frac{1}{j \omega C_x} = \frac{1}{j \cdot 2\pi \cdot f_0 \cdot C_x}$
    *   $V_+ = V_{in} \cdot \frac{Z_C}{Z_C+R} = 1 \times \frac{-j9.95}{-j9.95+10} = 0.705 \angle -45^\circ V_{pk-pk}$
    *   $V_- @ 55\% RH = 1 \times \frac{-j8.99}{-j8.99+10} = 0.669 \angle -4^\circ V_{pk-pk}$
    *   $V_- @ 95\% RH = 0.641 \angle -50^\circ V_{pk-pk}$

**Given Parameters and Objectives**

*   The slide lists the given parameters:
    *   $C_x$ is a humidity sensor with a capacitance of 160 pF at 5% RH and a sensitivity of $\Delta C_x / \%RH = 0.34 [pF/\%RH]$.
    *   $V_{in} = 1 V_{pk-pk}$ at 100 kHz, $R_1 = R_2 = 10 k\Omega$, and $C_1 = 160 pF$.
*   The objectives are to:
    *   Determine $\Delta v = V_+ - V_-$ at 5%, 55%, and 95% RH.

**Handwritten Notes and URLs**

*   The slide includes handwritten notes in blue and red ink, which appear to be calculations and annotations related to the problem.
*   Two URLs are provided at the bottom of the slide:
    *   https://everycircuit.com/circuit/5389244734111744
    *   https://www.digikey.ca/en/products/detail/te-connectivity-measurement-specialties/HPP801A031/697731

Overall, the slide provides a comprehensive overview of the problem, including the circuit diagram, equations, and given parameters. The handwritten notes and URLs suggest that the slide is part of a lecture or tutorial on capacitive sensors and Wheatstone bridges.

### Slide 40

The slide contains the following content:

* A title: **4.4 – Active Sensors and Techniques**
* A slide number: **40**
* A logo in the bottom-right corner, which appears to be a shield with a yellow and orange color scheme, featuring a red dragon and other designs.

The background of the slide features:
* A purple and black bar at the top
* A white section below the top bar, containing the title and slide number
* An image of a circuit board at the top of the slide, featuring teal-colored lines and silver dots on a dark background.

There are no equations, formulas, definitions, or bullet points on this slide. The slide appears to be a title slide for a section on active sensors and techniques, likely in a presentation related to computer science or engineering.

### Slide 41

The image presents a slide from a presentation on active sensor principles, featuring a clear and organized layout. The title, "Active Sensor Principles," is prominently displayed in bold black text at the top of the slide.

**Main Points:**

* **Definition of Active Sensors:** 
  - Active sensors rely on physics principles that couple sensor input and electrical domain.
  - Possibly through intermediate domains.

* **Common Effects Used in Active Sensors:** 
  - Hall Effect
  - Electromagnetic Effect
  - Thermoelectric Effect
  - Piezoelectric Effect
  - Photoelectric Effect
  - Photovoltaic Effect

**Handwritten Notes:**

* A handwritten note in blue ink explains the concept of active sensing, distinguishing it from passive sensing. It highlights that active sensing involves applying energy to the environment to make sensing easier.
* Examples are provided to illustrate the difference between active and passive sensing, including:
  - Night vision vs. turning on a light
  - Ultrasound medical imaging, which sends out waves and senses the echoes

**Additional Information:**

* A small logo is present in the bottom-right corner of the slide, featuring a yellow shield with a red and black design.
* The background of the slide is white, with a purple and pink gradient bar at the top.

### Slide 42

The image presents a comprehensive overview of the Hall Effect, a fundamental concept in physics and engineering. The slide is divided into three main sections: Principle, Applications, and Use Cases.

**Principle**

*   **Current through long conductor**
    *   The Hall Effect is based on the interaction between a current-carrying conductor and a magnetic field.
*   **Transverse external magnetic field pushes e- against one side or the other**
    *   When a magnetic field is applied perpendicular to the current flow, it exerts a force on the electrons, causing them to accumulate on one side of the conductor.
*   **Difference in surface potentials proportional to magnetic field**
    *   The accumulation of electrons on one side of the conductor creates a potential difference between the two sides, which is directly proportional to the strength of the magnetic field.
*   **Magnetic Field → Force on e- → Voltage**
    *   The magnetic field induces a force on the electrons, leading to a voltage difference between the two sides of the conductor.
*   **(H → F → V)**
    *   The Hall Effect can be represented by the sequence: Magnetic Field (H) → Force (F) → Voltage (V).

**Applications**

*   **Proximity sensing, positioning, speed detection, current sensing**
    *   The Hall Effect is widely used in various applications, including proximity sensing, positioning, speed detection, and current sensing.

**Use Cases**

*   **Car shaft speed sensors, power supply current sensors, brushless DC electric motors**
    *   The Hall Effect is used in various applications, such as car shaft speed sensors, power supply current sensors, and brushless DC electric motors.

**Diagram**

*   A diagram is provided to illustrate the Hall Effect, showing a conductor with a current flowing through it and a magnetic field applied perpendicular to the current flow.
*   The diagram labels the following components:
    *   **B**: Magnetic field
    *   **Constant current**: The current flowing through the conductor
    *   **Hall element**: The region where the Hall Effect occurs
    *   **V Hall**: The voltage difference between the two sides of the conductor
    *   **I Hall**: The current flowing through the Hall element

**Additional Information**

*   A link to a website is provided at the bottom of the slide: https://www.digikey.ca/en/blog/hall-effect-sensor-basics
*   The slide number is 42, indicating that this is part of a larger presentation.

### Slide 43

The image presents a slide from a presentation on the electromagnetic effect, specifically focusing on the principle and applications of electromagnetic induction.

*   **Electromagnetic Effect**
    *   **Principle**
        *   "Electromagnetic Induction"
        *   Changing Magnetic Flux → Voltage
        *   $V = -\frac{d\Phi_B}{dt}$
        *   $\Phi_B$ is the B-field passing through an area
    *   **Applications**
        *   Proximity/position sensing, EM field sensing
    *   **Use Cases**
        *   Antennas, motion control, traffic sensing, spring compression sensing, flow and level sensing

The slide features a diagram illustrating a high-frequency magnetic field interacting with a target metal object. The diagram consists of:

*   A light blue rectangle representing the sensing coil
*   A white rectangle within the coil labeled "Internal circuit"
*   A dashed line indicating the high-frequency magnetic field
*   A metal target object positioned near the coil

The diagram is accompanied by labels and arrows that provide additional context:

*   The metal target object is labeled as "Target (Metal)"
*   The sensing coil is connected to the internal circuit
*   The high-frequency magnetic field is depicted as a dashed line surrounding the coil and target object

The slide also includes a URL at the bottom left corner: https://www.keyence.ca/ss/products/sensor/sensorbasics/proximity/info/

Overall, the slide effectively conveys the fundamental principle of electromagnetic induction and its various applications, along with a visual representation of how it works in a specific context.

### Slide 44

The image presents a comprehensive overview of the thermoelectric effect, including its principles and applications.

* **Thermoelectric Effect**
	+ **Principle**
		- Temperature Difference → Voltage
		- Seebeck effect:
			- ΔT → e- from hot to cold, ΔV
		- Peltier effect:
			- +/- heat when current through junction of different materials
			- e-/h+ generation or recombination
		- Thomson effect:
			- Create ΔT in a material to cause Peltier effect across gradient
* **Applications**
	+ Temperature sensing, energy harvesting, solid-state heating/cooling
* **Use Cases**
	+ Space power applications, thermoelectric heaters and coolers, thermocouples, IR detectors

The image provides a concise and informative summary of the thermoelectric effect, its underlying principles, and its various applications. The use cases listed highlight the diverse range of fields where this technology can be applied, from space exploration to temperature sensing and energy harvesting. Overall, the image effectively communicates the key concepts and potential uses of the thermoelectric effect. 

There are no diagrams or images on the slide. 

The slide number is 44. 

There is a link to a YouTube video at the bottom left: https://www.youtube.com/watch?v=PccE4WcfnAw 

There is a university logo at the bottom right.

### Slide 45

The slide provides an overview of the **Piezoelectric Effect**, which is a phenomenon where mechanical stress generates an electric voltage.

### **Principle**

The fundamental principle behind the piezoelectric effect is:
- **Mechanical stress → Voltage**

### **Applications**

The applications of the piezoelectric effect include:
- **Pressure, acceleration, strain, and force sensors**
- **Actuators**
- **Energy harvesting**

### **Use Cases**

Some specific use cases of the piezoelectric effect are:
- **Medical imaging (ultrasound)**
- **Non-Destructive Testing (NDT)**
- **Timekeeping**
- **Inkjet printers**
- **Vibration control**
- **Proximity sensing**

### **Diagram Descriptions**

The slide features three diagrams illustrating the piezoelectric effect under different conditions:

1. **Equilibrium State** ($\varepsilon = 0$):
   - The diagram shows a series of dipoles (represented by springs with a plus and minus sign on either end) arranged randomly.
   - There is no net electric field or polarization.
   - The dipoles are not aligned, and there is no external stress applied.

2. **Positive Strain** ($\varepsilon > 0$):
   - The diagram depicts the dipoles aligning under positive strain (expansion).
   - The distance $d$ increases to $d + \Delta d$.
   - The dipoles become more aligned, generating a positive electric field.

3. **Negative Strain** ($\varepsilon < 0$):
   - The diagram shows the dipoles under negative strain (compression).
   - The distance $d$ decreases to $d - \Delta d$.
   - The dipoles become more aligned in the opposite direction, generating a negative electric field.

### **Additional Information**

- The slide includes a URL at the bottom: **https://www.digikey.ca/en/articles/the-basics-of-applying-ultrasonic-transducers-for-sensing-objects-or-fluid-flow**
- The slide number is **45**.
- A logo is present in the bottom-right corner, likely representing an institution (though not specified).

### Slide 46

The image presents a slide from a presentation on the photoelectric effect, featuring a diagram and text that explain the principle, applications, and use cases of this phenomenon.

*   **Title**
    *   The title of the slide is "Photoelectric Effect" in bold black text.
*   **Principle**
    *   The principle of the photoelectric effect is described as: Photon → free e-
*   **Applications**
    *   The applications of the photoelectric effect include:
        *   Photomultiplier tubes
        *   Photoelectron spectroscopy
        *   Displays
        *   Light sensors
*   **Use Cases**
    *   The use cases of the photoelectric effect include:
        *   Medical imaging (PET)
        *   Optical encoders
        *   Presence/absence light meters
*   **Diagram**
    *   A diagram on the right side of the slide illustrates the photoelectric effect, showing:
        *   A gray rectangle with green and orange spheres inside
        *   A wavy blue line representing a photon entering the rectangle
        *   Three black arrows pointing upwards, indicating the ejection of electrons
        *   Three orange spheres outside the rectangle, representing the ejected electrons

The slide provides a concise overview of the photoelectric effect, its principle, applications, and use cases, accompanied by a diagram that visualizes the process.

### Slide 47

The image presents a comprehensive overview of the photovoltaic effect, its principle, applications, and use cases. The main points are:

* **Photovoltaic Effect**
	+ Title of the slide
* **Principle**
	+ Photon → e- h+ generation
* **Applications**
	+ Energy production, light sensors, photodiodes, imaging
* **Use Cases**
	+ Solar panels, digital cameras

The slide also features a diagram illustrating the photovoltaic effect, which includes:

* A cross-sectional view of a solar cell with labeled components:
	+ Front electrical contact
	+ N-type
	+ Depletion zone
	+ P-type
	+ N-type
* Arrows indicating electron flow and hole movement
* A yellow arrow representing photon absorption
* A logo for G2V in the bottom-right corner

The diagram shows the process of photon absorption, electron-hole pair generation, and the flow of electrons and holes through the solar cell. The slide provides a clear and concise introduction to the photovoltaic effect, its underlying principles, and its practical applications. 

At the bottom of the slide, there is a link to a website: https://g2voptics.com/photovoltaics-solar-cells/theory-of-solar-cells/. The slide number is 47. In the bottom-right corner, there is a logo that appears to be a university crest.

### Slide 48

The slide contains a simple graphic and text.

* The text "Thanks!" is written in bold, black font at the top left corner of the slide.
* A large, black graphic of a hand giving a thumbs up is drawn in the center of the slide. The thumb is pointing upwards, and the other fingers are curled under. A long arrow extends from the thumb up and to the right.
* A small, black number "48" is centered at the bottom of the slide.
* A logo is present in the bottom-right corner of the slide. The logo features a yellow shield with a red design on it, and a black and white chevron pattern.
* A purple and lavender gradient line runs across the top of the slide.

