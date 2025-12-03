# Lecture 27 - Triple Integrals Spherical Coordinates

## Study Notes

# Problem‑Solving Notes – Triple Integrals  
*(spherical + cylindrical coordinates)*  

---

## Core Formulas & Definitions  

| Symbol | Meaning | LaTeX | Typical Use |
|--------|---------|-------|-------------|
| $\rho$ | Distance from the origin | $\rho$ | All spherical expressions |
| $\theta$ | Azimuthal angle in the $xy$‑plane | $\theta$ | Rotational symmetry about $z$–axis |
| $\phi$ | Polar angle from the positive $z$‑axis | $\phi$ | Inclination from $z$–axis |
| $r$ | Cylindrical radial coordinate | $r$ | All cylindrical expressions |
| $x,y,z$ | Cartesian coordinates | $x,y,z$ | Standard 3‑D problems |
| $dV$ | Volume element | $\begin{cases}\rho^{2}\sin\phi\,d\rho\,d\phi\,d\theta\\[4pt]r\,dr\,d\theta\,dz\end{cases}$ | Change to spherical or cylindrical |
| $f$ | Scalar field (e.g., density) | $f$ | Integrand |
| $V=\iiint_{D} f\,dV$ | Triple integral over region $D$ | $V=\iiint_{D}f\,dV$ | Volume, mass, etc. |
| **Surface equations** | | | |
| Sphere | $x^{2}+y^{2}+z^{2}=R^{2}$ | $\rho=R$ | $r^{2}+z^{2}=R^{2}$ |
| Cone | $z^{2}=k(x^{2}+y^{2})$ | $\tan\phi=\sqrt{k}\;\Rightarrow\;\phi=\arctan\sqrt{k}$ | $z=\pm r/\sqrt{k}$ |
| Paraboloid | $z=a x^{2}+b y^{2}$ | $z=\rho\cos\phi=a\rho^{2}\sin^{2}\phi\cos^{2}\theta+b\rho^{2}\sin^{2}\phi\sin^{2}\theta$ | $z=a r^{2}\cos^{2}\theta+b r^{2}\sin^{2}\theta$ |
| Inverted paraboloid | $z=8-(x^{2}+y^{2})$ | $z=8-\rho^{2}\sin^{2}\phi$ | $z=8-r^{2}$ |

---

## Key Concepts & Intuition  

- **Coordinate‑system choice**  
  - *Rectangular*: use when no obvious symmetry.  
  - *Cylindrical*: best for rotation about the $z$–axis.  
  - *Spherical*: best for symmetry about a point.  
- **Jacobian**  
  - $\rho^{2}\sin\phi$ (spherical) or $r$ (cylindrical).  
  - Always multiply the integrand by the Jacobian.  
- **Projection method**  
  1. Sketch the region and its projection onto the $xy$‑plane.  
  2. Determine bounds in that plane.  
  3. “Lift” the bounds using the surface equations.  
- **Symmetry tricks**  
  - Full rotation → $\theta:0\to2\pi$; half/quarter → adjust.  
  - Even/odd integrands in $\theta$ or $\phi$ can reduce integrals to zero or halve the effort.  
- **Different orders of integration**  
  - Any permutation of $d\rho\,d\phi\,d\theta$ or $dr\,d\theta\,dz$ is valid; choose the one that simplifies limits.  
- **Six combinations of volume differentials**  
  - $d\rho\,d\phi\,d\theta,\; d\rho\,d\theta\,d\phi,\; d\phi\,d\rho\,d\theta,\ldots$  
  - Useful when a particular order yields constant limits.

---

## Problem‑Solving Strategies  

