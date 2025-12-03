# Lecture 32 - Surface Integrals

## Study Notes

# Surface Integrals – Exam‑Ready Problem‑Solving Notes

---

## Core Formulas & Definitions

| Symbol | Meaning | Typical Use |
|--------|---------|-------------|
| \(S\) | Surface in \(\mathbb{R}^3\) (implicit \(f(x,y,z)=c\) or parametric \(\mathbf r(u,v)\)) | All surface‑integral problems |
| \(R\) | Projection of \(S\) onto a coordinate plane or the parameter domain | Convert surface integral to a planar double integral |
| \(\nabla f\) | Gradient of \(f\) (normal vector to \(S\) when \(S: f=c\)) | Needed for the Jacobian factor |
| \(\hat p\) | Unit vector normal to the chosen projection plane (\(\hat k,\hat j,\hat i\)) | Appears in the change‑of‑variables formula |
| \(\gamma\) | Angle between \(\nabla f\) and \(\hat p\) | \(\cos\gamma = \dfrac{|\nabla f\!\cdot\!\hat p|}{|\nabla f|}\) |
| \(d\sigma\) | Surface‑area element on \(S\) | Fundamental in surface integrals |
| \(dA\) | Area element on the projection \(R\) | Used after projecting \(S\) |
| \(\delta(x,y,z)\) | Surface density (mass per unit area) | Mass, moments, inertia calculations |
| \(g(x,y,z)\) | Scalar field to integrate over \(S\) | General integrand |

### Scalar Surface Integral

\[
\boxed{\displaystyle \iint_S g\,d\sigma}
\]

If \(S\) is given implicitly by \(f(x,y,z)=c\) and we project onto a plane with normal \(\hat p\),

\[
\boxed{\displaystyle 
\iint_S g\,d\sigma
= \iint_R g(x,y,z)\;
\frac{|\nabla f|}{|\nabla f\!\cdot\!\hat p|}\,dA}
\]

---

### Mass and Moments of a Thin Shell

| Quantity | Formula |
|----------|---------|
| Surface area | \(A_S = \iint_S d\sigma\) |
| Mass | \(M_S = \iint_S \delta\,d\sigma\) |
| First moments | \(\displaystyle M_{yz}=\iint_S x\,\delta\,d\sigma,\;
  M_{xz}=\iint_S y\,\delta\,d\sigma,\;
  M_{xy}=\iint_S z\,\delta\,d\sigma\) |
| Center of mass | \(\displaystyle \bar{x}=\frac{M_{yz}}{M_S},\;
  \bar{y}=\frac{M_{xz}}{M_S},\;
  \bar{z}=\frac{M_{xy}}{M_S}\) |
| Moments of inertia about coordinate axes | \(\displaystyle 
I_x=\iint_S (y^2+z^2)\,\delta\,d\sigma,\;
I_y=\iint_S (x^2+z^2)\,\delta\,d\sigma,\;
I_z=\iint_S (x^2+y^2)\,\delta\,d\sigma\) |
| Moment of inertia about a line \(L\) | \(\displaystyle 
I_L=\iint_S r^2(x,y,z)\,\delta\,d\sigma\)  (with \(r\) distance to \(L\)) |

---

## Key Concepts & Intuition

- **Surface element ≈ parallelogram on the tangent plane.**  
  Its area equals the area of the projection divided by \(\cos\gamma\).

- **Change of variables to a planar domain.**  
  Replace \(d\sigma\) with \(\dfrac{|\nabla f|}{|\nabla f\!\cdot\!\hat p|}\,dA\).

- **Projection choice.**  
  Pick \(\hat p\) so that the projection is simple and \(|\nabla f\!\cdot\!\hat p|\neq0\).

- **Thin shell physics.**  
  All physical quantities (mass, moments, inertia) are surface integrals with the density \(\delta\) as the integrand.

- **Moments of inertia about axes.**  
  Integrate the squared distance to the axis times density; the axis itself appears in the integrand.

