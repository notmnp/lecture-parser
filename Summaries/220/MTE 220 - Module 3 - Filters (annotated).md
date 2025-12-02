# MTE 220 - Module 3 - Filters (annotated)

## Study Notes

# Filters & Laplace Analysis – Problem‑Solving Exam Notes  

---

## Core Formulas & Definitions  

| # | Formula | Symbols | When to Use |
|---|---------|---------|-------------|
| 1 | **Laplace Transform** | $$V(s)=\displaystyle\int_{0}^{\infty}v(t)\,e^{-st}\,dt$$ | Convert time‑domain signals to \(s\)-domain |
| 2 | **Inverse Laplace** | $$v(t)=\displaystyle\frac{1}{2\pi j}\int_{\gamma-j\infty}^{\gamma+j\infty}V(s)\,e^{st}\,ds$$ | Recover \(v(t)\) |
| 3 | **Fourier Transform** | $$V(j\omega)=\displaystyle\int_{-\infty}^{\infty}v(t)\,e^{-j\omega t}\,dt$$ | Steady‑state analysis (\(\sigma=0\)) |
| 4 | **Impedances** | $$Z_C=\frac{1}{sC},\qquad Z_L=sL$$ | Replace \(R,\!C,\!L\) in the \(s\)‑domain |
| 5 | **Voltage Divider** | $$V_{\text{out}}=V_{\text{in}}\frac{Z_2}{Z_1+Z_2}$$ | Node voltage in linear circuits |
| 6 | **Passive RC LPF** | $$H_{\text{LPF}}(s)=\frac{1}{1+sRC}$$ | Series RC, output across \(C\) |
| 7 | **Passive RC HPF** | $$H_{\text{HPF}}(s)=\frac{sRC}{1+sRC}$$ | Series RC, output across \(R\) |
| 8 | **RC Band‑Pass** | $$H_{\text{BP}}(s)=\frac{sR_1C_1}{s^2R_1R_2C_1C_2+s(R_1C_1+R_2C_2+R_1C_2)+1}$$ | Cascaded first‑order stages |
| 9 | **RC Band‑Reject** | $$H_{\text{BR}}(s)=1-H_{\text{HPF}}(s)H_{\text{LPF}}(s)$$ | Summing LPF+HPF |
|10 | **Active RC LPF (inverting)** | $$H_{\text{ARCLPF}}(s)=-\frac{R_f}{R_i}\frac{1}{1+sR_fC_f}$$ | Feedback \(R_f\), input \(R_i\) |
|11 | **Active RC HPF (inverting)** | $$H_{\text{ARCHPF}}(s)=-\frac{R_f}{R_i}\frac{sR_iC_i}{1+sR_iC_i}$$ | Series \(C_i\)–\(R_i\) to ground |
|12 | **Active Band‑Pass** | $$H_{\text{ARP}}(s)=-\frac{R_f}{R_i}\frac{sC_i}{1+sR_iC_i}\frac{1}{1+sR_fC_f}$$ | HPF + LPF cascade |
|13 | **Resonant Frequency (LC)** | $$\omega_0=\frac{1}{\sqrt{LC}}$$ | Natural oscillation |
|14 | **General 2nd‑order TF** | $$H(s)=\frac{\omega_0^2}{s^2+2\alpha s+\omega_0^2}
      =\frac{\omega_0^2}{s^2+2\zeta\omega_0 s+\omega_0^2}
      =\frac{\omega_0^2}{s^2+\frac{\omega_0}{Q}s+\omega_0^2}$$ | Any 2nd‑order LTI system |
|15 | **Pole Locations** | $$s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}
          =-\zeta\omega_0\pm j\omega_0\sqrt{1-\zeta^2}$$ | Transient behavior |
|16 | **Damping–Q Relations** | 
$$
\omega_0=\sqrt{\omega_1\omega_2},\quad
BW=\omega_2-\omega_1=\frac{\omega_0}{Q}=2\alpha,\quad
\alpha=\frac{\omega_0}{2Q},\quad
\zeta=\frac{1}{2Q}
$$ | Map bandwidth, Q, damping |
|17 | **RLC Series TFs** | 
$$
\begin{aligned}
H_{\text{LP}}(s)&=\frac{1}{s^2+\frac{R}{L}s+\frac{1}{LC}}\\
H_{\text{HP}}(s)&=\frac{s^2}{s^2+\frac{R}{L}s+\frac{1}{LC}}\\
H_{\text{BP}}(s)&=\frac{s\frac{R}{L}}{s^2+\frac{R}{L}s+\frac{1}{LC}}\\
H_{\text{BS}}(s)&=\frac{1}{s^2+\frac{R}{L}s+\frac{1}{LC}}
\end{aligned}
$$ | Design of passive RLC filters |
|18 | **Parallel RLC TF** | $$H_{\text{par}}(s)=\frac{R}{R+sL+\frac{1}{sC}}=\frac{1}{1+s\frac{R}{L}+\frac{1}{sRC}}$$ | Parallel circuit, output across \(V_{out}\) |
|19 | **Parallel RLC Q** | $$Q=\omega_0 R C,\quad\omega_0=\frac{1}{\sqrt{LC}}$$ | Quality factor in parallel |
|20 | **Bode Magnitude** | $$M_{\text{dB}}(\omega)=20\log_{10}\lvert H(j\omega)\rvert$$ | Plot magnitude |
|21 | **Bode Phase** | $$\angle H(j\omega)=\tan^{-1}\!\frac{\Im\{H(j\omega)\}}{\Re\{H(j\omega)\}}$$ | Plot phase |
|22 | **Factor Magnitude (dB)** | $$\bigl|s/\omega_c\bigr|_{\text{dB}}=20\log_{10}\!\bigl(\omega/\omega_c\bigr)$$ | Zero at origin |
|23 | **Factor Phase** | \(\angle(s/\omega_c)=+90^\circ,\ \angle(1/s)=-90^\circ\) | Pole/zero at origin |
|24 | **Step Response (LPF)** | $$y(t)=K\bigl(1-e^{-t/\tau}\bigr)u(t),\quad \tau=\frac{1}{\omega_c}$$ | First‑order LPF |
|25 | **Step Response (HPF)** | $$y(t)=K\,e^{-t/\tau}u(t),\quad \tau=\frac{1}{\omega_c}$$ | First‑order HPF |
|26 | **Bode Slope Rules** | • One pole: –20 dB/dec<br>• One zero: +20 dB/dec<br>• Complex‑conjugate pair: ±40 dB/dec near resonance | Asymptote construction |
|27 | **Constant Passband Gain** | \(A(s)=A_{\text{PB}}\cdot(\text{other factors})\) | Vertical shift only |
|28 | **Zero at Origin** | \(A(s)=s\tau_0\) | +20 dB/dec slope, +90° phase |
|29 | **Real Zero** | \(A(s)=1+s\tau_z=1+j\omega\tau_z\) | +20 dB/dec after \(\omega_z\), phase rises from 0° to +90° |
|30 | **Real Pole** | \(A(s)=1/(1+s\tau_p)=1/(1+j\omega\tau_p)\) | –20 dB/dec after \(\omega_p\), phase falls from 0° to –90° |
|31 | **Example TF** | \(A(s)=\dfrac{s+100}{(s+1)(s+10\,000)}\) | Four‑factor Bode sketch (zero & two poles) |

---

## Key Concepts & Intuition  

- **Domain Shift** – \(s=\sigma+j\omega\):  
  * \(\sigma>0\): transient decay.  
  * \(\sigma=0\): steady‑state frequency response (Fourier).  

- **Impedance Trends** – \(Z_C=1/(sC)\) drops with \(\omega\); \(Z_L=sL\) rises.  

- **Transfer Function** – \(H(s)=Y(s)/X(s)\).  
  * **Poles** → natural decay; **zeros** → frequency shaping.  
  * **Order** of the denominator dictates complexity.  

- **First‑Order Filters** – One pole or zero.  
  * **Passive**: no gain.  
  * **Active**: multiply by \(-R_f/R_i\) (inverting) or \(1+R_f/R_i\) (non‑inverting).  

- **Zero at Origin** – Adds +20 dB/dec and +90° phase for all \(\omega\).  

- **Real Zero** – Starts flat at 0 dB, then slopes +20 dB/dec after \(\omega_z=1/\tau_z\).  
  Phase rises from 0° to +90° over the transition band.  

- **Real Pole** – Starts flat at 0 dB, then slopes –20 dB/dec after \(\omega_p=1/\tau_p\).  
  Phase falls from 0° to –90°.  

- **Second‑Order Circuits** – Two poles create resonance.  
  * \(\zeta=1/(2Q)\).  
  * Bandwidth \(BW=\omega_0/Q\).  
  * Peak magnitude ≈ \(20\log_{10}Q\) dB at \(\omega_0\).  

- **Bode Sketching Rules** – Each pole/zero changes slope by ±20 dB/dec; complex pair ±40 dB/dec near resonance.  

- **Constant Gain** – Shifts the whole magnitude plot by \(20\log_{10}K\) dB, no phase effect.  

- **High‑Q vs Low‑Q** –  
  * **High‑Q** (sharp band‑pass): use a single higher‑order stage.  
  * **Low‑Q**: cascade separate LPF + HPF.  

---

## Problem‑Solving Strategies  

### 1.  Derive a Transfer Function  

| Cue | Checklist | Common Mistakes |
|-----|-----------|-----------------|
| “Find \(H(s)\)” | 1. Convert the circuit to the \(s\)-domain.<br>2. Use node‑ or mesh‑analysis to write \(V_{\text{out}}/V_{\text{in}}\).<br>3. Express as a rational function \(K\prod(s+a_i)/\prod(s+b_j)\).<br>4. Cancel common factors before simplifying. | Ignoring component signs; mis‑placing series/parallel elements. |

### 2.  Calculate Cut‑off / Resonant Frequencies  

| Filter | Formula | Notes |
|--------|---------|-------|
| RC LPF/HPF | \(\omega_c=\frac{1}{RC}\) | \(f_c=\omega_c/2\pi\) |
| LC / RLC | \(\omega_0=\frac{1}{\sqrt{LC}}\) | No \(R\) dependence |
| Parallel RLC | \(\omega_0=\frac{1}{\sqrt{LC}},\ Q=\omega_0RC\) | Use given \(R\) to solve for \(L,C\) |
| Band‑Pass (RC) | \(f_L=\frac{1}{2\pi R_1C_1}\), \(f_H=\frac{1}{2\pi R_2C_2}\), \(f_0=\sqrt{f_L f_H}\) | |

**Parallel RLC Design** – Given \(f_0,\,Q,\,R\):  

1. \(\omega_0=2\pi f_0\).  
2. \(C=\dfrac{Q}{\omega_0 R}\).  
3. \(L=\dfrac{1}{\omega_0^2 C}\).  

### 3.  Sketch a Bode Plot (Factored TF)  

1. **List** all poles, zeros, and constant gain \(K\).  
2. **Magnitude**  
   * Start at \(20\log_{10}K\) dB.  
   * Add ±20 dB/dec for each pole/zero.  
   * Near \(\omega_c\), apply ±3 dB correction for the first break.  
3. **Phase**  
   * 0° for constant term.  
   * +90° per zero, –90° per pole.  
   * Transition over \([0.1\omega_c,10\omega_c]\).  
4. For a second‑order pair, add ±40 dB/dec near resonance.  

### 4.  Solve Time‑Domain Step/Impulse Response  

1. Multiply \(H(s)\) by \(1/s\) for a step input.  
2. Inverse Laplace using standard forms.  
3. For 2nd‑order:  
   $$y(t)=K\Bigl(1-e^{-\alpha t}\!\bigl[\cos(\omega_dt)+\tfrac{\alpha}{\omega_d}\sin(\omega_dt)\bigr]\Bigr)u(t)$$  
4. Always attach \(u(t)\) for causality.  

### 5.  Analyze Real Zero / Pole Bode Features  

| Transfer | Magnitude (dB) | Phase | Transition Frequency |
|----------|----------------|-------|----------------------|
| Real Zero: \(1+s\tau_z\) | \(10\log_{10}\!\bigl[1+(\omega/\omega_z)^2\bigr]\) | \(\tan^{-1}(\omega/\omega_z)\) | \(\omega_z=1/\tau_z\) |
| Real Pole: \(\frac{1}{1+s\tau_p}\) | \(-10\log_{10}\!\bigl[1+(\omega/\omega_p)^2\bigr]\) | \(-\tan^{-1}(\omega/\omega_p)\) | \(\omega_p=1/\tau_p\) |
| Zero at Origin: \(s\tau_0\) | \(-20\log_{10}(\omega/\omega_0)\) | \(-90^\circ\) | All \(\omega>0\) |

Use these formulas to calculate exact dB/phase points and to verify hand‑sketched Bode lines.

### 6.  Design RC or RLC Filters  

1. Select target \(f_c\) or \(f_0\).  
2. Pick convenient \(R\) (e.g., 10 kΩ).  
3. Compute \(C\) or \(L\) from the corresponding formula.  
4. Check tolerance impact on \(f_c\) and \(Q\).  

### 7.  Build Active First‑ or Second‑Order Filters  

* **Gain** – Inverting: \(A=-Z_f/Z_i\); Non‑inverting: \(A=1+Z_f/Z_i\).  
* **Pole placement** – Put \(C\) in the feedback branch for LPF, or in the input branch for HPF.  
* **Zero at origin** – Insert a \(C\) in the branch opposite the pole.  
* **Band‑Pass** – Cascade inverting HPF and LPF.  
* **Notch/Reject** – Parallel LPF + HPF with summing; or single‑op‑amp notch using \(C\) in parallel with \(R\).  

### 8.  Evaluate Attenuation / Noise Rejection  

1. Identify noise frequency \(f_n\).  
2. Compute \(|H(j2\pi f_n)|\) (dB).  
3. Ensure attenuation meets specification (e.g., ≥ 40 dB).  

### 9.  Example Bode Sketch – \(A(s)=\frac{s+100}{(s+1)(s+10\,000)}\)  

1. **Constant factor**: \(K=\frac{100}{10\,000}=0.01=-40\) dB.  
2. **Poles** at \(-1\) rad/s and \(-10\,000\) rad/s:  
   * Start at –40 dB.  
   * Slope –20 dB/dec after 1 rad/s (first pole).  
3. **Zero** at \(-100\) rad/s:  
   * Slope +20 dB/dec after 100 rad/s (cancels first pole).  
4. **Resulting slope**:  
   * –20 dB/dec from 1 to 100 rad/s.  
   * 0 dB/dec from 100 to 10 000 rad/s.  
   * –20 dB/dec after 10 000 rad/s.  
5. **Phase**:  
   * 0° before 1 rad/s.  
   * –45° at 1 rad/s, –90° after 1 rad/s.  
   * +45° around 100 rad/s, 0° after 100 rad/s.  
   * –45° around 10 000 rad/s, –90° after.  

