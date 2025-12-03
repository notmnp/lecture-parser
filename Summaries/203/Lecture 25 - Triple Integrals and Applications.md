# Lecture 25 - Triple Integrals and Applications

## Study Notes

# Triple Integrals – Problem‑Solving Exam Notes

---

## Core Formulas & Definitions

| Concept | Formula | Symbols | When to Use |
|---------|---------|---------|-------------|
| **Triple Integral** | \[
\iiint_D f(x,y,z)\,dV
\] | \(f\) – scalar integrand<br>\(D\) – 3‑D region<br>\(dV=dx\,dy\,dz\) (Cartesian) | General volume, mass, moment calculations |
| **Volume of a Solid** | \[
V(D)=\iiint_D 1\,dV
\] | 1 – unit integrand | When the solid is defined only by bounds |
| **Volume Between Two Surfaces** | \[
V=\iint_R\bigl(f_{\text{top}}(x,y)-f_{\text{bottom}}(x,y)\bigr)\,dA
\] | \(R\) – projection of \(D\) onto a coordinate plane | Compute \(V\) when \(f_{\text{top}},f_{\text{bottom}}\) are known |
| **Change of Variables (Jacobian)** | \[
\iiint_D f(x,y,z)\,dV = \iiint_{D'} f\bigl(g(u,v,w)\bigr)\,|J|\,du\,dv\,dw
\] | \(J=\partial(x,y,z)/\partial(u,v,w)\) | Simplify integrals or exploit symmetry |
| **Mass of a Solid** | \[
M=\iiint_D \delta(x,y,z)\,dV
\] | \(\delta\) – density | Variable density |
| **First Moments (for center of mass)** | \[
M_{yz}=\iiint_D x\,\delta\,dV,\;
M_{xz}=\iiint_D y\,\delta\,dV,\;
M_{xy}=\iiint_D z\,\delta\,dV
\] | \(M_{yz}\) – moment about \(yz\)-plane, etc. | Find centroid |
| **Center of Mass** | \[
\bar{x}=\frac{M_{yz}}{M},\quad
\bar{y}=\frac{M_{xz}}{M},\quad
\bar{z}=\frac{M_{xy}}{M}
\] | \(\bar{x},\bar{y},\bar{z}\) – centroid coordinates | |
| **Moments of Inertia** | \[
\begin{aligned}
I_x &= \iiint_D (y^2+z^2)\,\delta\,dV,\\
I_y &= \iiint_D (x^2+z^2)\,\delta\,dV,\\
I_z &= \iiint_D (x^2+y^2)\,\delta\,dV .
\end{aligned}
\] | \(I_x,I_y,I_z\) – inertia about coordinate axes | Rotational dynamics |
| **Integration Limits (Cartesian)** | \[
\iiint_D f\,dV=
\int_{x=a}^{b}
\int_{y=g_1(x)}^{g_2(x)}
\int_{z=f_1(x,y)}^{f_2(x,y)}
f(x,y,z)\,dz\,dy\,dx
\] | \(f_1,f_2\) – lower/upper \(z\)-surfaces; \(g_1,g_2\) – \(y\)-bounds; \(a,b\) – \(x\)-bounds | Any order of integration; choose convenient bounds |

---

## Key Concepts & Intuition

- **Projection & Fubini** – To determine bounds, sketch the 3‑D region and its shadow on a coordinate plane. For each \((x,y)\) in the projection, find where a vertical line (parallel to \(z\)) enters and leaves the solid.
- **Intersection Curve** – For solids bounded by two surfaces \(z=f_{\text{top}}\) and \(z=f_{\text{bottom}}\), set \(f_{\text{top}}=f_{\text{bottom}}\) to locate their curve of intersection; this projects to a 2‑D region \(R\).
- **Volume as Area × Height** – \(V=\iint_R (f_{\text{top}}-f_{\text{bottom}})\,dA\). The integrand is the vertical thickness at each \((x,y)\).
- **Elliptical Projection** – If \(R\) is an ellipse \(ax^2+by^2\le c\), a scaling transformation (e.g., \(u=x,\;v=\sqrt{b/a}\,y\)) turns it into a circle and introduces a Jacobian factor.
- **Symmetry** – Exploit symmetry to simplify limits or integrands (e.g., if \(D\) is symmetric about a plane, the centroid coordinate in that direction is zero).

---

## Problem‑Solving Strategies

### A. Volume Between Two Surfaces

1. **Identify surfaces** \(z=f_{\text{top}}\) and \(z=f_{\text{bottom}}\).
2. **Find intersection curve**:
   \[
   f_{\text{top}}(x,y)=f_{\text{bottom}}(x,y)\;\Rightarrow\; \text{equation of }R.
   \]
3. **Project onto a plane** (usually \(xy\)) to obtain \(R\).
4. **Set up the integral**:
   \[
   V=\iint_R \bigl(f_{\text{top}}-f_{\text{bottom}}\bigr)\,dA.
   \]
5. **Choose coordinates**:
   - If \(R\) is circular → polar.
   - If \(R\) is elliptical → scale to a circle (Jacobian \(\frac{1}{\sqrt{a/b}}\)).
6. **Integrate** stepwise; keep track of the Jacobian if a change of variables is used.
7. **Verify units**: result should be \(\text{length}^3\).

**Example – \(z=x^2+3y^2\) and \(z=8-x^2-y^2\)**

| Step | Detail |
|------|--------|
| 1 | \(f_{\text{top}}=8-x^2-y^2,\;f_{\text{bottom}}=x^2+3y^2\) |
| 2 | \(x^2+3y^2 = 8-x^2-y^2 \Rightarrow x^2+2y^2=4\) (ellipse) |
| 3 | Project \(R\): \(x^2+2y^2\le4\) |
| 4 | \(V=\iint_R\bigl(8-2x^2-4y^2\bigr)\,dA\) |
| 5 | Scale \(y=\frac{u}{\sqrt{2}}\) → Jacobian \(1/\sqrt{2}\). Ellipse becomes circle \(x^2+u^2\le4\). |
| 6 | Integral in polar: \(r\) from \(0\) to \(2\), \(\theta\) from \(0\) to \(2\pi\) |
   \[
   V=\frac{1}{\sqrt{2}}\int_0^{2\pi}\!\!\int_0^2\!\!\bigl(8-2r^2\bigr)\,r\,dr\,d\theta
   =\frac{1}{\sqrt{2}}\,(2\pi)\,8=8\pi\sqrt{2}.
   \] |
| 7 | Units: \(\text{m}^3\). |

---

### B. Mass, Center of Mass, Moments of Inertia

1. **Mass**: \(M=\iiint_D \delta\,dV\). If \(\delta\) is constant, reduce to \(V\).
2. **First Moments**: \(M_{yz}=\iiint_D x\delta\,dV\), etc. Use symmetry to set some moments to zero.
3. **Centroid**: \(\bar{x}=M_{yz}/M\), etc.
4. **Moments of Inertia**: pick axis, write integrand as squared perpendicular distance times \(\delta\).
5. **Integration Order**: choose the order that keeps bounds simple (often integrate \(z\) first when \(f_{\text{top}},f_{\text{bottom}}\) are simple).
6. **Check**: If \(\delta\) is constant, compare with formulas for uniform density solids.

---

### C. Setting Up Integration Limits (General Guidance)

| Variable | How to find bounds | Typical cues |
|----------|--------------------|--------------|
| \(z\) | Draw line parallel to \(z\) through \((x,y)\); enter/leave surfaces → \(z_{\min}(x,y), z_{\max}(x,y)\). | “Upper surface” / “lower surface”. |
| \(y\) | Draw line parallel to \(y\) through \((x)\) in the projection; bounds \(y_{\min}(x), y_{\max}(x)\). | “Projection onto \(xy\)-plane”. |
| \(x\) | Endpoints of projection; constants or functions of other variables. | “Outer limits of projection”. |
| Change of order | Swap the roles of \(x,y,z\) as needed; recompute bounds accordingly. | “Simplify bounds” or “Avoid messy integrals”. |

---

## Common Pitfalls & Checks

| Mistake | Why It Happens | Quick Check |
|---------|----------------|-------------|
| **Incorrect bounds** | Confusing the projection limits with actual limits | Sketch region; ensure inner bound ≤ outer bound |
| **Omitting density** | Forgetting \(\delta\) in mass or inertia integrals | Write integrand explicitly with \(\delta\) before integrating |
| **Wrong inertia distance** | Using a coordinate instead of perpendicular distance | Verify integrand: e.g., for \(I_x\) it must be \(y^2+z^2\) |
| **Wrong Jacobian** | Forgetting scaling factor after a variable change | Multiply by \(|J|\) after substitution |
| **Skipping symmetry** | Missing zero coordinates of centroid | Check if region is symmetric about a plane; set centroid coordinate to zero |
| **Unit mismatch** | Mixing length units | Dimensional analysis after integration |

---

## Quick Reference Checklist for Exams

1. **Read the problem carefully** – identify surfaces, density, axis of rotation.
2. **Sketch** the solid and its projection; label intersection curves.
3. **Determine intersection** by equating upper and lower surfaces.
4. **Choose coordinate system**:
   - Cartesian if bounds are simple.
   - Polar or elliptical scaling if region is circular/elliptical.
5. **Set up limits** in chosen order; write the integrand.
6. **Perform integrations** step by step; keep track of Jacobian if any.
7. **Compute physical quantities** (mass, centroid, inertia) using appropriate formulas.
8. **Verify**: correct units, bounds, and that the result is reasonable (e.g., positive, matches symmetry expectations).

With these concise formulas and strategies, you can tackle any typical triple‑integral problem on the exam. Good luck!

---

## Raw Slide Summaries

### Slide 1

The image is a slide from a presentation about triple integrals in rectangular coordinates, featuring a title, diagrams, and a photograph.

*   **Title and Reference**
    *   The title "Triple Integrals in Rectangular Coordinates" is prominently displayed at the top of the slide.
    *   Below the title, a yellow box contains the text "Trim Ch 13, S. 13.8, 13.9", which likely references the relevant sections in a textbook.
*   **Diagrams**
    *   Two diagrams are presented on the left side of the slide.
    *   The first diagram illustrates a single-variable function, f(x), plotted against x, with the area under the curve shaded. The integral of f(x) dx is written below it.
    *   The second diagram depicts a double integral, showing a surface defined by f(x,y) over a region R in the xy-plane. The double integral of f(x,y) dA is written below it, with the notation "dxdy or dydx" indicating the order of integration.
*   **Photograph**
    *   On the right side of the slide, a photograph shows a large, silver, cylindrical tank with pipes and valves attached to it.
    *   The tank appears to be made of metal and has a ladder leading up to the top.
    *   The background of the photograph suggests an industrial setting, possibly a factory or construction site.
*   **University Logo and URL**
    *   At the bottom-left corner of the slide, the logo for the University of Waterloo is displayed.
    *   Below the logo, the text "UNIVERSITY OF WATERLOO" is written in black font.
    *   In the bottom-right corner, a URL is provided: "https://www.kesarequipments.com/bitumen-heating-and-%20storage-tank.html".
*   **Background**
    *   The background of the slide is white, providing a clean and neutral backdrop for the content.

In summary, the slide effectively conveys information about triple integrals in rectangular coordinates through a combination of diagrams, a photograph, and relevant references. The use of visual aids and clear labeling makes the content more engaging and easier to understand.

### Slide 2

The image is a slide from a presentation on triple integrals in rectangular coordinates, featuring a diagram and mathematical equations. The title "Triple Integrals in Rectangular Coordinates" is prominently displayed at the top.

*   **Title and Subtitle**
    *   The title is centered at the top of the slide.
    *   Below the title, the subtitle reads: "For a function f(x,y,z) defined over a three-dimensional region D,".
*   **Diagram**
    *   A diagram is drawn on the left side of the slide, illustrating a 3D region D with axes labeled x, y, and z.
    *   The region D is represented by a black outline, with various points and vectors marked inside it.
    *   Blue arrows are used to label the axes, while red text and symbols are used to annotate the diagram.
*   **Mathematical Equations**
    *   To the right of the diagram, several mathematical equations are written in red and blue.
    *   The equations appear to be related to the definition of a triple integral and its application to the region D.
    *   The equations include symbols such as ΔVk, Δxk, Δyk, Δzk, and f(xk,yk,zk).
*   **Text Below the Diagram**
    *   Below the diagram, a paragraph of text explains that these integrals are mainly used when the solid over which we will be integrating has no particular symmetry about any of the coordinate axes.
*   **University Logo**
    *   In the bottom-right corner of the slide, the logo for the University of Waterloo is displayed.

The slide provides a clear and concise overview of triple integrals in rectangular coordinates, including a visual representation of the concept and relevant mathematical equations.

### Slide 3

The image presents a slide from a presentation on the topic of "Applications of Triple Integrals." The content is organized as follows:

**Title and Reference**
* The title "Applications of Triple Integrals" is prominently displayed in large, bold, black font at the center-left of the slide.
* Below the title, in smaller gray font, is the reference "Ch.13, S. 13.10," indicating the chapter and section in a textbook or resource.

**University Logo and Name**
* In the bottom-right corner, the logo and name of the "UNIVERSITY OF WATERLOO" are displayed.
* The logo features a shield with a red and yellow design, accompanied by a black and white chevron.

**Background and Design**
* The background of the slide is white, providing a clean and neutral backdrop for the content.
* A horizontal bar at the top of the slide features a gradient that transitions from black to yellow, adding a touch of color and visual interest.

Overall, the slide appears to be the title slide for a presentation on the applications of triple integrals, likely used in a university course or lecture.

### Slide 4

The image presents a slide from a presentation on the topic of "Volume of a Solid" in the context of calculus, specifically focusing on triple integrals. The slide is divided into several sections, each containing key information and visual aids to illustrate the concept.

*   **Title and Introduction**
    *   The title "Volume of a Solid" is prominently displayed at the top.
    *   A brief introduction follows, stating, "Similar that what we saw before for Double Integrals applications..." and explaining that if a function $f(x,y,z)$ is defined over a region $D$ and equals 1, it can be used to define the volume of the solid region $D$.
*   **Mathematical Formulation**
    *   The volume $V$ of the solid region $D$ is given by the triple integral $\iiint_{D} dV$.
    *   This formula is central to understanding how to calculate volumes using triple integrals.
*   **Visual Representation**
    *   A 3D graph illustrates a solid region $D$, which is a rectangular prism with dimensions 2x2x2.
    *   The graph is labeled with axes (x, y, z) and includes a function $f(x,y,z) = 1$ defined over $D$.
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner, indicating the academic institution associated with the presentation.

In summary, the slide effectively communicates the concept of calculating the volume of a solid using triple integrals, providing both a mathematical formulation and a visual representation to aid understanding.

### Slide 5

The image presents a slide from a lecture on the average value of a function f(x,y,z) in three-dimensional space, featuring a diagram and mathematical equations.

*   The title "Average Value of a Function f(x,y,z)" is prominently displayed at the top of the slide.
    *   The title is written in bold black font.
    *   It provides the main topic of discussion for the slide.
*   A definition and equation for the average value of a function f(x,y,z) over a region D in space are provided below the title.
    *   The definition states that the average value is defined as the triple integral of f(x,y,z)dV divided by the triple integral of dV over the region D.
    *   The equation is presented as: A_D = (∫∫∫_D f(x,y,z)dV) / (∫∫∫_D dV)
    *   This equation is used to calculate the average value of a function over a given region.
*   A 3D diagram illustrating a solid region D is shown on the left side of the slide.
    *   The diagram depicts a rectangular prism with dimensions labeled on its edges.
    *   The x, y, and z axes are labeled, indicating the orientation of the prism in 3D space.
    *   The diagram is used to visualize the concept of a solid region D.
*   Additional text on the right side of the slide explains the practical application of the average value of a function.
    *   It is mentioned that if T(x,y,z) represents the temperature at a point (x,y,z) within the solid region D, then the average value of T(x,y,z) over D gives the average temperature of the solid D.
    *   This provides a real-world context for understanding the concept of average value.
*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.
    *   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.
    *   The logo indicates that the slide is from a lecture or presentation affiliated with the University of Waterloo.

In summary, the slide effectively conveys the concept of the average value of a function f(x,y,z) over a region D in 3D space, providing both a mathematical definition and a practical example related to temperature distribution within a solid region.

### Slide 6

The image presents a slide from a presentation on the topic of "Mass, Moments and Center of Mass of Solid Objects in Space." The slide is divided into three main sections: the title, the content, and the diagram.

**Title Section**

* The title is prominently displayed at the top of the slide in large black text.
* It reads: "Mass, Moments and Center of Mass of Solid Objects in Space."

**Content Section**

* The content section is located below the title and consists of several paragraphs of text.
* The first paragraph defines the density function δ(x,y,z) as the density of an object occupying a region D in space, measured in units of mass per unit volume.
* The second paragraph introduces the concept of mass, denoted by M, which is calculated using the triple integral of the density function over the region D.
* The third paragraph discusses the first moments about the three coordinate planes x, y, and z, respectively, and provides formulas for calculating these moments.
* The fourth paragraph explains how to find the coordinates of the center of mass of the object using the formulas provided.

**Diagram Section**

* The diagram is situated on the right-hand side of the slide and illustrates a 3D object with a green surface.
* The object is labeled as "D" and has a small cube inside it, representing a small volume element.
* The diagram also includes labels for the x, y, and z axes, as well as an arrow pointing to the cube with the label "Δm_k = δ(x_k,y_k,z_k) ΔV_k."
* In the bottom-right corner of the slide, there is a logo for the University of Waterloo.

**Formulas and Equations**

* The slide includes several formulas and equations related to the topic, including:
	+ M = ∫∫∫_D δ(x,y,z)dV
	+ M_yz = ∫∫∫_D xδ(x,y,z)dV
	+ M_xz = ∫∫∫_D yδ(x,y,z)dV
	+ M_xy = ∫∫∫_D zδ(x,y,z)dV
	+ x̄ = M_yz / M
	+ ȳ = M_xz / M
	+ z̄ = M_xy / M

Overall, the slide provides a clear and concise overview of the concepts related to the mass, moments, and center of mass of solid objects in space.

### Slide 7

The image displays a slide from a presentation about the moments of inertia of solid objects in space. The title, "Moments of Inertia of Solid objects in Space," is prominently displayed at the top.

*   **Title and Subtitle**
    *   The title is written in large black text.
    *   The subtitle, "The moments of inertia (second moments) about the coordinate axes:", is written in smaller red and black text below the title.
*   **Equations for Moments of Inertia**
    *   Three equations are presented to calculate the moments of inertia about the x, y, and z axes.
        *   $I_x = \iiint (y^2 + z^2)\delta(x,yz)dV$
        *   $I_y = \iiint (x^2 + z^2)\delta(x,yz)dV$
        *   $I_z = \iiint (x^2 + y^2)\delta(x,yz)dV$
*   **Moments of Inertia about a Line L**
    *   A section titled "Moments of Inertia about a line L:" is displayed.
    *   An equation is provided to calculate the moment of inertia about a line L.
        *   $I_L = \iiint r^2(x,y,z)\delta(x,y,z)dV$
    *   A note clarifies that $r(x,y,z)$ represents the distance from the point $(x,y,z)$ to the line L.
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner.

In summary, the image presents a concise overview of the moments of inertia of solid objects in space, including equations for calculating the moments of inertia about the coordinate axes and a line L, along with a clarification on the distance $r(x,y,z)$.

### Slide 8

The slide is titled "Triple Integrals in Cartesian Coordinates - Finding Limits of Integration." Below the title, there is a diagram of a 3D region D, bounded by two surfaces z = f1(x,y) and z = f2(x,y), with a projection onto the xy-plane labeled R. The diagram includes labels for the x, y, and z axes.

**Key Components of the Diagram:**

*   The region D is a 3D shape with a curved top and bottom.
*   The top surface is labeled "z = f2(x,y)" and the bottom surface is labeled "z = f1(x,y)".
*   A vertical line is drawn through the region, entering at z = f1(x,y) and leaving at z = f2(x,y).
*   The projection of the region onto the xy-plane is labeled R, with boundaries y = g1(x) and y = g2(x).
*   The limits of integration for y are from g1(x) to g2(x).

**Equations and Formulas:**

*   The equation for the triple integral is given as I = ∫∫∫D f(x,y,z) dV.
*   The integral is written in Cartesian coordinates as ∫∫R ∫f1(x,y)f2(x,y) f(x,y,z) dz dy dx.

**Text and Notations:**

*   The text "We want to evaluate, six possibilities" is written next to the equation for the triple integral.
*   The notation "∫∫R ∫f1(x,y)f2(x,y) f(x,y,z) dz dy dx" is shown, indicating one of the possible orders of integration.
*   The University of Waterloo logo is displayed in the bottom-right corner.

**Overall Content:**

The slide provides a visual representation of a 3D region and its projection onto the xy-plane, along with the corresponding triple integral and its limits of integration. The diagram and equations illustrate how to evaluate a triple integral in Cartesian coordinates.

### Slide 9

The slide displays the following content:

**Title:** 
* "Triple Integrals in Cartesian Coordinates - Finding Limits of Integration" in black text.

**Main Equation:**
* A triple integral equation is written in green, red, and blue text:
  * $I = \int_{x=a}^{x=b} \int_{y=g_1(x)}^{y=g_2(x)} \int_{z=f_1(x,y)}^{z=f_2(x,y)} f(x,y,z) \, dz \, dy \, dx$

**Color Breakdown of the Equation:**
* Green: integral signs, $f(x,y,z)$, $dz$, $dy$, $dx$, and the variable of integration limits ($x$, $y$, $z$)
* Red: $y=g_2(x)$ and $y=g_1(x)$
* Blue: $z=f_2(x,y)$ and $z=f_1(x,y)$
* Black: $x=a$ and $x=b$

**Logo and Institution:**
* The University of Waterloo logo is displayed in the bottom-right corner, featuring a shield with a yellow background and red designs. The logo is accompanied by the text "UNIVERSITY OF WATERLOO" in black.

**Background and Design Elements:**
* The background of the slide is white.
* A yellow stripe is visible at the top, followed by a black stripe.

### Slide 10

The image presents a slide from a lecture on "Finding Limits of Integration: A 3D Version of Fubini's Theorem." The slide is divided into four main bullet points, each with a sublist that provides further explanation.

*   **SKETCH**
    *   Sketch D and its vertical projection in the x-y plane R, called "shadow". 
    *   Label upper and lower bound surfaces of D and the upper and lower bounding curves of R.
*   **Find the z-limits of integration**
    *   Draw a line M passing through a typical point (x,y) in R, and parallel to the z-axis. 
    *   As z increases, M enters D at z = f1(x,y) and leaves at z = f2(x,y).
*   **Find the y-limits of integration**
    *   Draw a line L through (x,y) parallel to the y-axis. 
    *   In this case, as y increases, L enters at y = g1(x) and leaves at y = g2(x).
*   **Find the x-limits of integration**
    *   Sweep the line L in a way to include all lines through R parallel to the y-axis from x = a to x = b in our figure.

The slide provides a step-by-step guide to finding the limits of integration for a 3D region using Fubini's Theorem. It emphasizes the importance of sketching the region and its projection onto the x-y plane, labeling the upper and lower bound surfaces, and determining the limits of integration for each variable. The slide is from the University of Waterloo, as indicated by the logo in the bottom-right corner.

### Slide 11

The image presents a mathematical problem related to the calculation of a triple integral, specifically finding the volume of a region enclosed by two surfaces. The problem is titled "Problem - Calculation of a Triple Integral" and is accompanied by a diagram illustrating the region.

Here are the key elements of the image:

* **Title**: 
	+ Text: "Problem - Calculation of a Triple Integral"
	+ Font: Black, bold
* **Problem Statement**:
	+ Text: "Find the volume of the region D enclosed by the surfaces z = x^2 + 3y^2 and z = 8 - x^2 - y^2."
	+ Font: Black
* **Step 1: Sketch**:
	+ Diagram: A 3D graph showing the two surfaces and their intersection
	+ Labels:
		- "z = x^2 + 3y^2"
		- "z = 8 - x^2 - y^2"
		- "D" (region enclosed by the surfaces)
	+ Arrows:
		- Blue arrow pointing to the surface "z = x^2 + 3y^2"
		- Red arrow pointing to the surface "z = 8 - x^2 - y^2"
* **Equations and Formulas**:
	+ "dV = dzdydx" (written in red)
	+ "x^2 + 2y^2 = 4" (written in green)
	+ "y = ±√((4-x^2)/2)" (written in green)
	+ "y = -√((4-x^2)/2)" (written in green)
* **University Logo**:
	+ Logo: University of Waterloo
	+ Location: Bottom-right corner of the image

In summary, the image presents a mathematical problem involving the calculation of a triple integral to find the volume of a region enclosed by two surfaces. The diagram illustrates the region and the surfaces, while the equations and formulas provide the necessary information to solve the problem. The University of Waterloo logo is displayed in the bottom-right corner, indicating the institution associated with the content.

### Slide 12

The image presents a slide from a lecture on the calculation of a triple integral, featuring a step-by-step solution to a problem. The slide is divided into two main sections: "Step 2" and "Step 3," which are part of a larger problem-solving process.

**Step 2: Determine the Intersection of the Two Surfaces (Labels)**

*   The two surfaces are defined by the equations:
    *   $z = x^2 + 3y^2$
    *   $z = 8 - x^2 - y^2$
*   To find their intersection, we equate the two expressions for $z$:
    *   $x^2 + 3y^2 = 8 - x^2 - y^2$
*   Simplifying the equation yields:
    *   $2x^2 + 4y^2 = 8$
    *   $\downarrow$
    *   $x^2 + 2y^2 = 4$
*   The resulting equation represents an ellipse.

**Step 3: Setup the Integral (Determine the Limits of Integration)**

*   The triple integral is set up as:
    *   $\int_{-2}^{2} \int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}} \int_{x^2+3y^2}^{8-x^2-y^2} dz\,dy\,dx$