| Problem Type | Cues | Typical Setup | Step‑by‑Step Checklist | Common Mistakes |
|--------------|------|---------------|------------------------|-----------------|
| **Volume inside a surface** | “Volume of …” | $\displaystyle V=\iiint_{D}1\,dV$ | 1. Identify symmetry → choose coordinates.<br>2. Convert surface equations.<br>3. Determine bounds for each variable.<br>4. Include Jacobian.<br>5. Evaluate. | Forgetting Jacobian; wrong $\phi$ limits. |
| **Mass or center of mass** | “Mass of …” or “center of mass” | $\displaystyle M=\iiint_{D}\rho\,dV,\;\bar{x}=\frac{1}{M}\iiint_{D}x\rho\,dV$ | Same as volume, but integrand includes density. | Mixing up density function and $z$ limits. |
| **Intersection of surfaces** | “bounded by …” | Find intersection curve → solve for radial/angle limits. | 1. Solve $z$ surfaces for $x,y$ intersection.<br>2. Express intersection in chosen coordinates.<br>3. Set inner/outer limits accordingly. | Missing inner surface or using wrong sign for $z$ bounds. |
| **Symmetric region about an axis** | “cylindrical symmetry” | $\theta$ limits 0→$2\pi$; $r$ from 0 to $f(\theta)$ | Use symmetry to simplify $\theta$ integration. | Over‑restricting $\theta$ when symmetry is full. |
| **Region with angular restriction** | “between planes $y=0$ and $y=x$” | Adjust $\theta$ limits accordingly (e.g., $0\le\theta\le\pi/4$). | Convert inequalities to angles. | Forgetting to convert to proper angle bounds. |
| **Change of order** | “simplify evaluation” | Pick order that yields constant limits. | Test each variable order before integration. | Choosing an order that gives variable limits inside integrals. |

### Example: Volume Inside a Unit Sphere Above the $xy$–Plane, Cut by a Cone  

1. **Surface conversion**  
   - Sphere: $\rho=1$  
   - Cone: $\tan\phi=\sqrt{3}\;\Rightarrow\;\phi=\pi/3$  
2. **Bounds**  
   - $\rho:0\to1$  
   - $\phi:0\to\pi/3$ (above cone)  
   - $\theta:0\to2\pi$ (full rotation)  
3. **Integral**  
   $$
   V=\int_{0}^{2\pi}\!\int_{0}^{\pi/3}\!\int_{0}^{1}\rho^{2}\sin\phi\,d\rho\,d\phi\,d\theta
   $$
4. **Evaluation** – compute inner integrals first; result $V=\pi/3$.

---

## Common Pitfalls & Quick Checks  

| Pitfall | Check |
|---------|-------|
| **Missing Jacobian** | Did the integrand contain $\rho^{2}\sin\phi$ or $r$? |
| **Wrong angle orientation** | $\phi$ measured from +$z$; $\theta$ around $z$ in the $xy$‑plane. |
| **Improper limits** | Sketch region; confirm lower limit ≤ upper limit for every variable. |
| **Sign errors in $z$ bounds** | Lower surface must be the smaller $z$‑value at each $(r,\theta)$. |
| **Symmetry misuse** | Verify integrand is even/odd before simplifying. |
| **Differential order confusion** | Any permutation of differentials is allowed; choose the one with simplest limits. |
| **Unit mismatch** | When converting $z$ to spherical: $z=\rho\cos\phi$; converting $r$ to spherical: $r=\rho\sin\phi$. |

---

## Quick Reference Cheat‑Sheet  

```latex
% Spherical coordinates
(x,y,z) = (\rho\sin\phi\cos\theta,\;\rho\sin\phi\sin\theta,\;\rho\cos\phi)
\quad dV = \rho^{2}\sin\phi\,d\rho\,d\phi\,d\theta
```

```latex
% Cylindrical coordinates
(x,y,z) = (r\cos\theta,\;r\sin\theta,\;z)
\quad dV = r\,dr\,d\theta\,dz
```

```latex
% Volume of ice‑cream cone (sphere & cone)
V = \int_{0}^{2\pi}\int_{0}^{\pi/3}\int_{0}^{1}\rho^{2}\sin\phi\,d\rho\,d\phi\,d\theta
  = \frac{\pi}{3}
```

```latex
% Volume between paraboloids (cylindrical)
V = \int_{0}^{2\pi}\int_{0}^{\frac{2}{\sqrt{1+\sin^{2}\theta}}}
      \int_{r^{2}(1+2\sin^{2}\theta)}^{\,8-r^{2}}
      r\,dz\,dr\,d\theta
```

---

**Quick tip:**  
Always start with **geometry → bounds → Jacobian → integration**.  
If the algebra looks messy, try a different coordinate system or a different order of integration.  
Keep this checklist handy while you solve practice problems. Happy integrating!

