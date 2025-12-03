# Lecture 26 - Triple Integrals Cylindrical Coordinates

## Study Notes

# Triple Integrals in Cylindrical Coordinates – Exam Study Notes  

## Core Formulas & Definitions  

| Formula | What it means | When to use |
|---------|----------------|--------------|
| **Cylindrical coordinates** | $$x = r\cos\theta,\qquad y = r\sin\theta,\qquad z = z$$ | Convert a Cartesian point \((x,y,z)\) to \((r,\theta,z)\). |
| **Jacobian (volume element)** | $$dV = r\,dr\,d\theta\,dz$$ | Always include the factor \(r\) in a cylindrical triple integral. |
| **General triple integral** | $$\iiint_D f(x,y,z)\,dV = \int_{\theta_1}^{\theta_2}\int_{r_{\min}(\theta)}^{r_{\max}(\theta)}\int_{z_{\min}(r,\theta)}^{z_{\max}(r,\theta)} f(r,\theta,z)\,r\,dz\,dr\,d\theta$$ | When \(D\) is naturally described by radial symmetry. |
| **Volume of a solid** | $$V = \iiint_D dV$$ | Needed for mass or centroid calculations with constant density. |
| **First moments** | $$M_x = \iiint_D x\,dV,\qquad M_y = \iiint_D y\,dV,\qquad M_z = \iiint_D z\,dV$$ | Compute centroid coordinates. |
| **Centroid (center of mass)** | $$\bar{x}=\frac{M_x}{V},\quad \bar{y}=\frac{M_y}{V},\quad \bar{z}=\frac{M_z}{V}$$ | Uniform density. |
| **Symmetry shortcut** | If \(D\) and density are rotationally symmetric about the \(z\)-axis, then \(\bar{x}=\bar{y}=0\). | Reduces centroid problem to one integral for \(\bar{z}\). |
| **Projection bounds** | On the \(xy\)-plane: \(\theta\) from \(\alpha\) to \(\beta\); \(r\) from \(h_1(\theta)\) to \(h_2(\theta)\). | Determine radial/angular limits before integrating in \(z\). |
| **Vertical limits** | For fixed \((r,\theta)\): \(z\) from \(g_1(r,\theta)\) to \(g_2(r,\theta)\). | Set after sketching the solid. |

---

## Key Concepts & Intuition  

- **Decomposition** – Cylindrical coordinates split space into radial distance \(r\), azimuthal angle \(\theta\), and height \(z\).  
- **Volume element** – The factor \(r\) accounts for the circumference of a circle of radius \(r\).  
- **Symmetry** – Rotational symmetry about the \(z\)-axis often forces \(\bar{x}=\bar{y}=0\).  
- **Sketch first** – Draw the projection \(R\) on the \(xy\)-plane and the vertical slices before writing limits.  

---

## Problem‑Solving Strategies  

### 1. Setting Up a Triple Integral  

| Cue | Checklist | Typical Result |
|-----|-----------|----------------|
| **Solid described by surfaces** | 1. Identify all bounding surfaces.<br>2. Sketch the projection \(R\).<br>3. Determine \(\theta\) limits \(\alpha\to\beta\).<br>4. For each \(\theta\), find \(r\) limits \(h_1(\theta)\to h_2(\theta)\).<br>5. For each \((r,\theta)\), find \(z\) limits \(g_1(r,\theta)\to g_2(r,\theta)\). | Correct nested integrals. |
| **Integrand \(f(x,y,z)\)** | Convert \(f\) to \(f(r,\theta,z)\) using \(x=r\cos\theta,\;y=r\sin\theta\). | Simplified integrand, e.g. \(r^2+z\). |
| **Symmetry present** | Verify rotational symmetry in both domain and integrand. If true, set \(\bar{x}=\bar{y}=0\). | Reduces work for centroids. |
| **Volume needed first** | Compute \(V\) before first moments if density is constant. | Avoid carrying \(\rho\) through the calculation. |

### 2. Computing Volume  

1. Write \(dV = r\,dr\,d\theta\,dz\).  
2. Integrate \(z\) first if bounds are simple.  
3. Use symmetry to collapse \(\theta\) limits if appropriate.  

### 3. Center of Mass (Constant Density)  