---

## Common Pitfalls & Checks  

| Issue | Quick Check | Fix |
|-------|-------------|-----|
| Mixing \(s\) & \(j\omega\) | Are you evaluating \(H(j\omega)\) only for steady‑state? | Use \(s=j\omega\) only in Bode plots. |
| Wrong sign for \(Z_L\) | Is \(Z_L=sL\) or \(-sL\)? | Confirm passive sign convention. |
| Zero at origin missed | Did you include the factor \(s\) in the numerator? | Adds +20 dB/dec slope. |
| Units mismatch | Are \(\omega\) rad/s, \(f\) Hz? | Convert \(f=\omega/(2\pi)\). |
| Constant gain omitted | Did you shift magnitude by \(20\log_{10}K\)? | Add vertical offset. |
| Slope change errors | Does each pole/zero change slope by ±20 dB/dec? | Re‑count. |
| Step response missing \(u(t)\) | Is the response causal? | Include \(u(t)\). |
| Parallel RLC Q wrong | Use \(Q=\omega_0RC\) (parallel) not \(Q=\frac{R}{\sqrt{L/C}}\). | Re‑derive. |
| High‑Q design too narrow | Check \(f_H/f_L\) ratio < 4 → consider higher order. | Upgrade filter order. |
| Loading ignored | Did you buffer the filter? | Use high‑impedance buffer. |

--- 

### Cheat‑Sheet Highlights  

- **Resonance:** \(\omega_0=1/\sqrt{LC}\).  
- **Q (Parallel):** \(Q=\omega_0RC\).  
- **Q (Series):** \(Q=\omega_0L/R\).  
- **Bandwidth:** \(BW=\omega_0/Q\).  
- **Pole/Zero Bode Effect:** ±20 dB/dec per pole/zero; ±40 dB/dec for complex pair.  
- **Zero at Origin:** +20 dB/dec, +90° phase.  
- **Constant Gain:** Vertical shift only.  

Use this compact framework to identify the problem type, apply the right formulas, and avoid the most frequent errors. Good luck on the exam!

---

## Raw Slide Summaries

### Slide 1

The image presents a slide from a presentation, likely used in an educational setting, specifically for the course "MTE 220 - Sensors and Instrumentation" at the University of Waterloo's Faculty of Engineering.

**Title and Course Information**

* The title "Module 3" is prominently displayed in large black text on the left side of the slide.
* Below the title, the word "Filters" is written in slightly smaller but still bold black text.
* Further down, the course code and name "MTE 220 - Sensors and Instrumentation" are provided in gray text.

**University Logo and Faculty Information**

* At the bottom-left corner of the slide, the University of Waterloo's logo is visible, featuring a shield with a red and gold design.
* Adjacent to the logo, the text "UNIVERSITY OF WATERLOO" appears in black, followed by "FACULTY OF ENGINEERING" in the same color, separated by a vertical black line.

**Background and Design Elements**

* The background of the slide is divided into two distinct sections:
	+ The left side features a white background with a black bar at the top, accompanied by a purple stripe underneath.
	+ The right side showcases a close-up image of a circuit board, characterized by its dark background and teal-colored circuitry. The image is overlaid with various components, including silver dots and circular patterns.

Overall, the slide effectively conveys the topic and context of the presentation, while also incorporating the university's branding and visual identity.

### Slide 2

The image presents a slide from a presentation on Laplace Domain Analysis, featuring a title and a background image of a circuit board.

* The top section of the slide is dominated by a large image of a circuit board, which serves as the background.
	+ The circuit board is depicted in shades of teal and black, with various components and pathways visible.
	+ The image occupies the top two-thirds of the slide.
* Below the circuit board image, the title "3.1 - Laplace Domain Analysis" is prominently displayed in bold black font.
	+ The title is centered and takes up approximately one-third of the slide's height.
* At the bottom of the slide, the number "2" is printed in small black text, indicating that this is the second slide in the presentation.
	+ The number is centered and appears below the title.
* In the bottom-right corner of the slide, a small logo is visible.
	+ The logo features a yellow shield with a red design inside, although the exact details are not clear due to its small size.

In summary, the slide effectively conveys the topic of Laplace Domain Analysis through its title and background image of a circuit board, while also providing context with the slide number and logo.

### Slide 3

The image is a lecture slide titled "Premise" in bold, black font at the top-left corner. The slide has a white background with a purple and black header.

*   **Title and Header**
    *   The title "Premise" is displayed prominently.
    *   The header features a gradient that transitions from light purple to dark purple, accompanied by a black border at the top.
*   **Main Content**
    *   The main content is divided into bullet points, which discuss the limitations of the time domain and the benefits of using the Fourier domain for analysis.
    *   The first point highlights the complexity of calculus in the time domain, stating that it "inhibits insight and analysis."
    *   The second point explains that the Fourier domain simplifies things for linear systems by utilizing impedance.
    *   The third point outlines two problems:
        *   The presence of many "j"s complicates expressions.
        *   Sinusoids persist indefinitely, but real signals and systems do not.
    *   The fourth point presents the Laplace Domain as a solution to these problems.
*   **Diagram**
    *   A diagram is situated on the right side of the slide, illustrating the relationship between different domains.
    *   The diagram features a graph with two axes: Time Domain on the y-axis and Fourier Domain on the x-axis.
    *   The Laplace Domain is positioned above the Fourier Domain, with arrows indicating the direction of the relationships between the domains.
    *   The diagram includes labels and annotations, such as "Damped sine waves" and "Pure sine waves," to provide additional context.
*   **Annotations and Footer**
    *   The slide includes handwritten annotations in blue, red, and green ink, which appear to be notes or comments added by the presenter.
    *   The footer displays the number "3" and a URL: https://www.youtube.com/watch?v=3IAMpH4xF9Q.
    *   A logo is visible in the bottom-right corner, although its details are not discernible.

In summary, the slide presents a clear and concise overview of the premise, discussing the limitations of the time domain and the advantages of using alternative domains like the Fourier and Laplace domains. The diagram provides a visual representation of the relationships between these domains, while the annotations offer additional insights and context.

### Slide 4

The image presents a comprehensive overview of signals in different domains, featuring a white background with a purple banner at the top. The title, "Signals in Different Domains," is prominently displayed in large black text.

**Main Points:**

* **Time Domain:**
	+ Basis: δ(t)
	+ Graph showing a signal v(t) with a blue dashed line and a black solid line, illustrating the representation of a signal in the time domain.
* **Fourier Domain:**
	+ Basis: e^(jωt) = cos(ωt) + j sin(ωt)
	+ Graph displaying the magnitude of V(jω) against frequency, highlighting the frequency components of the signal.
* **Laplace Domain:**
	+ Basis: Time & Freq.
	+ Equation: s = σ + jω, e^(st) = e^(σ+jω)t = e^(σt)e^(jωt)
	+ Graph illustrating the relationship between the Laplace transform and the time-frequency domain.

**Additional Visuals:**

* A 3D graph showing the transformation of a signal from the time domain to the frequency domain.
* A diagram illustrating the measurement of signals in both the time and frequency domains.
* A mathematical equation: V(jω) = ∫e^(-jωt)v(t)dt, which represents the Fourier transform of a signal.

**Key Takeaways:**

* Signals can be represented in different domains, including time, Fourier, and Laplace.
* Each domain provides a unique perspective on the signal, with the time domain showing the signal's amplitude over time, the Fourier domain displaying the signal's frequency components, and the Laplace domain representing the signal in terms of its poles and zeros.
* The Fourier transform is a powerful tool for analyzing signals in the frequency domain.

Overall, the image effectively conveys the importance of understanding signals in different domains, providing a clear and concise visual representation of the concepts.

### Slide 5

The image presents a slide from an electrical engineering lecture, focusing on the analysis of an RC circuit. The title "Example: RC Circuit" is prominently displayed in bold black text at the top left.

**Circuit Diagram**

*   A simple RC circuit diagram is shown, comprising:
    *   A voltage source (Vin) on the left
    *   A resistor (R) connected in series with the voltage source
    *   A capacitor (C) connected in parallel with the output voltage (Vout)

**Mathematical Derivations**

*   The impedance of the capacitor (Zc) is derived as 1/(jωC) = 1/(sC), where s = jω
*   The output voltage (Vout) is expressed in terms of the input voltage (Vin) using the voltage divider formula: Vout = Vin \* (Zc / (Zc + R))
*   The expression for Vout is simplified to: Vout = Vin \* (1/(sC)) / ((1/(sC)) + R)
*   Further simplification yields: Vout = Vin \* (1 / (1 + sRC))

**Key Points and Formulas**

*   The use of "s" instead of "jω" is emphasized
*   The formula for Vout/Vin is derived and simplified
*   The "standard form" and "canonical form" of the transfer function are highlighted
*   Instructions are provided for obtaining a frequency plot:
    *   Set s = jω
    *   Plot magnitude and phase as a function of ω or f

**Additional Notes**

*   The slide includes handwritten notes and annotations, indicating that it is part of a lecture or tutorial.
*   The background of the slide is white, with a purple gradient border at the top.

### Slide 6

The image presents a slide from a presentation on transfer functions and passive first-order filters, featuring a title and a background with a circuit board design.

*   The top third of the image is occupied by a dark blue-green circuit board pattern, which gradually fades into white towards the bottom.
    *   The circuit board design is intricate, with various lines, shapes, and dots visible.
    *   The circuit board pattern is not labeled or annotated in any way.
*   Below the circuit board pattern, the title "3.2 - Transfer Functions and Passive First-Order Filters" is prominently displayed in large black text.
    *   The title is centered and takes up two lines.
    *   The font used for the title is bold and sans-serif.
*   In the bottom-right corner of the image, a small logo is visible.
    *   The logo features a shield with a red and yellow design, accompanied by a black shape resembling a chevron or an arrowhead.
    *   The logo is not labeled or annotated in any way.
*   At the very bottom of the image, the number "6" is displayed in small black text, indicating that this is likely the sixth slide in the presentation.
    *   The number is centered and appears to be a page number or slide counter.

In summary, the image presents a slide from a presentation on transfer functions and passive first-order filters, featuring a title, a circuit board pattern, and a logo. The title is prominently displayed in large black text, while the circuit board pattern and logo are not labeled or annotated. The image also includes a page number or slide counter at the bottom.

### Slide 7

The image presents a slide titled "Transfer Functions" in large black text at the top left, set against a white background with a purple gradient bar above it.

**Main Content**

* The slide features a simple voltage divider circuit diagram on the left side, comprising:
	+ A voltage source labeled "Vin" with a positive terminal connected to a resistor "R1" and a negative terminal connected to ground.
	+ The other end of "R1" is connected to a node labeled "Vout," which is also connected to another resistor "R2."
	+ The other end of "R2" is connected to ground.
* Three bullet points on the right side of the slide:
	+ "Relate one state to another... for each frequency."
	+ "Like a frequency-dependent gain"
	+ "Consider a simple voltage divider"

**Equations and Formulas**

* Below the bullet points, an equation is written in blue and red handwriting-style text:
	+ "Vout/Vin = R2/(R1+R2) [V/V]"
	+ The abbreviation "TF" is written below the equation in red handwriting-style text.

**Additional Elements**

* A small logo resembling a shield with a red and yellow design is located in the bottom-right corner.
* The number "7" is centered at the bottom of the slide.

This description provides a detailed and accurate representation of the slide's content, including the diagram, equations, and other elements.

### Slide 8

The image presents a slide titled "Transfer Function (Linear Plot)" that appears to be part of an educational presentation on electrical engineering or a related field. The slide is divided into two main sections: a circuit diagram and a graph.

*   **Circuit Diagram:**
    *   The circuit consists of a voltage source labeled "Vin" connected in series with two resistors.
    *   One resistor is fixed at 10 kΩ, while the other is variable, denoted as "R".
    *   The output voltage "Vout" is taken across the variable resistor "R".
    *   The circuit is drawn using standard electrical engineering symbols.
*   **Graph:**
    *   The graph plots the transfer function "A(R)" against the resistance "R" in kΩ.
    *   The x-axis ranges from 0 to 100 kΩ, and the y-axis ranges from 0 to 1.
    *   The graph shows a red curve that starts at 0 and increases as "R" increases, eventually reaching a plateau at 1.
    *   The curve is not linear but rather follows a specific mathematical relationship.
*   **Mathematical Relationship:**
    *   Below the graph, the equation "A = Vout/Vin" is written, indicating that "A" represents the ratio of the output voltage to the input voltage.
    *   This equation is a key concept in understanding the transfer function of the circuit.
*   **Additional Elements:**
    *   In the bottom-right corner of the slide, there is a logo that appears to be associated with the University of Maryland, suggesting that the presentation may have been created by or for this institution.

In summary, the slide illustrates a simple voltage divider circuit and its transfer function, which is plotted against the variable resistance "R". The graph shows how the output voltage ratio "A" changes as "R" varies, providing insight into the circuit's behavior.

### Slide 9

The image depicts a slide from a presentation on transfer functions, specifically focusing on log plots. The title "Transfer Function (Log Plot)" is prominently displayed at the top.

**Key Components:**

*   A circuit diagram is shown on the left side of the slide, featuring a voltage source labeled "Vin" and a resistor network with values of 10 kΩ and R.
*   The output voltage "Vout" is indicated across the resistor R.
*   To the right of the circuit diagram, a mathematical expression for the transfer function (TF) is provided: TF = R2 / (Ra + R1) = 1 / (1 + R1/R2).
*   Below the transfer function equation, a graph is presented with the title "A(R)dB" on the y-axis and "R [kΩ]" on the x-axis. The graph displays a red curve that increases as R increases, eventually reaching a plateau.
*   The slide number "9" is visible at the bottom center, and a logo is situated in the bottom-right corner.

**Summary:**

The slide provides a comprehensive overview of transfer functions, including a circuit diagram, a mathematical expression for the transfer function, and a graph illustrating the relationship between A(R)dB and R. The content is presented in a clear and organized manner, making it suitable for educational or instructional purposes.

### Slide 10

The image presents a slide titled "Transfer Function of RC Circuit" in large black text at the top, set against a white background with a purple gradient bar above it. The slide is divided into two sections: the left side features two circuit diagrams, while the right side contains explanatory text and equations.

*   **Circuit Diagrams:**
    *   The top diagram illustrates an RC circuit with a voltage source (Vin) connected to a resistor (R) and a capacitor (C) in series.
        *   Vin is represented by a circle with a plus sign and a minus sign inside, indicating the positive and negative terminals.
        *   R is depicted as a zigzag line, symbolizing resistance.
        *   C is represented by two parallel lines, indicating capacitance.
        *   Vout is labeled at the node between R and C.
    *   The bottom diagram shows the same RC circuit but with the capacitor replaced by its impedance (Zc).
        *   Zc is represented by a rectangle with the label "Zc" inside.
