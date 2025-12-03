# Lecture 20 - Relative Maxima and Minima

## Study Notes

# Relative Extrema of Multivariable Functions – Problem‑Solving Exam Notes  

---

## Core Formulas & Definitions  

| Symbol | Meaning | Typical Usage |
|--------|---------|---------------|
| \(f:\mathbb R^2\to\mathbb R\) | Bivariate function | Every problem |
| \(\nabla f(a,b)=\bigl(f_x(a,b),f_y(a,b)\bigr)\) | Gradient vector | Find critical points |
| \((a,b)\) with \(f_x(a,b)=f_y(a,b)=0\) | **Critical point** | Candidate for extremum or saddle |
| \(f_{xx},\,f_{yy},\,f_{xy}=f_{yx}\) | Second partial derivatives | Build the Hessian |
| \(D(a,b)=f_{xx}f_{yy}-f_{xy}^2\) | **Hessian determinant** | Classify critical points |
| **Classification rules** | • \(D>0,\ f_{xx}>0\) → local minimum  <br>• \(D>0,\ f_{xx}<0\) → local maximum  <br>• \(D<0\) → saddle  <br>• \(D=0\) → inconclusive | Apply after computing \(D\) and \(f_{xx}\) |
| **Gradient‑direction test** | • Gradients point *toward* CP → local maximum  <br>• Gradients point *away* from CP → local minimum  <br>• Gradients mixed → saddle | Quick visual check with contour plot |
| **Contour behavior** | • Contours tighten toward CP → local minimum  <br>• Contours widen away from CP → local maximum  <br>• Contours change direction → saddle | Visual confirmation |

---

## Key Concepts & Intuition  

- **Critical point**: point where the tangent plane is horizontal (all first derivatives zero) or where the function is not differentiable.  
- **First‑derivative test**: set \(\nabla f=0\).  
- **Second‑derivative test**: use the Hessian determinant \(D\) and \(f_{xx}\) to capture curvature.  
- **Gradient direction**: in a small neighbourhood, the vector \(\nabla f\) points in the direction of greatest increase.  
  - At a *maximum*, \(\nabla f\) points *toward* the CP.  
  - At a *minimum*, \(\nabla f\) points *away* from the CP.  
  - Mixed behaviour indicates a *saddle*.  
- **Contours**: level curves of \(f\). Their shape around a CP mirrors the gradient behaviour (tightening = minimum, widening = maximum, mixed = saddle).  
- **Boundaries**: extrema may also occur on the domain boundary; treat separately (parameterisation or Lagrange multipliers).

---

## Problem‑Solving Strategies  

1. **Locate critical points**  
   - Compute \(f_x,\;f_y\).  
   - Solve \(f_x=0,\;f_y=0\).  
   - Check points where a partial derivative does **not** exist.  
   - *Cue*: “critical point”, “stationary point”, “gradient zero”.

2. **Classify each critical point**  
   - Compute \(f_{xx},\;f_{yy},\;f_{xy}\).  
   - Evaluate \(D=f_{xx}f_{yy}-f_{xy}^2\).  
   - Apply the classification rules.  
   - *If \(D=0\)*: use higher‑order terms or sign analysis in a neighbourhood.  

3. **Use the gradient‑direction test (optional but fast)**  
   - Sample \(\nabla f\) slightly inside a small square around the CP.  
   - Observe whether vectors point toward, away, or in mixed directions.  
   - *Cue*: “gradient arrows on contour plot”.

4. **Confirm with contour behaviour (if a plot is available)**  
   - Look for tightening, widening, or changing direction of level curves.  
   - Match with algebraic classification.

5. **Check boundary extrema (if domain is bounded)**  
   - Parameterise the boundary or apply Lagrange multipliers.  
   - Evaluate \(f\) on the boundary and compare with interior points.  

6. **Compile results**  
   - List each point, its classification, and the corresponding function value (if needed).  
   - State whether it is a *local* or *global* extremum based on the domain.

