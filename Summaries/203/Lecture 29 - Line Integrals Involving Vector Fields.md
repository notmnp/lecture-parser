# Lecture 29 - Line Integrals Involving Vector Fields

## Study Notes

# Line Integrals & Work in Vector Fields

---

## Core Formulas & Definitions

| Symbol / Formula | What it means | When/why to use |
|---|---|---|
| $\displaystyle \mathbf F(x,y,z)=P\,\mathbf i+Q\,\mathbf j+R\,\mathbf k$ | Vector field in $\mathbb R^3$ | Any line‑integral problem |
| $\displaystyle \mathbf r(t)=x(t)\,\mathbf i+y(t)\,\mathbf j+z(t)\,\mathbf k,\;a\le t\le b$ | Parametric curve $C$ | Convert a line integral to a single‑variable integral |
| $d\mathbf r=\mathbf r'(t)\,dt=\hat{\mathbf t}\,ds$ | Differential displacement; $\hat{\mathbf t}$ is unit tangent, $ds$ arc length | Most common form of a line integral |
| $\displaystyle W=\int_C\mathbf F\!\cdot d\mathbf r
   =\int_a^b \mathbf F(\mathbf r(t))\!\cdot\mathbf r'(t)\,dt$ | Work (or flow) integral | Work done by $\mathbf F$ on a particle along $C$ |
| $\displaystyle \oint_C \mathbf F\!\cdot d\mathbf r$ | Circulation integral | Closed curves; measures net rotation |
| $\displaystyle \int_{-C}\mathbf F\!\cdot d\mathbf r=-\int_C \mathbf F\!\cdot d\mathbf r$ | Orientation rule | Reversing traversal flips the sign |
| $\displaystyle \mathbf F\!\cdot d\mathbf r=P\,dx+Q\,dy+R\,dz$ | Differential form | Useful when $dx,dy,dz$ are given explicitly |
| $\displaystyle \nabla\times\mathbf F
   =\begin{pmatrix}
      \partial R/\partial y-\partial Q/\partial z\\
      \partial P/\partial z-\partial R/\partial x\\
      \partial Q/\partial x-\partial P/\partial y
    \end{pmatrix}$ | Curl of $\mathbf F$ | Test for conservativeness |
| **Conservative test** |
| $\displaystyle \nabla\times\mathbf F=0\;\Longrightarrow\;
   \mathbf F=\nabla\phi,\;
   \int_C \mathbf F\!\cdot d\mathbf r=\phi(\mathbf r(b))-\phi(\mathbf r(a))$ | Fundamental theorem for line integrals | Skip integration if field is conservative and domain is simply connected |

**Symbols**

| Symbol | Meaning |
|---|---|
| $P,Q,R$ | Component functions of $\mathbf F$ |
| $x(t),y(t),z(t)$ | Parametric coordinates |
| $a,b$ | Parameter limits |
| $\mathbf r'(t)=\frac{d\mathbf r}{dt}$ | Velocity vector of the curve |
| $dx,dy,dz$ | Differentials along $C$ |
| $\hat{\mathbf t}$ | Unit tangent to $C$ |
| $\phi$ | Potential function if $\mathbf F$ is conservative |

---

## Key Concepts & Intuition

* **Tangential component** – The quantity integrated is the projection of $\mathbf F$ onto the direction of motion: $\mathbf F\!\cdot\hat{\mathbf t}\,ds$.
* **Work vs Flow vs Circulation** –  
  * *Work* (force field, open path).  
  * *Flow* (velocity field, open path).  
  * *Circulation* (velocity field, closed path).  
  All are represented by $\int\mathbf F\!\cdot d\mathbf r$; the distinction lies in the physical interpretation and path type.
* **Orientation matters** – Counter‑clockwise orientation is taken as positive for planar curves; reversing the path changes sign.
* **Conservative fields** – If $\nabla\times\mathbf F=0$ on a simply connected domain, the integral depends only on endpoints; evaluate a potential $\phi$ instead of integrating.
* **Parametrization is the workhorse** – Turn the curve into a single‑variable function of $t$; then use $d\mathbf r=\mathbf r'(t)dt$.