---

## Raw Slide Summaries

### Slide 1

The image presents a lecture slide on Spherical Coordinates, featuring a title, a diagram, and an image of a robot. The content is organized as follows:

*   **Title and Reference**
    *   The title "Spherical Coordinates" is prominently displayed in large black text at the top center of the slide.
    *   Below the title, a yellow rectangle contains the reference "Trim Ch 13, S. 13.12" in black text.
*   **Diagram and Mathematical Expression**
    *   A hand-drawn diagram is situated to the left of the slide, illustrating a 3D coordinate system with axes labeled x, y, and z.
    *   The diagram includes a curved surface and a vector pointing upwards along the z-axis.
    *   Below the diagram, a mathematical expression is written: "I = ∭ f(x,y,z) dV".
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-left corner of the slide, featuring a shield with a red and gold design, accompanied by the university's name in black text.
*   **Image of BB-8**
    *   An image of the Star Wars character BB-8 is shown on the right side of the slide, depicting the droid in a futuristic setting.
    *   The image is sourced from the URL "https://www.starwars.com/databank/bb-8", which is provided below the image.
*   **Background and Design Elements**
    *   The slide's background is white, with a black and yellow bar at the top.

In summary, the slide provides a concise introduction to spherical coordinates, referencing a specific section in a textbook, and features a diagram illustrating the concept, along with a mathematical expression. The University of Waterloo logo is displayed, and an image of BB-8 is included, likely as a visual aid or thematic element.

### Slide 2

The image is a slide from a presentation on triple integrals in spherical coordinates, featuring a diagram and accompanying text.

**Title**
The title of the slide is "Triple Integrals in Spherical Coordinates" in bold black font at the top.

**Text**
Below the title, a paragraph explains that when problems are symmetric about a point or have spherical symmetry, it is useful to consider triple integrals in spherical coordinates. The spherical coordinates (ρ, θ, φ) of a point P(x, y, z) in space are shown in the figure below.

**Diagram**
A 3D diagram illustrates the concept, with the following elements:
* A coordinate system with x, y, and z axes
* A point P(x, y, z) represented by a yellow dot
* A line segment OP connecting the origin O to point P
* Angles θ and φ labeled
* A projection of point P onto the xy-plane, labeled P'(x, y, 0)
* A line segment OP' connecting the origin O to point P'

**Bullet Points**
Three bullet points provide definitions for the variables:
* ρ = |OP|, ρ ≥ 0 is the distance from the origin to P(x, y, z)
* φ, 0 ≤ φ ≤ π is the angle between the positive z-axis and |OP|
* θ, 0 ≤ θ ≤ 2π is the same angle as in cylindrical coordinates

**Logo**
In the bottom-right corner, the University of Waterloo logo is displayed, accompanied by the university's name in black text.

**Background**
The background of the slide is white, with a black bar at the top featuring a yellow stripe.

### Slide 3

The image presents a comprehensive overview of the relationships between rectangular and spherical coordinates, featuring a diagram and accompanying equations.

*   The title "Relationships between Rectangular and Spherical Coordinates" is prominently displayed at the top.
    *   The title is written in large black text.
    *   Below the title, a brief description explains that the relationship between rectangular and spherical coordinates can be found geometrically.
*   A diagram illustrating the geometric representation of the coordinates is shown on the left side of the image.
    *   The diagram features a 3D coordinate system with x, y, and z axes.
    *   A point P is labeled with its rectangular coordinates (x, y, z) and spherical coordinates (ρ, θ, φ).
    *   The diagram includes various angles and distances, such as ρ, θ, φ, r, and z, which are used to derive the relationships between the coordinates.
*   A list of equations derived from the diagram is presented on the right side of the image.
    *   The equations are based on the triangles OPQ and OPP' in the diagram.
    *   The equations include:
        *   z = ρcosφ
        *   r = ρsinφ
        *   x = ρsinφcosθ
        *   y = ρsinφsinθ
        *   ρ = √(x^2 + y^2 + z^2) = √(r^2 + z^2)
    *   These equations demonstrate how to transform between rectangular and spherical coordinates.