---

## Common Pitfalls & Quick Checks  

| Pitfall | Why it happens | Quick Check |
|---------|----------------|-------------|
| Omitting points where a derivative fails to exist | Gradient may not exist but still be a critical point | Explicitly test points where \(f_x\) or \(f_y\) is undefined |
| Sign error in \(D\) or \(f_{xx}\) | Algebraic slip | Re‑differentiate or use CAS; test on simple cases like \(f=x^2+y^2\) |
| Confusing max/min rule for \(D>0\) | Misremembering the sign of \(f_{xx}\) | Write the rule before solving; verify with \(f=x^2-y^2\) |
| Ignoring boundary extrema | Domain constraints overlooked | After classifying interior points, evaluate \(f\) on the boundary |
| Assuming \(D=0\) → “no answer” | Test is inconclusive | Examine higher‑order terms or check the sign of \(f\) around the point |
| Misreading contour behaviour | Visual ambiguity | Check both the direction of gradient arrows and the shape of level curves |

---

### Quick Example (Checklist)

1. **Given** \(f(x,y)=x^4+y^4-4xy+1\).  
2. *Critical points*: solve \(f_x=4x^3-4y=0,\ f_y=4y^3-4x=0\) → \((0,0),\,(1,1),\,(-1,-1)\).  
3. *Second derivatives*: \(f_{xx}=12x^2,\ f_{yy}=12y^2,\ f_{xy}=-4\).  
4. *Determinants*: \(D=144x^2y^2-16\).  
5. *Classification*: \((0,0)\) → \(D=-16<0\) → saddle; \((\pm1,\pm1)\) → \(D>0,\ f_{xx}>0\) → local minima.  
6. *Contour check*: contours tighten around \((\pm1,\pm1)\), open at \((0,0)\).  

---

*These concise, step‑by‑step rules should cover all typical exam questions on relative extrema for functions of two variables.*

---

## Raw Slide Summaries

### Slide 1

The image presents a slide from a lecture on multivariable functions, specifically focusing on relative maxima and minima. The title, "Relative Maxima and Minima of Multivariable Functions," is prominently displayed at the top in large black text.

**Title Section:**

* Title: "Relative Maxima and Minima of Multivariable Functions"
* Yellow rectangle with text: "Trim Ch 11, S. 12.10"

**Outline:**

* 1. Critical Points
* 2. Classifying Critical Points

**Image:**

* A white drone is shown flying in the sky, with a blue sky and clouds in the background.
* The drone is labeled with a blue diagram, indicating its dimensions:
	+ x
	+ y
	+ z
* A URL is provided below the image: https://www.shutterstock.com/image-photo/unmanned-aircraft-system-uas-quadcopter-drone-1027003081
* A handwritten equation is written below the image: V(x,y,z) = xyz

**University Logo:**

* The University of Waterloo logo is displayed in the bottom-left corner, featuring a yellow shield with a red design and the university's name in black text.

Overall, the slide appears to be introducing the concept of relative maxima and minima in multivariable functions, with a visual representation of a drone and its dimensions.

### Slide 2

The image presents a slide from a lecture on multivariable functions, specifically focusing on relative maxima and minima. The title, "Relative Maxima and Minima of Multivariable Functions," is prominently displayed at the top.

**Visual Elements:**

* A 3D graph is centered in the image, showcasing a surface with multiple peaks and valleys.
* The graph is labeled with various points, including (a, b), (c, d), and (x, y), accompanied by corresponding z-values.
* Arrows and annotations are used to highlight specific features of the graph, such as the maximum and minimum values.

**Key Concepts:**

* The slide emphasizes that a relative maximum or minimum is not necessarily the largest or smallest value that the function will ever take.
* The graph illustrates this concept by showing multiple local maxima and minima, with annotations explaining their significance.

