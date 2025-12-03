# Lecture 30 - Fundamental Theorem and Conservative Fields

## Study Notes

# Exam Notes – Line Integrals & Conservative Vector Fields  

---

## Core Formulas & Definitions  

| Symbol | Formula | Meaning | Use‑Case |
|--------|---------|---------|----------|
| $C$ | $\displaystyle \int_C \mathbf F\!\cdot d\mathbf r$ | Line integral of a vector field | Work, circulation, or any integral along a curve |
| $\mathbf r(t)$ | $\mathbf r(a\le t\le b)$ | Parametrization of $C$ | Convert $\int_C$ to an ordinary integral: $\displaystyle \int_a^b \mathbf F(\mathbf r(t))\!\cdot\!\mathbf r'(t)\,dt$ |
| $\nabla f$ | $\displaystyle \begin{pmatrix} f_x\\ f_y\\ f_z \end{pmatrix}$ | Gradient of a scalar potential | Characterizes a conservative field |
| $\mathbf F$ | $\displaystyle \nabla f$ | Conservative field definition | Tests whether $\mathbf F$ is gradient of some $f$ |
| $\displaystyle \oint_C \mathbf F\!\cdot d\mathbf r$ | $0$ | Closed‑curve integral in a conservative field | Path independence |
| Curl (3‑D) | $\displaystyle \nabla\times\mathbf F = \begin{pmatrix} R_y-Q_z\\ P_z-R_x\\ Q_x-P_y\end{pmatrix}$ | Measure of local rotation | Necessary for conservativeness |
| 2‑D component test | $\displaystyle \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$ | Simplified curl test | Sufficient in a simply connected region with continuous partials |
| Potential construction | $f(x,y)=\int P(x,y)\,dx+g(y)$ → $f_y=Q$ → solve $g(y)$ | Stepwise method | Find $f$ when $\mathbf F=(P,Q)$ is conservative |
| Fundamental Theorem of Line Integrals | $\displaystyle \int_C \nabla f\!\cdot d\mathbf r = f(\mathbf r(b)) - f(\mathbf r(a))$ | Work equals change in potential | Compute work without path details |

---

## Key Concepts & Intuition  

* **Conservativeness** ⇔ existence of a scalar potential $f$ with $\mathbf F=\nabla f$.  
* **Path Independence** – integral depends only on start and end points.  
* **Closed‑Path Property** – any closed loop in a conservative field yields zero work.  
* **Domain Matters** – curl $=0$ is only sufficient for conservativeness on an open, simply connected domain.  
* **Component Test** – in $\mathbb R^2$ a single partial‑derivative equality suffices.  

---

## Problem‑Solving Strategies  

### 1. Verify that a field is conservative  

| Step | Action | Why |
|------|--------|-----|
| 1 | **Check the domain** – open, connected, simply connected? | Guarantees sufficiency of curl/partial‑derivative tests. |
| 2 | **Apply the appropriate test** | 2‑D: $\partial P/\partial y = \partial Q/\partial x$. <br>3‑D: $\nabla\times\mathbf F = \mathbf 0$. |
| 3 | **Construct a potential** (if test passes) | Integrate one component, solve for the “constant” of integration using the other component. |
| 4 | **Verify** – compute $\nabla f$ and compare to $\mathbf F$ | Confirms no algebraic slip. |

**Checklist**: Domain → Test → Potential → Verify.

---

### 2. Compute work between two points (conservative field)  

1. **Find a potential** $f$ (Step 1).  
2. **Evaluate** $f$ at the endpoints: $W = f(\mathbf b)-f(\mathbf a)$.  
3. **Result** – constant of integration cancels automatically.

---

### 3. Compute work along a specified curve (conservative or not)  

1. **If conservative** → use Step 2.  
2. **If not**  
   1. Parametrize $C$: $\mathbf r(t),\, t_0\le t\le t_1$.  
   2. Substitute: $\displaystyle \int_{t_0}^{t_1} \mathbf F(\mathbf r(t))\!\cdot\!\mathbf r'(t)\,dt$.  
   3. Integrate (exact or approximate).  

*Tip*: Always keep the $dt$ after replacing $d\mathbf r$ with $\mathbf r'(t)\,dt$.

