# Lecture 35 - Stoke's Theorem

## Study Notes

# Curl & Stokes / Green – Problem‑Solving Exam Notes

---

## Core Formulas & Definitions

| Formula | Symbols & Meaning | When to Use |
|---------|-------------------|-------------|
| **Curl (3‑D)**<br>$$\nabla \times \mathbf{F}= \begin{vmatrix}\hat{\imath}&\hat{\jmath}&\hat{k}\\ \partial_x&\partial_y&\partial_z\\ P&Q&R\end{vmatrix}$$ | • $\mathbf{F}=P\,\hat{\imath}+Q\,\hat{\jmath}+R\,\hat{k}$  <br>• $\partial_x=\partial/\partial x$, etc. <br>• Unit vectors $\hat{\imath},\hat{\jmath},\hat{k}$ | Compute local rotation; test for irrotationality ($\nabla\times\mathbf{F}=0$). |
| **Curl (2‑D, scalar)**<br>$$\operatorname{curl}_k \mathbf{F}= \partial_x Q-\partial_y P$$ | • $\mathbf{F}=P\,\hat{\imath}+Q\,\hat{\jmath}$ in the $xy$–plane. | Evaluate planar field rotation; feed into Green’s Theorem. |
| **Stokes’ Theorem**<br>$$\oint_{\partial S}\mathbf{F}\!\cdot\! d\mathbf{r}= \iint_S (\nabla\times\mathbf{F})\!\cdot\! \hat{\mathbf{n}}\, d\sigma$$ | • $S$: smooth, oriented surface. <br>• $\partial S$: positively oriented boundary curve (right‑hand rule). <br>• $\hat{\mathbf{n}}$: unit normal. | Convert a closed line integral into a surface integral of the curl. |
| **Green’s Theorem (circulation form)**<br>$$\oint_{C}\mathbf{F}\!\cdot\! d\mathbf{r}= \iint_D (\partial_x Q-\partial_y P)\, dA$$ | • $C$: simple, positively oriented curve in the $xy$–plane. <br>• $D$: region bounded by $C$. | Fast evaluation of planar line integrals; the integrand is the scalar curl. |
| **Irrotational Field**<br>$$\nabla\times\mathbf{F}= \mathbf{0}$$ | • No local rotation; the field is locally conservative. | Determines if $\oint \mathbf{F}\cdot d\mathbf{r}=0$ in any simply connected region. |
| **Conservative Field (in simply connected domain)**<br>$$\mathbf{F}=\nabla\phi \quad\Longleftrightarrow\quad \nabla\times\mathbf{F}=0$$ | • $\phi$: scalar potential. | Guarantees path independence; shortcut for many integrals. |

---

## Key Concepts & Intuition

- **Curl ≠ Divergence** – Curl checks for rotation; divergence checks for sources/sinks.  
- **Orientation** – Right‑hand rule: thumb along $\hat{\mathbf{n}}$, fingers curl in the direction of the curve. Wrong orientation flips sign.  
- **Smooth, Oriented Surface** – Must be differentiable; its boundary must match the given curve.  
- **Planar Specialization** – In the $xy$–plane, only the $k$–component of the curl matters; Stokes reduces to Green.  
- **Irrotational ⇔ Zero Curl** – In a simply connected domain, this is equivalent to being conservative.  
- **Green’s Circulation‑Curl Form** – “Tangential” form; the scalar curl appears as the integrand.

---

## Problem‑Solving Strategies

### 1.  Evaluate a Closed Line Integral

| Step | Action | Check |
|------|--------|-------|
| **1. Identify field type** | 3‑D or 2‑D? | If 2‑D → use Green. |
| **2. Test for conservativeness** | Compute $\nabla\times\mathbf{F}$; if zero and domain simply connected → integral = 0. | Verify simply connectedness (no holes). |
| **3. Choose an approach** | • Use Stokes/Green if curl is simpler. <br>• Use parameterization of the curve directly if the integral is simple. | Compare effort. |
| **4. For Stokes/Green** | • Compute the curl. <br>• Parameterize the surface/region. <br>• Compute $\hat{\mathbf{n}}\,d\sigma$ (planar: $dA$, non‑planar: $|\mathbf{r}_u\times\mathbf{r}_v|\,du\,dv$). | Confirm orientation via right‑hand rule. |
| **5. Evaluate the surface integral** | Perform the double integral, simplify algebraically. | Watch for symmetry that kills the integral. |
| **6. Verify sign** | Check orientation of the chosen normal against the curve direction. | Flip if result negative but should be positive (or vice‑versa). |