*   The limits of integration are determined by the intersection of the two surfaces and the region bounded by the ellipse.

The slide is presented by the University of Waterloo, as indicated by the logo in the bottom-right corner.

### Slide 13

The image presents a slide from a lecture on the calculation of a triple integral, titled "Problem - Calculation of a Triple Integral" in large black text at the top. The slide is divided into two sections: the title and the content.

**Title Section**

* The title is centered and written in large black text.
* A yellow bar runs along the top edge of the slide, with a thick black border above it.

**Content Section**

* **Step 4: Solve the Integral**
	+ The step is written in smaller black text below the title.
	+ A series of mathematical equations are presented in blue handwriting-style text, detailing the solution to the integral.
	+ The equations involve various mathematical operations, including integration, substitution, and simplification.
	+ The final equation is incomplete, indicating that the solution is ongoing.
* **University of Waterloo Logo**
	+ Located in the bottom-right corner of the slide.
	+ Features a red and gold shield with a black design, accompanied by the university's name in black text.

The slide provides a clear and concise visual representation of the problem and its solution, making it an effective tool for teaching and learning.

### Slide 14

The slide is titled "Problem - Calculation of a Triple Integral" in large, bold, black font at the top.

Below the title, there are two lines of mathematical expressions written in blue and red digital handwriting. The first line is:

V = ∫ from -2 to 2 (4 - x^2)^(3/2) dx

Below this, the substitution is written in red:

x = 2sin(u)

The next part of the solution is indicated by three red dots, followed by the final answer:

V = 8π√2

The final answer is underlined twice.

In the bottom-right corner, the University of Waterloo logo is displayed, featuring a shield with a red and gold design. The text "UNIVERSITY OF WATERLOO" appears next to the logo in black font.

The slide's background is white, with a thick black bar at the top and a thin gold stripe below it.

### Slide 15

The image presents a slide from a presentation on triple integrals in rectangular coordinates, featuring the title "Summary" at the top left. The slide is divided into two main sections: the first provides an overview of when to use triple integrals in rectangular coordinates, while the second outlines the steps to solve a triple integral problem.

**Main Points:**

*   **Triple Integrals in Rectangular Coordinates**
    *   Used when the solid over which we are integrating has no particular symmetry about any of the coordinate axes.
*   **Steps to Solve a Triple Integral Problem**
    *   Sketch
    *   Decide on the order of integration
    *   Determine the limits of integration
    *   Solve the integral

**Summary:**

The slide provides a concise summary of when to use triple integrals in rectangular coordinates and the steps involved in solving such problems. It emphasizes the importance of sketching the region, deciding on the order of integration, determining the limits of integration, and solving the integral. The slide is part of a larger presentation, likely from the University of Waterloo, as indicated by the logo in the bottom-right corner.

### Slide 16

The image is a slide from a presentation, likely a concluding slide, featuring the University of Waterloo's logo and a message of appreciation.

*   The top border of the slide is black with a yellow stripe underneath.
    *   The black and yellow stripes are horizontal and span the entire width of the slide.
    *   The black stripe is at the top, and the yellow stripe is below it.
*   The University of Waterloo logo is on the left side of the slide.
    *   The logo is a shield with a yellow background and red lions on either side.
    *   A black chevron is in the middle of the shield, pointing upwards.
    *   To the right of the logo, "UNIVERSITY OF WATERLOO" is written in bold black text.
*   Below the logo and university name, "Thank you" is written in bold black text.
    *   The text is centered on the slide.
    *   It is likely the final slide in a presentation, serving as a conclusion or expression of gratitude.

The slide effectively conveys a sense of appreciation and affiliation with the University of Waterloo.