**Mathematical Notations:**

* The slide includes mathematical notations, such as f(x, y) and f(a, b), which represent the function and its values at specific points.
* The notation "No larger values of f(x, y) nearby f(a, b) ≥ f(x, y)" indicates that the point (a, b) is a local maximum, while "No smaller values of f(x, y) are nearby f(c, d) ≤ f(x, y)" indicates that the point (c, d) is a local minimum.

**Institutional Affiliation:**

* The University of Waterloo logo is displayed in the bottom-right corner of the image, indicating the institution responsible for the lecture.

Overall, the image provides a clear and concise visual representation of the concepts related to relative maxima and minima of multivariable functions, making it an effective teaching tool for students.

### Slide 3

The provided image is a lecture slide titled "First Derivative Test for Relative Extrema" and includes a diagram illustrating the concept. 

The slide contains the following elements:
* Title: "First Derivative Test for Relative Extrema" in large black text at the top.
* Subtitle: "Let us look closer at one of the relative extrema of the function z = f(x,y)" in smaller black text below the title.
* A 3D graph diagram:
  - The graph is centered on the slide, with three axes labeled x, y, and z.
  - The z-axis is vertical, while the x and y axes are in the horizontal plane.
  - The graph has a curved surface with a peak at point P(a,b,z).
  - Two tangent lines are drawn on the surface at point P, one in the x-direction (red) and one in the y-direction (blue).
  - The equations for these tangent lines are g(x) = f(x,b) and h(y) = f(a,y), respectively.
  - The partial derivatives of the function z = f(x,y) are shown as ∂z/∂x = 0 and ∂z/∂y = 0.
* Text below the diagram: 
  - "We can see that if a relative maximum of f(x,y) occurs at (a,b), then the tangent lines are part of a horizontal plane with normal (0,0,1)".
* University logo: 
  - The University of Waterloo logo is displayed in the bottom-right corner of the slide.

The diagram and accompanying text illustrate the concept of the first derivative test for relative extrema in multivariable calculus, specifically for a function of two variables, z = f(x,y).

### Slide 4

The image is a slide from a presentation on the topic of "First Derivative Test - Critical Points." The title is prominently displayed at the top in large black text. Below the title, the main content of the slide is presented in smaller black text.

Here is a detailed breakdown of the information on the slide:

*   A point (a, b) in the domain of f(x,y) is said to be a critical point if,
    *   The partial derivatives of f with respect to x and y are both equal to zero at (a, b).
        *   ∂f/∂x |a,b = 0
        *   ∂f/∂y |a,b = 0
    *   Or if one (or both) of these derivatives does not exist at (a,b).
*   Then,
    1.  If f(x,y) has a relative maximum or minimum at (a, b), then (a, b) is a critical point!
    2.  However, not all critical points give rise to maxima or minima

At the bottom right corner of the slide, there is a logo for the University of Waterloo.

In summary, the slide discusses the concept of critical points in the context of multivariable calculus, specifically for functions of two variables. It defines what constitutes a critical point and highlights the relationship between critical points and relative maxima or minima. The content is presented in a clear and concise manner, making it suitable for an educational setting.

### Slide 5

The image presents a slide from a lecture on multivariable calculus, specifically focusing on the concept of a saddle point. The title "Example - Saddle Point" is prominently displayed at the top.

**Title and Problem Statement**

*   **Title:** Example - Saddle Point
*   **Problem Statement:** Find the relative extreme values for
    *   $f(x,y) = \frac{y^2}{b^2} - \frac{x^2}{a^2}$

**Solution**

*   **Step 1: Determine the critical points**
    *   $f_x = -\frac{2x}{a^2}$
    *   $f_y = \frac{2y}{b^2}$
    *   $f_x = f_y = 0 \rightarrow \begin{cases} x = 0 \\ y = 0 \end{cases} \rightarrow (0,0) \rightarrow \text{only CP}$
