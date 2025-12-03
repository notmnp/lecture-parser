# Lecture 24 - Double Integrals Applications

## Study Notes

# Double Integrals – Problem‑Solving Study Notes

---

## Core Formulas & Definitions

| Topic | Formula | Symbols Explained | Typical Use |
|-------|---------|-------------------|-------------|
| **Area of a region \(R\)** | $$A_R=\iint_R dA$$ | \(dA\) = infinitesimal area element | Compute geometric area, needed for averages and densities. |
| **Average value of \(f\)** | $$\overline{f}=\frac{1}{A_R}\iint_R f(x,y)\,dA$$ | \(\overline{f}\) = mean of \(f\) over \(R\) | Mean temperature, concentration, etc. |
| **Mass of a plate** | $$M=\iint_R \delta(x,y)\,dA$$ | \(\delta(x,y)\) = mass density (kg m\(^{-2}\)) | Variable or constant density. |
| **First moments** | $$M_x=\iint_R y\,\delta\,dA,\qquad M_y=\iint_R x\,\delta\,dA$$ | \(M_x,M_y\) = moments about the \(x\)- and \(y\)-axes | Needed for centroid. |
| **Center of mass** | $$\bar{x}=\frac{M_y}{M},\qquad \bar{y}=\frac{M_x}{M}$$ | \((\bar{x},\bar{y})\) = centroid | Locate balancing point. |
| **Moments of inertia** | <br>• About \(x\)-axis: $$I_x=\iint_R y^2\,\delta\,dA$$<br>• About \(y\)-axis: $$I_y=\iint_R x^2\,\delta\,dA$$<br>• About origin: $$I_0=\iint_R (x^2+y^2)\,\delta\,dA = I_x+I_y$$ | \(r(x,y)\) = distance from \((x,y)\) to the axis | Rotational inertia of laminae. |
| **Polar transform** | $$x=r\cos\theta,\qquad y=r\sin\theta,\qquad r^2=x^2+y^2$$ | \(r\ge0\) = radial distance; \(\theta\) = polar angle | Express curves \(r=f(\theta)\). |
| **Differential area in polar** | $$dA=r\,dr\,d\theta$$ | Jacobian factor \(r\) | Use whenever integrating in polar coordinates. |

---

## Key Concepts & Intuition

- **Choosing integration order**  
  *Sketch the region first.*  
  • If vertical strips give simple \(y\)-limits, use \(dx\,dy\).  
  • If horizontal strips are cleaner, use \(dy\,dx\).  
  • Re‑order only when it simplifies bounds or integrand.

- **Setting bounds**  
  • Find all intersection points of boundary curves.  
  • For a fixed outer variable, express the inner variable’s limits as functions of it.  
  • Verify that the inner limits are **functions of the outer variable only**.

- **Polar coordinates**  
  • Use when the region is radial (circles, annuli, sectors) or when boundaries are given as \(r=f(\theta)\).  
  • \(\theta\) limits span the angular extent once; \(r\) limits span the radial extent.  
  • Remember \(r\ge0\); if the region crosses the origin, split into sub‑regions.

- **Center of mass symmetry**  
  • If the region is symmetric about an axis, the corresponding centroid coordinate is the axis value (e.g., \(\bar{y}=0\) for symmetry about \(x\)-axis).

---

## Problem‑Solving Strategies

### 1. Area Between Curves (Cartesian)

1. **Sketch** the curves; note intersections.  
2. Decide outer variable (usually the one whose bounds are constant or easier).  
3. Write \(A=\displaystyle\int_{x_1}^{x_2}\!\!\int_{y_{\text{bot}}(x)}^{y_{\text{top}}(x)}dy\,dx\).  
4. Evaluate inner integral as \(y_{\text{top}}-y_{\text{bot}}\).  
5. Integrate the resulting single integral.

### 2. Average Value of \(f\)

1. Compute area \(A_R\).  
2. Compute \(\iint_R f\,dA\).  
3. Divide: \(\overline{f}= (\iint_R f\,dA)/A_R\).

### 3. Mass & Center of Mass

