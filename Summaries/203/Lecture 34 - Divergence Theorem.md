# Lecture 34 - Divergence Theorem

## Study Notes

# Divergence & Flux – Exam‑Ready Problem‑Solving Notes

---

## Core Formulas & Definitions

| Concept | Formula | Symbols & Meaning | When to Use |
|---------|---------|-------------------|-------------|
| **Gradient of a scalar field** | $$\nabla f = \left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\right)$$ | $f=f(x,y,z)$ – scalar field.  $\nabla$ – del operator. | Turn a scalar into a vector (direction of steepest ascent). |
| **Divergence of a vector field** | $$\operatorname{div}\mathbf{F} = \nabla\!\cdot\!\mathbf{F}= \frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}$$ | $\mathbf{F}=P\,\mathbf{i}+Q\,\mathbf{j}+R\,\mathbf{k}$. | Measure local “spreading” of a field. Needed for flux calculations. |
| **Divergence in cylindrical coordinates** | $$\operatorname{div}\mathbf{F}= \frac{1}{r}\frac{\partial(rF_r)}{\partial r}+\frac{1}{r}\frac{\partial F_\theta}{\partial \theta}+\frac{\partial F_z}{\partial z}$$ | $F_r,F_\theta,F_z$ – components in $(r,\theta,z)$. | When the geometry is cylindrical; simplifies volume integrals. |
| **Flux through a surface** | $$\Phi=\iint_{S}\mathbf{F}\!\cdot\!\hat{\mathbf{n}}\,dS$$ | $\hat{\mathbf{n}}$ – outward unit normal to $S$. | Direct surface integral; use when $S$ is easy to parametrize. |
| **Flux via parametric surface** | If $S$ is given by $\mathbf{r}(u,v)$, then $\hat{\mathbf{n}}\,dS=\bigl(\mathbf{r}_u\times\mathbf{r}_v\bigr)\,du\,dv$. | $\mathbf{r}_u=\partial\mathbf{r}/\partial u$, etc. | Compute $\mathbf{F}\!\cdot\!(\mathbf{r}_u\times\mathbf{r}_v)$ and integrate over the parameter domain. |
| **Divergence Theorem (3‑D)** | $$\iiint_{V}\operatorname{div}\mathbf{F}\,dV = \iint_{\partial V}\mathbf{F}\!\cdot\!\hat{\mathbf{n}}\,dS$$ | $V$ – solid, $\partial V$ – closed surface bounding $V$. | Replace a hard surface integral by an easier volume integral. |
| **Flux via divergence in 2‑D (Green’s normal‑vector form)** | $$\oint_{C}\mathbf{F}\!\cdot\!\hat{n}\,ds=\iint_{D}\operatorname{div}\mathbf{F}\,dA$$ | $C$ – positively oriented closed curve, $D$ – interior. | Compute 2‑D flux as an area integral. |
| **Green’s Theorem (circulation form)** | $$\oint_{C}P\,dx+Q\,dy=\iint_{D}\!\Bigl(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Bigr)\,dA$$ | $(P,Q)$ – components of $\mathbf{F}$ in the plane. | Convert a line integral of $Pdx+Qdy$ into an area integral. |
| **Incompressible field** | $\operatorname{div}\mathbf{F}=0$ everywhere. | Field has no local net outflow. | If $\operatorname{div}\mathbf{F}=0$ → zero flux through any closed surface. |

---

## Key Concepts & Intuition

- **Outward normal orientation**  
  *A positively oriented curve in the plane (counter‑clockwise) corresponds to an outward normal pointing outward in the surface integral.*

- **Zero flux on a single closed surface**  
  *Does **not** imply $\operatorname{div}\mathbf{F}=0$ everywhere; only that the net outflow across that particular surface is zero. If flux is zero for **every** closed surface, then $\operatorname{div}\mathbf{F}\equiv0$.*

- **Green’s theorem as a 2‑D divergence theorem**  
  *Standard form gives circulation; normal‑vector form gives flux.*

- **Coordinate choice matters**  
  *Symmetry or simple bounds (rectangular, polar, cylindrical, spherical) can reduce the integral drastically.*