---

## Problem‑Solving Strategies

### 1. Work or Flow along a Parametrized Curve

1. **Extract** $\mathbf F=(P,Q,R)$.  
2. **Parametrize** $C$: $\mathbf r(t)=(x(t),y(t),z(t)),\;a\le t\le b$.  
3. **Compute** $\mathbf r'(t)$.  
4. **Form the integrand**:  
   $$\mathbf F(\mathbf r(t))\!\cdot\mathbf r'(t)
   =P\,x'(t)+Q\,y'(t)+R\,z'(t).$$  
5. **Integrate** over $[a,b]$.  
6. **Check orientation**; multiply by $-1$ if the curve was traversed opposite to the given orientation.  

### 2. Circulation Integral (Closed Path)

1. Verify the path is closed. If not, close it explicitly or use a known closed path.  
2. Follow the work‑along‑curve steps, but use $\oint$ and ensure counter‑clockwise orientation (positive).  
3. If $\nabla\times\mathbf F=0$ and the domain is simply connected, shortcut to the potential difference.

### 3. Conservative Field Shortcut

1. **Test** $\nabla\times\mathbf F=0$.  
2. **Find** a potential $\phi$ by integrating component functions (e.g., $P=\partial\phi/\partial x$, etc.).  
3. Evaluate $\phi$ at the endpoints: $W=\phi(\text{end})-\phi(\text{start})$.

### 4. Using Green’s / Stokes’ Theorem (2‑D & 3‑D)

| Context | Formula | When useful |
|---|---|---|
| 2‑D planar curve $C$ | $\displaystyle \oint_C P\,dx+Q\,dy
   =\iint_D \!\!\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA$ | Closed curve; integrand is easier to evaluate over the region $D$. |
| 3‑D surface $S$ with boundary $C$ | $\displaystyle \oint_C \mathbf F\!\cdot d\mathbf r
   =\iint_S (\nabla\times\mathbf F)\!\cdot\mathbf n\,dS$ | When $\nabla\times\mathbf F$ is simpler than $\mathbf F$ itself. |

### 5. Recognizing Cues

| Cue | Typical Pattern | Action |
|---|---|---|
| “arc/segment/quarter‑circle” | Parametrization via trigonometric functions | $t$ runs from starting angle to ending angle |
| “force field” | 3‑D or 2‑D vector field | Compute work integral |
| “velocity field” | 3‑D or 2‑D vector field | Compute flow or circulation |
| “closed curve” | Need circulation | Use $\oint$ and ensure positive orientation |
| “conservative field” | Mentioned or curl test suggested | Find potential |
| “Green’s / Stokes’ theorem” | Problem hints at region or surface | Switch to area or surface integral |

---

## Common Pitfalls & Checks

| Pitfall | What to check |
|---|---|
| Sign error from orientation | Verify traversal direction; reverse if necessary |
| Mixing $ds$ and $d\mathbf r$ | Use $d\mathbf r$ for dot product with $\mathbf F$; $ds$ only in arc‑length integrals |
| Wrong parameter limits | Confirm $t$ corresponds to start and end of the actual path |
| Unsimplified integrand | Combine terms before integrating; avoid algebraic slip-ups |
| Assuming field is conservative without checking | Compute $\nabla\times\mathbf F$ and confirm domain is simply connected |
| Using $\oint$ on an open curve | Only use $\oint$ for closed loops |
| Unit mismatch | Force (N) × distance (m) → work (J) |
| Neglecting negative work | Verify geometry: a negative result means the field opposes motion, not a mistake |
| Forgetting to integrate all components | Ensure $P\,dx+Q\,dy+R\,dz$ covers the entire vector field |

---

### Quick Example (Recap)

**Problem** – Work by $\mathbf F(x,y)=x^2\,\mathbf i-xy\,\mathbf j$ along the quarter circle $C:\;\mathbf r(t)=\cos t\,\mathbf i+\sin t\,\mathbf j,\;0\le t\le\pi/2$.