*   **Explanatory Text and Equations:**
    *   The text on the right side of the slide explains that the same concept applies, but now frequency determines the variable resistance.
    *   Three equations are provided:
        *   TF = Zc / (Zc + R)
        *   TF = 1 / (1 + sRC) = A(s)
        *   (s = jω) = 1 / (1 + jωRC) = A(jω)

In summary, the slide illustrates the transfer function of an RC circuit, highlighting how the frequency affects the variable resistance. The two circuit diagrams demonstrate the equivalent representation of the capacitor as an impedance, and the accompanying equations provide a mathematical description of the transfer function in both the s-domain and the frequency domain.

### Slide 11

The image presents a detailed analysis of an RC circuit using a qualitative approach, focusing on its behavior and characteristics.

**Title and Circuit Diagram**

* The title "RC Circuit - Qualitative Approach" is prominently displayed at the top.
* A circuit diagram is shown, consisting of:
	+ A voltage source (Vin) on the left.
	+ A resistor (R) connected in series with the voltage source.
	+ A capacitor (C) connected in parallel with the output (Vout).

**Circuit Analysis**

* The circuit is analyzed for low-frequency (LF) and high-frequency (HF) conditions:
	+ LF: The capacitor acts as an open circuit (O.C.), and Vout = Vin, with a gain (ALF) of 1 (0 dB).
	+ HF: The capacitor acts as a short circuit (S.C.), and Vout = 0, with a gain (AHF) of 0.

**Behavior and Characteristics**

* The behavior of the circuit changes dramatically when the impedance of the capacitor (Zc) equals the resistance (R).
* The circuit is identified as a Lowpass Filter (LPF).
* The output voltage (Vout) is between Vin and 0, with a gain (A) ranging from 1 to 0 as the frequency (f) varies from 0 to infinity.

**Additional Notes and Equations**

* The impedance of the capacitor is represented by Zc, and the condition for the dramatic change in behavior is |Zc| = R.
* The gain (A) is described as a function of frequency, ranging from 1 to 0 as f goes from 0 to infinity.
* A small diagram at the top illustrates the capacitor's behavior at LF and HF, with equivalent circuits showing it as an open circuit and a short circuit, respectively.

### Slide 12

The image presents a slide titled "RC Circuit - Analytical Approach" in black text at the top, with a white background and a purple gradient bar above it. The slide is divided into two main sections: a circuit diagram on the left and mathematical equations on the right.

**Circuit Diagram:**

*   The circuit consists of a voltage source (Vin) connected to a resistor (R) and a capacitor (C) in series.
*   The output voltage (Vout) is taken across the capacitor.
*   The circuit is labeled as a low-pass filter (LPF).

**Mathematical Equations:**

*   The transfer function of the circuit is given by:

    A = Zc / (Zc + R) = 1 / (1 + sRC) = 1 / (1 + jωRC)

    where s = jω, Zc is the impedance of the capacitor, and R is the resistance.

*   The magnitude of the transfer function is:

    |A(jω)| = |1 / (1 + jωRC)| = 1 / √(1 + (ωRC)^2)

*   The focus is on the magnitude of the transfer function, not the phase.
*   Two cases are considered:
    *   Low Frequency (LF): ω → 0, |A(jω)| → 1
    *   High Frequency (HF): ω → ∞, |A(jω)| → 1 / (ωRC) → 0

**Additional Information:**

*   The slide is labeled as "12" at the bottom center, indicating that it is the 12th slide in a presentation.
*   A logo is present in the bottom-right corner, featuring a shield with a red and yellow design.

Overall, the slide provides a detailed analysis of an RC circuit as a low-pass filter, including its transfer function and frequency response.

### Slide 13

The image presents a detailed lecture slide on the topic of "Cutoff Frequency." Here is a comprehensive summary of the content:

**Title and Circuit Diagram**

* The title "Cutoff Frequency" is prominently displayed at the top left of the slide.
* A circuit diagram is shown, consisting of:
	+ A voltage source Vin
	+ A resistor R
	+ A capacitor Zc
	+ The output voltage Vout is taken across the capacitor

**Handwritten Notes**

* The handwritten notes on the slide are written in blue, black, and red ink.
* The notes discuss the transition of the behavior from A ≈ 1 to A ≈ 1/ωRC.
* A key statement is: "There's a special frequency when |Zc| = R, when they are equally important."
* The notes also derive the cutoff frequency ωc, where:
	+ |Zc| = R
	+ 1/ωcC = R
	+ ωc = 1/RC = 1/τ

**Definitions and Formulas**

* The slide lists several definitions and formulas related to cutoff frequency, including:
	+ Cutoff frequency: ωc, fc
	+ Corner frequency: ωc, fc
	+ "-3dB" frequency: ω-3dB, f-3dB
	+ Half Power Frequency: |A(jω)|^2 = (1/√2)^2 = 1/2
* The transfer function A(s) is given by:
	+ A(s) = 1 / (1 + sRC)
	+ A(s) = 1 / (1 + s/ωc)
	+ s = jω

**Additional Notes**

* A note at the bottom of the slide states: "Note sRC = sτ"
* The slide number "13" is displayed at the bottom center.
* A logo is present in the bottom-right corner of the slide.

Overall, the slide provides a detailed discussion of the cutoff frequency, including its definition, derivation, and relevance to the circuit diagram.

### Slide 14

The image presents a slide titled "Example: Circuit to Transfer Function" and features a detailed analysis of an electronic circuit. The slide is divided into two main sections: a diagram on the left and a series of equations and notes on the right.

**Diagram:**

*   The diagram depicts a circuit with various components, including resistors (R1, Rf, Ri), an inductor (L1), and a voltage source (Vin).
*   The circuit is labeled with different stages, including "Stage 1" and "Stage 2."
*   The diagram also includes annotations, such as "Filter (Voltage Div.)" and "Noninverting Amp."

**Equations and Notes:**

*   The right side of the slide presents a series of equations and notes related to the circuit.
*   The equations derive the transfer function (T.F.) of the circuit, starting with the voltage gain (A1(s)) and the output voltage (Vout).
*   The notes provide additional context and explanations, including the definition of the transfer function and the derivation of the frequency domain expression.
*   The equations involve various mathematical operations, such as multiplication, division, and integration, and include symbols like s, ωc, and jω/ωc.
*   The notes also reference specific values, like R1/L and 1/τ, and provide comments on the circuit's behavior, including its high-pass characteristics.

**Key Points:**

*   The slide provides a step-by-step derivation of the transfer function for the given circuit.
*   The circuit is analyzed in two stages, with the first stage involving a voltage divider and the second stage involving a non-inverting amplifier.
*   The transfer function is derived using the voltage gain and output voltage equations.
*   The frequency domain expression is obtained by substituting s = jω into the transfer function.

**Overall:**

*   The slide presents a detailed analysis of an electronic circuit, deriving its transfer function and providing insights into its behavior.
*   The diagram and equations work together to illustrate the circuit's operation and characteristics.
*   The notes provide additional context and explanations, making the slide a valuable resource for understanding the circuit's behavior and transfer function.

### Slide 15

The slide is titled "Example: Circuit to Transfer Function" and contains a circuit diagram on the left-hand side, along with corresponding equations and handwritten notes on the right. Here is a detailed description of the slide's content:

**Circuit Diagram:**

* The circuit consists of an input voltage (Vin) connected to a resistor (R1) in series with an inductor (L1), which is grounded.
* The output voltage (Vout) is taken across the output of an operational amplifier (op-amp), which has its non-inverting input connected to the junction of R1 and L1.
* The op-amp has a feedback resistor (Rf) connected between its output and inverting input, and a resistor (Ri) connected between the inverting input and ground.

**Equations:**

* The transfer function A(s) is given by the equation:
  A(s) = (s/ωc / (1 + s/ωc)) * (1 + Rf/Ri)
  where ωc = R1/L1
* The equation is broken down into two parts: A1 = s/ωc / (1 + s/ωc) and A2 = 1 + Rf/Ri
* A1 is labeled as "AHPF" (High-Pass Filter) and A2 is labeled as "APB = 'Pass band Gain'"

**Handwritten Notes:**

* The notes are written in blue and red ink.
* The blue notes state:
  - "Can sub in s = jω = j·2πf to do a frequency response plot (Bode Plot)"
  - "Analytical models (equation-based) allow us to design in a way that numerical simulation does not."
  - "Converts circuit topology and component values to frequency-dependent behaviour (eg ωc)"
* The red notes highlight the terms "A1", "A2", and "APB = 'Pass band Gain'".

Overall, the slide illustrates how to derive a transfer function from a given circuit diagram and provides additional context on the significance of the transfer function in analyzing the circuit's behavior.

### Slide 16

The image presents a table titled "Passive First-Order Filters" with four columns and three rows, providing information on different types of filters. The first column lists the filter types, while the second column displays their transfer functions, and the third and fourth columns illustrate the capacitor and inductor implementations, respectively.

*   **Title and Subtitle**
    *   The title "Passive First-Order Filters" is displayed in black text at the top of the image.
    *   A subtitle "(First-Order: Max power of s is 1)" is written in blue handwriting to the right of the title.
*   **Table Structure**
    *   The table consists of four columns and three rows.
    *   The first row contains column headers: "Type", "Transfer Function", "Capacitor Implementation", and "Inductor Implementation".
    *   The first column lists two filter types: "Lowpass" and "Highpass".
*   **Transfer Functions**
    *   The transfer function for the Lowpass filter is given as $\frac{1}{1 + s/\omega_c}$, where $\omega_c = \frac{1}{RC}$ or $\frac{R}{L}$.
    *   The transfer function for the Highpass filter is $\frac{s/\omega_c}{1 + s/\omega_c}$, with $\omega_c = \frac{1}{RC}$ or $\frac{R}{L}$.
*   **Capacitor Implementations**
    *   For the Lowpass filter, the capacitor implementation is shown as a circuit diagram with $V_{in}$, $R$, and $C$ connected in series, and $V_{out}$ taken across $C$.
    *   For the Highpass filter, the capacitor implementation is depicted as a circuit diagram with $V_{in}$, $C$, and $R$ connected in series, and $V_{out}$ taken across $R$.
*   **Inductor Implementations**
    *   For the Lowpass filter, the inductor implementation is illustrated as a circuit diagram with $V_{in}$, $L$, and $R$ connected in series, and $V_{out}$ taken across $R$.
    *   For the Highpass filter, the inductor implementation is shown as a circuit diagram with $V_{in}$, $R$, and $L$ connected in series, and $V_{out}$ taken across $L$.
*   **Additional Information**
    *   The slide number "16" is displayed at the bottom center of the image.
    *   A logo is visible in the bottom-right corner, although its details are not discernible.

### Slide 17

The image is a slide from a presentation about Bode plots, a graphical representation used in control theory and signal processing to analyze the frequency response of systems. The slide is titled "3.3 - Bode Plots" and features a diagram illustrating the relationship between circuits, transfer functions (TF), and Bode plots.

Here are the key elements of the image:

* **Title and Background**
	+ The title "3.3 - Bode Plots" is written in bold black text on the left side of the slide.
	+ The background of the slide is white, with a decorative border at the top featuring a circuit board design in shades of blue and green.
* **Diagram**
	+ The diagram is drawn in blue ink and consists of three labels: "Circuit", "TF", and "Bode Plot".
	+ The labels are connected by arrows, indicating the relationships between them.
	+ The diagram suggests that a circuit can be represented by a transfer function (TF), which can then be used to generate a Bode plot.
* **Statistics**
	+ There are no explicit statistics presented in the image.
	+ However, the number "17" is displayed at the bottom center of the slide, likely indicating the slide number.

In summary, the image is a slide from a presentation that introduces the concept of Bode plots and their relationship to circuits and transfer functions. The diagram provides a visual representation of how these concepts are interconnected, and the slide is designed to be informative and easy to follow.

### Slide 18

The image presents a detailed lecture slide on plotting transfer functions, specifically focusing on the graphical representation of a low-pass filter's frequency response. The slide is divided into several key components, which are summarized below:

**Title and Main Text**

* The title "Plotting a Transfer Function" is prominently displayed at the top of the slide.
* A bullet point below the title states, "We can make a plot of |A(jω)| vs ω (set s = jω gives 1/(1+jω/ωc))".

**Graph**

* A graph is shown on the left side of the slide, with the following characteristics:
	+ The x-axis is labeled as ω (rad/s) and spans from ωc/100 to 100ωc.
	+ The y-axis is labeled as |A(jω)| (dB) and ranges from -40 to 20.
	+ The graph features three curves:
		- A red curve labeled "straight-line approx."
		- A blue curve labeled "Realistic"
		- A straight line with a slope of -20 dB/decade

**Equations and Formulas**

* Several equations and formulas are written on the right side of the slide:
	+ AdB = 20 log10(|A|)
	+ |ALPF| @ LF ≅ 1 = 0 dB
	+ |ALPF| ω > ωc ≅ |1/(jω/ωc)| = ωc/ω
	+ ∴ every ω x 10 → |A| ÷ 10 = -20 dB, ω x 100 → |A| ÷ 100 = -40 dB

**Additional Notes**

* A handwritten note in green text reads, "As a circuit designer, I can move ωc since ωc = 1/RC."
* A logo is visible in the bottom-right corner of the slide.

**Transfer Function**

* The transfer function for a low-pass filter is written in blue text: "LPF: 1/(1+s/ωc)".
* The transfer function is also represented in the equation "1/(1+jω/ωc)".

Overall, the slide provides a comprehensive overview of plotting transfer functions, including the graphical representation of a low-pass filter's frequency response, relevant equations, and formulas.

### Slide 19

The image presents a lecture slide on Bode plots, specifically focusing on low-pass filters. The title "Bode Plot - Lowpass Filter" is prominently displayed at the top.

*   **Title and Introduction**
    *   The title "Bode Plot - Lowpass Filter" is in large black text.
    *   Below the title, there are three bullet points that introduce the concept of Bode plots and their application to low-pass filters.
*   **Mathematical Derivation**
    *   The derivation of the transfer function A(s) for a low-pass filter is shown, starting with the equation A(s) = 1/(sC)/(R + 1/sC).
    *   The equation is simplified to A(s) = 1/(sRC + 1) and further to A(s) = 1/(s/ωc + 1), where ωc = 1/RC.
    *   The frequency response is obtained by substituting s = jω, resulting in A(jω) = 1/(jω/ωc + 1).
*   **Bode Magnitude Plot**
    *   The Bode magnitude plot is discussed, with the magnitude of A(jω) plotted against frequency.
    *   The plot is divided into two asymptotes: one below ωc and one above ωc.
    *   Below ωc, the magnitude is approximately 0 dB, while above ωc, it decreases at a rate of -20 dB/decade.
*   **Bode Phase Plot**
    *   The Bode phase plot is also discussed, with the phase angle of A(jω) plotted against frequency.
    *   The phase angle is 0° below ωc and -90° above ωc, with a transition region around ωc.