---

## Problem‑Solving Strategies

### 1. **Compute the Divergence of a Field**

**Cues**  
- Expression of $\mathbf{F}$ as $P\mathbf{i}+Q\mathbf{j}+R\mathbf{k}$ or in cylindrical coordinates.  
- Question asks “div $\,\mathbf{F}$” or “source strength”.

**Checklist**  
1. Identify components $P,Q,R$ (or $F_r,F_\theta,F_z$).  
2. Take partial derivatives w.r.t. the appropriate variables.  
3. Sum them.  
4. Simplify.

**Common Mistake** – Forgetting a component in 3‑D or mixing up variables in cylindrical form.

---

### 2. **Flux Through a Closed Surface (3‑D)**

**Cues**  
- Surface described (sphere, cylinder, plane segments).  
- Vector field given.  
- “Flux” or “$\iint_S\mathbf{F}\!\cdot\!\hat{n}\,dS$”.

**Checklist**  
1. **Decide**:  
   - Direct surface integral if the surface is simple or only one piece.  
   - Divergence theorem if the enclosed volume is easier.
2. **If using Divergence Theorem**  
   - Compute $\operatorname{div}\mathbf{F}$.  
   - Identify volume $V$ and its limits (Cartesian, spherical, or cylindrical).  
   - Evaluate $\iiint_V \operatorname{div}\mathbf{F}\,dV$.
3. **If direct**  
   - Parameterize each surface patch $\mathbf{r}(u,v)$.  
   - Compute $\mathbf{r}_u\times\mathbf{r}_v$ for the oriented area element.  
   - Integrate $\mathbf{F}\!\cdot\!(\mathbf{r}_u\times\mathbf{r}_v)$ over the patch.
4. **Check** the orientation: outward normal; if inward, negate the result.

**Tip** – For a closed surface built from planes and curved pieces, use the divergence theorem to avoid multiple surface integrals.

---

### 3. **Flux Through a Closed Curve (2‑D)**

**Cues**  
- Plane region with boundary $C$, field $\mathbf{F}=(P,Q)$.  
- Question asks “flux out of $D$” or “$\oint_C\mathbf{F}\!\cdot\!\hat{n}\,ds$”.

**Checklist**  
1. Use Green’s normal‑vector form to switch to an area integral:  
   $$\Phi = \iint_D \operatorname{div}\mathbf{F}\,dA = \iint_D \Bigl(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}\Bigr)\,dA.$$
2. Draw or sketch $D$ to choose convenient coordinates (rectangular → Cartesian; radial symmetry → polar).  
3. Set up limits and evaluate the double integral.  

**Alternative** – If the line integral is simpler, use  
$$\Phi = \oint_C (P\,dy - Q\,dx).$$  

**Common Mistake** – Using the circulation form ($Pdx+Qdy$) instead of the flux form.

---

### 4. **Using Green’s Theorem for Circulation**

**Cues**  
- Asked for $\oint_C P\,dx + Q\,dy$ or “circulation of $\mathbf{F}$”.  

**Checklist**  
1. Compute $\partial Q/\partial x$ and $\partial P/\partial y$.  
2. Form integrand $\partial Q/\partial x-\partial P/\partial y$.  
3. Integrate over $D$ using the most convenient coordinates.  

**Pitfall** – Mixing the sign in the integrand; always use $\partial Q/\partial x - \partial P/\partial y$.

---

### 5. **Determining If a Field is Incompressible**

**Cues**  
- Question: “What does zero flux through every closed surface imply?”  

**Checklist**  
1. If the flux $\iint_{\partial V}\mathbf{F}\!\cdot\!\hat{n}\,dS=0$ for **all** closed surfaces $V$, then by the divergence theorem, $\iiint_V \operatorname{div}\mathbf{F}\,dV=0$ for all $V$.  
2. The only way this holds for arbitrary $V$ is $\operatorname{div}\mathbf{F}=0$ everywhere.  
3. Conclude that the field is incompressible.

**Note** – Zero flux for *one* particular surface does **not** guarantee incompressibility; it only tells that the net outflow across that surface cancels.

---