---

### 4. Evaluate a closed‑loop integral  

1. **Check conservativeness** (Steps 1‑3).  
2. **If conservative** → answer is $0$.  
3. **If not** → parametrize the loop and apply Step 3.  

*Important*: A non‑simply connected domain (e.g., a punctured plane) can give non‑zero closed integrals even if $\nabla\times\mathbf F=\mathbf 0$.

---

### 5. Test path independence  

1. Choose two different paths between the same endpoints.  
2. Compute integrals via potential (if conservative) or directly.  
3. If results match → field is conservative; otherwise, it is not.

---

## Common Pitfalls & Checks  

| Pitfall | Quick Check |
|---------|-------------|
| Assume $\nabla\times\mathbf F=0$ ⇒ conservative | Verify domain is simply connected |
| Ignore domain continuity | Ensure $\mathbf F$ is defined and continuous on the whole path |
| Skip potential consistency | Differentiate $f$ w.r.t. all variables and compare to $\mathbf F$ |
| Forget orientation | Reversing the path changes the sign of the integral |
| Omit $dt$ after substitution | Remember $d\mathbf r=\mathbf r'(t)\,dt$ |
| Assume closed integral is zero | Only if field is conservative on the domain |

---

## Quick Worked Example  

**Field:** $\displaystyle \mathbf F(x,y)=(3+2xy)\,\mathbf i + (x^2-3y^2)\,\mathbf j$  
**Goal:** Work from $(0,1)$ to $(0,-e^{\pi})$.

1. **Domain:** $\mathbb R^2$ – simply connected.  
2. **Component test:** $\partial P/\partial y = 2x$, $\partial Q/\partial x = 2x$ → conservative.  
3. **Potential**  
   * Integrate $P$: $f= \int(3+2xy)\,dx = 3x + x^2y + g(y)$.  
   * Differentiate w.r.t. $y$: $f_y = x^2 + g'(y) = Q = x^2 - 3y^2$ → $g'(y)=-3y^2$.  
   * Integrate $g$: $g(y) = -y^3 + C$.  
   * $f(x,y)=3x+x^2y-y^3 + C$.  
4. **Work**  
   * $f(0,-e^{\pi}) = -(-e^{\pi})^3 + C = e^{3\pi}+C$.  
   * $f(0,1) = -1 + C$.  
   * $W = (e^{3\pi}+C)-(-1+C)= e^{3\pi}+1$.

Result: $W = e^{3\pi}+1$.

---

### Bottom Line

* **Domain first** – always check before applying tests.  
* **Use potentials** whenever possible to avoid messy parametrizations.  
* **Close the loop** only if the field is confirmed conservative.  
* **Keep a checklist** of domain, test, potential, verification to catch mistakes early.  

These concise, formula‑centric notes give you a quick reference for tackling any exam problem on line integrals and conservative vector fields.

---

## Raw Slide Summaries

### Slide 1

The image is a slide from a presentation on the topic of "Fundamental Theorem and Conservative Fields." The title is prominently displayed at the top, followed by a yellow box with the text "Trim Ch 14,S.14.4-14.5" in black font.

*   **Title and Reference**
    *   Title: Fundamental Theorem and Conservative Fields
    *   Reference: Trim Ch 14,S.14.4-14.5
*   **Outline**
    *   1. Fundamental Theorem of Line Integrals (Independence of Path)
    *   2. Conservative Fields
*   **Image**
    *   A graphic illustrating the gravitational field of Earth and Moon
    *   The image features a black background with purple arrows representing the gravitational field lines
    *   The Earth and Moon are depicted as orange and blue spheres, respectively, surrounded by concentric red circles
*   **University Logo and URL**
    *   University of Waterloo logo in the bottom-left corner
    *   URL: https://commons.wikimedia.org/wiki/File:Earth-moon-field.svg in the bottom-right corner

The slide provides an overview of the topics to be covered, including the fundamental theorem of line integrals and conservative fields, accompanied by a visual representation of the gravitational field between Earth and Moon.

### Slide 2