*   **Graphs**
    *   Two graphs are shown on the right side of the slide: a Bode magnitude plot and a Bode phase plot.
    *   The Bode magnitude plot shows the magnitude of A(jω) in decibels (dB) versus frequency on a logarithmic scale.
    *   The Bode phase plot shows the phase angle of A(jω) in degrees versus frequency on a logarithmic scale.
    *   Both graphs have a red line representing the asymptotic behavior and a blue dashed line representing the actual response.

In summary, the slide provides a detailed explanation of Bode plots for low-pass filters, including the mathematical derivation of the transfer function, the construction of Bode magnitude and phase plots, and the interpretation of the resulting graphs. The slide is likely part of a larger presentation on control systems or signal processing.

### Slide 20

The image presents a comprehensive analysis of a Bode Plot for a Highpass Filter, featuring a detailed breakdown of the filter's characteristics and behavior.

**Title and Equations**

* The title "Bode Plot - Highpass Filter" is prominently displayed at the top.
* The equation for the transfer function A(s) is given as:

  $A(s) = \frac{sL}{sL+R} = \frac{\frac{sL}{R}}{\frac{sL}{R}+1} = \frac{s\tau_c}{s\tau_c+1} = \frac{\frac{s}{\omega_c}}{\frac{s}{\omega_c}+1}$

  This equation is labeled as "HPF" (Highpass Filter).

**Bode Magnitude Plot**

* The Bode Magnitude Plot is described, with the instruction to "Plot |A(s)| and ∠A(s)".
* The plot is generated by substituting s = jω and sweeping the frequency.
* Two asymptotes are identified:
  + Below ωc, A(jω) ≈ $\frac{1}{j\omega/\omega_c}$, resulting in a slope of +20 dB/decade.
  + Above ωc, A(jω) approaches 1, resulting in 0 dB.

**Graphical Representation**

* Two graphs are presented:
  + The top graph displays the magnitude of A(s) in decibels (dB) versus frequency (ω) on a logarithmic scale.
  + The bottom graph shows the phase angle of A(s) versus frequency (ω) on a logarithmic scale.

**Key Features and Asymptotes**

* The magnitude plot has two asymptotes:
  + A low-frequency asymptote with a slope of +20 dB/decade.
  + A high-frequency asymptote at 0 dB.
* At ω = ωc, the magnitude is -3 dB.
* The phase plot has two asymptotes:
  + A low-frequency asymptote at 90°.
  + A high-frequency asymptote at 0°.

**Additional Notes and Annotations**

* Various annotations and notes are scattered throughout the slide, providing additional context and explanations for the Bode Plot and its characteristics. These include:
  + "Pass band" and "Freq. that made it through the filter" annotations on the magnitude plot.
  + "20 dB/decade rolloff" annotation on the magnitude plot.
  + Calculations and derivations for the asymptotes and phase angles.

Overall, the image provides a thorough analysis of the Bode Plot for a Highpass Filter, including its transfer function, magnitude and phase plots, and key characteristics.

### Slide 21

The image presents a detailed explanation of Bode Magnitude Plots of Factored Transfer Functions (TF). The content is structured as follows:

**Title**
- "Bode Magnitude Plots of Factored TF"

**Main Bullet Points**

1. **Sometimes the TF isn't easy to decompose into LPF and HPF terms**
   - Sub-bullet point: "We can take a more generic approach in these cases"

2. **Thanks to logarithms, each factor in 's' can be treated individually**
   - Equation: $|A(s)|_{dB} = |N_1(s)|_{dB} + |N_2(s)|_{dB} + \cdots - |D_1(s)|_{dB} - |D_2(s)|_{dB} + \cdots$
   - Explanation: "because $\log(AB/C) = \log A + \log B - \log C$"

**Example and Further Explanation**

- The transfer function $A(s)$ is given by: $A(s) = \frac{N_1(s)N_2(s)\cdots}{D_1(s)D_2(s)\cdots}$
- A specific example is provided: $A(s) = \frac{s/\omega_c}{(s/\omega_c + 1)}(1 + \frac{R_f}{R_i}) = A_{HPF} \cdot A_{PB}$
- Breaking down $A(s)$ into its components in decibels: $|A(s)|_{dB} = |A_{HPF}| + |A_{PB}|$
- Further decomposition: $|A(s)|_{dB} = |s/\omega_c|_{dB} + |(1 + \frac{R_f}{R_i})|_{dB} - |s/\omega_c + 1|_{dB}$
- Labels:
  - $N_1$ and $D_1$ are labeled under the terms in the example transfer function.
  - The terms are also represented as $N_{dB}$ and $D_{dB}$ in the decomposition.

**Visual Elements and Layout**

- The slide has a white background with a purple gradient bar at the top.
- The title is prominently displayed in large black text.
- The main text and equations are presented in a clear, readable format, with key equations and terms highlighted or annotated in blue and red ink.
- A logo is visible in the bottom-right corner, though its details are not specified.

**Overall Content Summary**

The slide discusses how to handle transfer functions that are not easily decomposed into low-pass filter (LPF) and high-pass filter (HPF) terms by using a more generic approach based on logarithms. This allows for the treatment of each factor in 's' individually, simplifying the analysis of Bode magnitude plots for complex transfer functions.

### Slide 22

The slide is titled "Factored TF Bode Magnitude Example." It contains two main bullet points and a graph. 

*   The first bullet point states: "Plot |A(s)| = |sL / (sL + R)| = |(s / ωc) / (s / ωc + 1)|."
    *   This equation is related to the magnitude of a transfer function A(s).
    *   The variables are:
        *   A(s): transfer function
        *   s: complex frequency
        *   L: inductance
        *   R: resistance
        *   ωc: cutoff frequency
*   The second bullet point reads: "Consider each factor individually:"
    *   Two equations are provided to analyze the magnitude of A(s) in decibels (dB).
    *   The first equation is: |A(s)|dB = |(s / ωc)|dB - |(s / ωc) + 1|dB
        *   This equation breaks down the magnitude of A(s) into two components.
    *   The second equation is: |A(jω)|dB = |(jω / ωc)|dB - |(jω / ωc) + 1|dB
        *   This equation is similar to the first one but substitutes s with jω, where j is the imaginary unit and ω is the angular frequency.
*   The graph on the right-hand side of the slide displays the magnitude of A(s) in dB against the angular frequency ω in rad/s.
    *   The x-axis represents ω, ranging from ωc/100 to 100ωc.
    *   The y-axis represents |A(s)|dB, ranging from -20 to 20.
    *   Three lines are plotted on the graph:
        *   A blue line representing the magnitude of the factor |(s / ωc)|dB.
        *   A red dashed line representing the magnitude of the factor -|(s / ωc) + 1|dB, including the negative sign.
        *   A green line representing the overall magnitude |A(jω)|dB, which is the difference between the blue and red lines.
    *   The graph illustrates how the individual factors contribute to the overall magnitude response of the transfer function A(s).

### Slide 23

The image presents a slide from a presentation on Bode phase plots of factored transfer functions (TF). The title, "Bode Phase Plots of Factored TF," is prominently displayed at the top.

**Key Points:**

*   **Phase:** The phase of each factor is a complex number at any frequency, allowing for individual treatment.
*   **Mathematical Derivation:**
    *   $\angle A(s) = \angle \left(\frac{N_1(s)N_2(s)\cdots}{D_1(s)D_2(s)\cdots}\right)$
    *   $= \angle (N_1(s)N_2(s)\cdots) - \angle (D_1(s)D_2(s)\cdots)$
    *   $= \angle N_1(s) + \angle N_2(s) + \cdots - \angle D_1(s) - \angle D_2(s) - \cdots$

**Summary:**

The slide provides a concise overview of Bode phase plots for factored transfer functions, highlighting the importance of considering the phase of each factor individually. The mathematical derivation demonstrates how to calculate the overall phase angle of a transfer function by combining the phase angles of its constituent factors.

### Slide 24

The image presents a slide from a presentation on control systems, specifically focusing on the Bode phase plot of a transfer function. The title "Factored TF Bode Phase Example" is prominently displayed at the top.

**Main Points:**

* **Transfer Function**
	+ The transfer function is given as $A(s) = \frac{sL}{sL+R} = \frac{\frac{s}{\omega_c}}{\frac{s}{\omega_c}+1}$
	+ This represents a simple RC circuit with a capacitor and resistor
* **Bode Phase Plot**
	+ The Bode phase plot is a graphical representation of the phase response of the system
	+ The plot shows the phase angle of the system's output relative to its input as a function of frequency
* **Phase Response**
	+ The phase response is calculated using the formula $\angle A(j\omega) = \angle \left(\frac{j\omega}{\omega_c}\right) - \angle \left(\frac{j\omega}{\omega_c} + 1\right)$
	+ The phase response is broken down into two components: the phase of the numerator and the phase of the denominator
* **Graphical Representation**
	+ The graph shows the phase response of the system as a function of frequency
	+ The x-axis represents the frequency in rad/s, ranging from $\omega_c/100$ to $100\omega_c$
	+ The y-axis represents the phase angle in degrees, ranging from -90° to 90°
	+ The graph consists of three lines: a green line representing the phase of the numerator, a red line representing the phase of the denominator, and a blue line representing the overall phase response
	+ The dashed red line includes the negative sign, indicating the phase shift due to the negative feedback

**Summary:**

The image provides a detailed example of how to construct a Bode phase plot for a given transfer function. The transfer function represents a simple RC circuit, and the Bode phase plot is used to analyze the phase response of the system. The plot is broken down into its constituent parts, showing the phase response of the numerator and denominator separately. The resulting graph provides a visual representation of the system's phase response as a function of frequency.

### Slide 25

The image presents a lecture slide titled "Example: Unwanted Filters" and focuses on deriving the factored transfer function of a sensor and noninverting amplifier.

**Slide Content**

* The title "Example: Unwanted Filters" is displayed prominently at the top of the slide.
* A bullet point below the title states: "Derive the factored transfer function of a sensor (including output resistance) and noninverting amplifier (including input capacitance)".
* A circuit diagram is shown on the left side of the slide, enclosed within a dotted blue rectangle. The diagram includes:
	+ A voltage source labeled "Vin"
	+ A resistor labeled "Rout"
	+ Capacitors labeled "C+" and "C-"
	+ Resistors labeled "Ri" and "Rf"
	+ An operational amplifier
* Equations and formulas are written around the circuit diagram, including:
	+ Zi = Ri || Zc, Zc = 1/sC
	+ A(s) = Vout/Vin = A1(s) * A2(s)
	+ A1(s) = (1 + Rf/Ri) * (1/(1 + s/ωc1)) * (1 + s/ωcz)
* An approach to analyzing the circuit is outlined on the right side of the slide, which involves:
	+ Breaking down the circuit into separate amplifier blocks (A1 and A2)
	+ Deriving the transfer functions for each block
	+ Combining the transfer functions to obtain the overall transfer function
* The transfer functions for A1 and A2 are derived using the circuit diagrams and equations, including:
	+ A1 = V+/Vin = 1/(1 + s/ωc), ωc = 1/(Rout*C+)
	+ A2 = Vout/V+ = (Ri + Rf(1 + s/ωc2))/Ri = (1 + Rf/Ri)(1 + s/ωc2), ωc2 = 1/(Rf||Ri)*C-

**Key Concepts and Takeaways**

* The slide illustrates the importance of considering the output resistance of a sensor and the input capacitance of a noninverting amplifier when deriving the transfer function.
* The factored transfer function is derived by breaking down the circuit into separate amplifier blocks and combining their transfer functions.
* The resulting transfer function includes a low-pass filter (LPF) and a real zero, which are critical components in understanding the frequency response of the circuit.

### Slide 26

The image presents a lecture slide titled "Example: Unwanted Filters" and features a Bode magnitude plot. The slide is divided into two main sections: the left side contains mathematical equations and formulas, while the right side displays a graph.

**Left Section:**

*   The title "Example: Unwanted Filters" is prominently displayed at the top.
*   Below the title, a bullet point reads, "Create the Bode magnitude plot given:" followed by several equations and formulas:
    *   $R_{out} = 100 \Omega$, $C_+ = C_- = 3 pF$, $R_f = 1 M\Omega$, $R_i = 10 k\Omega$
    *   $A_{PB} = 1 + \frac{R_f}{R_i} = 101 V/V = 40 dB$
    *   $\omega_{c1} = \frac{1}{R_{out}C_+} = \frac{1}{100 \times 3p} = 3.33 Grad/s = 531 MHz$
    *   $\omega_{c2} = \frac{1}{(R_f||R_i)C_-} = \frac{1}{(1M||10k) \cdot 3p} = 33.7 Mrad/s = 5.36 MHz$
    *   $A = A_{PB} \cdot A_{LPF} \cdot A_{Rz}$

**Right Section:**

*   A Bode magnitude plot is displayed, featuring a graph with the following characteristics:
    *   The x-axis represents frequency (f) in MHz, spanning from 0.5 to 500 MHz.
    *   The y-axis represents the magnitude of A(s) in decibels (dB), ranging from -40 to 80 dB.
    *   The graph includes three lines: a black line, a blue line, and a red line, as well as a green line.
    *   The black line starts at approximately 80 dB and decreases to around 40 dB.
    *   The blue line remains constant at 40 dB.
    *   The red line begins at 0 dB and increases to approximately 20 dB.
    *   The green line starts at 0 dB and decreases to around -20 dB.
    *   The graph is labeled with various points, including $\omega_{c2}$ and $\omega_{c1}$, which correspond to the frequencies calculated in the equations on the left side of the slide.

**Additional Elements:**

*   At the bottom of the slide, a URL is provided: https://everycircuit.com/circuit/5437570582052864
*   A logo is visible in the bottom-right corner of the slide.

Overall, the slide appears to be discussing the creation of a Bode magnitude plot for a specific circuit configuration, using the given equations and formulas to analyze the frequency response of the system.

### Slide 27

The image is a slide from a presentation about active first-order filters, likely used in an educational setting. The slide features a title, a background image, and a logo.

**Title:**
The title of the slide is "3.4 - Active First-Order Filters" in bold black font, centered on the left side of the page.

**Background Image:**
The top portion of the slide displays a background image that resembles a circuit board. The image is predominantly teal and features various components such as wires, microchips, and other electronic elements.

**Logo:**
In the bottom-right corner of the slide, there is a small logo consisting of a yellow shield with a red design inside it. The logo appears to be associated with the University of Cambridge, as indicated by the crest-like design.

**Page Number:**
At the bottom center of the slide, the number "27" is displayed in small black font, indicating that this is the 27th slide in the presentation.

Overall, the slide appears to be introducing a topic related to active first-order filters, which are likely to be discussed in more detail in subsequent slides.

### Slide 28

The image presents a slide titled "Constructing Filters" with a white background and a purple gradient bar at the top. The title is prominently displayed in large black text, followed by five bullet points that outline the key concepts related to constructing filters.