## Common Pitfalls & Checks

| Pitfall | Check |
|---------|-------|
| **Wrong normal orientation** | Verify the surface normal points outward; for 2‑D curves, ensure counter‑clockwise orientation. |
| **Mixing circulation & flux formulas** | Use $P\,dy - Q\,dx$ for flux, $P\,dx + Q\,dy$ for circulation. |
| **Incorrect coordinate limits** | Sketch region; double‑check bounds before integrating. |
| **Omitting a component in divergence** | List $P, Q, R$ (or $F_r, F_\theta, F_z$) before differentiating. |
| **Ignoring symmetry** | Look for odd integrands over symmetric limits; they often vanish. |
| **Assuming zero flux ⇒ zero divergence everywhere** | Only true if flux is zero for every closed surface. |
| **Using the wrong version of Green’s theorem** | Identify whether the problem asks for circulation or flux. |
| **Skipping the divergence theorem step** | When the volume is simpler than the surface, always consider the divergence theorem first. |

---

**Bottom line:**  
Master the two versions of Green’s theorem (circulation and flux) and the divergence theorem. These transform complex surface or line integrals into more tractable volume or area integrals. Always check orientation, choose the simplest coordinate system, and verify each step algebraically. Good luck on the exam!

---

## Raw Slide Summaries

### Slide 1

The image is a slide from a presentation on the topic of "Divergence and the Divergence Theorem" in mathematics, specifically covering material from Trimester Chapter 14, sections 14.1 and 14.9.

**Title Section:**
The title, "Divergence and the Divergence Theorem," is prominently displayed in large black text at the top center of the slide. Below the title, a yellow rectangle contains the text "Trim Ch 14, 14.1,14.9" in smaller black font.

**Outline Section:**
To the left of the slide, under the heading "Outline:" in bold black text, are three numbered points:

1. The Concept of Divergence
2. Second Form of Green's Theorem
3. The Divergence Theorem

**Graph Section:**
On the right side of the slide, a 3D graph is presented, titled "Uniformly expanding vector field." The graph features blue arrows of varying lengths pointing outward from the center, indicating the direction and magnitude of the vectors. The x, y, and z axes are labeled with values ranging from -1 to 1.

**University Logo and URL:**
At the bottom left corner of the slide, the University of Waterloo logo is displayed, accompanied by the university's name in black text. In the bottom right corner, a URL is provided: "https://www.mathworks.com/help/matlab/ref/quiver3.html."

**Background:**
The slide has a clean white background, with a yellow stripe at the top and a black stripe above it, adding a touch of color and visual appeal to the design.

### Slide 2

The image presents a slide from a lecture on the concept of divergence, featuring three diagrams and accompanying text.

*   **Title**
    *   The title "Divergence" is prominently displayed in bold black font at the top left of the slide.
*   **Diagrams**
    *   Three diagrams are arranged horizontally across the center of the slide, each illustrating a different scenario related to molecular density and divergence.
        *   The first diagram depicts a central point with arrows radiating outward, labeled "Density of molecules around the center?" and accompanied by the statement "Density of molecules decreases!" in green text. The arrows are colored red and blue, indicating outward movement.
        *   The second diagram shows a similar central point with arrows converging inward, also labeled "Density of molecules around the center?" and accompanied by the statement "Density of molecules is increasing" in green text, followed by "'Sink' Molecules converge!" in red text. The arrows are again colored red and blue, this time indicating inward movement.
        *   The third diagram illustrates a flow of molecules along curved lines, labeled "Density of molecules inside?" and accompanied by the statement "It does not look like density of molecules inside changes" in blue text, followed by "There is no divergence!" in red text. The arrows are colored blue, indicating the direction of flow.
*   **Text**
    *   Below the diagrams, two bullet points provide further explanation:
        *   "Divergence is a measure of how much a vector field 'diverges' or 'spreads away' from a given point in space."
        *   "The divergence is related to the flux!"
*   **University Logo**
    *   In the bottom-right corner, the University of Waterloo logo is displayed, featuring a shield with a crest and the university's name in black text on a yellow background.