The image presents a lecture slide on the Fundamental Theorem of Line Integrals, featuring a clear and organized layout. The title, "Fundamental Theorem of Line Integrals," is prominently displayed in large black text at the top of the slide.

**Key Components:**

* **Title:** "Fundamental Theorem of Line Integrals" in large black text
* **Text Sections:**
	+ Introduction to the theorem
	+ Statement of the theorem
	+ Explanation of the theorem's application
* **Mathematical Equations:**
	+ Definition of a smooth curve C
	+ Parametrization of C by r(t)
	+ Statement of the fundamental theorem of line integrals
	+ Recall of the fundamental theorem of calculus
* **Visual Elements:**
	+ Red handwritten notes in a cloud-shaped bubble
	+ University of Waterloo logo in the bottom-right corner
* **Color Scheme:**
	+ White background
	+ Black text
	+ Yellow border at the top
	+ Red handwritten notes

**Summary:**

The slide provides a comprehensive overview of the Fundamental Theorem of Line Integrals, including its statement, application, and relation to the fundamental theorem of calculus. The use of clear headings, concise bullet points, and visual elements enhances the slide's readability and understanding.

### Slide 3

The image presents a slide from a lecture on the topic of "Path Independence" in mathematics, specifically focusing on the implications of the fundamental theorem of line integrals.

**Title and Introduction**

* The title "Path Independence" is prominently displayed at the top of the slide.
* A brief introduction follows, stating, "Let us look at the implication of the fundamental theorem of line integrals."

**Graphical Representation**

* A graph is shown with two axes labeled "x" and "y".
* The graph features two curves, C1 and C2, which are drawn in black and red, respectively.
* Both curves originate from the point (a, t=a) and terminate at the point (b, t=b).
* The curves are not straight lines but rather smooth, continuous paths.

**Mathematical Equations**

* Three equations are presented to the right of the graph:
	+ W1 = ∫[C1] ∇f · dr = f(r(b)) - f(r(a))
	+ W2 = ∫[C2] ∇f · dr = f(r(b)) - f(r(a))
	+ W = ∫[C1] ∇f · dr = ∫[C2] ∇f · dr
* These equations demonstrate that the line integral of a conservative vector field (∇f) along different paths (C1 and C2) between the same endpoints yields the same result.

**University Logo**

* In the bottom-right corner of the slide, the logo of the University of Waterloo is displayed.

This slide effectively illustrates the concept of path independence in the context of line integrals, highlighting the significance of the fundamental theorem of line integrals.

### Slide 4

The image presents a slide from a presentation on conservative fields, featuring a white background with a black and yellow bar at the top. The title "Conservative Fields" is prominently displayed in large black text.

*   **Title and Definition**
    *   The title "Conservative Fields" is written in large black text.
    *   A vector field $\vec{F}$ is defined as a "conservative field" if it is the gradient of some scalar function $f$, denoted as $\vec{F} = \vec{\nabla}f$.
    *   The scalar function $f$ is referred to as a "potential field."
*   **Mathematical Equation**
    *   The equation $\int_{C} \vec{F} \cdot d\vec{r} = \int_{C} \vec{\nabla}f \cdot d\vec{r}$ is presented, illustrating the relationship between the line integral of a conservative field and its potential function.
*   **Fundamental Theorem of Line Integrals**
    *   The fundamental theorem of line integrals states that work integrals of conservative fields are independent of path.
    *   This means that the work done by a conservative force on an object is path-independent.
*   **Physical Meaning**
    *   The physical meaning of conservative fields is explained, highlighting that the work done by a conservative force on a particle is independent of the path taken.
*   **University Logo**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner, indicating the institution associated with the presentation.

In summary, the slide provides a concise overview of conservative fields, including their definition, mathematical representation, and physical significance, along with the university's logo.

### Slide 5

The image presents a slide from a lecture on "Closed Paths in Conservative Fields" at the University of Waterloo. The title is prominently displayed in large black text at the top, followed by a subtitle that reads, "Let us look at a closed curve C on D:" in smaller black text.

**Key Elements:**

