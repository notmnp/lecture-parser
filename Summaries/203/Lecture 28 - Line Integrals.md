# Lecture 28 - Line Integrals

## Study Notes

# Line‑Integral Study Guide (Scalar, Arc‑Length Form)

## Core Formulas & Definitions

| Symbol | Meaning | Typical Use |
|--------|---------|-------------|
| **$C$** | Curve of integration | Any smooth or piecewise smooth path |
| **$\mathbf{r}(t)$** | Parametrization of $C$ | $a\le t\le b$ |
| **$a,b$** | Parameter limits | Trace $C$ once |
| **$f(x,y,z)$** | Scalar field | Height, density, temperature, etc. |
| **$\mathbf{r}'(t)$** | Velocity vector | $\dfrac{d\mathbf{r}}{dt}$ |
| **$\|\mathbf{r}'(t)\|$** | Speed | $\sqrt{(x')^2+(y')^2+(z')^2}$ |
| **$ds$** | Arc‑length differential | $\|\mathbf{r}'(t)\|\,dt$ |
| **$\displaystyle\int_C f\,ds$** | Line integral of $f$ | Sum of “height × length” along $C$ |
| **$\displaystyle\int_{C_i} f\,ds$** | Integral over a segment | Piecewise curves |
| **$s(t)$** | Arc‑length function (optional) | $s(t)=\int_{t_0}^t \|\mathbf{r}'(\tau)\|\,d\tau$ |

### Important Formulas

1. **Arc‑length element**  
   $$
   ds = \|\mathbf{r}'(t)\|\,dt
   = \sqrt{\left(\frac{dx}{dt}\right)^2
           +\left(\frac{dy}{dt}\right)^2
           +\left(\frac{dz}{dt}\right)^2}\;dt
   $$

2. **Line integral in parameter form**  
   $$
   \int_{C} f\,ds
   =\int_{a}^{b} f\bigl(x(t),y(t),z(t)\bigr)\;
                 \|\mathbf{r}'(t)\|\,dt
   $$

3. **Speed of a circle of radius 1**  
   If $\mathbf{r}(t)=\langle\cos t,\sin t\rangle$, then  
   $$
   \|\mathbf{r}'(t)\|=\sqrt{(-\sin t)^2+(\cos t)^2}=1
   $$

4. **Substitution for $\int \cos t\,\sin t\,dt$**  
   Let $u=\sin t$, $du=\cos t\,dt$.  
   $$
   \int \cos t\,\sin t\,dt = \int u\,du = \frac{u^2}{2} = \frac{\sin^2 t}{2}
   $$

---

## Key Concepts & Intuition

- **$ds$ is the infinitesimal arc length** – the length of the tiny displacement $\mathbf{r}'(t)dt$.  
- **Scalar line integrals are *orientation‑independent***: reversing $C$ changes $t$ limits but not the value.  
- **Geometric meaning**: $\int_C f\,ds$ is the area of a wall of height $f$ erected over $C$.  
- **Piecewise curves**: integrate each smooth segment and sum; no sign change is needed for scalars.  
- **Constant $f$**: reduces to $f$ times the length of $C$.  
- **$f$ depending only on one coordinate** often simplifies after substitution.  

---

## Problem‑Solving Strategies

1. **Identify the curve $C$**  
   * Parametric? Explicit? Implicit?  
   * Write a convenient parametrization $\mathbf{r}(t)$.

2. **Check the parametrization**  
   * Verify $a\le t\le b$ covers $C$ exactly once.  
   * For piecewise curves, split into $\mathbf{r}_i(t)$ with appropriate bounds.

3. **Compute the speed**  
   * Differentiate: $\mathbf{r}'(t)$.  
   * Find magnitude: $\|\mathbf{r}'(t)\|$ (always $\ge0$).

4. **Form the integrand**  
   * Substitute $(x(t),y(t),z(t))$ into $f$.  
   * Multiply by $\|\mathbf{r}'(t)\|$.

5. **Set up the integral**  
   $$
   \int_{a}^{b} f\bigl(x(t),y(t),z(t)\bigr)\;\|\mathbf{r}'(t)\|\,dt
   $$

6. **Integrate**  
   * **Direct** if simple.  
   * **Substitution** when a composition appears.  
   * **Definite** integrals: use FTC; evaluate limits.  

7. **Special patterns**  
   * **$f$ constant**: $f \times \text{(arc length)}$.  
   * **$f$ linear**: $ax+by+cz$ → often cancels after substitution.  
   * **$f$ quadratic or product**: may lead to trigonometric integrals; use identities or substitutions.  