In summary, the slide effectively illustrates the concept of divergence through visual representations and concise explanations, providing a clear understanding of the relationship between molecular density and divergence.

### Slide 3

The image presents a slide from a presentation on vector calculus, specifically focusing on the concept of divergence. The title "Divergence" is prominently displayed at the top.

*   **Title and Introduction**
    *   The title "Divergence" is written in large black text.
    *   Below the title, a brief introduction explains that the gradient vector field of a scalar function f(x,y,z) will be written.
*   **Mathematical Definition**
    *   The equation for the gradient vector field is provided: $\vec{\nabla}f = \left(\frac{\partial}{\partial x}\hat{i} + \frac{\partial}{\partial y}\hat{j} + \frac{\partial}{\partial z}\hat{k}\right)f(x,y,z) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)$.
    *   The del operator $\vec{\nabla}$ is defined as $\left(\frac{\partial}{\partial x}\hat{i} + \frac{\partial}{\partial y}\hat{j} + \frac{\partial}{\partial z}\hat{k}\right)$.
    *   The divergence of a vector field $\vec{F} = P\hat{i} + Q\hat{j} + R\hat{k}$ is given by $\operatorname{div}(\vec{F}) = \vec{\nabla} \cdot \vec{F}$.
    *   The divergence is calculated as $\operatorname{div}(\vec{F}) = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$.
*   **Key Points and Conclusion**
    *   A note highlights that divergence takes a vector field and returns a scalar field, whereas the gradient takes a scalar field and returns a vector field.
    *   The University of Waterloo logo is displayed in the bottom-right corner.

In summary, the slide provides a clear and concise explanation of the concept of divergence in vector calculus, including its mathematical definition and key properties.

### Slide 4

The image is a slide from a presentation titled "Making Sense of the Divergence and Flux" and features a diagram illustrating the concept of divergence in two dimensions.

*   The title is prominently displayed at the top, with the subtitle "To make sense of the divergence, let us look at a curve in 2D," written below it.
*   A thought bubble contains the equation $\vec{F} = P\hat{i} + Q\hat{j}$, indicating that $\vec{F}$ is a vector field represented by its components $P$ and $Q$ in the $x$ and $y$ directions, respectively.
*   A 3D coordinate system is drawn, with the $x$, $y$, and $z$ axes labeled. The $z$-axis is pointing upwards, while the $x$ and $y$ axes are on the horizontal plane.
*   A green oval shape is drawn on the $xy$-plane, representing a closed curve $C$. The curve is parameterized by $\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j}$, where $t$ is a parameter.
*   Several blue arrows are drawn inside and around the oval, indicating the direction of the vector field $\vec{F}$ at different points.
*   A red arrow labeled $\hat{n}$ is drawn perpendicular to the curve $C$, representing the outward unit normal vector to the curve.
*   The equation $\oint_{C} \vec{F} \cdot \hat{n} ds = ?$ is written next to the diagram, suggesting that the integral of the dot product of $\vec{F}$ and $\hat{n}$ along the curve $C$ is being evaluated.
*   The equation $\hat{n} = \hat{T} \times \hat{k}$ is written below the diagram, showing how the unit normal vector $\hat{n}$ can be calculated using the tangent vector $\hat{T}$ and the unit vector $\hat{k}$ in the $z$-direction.
*   The equation $\hat{k} = (0,0,1)$ is written below, specifying the components of the unit vector $\hat{k}$.
*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

In summary, the image presents a visual representation of the concept of divergence in two dimensions, using a diagram to illustrate the vector field $\vec{F}$ and its interaction with a closed curve $C$. The accompanying equations provide mathematical expressions for calculating the flux of $\vec{F}$ through $C$.

### Slide 5

The image presents a slide from a lecture on vector calculus, specifically focusing on the divergence and flux. The title "Making Sense of the Divergence and Flux" is prominently displayed at the top in bold black text.

**Key Equations and Formulas**

The slide features several key equations and formulas, including:

* **Tangent Vector**: $\hat{T} = \frac{d\vec{r}}{ds} = \frac{dx}{ds}\hat{i} + \frac{dy}{ds}\hat{j}$
* **Normal Vector**: $\hat{n} = \hat{T} \times \hat{k} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{dx}{ds} & \frac{dy}{ds} & 0 \\ 0 & 0 & 1 \end{vmatrix} = \frac{dy}{ds}\hat{i} - \frac{dx}{ds}\hat{j}$
* **Flux**: $\vec{F} \cdot \hat{n} = (P\hat{i} + Q\hat{j}) \cdot (\frac{dy}{ds}\hat{i} - \frac{dx}{ds}\hat{j}) = P\frac{dy}{ds} - Q\frac{dx}{ds}$
* **Line Integral**: $\oint_C \vec{F} \cdot \hat{n} ds = \oint_C Pdy - Qdx$

**Additional Notations**

* The notation "NORMAL COMP. VECTOR FIELD" is written in blue text to the right of the flux equation.
* The University of Waterloo logo is displayed in the bottom-right corner, indicating the institution associated with the lecture.

**Overall Content**

The slide provides a concise overview of the mathematical concepts related to divergence and flux, including the definitions of tangent and normal vectors, and the calculation of flux through a line integral. The use of color-coded text (red and blue) helps to distinguish between different components of the equations and highlights important concepts.

### Slide 6

The image presents a slide from a lecture on the topic of "Making Sense of the Divergence and Flux" in the context of vector calculus, specifically focusing on Green's Theorem. The content is divided into sections, with key equations and explanations provided.

**Title and Introduction**

*   The title "Making Sense of the Divergence and Flux" is prominently displayed at the top.
*   Below the title, the text "Recall that the Green's Theorem is given by," serves as an introduction to the main equation.

**Green's Theorem Equation**

*   The equation for Green's Theorem is presented:
    *   $\oint_{C} Pdx + Qdy = \iint_{D} \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$
*   Handwritten notes above the equation indicate new assignments for P and Q: $Q = P$ and $P = -Q$.

**Application of Green's Theorem to 2-D Flux Integral**

*   The text "Let us use Green's Theorem to calculate this 2-D flux integral:" precedes the application.
*   The equation derived from Green's Theorem for the 2-D flux integral is:
    *   $\oint_{C} -Qdx + Pdy = \iint_{D} \left(\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y}\right) dA$
    *   This is further annotated to show its equivalence to $\oint_{C} \vec{F} \cdot \hat{n} ds$, where $\iint_{D} \left(\frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y}\right) dA$ is labeled as "div $\vec{F}$".

**Additional Information**

*   The University of Waterloo logo is displayed in the bottom-right corner, indicating the institution associated with the lecture.
*   The background of the slide is white, with a black and yellow border at the top, and the main text and equations are presented in black, with handwritten notes in blue.

### Slide 7

The slide is titled "Green's Normal Vector Form" and contains the following information:

* A statement: "We can therefore re-write the flux across the curve C as,"
* An equation: 
  * $\oint \vec{F} \cdot \hat{n} ds = \iint_{D} div(\vec{F}) dA$
  * The left-hand side of the equation is annotated with "Flux Across the Curve C" in blue handwriting.
  * The right-hand side of the equation is annotated with "Sums up All Divergence Across D" in blue handwriting.
* A statement: "This expression is known as the Green's Normal Vector Form"
* A logo for the University of Waterloo in the bottom-right corner.

The slide has a white background with a black and yellow border at the top. There are no diagrams or images on the slide. The text is presented in a clear and concise manner, with the equation and annotations being the main focus of the slide.

### Slide 8

The image is a slide from a presentation on the topic of divergence in vector fields, titled "Sign of the Divergence" and attributed to the University of Waterloo.

*   The title is displayed prominently at the top of the slide.
    *   The title is written in large black text.
*   A subtitle below the title reads, "Going back to our initial fields,".
    *   The subtitle is written in smaller black text.
*   Three hand-drawn diagrams are presented, each illustrating a different scenario related to divergence.
    *   The first diagram shows a field spreading away from a central point, with arrows radiating outward.
        *   The diagram includes the notation "IF FIELD SPREADS AWAY" and "div → +".
    *   The second diagram depicts a field converging towards a central point, with arrows pointing inward.
        *   The diagram includes the notation "IF FIELD IS CONVERGING" and "div → -".
    *   The third diagram illustrates a field with zero divergence, represented by arrows that are not converging or diverging.
        *   The diagram includes the notation "IF div → ZERO!" and "FIELD IS CALLED 'INCOMPRESSIBLE'".