- **Inertia about an arbitrary line.**  
  Compute \(r^2\) (squared distance to the line) analytically or via coordinate shift.

---

## Problem‑Solving Strategies

### 1. Surface Integral of a Scalar Field on \(S: f=c\)

1. **Choose projection plane**  
   - Use \(\hat k\) for \(xy\)-projection if \(f\) can be solved for \(z\), etc.
2. **Solve for the normal variable**  
   - Express \(z=h(x,y)\) or \(x=h(y,z)\) as needed.
3. **Compute \(\nabla f\) and the Jacobian factor**  
   - \(\displaystyle J=\frac{|\nabla f|}{|\nabla f\!\cdot\!\hat p|}\).
4. **Set up the planar integral**  
   - \(\displaystyle \iint_R g(x,y,h(x,y))\,J\,dx\,dy\) (or appropriate variables).
5. **Integrate**  
   - Use symmetry, polar coordinates, or standard techniques.

**Typical Cues:** “Implicit surface,” “change of variables,” “projection onto …”

---

### 2. Surface Integral on a Parametric Surface \(\mathbf r(u,v)\)

1. **Compute tangent vectors**  
   - \(\mathbf r_u,\ \mathbf r_v\).
2. **Find normal vector**  
   - \(\mathbf n = \mathbf r_u \times \mathbf r_v\).
3. **Surface element**  
   - \(d\sigma = |\mathbf n|\,du\,dv\).
4. **Integral**  
   - \(\displaystyle \iint_D g(\mathbf r(u,v))\,|\mathbf r_u \times \mathbf r_v|\,du\,dv\).

**Typical Cues:** “Parametric surface,” “cross product,” “tangent vectors.”

---

### 3. Mass, Center of Mass, and Moments of a Thin Shell

1. **Identify \(\delta(x,y,z)\).**  
2. **Compute mass**  
   - \(M_S = \iint_S \delta\,d\sigma\).
3. **Compute first moments**  
   - \(M_{yz}=\iint_S x\,\delta\,d\sigma\) etc.
4. **Center of mass**  
   - \(\bar{x}=M_{yz}/M_S\), \(\bar{y}=M_{xz}/M_S\), \(\bar{z}=M_{xy}/M_S\).
5. **Compute moments of inertia**  
   - Use the formulas for \(I_x,I_y,I_z\).

**Typical Cues:** “Center of mass,” “first moments,” “moment of inertia,” “density \(\delta\).”

---

### 4. Moment of Inertia About an Arbitrary Line \(L\)

1. **Express the distance squared \(r^2(x,y,z)\) to \(L\).**  
   - If \(L\) is along a unit direction \(\mathbf u\) and passes through \(\mathbf a\), then  
     \(\displaystyle r^2 = |\mathbf r - \mathbf a|^2 - \bigl((\mathbf r - \mathbf a)\!\cdot\!\mathbf u\bigr)^2\).
2. **Set up the integral**  
   - \(\displaystyle I_L=\iint_S r^2\,\delta\,d\sigma\).
3. **Evaluate** using the same projection or parametric methods as above.

**Typical Cues:** “Moment of inertia about a line,” “distance to line,” “\(r^2\) factor.”

---

### 5. Integrating Over a Cube

1. **Break the cube into six faces** (each a planar surface).  
2. **Treat each face**: \(d\sigma = dA\); evaluate the integrand on that face.  
3. **Sum the six integrals**.

**Typical Cues:** “Cube surface,” “six faces,” “planar surfaces.”

---

## Common Pitfalls & Checks