*   **Step 2: Look at the vicinity around the critical points**
    *   All points in the x-axis ($y = 0$):
        *   $f(x,y) = -\frac{x^2}{a^2} < 0$ (If $x \neq 0$)

**University Logo**

*   The University of Waterloo logo is displayed in the bottom-right corner.

This detailed summary captures all the content present on the slide, including equations, definitions, and written text, ensuring that no information is omitted or simplified.

### Slide 6

The image is a slide from a presentation on the topic of saddle points, featuring a diagram and an example.

**Title**
The title of the slide is "Example - Saddle Point" in bold black text at the top left.

**Text**
Below the title, the text reads: "All points in the y-axis (x = 0): f(x,y) = y^2/b^2 > 0 (If y ≠ 0)". This is followed by "Value of f(x,y) in the vicinity of critical point?" and then "CAN BE POSITIVE OR NEGATIVE → SADDLE POINT!" in green handwriting-style text.

**Diagram**
The diagram is a 3D graph showing a saddle-shaped surface with various labels and annotations. The graph has three axes: x, y, and z. The surface is labeled as "Saddle point" and has several curves and lines drawn on it, including:

* A parabola z = c/b^2 y^2 in the yz-plane
* A parabola z = -c/a^2 x^2 in the xz-plane
* Part of the hyperbola y^2/b^2 - x^2/a^2 = 1 in the plane z = c
* Part of the hyperbola x^2/a^2 - y^2/b^2 = 1 in the plane z = -c

The diagram also includes labels for the hyperbola and parabola.

**Image**
To the right of the diagram is a photograph of a mountain with a saddle-shaped peak, accompanied by the caption "Mountain with a shape of a saddle".

**Footer**
At the bottom right of the slide is the logo for the University of Waterloo.

Overall, the slide appears to be part of a lecture or presentation on multivariable calculus, specifically discussing the concept of saddle points and their properties.

### Slide 7

The slide is titled "Second Derivative Test - Classifying Critical Points" and contains the following information:

**Title and Introduction**

* The title is in large, bold, black text at the top of the slide.
* The subtitle reads, "A way to determine if a critical point is a relative extrema is by using the second derivative test."

**Definitions and Equations**

* The slide states, "Suppose (a, b) is a critical point of f(x, y). Let us then define:"
* Three equations are defined:
  * A = fxx(a, b)
  * B = fxy(a, b)
  * C = fyy(a, b)
* The term "Hessian" is handwritten in blue next to these equations, with an arrow pointing to the equation: D = B^2 - AC = fxy^2 - fxxfyy

**Second Derivative Test Conditions**

* The slide then states, "Then," followed by four conditions:
  * i. If D < 0 and A < 0, then (a, b) is a relative maximum
  * ii. If D < 0 and A > 0, then (a, b) is a relative minimum
  * iii. If D > 0, then (a, b) is a saddle point
  * iv. If D = 0, no conclusion can be made

**Logo and Institution**

* The University of Waterloo logo is displayed in the bottom-right corner of the slide.

The slide presents a clear and concise explanation of the second derivative test for classifying critical points in multivariable calculus.

### Slide 8

The image shows a lecture slide titled "Example - Classifying Critical Points" in large, bold black text at the top. The slide is divided into sections, with the main content presented in a clear and organized manner.

*   **Problem Statement:**
    *   The problem is to find and classify the critical points of the function: $f(x,y) = x^4 + y^4 - 4xy + 1$
*   **Solution:**
    *   **Step 1: Determine the critical points**
        *   The partial derivatives of the function are calculated:
            *   $f_x = 4x^3 - 4y$
            *   $f_y = 4y^3 - 4x$
        *   Setting these partial derivatives equal to zero gives:
            *   $f_x = 0 \rightarrow x^3 - y = 0$ (1)
            *   $f_y = 0 \rightarrow y^3 - x = 0$ (2)
        *   Solving equations (1) and (2) simultaneously:
            *   $(x^3)^3 - x = x^9 - x = x(x^8 - 1) = x(x^2 - 1)(x^2 + 1)(x^4 + 1)$
