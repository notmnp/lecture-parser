# Lecture 33 - Surface Integrals Involving Vector Fields

## Study Notes

# Surface Integrals & Flux – Exam‑Ready Problem‑Solving Guide  

> **Core focus:** *What formulas to remember, why they’re useful, and how to apply them step‑by‑step.*

---

## Core Formulas & Definitions

| Formula | Meaning of symbols | When/why to use |
|---------|---------------------|-----------------|
| $$\iint_S g(x,y,z)\,d\sigma$$ | Scalar field \(g\); surface element \(d\sigma\). | Surface integral of a scalar field – e.g. surface area, mass, center of mass. |
| $$d\sigma = \left|\frac{\nabla f}{\nabla f\cdot \hat{p}}\right| dA = \frac{|\nabla f|}{|\nabla f\cdot\hat{p}|}\,dA$$ | \(f(x,y,z)=C\) is an implicit surface; \(\hat{p}\) is any unit vector (often \(\hat{k}\) or \(\hat{i}\)). | Convert a surface integral over an implicit surface to a double integral over its projection \(R\) in the \(xy\), \(xz\), or \(yz\) plane. |
| $$\iint_S \mathbf F\cdot \mathbf n\,d\sigma\;=\;\text{Flux of }\mathbf F\text{ through }S$$ | \(\mathbf F=(P,Q,R)\); \(\mathbf n\) is a unit normal. | Compute net flow of a vector field across a surface. |
| $$\mathbf n = \frac{\nabla f}{|\nabla f|}$$ | Normal to the level surface \(f(x,y,z)=C\). | Quickly find the outward normal for implicit surfaces. |
| $$d\sigma = |\mathbf r_u\times \mathbf r_v|\,du\,dv$$ | Parametrization \(\mathbf r(u,v)\). | Surface integrals for parametrically defined surfaces. |
| $$\iint_S \mathbf F\cdot \mathbf n\,d\sigma = \iint_R \mathbf F(\mathbf r(u,v))\cdot(\mathbf r_u\times \mathbf r_v)\,du\,dv$$ | Same as above but expressed in parametric form. | When the surface is given by a parametrization. |
| **Orientation** | *Positive* orientation → unit normal points *outward* of a closed region; *Negative* → inward. | Needed to decide the sign of flux. |
| **Non‑orientable surface** | No continuous choice of \(\mathbf n\). | Flux integrals are undefined; treat as a caution. |

---

## Key Concepts & Intuition

- **Surface element \(d\sigma\)**  
  *Area of an infinitesimal patch of the surface.*  
  • For a graph \(z=g(x,y)\): \(d\sigma=\sqrt{1+g_x^2+g_y^2}\,dA\).  
  • For an implicit surface \(f(x,y,z)=C\): use the gradient‑based formula above.  
  • For parametrizations: use the magnitude of the cross product of partials.

- **Normal vector \(\mathbf n\)**  
  • *Unit* and *perpendicular* to the surface.  
  • Determines the direction of the flow being counted in a flux integral.

- **Flux**  
  • \(\mathbf F\cdot\mathbf n\) is the *normal component* of the vector field.  
  • Integration over the surface gives the *net rate* at which the vector field crosses the surface.

- **Orientation**  
  • For closed surfaces, outward normals give *positive* flux.  
  • For open surfaces, choose a consistent normal field (e.g., upward or outward).  
  • The two possible normals on a smooth surface are continuous but opposite; pick one to define orientation.

- **Non‑orientable surfaces (e.g., Möbius strip)**  
  • No global continuous normal exists → flux integrals are not well‑defined.  
  • Important to check before setting up a flux integral.

---

## Problem‑Solving Strategies

