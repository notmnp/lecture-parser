# Lecture 25 - Problem Double Integrals Polar Coordinates

## Study Notes

# Double Integrals in Polar Coordinates – Exam Study Guide  

## Core Formulas & Definitions  

| Formula | Meaning & Symbols | When to Use |
|---------|--------------------|-------------|
| **Area in polar form**<br>$$A=\displaystyle\int_{\theta=a}^{b}\int_{r=r_{\text{inner}}}^{r_{\text{outer}}} r\,dr\,d\theta$$ | $r$ = radial coordinate. <br>$\theta$ = angle (rad). <br>Inner/outer bounds are the smallest/largest $r$ that enclose the region for a given $\theta$. | Calculating area bounded by two polar curves or by a polar curve and a line/constant radius. |
| **Double integral in polar**<br>$$\iint_{D} f(x,y)\,dA=\displaystyle\int_{\theta=a}^{b}\int_{r=r_{\text{inner}}}^{r_{\text{outer}}} f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta$$ | Jacobian $r$ appears because $dA = r\,dr\,d\theta$. | Evaluating any double integral where the region is conveniently described in polar coordinates. |
| **Intersection of polar curves**<br>$$r_1(\theta)=r_2(\theta)$$ | Solve for $\theta$ to find where curves cross. | Determining limits of $\theta$ when two curves bound a region. |
| **Trigonometric identities** | • $2\sin^2\theta = 1-\cos2\theta$ <br>• $\sin(-\theta)=-\sin\theta$, $\cos(-\theta)=\cos\theta$ | Simplify integrands that contain $\sin^2$ or $\cos^2$. |
| **Symmetry** | If the region is symmetric about the $x$-axis or $y$-axis, limits can be halved or doubled. | Reduce the integral domain, especially when $\theta$ limits are symmetric about $0$. |

---

## Key Concepts & Intuition  

- **Polar vs Cartesian**  
  - In polar, curves often become simple (e.g., circles, cardioids).  
  - The extra $r$ factor in the integrand accounts for the “stretching” of area elements.

- **Bounding Region**  
  - Identify *outer* and *inner* radius functions for each $\theta$.  
  - Sketch the curves: a visual check ensures correct bounds.

- **Angle Limits**  
  - Find all $\theta$ where the inner and outer curves intersect.  
  - Order the intersection angles from smallest to largest to set $\theta$ limits.

- **Area of a Region**  
  - A special case of a double integral with integrand $f \equiv 1$.

- **Changing Order of Integration**  
  - Often unnecessary but useful if the $r$-bounds are complicated; may require solving for $\theta$ as a function of $r$.

---

## Problem‑Solving Strategies  

### 1. Area Between Two Polar Curves  

1. **Sketch** the curves.  
2. **Set intersection equation**: $r_1(\theta)=r_2(\theta)$ → solve for $\theta$.  
3. **Determine which curve is outer** over each $\theta$ interval.  
4. **Write area integral** using the outer–inner formula.  
5. **Evaluate**:  
   - Integrate w.r.t. $r$ first: $\int r\,dr = \frac12 r^2$.  
   - Simplify integrand; apply trig identities if needed.  
   - Integrate w.r.t. $\theta$.

*Typical cues*: phrases like “inside” vs “outside,” “between,” “between curves.”

### 2. Area Inside a Single Polar Curve  

1. **Find $\theta$ limits**: identify where the curve returns to the pole or is symmetric.  
2. **Set integral**: $A = \frac12\int_{\theta_1}^{\theta_2} r(\theta)^2\,d\theta$.  
3. **Simplify** using identities; integrate.  

*Typical cues*: “area bounded by $r=…$” or “inside the curve.”

### 3. Double Integral over a Polar Region  

1. **Express function** in terms of $r,\theta$: $f(x,y)=f(r\cos\theta,r\sin\theta)$.  
2. **Set bounds** as per region description.  
3. **Write integral** with Jacobian $r$.  
4. **Compute inner integral** (often in $r$).  
5. **Compute outer integral** (in $\theta$).  

*Typical cues*: “evaluate $\iint_D (x^2+y^2)\,dA$ where $D$ is …”

---

## Common Pitfalls & Checks  

| Pitfall | How to Avoid |
|---------|--------------|
| **Wrong order of bounds** | Double‑check which curve is outer/inner for each $\theta$. |
| **Incorrect $\theta$ limits** | Verify by solving $r_1(\theta)=r_2(\theta)$; plot to confirm. |
| **Missing Jacobian $r$** | Remember that $dA = r\,dr\,d\theta$; omission halves the area. |
| **Neglecting symmetry** | Use symmetry to simplify limits; otherwise you may integrate unnecessary intervals. |
| **Algebraic errors in trigonometric simplification** | Apply identities carefully; verify with small numerical checks. |
| **Sign errors from limits** | Keep track of bounds; if $\theta$ decreases, flip sign accordingly. |

---

### Quick Checklist for Exam Problems  

1. **Identify** the region and curves.  
2. **Sketch** (even a rough one).  
3. **Find intersections** → $\theta$ limits.  
4. **Determine outer/inner** radius for each $\theta$.  
5. **Write integral** (area or double integral).  
6. **Include Jacobian $r$**.  
7. **Simplify integrand** (use trig identities).  
8. **Integrate** first w.r.t. $r$, then $\theta$.  
9. **Check units / sign**.  
10. **Verify with symmetry** if applicable.  

--- 

**Good luck!** Focus on correctly setting up the integral; the algebraic evaluation usually follows straightforwardly.

---

## Raw Slide Summaries

### Slide 1