*   The slide is from the University of Waterloo, as indicated by the logo in the bottom-right corner.

The slide provides a clear and step-by-step solution to the problem, with the calculations and equations presented in a logical and easy-to-follow order.

### Slide 9

The image presents a slide from a lecture on "Classifying Critical Points" from the University of Waterloo. The title, "Example - Classifying Critical Points," is prominently displayed in large black text at the top.

*   **Title and Subtitle**
    *   Title: "Example - Classifying Critical Points" in large black text
    *   Subtitle: "THREE REAL ROOTS:" in blue handwritten text
*   **Roots of the Equation**
    *   Three real roots are listed: x = 0, x = 1, and x = -1
*   **Critical Points (CP)**
    *   Three critical points are identified:
        *   (0,0) corresponding to x = 0
        *   (1,1) corresponding to x = 1
        *   (-1,-1) corresponding to x = -1
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner, featuring a shield with a red and yellow design, accompanied by the university's name in black text.

The slide provides a clear and concise example of classifying critical points, with a focus on the roots of an equation and their corresponding critical points.

### Slide 10

The slide titled "Example - Classifying Critical Points" presents a step-by-step application of the second derivative test to classify critical points. The content is as follows:

**Title and Step**
- Title: "Example - Classifying Critical Points"
- Step 2: "Apply the second derivative test at every critical point"

**Formulas and Calculations**
- A = fxx = 12x^2
- B = fxy = -4
- C = fyy = 12y^2
- D = B^2 - AC = (-4)^2 - (12x^2)(12y^2)
- Simplified expression for D: D = 16 - 144x^2y^2

**Evaluation at Critical Points**
1. At (0,0):
   - D(0,0) = 16 > 0
   - Classification: Saddle Point

2. At (1,1):
   - D(1,1) = -128 < 0
   - A(1,1) = 12 > 0
   - Classification: Relative Minimum (REL. MIN)

**Institutional Logo**
- The University of Waterloo logo is displayed in the bottom-right corner of the slide.

This summary captures the essential information on the slide, including the title, the step being illustrated, the formulas used for the second derivative test, and the application of these formulas to two critical points, (0,0) and (1,1), along with their respective classifications.

### Slide 11

The image presents a slide from a lecture on mathematics, specifically focusing on the classification of critical points in multivariable calculus. The title "Example - Classifying Critical Points" is prominently displayed at the top.

**Key Content:**

*   **Title and Example Number:** The title is followed by the number "3" circled in blue, indicating that this is the third example in a series.
*   **Mathematical Expressions:** Two mathematical expressions are written below the title:
    *   $D(-1,-1) = -128 < 0$
    *   $A(-1,-1) = 12 > 0$
    These expressions are accompanied by an arrow pointing to the right, leading to the conclusion "REL. MIN."
*   **Function and Graphs:** The slide features two graphs related to the function $z = x^4 + y^4 - 4xy + 1$:
    *   **3D Graph:** A 3D graph of the function is shown on the left, illustrating its shape and structure.
    *   **Contour Map:** A contour map of the same function is displayed on the right, providing a 2D representation of the function's behavior.
*   **Labels and Annotations:** Both graphs are labeled and annotated with relevant information, including:
    *   "Graph of the function" below the 3D graph
    *   "Contour Map" below the contour map
    *   Labels on the contour map indicating "Saddle Point" and "Relative minimum"
*   **University Logo:** The University of Waterloo logo is displayed in the bottom-right corner of the slide.

**Visual Elements:**

*   The slide has a white background with a yellow stripe at the top.
*   The title is in large black text, while the rest of the content is presented in a mix of blue, red, and black text.
*   The 3D graph and contour map are rendered in a combination of colors, including purple, brown, and blue.