**Bullet Points:**

*   We have enough building blocks to do frequency-domain filtering
    *   This means amplifying some frequencies, and attenuating others
*   0 < Gain < 1 using voltage divider
*   Gain < 0 or Gain > 1 using opamps
*   Low-pass or high-pass filters using L and C
*   Multiply frequency response by putting building blocks in series
*   Add signals using opamps

**Circuit Diagrams:**

The slide features seven circuit diagrams, each labeled with a number from 1 to 7. These diagrams are accompanied by corresponding labels and equations, which are used to illustrate the concepts discussed in the bullet points.

**Circuit Diagram Details:**

1.  A simple voltage divider circuit with two resistors (R1 and R2) connected in series between Vin and Vout.
2.  A non-inverting op-amp circuit with input voltage Vin, input resistor Ri, and feedback resistor Rf.
3.  Another non-inverting op-amp circuit similar to diagram 2.
4.  A low-pass filter circuit consisting of a resistor R and capacitor C.
5.  A high-pass filter circuit with capacitor C and resistor R.
6.  A block diagram representing a cascade of a high-pass filter (HPF) and a low-pass filter (LPF).
7.  An inverting op-amp circuit with two input voltages (Vin1 and Vin2), input resistors Ri, and feedback resistor Rf.

**Additional Elements:**

*   A logo in the bottom-right corner, featuring a shield with a red and yellow design.

Overall, the slide provides a comprehensive overview of the building blocks and techniques used to construct filters, along with relevant circuit diagrams and equations to support the concepts discussed.

### Slide 29

The slide is titled "Active Filters" and has a white background with a black, purple, and pink gradient bar at the top. The main content of the slide is as follows:

*   Three bullet points:
    *   "Passive filters have a maximum gain of 1 [V/V]"
    *   "We can build the filter into our basic opamp amplifiers"
    *   "Simplest is to use inverting amp with Zf and Zi"

A diagram is shown on the left side of the slide, which appears to be a circuit diagram for an inverting amplifier. The diagram includes:

*   Vin: input voltage
*   Zi: input impedance
*   Zf: feedback impedance
*   Vout: output voltage
*   An operational amplifier (op-amp) with a negative (-) input and a positive (+) input, where the positive input is grounded.

To the right of the diagram, there are two equations/formulas written in different colors:

*   A = -Zf/Zi (written in blue and red)
    *   "180° phase shift usually doesn't matter" is written below this equation in red.

A table is also present to the right of the equation, with two columns labeled "Want" and "Do". The table contains:

| Want | Do |
| --- | --- |
| \|A\|↑ | \|Zf\|↑ or \|Zi\|↓ |
| \|A\|↓ | \|Zf\|↓ or \|Zi\|↑ |

The table is written in blue.

At the bottom center of the slide, the number "29" is displayed in small black text, likely indicating the slide number. In the bottom-right corner, there is a logo featuring a shield with a red and yellow design.

Overall, the slide presents information about active filters, including their construction using op-amp amplifiers and the simplest implementation using an inverting amplifier.

### Slide 30

The image presents a detailed analysis of an Active RC Low Pass Filter (LPF) circuit, including its schematic, transfer function, and frequency response.

**Title and Circuit Schematic**

* The title "Active RC LPF" is prominently displayed in the top-left corner.
* Two identical circuit schematics are shown, illustrating the Active RC LPF configuration, which consists of:
	+ An operational amplifier
	+ Input resistor Ri
	+ Feedback resistor Rf
	+ Capacitor Cf connected in parallel with Rf

**Transfer Function and Impedance Calculations**

* The impedance of the feedback network (Zf) is calculated as the parallel combination of Rf and Cf, yielding:
	+ Zf = Zcf || Rf = (sCf + 1/Rf)^-1 = Rf / (1 + sRfCf)
* The gain (A) of the circuit is derived as:
	+ A = -Zf / Ri = -Rf / Ri \* (1 / (1 + sRfCf))

**Frequency Response Analysis**

* The frequency response is analyzed in three regions:
	1. **Low Frequency (ω << ωc)**:
		- The gain is approximated as A ≈ -Rf / Ri = APB
		- A diagram illustrates the simplified circuit, showing Rf dominant in the feedback network
	2. **Cutoff Frequency (ω = ωc)**:
		- The magnitude of the gain at the cutoff frequency is calculated as |A(jωc)| = 1/√2 \* |APB|
		- A diagram shows the impedance of Cf equal to Rf at the cutoff frequency
	3. **High Frequency (ω >> ωc)**:
		- The gain is approximated as A ≈ APB \* (1 / (jω/ωc))

**Bode Plot and Design Considerations**

* A Bode plot illustrates the frequency response of the Active RC LPF, showing:
	+ A flat passband with a gain of APB
	+ A -20 dB/decade roll-off beyond the cutoff frequency ωc
* The note highlights two important design parameters: APB and ωc, with three degrees of freedom: Ri, Rf, and Cf
* A suggestion is made to choose a reasonable starting value for one component and iterate if needed

**Additional Information**

* A URL is provided at the bottom-left corner, referencing a specific circuit on everycircuit.com
* A logo is displayed in the bottom-right corner, featuring a shield with a red and black design.

### Slide 31

The image presents a slide titled "Active RC HPF" with a comprehensive analysis of an active high-pass filter circuit. The slide is divided into several sections, each providing detailed information about the circuit's behavior and characteristics.

**Circuit Diagram**
The top-left corner of the slide features a circuit diagram, which includes:

*   A voltage source (Vin)
*   A capacitor (Ci) connected in series with a resistor (Ri) to form the input impedance (Zi)
*   An operational amplifier (op-amp) with a feedback resistor (Rf)

The circuit is labeled as an "Active RC HPF," indicating that it is an active high-pass filter implemented using resistors and capacitors.

**Mathematical Analysis**
Below the circuit diagram, a mathematical analysis is presented, including:

*   The expression for the input impedance (Zi) in terms of Ci, Ri, and s (the complex frequency variable)
*   The transfer function of the circuit, A(s), which relates the output voltage (Vout) to the input voltage (Vin)

The analysis involves deriving the transfer function using the op-amp's properties and the circuit components.

**Frequency Response**
The bottom-left corner of the slide displays a Bode plot, which illustrates the frequency response of the circuit. The plot shows:

*   The magnitude of the gain (|A(jω)|) versus frequency (ω) on a logarithmic scale
*   The cutoff frequency (ωc) marked on the plot

The Bode plot provides a visual representation of the circuit's filtering behavior.

**Low, Cutoff, and High Frequency Analysis**
The right-hand side of the slide presents a detailed analysis of the circuit's behavior at different frequency ranges, including:

*   **Low Frequency:** ω << ωc
    *   The gain (A) is approximately equal to -Rf/Ri times sRCi
    *   A simplified circuit diagram is shown, highlighting the dominant components at low frequencies
*   **Cutoff Frequency:** ω = ωc
    *   The magnitude of the input impedance (|Zi|) is equal to √2Ri
    *   The gain at the cutoff frequency is calculated, and the result is ApB - 3dB
    *   A simplified circuit diagram is shown, illustrating the circuit's behavior at the cutoff frequency
*   **High Frequency:** ω >> ωc
    *   The gain (A) is approximately equal to -Rf/Ri, which is equal to ApB
    *   A simplified circuit diagram is shown, highlighting the dominant components at high frequencies

Each section provides a clear understanding of the circuit's behavior under different frequency conditions.

**Additional Information**
The slide includes a URL at the bottom, "https://everycircuit.com/circuit/6248630201352192," which likely links to a simulation or further resources related to the circuit. The slide number "31" is also displayed, indicating that this is part of a larger presentation. A logo is visible in the bottom-right corner, although its details are not discernible.

Overall, the slide provides a thorough analysis of the active RC high-pass filter circuit, covering its circuit diagram, mathematical analysis, frequency response, and behavior at different frequency ranges.

### Slide 32

The image is a slide from a presentation on transducer filter design, featuring a white background with a black and purple header. The title, "Example - Transducer Filter Design," is prominently displayed in bold black text at the top.

**Main Content:**

* Two bullet points provide context for the example:
	+ A sensor operates at 4 kHz ± 1 kHz and is connected to a data acquisition circuit being designed.
	+ The sensor is powered by a boost converter that uses an inductor to boost the voltage to a higher working voltage, activated at a rate of 1 MHz.
* A task is presented: Design a filter that provides 100x gain (40 dB) and eliminates the switching noise from the boost converter.
* A graph is shown, illustrating the frequency response of the filter, with annotations indicating the desired frequency range and noise elimination.

**Graph Details:**

* The graph features a logarithmic x-axis representing frequency (kHz) and a y-axis representing gain (dB).
* Three curves are plotted:
	+ A blue curve representing the desired signal.
	+ A black curve representing the actual signal.
	+ A dotted curve representing the noise.
* Annotations on the graph include:
	+ "Do want" and "Don't want" labels.
	+ Arrows indicating the direction of the signal and noise.
	+ Notes on the graph, such as "Good job eliminating switching noise" and "Could use higher order filter to get > 20 dB/dec. rolloff."

**Additional Notes:**

* Handwritten notes in red and green ink are scattered throughout the slide, providing additional context and explanations.
* A small logo is visible in the bottom-right corner of the slide.

Overall, the image presents a clear and concise example of transducer filter design, with a focus on eliminating switching noise from a boost converter.

### Slide 33

The image presents a slide from a lecture on active filters, titled "Solution: One Stage, Active Filter." The slide is divided into two main sections: the left side contains bullet points outlining the problem and its solution, while the right side features a circuit diagram and a graph illustrating the frequency response of the filter.

**Left Side: Problem and Solution**

*   The problem statement:
    *   Eliminate 1 MHz noise
    *   Keep 4 ± 1 kHz signal
    *   Achieve 100 [V/V] gain
*   Solution:
    *   Use a Low-Pass Filter (LPF)
    *   Set the gain to 100 until at least 5 kHz, then drop
    *   Calculate the required component values:
        *   $\frac{R_f}{R_i} = 100$
        *   $\omega_c = 2\pi \times 10$ kHz (cutoff frequency)
        *   $\omega_c = \frac{1}{R_fC_f} = 2\pi \times 10$ krad/s
    *   Example calculation:
        *   Choose $R_i = 10 k\Omega$
        *   $\Rightarrow R_f = 1 M\Omega$
        *   $\Rightarrow C_f = \frac{1}{2\pi f_c R_f} = 15.9 pF$

**Right Side: Circuit Diagram and Frequency Response**

*   Circuit Diagram:
    *   An inverting amplifier configuration with an op-amp
    *   Input resistance $R_i$ connected between the input voltage $V_{in}$ and the inverting input of the op-amp
    *   Feedback resistance $R_f$ and capacitance $C_f$ connected in parallel between the output and the inverting input of the op-amp
*   Frequency Response Graph:
    *   A Bode plot showing the magnitude of the gain $|A|$ versus frequency $f$
    *   The gain is flat at 40 dB until the cutoff frequency $f_c$, then drops off
    *   The cutoff frequency is marked on the graph

**Equations and Formulas**

*   $A(s) = -\frac{Z_f}{R_i}$
*   $A(s) = -\frac{R_f}{R_i} \left(\frac{1}{1+sR_fC_f}\right)$
*   $\omega_c = \frac{1}{R_fC_f} = 2\pi \times 10$ krad/s
*   $f_c = \frac{1}{2\pi R_fC_f}$

The slide provides a clear and concise solution to the problem, including the necessary calculations and a graphical representation of the filter's frequency response.

### Slide 34

The image displays a slide from a presentation on the topic of "Resulting Spectrum." The slide is divided into two sections: a graph on the left and a summary on the right.

**Graph Section:**

*   The graph is titled "Resulting Spectrum" and features a logarithmic scale on both the x-axis (frequency) and y-axis (amplitude).
*   The x-axis is labeled with frequencies ranging from 4 kHz to 4000 kHz, while the y-axis is labeled with amplitudes in decibels (dB) from 0 to 40 dB.
*   A green line represents the frequency response of a filter, which starts at approximately 40 dB at low frequencies and rolls off at a rate of 20 dB/decade as the frequency increases.
*   The cutoff frequency (fc) is marked at 10 kHz, where the amplitude begins to decrease.
*   The graph also includes annotations indicating that the gain (A) is 40 dB, equivalent to 100 V/V.

**Summary Section:**

*   The summary section is titled "To Summarize:" and provides an overview of the key points related to the graph.
*   It highlights three levels of abstraction for analyzing the circuit:
    1.  **First Principles:** This involves applying fundamental principles such as Kirchhoff's Current Law (KCL), impedance (Zs) instead of resistance (Rs), and other basic circuit analysis techniques.
    2.  **Identify Familiar Circuits and Apply Results:** This level involves recognizing familiar circuit configurations and applying established results, such as using the gain formula for an inverting amplifier.
    3.  **System Black Level:** At this level, the focus is on understanding the overall system behavior, including the need for a particular amplitude and frequency response, and the use of active low-pass filters (LPFs).
*   Additionally, a note is made that noise is only slightly amplified.

In summary, the slide presents a graphical representation of the resulting spectrum of a single-stage, active, first-order low-pass filter used in an inverting amplifier configuration, along with a summary of the key concepts and principles involved in analyzing such a circuit.

### Slide 35

The image presents a lecture slide on Bandpass Filters, featuring a white background with a purple and black border at the top. The title "Bandpass Filters" is prominently displayed in bold black text.

**Main Content:**

* Four bullet points provide key information about bandpass filters:
	+ Only let frequencies in a certain range pass
	+ The range of frequencies is called the Bandwidth (BW)
	+ Goes from low to high -3dB frequencies (fL to fH)
	+ BW = fH - fL
* Three additional bullet points discuss center frequency and quality factor:
	+ Center Frequency (f0) is geometric mean: f0 = √(fLfH)
	+ Quality Factor (Q) is a measure of frequency selectivity: Q = f0/BW

**Handwritten Notes:**

* Blue handwriting on the right side of the slide explains the approach to be taken, including a diagram illustrating the process:
	+ Vin → HPF → LPF → Vout
	+ A = A1A2
* A graph below the diagram shows the frequency response of the filter, with annotations highlighting key features:
	+ fHPF = fL
	+ fLPF = fH
	+ |A|dB vs. f

**Additional Elements:**

* A logo in the bottom-right corner features a shield with a red and yellow design.
* The number "35" is printed in small text at the bottom center of the slide.

Overall, the slide provides a clear and concise overview of bandpass filters, including their definition, characteristics, and key parameters.

### Slide 36

The image presents a lecture slide on the topic of "Example: Bandpass" with a white background and a purple border at the top. The title is prominently displayed in large, bold black text.

**Main Content:**