### 2.  Compute the Curl of a Field

| Step | Action |
|------|--------|
| **1. Write components** | $P(x,y,z)$, $Q(x,y,z)$, $R(x,y,z)$ (set $R=0$ for 2‑D). |
| **2. Apply determinant or expanded formula** | Use the compact determinant or component‑wise differences. |
| **3. Simplify** | Combine like terms; cancel zero derivatives. |
| **4. Interpret** | Non‑zero vector → local rotation; zero vector → irrotational. |

### 3.  Apply Green’s Theorem (Planar)

| Step | Action |
|------|--------|
| **1. Confirm planar curve** | $C$ lies in $xy$–plane; simple and closed. |
| **2. Identify $P,Q$** | Extract from $\mathbf{F}=P\,\hat{\imath}+Q\,\hat{\jmath}$. |
| **3. Compute scalar curl** | $\partial_x Q-\partial_y P$. |
| **4. Set up area integral** | $\iint_D (\partial_x Q-\partial_y P)\,dA$; choose coordinates or symmetry. |
| **5. Integrate** | Evaluate over $D$. |
| **6. Check orientation** | Counter‑clockwise traversal → positive orientation; otherwise flip sign. |

### 4.  Verify Orientation in Practice

- **Right‑hand rule**: Thumb → $\hat{\mathbf{n}}$; fingers → boundary direction.  
- **Cross‑product check**: If two tangent vectors $\mathbf{T}_1,\mathbf{T}_2$ on $S$, then $\hat{\mathbf{n}}\propto\mathbf{T}_1\times\mathbf{T}_2$.  
- **Parametric surface**: If $\mathbf{r}(u,v)$, normal is $\mathbf{r}_u\times\mathbf{r}_v$; orientation is given by order of $u,v$.  
- **Curve parametrization**: For $\mathbf{r}(t)$, orientation is direction of increasing $t$.

---

## Common Pitfalls & Checks

| Pitfall | Fix |
|---------|-----|
| Wrong normal direction | Re‑draw surface; re‑apply right‑hand rule. |
| Using non‑planar $d\sigma$ as $dA$ | Compute $|\mathbf{r}_u\times\mathbf{r}_v|$ for curved surfaces. |
| Ignoring $R$ component in 3‑D curl | Include all components; even zero $R$ affects partials. |
| Assuming any zero curl ⇒ conservative | Confirm domain is simply connected. |
| Flipping curve orientation | Verify $t$ increase direction or use counter‑clockwise test. |
| Mixing up $\partial_x$ and $\partial_y$ in scalar curl | Double‑check signs: $\partial_x Q - \partial_y P$. |
| Reversing integration limits in surface parameterization | Ensure $u,v$ bounds match the region orientation. |

---

## Quick Reference Checklist

- **Field dimension?**  
  - 3‑D → full curl & Stokes.  
  - 2‑D → scalar curl & Green.  
- **Is the curl zero?**  
  - If yes and domain simply connected → integral = 0.  
- **Can we use a theorem?**  
  - Yes → set up surface/region integral.  
- **Is the chosen normal correct?**  
  - Right‑hand rule + cross‑product consistency.  
- **Do the partial derivatives look messy?**  
  - Look for symmetry or coordinate change (e.g., polar).  
- **Orientation mismatch?**  
  - Reverse sign.  

---

**Example Quick Flow:**  
1. **Line integral given** → Compute curl.  
2. **Curl non‑zero** → Choose Stokes/Green.  
3. **Parameterize surface** → Compute normal and area element.  
4. **Integrate** → Simplify algebra.  
5. **Check sign** → Adjust if needed.  

Good luck with the exam!

---

## Raw Slide Summaries

### Slide 1

The image is a presentation slide titled "Curl and the Stokes's Theorem" in large black text at the top. 

* The title is followed by a yellow box with black text that reads "Trim Ch 14, 14.1, 14.10".
* Below this, there is an outline with two points: 
  1. "The Concept of Curl"
  2. "Stoke's Theorem"