*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.
    *   The logo features the university's name in black and orange text, accompanied by a small orange graphic.

In summary, the slide provides a visual explanation of the concept of divergence in vector fields, using simple diagrams and notation to illustrate the different scenarios. The content is presented in a clear and concise manner, making it easy to understand for students or individuals new to the topic.

### Slide 9

The image presents a slide titled "The Divergence Theorem" in bold black text at the top, set against a white background with a black and yellow border at the top. The slide is divided into several sections, each containing various elements that convey information about the Divergence Theorem.

*   **Title and Diagram**
    *   The title "The Divergence Theorem" is prominently displayed at the top.
    *   A diagram illustrating the concept is drawn below the title, featuring a purple oval shape labeled "S" and "E" inside it.
    *   The diagram includes green arrows pointing outward from the surface "S", indicating the direction of the vector field.
    *   A blue 3D coordinate system is shown on the left side of the diagram.
*   **Mathematical Equations**
    *   The equation ∫∫S F·n dσ = ∫∫E div(F) dV is written to the right of the diagram, representing the Divergence Theorem.
    *   The equation is accompanied by explanatory notes in blue handwriting, which read: "Sums up all our differentials of flux across 'S'" and "Sums up the divergence of F across volume E".
*   **Definitions and Notations**
    *   Below the diagram, three definitions are provided:
        *   S → Boundary of E
        *   n → Outward unit vector
        *   F → Vector Field in 3D
    *   These definitions clarify the notation used in the equation and diagram.
*   **University Logo**
    *   In the bottom-right corner, the logo of the University of Waterloo is displayed, featuring a shield with a red and yellow design, accompanied by the university's name in black text.

In summary, the image effectively conveys the concept of the Divergence Theorem through a combination of visual and textual elements. The diagram illustrates the theorem's application to a 3D vector field, while the accompanying equations and definitions provide a clear understanding of the mathematical concepts involved.

### Slide 10

The image presents a slide from a presentation on the Divergence Theorem, featuring a white background with black text and a yellow stripe at the top. The title "Using the Divergence Theorem" is prominently displayed in large bold font.

**Problem Statement:**
The problem asks to find the flux of a given vector field across a solid formed by three surfaces:

*   The xy-plane
*   The x-z plane
*   Two surfaces defined by the equations:
    *   z = 1 - x^2
    *   y = 3 - z

The vector field is represented as:

F = (1/2x^2 + cos^2(2y))i + (xy)j + cos^2(xy)k

**Solution:**
The solution to the problem is provided below the problem statement, with the answer being:

Flux = 0

**University Logo:**
In the bottom-right corner of the slide, the logo of the University of Waterloo is displayed, accompanied by the university's name in black text.

Overall, the slide effectively conveys a mathematical problem and its solution related to the Divergence Theorem, set against a clean and simple visual backdrop.

### Slide 11

The image presents a slide from a presentation on the Divergence Theorem, featuring a 3D graph and accompanying mathematical equations.

**Title:** "Using the Divergence Theorem"

*   The title is prominently displayed in large black text at the top of the slide.
*   Below the title, the subtitle "Let us sketch the surface," is written in smaller black text.

**Graph:**

*   A 3D graph is centered on the slide, showcasing a curved surface with various lines and labels.
*   The x-axis is represented by a blue line extending from the origin to the right, labeled "x" at its end.
*   The y-axis is depicted as a blue line extending from the origin upwards, labeled "y" at its end.
*   The z-axis is shown as a blue line extending from the origin towards the viewer, labeled "z" at its end.
*   The surface is defined by three equations:
    *   z = 1 - x^2 (green curve)
    *   z = 0 (black line)
    *   y = 3 - z (red curve)

**Equations:**