*   The University of Waterloo logo is displayed in the bottom-right corner of the image.
    *   The logo features a shield with a red and gold crest, accompanied by the university's name in black text.

In summary, the image provides a clear and concise explanation of the relationships between rectangular and spherical coordinates, along with a visual representation and mathematical derivations. The equations presented enable the transformation between these two coordinate systems, making it a valuable resource for students and professionals working with 3D geometry and calculus.

### Slide 4

The image presents a slide from a lecture on triple integrals in spherical coordinates, featuring a diagram and accompanying text.

*   **Title**: 
    *   The title of the slide is "Triple Integrals in Spherical Coordinates."
    *   It is written in large black font at the top of the slide.
*   **Text**:
    *   The first paragraph explains that to set up the triple integral $I = \iiint_{D} f(x,y,z)dV$ in spherical coordinates, the element of volume $dV$ needs to be expressed in terms of $\rho, \theta,$ and $\phi$.
    *   The second paragraph describes the counterpart of a rectangular differential element of volume (a box) as a small spherical wedge.
*   **Diagram**:
    *   The diagram is a 3D representation of a small spherical wedge.
    *   The wedge is labeled with various symbols, including $\rho, \theta, \phi, d\rho, d\theta,$ and $d\phi$.
    *   The diagram also includes a coordinate system with x, y, and z axes.
*   **University Logo**:
    *   The University of Waterloo logo is displayed in the bottom-right corner of the slide.
    *   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.

In summary, the slide provides an introduction to triple integrals in spherical coordinates, explaining how to express the element of volume $dV$ in terms of $\rho, \theta,$ and $\phi$. The accompanying diagram illustrates a small spherical wedge, highlighting its various components and their relationships to the coordinate system.

### Slide 5

The image presents a slide from a lecture on "Triple Integrals in Spherical Coordinates" at the University of Waterloo. The slide is divided into two sections, each featuring a 3D diagram of a wedge shape.

**Title and Diagrams**

*   **Title**: "Triple Integrals in Spherical Coordinates" in bold black text
*   **Diagrams**: Two 3D diagrams of a wedge shape, labeled as "Side 1 of the wedge" and "Side 2 of the wedge"

**Diagram Details**

*   **Axes**: Each diagram has three axes: x, y, and z, represented by blue arrows
*   **Wedge Shape**: The wedge shape is depicted in blue, with various mathematical symbols and notations overlaid on it
*   **Notations**:
    *   $\rho$, $\phi$, and $\theta$ are used to represent spherical coordinates
    *   $d\rho$, $d\phi$, and $d\theta$ are used to represent infinitesimal changes in these coordinates
    *   $\rho \sin\phi d\theta$ is written in red, indicating the width of the wedge in the $\theta$ direction
    *   $\rho d\phi$ is written in red, indicating the height of the wedge in the $\phi$ direction

**University Logo**

*   The University of Waterloo logo is displayed in the bottom-right corner, featuring a shield with a crest and the university's name in black text

**Background**

*   The background of the slide is white, providing a clean and clear visual representation of the diagrams and text.

### Slide 6

The image presents a detailed diagram illustrating the concept of triple integrals in spherical coordinates, accompanied by relevant mathematical equations and notations. The diagram is titled "Triple Integrals in Spherical Coordinates" and features a 3D wedge shape with various labels and annotations.

**Diagram Components:**

*   A 3D wedge shape is drawn, with its base on the x-y plane and extending upwards along the z-axis.
*   The wedge is labeled with various symbols, including:
    *   $\rho$ (rho): represents the radial distance from the origin to a point within the wedge.
    *   $\phi$ (phi): denotes the angle between the positive z-axis and the line connecting the origin to the point.
    *   $\theta$ (theta): represents the azimuthal angle in the x-y plane.
    *   $d\rho$, $d\phi$, and $d\theta$: represent the infinitesimal changes in $\rho$, $\phi$, and $\theta$, respectively.
*   The diagram also includes annotations highlighting specific features of the wedge, such as:
    *   "Side 3 of the wedge": indicates that the wedge has three sides.
    *   "Don't forget me!!": appears to be a reminder to include a particular term or factor in the calculation.