1. $\mathbf r'(t)=(-\sin t\,\mathbf i+\cos t\,\mathbf j)$  
2. $\mathbf F(\mathbf r(t))=(\cos^2 t)\mathbf i-(\cos t\sin t)\mathbf j$  
3. Integrand: $(\cos^2 t)(-\sin t)+(-\cos t\sin t)(\cos t)= -2\sin t\,\cos^2 t$  
4. $W=\displaystyle\int_0^{\pi/2}(-2\sin t\,\cos^2 t)\,dt
   =-\frac{2}{3}\,.$  

Result: $W=-\frac23$ J (negative because the force opposes motion).  

---  

With these formulas, concepts, and step‑by‑step strategies, you’re ready to tackle any line‑integral problem on the exam.

---

## Raw Slide Summaries

### Slide 1

The image is a presentation slide titled "Line Integrals Involving Vector Fields" in large black text at the top. The slide appears to be from the University of Waterloo, as indicated by the logo in the bottom-left corner.

*   **Title and University Information**
    *   Title: "Line Integrals Involving Vector Fields"
    *   University: University of Waterloo
*   **Trimester and Section Information**
    *   Trimester: Trim Ch 14, S.14.3
*   **Image of Robotic Arm**
    *   A robotic arm is shown on the right side of the slide.
    *   The arm is gray with a yellow object being held by its end effector.
    *   The arm is positioned above a collection of colored blocks.
*   **URL**
    *   A URL is provided at the bottom of the slide: https://engineering.eckovation.com/pick-place-robotic-arm/
*   **Background**
    *   The background of the slide is white, with a black and yellow border at the top.

The slide effectively conveys the topic of the presentation, which is line integrals involving vector fields, and provides a visual representation of a robotic arm interacting with objects, likely related to the topic.

### Slide 2

The image depicts a slide from a presentation on line integrals involving vector fields, specifically focusing on the concept of work in physics.

*   **Title**: "Line Integrals Involving Vector Fields"
    *   The title is prominently displayed at the top of the slide.
*   **Subtitle**: "One of the most fundamental ideas in the world of physics is the idea of WORK."
    *   The subtitle provides context for the topic being discussed.
*   **Equation**: "Work = Force x Distance"
    *   This equation is a fundamental concept in physics, illustrating the relationship between work, force, and distance.
*   **Diagram**:
    *   A diagram is used to visualize the concept of work, featuring a block being pulled by a force vector.
    *   The force vector is represented by an arrow pointing upwards and to the right, with its magnitude labeled as 20N.
    *   The displacement vector is represented by an arrow pointing to the right, with its magnitude labeled as 5m.
    *   The angle between the force and displacement vectors is labeled as θ.
*   **Mathematical Derivation**:
    *   The derivation begins with the equation W = |F||d|cosθ, where W represents work, |F| is the magnitude of the force, |d| is the magnitude of the displacement, and θ is the angle between them.
    *   The equation is then simplified to W = F·d, where F·d represents the dot product of the force and displacement vectors.
    *   The dot product is equivalent to the component of the force vector in the direction of displacement times the distance.
*   **Key Points**:
    *   Work is the component of a force vector in the direction of displacement times distance.
    *   The dot product of two vectors is used to calculate work.
*   **University Logo**:
    *   The logo of the University of Waterloo is displayed in the bottom-right corner of the slide.

In summary, the slide effectively conveys the concept of work in physics, using a combination of text, equations, and diagrams to illustrate the relationship between force, distance, and work. The mathematical derivation provides a clear understanding of how work is calculated, and the key points summarize the main takeaways.

### Slide 3

The image presents a slide from a presentation on line integrals involving vector fields, featuring a diagram and accompanying text.

*   **Title**: "Line Integrals Involving Vector Fields"
    *   The title is prominently displayed at the top of the slide in bold black font.
*   **Text**: A paragraph explaining the concept of line integrals involving vector fields.
    *   The text describes a force field $\vec{F} = P\hat{i} + Q\hat{j}$ on $\mathbb{R}^2$, where $P$ and $Q$ are likely functions of $x$ and $y$. It also introduces a particle moving along a path $C: \vec{r}(t) = x(t)\hat{i} + y(t)\hat{j}$, with $a \leq t \leq b$.