1. **Volume**: \(V = \iiint dV\).  
2. **Moments**:  
   - \(M_x = \iiint x\,dV\) (often zero by symmetry).  
   - \(M_y = \iiint y\,dV\) (often zero).  
   - \(M_z = \iiint z\,dV\).  
3. **Centroid**: \(\bar{x}=M_x/V,\ \bar{y}=M_y/V,\ \bar{z}=M_z/V\).  
4. **Shortcut**: If \(D\) is symmetric about the \(xy\)-plane, \(\bar{z}\) is the average \(z\) value.  

### 4. Shell Method (Rotation About \(z\)-Axis)  

- Shell volume: \(dV = 2\pi r\,h\,dr\).  
- In cylindrical coordinates the factor \(r\) already implements the shell method.  

### 5. Variable Density  

- Include \(\rho(r,\theta,z)\) inside every integral.  
- Do not cancel \(\rho\) unless it is constant.

---

## Common Pitfalls & Checks  

| Issue | How to avoid |
|-------|--------------|
| **Missing \(r\) in \(dV\)** | Always write \(dV = r\,dr\,d\theta\,dz\) unless you are using a different coordinate system. |
| **Incorrect bounds** | Redraw the projection and verify each limit. Check that \(r_{\min} \le r_{\max}\) and that \(z_{\min}\le z_{\max}\). |
| **Order of integration** | After choosing an order, make sure all limits are expressed in terms of the remaining variables. |
| **Misapplied symmetry** | Confirm the domain and integrand are truly invariant under rotation or reflection before setting moments to zero. |
| **Density confusion** | Keep \(\rho\) inside the integrals if variable; if constant, cancel it only after computing \(V\). |
| **Units** | Ensure consistent units throughout; a missing factor of \(2\pi\) often comes from an omitted angular integral. |

---

## Quick Reference: Cylinder Under a Paraboloid  

- **Region**: \(x^2+y^2 \le 4,\; 0 \le z \le x^2+y^2\).  
- **Bounds**: \(\theta:0\to2\pi,\; r:0\to2,\; z:0\to r^2\).  
- **Volume**:  
  \[
  V = \int_0^{2\pi}\!\!\int_0^2\!\!\int_0^{r^2} r\,dz\,dr\,d\theta
      = \frac{16\pi}{3}
  \]
- **Centroid** (constant density):  
  \[
  \bar{z} = \frac{1}{V}\int_0^{2\pi}\!\!\int_0^2\!\!\int_0^{r^2} z\,r\,dz\,dr\,d\theta
          = \frac{4}{3}
  \]
  (so \((\bar{x},\bar{y},\bar{z})=(0,0,\tfrac{4}{3})\)).  

Use this template whenever the solid is bounded by a cylinder and a surface depending only on \(r\).

---

## Raw Slide Summaries

### Slide 1

The image presents a slide from a presentation on "Triple Integrals in Cylindrical Coordinates" for the University of Waterloo. The slide is divided into three main sections: title, image, and footer.

*   **Title Section**
    *   **Title**: "Triple Integrals in Cylindrical Coordinates"
        *   Font: Large, bold, black font
        *   Position: Centered at the top of the slide
    *   **Subtitle**: "Trim Ch 13, S. 13.11"
        *   Font: Smaller, black font within a yellow rectangle
        *   Position: Below the title, aligned to the left
*   **Image Section**
    *   **Image**: A large, silver cylindrical tank with various pipes and valves attached to it.
        *   Position: Right side of the slide, below the title section
        *   URL: "https://www.kesarequipments.com/bitumen-heating-and-%20storage-tank.html" (provided below the image)
*   **Footer Section**
    *   **University Logo**: University of Waterloo logo
        *   Position: Bottom-left corner of the slide
    *   **University Name**: "UNIVERSITY OF WATERLOO"
        *   Font: Black font next to the logo

The slide effectively conveys the topic of the presentation and provides a relevant visual example, while also crediting the source of the image and the institution.

### Slide 2

The image presents a slide from a lecture on triple integrals in cylindrical coordinates, featuring a diagram and accompanying text. The title, "Triple Integrals in Cylindrical Coordinates," is prominently displayed at the top of the slide.

*   **Title and Description**
    *   The title is followed by a brief description that explains the utility of cylindrical coordinates in physics and engineering problems involving one axis of symmetry.
    *   The text highlights the combination of polar coordinates in the xy-plane with the usual z-axis to obtain cylindrical coordinates for space.