**Mathematical Equations:**

*   The equation for the volume element $dV$ in spherical coordinates is provided: $dV = \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta$.
*   A triple integral is written in red text, representing the integration of a function $f(\rho, \phi, \theta)$ over the region defined by the wedge: $\iiint_D f(\rho, \phi, \theta) \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta$.

**Additional Elements:**

*   The University of Waterloo logo is displayed in the bottom-right corner of the image, indicating the institution associated with the lecture or presentation.

Overall, the image provides a clear and detailed visual representation of the concept of triple integrals in spherical coordinates, along with the necessary mathematical equations and notations to support understanding and application of this concept.

### Slide 7

The image is a slide from a presentation on finding limits of integration, likely used in a calculus or mathematics course at the University of Waterloo. The slide features a diagram and equations related to triple integrals in spherical coordinates.

*   **Title and University Logo**
    *   The title "Finding Limits of Integration" is prominently displayed at the top of the slide.
    *   The University of Waterloo logo is located in the bottom-right corner.
*   **Diagram**
    *   A 3D diagram is drawn on the slide, illustrating a region bounded by two surfaces defined by the equations $\rho = g_1(\phi, \theta)$ and $\rho = g_2(\phi, \theta)$.
    *   The diagram includes labels for the variables $\rho$, $\phi$, and $\theta$, as well as arrows indicating the direction of integration.
    *   The region is shaded to represent the volume being integrated.
*   **Equations**
    *   The equation for the triple integral in spherical coordinates is written as $I = \int_{\theta=\alpha}^{\beta} \int_{\phi=\phi_{min}}^{\phi_{max}} \int_{\rho=g_1(\phi,\theta)}^{g_2(\phi,\theta)} f(\rho,\phi,\theta)\rho^2\sin\phi d\rho d\phi d\theta$.
    *   The limits of integration are labeled and correspond to the boundaries shown in the diagram.
*   **Variables and Limits**
    *   The variables $\rho$, $\phi$, and $\theta$ are defined, along with their respective limits of integration.
    *   The functions $g_1(\phi, \theta)$ and $g_2(\phi, \theta)$ define the lower and upper bounds of the region in the $\rho$ direction.

In summary, the slide provides a visual representation of a region in 3D space and the corresponding triple integral in spherical coordinates, along with the necessary equations and limits of integration.

### Slide 8

The slide is titled "Finding Limits of Integration" and presents a step-by-step guide on determining the limits of integration for a triple integral in spherical coordinates.

**Main Points:**

1. **SKETCH**
   - Sketch D along with its projection R on the x-y plane, called "shadow".
   - Label surfaces that bound D, and the upper and lower bounding curves of R.

2. **Find the ρ-limits of integration**
   - Draw a ray M passing from the origin through D making an angle φ with the positive z-axis.
   - As ρ increases, M enters D at ρ = g1(φ,θ) and leaves at ρ = g2(φ,θ).
   - These are the ρ-limits of integration.

3. **Find the φ-limits of integration**
   - For any given θ, the angle φ that M makes with the z-axis runs from φ = φmin to φ = φmax.
   - These are the φ limits of integration.

4. **Find the θ-limits of integration**
   - Draw a projection of M on the x-y plane and call this projection L.
   - The ray sweeps over R as the angle θ runs from θ = α to θ = β in our figure.
   - These are the θ-limits of integration.

The slide is presented by the University of Waterloo, as indicated by the logo in the bottom-right corner.

### Slide 9

The slide titled "Problem - Spherical Coordinates" from the University of Waterloo presents a mathematical problem involving the calculation of a volume using spherical coordinates. 

The problem statement is as follows:
- Find the volume V of the Ice Cream Cone cut from the solid sphere, 
  given by the equation $x^2 + y^2 + z^2 = 1$ 
  and by the cone, given by the equation $z^2 = \frac{x^2 + y^2}{3}$, 
  above the x-y plane.

The answer to this problem is provided as $V = \frac{\pi}{3}$.

There are no diagrams or images on this slide; it contains only text and equations. The slide features the University of Waterloo's logo in the bottom-right corner.

### Slide 10