*   The slide features a graph illustrating the frequency response of a bandpass filter, accompanied by a list of questions related to the filter's characteristics.
*   The graph displays the gain (in decibels) versus frequency, with the x-axis labeled "f" and the y-axis labeled "|A|dB." The graph shows a peak at the center frequency, with the gain decreasing as the frequency moves away from the center.
*   The questions posed on the slide include:
    *   What is the filter center frequency, upper and lower 3dB frequencies, bandwidth, and Q?
    *   What is the gain at the center frequency?

**Equations and Formulas:**

*   The slide presents several equations and formulas related to the bandpass filter, including:
    *   A(s) = -Zf/Zi
    *   Zf = Zcf || Rf
    *   Zi = Zci + Ri
    *   A(s) = -Rf/Ri \* sCi/(1+sRiCi) \* 1/(1+sRfCf)
    *   APB = -1
    *   fHPF = 1/(2πRiCi) = 100Hz
    *   fLPF = 1/(2πRfCf) = 100kHz
    *   BW = 100k - 100 = 99.9 kHz
    *   fo = √(100\*100k) = 3.162 kHz
    *   Q = fo/BW = 3.162k/99.9k = 0.032

**Circuit Diagram:**

*   A circuit diagram is shown on the right-hand side of the slide, illustrating the configuration of the bandpass filter.
*   The diagram includes components such as resistors (Ri and Rf), capacitors (Ci and Cf), and an operational amplifier.

**Additional Information:**

*   A URL is provided at the bottom of the slide: https://everycircuit.com/circuit/5103425825800192
*   The slide number "36" is displayed in the bottom center.

Overall, the slide provides a comprehensive overview of the bandpass filter, including its frequency response, equations, and circuit diagram.

### Slide 37

The image presents a detailed analysis of a passive bandpass filter, including its circuit diagram and mathematical derivations. The title "Passive Bandpass" is prominently displayed at the top left.

**Circuit Diagram:**

*   The circuit consists of two resistors (R1 and R2), two capacitors (C1 and C2), and a voltage source (Vin).
*   The input voltage (Vin) is connected to the circuit through R1.
*   The output voltage (Vout) is taken across C2.
*   The circuit is labeled as a High-Pass Filter (HPF) and Low-Pass Filter (LPF) in series.

**Mathematical Derivations:**

*   The transfer function of the circuit is derived using nodal analysis.
*   The equations are written in blue and red ink, with some steps highlighted in red.
*   The derivation involves calculating the impedance of the capacitors (Zc1 and Zc2) and applying Kirchhoff's Current Law (KCL) to the nodes.
*   The resulting transfer function is expressed as a ratio of polynomials in s, where s is the complex frequency variable.
*   The transfer function is simplified and rearranged to show that it represents a second-order filter.

**Key Points:**

*   The circuit is complicated by loading effects.
*   The transfer function is derived using nodal analysis.
*   The filter is truly a second-order filter.
*   The derivation assumes no loading effects.

**Equations:**

*   Vout/Vin = A(s) = sR1C1 / [s^2R1R2C1C2 + s(R1C1 + R2C2 + R1C2) + 1]
*   A(s) = (sR1C1 / (sR1C1 + 1)) \* (1 / (sR2C2 + 1))

**Additional Information:**

*   The slide mentions that the topic will be covered in more detail in MTE 252 and 360.
*   The slide number (37) is displayed at the bottom center.

Overall, the image provides a comprehensive analysis of a passive bandpass filter, including its circuit diagram and mathematical derivations. The derivation is detailed and step-by-step, making it easy to follow along.

### Slide 38

The image presents a slide from a presentation on "Band Reject Filters," a topic in electrical engineering or signal processing. The slide is divided into sections, each containing key information about band reject filters.

**Title and Main Points**

*   The title "Band Reject Filters" is prominently displayed at the top left of the slide.
*   Three main points are listed below the title:
    *   Blocks a certain range of frequencies
        *   Also called Notch
    *   Often for removing noise at a known frequency

**Use Case Examples**

*   A list of use case examples is provided, including:
    *   60 Hz powerline EMI
    *   Switching regulator noise
    *   Clock frequencies
    *   PWM "Pulse Repetition Frequency"
    *   Other known problematic frequencies (e.g., nearby frequencies in use)

**Previous Setup**

*   A graph illustrating the previous setup is shown, with labels "LPF" and "HPF" and an arrow indicating the transition from HPF to LPF.

**Realistic First-Order Implementation**

*   A block diagram is presented, showing the implementation of a band reject filter using a low-pass filter (LPF) and a high-pass filter (HPF).
*   The diagram includes:
    *   Vin (input voltage)
    *   LPF and HPF blocks
    *   Vout (output voltage)
    *   A note stating that this implementation requires 3 opamp circuits and is complex, making it not worth it.

**Frequency Response Graph**

*   A graph illustrates the frequency response of the band reject filter, with:
    *   |A|dB on the y-axis
    *   f on the x-axis
    *   A shaded region indicating the rejected frequency range
    *   Labels fL/10, fL, f0, fH, and 10fH on the x-axis

**Practical Considerations**

*   Two practical considerations are noted:
    *   Higher-order filter
    *   Look for custom IC (Digi-key)
    *   Tackle in software

The slide provides a comprehensive overview of band reject filters, including their definition, use cases, and implementation considerations.

### Slide 39

The image presents a detailed lecture slide on designing a band-reject filter, a type of electronic filter that attenuates a specific frequency band while allowing all other frequencies to pass through.

**Title and Problem Statement**

* The title "Example: Band Reject" is prominently displayed at the top-left corner of the slide.
* The problem statement is: "Make a band reject filter with in-band gain of 40 dB, a center frequency of 10 kHz, and a bandwidth of 99 kHz."

**Key Parameters and Equations**

* The given parameters are:
	+ In-band gain (ApB) = 40 dB = 100 V/V
	+ Center frequency (f0) = 10 kHz
	+ Bandwidth (BW) = 99 kHz
* The equations used to solve the problem are:
	1. f0 = √(fL \* fH) = 10 kHz
	2. BW = fH - fL = 99 kHz

**Graph and Frequency Calculations**

* A graph is shown with a frequency axis, illustrating the band-reject filter's frequency response.
* The graph has two curves: one for the low-pass filter (LPF) and one for the high-pass filter (HPF).
* The lower cutoff frequency (fL) and upper cutoff frequency (fH) are calculated using the given equations.
* The calculated values are:
	+ fH = 100 kHz
	+ fL = 1 kHz

**Circuit Diagram and Component Labels**

* A circuit diagram is shown on the right-hand side of the slide, illustrating the implementation of the band-reject filter.
* The circuit consists of:
	+ A low-pass filter (LPF) and a high-pass filter (HPF) connected in parallel.
	+ An inverting summing amplifier.
* The component labels are:
	+ Rf1, Ri1, Cf1 for the LPF
	+ Rf2, Ri2, Ci2 for the HPF
	+ Rf3, Ri3 for the summing amplifier

**Gain Calculations and Component Values**

* The pass-band gain (ApB) is given as 100, which is split between the LPF, HPF, and summing amplifier.
* The gain distribution is:
	+ x10 in LPF and HPF
	+ x10 in summing amplifier
* The slide notes that there are 9 unknowns and 5 constraints, requiring 4 values to be chosen.

**Additional Notes**

* The slide includes additional notes and reminders, such as the need to choose 4 values (e.g., try 10 kΩ) and the presence of 9 unknowns and 5 constraints.

### Slide 40

The image presents a comprehensive summary of first-order passive and active filters, organized into a table with four rows and three columns. The title, "Summary: First-order Passive and Active Filters," is prominently displayed at the top.

**Table Structure:**

*   **Type**: Lists the types of filters, including Low Pass, High Pass, Band Pass, and Band Reject.
*   **Passive**: Provides equations and diagrams for passive filter implementations.
*   **Active**: Offers equations and diagrams for active filter implementations.

**Key Points:**

*   **Low Pass Filter:**
    *   Passive: The transfer function is given by $A_{LPF} = \frac{1}{\frac{s}{\omega_c} + 1}$, with a circuit diagram showing a resistor (R) and capacitor (C) configuration.
    *   Active: The transfer function is $A = A_{PB} \cdot A_{LPF} = -\frac{R_f}{R_i}(\frac{1}{\frac{s}{\omega_c}+1})$, with a circuit diagram featuring an operational amplifier (op-amp) and resistors/capacitors.
*   **High Pass Filter:**
    *   Passive: The transfer function is $A_{HPF} = \frac{\frac{s}{\omega_c}}{\frac{s}{\omega_c}+1}$, accompanied by a circuit diagram illustrating an inductor (L) and resistor (R) configuration.
    *   Active: The transfer function is $A = A_{PB} \cdot A_{HPF} = -\frac{R_f}{R_i}(\frac{\frac{s}{\omega_c}}{\frac{s}{\omega_c}+1})$, with a corresponding op-amp circuit diagram.
*   **Band Pass Filter:**
    *   Passive: A diagram shows a cascaded low-pass and high-pass filter configuration, with a note indicating that this will work but may require buffering due to loading effects.
    *   Active: The transfer function is $A = A_{PB} \cdot A_{LPF} \cdot A_{HPF} = -\frac{R_f}{R_i}(\frac{1}{\frac{s}{\omega_{LPF}}+1})(\frac{\frac{s}{\omega_{HPF}}}{\frac{s}{\omega_{HPF}}+1})$, featuring a circuit diagram with multiple op-amps.
*   **Band Reject Filter:**
    *   A diagram illustrates a parallel combination of low-pass and high-pass filters, with a summation node, and a note mentioning that practical implementations often exceed first-order filters.

**Additional Notes:**

*   The image includes handwritten notes in blue ink, providing additional context and explanations for the filter configurations and transfer functions.
*   A logo is visible in the bottom-right corner, although its details are not discernible.

Overall, the image serves as a concise reference for understanding the fundamental principles and implementations of first-order passive and active filters, covering various filter types and their characteristics.

### Slide 41

The image is a slide from a presentation, likely related to computer science or engineering. The slide's title, "Appendix A: Second-Order Filters," is prominently displayed in large black text at the bottom center of the page.

Here are the key elements of the image:

* **Header Section**
	+ A purple gradient bar spans the top of the image.
	+ Below the bar, a circuit board pattern is visible, featuring various shades of blue and green.
* **Main Content**
	+ The majority of the slide is blank, with a white background.
	+ The title "Appendix A: Second-Order Filters" is centered at the bottom of the page in large black text.
* **Footer Section**
	+ A small number "41" is printed in black text at the very bottom center of the page, likely indicating the slide number.
	+ In the bottom-right corner, a logo is visible, consisting of a yellow shield with a red design inside, accompanied by a black and white diagonal stripe.

In summary, the image presents a slide from a technical presentation, focusing on second-order filters, with a clean design and a prominent title.

### Slide 42

The image presents a slide titled "Limits of First Order Filters" in bold black text at the top left. The slide is divided into two sections: a text section on the left and a graph section on the right.

**Text Section:**

*   Two bullet points are listed below the title:
    *   The first bullet point states, "First order filters can be used to create bandpass and band-reject filters _if_ the corner frequencies are far away from each other."
    *   The second bullet point reads, "Too close (within about 4x), then there's not enough attenuation (-20dB/decade in first-order filters)."

**Graph Section:**

*   A graph is displayed on the right side of the slide, featuring a white background with a black border.
*   The y-axis is labeled "|A|dB" and ranges from -60 to 0, while the x-axis is labeled "f" and spans from an unspecified lower limit to an unspecified upper limit.
*   Three curves are plotted on the graph:
    *   A blue curve represents the frequency response of a filter with a low cutoff frequency (fL) and a high cutoff frequency (fH), where fH < 4fL.
    *   A black curve illustrates the frequency response of a filter with fH > 4fL.
    *   A red dashed line indicates the -3 dB point, which corresponds to the half-power point of the filter.
*   The graph also includes annotations:
    *   "fL" is written next to the lower cutoff frequency.
    *   "fH < 4fL" is written above the blue curve.
    *   "fH > 4fL" is written above the black curve.

In summary, the slide discusses the limitations of first-order filters in creating bandpass and band-reject filters, highlighting the importance of having corner frequencies that are sufficiently far apart. The accompanying graph illustrates the frequency response of these filters, demonstrating how the separation between cutoff frequencies affects their performance.

### Slide 43

The slide is titled "Limits of First Order Filters." The title is in large, bold black text at the top of the slide.

**Text Content:**

* Three bullet points are listed below the title:
  * "What if you want faster attenuation with frequency? Could just chain identical first-order filters."
  * "But recall this is just an approximation to a smoother curve"
  * "Need higher-order filters to do better than -20dB/decade with sharper transition from passband"

**Diagram:**

* A simple block diagram is drawn below the bullet points, showing three identical low-pass filters (LPF) connected in series. The input is labeled "Vin" and the output is labeled "Vout." The diagram is hand-drawn and includes the notation "all at ω0."

**Graphs:**

* Two graphs are displayed on the right side of the slide, both showing the frequency response of a filter.
  * The top graph has a blue, green, and red curve, with the x-axis labeled "ω rad/s" and the y-axis labeled "|A(s)|dB." The graph shows the frequency response of a filter, with the curves representing different orders or configurations.
  * The bottom graph is similar to the top graph, with the same x-axis and y-axis labels, and the same three curves (blue, green, and red).

**Additional Elements:**

* A logo is displayed in the bottom-right corner of the slide, featuring a shield with a red and yellow design.
* The slide number "43" is displayed at the bottom center of the slide.

Overall, the slide discusses the limitations of first-order filters and the need for higher-order filters to achieve faster attenuation with frequency. The diagrams and graphs provide visual aids to illustrate the concepts being discussed.

### Slide 44

The image presents a slide from a lecture on "Second Order Circuits," featuring a white background with black text and blue handwritten notes. The title, "Second Order Circuits," is prominently displayed at the top in bold, black font.

**Main Content:**

* Four bullet points summarize the key concepts:
	+ Second-order circuits involve two derivatives (s^2) separating states in the circuit.
	+ Resonance occurs when energy transfers from one form to another in a periodic manner, or when a physical system supports waves of particular frequencies.
	+ Resonance is characteristic of second- and higher-order systems, whereas first-order systems are governed by diffusion equations, such as heat transfer.
	+ Physical examples are provided, including:
		- A stick figure pushing a swing, illustrating the transfer of potential energy to kinetic energy.
		- A diagram of a frictionless mass-spring system, highlighting the exchange between spring energy and momentum.

**Handwritten Notes:**

* The handwritten notes in blue ink provide additional explanations and examples:
	+ Potential energy is converted to kinetic energy, and vice versa.
	+ The equation for the force exerted by a spring is given as F = -k \* x, where k is the spring constant and x is the displacement.
	+ The equation for momentum is F = m \* a = m \* ẍ, where m is the mass, a is the acceleration, and ẍ is the second derivative of displacement with respect to time.

**Additional Elements:**

* A small logo is visible in the bottom-right corner of the slide, although its details are not discernible.
* The number "44" is printed in small text at the bottom center of the slide, likely indicating the slide number.