The image is a presentation slide titled "Application Problem Double Integrals in Polar Coordinates" from the University of Waterloo. The title is prominently displayed in large black text at the top center of the slide.

*   **Title and Subtitle**
    *   The title is "Application Problem Double Integrals in Polar Coordinates."
    *   Below the title, there is a yellow rectangle with the text "Trim Ch 13, 13.7" inside it.
*   **Outline**
    *   The outline section is located below the title and subtitle.
    *   It contains a single point: "1. Application Problem Double Integrals in Polar Coordinates."
*   **University Logo and Name**
    *   The University of Waterloo logo is displayed at the bottom left of the slide.
    *   The logo features a shield with a red design on a yellow background, accompanied by the words "UNIVERSITY OF WATERLOO" in black text.
*   **Background**
    *   The background of the slide is white, with a gradient bar at the top that transitions from black to yellow.

The slide appears to be part of a lecture or presentation on double integrals in polar coordinates, likely for a mathematics or engineering course at the University of Waterloo.

### Slide 2

The image presents a slide from a presentation on the topic of "Problem - Area of a Region in Polar Coordinates." The slide is divided into several sections, each containing relevant information and visual aids.

*   **Title and Problem Statement**
    *   The title is prominently displayed at the top of the slide.
    *   The problem statement is: "Determine the area of the region that lies inside r = 3 + 2 sin θ and outside of r = 2."
*   **Solution**
    *   The solution is presented in a step-by-step manner.
    *   Step 1: Sketch, determine all intersections, and label.
    *   A graph is provided to illustrate the problem, featuring two curves: r = 3 + 2 sin θ and r = 2.
    *   The graph includes labels for the x and y axes, as well as annotations to highlight key points.
*   **Equations and Calculations**
    *   The equations for the two curves are given: r = 3 + 2 sin θ and r = 2.
    *   The intersection points of the two curves are calculated by setting the equations equal to each other: 3 + 2 sin θ = 2.
    *   The resulting equation is solved for θ, yielding values of 7π/6 and 11π/6.
*   **Graphical Representation**
    *   The graph shows the two curves intersecting at specific points.
    *   The region of interest is shaded, indicating the area to be calculated.
    *   The graph includes annotations to highlight important features, such as the intersection points and the boundaries of the region.
*   **University Logo**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner of the slide.

In summary, the slide provides a clear and concise presentation of a problem related to finding the area of a region in polar coordinates. The solution is broken down into manageable steps, accompanied by a graphical representation to aid understanding. The slide effectively communicates the necessary information to solve the problem, making it a useful resource for students or individuals seeking to learn about this topic.

### Slide 3

The image presents a slide from a lecture on polar coordinates, specifically focusing on the problem of finding the area of a region in polar coordinates. Here's a detailed breakdown of the slide's content:

**Title and Header**

* The title of the slide is "Problem - Area of a Region in Polar Coordinates."
* The header features a black bar at the top, followed by a yellow bar, and then a white background.

**Step 2: Setup the Limits of Integration**

* This section presents the formula for the area of a region in polar coordinates, given by:
  * A = ∫[θ=-π/6 to θ=7π/6] ∫[r=2 to r=3+2sin(θ)] r dr dθ
* The limits of integration are highlighted in green for θ and red for r.

**Step 3: Solve the Integral**

* The integral is evaluated as follows:
  * A = ∫[θ=-π/6 to θ=7π/6] (1/2)r^2 | from r=2 to r=3+2sin(θ) dθ
  * = ∫[θ=-π/6 to θ=7π/6] (1/2)(3+2sin(θ))^2 - (1/2)(2)^2 dθ

**Additional Information**

* The slide is presented by the University of Waterloo, as indicated by the logo in the bottom-right corner.
* The logo features a shield with a red and yellow design, accompanied by the text "UNIVERSITY OF WATERLOO" in black.

Overall, the slide provides a clear and concise explanation of the steps involved in solving the problem of finding the area of a region in polar coordinates.

### Slide 4

The slide, titled "Problem - Area of a Region in Polar Coordinates," presents a mathematical problem related to calculating the area of a region in polar coordinates. The slide displays a step-by-step solution to the problem, featuring several equations and formulas.

The solution begins with an integral expression, 
= ... = ∫[(-π/6) to (π/6)] (5/2 + 6sin(θ) + 2sin^2(θ)) dθ, 
which is simplified using the trigonometric identity 2sin^2(θ) = 1 - cos(2θ), highlighted in red. The equation then becomes 
= ∫[(-π/6) to (π/6)] (7/2 + 6sin(θ) - cos(2θ)) dθ.

The integral is evaluated, resulting in 
= [(7/2)θ - 6cos(θ) - (1/2)sin(2θ)] from (-π/6) to (π/6).

The final calculation yields 
= (11√3)/2 + (14π)/3 = 24.187.

In the bottom-right corner, the University of Waterloo logo is displayed, indicating the institution associated with the slide.

The content of the slide is presented on a white background, with a yellow and black border at the top, and the equations are written in black ink, except for the red annotation highlighting the trigonometric identity.

### Slide 5

The image is a slide from a presentation, likely the final slide, as it contains a message of gratitude. 

*   The top of the slide features a thick black bar followed by a thick yellow bar, both spanning the width of the image.
*   Below these bars, on the left side, is the University of Waterloo's logo, which includes a shield with a red lion on a yellow background and three black chevrons. To the right of the logo, in bold black text, is the university's name: "UNIVERSITY OF WATERLOO".
*   In the lower left corner of the slide, in large bold black text, is the phrase "Thank you".

The background of the slide is white.