* **Diagrams:** Two diagrams are presented, each featuring a green oval shape with arrows indicating direction. The left diagram includes labels for the x and y axes, while the right diagram is labeled with points A, B, C1, and C2.
* **Equations:** Three equations are displayed below the diagrams:
	+ $\oint_{C} \vec{F} \cdot d\vec{r} = \int_{C_{1}} \vec{F} \cdot d\vec{r} + \int_{C_{2}} \vec{F} \cdot d\vec{r}$
	+ $\vec{r}(a) = \vec{r}(b)$
* **Labels and Annotations:** Various labels and annotations are scattered throughout the diagrams, including "TERMINAL POINTS COINCIDE" and "D".
* **University Logo:** The University of Waterloo logo is displayed in the bottom-right corner, featuring a yellow shield with a red crest and the university's name in black text.

**Overall:** The slide appears to be discussing the properties of conservative fields and closed paths, using diagrams and equations to illustrate key concepts.

### Slide 6

The image presents a slide from a presentation on "Closed Paths in Conservative Fields" and features the University of Waterloo's logo in the bottom-right corner. The content is organized as follows:

* **Title**: "Closed Paths in Conservative Fields" in large black text at the top.
* **Main Content**:
	+ A statement about the line integral of a vector field F being independent of path and having the same terminals.
	+ An equation illustrating this concept, with the integral of F·dr over a closed curve C equal to zero.
	+ A condition for F to be conservative, implying that there is no need to solve the integral.
* **Physical Meaning**:
	+ A statement explaining that the work done by a conservative field F as a particle moves on a closed path is zero.
* **Visuals**:
	+ A yellow bar at the top of the slide, spanning its width.
	+ The University of Waterloo's logo in the bottom-right corner, featuring a shield with a red and gold design, accompanied by the university's name in black and gold text.
* **Background**: White background.

In summary, the image is a slide from a presentation discussing the properties of conservative fields, specifically the behavior of closed paths within them.

### Slide 7

The image presents a slide from a presentation on "Open and Simply Connected Regions" in mathematics, featuring diagrams and explanations. The title is prominently displayed at the top, followed by a brief introduction that sets the stage for the definitions and illustrations to come.

*   **Title and Introduction**
    *   Title: "Open and Simply Connected Regions"
    *   Introduction: "Before we continue, let us define open and simply connected regions (or a set of points)."
*   **Definitions and Diagrams**
    *   **Open Region**
        *   Definition: "Every point in D is the center of an open ball that lies entirely in D."
        *   Diagram: A graph with a blue dot inside a dashed circle, illustrating the concept of an open region.
    *   **Open and Connected Region**
        *   Definition: "Any two points can be joined by a smooth curve that lies in D."
        *   Diagram: A graph showing two points connected by a blue line within a dashed shape, demonstrating the property of being open and connected.
    *   **Open and Simply Connected Region**
        *   Definition: "Every loop inside D can be contracted all the way to a point in D without leaving the domain."
        *   Diagram: A graph featuring a dashed circle with a loop inside, illustrating the concept of an open and simply connected region.
*   **Visual Illustrations**
    *   Three graphs are presented, each with a different configuration of shapes and lines, accompanied by annotations and arrows to highlight key features.
    *   The graphs are used to visualize the definitions and properties of open, connected, and simply connected regions.
*   **University Logo**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner, indicating the institution associated with the presentation.

In summary, the image provides a clear and concise explanation of open and simply connected regions, supported by visual aids and definitions. The use of diagrams and graphs helps to illustrate the concepts, making the material more accessible and understandable for the audience.

### Slide 8

The image presents a slide from a presentation on "Open and Simply Connected Regions" in the context of mathematics, specifically focusing on vector calculus or complex analysis. The title is prominently displayed at the top.

*   **Title**: 
    *   "Open and Simply Connected Regions"
*   **Three Diagrams**:
    *   The first diagram illustrates a 3D coordinate system with x, y, and z axes.
        *   A red dashed line extends from the origin to infinity, labeled as "INFINITE LINE."
        *   The region is marked as "NOT OPEN AND SIMPLY CONNECTED."
    *   The second diagram shows another 3D coordinate system with x, y, and z axes.
        *   A red dashed line represents a "LINE SEGMENT."
        *   The region is labeled as "OPEN SIMPLY CONNECTED."
    *   The third diagram depicts a torus (doughnut-shaped surface) in a 3D coordinate system with x, y, and z axes.
        *   The torus is labeled as "TORUS."