1. \(M=\iint_R \delta\,dA\).  
2. \(M_x=\iint_R y\,\delta\,dA\); \(M_y=\iint_R x\,\delta\,dA\).  
3. \(\bar{x}=M_y/M,\; \bar{y}=M_x/M\).

### 4. Moment of Inertia

1. Identify axis/line.  
2. Choose integrand: \(y^2\delta\) for \(x\)-axis; \(x^2\delta\) for \(y\)-axis; \((x^2+y^2)\delta\) for origin.  
3. Set up \(\iint_R\) over the given region.  
4. Evaluate.

### 5. Polar Coordinate Integration

1. **Determine angular bounds** \(\theta\in[\alpha,\beta]\) from the sector or radial limits.  
2. **Find radial bounds**:  
   • Inner radius \(r_{\min}(\theta)=h_1(\theta)\) (often 0).  
   • Outer radius \(r_{\max}(\theta)=h_2(\theta)\).  
3. Write integral:  
   $$\iint_R f(x,y)\,dA = \int_{\alpha}^{\beta}\int_{h_1(\theta)}^{h_2(\theta)} f(r\cos\theta,\,r\sin\theta)\,r\,dr\,d\theta.$$  
4. Integrate \(r\) first if it simplifies (often the case).  
5. Check that \(\theta\) limits cover the region once.

### 6. Converting Cartesian to Polar

- Replace \(x\) and \(y\) with \(r\cos\theta\) and \(r\sin\theta\).  
- Add \(r\) factor to the integrand.  
- Adjust bounds to polar limits.

---

## Common Pitfalls & Checks

| Mistake | Why It Happens | Fix |
|---------|----------------|-----|
| **Incorrect bounds** | Forgetting dependence on outer variable. | Draw the region; write bounds explicitly as functions. |
| **Order swap errors** | Swapping \(dx\,dy\) to \(dy\,dx\) without changing limits. | Re‑derive limits for the new order. |
| **Missing \(r\) in \(dA\)** | Treating polar integral as \(\int dr\,d\theta\). | Always use \(r\,dr\,d\theta\). |
| **Wrong density** | Using constant density when \(\delta(x,y)\) varies. | Read the problem; plug in \(\delta(x,y)\) exactly. |
| **Neglecting denominator in average** | Using \(\iint f\,dA\) alone. | Remember \(\overline{f}= (\iint f\,dA)/A_R\). |
| **Integrating over wrong region** | Mis‑identifying intersection points. | Verify intersections numerically if uncertain. |
| **Sign errors** | Wrong order of limits. | Check with a quick numerical test. |
| **Over‑extending \(\theta\)** | Using \(0\)–\(2\pi\) for a half‑disk. | Restrict \(\theta\) to the actual angular span. |

---

### Quick Polar Integration Cheat Sheet

| Step | Action | Example |
|------|--------|---------|
| 1 | Identify \(\alpha,\beta\) from angular boundaries | Sector between \(\theta=0\) and \(\theta=\pi/3\). |
| 2 | Set \(r_{\min}=0\), \(r_{\max}=R\) (or \(h_1(\theta),h_2(\theta)\)) | Annulus: \(h_1=1,\;h_2=2\). |
| 3 | Write integral | \(\displaystyle\int_0^{\pi/3}\int_0^{R} f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta\). |
| 4 | Evaluate inner \(r\) integral (often polynomial in \(r\)). | \(\int_0^{R} r\,dr = R^2/2\). |
| 5 | Finish outer \(\theta\) integral. | \(\int_0^{\pi/3}\cos^2\theta\,d\theta\). |

---

**End of notes.**

---

## Raw Slide Summaries

### Slide 1

The image displays a slide from a presentation on double integrals, featuring the title "Double Integrals - Applications" in large black text at the top. The slide is divided into sections, with the main content organized as follows:

*   **Title and Reference**
    *   The title "Double Integrals - Applications" is prominently displayed.
    *   A yellow box below the title contains the text "Trim Ch 13, S. 13.5, 13.7", likely referencing the relevant chapter and sections in a textbook.
*   **Outline**
    *   The outline section is headed by the word "Outline:" in bold text.
    *   Two numbered points are listed:
        1.  Applications of Double Integrals
        2.  Double Integrals in Polar Coordinates
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-left corner, featuring a shield with a red crest and the university's name in black text.