*   **Definition of Cylindrical Coordinates**
    *   Two bullet points define the components of cylindrical coordinates:
        *   "r and θ" are polar coordinates of the vertical projection of P on the x-y plane.
        *   "z" is the rectangular vertical coordinate.
*   **Transformation Equations**
    *   A list of transformation equations is provided, relating Cartesian coordinates (x, y, z) to cylindrical coordinates (r, θ, z):
        *   x = r cos θ
        *   y = r sin θ
        *   r^2 = x^2 + y^2
        *   tan θ = y/x
        *   z = z
*   **Diagram**
    *   A 3D diagram illustrates the relationship between Cartesian and cylindrical coordinates, showing:
        *   A point P(r, θ, z) in 3D space.
        *   The projection of P onto the xy-plane.
        *   The angle θ between the positive x-axis and the projection of P.
        *   The distance r from the origin to the projection of P.
        *   The height z above the xy-plane.
*   **University Logo**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner of the slide.

In summary, the slide provides a concise introduction to triple integrals in cylindrical coordinates, including their definition, transformation equations, and a visual representation through a 3D diagram.

### Slide 3

The image presents a slide from a presentation on "Triple Integrals in Cylindrical Coordinates" at the University of Waterloo. The title, prominently displayed in large black text at the top, sets the stage for the detailed explanation that follows.

*   **Title and Context**
    *   The title "Triple Integrals in Cylindrical Coordinates" is centered at the top.
    *   Below the title, a brief description explains that the element of volume of the triple integral combines cartesian and polar coordinates.
*   **Mathematical Equations**
    *   The first equation defines the triple integral $I = \iiint_D f(x,y,z)dV$.
    *   A series of equations illustrate the conversion to cylindrical coordinates, culminating in $\iiint_D f(r,\theta,z) dz r dr d\theta$.
    *   The notation "FORGET ME NOT 'r'" is handwritten next to the final equation, emphasizing the importance of including 'r' in the integral.
*   **Graphical Representation**
    *   A 3D graph is drawn on the left side, illustrating the concept of cylindrical coordinates.
    *   The graph features axes labeled X, Y, and Z, with a curved surface and various symbols ($\Delta V_k$, $r\Delta\theta_k$, $\Delta r_k$, $\Delta z_k$) indicating the differential volume element in cylindrical coordinates.
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner, signifying the academic context of the presentation.

In summary, the slide provides a comprehensive overview of triple integrals in cylindrical coordinates, including the mathematical formulation and a visual representation to aid understanding.

### Slide 4

The image is a slide from a presentation on calculus, specifically discussing the topic of "Finding Limits of Integration in Cylindrical Coordinates." The slide is divided into two main sections: a diagram and accompanying equations.

**Title and Background**

*   The title "Finding Limits of Integration in Cylindrical Coordinates" is prominently displayed at the top of the slide.
*   The background of the slide is white, providing a clean and neutral backdrop for the content.

**Diagram**

*   The diagram is drawn in green and blue ink, with some red accents.
*   It depicts a 3D cylindrical region, labeled "D," with its base on the xy-plane and extending upwards along the z-axis.
*   The region is bounded by two curved surfaces: $z = g_1(r,\theta)$ and $z = g_2(r,\theta)$.
*   The projection of the region onto the xy-plane is shown, with the boundaries defined by $r = h_1(\theta)$ and $r = h_2(\theta)$, and the angular limits $\theta = \alpha$ and $\theta = \beta$.
*   The diagram also includes labels for the x, y, and z axes, as well as arrows indicating the direction of the positive axes.

**Equations**

*   The slide presents several equations related to the diagram, including:
    *   $\int_{\alpha}^{\beta} \int_{h_1(\theta)}^{h_2(\theta)} \int_{g_1(r,\theta)}^{g_2(r,\theta)} f(r,\theta,z) \, dz \, r \, dr \, d\theta$
    *   $z = g_1(r,\theta)$ and $z = g_2(r,\theta)$, which represent the lower and upper bounds of the z-integration, respectively.
    *   $r = h_1(\theta)$ and $r = h_2(\theta)$, which define the inner and outer radial limits of integration.
    *   $\theta = \alpha$ and $\theta = \beta$, which specify the angular limits of integration.

**University Logo**

*   In the bottom-right corner of the slide, the University of Waterloo logo is displayed, indicating the institution associated with the presentation.