*   **University Logo**:
    *   The logo of the University of Waterloo is displayed in the bottom-right corner.
*   **Background**:
    *   The background of the slide is white, providing a clean and neutral backdrop for the diagrams and text.

In summary, the slide effectively illustrates the concepts of open and simply connected regions through visual representations, making it easier for students to understand these abstract mathematical ideas.

### Slide 9

The image displays a slide from a presentation on the "Component Test for Conservative Fields" from the University of Waterloo. 

**Title**: 
The title, "Component Test for Conservative Fields," is prominently displayed in bold black text at the top of the slide.

**Content**:
Below the title, the slide outlines a mathematical concept related to vector fields and their properties. It begins by defining a vector field $\vec{F}$ as $P(x,y,z)\hat{i} + Q(x,y,z)\hat{j} + R(x,y,z)\hat{k}$.

**Key Points**:
* The scalar components of $\vec{F}$ have continuous partial derivatives on an open simply connected region $D$.
* Three conditions are given for $\vec{F}$ to be a conservative field on $D$:
	+ $\frac{\partial R}{\partial y} = \frac{\partial Q}{\partial z}$
	+ $\frac{\partial P}{\partial z} = \frac{\partial R}{\partial x}$
	+ $\frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$

**Conclusion**:
If these conditions are met, then $\vec{F}$ is a conservative field on $D$, meaning there exists a scalar function $f$ (also called a potential function) such that $\vec{\nabla}f = \vec{F}$.

**University Logo**:
In the bottom-right corner, the University of Waterloo's logo is visible, featuring a shield with a red and yellow design, accompanied by the university's name in black text.

This slide appears to be part of a larger educational resource or lecture on vector calculus, likely used in a mathematics or physics course.

### Slide 10

The slide is titled "So far..." and contains three main bullet points that summarize key concepts related to conservative fields.

*   The first bullet point states: "We learned that 'conservative fields' are the gradient of a 'potential function'".
*   The second bullet point reads: "We now know now why the work performed by a conservative field is"
    *   Followed by two sub-bullet points:
        *   "Independent of path"
        *   "Zero when the path is closed"
*   The third bullet point says: "If we can prove that a field $\overrightarrow{F}$ is conservative, then there is no need to solve the line integral!"
    *   Followed by the statement: "We can use the Fundamental Theorem of Line Integrals"

The slide features a white background with a yellow stripe at the top and a black stripe above it. The University of Waterloo logo is displayed in the bottom-right corner.

There are no diagrams or images on this slide; it is entirely text-based.

### Slide 11

The image presents a slide from a lecture on conservative fields and their potential functions, specifically focusing on a problem related to a given force field. The title "Conservative Fields and their Potential Functions" is prominently displayed at the top.

**Key Elements:**

* **Title:** "Conservative Fields and their Potential Functions"
* **Problem Statement:**
	+ A force field is given by the equation: $\vec{F}(x,y) = (3 + 2xy)\hat{i} + (x^2 - 3y^2)\hat{j}$
	+ Three parts to the problem:
		- Determine whether or not $\vec{F}(x,y)$ is conservative
		- If so, find a potential function for the vector field $\vec{F}(x,y)$
		- Evaluate the work integral $\int_{C} \vec{F} \cdot d\vec{r}$ when C is the curve given by: $\vec{r}(t) = (e^{t} \sin t)\hat{i} + (e^{t} \cos t)\hat{j}, \quad 0 \leq t \leq \pi$
* **University Logo:** The University of Waterloo logo is displayed in the bottom-right corner.

**Summary:**
The slide presents a problem involving a force field and asks the viewer to determine if it is conservative, find a potential function if it is, and evaluate a work integral along a specific curve.

### Slide 12

The image presents a slide from a lecture on Conservative Fields and their Potential Functions, featuring a white background with black text and blue handwritten notes.

*   **Title**
    *   The title "Conservative Fields and their Potential Functions" is displayed in large black font at the top of the slide.
