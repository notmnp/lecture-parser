# Lecture 23 - Double Integrals and Double Iterated Integrals

## Study Notes

# Double Integrals – Problem‑Solving Exam Notes

---

## Core Formulas & Definitions

| Formula | Symbols | When to Use |
|---------|---------|-------------|
| **Iterated integral over a rectangle**<br>$$\iint_R f(x,y)\,dA = \int_a^b\int_c^d f(x,y)\,dy\,dx$$ | $R=[a,b]\times[c,d]$ – rectangular base<br>$f(x,y)$ – integrand<br>$dy\,dx$ – order of integration | Compute volume under a surface over a rectangle |
| **General region – Type 1**<br>$$R=\{(x,y)\mid a\le x\le b,\;g_1(x)\le y\le g_2(x)\}$$<br>$$\iint_R f(x,y)\,dA = \int_a^b\int_{g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx$$ | $g_1,g_2$ – lower/upper bounds as functions of $x$ | Region bounded on top/bottom by curves, side limits fixed |
| **General region – Type 2**<br>$$R=\{(x,y)\mid c\le y\le d,\;h_1(y)\le x\le h_2(y)\}$$<br>$$\iint_R f(x,y)\,dA = \int_c^d\int_{h_1(y)}^{h_2(y)} f(x,y)\,dx\,dy$$ | $h_1,h_2$ – lower/upper bounds as functions of $y$ | Region bounded on left/right by curves, top/bottom limits fixed |
| **Union of sub‑regions**<br>$$R=R_1\cup R_2,\qquad R_1\cap R_2=\varnothing$$<br>$$\iint_R f(x,y)\,dA = \iint_{R_1} f(x,y)\,dA+\iint_{R_2} f(x,y)\,dA$$ | Split a complicated region into simpler pieces | Needed when $R$ is neither Type 1 nor Type 2 |
| **Fubini’s Theorem**<br>$$\iint_R f(x,y)\,dA=\int_a^b\int_c^d f(x,y)\,dy\,dx=\int_c^d\int_a^b f(x,y)\,dx\,dy$$ | $f$ continuous on $R$ | Swap integration order; choose the one that simplifies the inner integral |
| **Volume under a surface**<br>$$V=\iint_R f(x,y)\,dA$$ | $f(x,y)$ – height function $z$ above $R$ | Physical volume problems where $z$ is given by a surface |

---

## Key Concepts & Intuition

- **Iterated integrals** transform a 2‑D accumulation into two 1‑D operations.  
- **Type 1 vs. Type 2**: choose the order that makes the bounds *constant* in the outer integral.  
- **Non‑rectangular regions** are handled by expressing limits as functions of the other variable.  
- **Splitting a region** is essential when the boundaries change direction or when the region is irregular.  
- **Reversing the order** can reduce algebraic complexity or avoid difficult integrands.  
- **Fubini’s Theorem** guarantees equivalence for continuous $f$; verify continuity before swapping.

---

## Problem‑Solving Strategies

| Problem | Typical Cues | Checklist / Steps |
|---------|--------------|-------------------|
| **Volume of a solid with a given surface** | “volume”, “top surface”, “plane”, “z = …” | 1. Identify base region $R$ in $xy$‑plane.<br>2. Write height function $z = g(x,y)$ from the surface equation.<br>3. Choose region type (1 or 2) that yields simple bounds.<br>4. Set up iterated integral $V=\iint_R g(x,y)\,dA$. |
| **Set up a double integral over a non‑rectangular region** | “region bounded by …”, “curves”, “limits given as functions” | 1. Sketch the region.<br>2. Decide if a Type 1 or Type 2 description is simpler.<br>3. Write bounds for the outer variable (constant limits).<br>4. Write inner bounds as functions of the outer variable. |
| **Reverse order of integration** | “reverse”, “change order”, “different bounds” | 1. Sketch the region.<br>2. Identify new bounds for the opposite variable.<br>3. Write the reversed iterated integral.<br>4. Evaluate; compare complexity to original order. |
| **Integrate over a union of sub‑regions** | “non‑rectangular”, “split”, “R = R₁∪R₂” | 1. Decompose $R$ into simpler parts (often each part is Type 1 or Type 2).<br>2. Set up an integral for each sub‑region.<br>3. Add the results. |
| **Check continuity / applicability of Fubini** | “piecewise”, “discontinuous” | 1. Verify $f$ is continuous on $R$.<br>2. If not, split region further or use absolute convergence test. |

### Example Workflow: Volume of a Triangular Prism

**Given**  
- Base: triangle with vertices $(0,0),(1,0),(1,1)$ (bounded by $x$‑axis, $y=x$, $x=1$).  
- Top surface: plane $x+y+z=3$ → $z=3-x-y$.

**Step 1: Choose order**  
- Type 1: $0\le x\le 1$, $0\le y\le x$.  
- Type 2: $0\le y\le 1$, $y\le x\le 1$.

**Step 2: Write integral** (using Type 1)  
$$V=\int_{0}^{1}\int_{0}^{x}\bigl(3-x-y\bigr)\,dy\,dx$$

**Step 3: Inner integral**  
$$\int_{0}^{x}(3-x-y)\,dy = 3y - xy - \tfrac12 y^2\Big|_{0}^{x} = 3x - x^2 - \tfrac12 x^2 = 3x - \tfrac32 x^2$$

**Step 4: Outer integral**  
$$V=\int_{0}^{1}\left(3x-\tfrac32x^2\right)\,dx = \tfrac32x^2-\tfrac12x^3\Big|_{0}^{1}= \tfrac32-\tfrac12=1$$

**Result** – volume = **1** cubic unit.  
*(If reversed order: $V=\int_{0}^{1}\int_{y}^{1}(3-x-y)\,dx\,dy$ gives the same result with a slightly different algebraic path.)*

---

## Common Pitfalls & Checks

- **Wrong bounds**: Always sketch the region and double‑check that limits exactly match the described shape.
- **Mixed up order**: If bounds are written as functions of the *wrong* variable, the inner integral will be impossible or produce incorrect limits.
- **Sign errors**: Keep track of negative signs, especially when integrating linear terms.
- **Skipping the height function**: For volume problems, forget to express $z$ in terms of $x,y$ (e.g., from a plane equation).
- **Assuming Fubini without continuity**: Piecewise or discontinuous $f$ may violate Fubini; split the region or use a convergence test.
- **Over‑splitting**: Splitting into sub‑regions is only needed if the bounds change; unnecessary splitting makes the problem harder.
- **Units**: For volume, confirm that $f(x,y)$ indeed represents a height; if it's a density, multiply by area element appropriately.

---

### Quick Exam Checklist

1. **Identify** region $R$ and integrand $f(x,y)$.  
2. **Determine** if $R$ is rectangular, Type 1, Type 2, or needs splitting.  
3. **Choose** integration order that keeps outer limits constant.  
4. **Set up** iterated integral(s).  
5. **Integrate** inner first (treat other variable as constant).  
6. **Integrate** outer next.  
7. **Verify** bounds, signs, and final answer.  

Follow this workflow, and you’ll tackle any double‑integral problem efficiently.

---

## Raw Slide Summaries

### Slide 1

The image presents a slide from a presentation on multiple integrals, specifically focusing on double integrals. The title "Multiple Integrals - Double Integrals" is prominently displayed in large black text at the top of the slide.

**Title and Reference**
* Title: Multiple Integrals - Double Integrals
* Reference: Trim Ch 13, S. 13.1, 13.2 (highlighted in yellow)

**Outline**
The slide outlines three key topics related to double integrals:
1. Double Integrals over rectangles
2. Double Iterated Integrals (Fubini's Theorem)
3. Evaluation of Double Integrals by Double Iterated Integrals

**Institutional Affiliation**
The slide is affiliated with the University of Waterloo, as indicated by the logo in the bottom-left corner. The logo features a shield with a red and gold design, accompanied by the university's name in bold black text.

**Background and Design**
The slide has a clean white background, with a thick black bar at the top and a thinner yellow bar below it, creating a visually appealing contrast.

### Slide 2

The image presents a slide from a presentation on the topic of "Double Integral over Rectangles," likely from a mathematics course at the University of Waterloo. The slide is divided into several sections, each containing various elements that convey information about the concept.

**Title and Introduction**

*   The title "Double Integral over Rectangles" is prominently displayed in large black text at the top of the slide.
*   A question is posed below the title: "Do you remember when in the process of finding the area under a curve we arrived at the definition of integrals?" This suggests that the presentation is building upon previously covered material.

**Graph and Mathematical Expressions**

*   A graph is shown, illustrating a function y = f(x) over the interval [a, b]. The graph features a curved line representing the function, with several vertical lines and points labeled along the x-axis.
*   The x-axis is labeled with points a, x1, x2, xi-1, xi, and b, indicating a partition of the interval [a, b] into subintervals.
*   The y-axis is labeled with the function y = f(x), and a point on the graph is marked as f(xi*), suggesting the use of a Riemann sum to approximate the area under the curve.
*   Below the graph, a mathematical expression is written: A = lim n→∞ Σ f(xi*) Δx = ∫[a, b] f(x) dx. This represents the definition of a definite integral as the limit of a Riemann sum.

**Additional Text and Logo**

*   The text "To calculate the area, we used a Riemann sum" is written below the graph, providing context for the mathematical expression.
*   In the bottom-right corner of the slide, the logo for the University of Waterloo is displayed, indicating the institution associated with the presentation.

In summary, the slide provides a review of the concept of definite integrals and Riemann sums, setting the stage for the discussion of double integrals over rectangles. The graph and mathematical expressions work together to illustrate the definition of a definite integral, while the additional text and logo provide context and attribution.

### Slide 3

The image presents a slide from a lecture on double integrals over rectangles, featuring a title, a brief introduction, and a diagram illustrating the concept.

*   **Title and Introduction**
    *   The title "Double Integral over Rectangles" is prominently displayed in large black text at the top of the slide.
    *   Below the title, a sentence explains that the lecture will explore finding the volume under a surface and define double integrals.
*   **Diagram**
    *   The diagram is a 3D graph with x, y, and z axes, showcasing a rectangular region R in the xy-plane and a surface S defined by the function z = f(x,y).
    *   The region R is bounded by the lines x = a, x = b, y = c, and y = d, forming a rectangle.
    *   The surface S is represented by a curved surface above the region R, with the function f(x,y) defining its height at each point (x,y) within R.
    *   A sample point (x*,y*) is marked within the region R, and the corresponding value of the function f(x*,y*) is indicated on the surface S.
    *   The diagram also includes annotations such as "ΔA" and "f(x*,y*)" to highlight key elements of the concept being illustrated.
*   **University Logo**
    *   In the bottom-right corner of the slide, the logo of the University of Waterloo is displayed, indicating the institution associated with the lecture.

In summary, the slide provides a clear and concise introduction to the topic of double integrals over rectangles, accompanied by a visual representation that helps to illustrate the underlying mathematical concepts.

### Slide 4

The image displays a lecture slide on the topic of "Double Integral over Rectangles." The slide is divided into three sections, each containing mathematical equations and text. The title is prominently displayed in large black font at the top of the slide.

*   **Title**
    *   "Double Integral over Rectangles" in large black font
*   **First Section**
    *   Text: "The volume under a surface can be expressed as another Riemann sum,"
    *   Equation: $V = \sum_{i=1}^{n} \sum_{j=1}^{m} f(x_{ij}^{*}, y_{ij}^{*}) \cdot \Delta A$
*   **Second Section**
    *   Text: "Which in the limit gives us the exact volume under the surface,"
    *   Equation: $V = \lim_{m,n \to \infty} \sum_{i=1}^{n} \sum_{j=1}^{m} f(x_{ij}^{*}, y_{ij}^{*}) \cdot \Delta A = \iint_{R} f(x,y)dA$
*   **Third Section**
    *   Text: "$\iint_{R} f(x,y)dA$ is called the double integral of $f(x,y)$ over the region $R$"
*   **Logo**
    *   University of Waterloo logo in the bottom-right corner

The slide provides a clear and concise explanation of the concept of double integrals over rectangles, including the definition and a visual representation of the Riemann sum. The use of mathematical equations and notation adds precision and clarity to the explanation. Overall, the slide effectively communicates the key concepts and ideas related to double integrals over rectangles.

### Slide 5

The image presents a slide from a presentation on calculus, specifically focusing on Fubini's Theorem for calculating double integrals. The title "Calculating Double Integrals - Fubini's Theorem" is prominently displayed at the top.

*   **Title and Subtitle**
    *   The title is in large black text.
    *   Below the title, there is a subtitle that reads: "If $f(x,y)$ is continuous on $R = [a,b] \times [c,d]$, then"
*   **Equations**
    *   Two equations are provided, each representing Fubini's Theorem.
    *   The first equation is: $\iint_R f(x,y)dA = \int_a^b \int_c^d f(x,y) dy dx$
    *   The second equation is: $\iint_R f(x,y)dA = \int_c^d \int_a^b f(x,y) dx dy$
    *   The inner integrals are highlighted in red, with the label "INNER INTEGRAL" written above them.
*   **Explanation**
    *   A paragraph below the equations explains that these integrals are called iterated integrals and that Fubini's Theorem allows for the calculation of double integrals in either order.
*   **Logo and University Name**
    *   In the bottom-right corner, there is a logo accompanied by the text "UNIVERSITY OF WATERLOO".
*   **Background**
    *   The background of the slide is white, with a yellow and black border at the top.

In summary, the image effectively illustrates Fubini's Theorem for calculating double integrals, providing a clear and concise explanation of the concept along with relevant equations and a university logo.

### Slide 6

The image displays a slide from a presentation on calculus, specifically focusing on the calculation of a double integral. The title "Example - Calculation of a Double Integral" is prominently displayed at the top.

*   The main equation is presented as:
    *   $\iint_{R} f(x,y)dA$
    *   where $f(x,y) = 1 - 6x^2y$ and $R: 0 \leq x \leq 2, -1 \leq y \leq 1$
*   The solution involves determining the limits of integration when $dA = dxdy$.
    *   $I = \int_{-1}^{1} \int_{0}^{2} (1-6x^2y) dx dy$
    *   $I = \int_{-1}^{1} [\int_{0}^{2} (1-6x^2y) dx] dy$
    *   $INNER INTEGRAL$
*   A graph is shown to the right of the equations, illustrating the region of integration.
    *   The x-axis ranges from -1 to 2.
    *   The y-axis ranges from -1 to 1.
    *   The region $R$ is bounded by the lines $x=0$, $x=2$, $y=-1$, and $y=1$.
*   The University of Waterloo logo is displayed in the bottom-right corner.

In summary, the slide provides a step-by-step example of calculating a double integral over a rectangular region, with a clear explanation of the process and a visual representation of the region of integration.

### Slide 7

The image presents a slide from a presentation on calculus, specifically focusing on the calculation of a double integral. The title "Example - Calculation of a Double Integral" is prominently displayed at the top.

*   **Title and Banner**
    *   The title is centered in large black text.
    *   A yellow banner with a black border is situated above the title.
*   **Mathematical Equations**
    *   A series of mathematical equations are written in blue ink below the title.
    *   The equations appear to be solving a double integral problem.
    *   The equations are as follows:
        *   I = ∫(-1 to 1) [x - 6y(x^3)/3] from 0 to 2 dy
        *   I = ∫(-1 to 1) [{2 - 6y(2)^3/3} - 0] dy
        *   I = ∫(-1 to 1) (2 - 16y) dy = [2y - 16(y^2)/2] from -1 to 1
        *   = 4
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner.
    *   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.

In summary, the image showcases a step-by-step solution to a double integral problem, with the final answer being 4. The slide is likely part of a larger presentation on calculus, and the University of Waterloo logo indicates that it may be from a lecture or educational resource provided by the institution.

### Slide 8

The image presents a slide from a presentation on double integrals, featuring a title and a mathematical problem. The title, "Problem - Calculation of a Double Integral," is prominently displayed in large black text at the top of the slide.

*   **Title**
    *   The title is centered and written in bold, black font.
    *   It reads: "Problem - Calculation of a Double Integral"
*   **Subtitle**
    *   Below the title, a subtitle is provided in smaller black text.
    *   It states: "Determining the limits of integration for dA = dydx"
*   **Mathematical Problem**
    *   A mathematical problem is presented, involving a double integral.
    *   The integral is written as: I = ∫[0,2] ∫[-1,1] (1-6x^2y) dy dx
    *   The inner integral is highlighted with a red underline and labeled "INNER INTEGRAL"
    *   A smiley face is drawn next to the label, accompanied by the text "FOR YOU"
*   **Graph**
    *   A graph is displayed on the left side of the slide, illustrating the region of integration.
    *   The graph features a green rectangle labeled "R" with coordinates (0,-1), (2,-1), (2,1), and (0,1).
    *   A red line is drawn from the point (1,-1) to (1,1), intersecting the rectangle.
    *   The x-axis and y-axis are labeled, with the x-axis ranging from 0 to 2 and the y-axis ranging from -1 to 1.
*   **University Logo**
    *   In the bottom-right corner, the logo of the University of Waterloo is displayed.
    *   The logo features a shield with a yellow and red design, accompanied by the university's name in black text.

In summary, the slide presents a mathematical problem involving a double integral, along with a graph illustrating the region of integration. The problem requires determining the limits of integration for the given function.

### Slide 9

The image presents a slide from a lecture on double integrals, specifically focusing on general regions. The title "Double Integral over General Regions" is prominently displayed at the top, followed by a concise introduction that sets the context for the discussion.

**Key Points:**

*   **Introduction**
    *   The slide begins by acknowledging that most regions of integration are not rectangular.
    *   It then introduces the concept of considering the integral over a region R in the x-y plane.
*   **Mathematical Representation**
    *   The double integral over the region R is represented as $\iint_{R} f(x,y)dA$.
    *   The slide explains that there are two types of general R regions over which integration will be performed.
*   **Region Type 1**
    *   Region Type 1 is defined as $R = \{(x,y)|a \leq x \leq b, g_1(x) \leq y \leq g_2(x)\}$.
    *   A graph illustrates this concept, showing the boundaries of the region and the functions $g_1(x)$ and $g_2(x)$.
    *   The integral over Region Type 1 is expressed as $\int_{a}^{b} \int_{g_1(x)}^{g_2(x)} f(x,y) dy dx$.
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

In summary, the slide provides a clear and concise introduction to double integrals over general regions, defining Region Type 1 and illustrating its representation through a graph and mathematical notation.

### Slide 10

The slide is titled "Double Integral over General Regions" and features a diagram and equation related to Region Type 2.

**Title and Definition**

* The title "Double Integral over General Regions" is prominently displayed at the top of the slide.
* Below the title, the definition of Region Type 2 is given as: R = {(x,y) | h1(y) ≤ x ≤ h2(y), c ≤ y ≤ d}

**Diagram**

* The diagram is a graph with x and y axes, featuring:
	+ A blue y-axis on the left and a blue x-axis at the bottom.
	+ Two green curves labeled x = h1(y) and x = h2(y), representing the lower and upper bounds of the region R, respectively.
	+ A red horizontal line segment within the region, labeled "ENTERS R" at the left end and "LEAVES" at the right end.
	+ The region R is bounded by the two green curves and the horizontal lines y = c and y = d.

**Equation**

* The equation for the double integral over Region Type 2 is given as: I = ∫[c,d] (∫[h1(y),h2(y)] f(x,y) dx) dy
* The inner integral is labeled "INNER" and has limits of integration from x = h1(y) to x = h2(y).

**Additional Labels and Notations**

* The diagram includes additional labels and notations, such as:
	+ The label "d" on the y-axis, corresponding to the upper limit of integration.
	+ The label "c" on the y-axis, corresponding to the lower limit of integration.
	+ The notation "x = h2(y)" above the upper green curve.
	+ The notation "x = h1(y)" below the lower green curve.

**University Logo**

* The University of Waterloo logo is displayed in the bottom-right corner of the slide.

Overall, the slide provides a clear and concise explanation of double integrals over general regions, specifically Region Type 2, along with a diagram and equation to illustrate the concept.

### Slide 11

The image presents a slide from a lecture on double integrals over general regions, featuring a title, a diagram, and an equation. The content can be broken down into the following components:

*   **Title and Subtitle**
    *   The title "Double Integral over General Regions" is prominently displayed at the top of the slide.
    *   Below the title, the subtitle "Regions that are neither Type 1 or Type 2:" provides context for the discussion that follows.
*   **Text Explanation**
    *   The accompanying text explains that certain regions can be expressed as the union of two or more regions, denoted as $R_1 \cup R_2$.
*   **Diagram**
    *   A graph is shown with two axes, x and y, and a green outline representing the region $R$, which is divided into two sub-regions, $R_1$ and $R_2$, by a vertical dashed line.
    *   The region $R$ is irregularly shaped, with $R_1$ and $R_2$ being distinct parts of it.
*   **Equation**
    *   The equation $\iint_R f(x,y) dA = \iint_{R_1} f(x,y) dA + \iint_{R_2} f(x,y) dA$ is written below the graph, illustrating how to calculate the double integral over the region $R$ by breaking it down into the integrals over $R_1$ and $R_2$.
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner of the slide, indicating the institution associated with the lecture.

In summary, the slide discusses how to handle regions that are neither Type 1 nor Type 2 when evaluating double integrals, by breaking them down into simpler regions and summing the integrals over these sub-regions.

### Slide 12

The image presents a mathematical problem and its solution, specifically focusing on finding the volume of a solid. The problem is titled "Problem - Finding the Volume of a Solid" and is accompanied by a diagram illustrating the solid in question.

*   **Problem Statement:**
    *   The task is to determine the volume of a prism with a triangular base in the x-y plane.
    *   The base is bounded by the x-axis and the lines y = x and x = 1.
    *   The top of the prism lies on the plane defined by the equation x + y + z = 3.
*   **Solution:**
    *   **Step 1:** Sketch the solid and the region R of integration, labeling all curves and intersections.
    *   A 3D graph is provided, showing the solid and its boundaries.
    *   The graph includes labels for the axes (x, y, z), the lines y = x and x = 1, and the plane x + y + z = 3.
    *   The vertices of the triangular base are marked as (0,0), (1,0), and (1,1).
    *   The top surface of the prism is shown intersecting the plane x + y + z = 3.
    *   The z-axis is labeled with the value 3 at the top, indicating the height of the prism.
*   **Additional Information:**
    *   The University of Waterloo logo is displayed in the bottom-right corner of the image.

In summary, the image presents a mathematical problem involving the calculation of the volume of a prism with a triangular base and a top surface defined by a specific plane. The solution involves sketching the solid and identifying the region of integration, followed by labeling the relevant curves and intersections. The provided graph illustrates the solid and its boundaries, facilitating the understanding of the problem and its solution.

### Slide 13

The slide is titled "Problem - Finding the Volume of a Solid" and has a white background with a black and yellow bar at the top. The University of Waterloo logo is visible in the bottom-right corner.

*   The title is prominently displayed in large, bold black text.
*   Below the title, there are two steps outlined:
    *   **Step 2: Chose the order for dA and determine the limits of integration**
        *   A graph is shown with a green line representing a function, likely y = x, on a standard Cartesian coordinate system with x and y axes.
        *   The graph has a blue y-axis and x-axis, with a green dashed line indicating a specific y-value.
        *   The region of interest appears to be bounded by the green line, the y-axis, and the dashed green line.
    *   **Step 3: Perform the integration**
        *   No additional information or equations are provided for this step on the slide.

The slide appears to be part of a presentation on solving problems related to finding the volume of a solid, likely in the context of calculus, specifically using integration.

### Slide 14

The image is a slide from a presentation on calculus, specifically focusing on the problem of finding the volume of a solid.

*   **Title**: The title of the slide is "Problem - Finding the Volume of a Solid" in bold black text.
    *   It is centered at the top of the slide and written in large font.
*   **Subtitle**: Below the title, there is a subtitle that reads, "What happens if we were to reverse the order of integration?"
    *   This text is in smaller black font compared to the title.
*   **Graph**: On the left side of the slide, there is a graph with x and y axes.
    *   The x-axis is horizontal, and the y-axis is vertical.
    *   There are two lines on the graph: one green diagonal line and one blue vertical line.
    *   The green line starts at the origin (0, 0) and slopes upward to the right.
    *   The blue line is parallel to the y-axis and intersects the x-axis at a point between 0 and 1.
    *   There is a dotted horizontal line that represents the upper limit of integration.
*   **University Logo**: In the bottom-right corner of the slide, there is a logo for the University of Waterloo.
    *   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.

In summary, the slide presents a problem related to reversing the order of integration when finding the volume of a solid, accompanied by a graph illustrating the concept. The University of Waterloo's logo is displayed in the bottom-right corner.

### Slide 15

The image presents a summary slide related to double integrals, featuring a white background with black text and a yellow stripe at the top. The content is organized into three main bullet points, which are described below:

*   **Title and First Bullet Point**
    *   The title "Summary" is prominently displayed in large, bold font at the top left of the slide.
    *   The first bullet point states, "We have defined the double integral over a rectangle while attempting to solve a volume problem."
    *   Below this statement, the equation for the volume is given as $V = \iint_{R} f(x,y)dA$.
*   **Second Bullet Point**
    *   The second bullet point reads, "Fubini's Theorem says that we may calculate a double iterated integral in either order, $dydx$ or $dxdy$."
*   **Logo and Institution**
    *   In the bottom-right corner of the slide, the logo for the University of Waterloo is displayed, accompanied by the institution's name in black text.

In summary, the slide provides a concise overview of double integrals, highlighting their definition and application in solving volume problems, as well as Fubini's Theorem, which allows for the calculation of double iterated integrals in either order.