* To the right of the outline, there is a photograph of a sailboat on rough seas, with a red rectangle highlighting a section of the water.
* At the bottom of the slide, there is a logo for the University of Waterloo, accompanied by a caption that reads: "Pascal Oddo's Leopard 3 in rough seas during the 2017 Rolex Middle Sea Race (https://i.imgur.com/30iDYV3.jpg)".
* The background of the slide is white, with a black and yellow border at the top.

The slide appears to be part of a lecture or presentation on vector calculus, specifically covering the topics of curl and Stokes' theorem.

### Slide 2

The image presents a detailed diagram illustrating the concept of curl in fluid dynamics, featuring handwritten notes and equations on a white background.

**Title**
At the top center, the title "The Concept of Curl" is prominently displayed in large black text.

**Diagrams**
Two diagrams are presented side by side, each with its own set of annotations. The left diagram depicts a graph with a blue x-axis and y-axis, accompanied by arrows indicating the direction of water flow. A red vertical line is drawn along the y-axis, while a green diagonal line intersects the x-axis. The annotations highlight the movement of water to the right, with increasing speed as it moves further to the right. The diagram also includes the equation "F = y^2 i" and notes that "water is moving to the right but faster" and "if F changes in the 'x' direction -> net torque on twig." A blue arrow points to the text "The curl (F) is a measure of how much F is rotating."

The right diagram shows a similar graph with a blue x-axis and y-axis, featuring a red curved line that illustrates the concept of net torque or "curl." The annotations emphasize that "net torque or 'curl' is larger."

**Logo**
In the bottom-right corner, the logo for the University of Waterloo is displayed, consisting of a black shield with a gold crest and the university's name written in black text.

**Background**
The image features a white background with a yellow stripe at the top.

Overall, the image effectively conveys complex concepts related to fluid dynamics and curl, making it a valuable resource for students and professionals in the field.

### Slide 3

The image presents a slide from a presentation on vector calculus, specifically focusing on the definition of curl. The title "Definition of Curl" is prominently displayed at the top in bold black text.

Below the title, the main content is organized into three sections:

**Section 1: Definition**
The first section defines the curl of a vector field $\vec{F} = P\hat{i} + Q\hat{j} + R\hat{k}$ as $\text{CURL}(\vec{F}) = \vec{\nabla} \times \vec{F}$.

**Section 2: Computation**
The second section explains how to compute the curl using the determinant formula:
$\text{CURL}(\vec{F}) = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{vmatrix}$.

**Section 3: Expanded Formula**
The third section provides the expanded formula for the curl:
$\text{CURL}(\vec{F}) = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}\right)\hat{i} + \left(\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}\right)\hat{j} + \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\hat{k}$.

In the bottom-right corner, the logo of the University of Waterloo is visible, featuring a shield with a red and yellow design, accompanied by the university's name in black text. The background of the slide is white, with a yellow stripe at the top and a black stripe above it.

### Slide 4

The image presents a slide from a presentation on the topic of "Making Sense of the Curl" in the context of vector calculus, specifically focusing on the circulation of a vector field around closed paths.

*   The title "Making Sense of the Curl" is prominently displayed at the top of the slide.
    *   It is followed by a brief introduction that sets the stage for the discussion: "Let us suppose that we want to calculate the total counter-clockwise circulation $\oint_{C} \vec{F} \cdot d\vec{r}$ on the following closed paths."
*   Two diagrams are presented side by side to illustrate the concept.
    *   Both diagrams feature a green curve representing the closed path $C$, with arrows indicating the direction of traversal.
    *   The diagrams also include purple arrows to represent the vector field $\vec{F}$ and a red rectangle to symbolize an object being pushed or rotated by the field.
    *   The left diagram shows the object being pushed without rotation, resulting in zero circulation ($\oint_{C} \vec{F} \cdot d\vec{r} = 0$) and zero curl ($\text{curl} \vec{F} = 0$).
    *   In contrast, the right diagram depicts the object being rotated, leading to positive circulation ($\oint_{C} \vec{F} \cdot d\vec{r} > 0$) and positive curl ($\text{curl} \vec{F} > 0$).
*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

In summary, the slide effectively illustrates the relationship between the circulation of a vector field around a closed path and the curl of the field, using visual aids to facilitate understanding of these fundamental concepts in vector calculus.

### Slide 5