The slide's background is white, with a decorative border at the top consisting of a black bar and a yellow gradient. The overall design suggests that this is an introductory slide for a lecture or presentation on the topic of double integrals and their applications.

### Slide 2

The image presents a slide from the University of Waterloo, titled "Area of Bounded Regions in the Plane." The slide is divided into three sections: the title, the main content, and a diagram.

**Title Section**
* The title is centered at the top of the slide.
* It reads "Area of Bounded Regions in the Plane" in large black text.

**Main Content Section**
* Below the title, a statement explains that the area of a bounded region R in the plane can be obtained if z = f(x,y) = 1.
* A mathematical equation is provided: A_R = ∫∫_R dA.
* The area of the region R will be given by this equation.

**Diagram Section**
* A graph is displayed, showing a closed curve labeled "R" on a coordinate plane with x and y axes.
* The region enclosed by the curve is shaded, representing the thin lamina.
* A small circle within the region is labeled "(x,y)" and has an arrow pointing to it, indicating the point (x,y).
* Another label, "dA," is placed near the center of the circle, suggesting that dA represents an infinitesimal area element.
* A red arrow points to the boundary of the region, labeling it as "Thin Lamina."

**Footer Section**
* In the bottom-left corner, a copyright notice reads "Copyright © 2008 Pearson Education Canada."
* In the bottom-right corner, the University of Waterloo's logo is displayed, featuring a shield with a yellow and red design, accompanied by the university's name in bold black text.

In summary, the slide discusses the concept of calculating the area of a bounded region in the plane using double integrals, providing a mathematical formula and a visual representation through a graph.

### Slide 3

The image presents a problem related to the area of bounded regions in the plane, specifically asking to find the area enclosed by the parabola $y = x^2$ and the curve $y = x + 2$. The solution is broken down into steps, with the first step involving sketching the region R of integration and labeling all curves and intersections.

**Problem Statement:**

*   Find the area of the region R enclosed by the parabola $y = x^2$ and the curve $y = x + 2$.

**Solution:**

*   **Step 1:** Sketch the region R of integration and label all curves and intersections.

**Graphical Representation:**

*   The graph displays the parabola $y = x^2$ and the line $y = x + 2$.
*   The region R is bounded by these two curves.
*   The intersection points are labeled as (-1,1) and (2,4).
*   The x-axis and y-axis are also visible, with the x-axis labeled as "x" and the y-axis labeled as "y".

**Mathematical Formulation:**

*   The area A of the region R is given by the double integral $\iint_{R} dA$.
*   Two different methods are presented to evaluate this integral:
    *   $A = \int_{0}^{1} \int_{-\sqrt{y}}^{\sqrt{y}} dxdy + \int_{1}^{4} \int_{y-2}^{\sqrt{y}} dxdy$
    *   The expression $dydx$ is crossed out, indicating that it is not used in the solution.

**University Logo:**

*   The University of Waterloo logo is displayed in the bottom-right corner of the image.

### Slide 4

The image depicts a lecture slide from the University of Waterloo, focusing on the topic "Problem: Area of Bounded Regions in the Plane." The slide is divided into two main sections: a graph on the left and a set of equations on the right.

**Graph Section:**

*   The graph is a coordinate plane with x and y axes.
*   It features two curves: $y = x^2$ (a parabola) and $y = x + 2$ (a straight line).
*   The region bounded by these curves is shaded, with the limits of integration marked.
*   The points of intersection between the two curves are labeled as (-1, 1) and (2, 4).
*   Arrows indicate the direction of integration, with "ENTERS" and "LEAVES" annotations to clarify the order of integration.

**Equations Section:**

*   The equations are presented in a step-by-step format, illustrating the process of determining the area of the bounded region.
*   The first equation sets up the double integral for the area: $A = \int_{x=-1}^{x=2} \int_{y=x^2}^{y=x+2} dy dx$.
*   The second equation evaluates the inner integral: $A = \int_{-1}^{2} [y]_{x^2}^{x+2} dx$.
*   The third equation simplifies the expression: $A = \int_{-1}^{2} (x+2-x^2) dx$.
*   The fourth equation evaluates the integral: $A = [\frac{x^2}{2} + 2x - \frac{x^3}{3}]_{-1}^{2}$.
*   The final equation calculates the numerical value of the area: $A = \frac{9}{2}$.