8. **Quick Example** – *Quarter circle, $f(x,y)=xy$*  
   * $\mathbf{r}(t)=\langle\cos t,\sin t\rangle$, $t\in[0,\pi/2]$.  
   * $\|\mathbf{r}'(t)\|=1$.  
   * Integral: $\int_{0}^{\pi/2}\cos t\,\sin t\,dt = \frac{\sin^2 t}{2}\Big|_0^{\pi/2}= \frac12$.

---

### Quick Checklist for Typical Problem Types

| Problem Type | Cue | Key Steps |
|--------------|-----|-----------|
| Parametric curve | “$\mathbf{r}(t)$” | Use formula (2) directly |
| Implicit curve | “$x^2+y^2=1$” | Convert to $x=\cos t$, $y=\sin t$ or $x=t$, $y=g(t)$ |
| Piecewise curve | “$C=C_1\cup C_2$” | Separate integrals, then add |
| Arc‑length only | “$\int_C 1\,ds$” | Integrate $\|\mathbf{r}'(t)\|$ |
| Constant $f$ | “$f=k$” | $k$ × length |
| Linear $f$ | “$f=ax+by$” | Simplify after substitution |
| Product $xy$ | “$f=xy$” | Expect trigonometric integrals; use substitution $u=\sin t$ |

---

## Common Pitfalls & Checks

| Pitfall | Why it hurts | Quick check |
|---------|--------------|-------------|
| Omit $\|\mathbf{r}'(t)\|$ | Misses the arc‑length element | Multiply by speed after substitution |
| Wrong bounds after re‑parametrization | Incomplete curve, duplicate, or missing part | Verify $t$ limits cover $C$ once |
| Drop absolute value / square root | Speed becomes negative or complex | Use $\sqrt{(\cdot)^2}$; check sign |
| Confuse $ds$ with $dt$ | Integral value wrong | Always include $\|\mathbf{r}'(t)\|\,dt$ |
| Neglect piecewise splitting | Sum of parts missing | Identify each smooth segment |
| Assume $f$ constant when it’s not | Incorrect simplification | Inspect $f$ for $t$‑dependence |
| Missed substitution in trigonometric integrals | Integration fails | Look for product of trig functions, try $u=\sin t$ or $\cos t$ |
| Forget orientation independence for scalars | Double counting | Remember scalar integrals are direction‑free |

---

## Quick Reference

- **$ds = \|\mathbf{r}'(t)\|\,dt$** – always non‑negative.  
- **Line integral**: $\displaystyle\int_C f\,ds = \int_a^b f(\mathbf{r}(t))\,\|\mathbf{r}'(t)\|\,dt$.  
- **Arc length of a circle**: $\|\mathbf{r}'(t)\|=1$ for $r(t)=\langle\cos t,\sin t\rangle$.  
- **Substitution**: For $\int \cos t\,\sin t\,dt$, let $u=\sin t$.  

Use this compact structure as your go‑to cheat sheet when tackling scalar line‑integral problems. Happy calculating!

---

## Raw Slide Summaries

### Slide 1

The image presents a slide from the University of Waterloo, titled "Line Integrals" in large black text at the top left. The slide is divided into several sections, each containing various elements.

*   **Title and Subtitle**
    *   The title "Line Integrals" is prominently displayed in large black text.
    *   Below the title, a yellow rectangle contains the text "Trim Ch 14, S.14.2" in black.
*   **Mathematical Equations and Diagrams**
    *   A series of green and blue handwritten equations and diagrams are scattered across the top half of the slide.
    *   The equations appear to be related to line integrals, with symbols such as ∫, f(x,y,z), and dV.
    *   The diagrams depict 3D coordinate systems with x, y, and z axes, as well as curves and surfaces.
*   **Image of the Aurora Borealis**
    *   A photograph of the Aurora Borealis (Northern Lights) is displayed on the right side of the slide.
    *   The image shows a dark sky with green and purple hues, accompanied by a body of water and mountains in the foreground.
    *   The URL "https://i.ytimg.com/vi/T75IKSXVlclc/maxresdefault.jpg" is provided below the image.
*   **University Logo**
    *   The University of Waterloo logo is located at the bottom left of the slide.
    *   The logo features a shield with a red crest and the words "UNIVERSITY OF WATERLOO" in black text.