| Problem Type | Typical Cues | Checklist / Steps |
|--------------|--------------|-------------------|
| **Compute surface area of a graph** | “Surface area of \(z=g(x,y)\) over region \(R\)” | 1. Write \(d\sigma=\sqrt{1+g_x^2+g_y^2}\,dA\). <br>2. Integrate \(\int\!\int_R \sqrt{1+g_x^2+g_y^2}\,dA\). |
| **Mass of a thin shell** | “Mass with density \(\rho(x,y,z)\)” | 1. Set up \(\iint_S \rho\,d\sigma\). <br>2. Convert \(d\sigma\) to \(dA\) or use parametrization. |
| **Flux through a parametrized surface** | “Flux of \(\mathbf F\) across the surface \(\mathbf r(u,v)\)” | 1. Compute \(\mathbf r_u\times \mathbf r_v\). <br>2. Take dot product \(\mathbf F(\mathbf r(u,v))\cdot(\mathbf r_u\times \mathbf r_v)\). <br>3. Integrate over the parameter domain. |
| **Flux through an implicit surface** | “Flux of \(\mathbf F\) through \(f(x,y,z)=C\)” | 1. Find \(\mathbf n=\nabla f/|\nabla f|\). <br>2. Compute \(\mathbf F\cdot \mathbf n\). <br>3. Use \(d\sigma = |\nabla f|/|\nabla f\cdot \hat{p}|\,dA\) to convert to a planar double integral. |
| **Flux across a closed surface** | “Outward flux through a sphere/torus” | 1. Confirm outward normal orientation. <br>2. If convenient, use divergence theorem: \(\iiint_V \nabla\cdot\mathbf F\,dV\). <br>3. Otherwise, set up surface integral directly. |
| **Check orientability** | “Is the surface Möbius? Non‑orientable?” | 1. Try to assign a continuous normal field. <br>2. If impossible, flux integral is undefined. |
| **Unit normal choice** | “Positive orientation” vs “Negative orientation” | 1. Identify the region the surface bounds. <br>2. Point normal outward → positive. <br>3. Point inward → negative. |

---

## Common Pitfalls & Checks

| Mistake | Why it’s bad | Quick fix |
|---------|--------------|-----------|
| **Wrong normal direction** | Flux sign flips, physical interpretation wrong. | Always double‑check orientation: for closed surfaces, outward normal is standard. |
| **Using \(\nabla f\) instead of \(\mathbf n\)** | Magnitude mis‑scaled → wrong flux. | Normalize: \(\mathbf n=\nabla f/|\nabla f|\). |
| **Ignoring Jacobian of parametrization** | Area element incorrect. | Verify \(|\mathbf r_u\times \mathbf r_v|\) is used. |
| **Confusing \(d\sigma\) with \(dA\)** | Integral over wrong domain. | Convert properly: \(d\sigma = \frac{|\nabla f|}{|\nabla f\cdot \hat{p}|}\,dA\) or \(|\mathbf r_u\times \mathbf r_v|\,du\,dv\). |
| **Assuming orientation on non‑orientable surfaces** | Flux integral is undefined. | Check for a continuous normal field before proceeding. |
| **Omitting the dot product** | Flux computed as scalar area instead of normal component. | Always compute \(\mathbf F\cdot \mathbf n\). |
| **Using wrong projection plane** | Wrong limits of integration. | Pick the plane orthogonal to \(\hat{p}\) that simplifies \(|\nabla f\cdot\hat{p}|\). |
| **Overlooking symmetry** | Extra work. | Look for even/odd integrands or cancellation. |

---

### Quick Reference Cheat Sheet

- **Flux**: \(\displaystyle \Phi = \iint_S \mathbf F\cdot \mathbf n\,d\sigma\)
- **Unit normal (implicit)**: \(\displaystyle \mathbf n=\frac{\nabla f}{|\nabla f|}\)
- **Surface element (param)**: \(\displaystyle d\sigma=|\mathbf r_u\times \mathbf r_v|\,du\,dv\)
- **Surface element (graph)**: \(\displaystyle d\sigma=\sqrt{1+g_x^2+g_y^2}\,dA\)
- **Orientation**: Outward → positive; Inward → negative for closed surfaces.

Use this guide as a quick roadmap when tackling any surface–integral or flux problem on the exam. Good luck!

---

## Raw Slide Summaries

### Slide 1

The image presents a lecture slide titled "Surface Integrals Involving Vector Functions" from the University of Waterloo. The slide is divided into several sections, each containing distinct information.

*   **Title and Reference**
    *   The title "Surface Integrals Involving Vector Functions" is prominently displayed at the top of the slide.
    *   Below the title, a yellow box contains the text "Trim Ch 14, 14.7, 14.8," likely referencing the relevant chapters or sections in a textbook.
*   **Outline**
    *   The outline section is presented in a list format with two main points:
        1.  The concept of flux
        2.  Surface integrals involving vector fields
*   **Diagram and Equations**
    *   A diagram illustrating the concept of surface integrals involving vector functions is shown on the right side of the slide.
    *   The diagram includes various mathematical symbols and notations, such as $\vec{F}$, $d\sigma$, $g(x,y,z)$, and $f(x,y,z)=C$.
    *   Two equations are written below the diagram:
        *   $\iint_S g(x,y,z) d\sigma = \iint_R g(x,y,z) \frac{|\nabla f|}{|\nabla f \cdot \hat{p}|} dA$
        *   $d\sigma = \frac{|\nabla f|}{|\nabla f \cdot \hat{p}|} dA$
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-left corner of the slide.