**Additional Elements:**

*   The title "Problem: Area of Bounded Regions in the Plane" is displayed prominently at the top of the slide.
*   The subtitle "Step 2: Chose the order for dA and determine the limits of integration" provides context for the content.
*   The University of Waterloo logo is visible in the bottom-right corner, indicating the institution associated with the lecture.

### Slide 5

The image presents a slide from a lecture on calculus, specifically focusing on the concept of the average value of a function over a region. The title, "Average Value of $f(x,y)$ over a Region R," is prominently displayed at the top.

*   **Title and Equation**
    *   The title is in large black text.
    *   Below the title, the equation for the average value of $f(x,y)$ over a region R is given: $A_R = \frac{1}{\iint_R dA} \iint_R f(x,y)dA$.
*   **Graphical Representation**
    *   A graph illustrates a thin lamina R in the Cartesian coordinate system, with x and y axes labeled.
    *   The lamina is depicted as a blue outline, containing a small area dA around the point (x,y).
    *   The graph is accompanied by a red arrow pointing to the lamina, labeled "Thin Lamina."
*   **Practical Application**
    *   A section titled "Practical Application:" explains that if T(x,y) represents the temperature at (x,y) on the lamina, the average of T(x,y) over R gives the average temperature across the whole lamina.
*   **Copyright and University Information**
    *   At the bottom left, the copyright notice reads "Copyright © 2008 Pearson Education Canada."
    *   The University of Waterloo logo is displayed in the bottom-right corner, featuring a yellow shield with a black design and the university's name in black text.
*   **Background**
    *   The background of the slide is white, with a thick black bar at the top and a thin yellow stripe below it.

In summary, the slide effectively conveys the concept of the average value of a function over a region, providing a clear equation and graphical representation, along with a practical application and relevant copyright and university information.

### Slide 6

The image is a slide from a presentation on the topic of "Mass and Center of Mass of Thin Plates." The title is prominently displayed at the top, followed by a brief introduction that sets the context for the discussion.

*   **Title and Introduction**
    *   The title "Mass and Center of Mass of Thin Plates" is written in large black text.
    *   A brief introduction below the title explains that the distribution of mass is continuous over a thin plate, and the density is defined as $\delta(x,y) = \frac{mass}{unit area}$.
*   **Three Key Points**
    *   **1. Mass**
        *   The mass $M$ is given by the double integral $\iint_R \delta(x,y)dA$.
    *   **2. First Moments**
        *   The first moments $M_x$ and $M_y$ are defined as $\iint_R y\delta(x,y)dA$ and $\iint_R x\delta(x,y)dA$, respectively.
    *   **3. Center of Mass**
        *   The center of mass is located at $(\bar{x},\bar{y})$, where $\bar{x} = \frac{M_y}{M}$ and $\bar{y} = \frac{M_x}{M}$.
*   **Illustration**
    *   A simple illustration of a thin plate with a curved boundary is shown on the right side of the slide.
    *   The center of mass is marked with a small dot labeled $(\bar{x},\bar{y})$.
    *   The region $R$ is labeled accordingly.
*   **University Logo**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner of the slide.

In summary, the slide provides a concise overview of the concepts related to the mass and center of mass of thin plates, including the definition of density, the calculation of mass and first moments, and the determination of the center of mass. The accompanying illustration helps to visualize these concepts.

### Slide 7

The image presents a slide from a presentation on the "Moments of Inertia of Thin Plates" at the University of Waterloo.

**Title and Content**

* The title is prominently displayed in large, bold black text at the top of the slide.
* Below the title, four numbered points outline the moments of inertia for thin plates, each accompanied by a corresponding mathematical equation.

**Equations and Formulas**

1. **About the x-axis:**
   * Ix = ∫∫R y^2 δ(x,y) dA
2. **About the y-axis:**
   * Iy = ∫∫R x^2 δ(x,y) dA