| Pitfall | Why It Happens | Fix |
|---------|----------------|-----|
| **Using \(d\sigma = dA\) for non‑planar surfaces** | Forgetting the Jacobian factor | Always compute \(\dfrac{|\nabla f|}{|\nabla f\!\cdot\!\hat p|}\) |
| **Choosing a projection where \(|\nabla f\!\cdot\!\hat p|=0\)** | Surface tangent to projection plane → division by zero | Pick a plane where the normal has a non‑zero component |
| **Omitting absolute values** in \(|\nabla f\!\cdot\!\hat p|\) | Sign errors change the integral | Use absolute values in the denominator |
| **Wrong limits for \(R\)** | Misreading the projection bounds | Sketch \(R\) or solve for the variable explicitly |
| **Incorrect density placement** | Mixing up \(\delta\) with \(g\) | Remember \(\delta\) multiplies the surface element only for mass and inertia |
| **Forgetting to square distance for inertia** | Using \(r\) instead of \(r^2\) | Explicitly write \(r^2\) in the integrand |
| **Misidentifying the axis in moments of inertia** | Confusing \(x^2\) with \(y^2\) etc. | Verify the axis of rotation before writing the integrand |

---

## Quick Reference

- **Surface integral:**  
  \(\displaystyle \iint_S g\,d\sigma = \iint_R g\,\frac{|\nabla f|}{|\nabla f\!\cdot\!\hat p|}\,dA\)

- **Area:** replace \(g\) with \(1\).  
- **Mass:** replace \(g\) with \(\delta\).  
- **First moments:** \(g = x\delta,\; y\delta,\; z\delta\).  
- **Moments of inertia:** \(g = (y^2+z^2)\delta,\; (x^2+z^2)\delta,\; (x^2+y^2)\delta\).  
- **Inertia about line \(L\):** \(g = r^2\delta\).  
- **Center of mass:** \(\bar{x}=M_{yz}/M_S,\; \bar{y}=M_{xz}/M_S,\; \bar{z}=M_{xy}/M_S\).

With these formulas, concepts, and step‑by‑step strategies, you’re ready to tackle any surface‑integral problem on the exam.

---

## Raw Slide Summaries

### Slide 1

The image is a slide from a presentation on surface integrals, featuring a diagram and text.

*   **Title**: "Surface Integrals"
    *   The title is prominently displayed in large black font at the top left of the slide.
    *   It is centered and stands out against the white background.
*   **Trim Ch 14, 14.7, 14.8**
    *   Below the title, there is a yellow box with black text that reads "Trim Ch 14, 14.7, 14.8".
    *   This likely refers to the relevant chapters or sections in a textbook.
*   **Outline**
    *   The outline is presented in two main points:
        1.  Surface integrals of scalar functions
        2.  Surface Integrals Applications
    *   These points are listed below the title and yellow box, providing a clear structure for the content to be covered.
*   **Diagram**
    *   The diagram is a 3D graph with axes labeled x, y, and z.
    *   It features a curved surface S, a region R, and various mathematical notations and symbols.
    *   The diagram is annotated with handwritten notes, including equations and labels.
*   **Mathematical Notations and Symbols**
    *   The diagram includes several mathematical notations and symbols, such as:
        *   g(x,y,z)
        *   f(x,y,z) = C
        *   dσ
        *   ∫∫g(x,y,z)dσ
    *   These notations and symbols are used to represent the surface integral and its components.
*   **University of Waterloo Logo**
    *   The University of Waterloo logo is displayed in the bottom-left corner of the slide.
    *   The logo features a shield with a red lion and a banner with the university's name.

In summary, the image is a slide from a presentation on surface integrals, covering topics such as surface integrals of scalar functions and their applications. The diagram illustrates the concept of a surface integral, with various mathematical notations and symbols used to represent the different components involved.

### Slide 2

The image is a slide from a presentation on surface integrals, featuring a diagram and accompanying text. The title "Surface Integrals" is prominently displayed in large black font at the top of the slide.

**Main Points:**

*   **Title:** Surface Integrals
    *   The title is written in large black font.
*   **Text:**
    *   The text explains the concept of surface integrals, including the need to partition a surface into "surface area elements" and the formula for calculating the surface integral.
    *   The text is written in black font, with some equations and variables highlighted in red, blue, or green.
*   **Diagram:**
    *   The diagram illustrates the concept of surface integrals, showing a surface S with a grid pattern and a projection onto a region R.
    *   The diagram includes various labels and annotations, such as $\Delta \sigma_k$, $g(x,y,z)$, and $f(x,y,z) = C$.
    *   The diagram is drawn in black, blue, and green ink.