The image presents a slide from a lecture on spherical coordinates, featuring a diagram and various annotations. The title "Problem - Spherical Coordinates" is prominently displayed at the top, followed by the subtitle "Step 1: Sketch." The diagram is accompanied by several equations and labels that provide context to the problem being illustrated.

*   The diagram is a 3D representation of a sphere with various lines and arrows drawn on it.
    *   The sphere is centered at the origin (0, 0, 0) and has a radius of 1 unit.
    *   Three axes are labeled: x, y, and z.
    *   A red curve is drawn on the surface of the sphere, representing a path or trajectory.
    *   Several green and blue lines are also drawn, intersecting the sphere at various points.
    *   Arrows are used to indicate the direction of the axes and the orientation of the sphere.
*   The annotations surrounding the diagram provide additional information about the problem.
    *   The equation x^2 + y^2 + z^2 = 1 is written next to the sphere, indicating that it is a unit sphere.
    *   The label "LEAVES" is written near the top of the diagram, possibly referring to the red curve.
    *   The label "ENTERS" is written near the bottom of the diagram, possibly referring to the point where the green line intersects the sphere.
    *   The equation z^2 = x^2 + y^2 is written near the bottom-left of the diagram, possibly representing a cone or other surface.
    *   The label "R" is written near the center of the diagram, possibly representing the radius of the sphere.
    *   The label "φ = π/3" is written near the bottom-left of the diagram, possibly representing an angle or other parameter.
*   The background of the slide is white, providing a clean and simple backdrop for the diagram and annotations.
*   In the bottom-right corner, the logo for the University of Waterloo is displayed, indicating the institution responsible for creating the slide.

In summary, the image presents a detailed diagram of a sphere in spherical coordinates, accompanied by various annotations and equations that provide context to the problem being illustrated. The diagram shows a unit sphere with a red curve drawn on its surface, as well as several other lines and arrows that intersect the sphere at various points. The annotations include equations and labels that describe the geometry of the sphere and the curves drawn on it. Overall, the image appears to be a teaching tool used to help students understand the concept of spherical coordinates and how to visualize problems involving them.

### Slide 11

The image presents a slide from a lecture on spherical coordinates, titled "Problem - Spherical Coordinates" in large black text at the top. The slide is divided into two sections: the title and a step-by-step solution to a problem.

* **Title**
	+ "Problem - Spherical Coordinates" in large black text
	+ A yellow bar underneath the title
* **Step 2: Transform all equations to spherical coordinates and label all surfaces, shadow, and intersection points.**
	+ A red handwritten equation for a sphere: x^2 + y^2 + z^2 = 1 → ρ = 1
	+ A green handwritten equation for a cone: z^2 = (x^2 + y^2)/3 → (ρcosφ)^2 = ((ρsinφcosθ)^2 + (ρsinφsinθ)^2)/3
	+ Simplification of the cone equation: ρ^2cos^2φ = ρ^2sin^2φ/3 → tanφ = √3 → φ = π/3
	+ A note about the shadow: 0 < θ ≤ 2π
* **University Logo**
	+ University of Waterloo logo in the bottom-right corner

The slide provides a clear and concise solution to a problem involving spherical coordinates, transforming equations for a sphere and a cone into spherical coordinates and labeling the surfaces, shadow, and intersection points.

### Slide 12

The image presents a slide from a presentation on spherical coordinates, featuring a white background with black text and blue, red, and green handwritten notes. The title "Problem - Spherical Coordinates" is prominently displayed at the top.

*   **Title and Step 3: Setup the integral and determine the limits of integration.**
    *   The title is in large black font.
    *   Step 3 is written below the title.
    *   A mathematical equation is presented, involving the variables $\theta$, $\phi$, and $\rho$, with limits of integration.
    *   The equation is:

        $V = \int_{\theta=0}^{\theta=\pi} \int_{\phi=0}^{\phi=\pi/3} \int_{\rho=0}^{\rho=1} \rho^2 \sin\phi d\rho d\phi d\theta$
*   **Step 3: Solve the integral**
    *   Another mathematical equation is shown, continuing from the previous step.
    *   The equation is evaluated step by step, with intermediate results.
    *   The final result is:

        $V = \int_{0}^{2\pi} -\frac{1}{3} \cos\phi \Big|_{0}^{\pi/3} d\theta$