In summary, the slide appears to be a lecture slide from a mathematics course at the University of Waterloo, covering the topic of line integrals. The slide includes a mix of mathematical equations, diagrams, and an image of the Aurora Borealis, which may be used to illustrate a concept or example.

### Slide 2

The image is a presentation slide titled "Line Integrals" and features a diagram illustrating the concept.

*   The title "Line Integrals" is prominently displayed at the top left of the slide.
    *   The title is written in large, bold black font.
*   A paragraph below the title explains the concept of line integrals.
    *   The text states that $f(x,y,z)$ is a real-valued function to be integrated over a curve defined by $\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$, where $a \leq t \leq b$.
    *   The equation is written in black font, with the variables $f(x,y,z)$ and $\vec{r}(t)$ highlighted in blue.
*   A 3D graph is shown on the slide, illustrating the curve $\vec{r}(t)$.
    *   The graph has three axes labeled $x$, $y$, and $z$, represented by blue arrows.
    *   The curve $\vec{r}(t)$ is depicted in green, with several points marked along its length.
    *   The starting point of the curve is labeled "$t=a$" and the ending point is labeled "$t=b$".
    *   A red vector $\vec{r}(t)$ is drawn from the origin to a point on the curve.
    *   The function $f(x,y,z)$ is represented by a green label near the top of the graph.
*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.
    *   The logo features a shield with a yellow and red design, accompanied by the university's name in black text.

The slide effectively conveys the concept of line integrals and provides a visual representation of the mathematical concept.

### Slide 3

The image presents a slide from a presentation on line integrals, featuring a title and several key points. The main points are as follows:

*   **Title**: 
    *   "Line Integrals" in bold black font
*   **Text**:
    *   A paragraph explaining the concept of line integrals, including the formula for evaluating a function f at a point (x_k, y_k, z_k) and forming the sum S_n = ∑[f(x_k, y_k, z_k) * Δs_k] from k=1 to n.
    *   A handwritten note in green explaining that as Δs_k approaches 0, S_n becomes the line integral of f over C, denoted as ∫[f(x,y,z)ds] from C, where a ≤ t ≤ b.
*   **Definition**:
    *   A statement defining line integrals as a powerful tool in mathematics and physics, particularly useful when dealing with quantities that vary along a path.
*   **Logo**:
    *   The University of Waterloo logo is displayed in the bottom-right corner.

In summary, the slide provides an introduction to line integrals, explaining their definition and significance in mathematics and physics.

### Slide 4

The image presents a visual representation of line integrals in the plane, specifically focusing on the concept of visual interpretation. The title "Line Integrals in the Plane - Visual Interpretation" is prominently displayed at the top.

**Key Components:**

* **Title:** "Line Integrals in the Plane - Visual Interpretation"
* **Graph:**
	+ 3D graph with x, y, and z axes
	+ Curved surface with a vertical wall constructed along a curve C
	+ The surface is colored in shades of blue, green, and yellow
	+ Arrows indicate the direction of the x, y, and z axes
* **Text:**
	+ Description of the graph: "If at each point (x,y) of C, we draw a vertical line of height z = f(x,y), a vertical wall is constructed."
	+ Mathematical equation: "Sn = ∫C f(x,y)ds"
	+ Explanation: "Adding them all up we obtain, Sn = ∫C f(x,y)ds"
	+ Visual interpretation: "We can visually interpret the line integral of a positive function f(x,y) ≥ 0 over a curve C, as the area of the 'fence' or 'curtain' drawn in the picture"
* **University Logo:**
	+ University of Waterloo logo in the bottom-right corner

**Summary:**

The image effectively illustrates the concept of line integrals in the plane, providing a clear visual representation of the mathematical concept. The graph and accompanying text work together to explain the idea of constructing a vertical wall along a curve C and calculating the area under the surface defined by the function f(x,y). The image is a useful tool for students and educators looking to understand and visualize this complex mathematical concept.

### Slide 5

The image presents a slide from a presentation on evaluating line integrals, featuring a white background with black text and yellow accents. The title, "Evaluating Line Integrals," is prominently displayed in large bold font at the top.

**Title and Introduction**

*   Title: Evaluating Line Integrals
*   Subtitle: Recalling from Chapter 11, the arc length parameter is defined as,

**Mathematical Equations**

*   $s(t) = \int_{t_0}^{t} |\vec{v}(\tau)|d\tau$
*   $ds = |\vec{v}(t)|dt$

**Line Integral Definition**

*   The line integral $S_n$ can be written as,
    *   $S_n = \int_{C} f(x,y,z)ds = \int_{C} f(x,y,z)|\vec{v}(t)|dt$
    *   $f(x(t), y(t), z(t))$ (handwritten in green)