**Overall:**

The slide provides a clear and concise example of classifying critical points in multivariable calculus, using a specific function and its graphical representations to illustrate the concepts.

### Slide 12

The image presents a slide from a presentation on the topic of "Classifying Critical Points using Contour Plots." The slide is divided into three main sections: the title, the content area, and the footer.

*   **Title**
    *   The title is prominently displayed in large black text at the top center of the slide.
    *   It reads "Classifying Critical Points using Contour Plots."
*   **Content Area**
    *   The content area is blank, with no text or images.
    *   It occupies the majority of the slide, leaving ample space for additional information or visuals.
*   **Footer**
    *   In the bottom-left corner, the University of Waterloo logo is displayed.
    *   The logo features a yellow shield with a red design and a black diagonal line.
    *   To the right of the logo, the text "UNIVERSITY OF WATERLOO" is written in black.

The slide appears to be an introductory or title slide, setting the stage for a discussion on classifying critical points using contour plots. The blank content area suggests that the presenter will fill in the details as they progress through the presentation.

### Slide 13

The image presents a slide from a presentation on local maxima, featuring a title, two graphs, and explanatory text.

*   **Title**
    *   The title "Local Maxima" is prominently displayed in large black font at the top left of the slide.
*   **Definition and Formula**
    *   To the right of the title, the definition of a critical point (CP) is provided: $f_x = 0, f_y = 0$, accompanied by the label "Center of the Contour".
*   **3D Graph**
    *   Below the title, on the left side of the slide, is a 3D graph illustrating a curved surface with a rainbow color scheme. The x, y, and z axes are labeled.
*   **Contour Graph**
    *   Adjacent to the 3D graph, on the right side of the slide, is a contour graph displaying concentric ellipses with numerical values ranging from -8 to 0. The x and y axes are labeled.
*   **Explanatory Text**
    *   At the bottom of the slide, the text reads: "All contours increase as we move toward the critical point."
*   **University Logo**
    *   In the bottom-right corner, the logo for the University of Waterloo is displayed, featuring a shield with a red and gold design, accompanied by the university's name in black text.

In summary, the slide effectively illustrates the concept of local maxima through a combination of visual representations and concise explanatory text, providing a clear understanding of the topic for the audience.

### Slide 14

The lecture slide titled "Local Minima" presents a comprehensive analysis of a critical point in a multivariable function, utilizing both 3D surface and contour plots to illustrate the concept. 

**Title and Definitions**

*   The title "Local Minima" is prominently displayed in large black text at the top left of the slide.
*   The definition of a Critical Point (CP) is provided: 
    *   $f_x = 0$
    *   $f_y = 0$
    *   Center of the Contour

**Visualizations**

*   A 3D surface plot is shown on the left side of the slide, featuring:
    *   A curved surface with a rainbow color scheme, transitioning from red at the top to blue at the bottom.
    *   The surface is oriented with the z-axis pointing upwards and the x and y axes extending outwards from the origin.
*   A contour plot is displayed on the right side of the slide, illustrating:
    *   Concentric ellipses centered around the origin, with contour values labeled.
    *   The x and y axes are clearly marked, with the origin at the center of the plot.

**Key Observations**

*   The text below the contour plot states: "All contours decrease as we move toward the critical point."
*   The University of Waterloo logo is located at the bottom right of the slide, indicating the institution associated with the presentation.

**Overall Content**

The slide effectively conveys the concept of a local minimum in a multivariable function, using a combination of mathematical definitions and visual representations to facilitate understanding.

### Slide 15

The image presents a slide from a presentation on the topic of "Saddle Point" in mathematics, specifically in the context of multivariable calculus. The slide is divided into two main sections: a 3D graph on the left and a contour plot on the right.

**3D Graph:**