The image is a slide from a presentation on vector calculus, specifically discussing Stokes' Theorem. The title of the slide is "Making Sense of the Curl" and it features a diagram and mathematical equations.

*   The title is in large black text at the top of the slide, with the subtitle "Let us suppose that we want to calculate the total counter-clockwise circulation $\oint_{C} \vec{F} \cdot d\vec{r}$ on the following closed paths." written below it in smaller text.
    *   The title is centered and takes up two lines.
    *   The subtitle is also centered and takes up two lines.
*   A diagram is shown on the left side of the slide, illustrating a closed curve $C$ enclosing a surface $S$.
    *   The diagram is hand-drawn in green, blue, and purple ink.
    *   The curve $C$ is represented by a green line, with arrows indicating the direction of integration.
    *   The surface $S$ is represented by a blue grid, with purple arrows indicating the direction of the normal vector.
    *   The diagram is labeled with various symbols, including $x$, $y$, and $z$, which represent the coordinates of the points on the curve and surface.
*   To the right of the diagram, several mathematical equations are written in red and green ink.
    *   The first equation is Stokes' Theorem, which relates the line integral of a vector field around a closed curve to the surface integral of the curl of the vector field over the surface enclosed by the curve.
    *   The equation is written as $\oint_{C} \vec{F} \cdot d\vec{r} = \iint_{S} (\nabla \times \vec{F}) \cdot \hat{n} d\sigma$.
    *   Below this equation, there are several other equations and notes that provide additional context and explanation.
    *   The equations include the value of the line integral over $C$, the sum of all curls over "S" in the normal direction, and the curl of $\vec{F}$.
*   At the bottom-right corner of the slide, there is a logo for the University of Waterloo.
    *   The logo features a shield with a crest and the words "UNIVERSITY OF WATERLOO" written next to it.

Overall, the slide provides a clear and concise explanation of Stokes' Theorem and its application to calculating the circulation of a vector field around a closed curve. The diagram and equations work together to illustrate the concept and provide a step-by-step guide to applying the theorem.

### Slide 6

The image presents a slide from a presentation on Stokes's Theorem, featuring a title, a mathematical definition, and an accompanying diagram. The content is as follows:

**Title**
* "Stokes's Theorem" in large black text at the top left of the slide.

**Mathematical Definition**

* A paragraph explaining the theorem:
	+ Let S be an oriented piece-wise smooth surface that is bounded by a simple, close, piecewise smooth boundary curve C with positive orientation.
	+ Let $\vec{F}$ be a vector field whose components have continuous partial derivatives on an open region that contains S.
	+ Then, $\oint_{C} \vec{F} \cdot d\vec{r} = \iint_{S} (\nabla \times \vec{F}) \cdot \hat{n} d\sigma$

**Diagram**

* A 3D graph with a green surface S and a red curve C on the right side of the slide.
* The surface S is oriented with purple arrows indicating its normal vector.
* The curve C is oriented counterclockwise when viewed from above.
* A blue arrow labeled "z" points upwards from the origin.
* A blue "x" and a blue "y" are shown at the end of two blue arrows pointing to the right and out of the page, respectively.

**University Logo**

* The University of Waterloo logo is displayed in the bottom-right corner of the slide.

This slide provides a concise overview of Stokes's Theorem, including its mathematical formulation and a visual representation of the concepts involved.

### Slide 7

The image presents a slide from a presentation on Stokes' Theorem and Surface Orientation, featuring two diagrams that illustrate the concept of orientation in relation to the theorem.

*   The title "Stokes's Theorem and Surface Orientation" is prominently displayed at the top of the slide.
    *   The title is written in bold black text.
*   A paragraph below the title explains the importance of using the correct orientation when applying Stokes' Theorem.
    *   The text is written in black font.
    *   It states, "To use Stoke's Theorem correctly we need to make sure that we are using the correct orientation."
*   Two diagrams are presented side-by-side, each depicting a surface S bounded by a curve C.
    *   The diagrams are hand-drawn and feature green lines representing the surface S and purple lines representing the curve C.
    *   A stick figure is shown walking along the curve C in both diagrams.
    *   In the left diagram, the stick figure is walking in a counterclockwise direction, while in the right diagram, it is walking in a clockwise direction.
    *   The left diagram is labeled "Positive Orientation," indicating that the orientation of the curve C is positive.
    *   The right diagram is also labeled "Positive Orientation," but with an additional notation indicating that the normal vector n̂ points outward from the surface S.