**Text and Logo**

*   To evaluate the line integral of a scalar function $f(x,y,z)$ we will then need the parametric equations of the curve $C$.
*   University of Waterloo logo (bottom-right corner)

The slide effectively conveys complex mathematical concepts related to line integrals, providing a clear and concise overview of the topic.

### Slide 6

The image presents a slide from a presentation on evaluating line integrals, featuring a clear and structured approach to the topic. The slide is divided into two main sections: "Step 1" and "Step 2," which outline the necessary steps for evaluating line integrals.

*   **Title and Header**
    *   The title of the slide is "Evaluating Line Integrals."
    *   The header is black with a yellow stripe underneath it.
*   **Step 1: Parametrization of Curve C**
    *   Find a smooth parametrization of the curve C.
    *   The parametrization is given by the vector function r(t) = x(t)i + y(t)j + z(t)k, where a ≤ t ≤ b.
*   **Step 2: Evaluating the Integral**
    *   Evaluate the integral Sn as, Sn = ∫[a,b] f(x(t), y(t), z(t)) |r'(t)| dt.
    *   The expression |r'(t)| is defined as √((dx/dt)^2 + (dy/dt)^2 + (dz/dt)^2).
*   **University Logo**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner of the slide.

In summary, the slide provides a concise and step-by-step guide to evaluating line integrals, including the parametrization of the curve C and the evaluation of the integral using the given formula.

### Slide 7

The image is a slide from a presentation on the topic of "Orientation of Line Integrals of real-valued functions." The title is prominently displayed at the top, followed by two diagrams that illustrate the concept. The diagrams are accompanied by handwritten notes and equations.

*   The first diagram shows a 3D coordinate system with a curve labeled "C" and a scalar field represented by the function f(x,y,z). The diagram is annotated with arrows indicating the direction of the curve and the scalar field.
    *   The equation ∫C f(x,y,z) ds = ∫-C f(x,y,z) ds is written below the diagrams, highlighting the property that the line integral of a real-valued function with respect to arc length remains unchanged when the direction of the curve is reversed.
*   The second diagram is similar to the first, but with the direction of the curve reversed.
    *   A thought bubble next to the second diagram contains the text "'ds' DOES NOT CHANGE SIGN," emphasizing that the arc length element "ds" remains positive regardless of the direction of the curve.
*   Below the diagrams, a statement reads: "For a line integral of a real-valued function with respect to arc length, we can change the direction of the curve without changing the value of the integral."
*   In the bottom-right corner, the logo of the University of Waterloo is displayed.

In summary, the image effectively illustrates the concept of orientation of line integrals of real-valued functions, highlighting the property that the line integral remains unchanged when the direction of the curve is reversed. The diagrams and accompanying notes provide a clear visual representation of this concept, making it easier for students to understand and apply it in their studies.

### Slide 8

The image is a slide from a presentation on the additivity property of line integrals, featuring a white background with black text and green handwriting. The title "Additivity Property of Line Integrals" is prominently displayed at the top.

*   **Title**
    *   The title is in large, bold, black font.
    *   It reads "Additivity Property of Line Integrals".
*   **Definition**
    *   The definition is written in smaller black font below the title.
    *   It states: "Let us define a curve C made by joining a finite number of curves C1, C2, C3, ..., Cn,".
*   **Graph**
    *   A graph is drawn in the center of the slide.
    *   The x-axis and y-axis are labeled with blue arrows.
    *   A green curve is plotted on the graph, comprising multiple segments labeled C1, C2, C3, ..., Cn.
    *   The curve is annotated with green handwriting, including the label "f(x,y)" and an arrow pointing to the curve.
*   **Property Statement**
    *   The statement of the additivity property is written in black font below the graph.
    *   It reads: "Line integrals have the useful property that if the curve C is made by joining a finite number of curves C1, C2, C3, ..., Cn, end to end,".
*   **Mathematical Formula**
    *   A mathematical formula is presented below the property statement.
    *   It states: "∫C fds = ∫C1 fds + ∫C2 fds + ∫C3 fds ... ∫Cn fds".
    *   The formula is written in black font, with the integral signs and variables in a larger size than the rest of the text.
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner of the slide.
    *   The logo features a yellow shield with a red design, accompanied by the university's name in black font.

In summary, the slide provides a clear explanation of the additivity property of line integrals, including a definition, graph, and mathematical formula. The content is presented in a concise and organized manner, making it easy to follow and understand.