*   **Diagram**: A graph illustrating the concept described in the text.
    *   The graph features a red curve labeled "C" representing the path of the particle, starting at point "t=a" and ending at point "t=b". The curve is plotted on a coordinate system with x and y axes.
    *   Blue arrows are scattered throughout the graph, indicating the direction of the force field $\vec{F}$ at various points.
*   **Question**: A question posed below the diagram.
    *   The question asks, "What is the work done on the particle by the field $\vec{F}$?"
*   **Logo**: A logo for the University of Waterloo.
    *   The logo is displayed in the bottom-right corner of the slide, featuring a shield with a red and yellow design, accompanied by the university's name in black text.

In summary, the slide provides an introduction to line integrals involving vector fields, using a diagram to visualize the concept and posing a question about calculating the work done on a particle by a force field. The slide appears to be part of a larger presentation or educational resource, likely used in a mathematics or physics course at the University of Waterloo.

### Slide 4

The image presents a slide from a presentation on line integrals involving vector fields, featuring a title and a diagram with accompanying text.

**Title:**
The title, "Line Integrals Involving Vector Fields," is prominently displayed in large black font at the top of the slide. Below it, a subtitle reads, "Zooming in and using the same definition or work we learned before," in smaller black font.

**Diagram:**
A diagram is centered on the slide, illustrating a curve labeled "C" in green, which begins at point "P1" and ends at point "P2." The curve is accompanied by several annotations:

*   A blue arrow labeled "F" points upward from the curve.
*   A red arrow labeled "dr" is tangent to the curve, indicating the direction of the curve.
*   A black line segment labeled "ds" represents an infinitesimal displacement along the curve.
*   The x- and y-axes are depicted in blue, with the x-axis labeled "x" and the y-axis labeled "y."

**Text:**
Below the diagram, handwritten text in blue explains the concept:

1.  "Using the same definition we know from before,"
2.  "dw = F.dr"
3.  "The total work, W = ∫dw = ∫F.dr"

**Logo and Footer:**
In the bottom-right corner, the University of Waterloo logo is displayed, featuring a yellow shield with a red and black design. The university's name is written in black font next to the logo.

Overall, the slide effectively conveys complex mathematical concepts through a clear and concise visual representation, making it an effective teaching tool for students of mathematics and physics.

### Slide 5

The image presents a lecture slide on "Line Integrals Involving Vector Fields" from the University of Waterloo. The title is prominently displayed in large black text at the top, followed by a detailed explanation of the concept.

*   **Title and Introduction**
    *   The title "Line Integrals Involving Vector Fields" is written in large black text.
    *   A brief introduction explains that to calculate work between $t = a$ and $t = b$, we need to relate the direction of motion ($d\vec{r}$) to the directed distance "s".
*   **Recalling from Section 11.1**
    *   The equation $\hat{T} = \frac{d\vec{r}}{ds} \rightarrow d\vec{r} = \hat{T}ds$ is recalled from Section 11.1.
*   **Differential of Work**
    *   The differential of work $dw$ is defined as $\vec{F} \cdot \hat{T}ds$, where $\vec{F}$ is the force component in the direction of motion.
    *   A cloud-shaped diagram illustrates the concept, with $W = \int_{C} \vec{F} \cdot \hat{T}ds$ written inside it.
*   **Line Integral Involving Vector Fields**
    *   The line integral involving vector fields is represented by the equation $W = \int_{C} \vec{F} \cdot \hat{T}ds$.
    *   The diagram labels this as a "LINE INTEGRAL INVOLVING VECTOR FIELDS".
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner, featuring a shield with a red and yellow design.

In summary, the image provides a clear and concise explanation of line integrals involving vector fields, including the definition of the differential of work and the line integral, accompanied by a visual representation and the University of Waterloo logo.

### Slide 6

The image presents a slide from a presentation on the topic of "The Work Integral" in mathematics, specifically focusing on its definition and application. The slide is structured to provide a clear understanding of the concept, starting with an introduction and followed by a detailed explanation.