*   **University of Waterloo Logo**
    *   The logo is located in the bottom-right corner of the slide.
    *   It features a shield with a red and yellow design, accompanied by the university's name in black text.

In summary, the slide outlines a problem involving spherical coordinates, guiding the reader through the process of setting up and solving an integral to calculate a volume. The solution is presented in a step-by-step manner, with the final result displayed prominently.

### Slide 13

The image presents a slide from a presentation on solving a problem involving spherical coordinates, with the title "Problem - Spherical Coordinates" prominently displayed in large black text at the top.

**Title and Content**

*   The title is centered and written in bold, black font.
*   Below the title, a mathematical equation is presented in blue handwriting-style text:
    *   $V = \int_{0}^{2\pi} (-\frac{1}{6} + \frac{1}{3}) d\theta$
    *   The integral is evaluated, resulting in:
        *   $V = \frac{1}{6} \theta |_{0}^{2\pi} \rightarrow V = \frac{\pi}{3}$

**University Logo and Branding**

*   In the bottom-right corner of the slide, the University of Waterloo logo is displayed.
*   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.

**Background and Design**

*   The slide's background is white, providing a clean and neutral backdrop for the content.
*   A thick black bar is visible at the top of the slide, with a yellow stripe running along its lower edge, adding a touch of color and visual interest to the design.

### Slide 14

The image presents a slide from a lecture on mathematics, specifically focusing on finding the volume of a region enclosed by two surfaces. The title "Bringing Back our Problem from Lecture 25" is prominently displayed at the top.

**Key Elements:**

* **Title:** "Bringing Back our Problem from Lecture 25"
* **Problem Statement:** Find the volume of the region D enclosed by the surfaces z = x^2 + 3y^2 and z = 8 - x^2 - y^2.
* **Step 1: Sketch**
	+ A 3D graph illustrating the intersection of the two surfaces.
	+ The graph features a red surface representing z = 8 - x^2 - y^2 and a blue surface representing z = x^2 + 3y^2.
	+ The x, y, and z axes are labeled, with the x-axis pointing to the left, the y-axis pointing to the right, and the z-axis pointing upwards.
	+ The region D is highlighted in red.
* **Mathematical Equations:**
	+ z = 8 - x^2 - y^2
	+ z = x^2 + 3y^2
	+ V = ∫∫∫dV (triple integral)
	+ Limits of integration: -√((4-x^2)/2) ≤ y ≤ √((4-x^2)/2), -2 ≤ x ≤ 2, x^2 + 3y^2 ≤ z ≤ 8 - x^2 - y^2
* **University Logo:** University of Waterloo logo in the bottom-right corner.

**Summary:**

The slide presents a mathematical problem involving the calculation of the volume of a region enclosed by two surfaces. The problem is broken down into steps, starting with a sketch of the region. The sketch is accompanied by mathematical equations that define the surfaces and the limits of integration for the triple integral used to calculate the volume. The University of Waterloo logo is displayed in the bottom-right corner, indicating the institution associated with the lecture.

### Slide 15

The image presents a detailed diagram related to a mathematical problem, titled "Bringing Back our Problem from Lecture 25" in bold black text at the top. The diagram is accompanied by various equations and notations, suggesting a complex mathematical concept is being illustrated.

**Key Elements:**

*   **Title:** "Bringing Back our Problem from Lecture 25"
*   **Diagram:**
    *   A 3D coordinate system with x, y, and z axes
    *   A red circle labeled "D" with an arrow pointing upwards
    *   A blue curve intersecting the red circle
    *   A green curve representing the intersection of the blue curve and the x-y plane
*   **Equations and Notations:**
    *   z = 8 - x^2 - y^2
    *   z = 8 - r^2
    *   z = x^2 + 3y^2
    *   z = r cos(θ) + 3r sin(θ)
    *   z = r^2 (1 + 2 sin^2(θ))
    *   y = ±√((4-x^2)/2)
    *   x^2 + 2y^2 = 4
    *   r = 2 / √(1 + sin^2(θ))