Overall, the slide effectively conveys the fundamental concepts of second-order circuits and resonance, using a combination of typed text and handwritten notes to facilitate understanding.

### Slide 45

The image presents a slide titled "LC Circuit" in the top-left corner, featuring a diagram and accompanying equations. The diagram is situated on the left side of the image, while the equations are on the right.

*   **Diagram:**
    *   The diagram depicts an LC circuit consisting of an inductor (L) and a capacitor (C).
    *   The inductor is represented by a coil symbol, and the capacitor is depicted as two parallel plates.
    *   The circuit is shown with a current (I) flowing through it, indicated by an arrow.
    *   The voltage across the capacitor is labeled as V.
    *   The diagram also includes labels for the magnetic field and electric field.
*   **Equations:**
    *   The first equation states that L and C are separated by two derivatives.
    *   The second equation expresses the voltage across the inductor as V = L(dI/dt).
    *   The third equation represents the current through the capacitor as -I = C(dV/dt).
    *   The fourth equation is derived from the previous two, resulting in (1/LC)V + (d^2V/dt^2) = 0.
    *   The fifth equation defines the resonant frequency (ω0) as 1/√(LC).
*   **Additional Text:**
    *   The slide includes additional text that reads, "Say 1/LC = ω0^2 ('Resonant Freq.')".
*   **Background and Layout:**
    *   The background of the slide is white, with a purple gradient bar at the top.
    *   The title "LC Circuit" is displayed in bold black font at the top-left corner.
    *   The diagram and equations are presented in a clear and organized manner, making it easy to follow the explanation.

In summary, the image effectively illustrates the concept of an LC circuit, including its components, equations, and resonant frequency. The diagram and equations work together to provide a comprehensive understanding of the circuit's behavior.

### Slide 46

The image depicts a lecture slide focused on RLC circuits, featuring handwritten notes and a diagram. The content is organized into several key points:

**Title and Main Points**

* Title: "RLC Circuits"
* Main point: "R dissipates the resonant energy as heat (I^2R losses)"

**Equations and Formulas**

* Equivalent impedance (Zeq) is derived as:
  * Zeq = R || ZL || Zc
  * = (1/R + 1/sL + sC)^-1
  * = sRL / (s^2RLC + sL + R)

**Definitions and New Terms**

* Definitions of new terms:
  * ω0 = 1/√(LC) = "Resonant Frequency"
  * "zeta" ζ = α/ω0 = "Damping Factor"
  * α = "Damping Attenuation" (s = e^(-αt) * e^(jωt))

**Circuit Diagram and Specifics**

* A diagram of an RLC circuit is shown, with components R, L, and C in parallel.
* For this specific circuit:
  * α = 1/(2RC)
  * ζ = 1/(2R) * √(L/C)
  * Zeq = (1/C)s / (s^2 + (1/RC)s + 1/LC) = (1/C)s / (s^2 + 2αs + ω0^2)

**Additional Information**

* A statement: "There are many ways to arrange R, L, and C."
* A page number "46" is visible at the bottom center of the slide.
* A logo is present in the bottom-right corner, featuring a shield with a red and black design.

### Slide 47

The image presents a slide from a presentation on RLC Passive Filters, featuring two circuit diagrams and their corresponding transfer functions. The title "RLC Passive Filters" is prominently displayed in large black text at the top left of the slide.

**Circuit Diagrams:**

*   **Low-Pass Filter:**
    *   The low-pass filter circuit diagram is situated below the title.
    *   It consists of a voltage source (Vi) connected to a resistor (R), an inductor (L), and a capacitor (C) in series.
    *   The output voltage (Vo) is taken across the capacitor.
*   **High-Pass Filter:**
    *   The high-pass filter circuit diagram is located below the low-pass filter diagram.
    *   It comprises a voltage source (Vi) connected to a resistor (R), a capacitor (C), and an inductor (L) in series.
    *   The output voltage (Vo) is taken across the inductor.

**Transfer Functions:**

*   **Low-Pass Filter:**
    *   The transfer function for the low-pass filter is given by the equation: Av = Vo/Vi = 1/(s^2 + (R/L)s + 1/LC)
    *   The resonant frequency (ωo) is calculated using the formula: ωo = 1/√(LC)
    *   The quality factor (Qo) is determined by the equation: Qo = 1/R \* √(L/C)
*   **High-Pass Filter:**
    *   The transfer function for the high-pass filter is represented by the equation: Av = Vo/Vi = s^2/(s^2 + (R/L)s + 1/LC)
    *   The resonant frequency (ωo) is calculated using the same formula as for the low-pass filter: ωo = 1/√(LC)
    *   The quality factor (Qo) is also determined by the same equation as for the low-pass filter: Qo = 1/R \* √(L/C)

In summary, the slide provides a concise overview of RLC passive filters, including their circuit diagrams and transfer functions, as well as key parameters such as resonant frequency and quality factor.

### Slide 48

The image depicts a slide from a presentation on RLC passive filters. The title, "RLC Passive Filters," is prominently displayed in bold black text at the top left of the slide.

**Circuit Diagrams**

The slide features two circuit diagrams:

*   **Band-pass filter**: The first diagram illustrates a band-pass filter, comprising an inductor (L), capacitor (C), and resistor (R) connected in series with a voltage source (Vi) and output voltage (Vo).
*   **Band-stop filter**: The second diagram shows a band-stop filter, consisting of a resistor (R), inductor (L), and capacitor (C) connected in series with a voltage source (Vi) and output voltage (Vo).

**Equations**

To the right of each diagram, the corresponding equations are provided, including:

*   **Transfer function (Av)**: The ratio of output voltage (Vo) to input voltage (Vi)
*   **Resonant frequency (ωo)**: The frequency at which the filter is designed to operate
*   **Quality factor (Qo)**: A measure of the filter's selectivity or bandwidth

The equations are presented in a clear and concise manner, with variables and constants defined as follows:

*   **s**: The complex frequency variable
*   **L**: Inductance
*   **C**: Capacitance
*   **R**: Resistance

**Slide Details**

The slide is numbered "48" at the bottom center, indicating its position within the presentation. A logo is visible in the bottom-right corner, although its details are not discernible.

Overall, the slide provides a concise and informative overview of RLC passive filters, including their circuit configurations and key equations.

### Slide 49

**Generalized Second-Order Response**

*   A second-order system will have a transfer function like this:

    $H(s) = \frac{\omega_0^2}{s^2 + 2\alpha s + \omega_0^2} = \frac{\omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2} = \frac{\omega_0^2}{s^2 + \frac{\omega_0}{Q} s + \omega_0^2}$

    *   Handwritten note: "Numerator changes of circuit config."
    *   Handwritten note: "Denom. is for all second-order systems"

*   The denominator has two roots (poles):

    $\omega_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2} = \omega_0\left[\sqrt{1 + \left(\frac{1}{2Q_0}\right)^2} \pm \frac{1}{2Q_0}\right] = -\zeta\omega_0 \pm j\omega_0\sqrt{1-\zeta^2}$

### Slide 50

The image presents a slide titled "Generalized Second-Order Response" in large black text at the top, set against a white background with a purple gradient bar above it. The slide is divided into two main sections: a list of bullet points on the left and a table with accompanying equations on the right.

**Title and Header**
* Title: "Generalized Second-Order Response"
* Purple gradient bar above the title

**Left Section: Bullet Points**
* A single bullet point stating, "There are many, but very related parameters:" followed by a table

**Table: Parameters and Definitions**
* A 7-row, 2-column table with light purple headers and rows
| Parameter | Definition |
| --- | --- |
| $\omega_0$ | Natural Frequency |
| BW | Bandwidth |
| $\omega_d$ | Damped Natural Frequency |
| $\omega_{1,2}$ | Pole locations |
| $\alpha$ | Damping Attenuation |
| $\zeta$ | Damping Factor, Damping Ratio |
| $Q_0$ | Quality Factor |

**Right Section: Equations**
* Five bullet points with equations:
  * $\omega_0 = \sqrt{\omega_1\omega_2} = \frac{1}{\sqrt{LC}}$
  * $\text{BW} = \omega_2 - \omega_1 = \frac{\omega_0}{Q_0} = 2\alpha$
  * $\omega_d = \sqrt{\omega_0^2 - \alpha^2} = \omega_0\sqrt{1 - \left(\frac{1}{2Q_0}\right)^2}$
  * $\alpha = \frac{\omega_0}{2Q_0} = 2\zeta Q_0 = \frac{\text{BW}}{2}$
  * $\zeta = \frac{\alpha}{\omega_0} = \frac{1}{2Q_0}$

**Footer**
* A small number "50" centered at the bottom
* A logo in the bottom-right corner featuring a shield with a red and yellow design

This detailed description captures all the information presented on the slide, including the title, bullet points, table, equations, and footer elements.

### Slide 51

The image presents a comprehensive overview of the generalized second-order response, featuring a detailed diagram and accompanying notes.

**Title**
The title, "Generalized Second-Order Response," is prominently displayed in bold black text at the top of the image.

**Main Content**
Below the title, a bullet point states, "Depending on the parameters, the roots can be real or complex conjugate." This is followed by a diagram illustrating the relationship between the roots and the parameters. The diagram consists of:

* A circle with its center at the origin, labeled with various mathematical expressions and symbols.
* Two axes: the real axis (α) and the imaginary axis (jω).
* Several points and lines are marked on the diagram, including:
	+ s = -α + jωd
	+ s = -α - jωd
	+ ζ = 1
	+ ωn
	+ cos^-1(ζ)
	+ θ

**Notes**
To the right of the diagram, handwritten notes in blue and green ink provide additional information:

* "Note about rolloff:" in blue ink.
* "There is a total change of slope of 40 dB when traversing the frequency spectrum (Bode magnitude plot). E.g." in blue ink.
* A simple graph illustrating the change in slope, with labels indicating the frequency spectrum and the corresponding slope changes.

**Additional Elements**
In the bottom-right corner, a logo featuring a shield with a red and yellow design is visible. The background of the image is white, with a purple gradient bar at the top. The number "51" is printed in small black text at the bottom center of the image.

Overall, the image provides a detailed explanation of the generalized second-order response, including its mathematical representation and graphical illustration.

### Slide 52

The image presents a slide titled "Generalized Second-Order Response," which appears to be part of a presentation on control systems or signal processing. The slide is divided into two main sections: a list of bullet points and a series of graphs.

**Title and Bullet Points**

*   The title, "Generalized Second-Order Response," is prominently displayed at the top of the slide.
*   Below the title, a bullet point reads: "Depending on the parameters, the poles can be:"
    *   a) Undamped (ζ = 0)
    *   b) Underdamped (ζ < 1)
    *   c) Critically Damped (ζ = 1)
    *   d) Overdamped (ζ > 1)

**Graphs**

*   The right side of the slide features four pairs of graphs, each corresponding to one of the damping conditions listed above.
*   Each pair consists of a pole-zero plot and a time-domain response graph.
*   The pole-zero plots show the location of the poles in the complex plane, with the real axis on the x-axis and the imaginary axis on the y-axis.
*   The time-domain response graphs display the system's output over time, with the x-axis representing time and the y-axis representing the amplitude of the response.

**Pole-Zero Plots and Time-Domain Responses**

*   For ζ = 0 (Undamped):
    *   Pole-zero plot: Two poles on the imaginary axis.
    *   Time-domain response: Sustained oscillations.
*   For 0 < ζ < 1 (Underdamped):
    *   Pole-zero plot: Two complex conjugate poles in the left half-plane.
    *   Time-domain response: Damped oscillations.
*   For ζ = 1 (Critically Damped):
    *   Pole-zero plot: Two real poles at the same location on the real axis.
    *   Time-domain response: No oscillations, with the response decaying exponentially.
*   For ζ > 1 (Overdamped):
    *   Pole-zero plot: Two distinct real poles on the real axis.
    *   Time-domain response: No oscillations, with the response decaying exponentially.

**Additional Elements**

*   A logo is visible in the bottom-right corner of the slide, although its details are not discernible.
*   The slide number "52" is displayed at the bottom center.

In summary, the slide provides a concise overview of the different types of second-order responses based on the damping ratio (ζ), accompanied by illustrative graphs that demonstrate the corresponding pole-zero plots and time-domain responses.

### Slide 53

The image presents a lecture slide titled "Various Damping Factors" and features three graphs. The slide is divided into two sections: the left side contains a single graph, while the right side displays two graphs.

**Left Section:**

*   The graph is labeled "Unit step response, H0,LP =1, ω0 =1, ζ varies."
*   It plots y(t) against time, showcasing the unit step response for different damping factors (ζ).
*   The graph includes multiple colored lines representing various damping factors, ranging from ζ = 0.1 to ζ = 4.
*   A legend in the lower right corner of the graph provides a key to the different colors and their corresponding damping factors.

**Right Section:**

*   The top-right graph displays the magnitude (in decibels) against frequency (ω/ωn), illustrating the frequency response of a system with varying damping factors.
*   The graph features multiple colored lines, each representing a different damping factor, and includes labels for the low-frequency asymptote and high-frequency asymptote.
*   The bottom-right graph plots the phase (in degrees) against frequency (ω/ωn), demonstrating the phase response of the system for different damping factors.
*   This graph also includes multiple colored lines representing various damping factors.

**Additional Elements:**

*   The slide number "53" is visible at the bottom center.
*   A logo is present in the bottom-right corner, although its details are not discernible.

Overall, the slide effectively illustrates the impact of different damping factors on the unit step response and frequency response of a system, providing a clear visual representation of the concepts being discussed.

### Slide 54

The image presents a slide titled "Bode Plot of Second Order" with two graphs and a logo.

**Title and Header**
The title is prominently displayed in large, bold, black font at the top left of the slide. A horizontal bar above the title features a gradient that transitions from light purple to dark purple.

**Graphs**

*   The left graph is a Bode plot, characterized by:
    *   A white background with a grid pattern.
    *   A black line representing the magnitude response, which decreases as frequency increases.
    *   Three blue dashed lines indicating different damping ratios (ζ = 0.1, ζ = 0.3, and ζ = 0.707).
    *   The y-axis labeled "A dB" ranges from -50 to 20.
*   The right graph displays:
    *   A pink curve representing a frequency response.
    *   A green shaded area under the curve between ω1 and ω2.
    *   The x-axis labeled "ω" with three points marked: ω1, ω0, and ω2.
    *   The y-axis is unlabeled.

**Footer and Logo**

*   The number "54" is centered at the bottom of the slide.
*   A logo is positioned in the bottom-right corner, featuring a yellow shield with a red and black design.

The slide's background is white, providing a clean and neutral backdrop for the graphs and other elements.

### Slide 55

The slide presents an example problem related to designing a parallel RLC circuit. The title, "Example Problem: Parallel RLC," is prominently displayed at the top.

**Problem Statement:**