*   The 3D graph is a colorful representation of a function, with the x-axis, y-axis, and z-axis labeled.
*   The graph features a saddle-shaped surface, characterized by a minimum point in one direction and a maximum point in another direction.
*   The graph is rendered in a rainbow color scheme, with the colors transitioning smoothly from red to blue.

**Contour Plot:**

*   The contour plot is a 2D representation of the same function as the 3D graph.
*   It displays a series of curved lines, each representing a specific value of the function.
*   The contours are labeled with numerical values, indicating the corresponding function values.
*   The plot has x and y axes, allowing for the visualization of the function's behavior in the xy-plane.

**Text and Equations:**

*   At the top-left corner of the slide, the title "Saddle Point" is prominently displayed in bold black text.
*   Below the title, a mathematical definition is provided: "Critical Point (CP): fx = 0, fy = 0."
*   Further down, the text states, "Intersection of 2 Contours."
*   A descriptive paragraph at the bottom of the slide explains that moving in one direction of the CP, the contours increase, and in a basically perpendicular direction, the contours decrease.

**Logo and Institution:**

*   In the bottom-right corner, the logo of the University of Waterloo is displayed, featuring a shield with a red and gold design, accompanied by the university's name in black text.

Overall, the slide effectively illustrates the concept of a saddle point in multivariable calculus, using both visual representations and mathematical definitions to convey the idea.

### Slide 16

The image presents a slide from a presentation on the topic of "Classifying Critical Points using the gradient vector" in a clear and concise manner.

*   **Title**
    *   The title is prominently displayed in large, bold black text at the top of the slide.
    *   It reads: "Classifying Critical Points using the gradient vector".
*   **University Logo and Name**
    *   In the bottom-left corner, the University of Waterloo's logo is accompanied by its name.
    *   The logo features a shield with a red design on a yellow background, situated above the text "UNIVERSITY OF WATERLOO".
*   **Background**
    *   The background of the slide is white, providing a clean and neutral backdrop for the content.
    *   A yellow gradient stripe runs along the top edge of the slide, adding a touch of color and visual interest.
*   **Overall Design**
    *   The slide's design is simple, yet effective in conveying the topic and affiliation.
    *   The use of a clear title, a recognizable university logo, and a clean background creates a professional and academic atmosphere.

In summary, the image is a straightforward presentation slide that effectively communicates the topic and the presenting institution. The design is simple, yet effective, making it easy to read and understand.

### Slide 17

The image presents a slide from a presentation on the topic of "Local Maxima" in mathematics, specifically in the context of multivariable calculus. The slide is divided into sections, each containing distinct elements that contribute to its overall content.

*   **Title and Header**
    *   The title "Local Maxima" is prominently displayed at the top left of the slide.
    *   A yellow bar separates the title from the rest of the content, adding visual distinction.
*   **Definition and Explanation**
    *   The definition of a Critical Point (CP) is provided: $f_x = 0, f_y = 0$, indicating that both partial derivatives with respect to x and y are zero.
    *   The term "Center of the Contour" is mentioned, suggesting a relationship between critical points and contour plots.
*   **Graphs and Illustrations**
    *   A 3D graph of a function $z = f(x,y)$ is shown, illustrating a local maximum. The graph features a rainbow color scheme, with the highest point colored red and gradually transitioning to blue towards the edges.
    *   A contour plot is displayed, showing the gradient vectors around a critical point. The arrows point towards the center, indicating the direction of the gradient.
*   **Text and Descriptions**
    *   The text "All gradients in the CP neighborhood are directed toward the CP" explains the behavior of gradients near a critical point.
    *   The University of Waterloo logo is present in the bottom-right corner, indicating the institution associated with the presentation.
*   **Statistics and Data**
    *   No specific statistics or numerical data are presented on this slide.

In summary, the slide provides a visual and textual explanation of local maxima in multivariable calculus, including definitions, graphical representations, and descriptions of gradient behavior around critical points.

### Slide 18