*   **Title**: "We can now define The Work Integral"
    *   The title is prominently displayed at the top of the slide.
    *   It is written in large font size, with "The Work Integral" highlighted in blue.
*   **Assumptions and Definitions**
    *   The slide assumes that $\vec{F} = P\hat{i} + Q\hat{j} + R\hat{k}$ represents a force field on $\mathbb{R}^3$.
    *   It defines a curve $C: \vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}, a \leq t \leq b$ as smooth.
*   **Work Done by a Force Field**
    *   The work done by $\vec{F}$ in moving a particle along the smooth curve $C$, from $t = a$ to $t = b$, is given by the line integral.
    *   The formula for work is provided as $\text{Work} = \int_{C} \vec{F} \cdot \hat{T}ds$.
*   **Definition of Work Integral**
    *   The integral is referred to as a "work integral."
    *   It is described as a line integral involving a vector field $\vec{F}$.
*   **University Logo**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner.
    *   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.

In summary, the slide effectively introduces and explains the concept of the work integral, providing a clear definition and formula for calculating the work done by a force field along a smooth curve.

### Slide 7

The image presents a slide from a lecture on "Flow and Circulation Line Integrals" at the University of Waterloo. The content is organized into sections, each addressing a specific aspect of line integrals in the context of fluid flow.

*   **Title and Introduction**
    *   The title "Flow and Circulation Line Integrals" is prominently displayed.
    *   The slide introduces the concept that if $\vec{F}$ represents a velocity field of a fluid flowing along a curve C, then the line integral is called a "flow integral."
*   **Flow Integral Formula**
    *   The formula for the flow integral is given as $\int_{a}^{b} \vec{F} \cdot \hat{T} ds$.
    *   This formula calculates the flow of a fluid along a curve defined by the velocity field $\vec{F}$.
*   **Circulation Integral for Closed Curves**
    *   For a closed curve C, the line integral is termed a "circulation integral," denoted as $\oint_{C} \vec{F} \cdot \hat{T} ds$.
    *   The circulation integral measures the tendency of the fluid to circulate in the positive direction around C.
*   **Notation for Closed Path Integrals**
    *   The symbol $\oint$ is used to denote a line integral over a closed path.
    *   This notation is specific to integrals around closed curves, distinguishing them from integrals over open paths.
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner.
    *   The logo indicates the academic institution associated with the lecture.

In summary, the slide explains the concepts of flow and circulation line integrals, providing formulas and notations relevant to understanding fluid dynamics. It distinguishes between flow integrals for general curves and circulation integrals for closed curves, highlighting their significance in analyzing fluid behavior.

### Slide 8

The image presents a slide from a lecture on the topic of "Orientation of Line Integrals Involving Vector Fields" at the University of Waterloo.

**Title and Introduction**

* The title, "Orientation of Line Integrals Involving Vector Fields," is prominently displayed in large black text at the top of the slide.
* A brief introduction explains that when dealing with line integrals involving vector fields, replacing the unit tangent vector $\hat{T}$ with $-\hat{T}$ is equivalent to replacing the curve $C$ with $-C$.

**Diagrams and Equations**

* Two 3D diagrams are shown, each illustrating a curve $C$ in a three-dimensional space with $x$, $y$, and $z$ axes.
	+ The left diagram depicts a curve $C$ with a unit tangent vector $\hat{T}$ and a vector field $\vec{F}$.
	+ The right diagram shows the same curve but with the unit tangent vector $-\hat{T}$.
* The equation for the line integral is given as $\int_{C} \vec{F} \cdot \hat{T} ds = \int_{C} \vec{F} \cdot d\vec{r}$.
* The text explains that for $+\hat{T}$, the signs of $dx$, $dy$, and $dz$ are in the same direction as $d\vec{r}$, and the orientation does not change.
* For $-\hat{T}$, the signs of $dx$, $dy$, and $dz$ are reversed, leading to the equation $\int_{-C} \vec{F} \cdot (-\hat{T}) ds = -\int_{C} \vec{F} \cdot d\vec{r}$.
* The equation $\int_{-C} \vec{F} \cdot d\vec{r} = -\int_{C} \vec{F} \cdot d\vec{r}$ is derived, highlighting the effect of reversing the orientation of the curve on the line integral.