*   **Text**
    *   Below the title, a paragraph explains that to use the component test for conservative fields, we need to first examine the domain of the force field.
    *   A mathematical equation is provided: $\vec{F}(x,y) = (3+2xy)\hat{i} + (x^2-3y^2)\hat{j}$.
    *   The domain of $\vec{F}$ is defined as $D = \mathbb{R}^2$, which is open and simply connected.
*   **Handwritten Notes**
    *   Blue handwritten notes are scattered throughout the slide, including:
        *   "Using component test:" followed by equations: $\frac{\partial P}{\partial y} = 2x$, $\frac{\partial Q}{\partial x} = 2x$, and $\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$.
        *   The conclusion that the field is conservative.
*   **Logo**
    *   In the bottom-right corner, the logo of the University of Waterloo is displayed, featuring a shield with a red and yellow design, accompanied by the university's name in black text.

The slide provides a clear and concise explanation of conservative fields and their potential functions, along with relevant mathematical equations and conclusions.

### Slide 13

The image presents a slide from a lecture on Conservative Fields and their Potential Functions, specifically focusing on finding a potential function for a given force field. The slide is divided into sections, each addressing a different aspect of the topic.

*   **Title and Subtitle**
    *   The title, "Conservative Fields and their Potential Functions," is prominently displayed at the top of the slide.
    *   Below the title, the subtitle "b. Finding a potential function for our force field" provides context for the content that follows.
*   **Mathematical Equations and Derivations**
    *   The equation for the force field, $\vec{F}(x,y) = (3 + 2xy)\hat{i} + (x^2 - 3y^2)\hat{j}$, is presented, along with the condition that $\vec{F} = \nabla f$.
    *   The gradient of $f$, denoted as $\nabla f$, is expressed as $f_x(x,y)\hat{i} + f_y(x,y)\hat{j}$, and equated to $\vec{F}$.
    *   The partial derivatives $f_x(x,y)$ and $f_y(x,y)$ are derived from the components of $\vec{F}$, yielding $f_x(x,y) = 3 + 2xy$ and $f_y(x,y) = x^2 - 3y^2$.
    *   The process of integrating $f_x(x,y)$ with respect to $x$ is demonstrated, resulting in $f(x,y) = \int(3+2xy)dx$.
*   **Key Points and Visuals**
    *   A cloud-shaped diagram illustrates the relationship between $\vec{F}$ and $\nabla f$, highlighting their equivalence.
    *   Yellow circles draw attention to the equations $f_x(x,y) = 3+2xy$ and $f_y(x,y) = x^2-3y^2$, emphasizing their importance.
    *   An arrow pointing to the right indicates the direction of integration with respect to $x$, while keeping $y$ constant.
*   **University Logo and Color Scheme**
    *   The University of Waterloo logo is displayed in the bottom-right corner of the slide, featuring a shield with a crest and the university's name written in black text.
    *   The color scheme of the slide includes a white background, black text, red and blue handwritten notes, and a yellow stripe at the top.

In summary, the slide provides a step-by-step explanation of how to find a potential function for a given force field, using mathematical derivations and visual aids to support the explanation.

### Slide 14

The image is a whiteboard slide titled "Conservative Fields and their Potential Functions" in large black text at the top. The title is followed by a series of mathematical equations and diagrams, written in various colors, including black, blue, red, green, and yellow.

**Equations and Diagrams:**

*   The first equation is f(x,y) = 3x + x^2y + g(y), with "(3)" written next to it and "CONSTANT OF INTEGRATION" below the underlined term "g(y)".
*   Below this, the text "Differantiating(3) with respect to 'y' and comparing with (2)" is written, followed by the equation fy = x^2 + g'(y) = -3y^2, with "x^2" highlighted in yellow.
*   The next section shows the steps to integrate g'(y) = -3y^2 with respect to "y", resulting in g(y) = -y^3 + K.
*   The final equation is f(x,y) = 3x + x^2y - y^3 + K, labeled as "(4)".
*   A diagram to the right of the equations illustrates the concept of equipotential curves, with arrows pointing upwards and a green curve labeled "E = -∇f".
*   The diagram also includes labels for "POTENTIAL FUNCTION" and "EQUIPOTENTIAL CURVES".

**University Logo:**