The image presents a slide from a lecture on Local Minima, featuring a white background with black text and diagrams. The title "Local Minima" is prominently displayed in large black font at the top left of the slide.

*   **Title and Subtitle**
    *   The title "Local Minima" is written in large black font.
    *   Below the title, two lines of text read: "Critical Point (CP): $f_x = 0, f_y = 0$" and "Center of the Contour".
*   **Diagrams**
    *   Two diagrams are presented side by side:
        *   The left diagram illustrates a 3D surface plot with a rainbow-colored grid, accompanied by an arrow pointing to the equation "z = f(x,y)".
        *   The right diagram displays a contour plot with a series of concentric circles, featuring arrows pointing outward from the center.
*   **Text Below Diagrams**
    *   A sentence below the diagrams states: "All gradients in the neighborhood of the CP are directed away from the CP".
*   **University Logo**
    *   In the bottom-right corner, the University of Waterloo logo is displayed, consisting of a shield with a red and gold crest, accompanied by the text "UNIVERSITY OF WATERLOO".

The slide effectively conveys information about local minima, critical points, and contour plots, providing a clear visual representation of the concepts.

### Slide 19

The image presents a slide from a lecture on the topic of "Saddle Point" in mathematics, specifically focusing on critical points and gradient behavior. The slide is divided into two main sections: a 3D graph on the left and a 2D contour plot on the right, accompanied by explanatory text.

*   **Title and Institution**
    *   The title "Saddle Point" is prominently displayed at the top-left corner.
    *   The University of Waterloo logo is shown at the bottom-right corner.
*   **3D Graph**
    *   The 3D graph illustrates a function z = f(x,y), showcasing its surface.
    *   The graph features a saddle-like shape, characteristic of a saddle point.
*   **2D Contour Plot**
    *   The contour plot displays the intersection of two curves, labeled as "Critical Point (CP): fx = 0, fy = 0".
    *   The plot includes arrows indicating the direction of the gradient.
    *   The text "Moving in one direction the gradients point toward the CP and from a basically perpendicular direction the gradients point away from the CP" explains the behavior of gradients around the critical point.
*   **Key Points**
    *   A critical point is defined as a point where both partial derivatives (fx and fy) equal zero.
    *   The intersection of two curves represents the critical point.
    *   Gradients point towards the critical point in one direction and away from it in a perpendicular direction.

In summary, the slide effectively illustrates the concept of a saddle point through visual representations and concise explanations, providing students with a clear understanding of critical points and gradient behavior.

### Slide 20

The image presents a slide from a presentation on the topic of "Summary," likely related to a calculus or mathematics course. The slide is divided into three main bullet points, each discussing a different aspect of the subject matter.

*   **Title and Bullet Points**
    *   The title "Summary" is prominently displayed in large black text at the top left of the slide.
    *   Three bullet points are listed below the title, each providing a concise statement about the topic.
        *   The first bullet point states, "To determine the critical points we use the first derivative test."
        *   The second bullet point reads, "To determine whether we have a relative maximum or relative minimum we use the second derivative test."
        *   The third bullet point notes, "We can use the contour plots and the concept of gradient to visually classify the relative extrema of a function of two variables."
*   **University Logo**
    *   In the bottom-right corner of the slide, the logo for the University of Waterloo is displayed.
    *   The logo features a shield with a yellow and red design, accompanied by the university's name in black text.
*   **Background and Design Elements**
    *   The background of the slide is white, providing a clean and neutral backdrop for the content.
    *   A yellow stripe runs along the top edge of the slide, adding a touch of color and visual interest.
    *   A thick black stripe is situated above the yellow stripe, creating a sense of depth and framing the content.

In summary, the slide provides a concise summary of key concepts related to determining critical points and classifying relative extrema using derivative tests and contour plots. The University of Waterloo logo is prominently displayed in the corner, indicating the institution's affiliation with the presentation.