**University Logo**

* The University of Waterloo logo is displayed in the bottom-right corner of the slide.

### Slide 9

The image presents a slide from a presentation on evaluating integrals involving vector fields, specifically focusing on Method 1. The title, "Evaluating Integrals Involving Vector Fields - Method 1," is prominently displayed at the top.

**Problem Statement:**
The problem is to find the work done by the force field, $\vec{F}(x,y) = x^2\hat{i} - xy\hat{j}$, in moving a particle along the quarter circle defined by $\vec{r}(t) = \cos t \hat{i} + \sin t \hat{j}; 0 \leq t \leq \pi/2$.

**Method 1:**
This method involves expressing the work integral as follows:

$W = \int_{C} \vec{F} \cdot d\vec{r} = \int_{a}^{b} \left(\vec{F}(\vec{r}(t))\right) \cdot \frac{d\vec{r}}{dt} dt$

**Key Elements:**

*   The force field $\vec{F}(x,y) = x^2\hat{i} - xy\hat{j}$ is given.
*   The quarter circle path is defined by $\vec{r}(t) = \cos t \hat{i} + \sin t \hat{j}; 0 \leq t \leq \pi/2$.
*   The work integral is expressed using Method 1.

**Visuals and Layout:**
The slide features a clean white background with black text, accompanied by a yellow bar at the top. The University of Waterloo logo is displayed in the bottom-right corner. The content is organized into clear sections, with headings and equations presented in a readable format. The use of blue handwriting-style text for some equations adds a touch of informality, suggesting that this may be a lecture slide or a screenshot from an educational resource.

### Slide 10

The lecture slide is titled "Evaluating Integrals Involving Vector Fields - Method 1" and contains the following information:

**Title and Steps**

* The title is in large black text at the top of the slide.
* The slide is divided into two main steps, labeled "Step 1" and "Step 2".

**Step 1: Evaluating $\vec{F}$ on Curve $C$**

* The text states: "To solve this integral, we first evaluate $\vec{F}$ on the curve $C$ as a function of the parameter 't'".
* A handwritten equation is given: $\vec{r}(t) = \begin{cases} x(t) = \cos t \\ y(t) = \sin t \end{cases}$
* Another handwritten equation is provided: $\vec{F}(\vec{r}(t)) = (\cos t)^2 \hat{i} - (\cos t)(\sin t) \hat{j}$, with annotations:
	+ Under $(\cos t)^2$, it is labeled as $x^2$.
	+ Under $(\cos t)$, it is labeled as $x$.
	+ Under $(\sin t)$, it is labeled as $y$.

**Step 2: Calculating $\frac{d\vec{r}}{dt}$**

* The text states: "We then calculate $\frac{d\vec{r}}{dt}$".
* A handwritten equation is given: $\frac{d\vec{r}}{dt} = -\sin t \hat{i} + \cos t \hat{j}$

**Additional Information**

* The University of Waterloo logo is displayed in the bottom-right corner of the slide.

Overall, the slide provides a step-by-step guide to evaluating integrals involving vector fields using Method 1.

### Slide 11

The image is a slide from a presentation on evaluating integrals involving vector fields, specifically titled "Evaluating Integrals Involving Vector Fields - Method 1." The slide presents a step-by-step solution to a problem, with the third step being the focus. The title is displayed prominently at the top in large black text.

*   **Title and Step Description**
    *   Title: Evaluating Integrals Involving Vector Fields - Method 1
    *   Step 3: Finally, we put together the line integral and integrate
*   **Mathematical Equations**
    *   $I = \int_{0}^{\pi/2} [\cos t^2 \hat{i} - \cos t \sin t \hat{j}] \cdot [-\sin t \hat{i} + \cos t \hat{j}] dt$
    *   $= \int_{0}^{\pi/2} (-2\sin t \cos^2 t) dt$
    *   $W = 2\frac{\cos^3 t}{3} \Big|_{0}^{\pi/2} = -\frac{2}{3}$