*   A paragraph below the diagrams provides further explanation of the concept of positive orientation.
    *   The text is written in black font.
    *   It states, "If we pick n̂ as the normal vector, to induce positive orientation on the curve C, we need to 'walk' along C in a way so that our head is pointing in the direction of n̂, and the surface S is to our left."
*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.
    *   The logo features the university's name in black text, accompanied by a crest or emblem.

In summary, the slide effectively illustrates the concept of surface orientation in relation to Stokes' Theorem, using clear and concise language and visual aids to convey the information.

### Slide 8

The image presents a lecture slide on Stokes's Theorem and Green's Theorem, featuring a detailed diagram and mathematical equations. The slide is divided into sections, with the title "Stokes's Theorem and Green's Theorem" prominently displayed at the top.

**Title and Subtitle**

*   **Title:** Stokes's Theorem and Green's Theorem
*   **Subtitle:** Stokes's Theorem is given by,

**Main Equation**

*   The main equation is: $\oint_{C} \vec{F} \cdot d\vec{r} = \iint_{S} (\vec{\nabla} \times \vec{F}) \cdot \hat{n} d\sigma$

**Text Below the Equation**

*   Let us look at a curve C in the x-y plane,

**Diagram**

*   The diagram is a 3D representation of a curve C in the x-y plane, with arrows indicating the direction of the curve.
*   The diagram includes various mathematical notations and symbols, such as:
    *   $\vec{F} = P\hat{i} + Q\hat{j}$
    *   $\text{CURL}(\vec{F}) = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & 0 \end{vmatrix} = (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\hat{k}$
    *   $C: \vec{r}(t) = x(t)\hat{i} + y(t)\hat{j}$

**University Logo**

*   The logo of the University of Waterloo is displayed in the bottom-right corner of the slide.

The slide provides a clear and concise explanation of Stokes's Theorem and its application to a curve in the x-y plane, accompanied by a detailed diagram and relevant mathematical equations.

### Slide 9

The image is a slide from a presentation on Stokes's Theorem and Green's Theorem, featuring handwritten notes in blue ink on a white background. The title, "Stokes's Theorem and Green's Theorem," is prominently displayed at the top in bold black text.

* **Title and Handwritten Notes**
	+ Title: "Stokes's Theorem and Green's Theorem" in bold black text
	+ Handwritten notes in blue ink
* **First Equation**
	+ $\text{CURL}(\vec{F}) \cdot \hat{k} = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$
	+ $\text{CURL}(\vec{F}) \cdot \hat{n}$ (notation below the equation)
* **Second Equation**
	+ $\oint_{C} \vec{F} \cdot d\vec{r} = \iint_{R_{xy}} \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$
	+ $dA$ is equivalent to $d\sigma$ for $R_{xy}$ (notation to the right of the equation)
* **Text Below the Equations**
	+ "Green's Circulation-Curl or Tangential form is the 2D version of Stokes's Theorem!" in blue text
* **University Logo**
	+ University of Waterloo logo in the bottom-right corner
* **Background and Border**
	+ White background
	+ Yellow and black border at the top

The slide presents a concise overview of the relationship between Stokes's Theorem and Green's Theorem, highlighting their connection through handwritten notes and equations.

### Slide 10

The image presents a slide from a presentation on vector calculus, featuring a white background with a black and yellow border at the top. The title "Summary" is prominently displayed in large, bold black text at the top left of the slide.

The main content of the slide consists of four bullet points, each describing a key concept related to vector fields and the Stokes' Theorem:

• The curl of a vector field is a measure of how much the vector field is rotating
• If the curl of a vector field is zero, the vector field is called "irrotational"
• The Stokes' Theorem states that the value of a line integral involving vector fields along a closed curve C (also called circulation), is equal to the sum of all the curls over the surface S bounded by that curve.
• For the Stoke's Theorem to apply, S should be a smooth surface oriented so that it induces a positive orientation of its boundary C

In the bottom-right corner of the slide, the logo for the University of Waterloo is visible, indicating the institution associated with the presentation.

Overall, the slide provides a concise summary of important concepts in vector calculus, making it a useful resource for students or professionals looking to review or understand these fundamental ideas.