*   In the bottom-right corner, the University of Waterloo logo is displayed, featuring a shield with a red and yellow design.

**Background:**

*   The background of the slide is white, with a yellow stripe at the top and a black border above it.

The slide appears to be part of a lecture or presentation on conservative fields and potential functions, likely in a mathematics or physics course.

### Slide 15

The image is a slide from a presentation on "Conservative Fields and their Potential Functions." The content is as follows:

**Title and Main Text**
* The title is "Conservative Fields and their Potential Functions" in large black text.
* The main text is: 
  * "c. Evaluating the work integral $\int_C \vec{F} \cdot d\vec{r}$ when C is the curve given by,"
  * $\vec{r}(t) = (e^t \sin t)\hat{i} + (e^t \cos t)\hat{j}, \quad 0 \leq t \leq \pi$
  * "To use the fundamental theorem of line integrals we need to determine the values of $\vec{r}(t)$ at the curve's terminal points:"

**Handwritten Notes**
* The handwritten notes are in blue ink and include:
  * "END POINTS OF C"
  * $\begin{cases} \vec{r}(0) = (0,1) \\ \vec{r}(\pi) = (0,-e^\pi) \end{cases}$
  * $W = \int_C \vec{F} \cdot d\vec{r} = \int_0^\pi \vec{\nabla}f \cdot d\vec{r} = f(0,e^\pi) - f(0,1)$
  * "EVALUATED IN (4)"
  * $W = e^{3\pi} + 1$

**Logo and Footer**
* In the bottom-right corner, there is a logo for the University of Waterloo.

The slide appears to be discussing the evaluation of a work integral using the fundamental theorem of line integrals, specifically for a conservative field. The handwritten notes provide additional steps and calculations to solve the problem.

### Slide 16

The image presents a slide from a lecture on Conservative vs. Non-Conservative Fields, featuring two graphs and mathematical equations.

*   The title "Conservative vs. Non-Conservative Fields" is prominently displayed at the top of the slide.
    *   The title is in large black text.
*   Two graphs are shown side-by-side, each with a yellow shaded area and blue arrows.
    *   The left graph has a red curve labeled "C1" and "C2" within the shaded area.
        *   The x-axis ranges from -2 to 2, and the y-axis ranges from -2 to 2.
        *   The equation below the graph is $\vec{F}(x,y) = (3 + 2xy)\hat{i} + (x^2 - 3y^2)\hat{j}$.
    *   The right graph has a red oval curve labeled "C" within the shaded area.
        *   The x-axis ranges from -10 to 10, and the y-axis ranges from -10 to 10.
        *   The equation below the graph is $\vec{F}(x,y) = (x-y)\hat{i} + (x-2)\hat{j}$.
*   Mathematical equations are written below the graphs.
    *   The equation for the left graph is $\vec{F}(x,y) = (3 + 2xy)\hat{i} + (x^2 - 3y^2)\hat{j}$.
    *   The equation for the right graph is $\vec{F}(x,y) = (x-y)\hat{i} + (x-2)\hat{j}$.
    *   Additional equations are written in blue ink: $\frac{\partial P}{\partial y} = -1$, $\frac{\partial Q}{\partial x} = 1$, and "NON-CONSERVATIVE".
*   The University of Waterloo logo is displayed in the bottom-right corner.
    *   The logo features a crest with a shield and the university's name written in blue text.

In summary, the slide compares conservative and non-conservative fields using graphical representations and mathematical equations. The left graph illustrates a conservative field, while the right graph shows a non-conservative field. The equations provided help to understand the properties of these fields.

### Slide 17

The image is a slide from a presentation, likely the final slide, expressing gratitude to the audience. 

*   The top of the slide features a black and yellow gradient bar.
*   On the left side, there is a logo for the University of Waterloo, which includes:
    *   A shield with a yellow background and red lions on it.
    *   A black and white chevron design overlaid on the shield.
    *   The words "UNIVERSITY OF WATERLOO" in bold black text to the right of the shield.
*   Below the logo, in large black text, it says "Thank you".

This slide appears to be a concluding slide, thanking the audience for their attention, and is likely from an academic or professional presentation related to the University of Waterloo.