*   **University Logo**
    *   University of Waterloo logo in the bottom-right corner

The slide provides a clear and concise solution to the problem, with each step building upon the previous one. The use of mathematical notation and symbols is consistent throughout, making it easy to follow along. The inclusion of the University of Waterloo logo in the bottom-right corner adds a touch of professionalism to the presentation. Overall, the slide effectively communicates the steps involved in evaluating integrals involving vector fields using Method 1.

### Slide 12

The image presents a slide from a presentation on evaluating integrals involving vector fields, specifically focusing on Method 1. The title "Evaluating Integrals Involving Vector Fields - Method 1" is prominently displayed at the top.

**Key Elements:**

* **Title:** "Evaluating Integrals Involving Vector Fields - Method 1"
* **Graph:** A graph showing the vector field F and the curve C
* **Vector Field F:** Represented by blue arrows
* **Curve C:** A pink curve
* **Work Done:** Calculated as W = -2/3
* **Explanation:** The work done is negative because the field impedes movement along the curve
* **University Logo:** University of Waterloo logo in the bottom-right corner

**Detailed Description:**

* The graph illustrates the vector field F and the curve C, providing a visual representation of the problem.
* The vector field F is depicted by blue arrows, while the curve C is represented by a pink curve.
* The work done is calculated as W = -2/3, indicating that the field impedes movement along the curve.
* The explanation provided highlights the significance of the negative work done, emphasizing that it is a result of the field's opposition to movement along the curve.

**Visual Representation:**

* The graph is positioned on the left side of the slide, with the vector field F and curve C clearly visible.
* The University of Waterloo logo is displayed in the bottom-right corner, indicating the institution associated with the presentation.

**Overall:**

The slide effectively conveys the concept of evaluating integrals involving vector fields using Method 1, providing a clear and concise visual representation of the problem and its solution.

### Slide 13

The image presents a slide titled "Evaluating Integrals Involving Vector Fields - Method 2" from the University of Waterloo. The slide is divided into sections, each addressing a specific aspect of the topic.

**Title and Problem Statement**

*   The title is prominently displayed at the top in bold black font.
*   Below the title, the word "Problem:" is followed by a statement that reads: "Find the work done by the force field," accompanied by the equation $\vec{F}(x,y) = x^2\hat{i} - xy\hat{j}$.

**Problem Details**

*   The problem involves moving a particle along a quarter circle defined by $C: \vec{r}(t) = \cos t \hat{i} + \sin t \hat{j}; 0 \leq t \leq \pi/2$.
*   This section provides the necessary information to understand the context of the problem.

**Method 2**

*   The heading "Method 2:" is followed by a statement referencing "Method 1," indicating that this slide builds upon previous knowledge or methods discussed earlier.
*   The text explains that given $\vec{F} = P\hat{i} + Q\hat{j} + R\hat{k}$ and the curve $C: \vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}, a \leq t \leq b$, the work done can be calculated using the formula $W = \int_{a}^{b} \vec{F} \cdot \left(\frac{d\vec{r}}{dt}\right) dt$.

**University Logo**

*   In the bottom-right corner, the University of Waterloo logo is displayed, featuring a shield with a red and black checkered pattern, accompanied by the university's name in black text.

This detailed description captures all the content presented on the slide, including equations, formulas, definitions, and written text, without omitting or simplifying any information.

### Slide 14

The image presents a slide from a lecture on vector calculus, specifically focusing on the evaluation of integrals involving vector fields using Method 2. The title, "Evaluating Integrals Involving Vector Fields - Method 2," is prominently displayed at the top.

Here is a detailed breakdown of the content on the slide:

*   **Title and Introduction**
    *   The title is in large black text.
    *   The subtitle "For Method 2, we perform the dot product as" is written below the title.