Overall, the slide provides a clear and concise visual representation of the concept of finding limits of integration in cylindrical coordinates, accompanied by relevant mathematical equations.

### Slide 5

The slide is titled "Finding Limits of Integration in Cylindrical Coordinates" and features a white background with black text, except for headings which are in purple. The University of Waterloo logo is displayed in the bottom-right corner. 

The content is organized into four main bullet points:

* **SKETCH**: 
  - Sketch D and its vertical projection in the x-y plane R, called "shadow".
  - Label upper and lower bound surfaces of D and the upper and lower bounding curves of R.

* **Find the z-limits of integration**:
  - Draw a line M passing through a typical point (r,θ) in R, and parallel to the z-axis.
  - As z increases, M enters D at z = g1(r,θ) and leaves at z = g2(r,θ).

* **Find the r-limits of integration**:
  - Draw a ray L through (r,θ) from the origin.
  - As r increases, the ray L enters at r = h1(θ) and leaves at r = h2(θ).

* **Find the θ-limits of integration**:
  - As the line L sweeps across R, the angle θ it makes with the positive x-axis runs from θ = α to θ = β.

There are no diagrams or images on this slide.

### Slide 6

The image shows a slide from a presentation on triple integrals and their applications, specifically focusing on finding the center of mass of a solid enclosed by a cylinder and bounded by a paraboloid and the x-y plane.

*   **Title**: "Problem - Triple Integrals and Applications"
    *   The title is in large black text at the top of the slide.
*   **Problem Statement**:
    *   The center of mass of the solid enclosed by the cylinder $x^2 + y^2 = 4$ bounded above by the paraboloid $z = x^2 + y^2$, and bounded below by the x-y plane is given by,
        *   $\overline{r_i} = \frac{\iiint_D r_i \delta(x,y,z)dV}{\iiint_D \delta(x,y,z)dV}$
    *   Where $\delta(x,y,z)$ is the density and $r_i$ are the coordinates of the center of mass $(\overline{x},\overline{y},\overline{z}) = (r_1,r_2,r_3)$.
*   **Task**:
    *   Find the center of mass of the solid assuming that the density is constant.
*   **Solution**:
    *   The section is labeled "Solution:" but does not contain any information.
*   **University Logo**:
    *   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

The slide presents a problem involving the calculation of the center of mass of a solid defined by specific boundaries and asks to find the center of mass under the assumption of constant density. The solution section is empty, indicating that the actual solution is not provided on this slide.

### Slide 7

The image presents a detailed lecture slide on the topic "Problem - Triple Integrals and Applications." The content is organized into several key elements, which are described below:

**Title and Step 1: Sketch**

* The title is prominently displayed at the top of the slide in large black text.
* Below the title, "STEP 1: SKETCH" is written in green handwriting-style text.

**3D Graph**

* A 3D graph is drawn on the left side of the slide, featuring:
	+ A cylindrical shape with a circular base and a curved top.
	+ The x, y, and z axes are labeled.
	+ The graph includes several equations and labels, such as:
		- z = x^2 + y^2 (red)
		- z = y^2 (blue)
		- x^2 + y^2 = 4 (green)
	+ The region of integration, R, is highlighted in red.

**Equations and Notes**

* To the right of the graph, several equations and notes are written in blue handwriting-style text:
	+ "BECAUSE OF SYMMETRY, Cm = (x̄, ȳ, z̄)" and "Cm = (0, 0, z̄)" with an asterisk symbol.
	+ "INTERSECTION:" followed by the equations:
		- z = x^2 + y^2
		- x^2 + y^2 = 4
	+ The resulting equation: "z = 4" and "r = 2" are highlighted in a blue circle.
* Below the graph, additional notes are written:
	+ "TRANSFORM TO CYLINDRICAL COORD" with the equation: "r^2 cos^2 θ + r^2 sin^2 θ = 4" simplified to "r^2 = 4" and then to "r = 2" within a yellow oval.

**University Logo**

* The University of Waterloo logo is displayed in the bottom-right corner of the slide.

Overall, the slide appears to be a detailed explanation of a problem involving triple integrals and their applications, with a focus on visualizing the region of integration and transforming the problem into cylindrical coordinates.

### Slide 8

The image presents a slide from the University of Waterloo, titled "Problem - Triple Integrals and Applications." The slide features a white background, a yellow bar at the top, and a black bar above it. The title is prominently displayed in large, bold, black text.