In summary, the slide provides an overview of surface integrals involving vector functions, including the concept of flux and the relevant mathematical equations. The diagram and equations presented on the slide help to illustrate the key concepts and provide a visual representation of the material.

### Slide 2

The slide is titled "Surface Integrals Involving Vector Fields" and contains the following content:

*   **Title and Subtitle**: 
    The title is "Surface Integrals Involving Vector Fields." Below the title, a sentence reads, "An important surface integral comes from looking at the magnitude of the component of a vector field $\vec{F} = P\hat{i} + Q\hat{j} + R\hat{j}$ going in the normal direction to a surface $S$."
*   **Text and Image**:
    The next line of text reads, "Let us look at this fishing net (surface $S$) submerged in water." Below this text, there is an image of a fishing net submerged in water. The image is annotated with red and blue markings, including:
    *   A red ellipse around the equation for $\vec{F}$, highlighting the components $P$, $Q$, and $R$. However, there is a mistake in the given equation, as it should be $R\hat{k}$ instead of $R\hat{j}$.
    *   The label "$S$" on the fishing net.
    *   A blue arrow labeled "$\hat{n}$" pointing outward from the net, indicating the normal direction.
    *   A red arrow labeled "$d\sigma$" pointing outward from the net, indicating the surface element.
    *   A red annotation around the edge of the net, likely indicating the surface $S$.
*   **Mathematical Expression**:
    Below the image, a mathematical expression is written in blue: $\iint_{S} \vec{F} \cdot \hat{n} d\sigma = \text{Flux of } \vec{F} \text{ through Surface } 'S'$. The expression is annotated to highlight that $\vec{F} \cdot \hat{n}$ represents the normal component of $\vec{F}$.
*   **Logo**:
    In the bottom-right corner of the slide, there is a logo for the University of Waterloo.

Overall, the slide appears to be introducing the concept of surface integrals involving vector fields, using the example of a fishing net submerged in water to illustrate the idea of flux through a surface.

### Slide 3

The image presents a white slide with black text and handwritten notes in blue and green, titled "Surface Integrals Involving Vector Fields." The title is centered at the top, accompanied by a yellow bar above it. Below the title, the subtitle "Physical Interpretation:" is displayed.

The slide features two thought bubbles containing the phrases "SOME FLUID" and "VELOCITY OF THE FLUID," respectively. The main content is organized into three sections:

**Left Section:**

* A blue handwritten note reads "SCALAR FUNCTION ρ(x,y,z)" with the subtext "MASS DENSITY" and the unit "[kg/m^3]"

**Center Section:**

* A blue handwritten equation: "v(x,y,z)" with the unit "[m/s]"
* A green handwritten equation: "F = ρv" with the subtext "MOMENTUM DENSITY"

**Right Section:**

* A green handwritten equation: "[kg/m^3] [m/s] [1] [m^2]" with the subtext "|F|"
* A green handwritten equation: "Kg/s"
* A green handwritten note: "AMOUNT OF MASS GOING OUT OF dσ IN THE DIR. OF n AT ANY GIVEN POINT IN TIME"

At the bottom of the slide, a green handwritten equation: "∫∫ F·n dσ" with the subtext "FLUX" and the unit "[m^2]". The University of Waterloo logo is displayed in the bottom-right corner.

The slide appears to be a lecture slide from a university course, likely used to explain the concept of surface integrals involving vector fields in the context of fluid dynamics.

### Slide 4

The image presents a slide from a presentation on surface integrals involving vector fields, featuring a diagram and mathematical equation. The title "Surface Integrals Involving Vector Fields" is displayed prominently at the top.

**Key Elements:**

* **Title:** "Surface Integrals Involving Vector Fields"
* **Diagram:**
	+ A 3D grid with a curved surface
	+ Arrows indicating the direction of the normal vector (n) and the vector field (F)
	+ Labels for the x, y, and z axes
* **Mathematical Equation:**
	+ Double integral of F · n dσ over the surface S
	+ Notation: F is a vector field, n is the unit normal vector, dσ is the surface element, and S is the surface
* **Text:**
	+ Explanation of the total flux across the fishing net in the direction of n
	+ Description of the process to solve a surface integral involving a vector field
* **Logo:**
	+ University of Waterloo logo in the bottom-right corner

**Summary:**

The slide effectively conveys the concept of surface integrals involving vector fields, using a combination of visual and mathematical representations. The diagram illustrates the orientation of the surface and the vector field, while the equation provides a concise formula for calculating the total flux. The text provides additional context and explanation, making the slide a useful resource for students and professionals in the field.