### Slide 9

The slide is titled "Example: Solving a Line Integral" in large black text at the top. Below the title, the text reads, "Suppose we have the function f(x,y) = xy." 

*   A 3D graph is shown below this text, with a grid pattern and a rainbow-colored surface that curves downward in the middle.
*   The x-axis ranges from -0.1 to 0.1, and the y-axis also ranges from -0.1 to 0.1. The z-axis ranges from -0.015 to 0.01.
*   Below the graph, the text states, "And the path," followed by the equation: 

    r(t) = cos t î + sin t ĵ, 0 ≤ t ≤ π/2
    x = cos t
    y = sin t

    This is written in black text, except for "x = cos t" and "y = sin t," which are handwritten in black.
*   To the right of the equations, a 2D graph is drawn in blue ink, showing a quarter-circle with the equation x^2 + y^2 = 1. 
    *   The x-axis and y-axis are labeled, and the graph is annotated with "t = π/2" at the top and "t = 0" on the right side.
    *   The quarter-circle is oriented such that it starts at (1,0) and ends at (0,1).
*   In the bottom-right corner, the University of Waterloo logo is displayed, featuring a shield with a red and yellow design. The logo is accompanied by the text "UNIVERSITY OF WATERLOO" in black.

### Slide 10

The image presents a slide from a presentation on solving line integrals, featuring a title and a diagram with accompanying equations.

*   **Title**
    *   The title is "Example: Solving a Line Integral" in bold black text at the top of the slide.
*   **Diagram**
    *   A 3D coordinate system is shown, with x, y, and z axes labeled.
    *   A curved surface is depicted, bounded by a curve C in the xy-plane.
    *   The curve C is parameterized by t, with t = 0 at one end and t = π/2 at the other.
    *   The function f(x,y) = xy is represented on the surface.
*   **Equations**
    *   The line integral A is defined as ∫f(x,y)ds along the curve C.
    *   The integral is rewritten as ∫xy ds, with ds expressed in terms of the parameterization of C.
    *   The parameterization of C is given by r(t) = cos(t)i + sin(t)j, with its derivative r'(t) = -sin(t)i + cos(t)j.
    *   The expression for A is simplified to ∫cost sin(t) dt.
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

In summary, the slide illustrates the process of solving a line integral using a specific example, providing a clear and step-by-step solution.

### Slide 11

The image presents a slide from a presentation, titled "Example: Solving a Line Integral" in bold black text at the top. The slide is divided into two sections: the title and the content.

**Title Section**

*   The title is centered and written in large, bold, black font.
*   A yellow bar separates the title from the rest of the content.

**Content Section**

*   The main content is written in black handwriting-style text on a white background.
*   The first line reads "|v'(t)| = √((-sin(t))^2 + (cos(t))^2) = 1".
*   Below this, the equation "A = ∫[0,π/2] cos(t)sin(t)(1)dt" is displayed.
*   A cloud-shaped annotation contains the text "d(sin(t)) = cos(t)dt".
*   Further down, the equation "A = [sin^2(t)/2] from 0 to π/2 = 1/2" is shown.
*   In the bottom-right corner, the logo for the University of Waterloo is visible, featuring a yellow shield with a red design and the university's name in black text.

In summary, the image displays a slide from a presentation on solving line integrals, providing a step-by-step example and featuring the University of Waterloo's logo.

### Slide 12

The image presents a slide from a presentation on the topic of line integrals, featuring a summary of key points. The title "Summary" is prominently displayed in large black text at the top left corner.

**Key Points:**

*   The line integral of a positive function f(x,y) ≥ 0 over a curve C can be interpreted as the area of a "fence" or "curtain" of height f(x,y) over the curve C.
*   For a line integral of a real-valued function with respect to arc length, the direction of the curve can be changed without affecting the value of the integral.
*   To evaluate a line integral f(x,y,z) over a curve C, we parametrize the curve to obtain the speed while re-writing the integral as a function of one variable.
*   Line integrals over curves forming a piecewise smooth curve can be added.

**Visual Elements:**

*   A yellow bar runs along the top edge of the slide, transitioning to black towards the left side.
*   The University of Waterloo logo is situated in the bottom-right corner, accompanied by the text "UNIVERSITY OF WATERLOO" in black font.

**Background:**

*   The background of the slide is white, providing a clean and neutral backdrop for the content.

Overall, the slide effectively summarizes the main concepts related to line integrals, making it a useful resource for students and educators alike.