*   **University Logo:**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner of the slide.
    *   The logo features a shield with a red and yellow design, accompanied by the university's name in black font.

**Summary:**

The image is a slide from a presentation on surface integrals, explaining the concept and providing a diagram to illustrate the idea. The text and diagram work together to help students understand how to calculate surface integrals, and the University of Waterloo logo indicates that the presentation is likely from a course or lecture at the university.

### Slide 3

The image presents a detailed diagram illustrating the concept of surface integrals, specifically focusing on the magnified view of $\Delta \sigma_k$ and its planar projected area $\Delta A_k$. The diagram is accompanied by explanatory text and annotations that provide insight into the mathematical relationships between various components.

*   **Title and Subtitle**
    *   The title "Surface Integrals" is prominently displayed at the top.
    *   The subtitle "Magnified view of $\Delta \sigma_k$ and its planar projected area $\Delta A_k$" is written below the title.
*   **Diagram**
    *   The diagram features a blue curve labeled $\Delta \sigma_k$, which represents a surface element.
    *   A red parallelogram is drawn on the surface, with one corner labeled $T_k$ and another corner labeled $\Delta P_k$.
    *   The diagram also includes a green rectangle labeled $\Delta A_k$, which represents the planar projection of $\Delta \sigma_k$.
    *   Arrows are used to indicate the direction of the normal vector $\hat{p}$ and the tangent plane to the surface at $T_k$.
*   **Annotations**
    *   The annotation "At $T_k \rightarrow$ Parallelogram $\Delta P_k$ is the tangent plane to S" explains the relationship between the tangent plane and the surface.
    *   The equation $\Delta \sigma_k \approx \Delta P_k$ indicates that the surface element is approximately equal to the parallelogram.
    *   The text "Small partitions" suggests that the diagram is representing a small portion of the surface.
*   **University Logo**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner of the image.

In summary, the image provides a detailed illustration of the concept of surface integrals, highlighting the relationship between a surface element and its planar projection. The diagram and accompanying annotations offer a clear visual representation of the mathematical concepts involved.

### Slide 4

The image is a slide from a presentation on Surface Integrals, featuring a diagram and equations. The title "Surface Integrals" is prominently displayed at the top left, with a subtitle below it that reads, "To relate $\Delta P_k$ and $\Delta A_k$, let us bring $T_k$ and $C_k$ together and rotate the figure."

**Diagram:**

*   The diagram is a 3D representation of two parallelograms, $T_k, C_k$ and $\Delta P_k$, with various vectors and labels.
*   The parallelogram $T_k, C_k$ is green, while $\Delta P_k$ is red.
*   Vectors $\vec{v}_f$, $\hat{n}$, and $\hat{p}$ are drawn, along with the angle between $\hat{n}$ and $\hat{p}$, labeled as $\gamma_k$.
*   The diagram also includes labels for $\Delta A_k$ and $\Delta P_k$.

**Equations:**

*   Four equations are written to the right of the diagram:
    *   $\Delta A_k = \Delta P_k \cos \gamma_k$
    *   $\Delta P_k = \frac{1}{\cos \gamma_k} \Delta A_k$ (equation 1), with the condition $\cos \gamma_k \neq 0$
    *   $|\vec{v}_f \cdot \hat{p}| = |\vec{v}_f||\hat{p}|\cos \gamma_k$ (using dot product)
    *   $\cos \gamma_k = \frac{|\vec{v}_f \cdot \hat{p}|}{|\vec{v}_f|}$ (equation 2)

**Additional Elements:**

*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

The image presents a detailed explanation of surface integrals, including a diagram and relevant equations, likely from a mathematics or engineering course at the University of Waterloo.

### Slide 5

The image displays a slide from a presentation on surface integrals, featuring a white background with black text and blue handwriting. The title "Surface Integrals" is prominently displayed at the top left.

**Key Elements:**