*   To the right of the graph, several equations are listed under the heading "INTERSECTIONS:" in black text.
*   The equations are:
    *   z = 1 - x^2
    *   x^2 = y - 2
    *   z = 3 - y
    *   x = ±1, y = 3, z = 0
    *   x = 0, y = 2, z = 1

**Logo:**

*   In the bottom-right corner of the slide, the logo for the University of Waterloo is displayed.
*   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.

Overall, the slide effectively illustrates the concept of the Divergence Theorem using a clear and concise visual representation, supported by relevant mathematical equations.

### Slide 12

The slide is titled "Using the Divergence Theorem" and features a white background with a horizontal stripe at the top that transitions from black to yellow. 

* The title, "Using the Divergence Theorem," is prominently displayed in large, bold, black font at the top of the slide.
* The University of Waterloo logo is located in the bottom-right corner, consisting of:
  * A shield with a red and gold design
  * The text "UNIVERSITY OF WATERLOO" in black font, with "WATERLOO" in bold

The slide is otherwise blank, with no additional content, diagrams, or images present.

### Slide 13

The image presents a slide from a presentation on the Divergence Theorem, featuring a 3D graph and accompanying text. The title, "Using the Divergence Theorem," is prominently displayed in large black font at the top of the slide.

**Key Elements:**

* **Title:** "Using the Divergence Theorem" in large black font
* **3D Graph:**
	+ Depicts a 3D surface with x, y, and z axes
	+ Surface defined by the equations:
		- z = 1 - x^2 (green curve)
		- y = 3 - z (red curve)
		- z = 0 (black line)
	+ Axes labeled with corresponding variables (x, y, z)
* **University Logo:**
	+ University of Waterloo logo in the bottom-right corner
	+ Features a shield with a red and gold crest, accompanied by the university's name in black text

**Summary:**

The slide effectively illustrates the application of the Divergence Theorem using a 3D graph, providing a clear visual representation of the concept. The inclusion of the University of Waterloo logo indicates the slide's origin and adds a touch of professionalism to the presentation.

### Slide 14

The image is a presentation slide titled "Using the Divergence Theorem" in large black text at the top. The title is centered and positioned below a thick black bar that spans the width of the slide, followed by a thin yellow bar.

*   The main content area of the slide is blank, with no text or images.
*   In the bottom-right corner, there is a logo for the University of Waterloo, featuring a shield with a red and gold design, accompanied by the university's name in black text.
*   The background of the slide is white.

This slide appears to be an introductory or title slide for a presentation on the Divergence Theorem, likely used in an academic setting at the University of Waterloo.

### Slide 15

The slide is titled "Using the Divergence Theorem" and features a white background with a black and yellow stripe at the top.

The title is prominently displayed in large, bold, black font at the top of the slide. 

Below the title, there is a question posed in smaller black text: "What does it imply about a vector field $\vec{F}$ when the flux through a surface is zero?" The word "Question:" is highlighted in blue.

In the bottom-right corner, the University of Waterloo logo is visible, accompanied by the text "UNIVERSITY OF WATERLOO" in black font. The logo consists of a shield with a crest above it, featuring a red and yellow design.

There are no diagrams or images on this slide, only text.

### Slide 16

The image presents a summary slide on the topic of divergence, likely from a lecture or presentation at the University of Waterloo. The content is structured into four main bullet points, each addressing a distinct aspect of divergence.

*   **Divergence Definition**
    *   The first bullet point defines divergence as a measure of how much a vector field "diverges" or "spreads away" from a given point in space.
*   **Divergence Theorem Statement**
    *   The second bullet point states the divergence theorem, which asserts that the net flux outward of a vector field across a closed surface in space can be calculated by integrating the divergence of the field over the region enclosed by the surface.
*   **Divergence Theorem Simplification**
    *   The third bullet point highlights the simplification provided by the divergence theorem, converting a surface integral over a surface S into a triple integral over a solid E enclosed by that surface.
*   **Incompressible Vector Field Condition**
    *   The fourth bullet point defines an incompressible vector field as one whose flux is zero.

In summary, the image provides a concise overview of key concepts related to divergence, including its definition, the divergence theorem, and its implications for calculating flux and characterizing incompressible vector fields.