3. **About a line L:**
   * IL = ∫∫R r^2(x,y) δ(x,y) dA
   * Where r(x,y) is the distance from (x,y) to L
4. **About the origin (Polar Moment):**
   * I0 = ∫∫R (x^2 + y^2) δ(x,y) dA = Ix + Iy

**Visual Elements**

* The slide features a white background with a black and yellow border at the top.
* The University of Waterloo's logo is displayed in the bottom-right corner, consisting of a shield with a red and yellow design, accompanied by the university's name in bold black text.

**Overall**

The slide provides a clear and concise overview of the moments of inertia for thin plates, including the relevant mathematical equations and formulas.

### Slide 8

The lecture slide, titled "Double Integrals in Polar Coordinates," presents a comprehensive overview of the topic. The title is prominently displayed in large, bold, black text at the top.

**Introduction and Explanation**

The slide begins by recalling that to specify the location of a point P(x, y) in the x-y plane in polar coordinates, we use its distance r from the origin and the angle θ made between the line segment from the origin to P(x, y) and the positive x-axis.

**Diagram and Equations**

A diagram is provided, illustrating the concept:

*   The diagram features a circle centered at the origin, with a point P(x, y) on its circumference.
*   The x and y axes are labeled, with the x-axis pointing to the right and the y-axis pointing upwards.
*   The radius r is drawn from the origin to point P, forming an angle θ with the positive x-axis.
*   The coordinates (x, y) are shown, with x being the horizontal distance from the y-axis and y being the vertical distance from the x-axis.
*   The diagram is accompanied by two equations:
    *   0 ≤ r ≤ ∞
    *   0 ≤ θ ≤ 2π

**Conversion to Polar Coordinates**

To convert a function f(x, y) from cartesian to polar coordinates, the following equations are used:

*   x = r cos θ
*   y = r sin θ
*   r² = x² + y²

These equations are presented in a bracketed format, with the three equations grouped together.

**University Logo**

In the bottom-right corner of the slide, the logo of the University of Waterloo is displayed, featuring a shield with a red and gold design, accompanied by the university's name in black text.

The slide's background is white, with a yellow stripe at the top and a black stripe above it, providing a clear and visually appealing format for the presentation.

### Slide 9

The image presents a slide from a lecture on double integrals in polar coordinates, featuring a graph and accompanying text.

*   The title "Double Integrals in Polar Coordinates" is prominently displayed at the top of the slide.
    *   The title is written in large black font.
*   A brief description below the title explains that when regions of integration are more easily described in polar coordinates, double integrals are used.
    *   The text is written in smaller black font.
*   A graph is centered on the slide, illustrating the concept of double integrals in polar coordinates.
    *   The graph features a coordinate system with x and y axes.
    *   Various lines and curves are plotted on the graph, including:
        *   A green curve labeled "r = h1(θ)".
        *   A blue curve labeled "r = h2(θ)".
        *   A purple line labeled "θ = β".
        *   A red dashed line.
        *   Several other lines and curves are present, but their labels are not clearly visible.
    *   The graph appears to be hand-drawn, with annotations and labels added in different colors.
*   To the right of the graph, a mathematical expression is written in blue ink.
    *   The expression reads: "We want to calculate ∫∫f(x,y)dA".
    *   The integral is taken over a region R, which is not explicitly defined on the slide.
*   In the bottom-right corner of the slide, the logo for the University of Waterloo is displayed.
    *   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.

In summary, the slide provides an introduction to double integrals in polar coordinates, including a graphical representation and a mathematical expression for calculating the integral over a region R.

### Slide 10

The image presents a detailed explanation of double integrals in polar coordinates, featuring a diagram and accompanying mathematical equations.

*   **Title**: "Double Integrals in Polar Coordinates"
    *   The title is prominently displayed at the top of the image.
*   **Subtitle**: "Zooming in the differential of area," 
    *   This subtitle is written below the title, providing context for the diagram that follows.
*   **Diagram**:
    *   The diagram illustrates the differential of area in polar coordinates, showcasing the relationship between the variables r, θ, and ΔA.
    *   The diagram includes labels for various components, such as r, Δr, Δθ, and dA, which are used to derive the formula for the double integral.