* **Title:** "Surface Integrals" in bold black font
* **Equations and Formulas:**
	+ Derived from equations (1) and (2)
	+ $\Delta P_k = \frac{|\nabla f|}{|\nabla f \cdot \hat{p}|} \Delta A_k$
	+ $|\nabla f \cdot \hat{p}| \neq 0$
	+ In the limit, $\Delta P_k \approx \Delta \sigma_k \rightarrow d\sigma = dP = \frac{|\nabla f|}{|\nabla f \cdot \hat{p}|} dA$
* **Definition:** "The surface integral of $g(x,y,z)$ over S"
* **Surface Integral Formula:**
	+ $\iint_S g(x,y,z) d\sigma = \iint_R g(x,y,z) \frac{|\nabla f|}{|\nabla f \cdot \hat{p}|} dA$
* **Logo:** University of Waterloo logo in the bottom-right corner
* **Color Scheme:** White background, black text, blue handwriting, and red outline around a cloud-shaped text box

**Summary:**

The slide presents a detailed explanation of surface integrals, including the derivation of the formula and its application. The equations and formulas are written in blue handwriting, while the title and logo are in black font. The University of Waterloo logo is displayed in the bottom-right corner.

### Slide 6

The image presents a slide from a presentation on surface integrals, featuring a white background with black text and a yellow stripe at the top. The title "So far..." is prominently displayed in large black font at the top left of the slide.

**Main Content:**

* A paragraph of text explains that for a surface S given by f(x,y,z) = c, where f is a continuously differentiable function, the surface integral of the continuous function g(x,y,z) over S is represented by the double integral over R.
* Two mathematical equations are provided:
	+ The first equation defines the surface integral: ∫∫S g(x,y,z)dσ
	+ The second equation defines dσ: dσ = |∇f| / |∇f · p̂| dA
* A statement below the equations clarifies that p̂ is a unit vector normal to R and |∇f · p̂| ≠ 0.
* A blue subtitle at the bottom of the slide reads: "Surface integrals are very important for studying fluids across membranes."

**Footer:**

* The University of Waterloo logo is displayed in the bottom-right corner, accompanied by the university's name in black text.

Overall, the slide appears to be part of a lecture or presentation on surface integrals, likely in the context of a mathematics or physics course at the University of Waterloo.

### Slide 7

The image presents a slide from a presentation on calculus, specifically focusing on the integration of a function over the surface of a cube. The title "Question..." is prominently displayed at the top left, followed by the question: "What would happen if we want to integrate a function g(x,y,z) over the whole surface of the cube?"

**Key Elements:**

*   A 3D diagram of a cube is shown, with its sides labeled A to F.
*   The cube is positioned in a 3D coordinate system, with x, y, and z axes.
*   The function g(x,y,z) is written in red text next to the cube.
*   Three equations are presented in red text to the right of the cube, illustrating the process of integrating the function over the surface of the cube.

**Equations:**

1.  $\iint_{CUBE SURFACES} g(x,y,z) d\sigma = \iint_{SIDE A} g d\sigma +$
2.  $\iint_{SIDE B} + ... + \iint_{SIDE F}$

**Additional Information:**

*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

**Summary:**

The slide poses a question about integrating a function over the surface of a cube and provides a visual representation of the cube and the relevant equations. The equations demonstrate how to break down the integration process into smaller components, integrating over each side of the cube and summing the results.

### Slide 8

The image presents a slide from a presentation on the applications of surface integrals, specifically focusing on 3D thin shells. The title, "Applications of Surface Integrals - 3D Thin Shells," is prominently displayed at the top in bold black text.

**Key Points:**

* **Area of a Surface S**
	+ Formula: $A_S = \iint_S d\sigma$
	+ Description: The area of a surface $S$ given by $f(x,y,z) = c$
* **Mass of a Thin Shell**
	+ Formula: $M_S = \iint_S \delta(x,y,z) d\sigma$
	+ Description: The mass of a thin shell, where $\delta(x,y,z)$ represents the density at $(x,y,z)$ defined as mass per unit area