The slide's content includes various mathematical equations and formulas, written in blue, green, and red ink. The equations are:

*   $\overline{z} = \frac{\iiint_D z \rho dV}{\iiint_D \rho dV} = \frac{\iiint_D z dV}{\iiint_D dV}$, where $\rho = const.$
*   $\int_{0}^{2\pi} \int_{0}^{a} \int_{0}^{r^2} z dz r dr d\theta$
*   $\int_{0}^{2\pi} \int_{0}^{a} \left[\frac{z^2}{2}\right]_{0}^{r^2} r dr d\theta = \int_{0}^{2\pi} \int_{0}^{a} \frac{r^5}{2} dr d\theta$

These equations are accompanied by notes and annotations, including "NUMERATOR" and "DON'T FORGET ME!" The University of Waterloo's logo is displayed in the bottom-right corner of the slide.

The overall appearance of the slide suggests that it is part of a lecture or presentation on triple integrals and their applications, likely in a mathematics or physics course.

### Slide 9

The image presents a slide from a presentation on triple integrals and their applications, featuring a white background with a yellow stripe at the top. The title, "Problem - Triple Integrals and Applications," is prominently displayed in large black text.

**Key Elements:**

* **Title:** "Problem - Triple Integrals and Applications" in large black text
* **Mathematical Equations:** A series of complex mathematical equations are written in green marker on the slide, including:
	+ Integral equations
	+ Algebraic expressions
	+ Calculations
* **University Logo:** The University of Waterloo logo is displayed in the bottom-right corner, featuring a shield with a red and gold design, accompanied by the university's name in black text
* **Background:** White background with a yellow stripe at the top

**Detailed Description:**

The slide appears to be a solution to a problem involving triple integrals, with the equations and calculations presented in a step-by-step manner. The use of green marker suggests that the equations were written on the slide during a live presentation or lecture. The presence of the University of Waterloo logo indicates that the presentation is affiliated with the university.

**Key Takeaways:**

* The slide presents a solution to a problem involving triple integrals and their applications
* The equations and calculations are presented in a step-by-step manner
* The presentation is affiliated with the University of Waterloo

### Slide 10

The image presents a slide from a presentation on triple integrals and their applications, specifically focusing on a problem related to the center of mass. The slide is titled "Problem - Triple Integrals and Applications" in bold black text at the top.

*   **Title**: The title is centered and written in large, bold font.
*   **Content**: Below the title, there is a handwritten note in green that reads: "THE CENTER OF MASS, c.m. (0,0, 4/3)". This suggests that the problem involves calculating or understanding the center of mass of an object or system.
*   **Logo**: In the bottom-right corner, there is a logo for the University of Waterloo. The logo features a shield with a red and gold design, accompanied by the university's name in black text.
*   **Background**: The background of the slide is white, providing a clean and simple backdrop for the content.

In summary, the image displays a slide discussing a problem related to the center of mass and its relation to triple integrals, presented by the University of Waterloo.

### Slide 11

The image is a slide from a presentation, likely used for educational purposes. The title of the slide is "Problem - Triple Integrals and Applications" in large black text at the top.

*   The title is centered and written in bold font.
*   Below the title, there is a blank space that takes up most of the slide.
*   At the bottom right corner of the slide, there is a logo for the University of Waterloo.
    *   The logo features a shield with a red and yellow design, accompanied by the words "UNIVERSITY OF WATERLOO" in black text.
    *   The logo is positioned below the main content of the slide, indicating that it is likely a footer or branding element.

The overall design of the slide is simple and clean, with a focus on presenting information in a clear and concise manner. The use of a blank space suggests that the slide may be intended to be used as a template or a placeholder for additional content.

### Slide 12

The image is a slide from a presentation, likely the final slide, expressing gratitude to the audience.

*   **University of Waterloo Logo**
    *   Located at the top left of the image
    *   Features a yellow shield with a black chevron and three red lions
    *   The text "UNIVERSITY OF WATERLOO" is written in large black font to the right of the logo
*   **Thank You Message**
    *   Positioned below the logo and university name
    *   Written in large black font
    *   Reads "Thank you"
*   **Background**
    *   White background
    *   A black and yellow stripe runs along the top edge of the image

The image appears to be a simple and professional way to conclude a presentation, likely used by the University of Waterloo.