*   **Mathematical Equations**:
    *   The equations provided are used to derive the formula for the double integral in polar coordinates.
    *   The first equation, $\Delta r = r_o - r_i$, represents the difference between the outer and inner radii.
    *   The second equation, $If r_o \approx r_i = r$, indicates that when the outer and inner radii are approximately equal, they can be represented by a single value, r.
    *   The third equation, $\Delta A \approx r \Delta \theta \Delta r$, approximates the area of the region bounded by the radii and the angle Δθ.
    *   The fourth equation, $In the limit: dA = r dr d\theta$, represents the differential of area in polar coordinates.
    *   The final equation, $\iint_R f(x,y) dA = \iint_R f(r \cos \theta, r \sin \theta) . r dr d\theta$, demonstrates how to convert a double integral from Cartesian coordinates to polar coordinates.
*   **University Logo**:
    *   The logo of the University of Waterloo is displayed at the bottom right corner of the image.

In summary, the image provides a clear and concise explanation of double integrals in polar coordinates, including a diagram and relevant mathematical equations. The content is suitable for an educational setting, such as a lecture slide, and is attributed to the University of Waterloo.

### Slide 11

The image presents a slide from a presentation on double integrals in polar coordinates, featuring a title, explanatory text, and a diagram.

*   **Title**
    *   The title is "Double Integrals in Polar Coordinates."
*   **Explanatory Text**
    *   The text below the title reads: "The limits of integration are determined in a similar but different way as the ones determined for cartesian coordinates."
*   **Diagram**
    *   The diagram is a graph with x and y axes.
    *   It includes several lines and curves:
        *   A red line labeled "L" extends from the origin to the upper right.
        *   Two green curves are labeled "r = h1(θ)" and "r = h2(θ)."
        *   Two purple lines are labeled "θ = α" and "θ = β."
        *   The area between the two green curves is shaded.
        *   The text "ENTERS" and "LEAVES" is written near the curves.
*   **Mathematical Equations**
    *   The equation ∫[α,β] ∫[h1(θ),h2(θ)] f(r cos θ, r sin θ) r dr dθ is displayed.
*   **University Logo**
    *   The logo of the University of Waterloo is shown in the bottom-right corner.

The slide provides a concise overview of double integrals in polar coordinates, including a diagram illustrating the concept and the relevant mathematical equation.

### Slide 12

The image is a slide from a presentation on double integrals, featuring a white background with a black and yellow border at the top. The title "Summary" is prominently displayed in bold, black font.

*   **Title and Bullet Points**
    *   The main content of the slide is presented in four bullet points:
        *   The first bullet point discusses the application of double integrals to calculate various physical problems, such as area, center of mass, and moment of inertia, for a thin plate covering a region in the plane.
        *   The second bullet point explains how to change double integrals to polar coordinates and evaluate them over regions bounded by polar equations.
        *   The third bullet point serves as a reminder that in polar coordinates, the element of area dA is not replaced by drdθ but by dA = r drdθ.
*   **University Logo**
    *   In the bottom-right corner, the logo of the University of Waterloo is displayed, featuring a shield with a red and yellow design, accompanied by the university's name in black text.
*   **Visual Elements**
    *   The slide includes a combination of black text and blue text, with the equation dA = r drdθ highlighted in blue.

In summary, the slide provides a concise overview of the key concepts related to double integrals, including their application to physical problems, conversion to polar coordinates, and the correct representation of the element of area in polar coordinates.

### Slide 13

The image is a slide from a presentation, likely the final slide, with a white background and a black and gold border at the top. The main content of the slide is centered around the University of Waterloo logo and a message of appreciation.

*   **University of Waterloo Logo**
    *   Located on the left side of the image
    *   Features a yellow shield with a red lion on either side
    *   A black chevron shape is positioned between the lions
    *   The text "UNIVERSITY OF WATERLOO" is written in bold, black font to the right of the logo
*   **Thank You Message**
    *   Displayed prominently below the logo and university name
    *   Written in bold, black font
    *   Reads "Thank you"

The slide appears to be a concluding slide, expressing gratitude to the audience.