*   **Mathematical Derivation**
    *   The first equation is: $W = \int_{a}^{b} \vec{F} \cdot \left(\frac{d\vec{r}}{dt}\right) dt = \int_{a}^{b} (P,Q,R) \cdot \left(\frac{dx}{dt}, \frac{dy}{dt}, \frac{dz}{dt}\right) dt$
    *   The second equation is: $W = \int_{a}^{b} \left(P\frac{dx}{dt} + Q\frac{dy}{dt} + R\frac{dz}{dt}\right) dt$
    *   The third equation simplifies to: $W = \int_{a}^{b} Pdx + Qdy + Rdz$
*   **Example**
    *   The example involves a 2-D vector field: $\vec{F}(x,y) = x^2\hat{i} - xy\hat{j}$
    *   The curve C is defined by: $\vec{r}(t) = \cos t \hat{i} + \sin t \hat{j}$
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner.

In summary, the slide provides a step-by-step derivation of the formula for evaluating integrals involving vector fields using Method 2, followed by an example illustrating its application to a 2-D vector field and curve C.

### Slide 15

The image presents a slide from a lecture on evaluating integrals involving vector fields, specifically focusing on Method 2. The title, "Evaluating Integrals Involving Vector Fields - Method 2," is prominently displayed in bold black text at the top of the slide.

**Step 1: Write P and Q in terms of the parametric equations of C and calculate dx and dy**

*   The step is written in black text below the title.
*   Four equations are presented in blue handwriting-style text:
    *   x = cos(t) → dx = -sin(t)dt
    *   y = sin(t) → dy = cos(t)dt
    *   P = x^2 → P = cos^2(t)
    *   Q = -xy → Q = -cos(t)sin(t)

**Additional Elements**

*   A yellow bar is visible at the top of the slide, accompanied by a thick black bar above it.
*   The University of Waterloo logo is situated in the bottom-right corner, featuring a shield with a red and yellow design, alongside the university's name in black text.

This slide provides a clear and concise overview of the first step in evaluating integrals involving vector fields using Method 2, along with the necessary mathematical derivations.

### Slide 16

The image is a slide from a lecture on evaluating integrals involving vector fields, specifically focusing on Method 2. The slide is titled "Evaluating Integrals Involving Vector Fields - Method 2" and features a white background with black text and blue handwritten equations.

**Title and Subtitle**

*   Title: Evaluating Integrals Involving Vector Fields - Method 2
*   Subtitle: Step 2: Put together the line integral and integrate

**Equations and Formulas**

*   The first equation is:

    W = ∫[0, π/2] (cos^2(t))(-sin(t)dt) + (-cos(t)sin(t))(cos(t)dt)

    This equation represents the line integral of a vector field along a curve, where P and Q are components of the vector field, and dx and dy are infinitesimal changes in x and y, respectively.
*   The second equation is:

    = ∫[0, π/2] -2sin(t)cos^2(t)dt

    This equation simplifies the previous expression by combining the terms and integrating with respect to t.
*   The third equation is:

    W = -2/3

    This is the result of evaluating the integral, which is equal to -2/3.
*   Additional text: "→ SAME AS BEFORE"

    This indicates that the result obtained using Method 2 is the same as the result obtained previously, likely using Method 1.

**Logo and Institution**

*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

**Overall Content**

The slide presents a step-by-step solution to evaluating a line integral involving a vector field using Method 2. The equations and formulas are handwritten in blue, while the title and subtitle are in black text. The result of the integration is -2/3, which matches the result obtained previously.

### Slide 17

The slide is titled "Summary" and contains four bullet points that summarize key concepts related to line integrals involving vector fields. The main points are:

*   A line integral involving a vector field $\vec{F}$ is the line integral of the scalar tangential component of $\vec{F}$ along C.
*   If the vector field $\vec{F}$ is force, it is called a work integral.
*   If the vector field $\vec{F}$ is velocity, it is called a flow (for open paths) and a circulation (for closed paths) integral
*   We have presented two methods to evaluate a line integral involving vector fields

The slide also features the University of Waterloo logo in the bottom-right corner, indicating that it is likely from a lecture or presentation at the university. The background of the slide is white, with a yellow and black border at the top.

There are no diagrams or images on the slide, only text. The title and bullet points are presented in a clear and concise manner, making it easy to read and understand the summary.