*   **Labels and Annotations:**
    *   "LEAVES" and "ENTERS" labels on the diagram
    *   "CYLINDRICAL COORD." notation next to the equations
*   **Logo and Institution:**
    *   University of Waterloo logo in the bottom-right corner

**Summary:**

The image presents a complex mathematical diagram with accompanying equations and notations, illustrating a problem from Lecture 25. The diagram features a 3D coordinate system, a red circle, and various curves, with labels and annotations providing context. The equations and notations suggest a focus on cylindrical coordinates and the transformation of functions between different coordinate systems. The University of Waterloo logo indicates the academic institution associated with the content.

### Slide 16

The image presents a lecture slide titled "Bringing Back our Problem from Lecture 25" in black text. The slide is divided into two main sections: the top section, which discusses cylindrical coordinates, and the bottom section, which explores spherical coordinates.

**Top Section: Cylindrical Coordinates**

* The title "CYLINDRICAL COORDINATES" is written in blue text.
* A triple integral is presented: $V = \int_{0}^{2\pi} \int_{0}^{\sqrt{1+\sin\theta}} \int_{r^2/(1+2\sin^2\theta)}^{8-r^2} dz \, r \, dr \, d\theta$
* The integral is annotated with notes in green and red text, including:
	+ "DO NOT FORGET!" in green text, accompanied by an arrow pointing to the $r$ term.
	+ "MESSIER!!" in red text.

**Bottom Section: Spherical Coordinates**

* The title "SPHERICAL??" is written in red text.
* An equation is presented: $z = 8 - x^2 - y^2 \rightarrow \rho \cos \phi = 8 - (\rho \sin \phi)^2 \rightarrow 8??$
* The equation is annotated with notes in red text, including:
	+ "SUPER MESSY!!" in red text.
* A logo for the University of Waterloo is displayed in the bottom-right corner.

In summary, the slide revisits a problem from Lecture 25, exploring solutions in both cylindrical and spherical coordinates. The cylindrical coordinates section presents a triple integral with annotations, while the spherical coordinates section examines an equation and notes the complexity of the solution.

### Slide 17

The image presents a slide from a presentation on triple integrals, featuring a white background with black text and a yellow stripe at the top. The title "Summary" is prominently displayed in large bold font at the top left.

*   **Title and Introduction**
    *   The title "Summary" is written in large bold font.
    *   Below the title, a bullet point reads: "We have covered all three types of triple integrals* for a function f(x,y,z)."
*   **Types of Triple Integrals**
    *   Three sub-bullet points list the different types of coordinates and their corresponding integral formulas:
        *   Rectangular coordinates: $\iiint_D f(x,y,z)dzdydx$
        *   Cylindrical coordinates: $\iiint_D f(r,\theta,z)dz rdrd\theta$
        *   Spherical coordinates: $\iiint_D f(\rho,\theta,\phi)\rho^2 \sin \phi d\rho d\phi d\theta$
*   **Coordinate Systems and Symmetry**
    *   Two bullet points discuss the application of different coordinate systems based on symmetry:
        *   Rectangular coordinates are mostly used for problems without clear symmetry.
        *   Cylindrical and spherical coordinates can be used for problems with symmetry about an axis and about a point, respectively.
*   **Note on Differentials of Volume**
    *   A footnote at the bottom of the slide states: "*Note that the differentials of volume can be used in six different combinations."
*   **University Logo**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner, featuring a red and gold crest accompanied by the university's name in black text.

In summary, the slide provides a concise overview of triple integrals, covering the three main types of coordinates and their applications, as well as a note on the flexibility of using differentials of volume in different combinations.

### Slide 18

The image is a slide from a presentation, likely the final slide, as it contains a "Thank you" message. The slide features the University of Waterloo logo and branding.

* **University of Waterloo Logo**
	+ Located on the left side of the image
	+ Shield-shaped with a yellow background and red lions
	+ Black chevrons pointing upwards
	+ Text "UNIVERSITY OF WATERLOO" in bold black font to the right of the logo
* **Thank You Message**
	+ Centered at the bottom of the image
	+ Text "Thank you" in bold black font
* **Background**
	+ White background
	+ Yellow and black gradient bar at the top of the image

The image does not contain any numerical data or statistics.