*   Design a parallel RLC circuit with input current (Iin) and output voltage (Vout) such that:
    *   Resonant frequency (fo) = 1 MHz
    *   Quality factor (Qo) = 10
    *   Resistance (R) = 50 Ω
    *   The task is to determine the values of inductance (L) and capacitance (C)

**Circuit Diagram:**

A circuit diagram is provided, illustrating a parallel RLC circuit with the following components:

*   Input current source (Iin)
*   Resistance (R)
*   Inductance (L)
*   Capacitance (C)
*   Output voltage (Vout)

**Equations and Formulas:**

The slide includes several equations and formulas used to solve the problem:

*   Resonant frequency equation: ωo = 1/√(LC) = 2πfo = 2π(1M)
*   Quality factor equation: Qo = ωoRC = 10
*   Derived values:
    *   C = 31.83 nF
    *   L = 795.8 nH
*   Additional formulas are provided in a green box:
    *   Qo = ωoRC
    *   α = 1/(2RC)

**Recall Section:**

A "Recall" section is included, listing relevant formulas:

*   Q = fo/BW
*   BW = fo/Q = 1M/10 = 100 kHz

**Additional Notes:**

*   A handwritten note suggests that Iin could represent an antenna.

Overall, the slide provides a comprehensive example problem for designing a parallel RLC circuit, including the necessary equations and formulas to determine the required component values.

### Slide 56

The image presents a lecture slide titled "Example Problem: RLC Filter." The slide is divided into two main sections: a circuit diagram on the left and a series of statements and equations on the right.

**Circuit Diagram:**

*   The circuit consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series.
*   The input voltage is denoted as V_i, and the output voltage is denoted as V_o.
*   The circuit is drawn with the input voltage on the left and the output voltage on the right.

**Transfer Function and Equations:**

*   The transfer function A(s) is given by the equation: A(s) = s^2 / (s^2 + s(ω_0/Q_0) + ω_0^2)
*   A series of equations are derived to determine the transfer function, including:
    *   V_o/V_i = Z_L / (Z_L + R + Z_C)
    *   V_o/V_i = sL / (sL + R + 1/sC)
    *   V_o/V_i = s^2LC / (s^2LC + sRC + 1)

**Multiple-Choice Statements:**

*   The slide presents a table with four statements related to the filter:
    *   active/passive
    *   low pass/high pass/band pass
    *   first order/second order/higher than second order
*   The correct answers are circled in red: "passive," "high pass," and "second order."

**Derivation of Transfer Function:**

*   The slide shows a step-by-step derivation of the transfer function, including:
    *   V_o/V_i = s^2 / (s^2 + s(1/RC) + 1/LC)
    *   1/LC = ω_0^2
    *   R/L = ω_0/Q_0
    *   Q_0 = ω_0L/R = (1/R)√(L/C)

**Additional Information:**

*   The slide number "56" is visible at the bottom center.
*   A logo is present in the bottom-right corner, featuring a shield with a red and yellow design.

### Slide 57

The slide is titled "Higher-Order Filters" and contains the following elements:

**Text:**
* Two bullet points:
  * "For low Q (~fH ≥ 4fL) you can cascade separate low- and high-pass circuits"
  * "High-Q requires a single higher-order stage"

**Diagrams and Figures:**
* A circuit diagram (Figure 6.5, left) showing an LC bandpass filter with:
  + Inductances labeled in mH
  + Capacitances labeled in pF
  + Component values:
    - 5725 pF capacitors
    - 97.5 mH, 605 mH, 143 mH inductors
    - 4979 pF, 5236 pF, 5025 pF, 583 pF capacitors
    - 16 mH inductors (multiple instances)
  + Source resistance (Rs) = 10k
  + Load resistance (RL) = 10k
* A graph (Figure 6.5, right) showing the measured response of the filter circuit with:
  + X-axis labeled "Frequency (kHz)"
  + Y-axis labeled "Relative Attenuation (dB)"
  + A curve showing the frequency response, with a sharp attenuation around 17-18 kHz

**Caption:**
* "Figure 6.5. Left: An unusually good LC bandpass filter (inductances in mH, capacitances in pF). Right: measured response of the filter circuit. The admirably sharp frequency response comes at the expense of degraded phase response; see discussion in §6.2.5. The 0 dB value in the response curve corresponds to ~9 dB of loss, assuming 10k source and load impedances."

**Other Elements:**
* A logo in the bottom-right corner, featuring a shield with a red and yellow design
* A page number "57" at the bottom center of the slide

### Slide 58

The image presents a slide from a presentation, titled "Appendix B: Bode Plot Reference." The slide is divided into two main sections: the top section features a graphic, and the bottom section contains text.

**Top Section:**

* A horizontal band spanning the width of the slide
* The band is composed of three distinct colors:
	+ Black (top)
	+ Purple (middle)
	+ White (bottom)
* Below the band, a graphic of a circuit board is displayed
* The circuit board is depicted in shades of blue and green, with silver dots and lines

**Bottom Section:**

* The title "Appendix B: Bode Plot Reference" is prominently displayed in large black text
* The number "58" is centered at the bottom of the slide, likely indicating the slide number
* A small logo is situated in the bottom-right corner
* The logo features a shield with a red and yellow design, accompanied by a black diagonal line

The background of the slide is white, providing a clean and neutral backdrop for the content.

### Slide 59

The slide is titled "TF → Bode: Constant Factor" and contains the following elements:

**Title and Equation**

* Title: "TF → Bode: Constant Factor"
* Equation: A(s) = APB, located in the top-right corner

**Bullet Points**

* Two bullet points:
	+ "Called the passband gain, APB"
	+ "Multiplying by a real constant shifts the magnitude vertically by |APB|dB and does not change the phase"

**Graphs**

* Two graphs, side by side:
	+ **Left Graph**
		- Vertical axis: |A(s)|dB
		- Horizontal axis: ω
		- A blue horizontal line is plotted, representing the magnitude
		- The line is labeled "|APB|dB"
	+ **Right Graph**
		- Vertical axis: ∠A(s)
		- Horizontal axis: ω
		- A blue horizontal line is plotted, representing the phase
		- The line is at 0°

**Additional Elements**

* A logo in the bottom-right corner, featuring a shield with a red and yellow design
* A number "59" at the bottom center of the slide, likely indicating the slide number
* A gradient bar at the top, transitioning from black to purple to light purple

### Slide 60

The slide is titled "TF → Bode: Zero at Origin" and presents information about transfer functions and Bode plots. Here's a detailed breakdown of the slide's content:

**Title and Equation**

* The title is "TF → Bode: Zero at Origin"
* The equation is: $A(s) = s\tau_0 = \frac{s}{\omega_0} = \frac{j\omega}{\omega_0}$

**Bullet Points**

* "In numerator, so 10x frequency gives 10x gain (+20 dB)"
* "0 dB at $\omega = \omega_0$, $90^\circ$ at all frequencies (j in numerator)"

**Graphs**

* Two graphs are presented side-by-side:
	+ **Left Graph:**
		- The x-axis is labeled "$\omega$" and ranges from $\omega_0/10$ to $10\omega_0$
		- The y-axis is labeled "$|A(s)|_{dB}$" and ranges from -20 to 20
		- The graph shows a blue line that:
			- Starts at a negative value on the y-axis at $\omega = \omega_0/10$
			- Crosses the x-axis at $\omega = \omega_0$
			- Increases to a positive value on the y-axis at $\omega = 10\omega_0$
			- The line is straight and has a positive slope
	+ **Right Graph:**
		- The x-axis is labeled "$\omega$"
		- The y-axis is labeled "$\angle A(s)$" and has a value of $90^\circ$ at the top
		- The graph shows a blue line that:
			- Remains constant at $90^\circ$ across all frequencies on the x-axis

**Additional Elements**

* A logo is present in the bottom-right corner of the slide, featuring a shield with a red and yellow design.
* The number "60" is displayed at the bottom center of the slide, likely indicating the slide number.

### Slide 61

The image presents a slide from a lecture on Bode plots, specifically focusing on the pole at the origin. The title "TF → Bode: Pole at Origin" is prominently displayed at the top left.

**Key Points and Equations:**

*   The transfer function A(s) is defined as 1/(sτ0) = ω0/s = ω0/(jω).
*   Two bullet points provide additional information:
    *   The denominator affects the frequency response, with a 10x increase in frequency resulting in a (1/10)x gain (-20 dB).
    *   At ω = ω0, the gain is 0 dB, and the phase angle is -90° at all frequencies due to the presence of j in the denominator, which is equivalent to -j in the numerator.

**Bode Plots:**

The slide features two Bode plots:

1.  **Magnitude Plot:**
    *   The magnitude plot displays the gain in decibels (dB) on the y-axis versus frequency (ω) on the x-axis.
    *   The plot shows a straight line with a negative slope, indicating a decrease in gain as frequency increases.
    *   Key points on the plot include:
        *   ω0/10
        *   ω0 (0 dB gain)
        *   10ω0
2.  **Phase Plot:**
    *   The phase plot displays the phase angle on the y-axis versus frequency (ω) on the x-axis.
    *   The plot shows a constant phase angle of -90° across all frequencies.

**Additional Details:**

*   The slide number "61" is visible at the bottom center.
*   A logo is present in the bottom-right corner, featuring a shield with a red and yellow design.

### Slide 62

The image presents a slide from a presentation on control systems, specifically focusing on the Bode plot of a real zero transfer function. The title "TF → Bode: Real Zero" is prominently displayed at the top.

**Key Elements:**

* **Title and Equation:**
	+ Title: "TF → Bode: Real Zero"
	+ Equation: A(s) = sτ0 + 1 = s/ω0 + 1 = jω/ω0 + 1
* **Bullet Points:**
	+ Low Freq: → 1 (0 dB)
	+ High Freq: → jω/ω0
	+ Transitions at ω0
* **Bode Plots:**
	+ Magnitude Plot (|A(s)|dB vs. ω)
		- Blue line at 0 dB for low frequencies
		- Red line with a slope of +20 dB/decade for high frequencies
		- Transition at ω0
	+ Phase Plot (∠A(s) vs. ω)
		- Blue line at 0° for low frequencies
		- Purple line increasing from 0° to 90° around ω0
		- Red line at 90° for high frequencies

**Summary:**

The slide illustrates the Bode plot of a real zero transfer function, highlighting its characteristics in both magnitude and phase. The plots demonstrate how the transfer function behaves at low and high frequencies, with a transition occurring at ω0. The equation provided relates the transfer function to the frequency ω and the parameter ω0.

### Slide 63

The image is a presentation slide discussing the Bode plot of a transfer function with a real pole.

**Title and Equations**

* The title at the top of the slide reads "TF → Bode: Real Pole" in black text.
* The equation for A(s) is given as:
  A(s) = 1 / (sτ0 + 1) = 1 / (s/ω0 + 1) = 1 / (jω/ω0 + 1)

**Key Points**

* Two bullet points highlight key aspects of the transfer function:
  * "Low Freq: → 1 (0 dB); High Freq: → ω0/jω; Transitions at ω0" 
  * "Same as lowpass TF"

**Bode Plots**

* Two Bode plots are presented side-by-side, illustrating the magnitude and phase response of the transfer function.
* The left plot shows the magnitude response, |A(s)|dB, with:
  + A blue line representing the low-frequency response (0 dB)
  + A red line representing the high-frequency response (-20 dB/decade roll-off)
  + The transition occurring at ω0
* The right plot shows the phase response, ∠A(s), with:
  + A blue line representing the low-frequency phase response (0°)
  + A purple line representing the phase transition
  + A red line representing the high-frequency phase response (-90°)

**Graph Details**

* Both plots have a logarithmic frequency axis (ω) and are labeled with key frequencies: ω0/10, ω0, and 10ω0.
* The magnitude plot has a vertical axis labeled "|A(s)|dB" with a range of -20 to 20 dB.
* The phase plot has a vertical axis labeled "∠A(s)" with a range of -90° to 0°.

**Additional Elements**

* The slide number "63" is displayed at the bottom center.
* A logo is visible in the bottom-right corner, featuring a shield with a red and gold design.

### Slide 64

The image presents a comprehensive analysis of a mathematical function, specifically a Bode plot, which is a graphical representation used to display the frequency response of a system. The slide is titled "Example: Plot" and features two graphs that illustrate the magnitude and phase responses of the given transfer function.

**Transfer Function:**
The transfer function is defined as:

A(s) = (s + 100) / ((s + 1)(s + 10k))

This can be rewritten in a different form:

A(s) = (100/10000) * ((s/100 + 1) / ((s + 1)(s/10k + 1)))

**Graphs:**

*   **Magnitude Response (|A(s)|dB):**
    *   The left graph displays the magnitude response of the system in decibels (dB) versus frequency (ω).
    *   The graph includes multiple lines representing different components of the system's response, including the total response (straight-line approximation and precise).
    *   The x-axis represents frequency (ω), and the y-axis represents the magnitude in dB.
*   **Phase Response (∠A(s)):**
    *   The right graph displays the phase response of the system in degrees versus frequency (ω).
    *   Similar to the magnitude response graph, it includes multiple lines representing different components of the system's phase response.
    *   The x-axis represents frequency (ω), and the y-axis represents the phase angle in degrees.

**Key Features:**

*   The graphs illustrate the frequency response of the system, with the magnitude response showing the gain or attenuation of the system at different frequencies, and the phase response showing the phase shift introduced by the system.
*   The total response is represented by both a straight-line approximation and a precise curve, allowing for a comparison between the two.
*   The graphs provide a detailed understanding of the system's behavior across different frequencies, which is essential in control systems analysis and design.

**Legend:**

*   Total response (straight-line approx.): Green solid line
*   Total response (precise): Green dotted line

**Additional Information:**

*   The slide includes a logo in the bottom-right corner, indicating the institution or organization associated with the presentation.
*   The page number "64" is displayed at the bottom center of the slide.

### Slide 65

The image is a slide from a presentation, likely the final slide, as it expresses gratitude to the audience. The slide features a simple yet distinctive design.

*   **Title and Header**
    *   The title of the slide is "Thanks!" in bold black text, positioned at the top left.
    *   A horizontal bar spans the top of the slide, transitioning from black on the left to purple on the right, with a subtle gradient effect.
*   **Main Content**
    *   A simple line drawing of a hand giving a thumbs-up gesture is centered on the slide.
    *   The hand is depicted in black outline, with the thumb pointing upwards and the other fingers curled around it.
    *   An arrow emerges from the tip of the thumb, pointing upwards and to the right, symbolizing approval or appreciation.
*   **Footer and Logo**
    *   At the bottom center of the slide, the number "65" is displayed in small black text, likely indicating the slide number.
    *   In the bottom-right corner, a small logo is visible, featuring a shield with a red and yellow design, accompanied by a black chevron. This logo may represent the organization or institution presenting the content.

In summary, the image is a concluding slide from a presentation, expressing thanks to the audience through a combination of text and a simple yet effective illustration.