### Slide 5

The image presents a slide from a presentation on "Orientable Surfaces - Open Surface" at the University of Waterloo. The title is prominently displayed in large black text at the top, with a yellow bar separating it from the rest of the content.

Below the title, a diagram illustrates an open surface, accompanied by mathematical equations and annotations. The diagram features a purple outline of a curved surface, labeled "S", with a blue arrow pointing to it. The equation "f(x,y,z) = C" is written above the surface, while the notation "n1 = -n2" appears to the right. A purple arrow connects the equation to the surface, and a blue arrow points to the surface, indicating the normal vector "n1". Another blue arrow, labeled "n2", is shown pointing in the opposite direction.

The slide includes two bullet points below the diagram:

*   Every surface has two fields of unit normal vectors on "S" that vary continuously with position.
*   The set we choose will give the surface its orientation.

In the bottom-right corner, the University of Waterloo logo is displayed, featuring a red and gold shield with a black and white design. The logo is accompanied by the university's name in black text.

The background of the slide is white, providing a clean and clear visual representation of the information. Overall, the image effectively conveys complex mathematical concepts related to orientable surfaces in a concise and organized manner.

### Slide 6

The image is a lecture slide titled "Orientable Surfaces - Closed Surface" and features a diagram of a closed surface.

*   The title is in large black text at the top of the slide.
*   Below the title, there is a purple diagram of a closed surface with the following elements:
    *   A purple oval shape representing the closed surface.
    *   The letter "S" inside the oval.
    *   A blue arrow pointing outward from the surface, labeled as "n".
    *   Purple handwriting above the diagram that reads "Boundary of solid region" and "f(x,y,z) = C".
*   Below the diagram, there are two bullet points in gold text:
    *   **a. Positive Orientation:** Unit normal vectors point outward from the region.
    *   **b. Negative Orientation:** Unit normal vectors point toward the region.
*   In the bottom-right corner of the slide, there is a logo for the University of Waterloo, featuring a shield with a red and yellow design and the university's name in black text.

The slide appears to be discussing the concept of orientable surfaces and closed surfaces in mathematics, specifically in the context of vector calculus.

### Slide 7

The image presents a slide from a presentation on non-orientable surfaces, featuring two diagrams and accompanying text.

*   **Title**
    *   The title of the slide is "Example of Non - Orientable Surface" in black text.
*   **First Diagram**
    *   The first diagram is labeled "Figure 14.37a" and titled "Thin, rectangular strip of paper."
    *   It displays a simple rectangle with labeled corners: C at the top left, B at the top right, D at the bottom left, and A at the bottom right.
    *   The rectangle is outlined in blue.
*   **Second Diagram**
    *   The second diagram is labeled "Figure 14.37b" and titled "Example of a nonorientable surface."
    *   It illustrates a twisted strip with a single side, resembling a Möbius strip.
    *   The strip has labeled points: BD and AC, with an arrow pointing to the normal vector n at point P.
    *   The strip is shaded in gray.
*   **Copyright Information**
    *   The copyright information is displayed below the diagrams, stating "Copyright © 2008 Pearson Education Canada."
*   **Logo**
    *   In the bottom-right corner, the University of Waterloo logo is visible, accompanied by the university's name in black text.

The image effectively illustrates the concept of a non-orientable surface using a simple diagram, providing a clear visual representation for understanding this mathematical concept.

### Slide 8

The image is a slide from a presentation about surface integrals, featuring a title and five bullet points. The title, "Summary," is prominently displayed in large black text at the top left of the slide.

*   The first bullet point reads: "Surface integrals of scalar fields allow us to integrate a function over a surface S in space."
*   The second bullet point states: "They can be used to calculate surface area, mass, first moments, center of mass and moments of inertia of a 3D thin shell."
*   The third bullet point explains: "To define surface integrals of vector fields, we need to first rule out non-orientable surfaces."
*   The fourth bullet point provides the formula for the flux of a three-dimensional vector field across an oriented surface: "The flux of a three-dimensional vector field $\vec{F}$ across an oriented surface in the direction of $\hat{n}$ is given by Flux = $\iint_{S} \vec{F} \cdot \hat{n} d\sigma$."
*   The fifth bullet point elaborates on the concept of flux: "If $\vec{F}$ is the velocity field of a three-dimensional fluid flow, the flux of $\vec{F}$ across $S$ is the net rate at which fluid is crossing $S$ in the chosen positive direction."

The background of the slide is white, with a yellow stripe at the top. In the bottom-right corner, the University of Waterloo logo is displayed, accompanied by the text "UNIVERSITY OF WATERLOO" in black font.