* **First Moments about Coordinate Planes**
	+ Formulas:
		- $M_{yz} = \iint_S x\delta(x,y,z)d\sigma$
		- $M_{xz} = \iint_S y\delta(x,y,z)d\sigma$
		- $M_{xy} = \iint_S z\delta(x,y,z)d\sigma$
	+ Description: The first moments about the coordinate planes

**Additional Information:**

* The University of Waterloo logo is displayed in the bottom-right corner, indicating the institution associated with the presentation.
* The background of the slide is white, providing a clean and neutral backdrop for the content.

Overall, the slide effectively conveys key concepts and formulas related to the applications of surface integrals in the context of 3D thin shells, making it a valuable resource for students and professionals in the field.

### Slide 9

The image presents a slide from the University of Waterloo, titled "Applications of Surface Integrals - 3D Thin Shells." This title is prominently displayed at the top in bold black text against a white background, with a yellow stripe separating it from the black header.

**Content:**

*   The slide is divided into three main sections, each numbered and dealing with a different application of surface integrals in the context of 3D thin shells.
*   **Section 4: Coordinates of Center of Mass**
    *   This section provides formulas for calculating the coordinates of the center of mass of a 3D thin shell.
    *   The formulas are given as:
        *   $\bar{x} = \frac{M_{yz}}{M_S}$
        *   $\bar{y} = \frac{M_{xz}}{M_S}$
        *   $\bar{z} = \frac{M_{xy}}{M_S}$
*   **Section 5: Moments of Inertia about Coordinate Axes**
    *   This section outlines the moments of inertia about the coordinate axes for a 3D thin shell.
    *   The formulas for the moments of inertia are:
        *   $I_x = \iint_S (y^2 + z^2) \delta(x,y,z) d\sigma$
        *   $I_y = \iint_S (x^2 + z^2) \delta(x,y,z) d\sigma$
        *   $I_z = \iint_S (x^2 + y^2) \delta(x,y,z) d\sigma$
*   **Section 6: Moment of Inertia about a Line L**
    *   This section discusses the moment of inertia about an arbitrary line $L$.
    *   The formula provided is:
        *   $I_L = \iint_S r^2(x,y,z) \delta(x,y,z) d\sigma$
    *   A note clarifies that $r(x,y,z)$ represents the distance from the point $(x,y,z)$ to line $L$.

**Additional Elements:**

*   In the bottom-right corner, the University of Waterloo's logo is displayed, featuring a shield with a red and yellow design, accompanied by the university's name in black text.

The slide effectively conveys complex mathematical concepts related to the applications of surface integrals in 3D thin shells, making it a valuable resource for students and professionals in the field of mathematics and engineering.

### Slide 10

The image is a slide from a presentation about surface integrals, featuring a title, three bullet points, and a logo.

*   **Title**
    *   The title of the slide is "Summary" in large black text.
    *   It is positioned at the top left corner of the slide.
*   **Bullet Points**
    *   There are three bullet points on the slide.
    *   The first bullet point reads: "Surface integrals of scalar fields allow us to integrate a function over a surface S in space."
    *   The second bullet point states: "They can be used to calculate surface area, mass, first moments, center of mass and moments of inertia of a 3D thin shell"
    *   The third bullet point says: "Surface integrals play a crucial role in understanding how fluids move across membranes"
    *   The bullet points are written in black text.
*   **Text Below Bullet Points**
    *   Below the bullet points, there is a sentence that reads: "In our next lecture, we will introduce surface integrals involving vector fields, where we will explore how these integrals help us model real-world phenomena like fluid flow!"
    *   This text is written in blue.
*   **Logo**
    *   At the bottom right corner of the slide, there is a logo for the University of Waterloo.
    *   The logo features a shield with a red and gold design, accompanied by the words "UNIVERSITY OF WATERLOO" in black text.

The slide provides a summary of the key points related to surface integrals, including their application to scalar fields, calculation of various physical quantities, and their role in understanding fluid movement. It also previews the next lecture, which will cover surface integrals involving vector fields and their application to modeling real-world phenomena.

