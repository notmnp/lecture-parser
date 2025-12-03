# Lecture 22 - Lagrange Multipliers

## Study Notes

# Lagrange Multipliers – Problem‑Solving Study Notes

---

## Core Formulas & Definitions  

| Formula | Meaning & Symbols | Typical Use |
|---------|-------------------|-------------|
| **Gradient condition (one constraint)** | $\displaystyle \nabla f(\mathbf{x}) = \lambda\,\nabla g(\mathbf{x})$ | Extrema of $f$ on the surface $g(\mathbf{x})=0$ |
| **Gradient condition (multiple constraints)** | $\displaystyle \nabla f(\mathbf{x}) = \sum_{k=1}^{m}\lambda_k\,\nabla g_k(\mathbf{x})$ | Extrema of $f$ when all constraints hold |
| **Lagrangian (any number of constraints)** | $\displaystyle \mathcal L(\mathbf{x},\boldsymbol\lambda)=f(\mathbf{x})-\sum_{k}\lambda_k\,g_k(\mathbf{x})$ | Encapsulates first‑order conditions in one expression |
| **Bordered Hessian (second‑derivative test)** | For $m$ constraints, $$\mathcal H =\begin{bmatrix}
0 & (\nabla g_1)^T & \dots & (\nabla g_m)^T\\
\nabla g_1 & \nabla^2 f & \dots & \nabla^2 f\\
\vdots & \vdots & \ddots & \vdots\\
\nabla g_m & \nabla^2 f & \dots & \nabla^2 f
\end{bmatrix}$$ | Sign pattern of leading principal minors decides max/min on the manifold |
| **KKT (inequality)** | $\lambda_k\ge0,\; g_k(\mathbf{x})\le0,\; \lambda_k g_k(\mathbf{x})=0$ | Handles inequality constraints (complementary slackness) |

*Symbols*  
- $\mathbf{x}=(x_1,\dots,x_n)$ – variable vector  
- $f(\mathbf{x})$ – objective function  
- $g_k(\mathbf{x})$ – $k$th constraint  
- $\lambda_k$ – Lagrange multiplier for constraint $k$  
- $\nabla f,\nabla g_k$ – gradients  
- $\nabla^2 f$ – Hessian of $f$

---

## Key Concepts & Intuition  

- **Tangency** – At an optimum, the level set of $f$ is tangent to the feasible surface; thus their gradients are linearly dependent.  
- **Multiplier meaning** – $\lambda_k$ is the sensitivity of the optimum value to a unit change in the $k$th constraint.  
- **Independent constraints** – The vectors $\{\nabla g_k\}$ must be linearly independent; otherwise the feasible set is not a smooth manifold and the method fails.  
- **Dimensionality** – With $m$ constraints in $\mathbb R^n$, the feasible manifold has dimension $n-m$.  
- **Substitution method** – Solve constraints for one or more variables, substitute into $f$, reduce dimensionality, then apply ordinary calculus.  
- **Boundary/inequality cases** – When the feasible region is closed or bounded, check boundary points or use KKT for inequalities.

---

## Problem‑Solving Strategies  

### 1. General Flow for Equality Constraints  

1. **Identify** objective $f$, all equality constraints $g_k(\mathbf{x})=0$, and domain restrictions.  
2. **Form Lagrangian** $\displaystyle \mathcal L=f-\sum_k\lambda_k g_k$.  
3. **First‑order conditions**  
   - $\displaystyle \frac{\partial\mathcal L}{\partial x_i}=0,\ i=1,\dots,n$  
   - $\displaystyle \frac{\partial\mathcal L}{\partial \lambda_k}=0\;\Rightarrow\;g_k(\mathbf{x})=0$  
4. **Solve** the resulting algebraic system for $(\mathbf{x},\boldsymbol\lambda)$.  
   - Use elimination of multipliers (subtract equations, substitute).  
   - For linear systems, solve with matrix algebra.  
5. **Check feasibility** – verify all constraints and domain limits.  
6. **Evaluate $f$** at each feasible candidate.  
7. **Second‑derivative test** – construct the bordered Hessian; determine sign pattern of its leading principal minors.  
8. **Boundary cases** – if the feasible set is bounded, compute $f$ on boundaries (vertices, edges) separately.  
9. **Inequalities** – if present, add KKT conditions or convert to slack variables.

---

### 2. One Constraint – Quick Checklist  

| Step | Action |
|------|--------|
| 1 | Compute $\nabla f$ and $\nabla g$. |
| 2 | Set $f_{x_i}= \lambda\,g_{x_i}$ for all $i$. |
| 3 | Add the constraint $g(\mathbf{x})=0$. |
| 4 | Solve the (usually linear) system for $(\mathbf{x},\lambda)$. |
| 5 | Verify domain and evaluate $f$. |
| 6 | Apply bordered Hessian to decide max/min. |

---

### 3. Two or More Constraints – Quick Checklist  

| Step | Action |
|------|--------|
| 1 | Write $\displaystyle \nabla f = \sum_{k=1}^{m}\lambda_k\nabla g_k$. |
| 2 | Write $m$ constraint equations $g_k(\mathbf{x})=0$. |
| 3 | Assemble the $(n+m)\times(n+m)$ system (gradients + constraints). |
| 4 | Solve for $(\mathbf{x},\lambda_1,\dots,\lambda_m)$. |
| 5 | Verify feasibility and compute $f$. |
| 6 | Use the bordered Hessian or restrict Hessian to tangent space. |
| 7 | Inspect boundary/edge cases if the feasible set is bounded. |

**Typical cue:** “Two constraints” → two gradient equations + two constraint equations.  
**Common algebra trick:** Subtract one gradient equation from another to eliminate a multiplier; then solve for the variables.

---

### 4. Substitution Method – When to Use  

- **When constraints are simple** (linear or easily solvable for a variable).  
- **When the objective is low‑dimensional after substitution** – reduces the problem to ordinary calculus.  

**Steps**  

1. **Solve constraints for one or more variables** (e.g., $x = h(y,z)$).  
2. **Substitute** into $f$ to get a reduced function $\tilde f$ in fewer variables.  
3. **Differentiate** $\tilde f$ with respect to the remaining variables, set to zero, solve.  
4. **Back‑substitute** to recover the full variable set.  
5. **Check feasibility** and boundary points.  

**Caution** – Substitution can produce extraneous solutions if the eliminated variable appears in denominators or inside even roots; always check domain.

---

### 5. Sample Two‑Constraint Problem (Quick Walk‑through)

> **Maximize** $f(x,y,z)=x+2y+3z$  
> **Subject to**  
> \[
> \begin{cases}
> x-y+z = 1\\
> x^{2}+y^{2} = 1
> \end{cases}
> \]

**Solution**  
1. $\mathcal L = x+2y+3z - \lambda(x-y+z-1)-\mu(x^{2}+y^{2}-1)$  
2. First‑order conditions →  
   $1-\lambda-2\mu x=0,\; 2+\lambda-2\mu y=0,\; 3-\lambda=0,\; x-y+z-1=0,\; x^{2}+y^{2}=1$  
3. From $3-\lambda=0$ get $\lambda=3$.  
4. Solve for $x,y$ in terms of $\mu$: $x=-1/\mu,\; y=5/(2\mu)$.  
5. Use $x^{2}+y^{2}=1$ → $\mu=\pm\sqrt{29}/2$.  
6. Pick the value that satisfies all equations; compute $z$ from $x-y+z=1$.  
7. Evaluate $f$ → $f_{\max}=3+\sqrt{29}$.  
8. Bordered Hessian test shows the solution is a global maximum on the feasible circle.

---

### 6. Common Problem Patterns  

| Pattern | Key Cue | Strategy |
|---------|---------|----------|
| **Linear objective, linear constraints** | “Maximize $ax+by+cz$ subject to $px+qy+rz=s$” | Solve linear system or use substitution if one variable is free. |
| **Quadratic objective, quadratic constraint** | $f(x,y)=x^{2}+xy+y^{2}$, $g(x,y)=x^{2}+y^{2}=R^{2}$ | Gradients are linear; often symmetric solutions (e.g., $x=y$). |
| **Volume/area with linear/quad constraint** | “Maximize $V=xyz$ with $x+y+z=const$” | Expect equal ratios (e.g., $x=y=z$). |
| **Cost minimization** | “Minimize $C=ax+by$ with budget $px+qy\leq B$” | Use KKT; the multiplier equals marginal cost per dollar. |
| **Inequality only** | “Find extrema of $f$ with $g(x)\le 0$” | Apply KKT; check if $g$ is active (equality) or inactive. |

---

## Common Pitfalls & Checks  

- **Missing a constraint** – Double‑check that every $g_k$ appears in the system.  
- **Domain violations** – E.g., $x<0$ when $x$ is a length; discard such solutions.  
- **Linear dependence of constraints** – If $\nabla g_i$ are not independent, the manifold is singular; the method fails.  
- **Sign errors** – A wrong sign on $\lambda$ can misclassify a maximum as a minimum. Verify by plugging back.  
- **Singular bordered Hessian** – Indicates degenerate cases; consider higher‑order tests or numerical verification.  
- **Boundary extrema** – For closed regions, evaluate $f$ on edges/corners; Lagrange multipliers do not capture them.  
- **Complementary slackness** – For inequalities, ensure $\lambda_k g_k=0$; otherwise you have an interior point with an inactive inequality.  
- **Algebraic simplification mistakes** – When eliminating multipliers, keep track of signs and factors; a single error can invalidate all solutions.

---

## Quick “What to Do Next” Checklist  

- [ ] Write down $f$, all equality constraints $g_k$, and domain restrictions.  
- [ ] Form $\mathcal L$ and write all first‑order equations.  
- [ ] Solve the system (eliminate multipliers, use substitution if helpful).  
- [ ] Verify feasibility (constraints + domain).  
- [ ] Evaluate $f$ at each candidate.  
- [ ] Apply bordered Hessian (or tangent‑space definiteness) to classify.  
- [ ] Check boundary/inequality cases separately (KKT or direct substitution).  

With these formulas, concepts, and step‑by‑step procedures you’re equipped to tackle any exam problem involving constrained optimization using Lagrange multipliers or the substitution method. Good luck!

---

## Raw Slide Summaries

### Slide 1

The lecture slide contains the title "The Method of Lagrange Multipliers" in large, bold black text at the top. Below the title, a yellow rectangle contains the text "Trim Ch 11, S. 12.12" in black text.

The main content of the slide is an outline, which is presented in a numbered list with two items:

1. Method of Lagrange Multipliers with one constraint
2. Method of Lagrange multipliers with two constraints

At the bottom left of the slide, the University of Waterloo logo is displayed. The logo consists of a shield with a red and yellow design, accompanied by the text "UNIVERSITY OF WATERLOO" in black.

The background of the slide is white, with a black and yellow bar at the top. The overall design is simple and clean, with clear headings and concise bullet points. There are no diagrams or images on this slide.

### Slide 2

The slide is titled "Method of Lagrange Multipliers - One Constraint" and is presented by the University of Waterloo.

**Text Content:**

* The title is prominently displayed at the top in large, bold font.
* The main text states: "Let us assume that we want to maximize a function z = f(x,y) with a domain D, and in that domain we have a constraint g(x,y) = 0."
* Below the diagram, the text reads: "To maximize f(x,y) on a constraint, we are looking for the highest f(x0,y0) value corresponding to a point P(x0,y0) in g(x,y) = 0."

**Diagram:**

* The diagram is a 3D graph with x, y, and z axes.
* The z-axis is labeled, and the x and y axes are shown at the bottom of the graph.
* A curved surface is plotted on the graph, representing the function z = f(x,y).
* The surface has a peak, and several contour lines are drawn on the xy-plane, labeled z = C1, z = C2, and z = C3.
* A red curve on the xy-plane represents the constraint g(x,y) = 0.
* The point P(x0,y0) is marked on the constraint curve, and a vertical line is drawn from this point to the surface, indicating the value f(x0,y0).
* The diagram is annotated with various labels, including "z = f(x,y)" and "g(x,y) = 0".

**Other Elements:**

* The University of Waterloo's logo is displayed in the bottom-right corner of the slide.

### Slide 3

The image presents a graph illustrating the Method of Lagrange Multipliers with one constraint. The title, "Method of Lagrange Multipliers - One Constraint," is prominently displayed at the top.

**Key Elements:**

*   The graph features a 3D coordinate system with x, y, and z axes.
*   A red curve represents the constraint g(x,y) = 0.
*   Multiple black curves are labeled as z = c1, z = c2, z = c3, and z = c4, indicating different values of z.
*   A blue curve intersects the red curve at a point marked with an "x" and labeled as P(x0,y0).
*   The graph is accompanied by text that reads, "Zooming in on what is happening in the x-y plane," and "Where would the maximum value be found?"

**Visual Representation:**

*   The graph is set against a white background, with a yellow bar at the top.
*   The University of Waterloo logo is displayed in the bottom-right corner.

**Overall:**

*   The image effectively illustrates the concept of the Method of Lagrange Multipliers with a single constraint, providing a clear visual representation of the mathematical principles involved.

### Slide 4

The image presents a slide from a presentation on the "Method of Lagrange Multipliers - One Constraint" in a clear and concise manner. The title, prominently displayed in bold black text at the top, sets the stage for the discussion that follows.

Below the title, a brief introduction is provided, outlining the objective of finding the point $P(x_0,y_0)$ that maximizes the function $f(x,y)$ subject to the constraint $g(x,y) = 0$. This is followed by a statement that invites the viewer to zoom in on the area where the two contours intersect.

The main visual element of the slide is a graph, which illustrates the concept being discussed. The graph features a red curve representing the constraint $g(x,y) = 0$, a green curve representing the function $f(x,y)$, and a blue coordinate system with x and y axes labeled accordingly. The point of intersection between the two curves is marked as $P(x_0,y_0)$, and the gradient vectors $\nabla f$ and $\nabla g$ are depicted as arrows emanating from this point.

A key observation is highlighted in the text below the graph, noting that both contours are tangent at $P(x_0,y_0)$. This is accompanied by a mathematical expression, $z = c$, written in green next to the green contour, indicating that the value of $z$ is constant along this curve.

In the bottom-right corner of the slide, the logo of the University of Waterloo is displayed, featuring a shield with a red and gold design, accompanied by the university's name in black text. The background of the slide is white, providing a clean and neutral backdrop for the content.

Overall, the slide effectively communicates the concept of using Lagrange multipliers to find the maximum or minimum of a function subject to a constraint, and the graph provides a clear visual representation of the underlying mathematics.

### Slide 5

The image presents a slide from a lecture on the Method of Lagrange Multipliers, specifically focusing on the case of one constraint. The slide is divided into sections, each containing mathematical equations and explanations.

*   **Title and Introduction**
    *   The title "Method of Lagrange Multipliers - One Constraint" is prominently displayed at the top.
    *   The introduction explains that because both contours are tangent at point P(x0, y0), the gradient of f is proportional to the gradient of g, and this relationship can be expressed as ∇f = λ∇g.
*   **Mathematical Derivation**
    *   The equation ∇f = λ∇g is expanded into its component form: (fx, fy) = λ(gx, gy).
    *   This leads to the system of equations: fx = λgx and fy = λgy.
    *   It is noted that since P(x0, y0) lies on the constraint, g(x, y) = 0.
*   **Equations and Method Explanation**
    *   Equations (1), (2), and (3) are highlighted as determining the Method of Lagrange Multipliers, with λ being referred to as the Lagrange Multiplier.
    *   The explanation concludes by stating that these equations can be generalized for a function of three variables and used to set up a general procedure for optimization.
*   **University Logo**
    *   The logo of the University of Waterloo is displayed in the bottom-right corner, indicating the institution associated with the lecture.

In summary, the slide provides a detailed explanation of the Method of Lagrange Multipliers for optimizing a function subject to a single constraint, including the derivation of the necessary equations and the introduction of the Lagrange Multiplier.

### Slide 6

The image presents a slide from a lecture on the "Method of Lagrange Multipliers - One Constraint." The title is prominently displayed at the top, followed by a brief introduction that outlines the objective of finding local maximum and minimum values of a function $f(x,y,z)$ subject to a constraint $g(x,y,z)=0$. The slide is divided into three main sections, each representing a step in the process.

*   **Step 1:**
    *   This step involves finding all values of $x$, $y$, $z$, and $\lambda$ that satisfy two equations:
        *   $\nabla f(x,y,z) = \lambda \nabla g(x,y,z)$ (Equation 1)
        *   $g(x,y,z) = 0$ (Equation 2)
    *   These equations are fundamental to the method of Lagrange multipliers.
*   **Step 2:**
    *   Evaluate $f(x,y,z)$ at all points $(x,y,z)$ resulting from Step 1.
    *   The largest value obtained is the maximum value of $f(x,y,z)$, while the smallest value is the minimum value of $f(x,y,z)$.
*   **Step 3:**
    *   Use the second derivative method to verify whether the critical points correspond to a maximum or a minimum when necessary.

In summary, the slide provides a clear and structured approach to applying the method of Lagrange multipliers with one constraint, guiding the reader through the necessary steps to identify local extrema of a function under a given constraint.

### Slide 7

The slide is titled "Our Box Problem Using Lagrange Multipliers" and presents a problem related to optimizing the volume of a rectangular box that can be carried by a drone.

The problem statement is as follows:
"A delivery company is using an unmanned aerial drone to pick up packages from their warehouse and deliver them to their clients. The drone can only carry rectangular boxes the sum of whose length and girth (i.e., the perimeter of a cross-section) does not exceed 108 inches. Find the dimensions of an acceptable box of the largest volume that the drone can pick up."

**Problem Solution**

The solution section is written in blue text and states:
"We want to maximize the volume: 
V(x,y,z) = xyz 
Subjected to the constraint: 
x + 2y + 2z = 108 
Which can be written as the level surface,"

**Image and Diagram**

To the right of the problem and solution, there is an image of a drone in flight, with a URL below it: "https://www.voanews.com/silicon-valley-technology/600000-commercial-drones-could-fill-us-skies-next-year". Below the image, a diagram illustrates a rectangular box with dimensions labeled x, y, and z, and the term "girth" is defined with an arrow pointing to the perimeter of the box's cross-section.

**University Logo**

In the bottom-right corner, the University of Waterloo logo is displayed, indicating the institution associated with the slide.

The slide effectively communicates the problem, its solution, and the relevant concepts, making it a clear and concise presentation of the material.

### Slide 8

The image presents a slide titled "Our Box Problem Using Lagrange Multipliers" in large black text at the top, set against a white background with a yellow stripe underneath the title and a black stripe above it. The slide is divided into two main sections: the top section contains the title and a problem statement, while the bottom section features handwritten notes in blue ink.

**Top Section:**

*   Title: "Our Box Problem Using Lagrange Multipliers"
*   Problem statement:
    *   Using the method of Lagrange multipliers (instead of the substitution method), we look for values of $x$, $y$, $z$ and $\lambda$ such that,
        *   $\nabla V(x,y,z) = \lambda \nabla g(x,y,z)$ (1)
        *   $g(x,y,z) = x + 2y + 2z - 108 = 0$ (2)

**Bottom Section:**

*   Handwritten notes in blue ink:
    *   "This gives,"
        *   $V_x = \lambda g_x \rightarrow yz = \lambda$ (3)
        *   $V_y = \lambda g_y \rightarrow xz = 2\lambda$ (4)
        *   $V_z = \lambda g_z \rightarrow xy = 2\lambda$ (5)
    *   "Multiplying by $x,y,z$ respectively"
        *   $xyz = \lambda x$ (6)
        *   $xyz = 2\lambda y$ (7)
        *   $xyz = 2\lambda z$ (8)
    *   "If $\lambda = 0$, it would imply that $x$, or $y$, or $z$ is zero AND CANNOT BE POSSIBLE FOR A BOX!"

**Logo:**

*   University of Waterloo logo in the bottom-right corner, featuring a black shield with a white "W" and the university's name in black text next to it.

The slide appears to be part of a lecture on optimization techniques, specifically using Lagrange multipliers to solve a problem related to a box. The handwritten notes suggest that the lecturer is working through the problem step-by-step, using the method of Lagrange multipliers to find the values of $x$, $y$, $z$, and $\lambda$ that satisfy the given conditions.

### Slide 9

The image is a slide from a presentation on the topic of "Our Box Problem Using Lagrange Multipliers." The slide features a white background with black text and blue handwritten notes.

*   **Title**
    *   The title, "Our Box Problem Using Lagrange Multipliers," is prominently displayed at the top of the slide in large black font.
*   **Equations and Notes**
    *   Below the title, there are several lines of blue handwritten notes that appear to be a solution to a mathematical problem.
    *   The notes include various equations and symbols, such as lambda (λ), x, y, and z, which are commonly used in calculus and optimization problems.
    *   The equations are written in a step-by-step format, suggesting that they are part of a worked example or proof.
*   **University Logo**
    *   In the bottom-right corner of the slide, there is a logo for the University of Waterloo.
    *   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.
*   **Statistics**
    *   P(36,18,18) = SAME ANSWER!
        *   x = 36
        *   y = 18
        *   z = 18

Overall, the slide appears to be a lecture slide from a mathematics course, likely at the University of Waterloo, and is discussing the application of Lagrange multipliers to solve an optimization problem related to a box.

### Slide 10

The image presents a mathematical diagram illustrating the concept of optimization with two constraints, titled "Optimization with Two Constraints" in large black text at the top. The diagram is accompanied by explanatory text and equations.

*   **Title and Introduction**
    *   The title "Optimization with Two Constraints" is displayed prominently at the top.
    *   A brief introduction explains that many problems require finding extreme values of a function f(x,y,z) subject to two constraints, g(x,y,z) = k and h(x,y,z) = l.
*   **Equations and Constraints**
    *   The function T = f(x,y,z) is defined, with variables x, y, and z.
    *   Two constraints are given: g(x,y,z) = k and h(x,y,z) = l.
    *   The equation ∇f = λ∇g + μ∇h is presented, where λ and μ are Lagrange multipliers.
*   **Diagram**
    *   A 3D graph is shown, featuring three surfaces: g(x,y,z) = k (green), h(x,y,z) = l (red), and f(x,y,z) (black).
    *   The intersection of the green and red surfaces forms a curve C.
    *   A point P is marked on curve C, where ∇f is perpendicular to C.
    *   Vectors ∇g and ∇h are depicted, both orthogonal to curve C at point P.
*   **Text and Explanations**
    *   The text explains that along curve C, we seek points P where f(x,y,z) has an extremum or where ∇f is perpendicular to C.
    *   The condition ∇g ≠ ∇h implies that ∇f = λ∇g + μ∇h.
    *   The University of Waterloo logo is displayed in the bottom-right corner.

In summary, the image illustrates the method of Lagrange multipliers for optimizing a function subject to two constraints. The diagram visualizes the intersection of the constraint surfaces and the extremum point on the resulting curve. The accompanying text provides a clear explanation of the mathematical concepts involved.

### Slide 11

The image is a slide from a presentation on the Method of Lagrange Multipliers, specifically discussing the case with two constraints. The slide is divided into sections, each containing relevant information.

*   **Title and Introduction**
    *   The title "Method of Lagrange Multipliers - Two Constraints" is prominently displayed at the top.
    *   The introduction explains that the function $f(x,y,z)$ is subject to two constraints, $g(x,y,z) = k$ and $h(x,y,z) = l$, where $g$ and $h$ are differentiable and $\vec{\nabla}g$ is not parallel to $\vec{\nabla}h$.
*   **Mathematical Formulation**
    *   The Method of Lagrange Multipliers is formulated as $\vec{\nabla}f = \lambda \vec{\nabla}g + \mu \vec{\nabla}h$, where $\lambda$ and $\mu$ are Lagrange multipliers.
    *   The constraints are restated as $g(x,y,z) = k$ and $h(x,y,z) = l$.
*   **Equations**
    *   Equation (1): $\vec{\nabla}f = \lambda \vec{\nabla}g + \mu \vec{\nabla}h$
    *   Equation (2): $g(x,y,z) = k$
    *   Equation (3): $h(x,y,z) = l$
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner.

In summary, the slide presents the Method of Lagrange Multipliers for optimizing a function subject to two constraints, providing the necessary mathematical formulation and equations.

### Slide 12

The image presents a slide from a presentation on optimization problems, specifically focusing on a problem with two constraints. The slide is titled "Optimization Problem - Two Constraints" and is attributed to the University of Waterloo.

*   **Title and Problem Statement**
    *   The title is prominently displayed at the top of the slide.
    *   The problem statement is given below the title: "Find the maximum value of the function f(x,y,z) = x + 2y + 3z on the curve of intersection of the plane x - y + z = 1 and the cylinder x^2 + y^2 = 1."
*   **Solution**
    *   The solution section is introduced with the heading "Solution:".
    *   A handwritten note in blue ink reads: "We are looking for the extreme values of f when (x,y,z) are restricted to lie on the curve of intersection!".
*   **University Logo**
    *   The University of Waterloo's logo is displayed in the bottom-right corner of the slide.
*   **Background and Design Elements**
    *   The background of the slide is white.
    *   A yellow stripe runs along the top edge of the slide, accompanied by a black stripe above it.

In summary, the slide outlines an optimization problem involving finding the maximum value of a function subject to two constraints, and provides a brief note on the approach to solving it.

### Slide 13

The image presents a slide from a presentation on optimization problems, specifically focusing on the concept of two constraints. The title "Optimization Problem - Two Constraints" is prominently displayed at the top.

Here is a detailed breakdown of the image's content:

*   **Title and Main Diagram**
    *   The title "Optimization Problem - Two Constraints" is written in black text at the top of the slide.
    *   A 3D graph is centered in the image, featuring a red plane, a green cylinder, and a black curved line.
    *   The x, y, and z axes are labeled with blue arrows.
*   **Equations and Functions**
    *   The function f(x,y,z) is represented by the black curved line on the graph.
    *   The constraint h(x,y,z) = x^2y^2 - 1 is associated with the green cylinder.
    *   The constraint g(x,y,z) = x - y + z - 1 corresponds to the red plane.
*   **Gradient Vectors and Optimization Conditions**
    *   Gradient vectors ∇f, ∇g, and ∇h are illustrated as arrows pointing in different directions.
    *   The condition ∇f = λ∇g + μ∇h is mentioned, indicating that the gradient of f lies in the plane determined by ∇g and ∇h.
*   **University Logo and Statistics**
    *   The University of Waterloo logo is displayed in the bottom-right corner.
    *   No specific statistics are presented in the image.

In summary, the image illustrates an optimization problem with two constraints, using a 3D graph to visualize the function f(x,y,z) and the constraints h(x,y,z) and g(x,y,z). The gradient vectors and their relationships are also depicted, highlighting the condition for optimal solutions.

### Slide 14

The image presents a slide titled "Optimization Problem - Two Constraints" in large black text at the top, with a yellow line underneath. The slide is divided into sections, each containing mathematical equations and explanations.

*   **Title and Header**
    *   Title: "Optimization Problem - Two Constraints"
    *   Yellow line underneath the title
*   **Mathematical Equations and Explanations**
    *   The first section starts with "Hence," followed by the equation ∇f = λ∇g + μ∇h, labeled as (1).
    *   "Constraints:" is written below, with two equations:
        *   x^2 + y^2 = 1, leading to h(x,y,z) = x^2 + y^2 - 1, labeled as (2)
        *   x - y + z = 1, leading to g(x,y,z) = x - y + z - 1, labeled as (3)
    *   "From (1)," is followed by the equation (1,2,3) = λ(1,-1,1) + μ(2x,2y,0), which is further broken down into three separate equations:
        *   1 = λ + 2xμ, labeled as (4)
        *   2 = -λ + 2yμ, labeled as (5)
        *   3 = λ, labeled as (6)
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner

The slide appears to be part of a lecture on optimization problems with multiple constraints, likely from a mathematics or engineering course at the University of Waterloo.

### Slide 15

The image shows a slide from the University of Waterloo, titled "Optimization Problem - Two Constraints." The slide contains handwritten notes in blue ink, detailing the solution to an optimization problem. The content is as follows:

* The title is prominently displayed at the top of the slide.
* Below the title, the notes begin with the statement: "From (6), λ = 3"
* The subsequent steps are:
  * "In (4) → 1 = 3 + 2xμ → 2xμ = -2 → x = -1/μ ... (7)"
  * "In (5) → 2 = -3 + 2yμ → y = 5/2μ ... (8)"
* The next section is titled "Replacing these values in the constraint eq' (2)"
* The equation is: "(-1/μ)^2 + (5/2μ)^2 = 1 → μ^2 = 29/4"
* The final step is: "μ = ±√29/2 ... (9)"
* The University of Waterloo logo is displayed in the bottom-right corner of the slide.

The slide presents a clear and step-by-step solution to an optimization problem with two constraints, using handwritten notes to guide the viewer through the derivation.

### Slide 16

The image presents a slide titled "Optimization Problem - Two Constraints" from the University of Waterloo, featuring a white background with black text and red handwritten notes. The title is prominently displayed at the top in large, bold, black font.

Below the title, the slide is divided into three sections of red handwritten text and equations, which appear to be a solution to an optimization problem involving two constraints.

*   The first section reads: "(9) IN (7)"
    *   $x = -\frac{1}{\mu} = -\left(\frac{1}{\pm\frac{5}{2}}\right)$
    *   $x = \mp \frac{2}{\sqrt{29}} --- (10)$
*   The second section states: "(9) IN (8)"
    *   $y = \frac{5}{2\mu} = \frac{5}{2(\pm\frac{5}{2})} = \pm \frac{5}{\sqrt{29}} --- (11)$
*   The third section explains: "REPLACING THESE VALUES IN THE CONSTRAINT EQ'(3) WE CAN FIND THE VALUE OF z,"
    *   $z = 1 - x + y$
    *   $= 1 - (\mp \frac{2}{\sqrt{29}}) + (\pm \frac{5}{\sqrt{29}})$

In the bottom-right corner, the University of Waterloo's logo is displayed, consisting of a shield with a red and yellow design, accompanied by the university's name in black text. The overall design suggests that this slide is part of a presentation or lecture on optimization problems, likely used in an academic setting.

### Slide 17

The image presents a white slide with black text and red handwritten notes, titled "Optimization Problem - Two Constraints" in bold black font at the top. The slide is divided into sections, each containing mathematical equations and explanations.

*   **Title**: 
    *   "Optimization Problem - Two Constraints"
    *   Font: bold black
    *   Position: top center of the slide
*   **Mathematical Equations**:
    *   Red handwritten notes throughout the slide
    *   Equations involve variables x, y, z, and f(x,y,z)
    *   Include fractions, square roots, and algebraic expressions
*   **Explanations**:
    *   Black handwritten text below the equations
    *   Discusses the corresponding values of f(x,y,z) and the maximum value of f(x,y,z) subject to constraints
    *   Includes a speech bubble with the equation f(x,y,z) = 3 + √29
*   **University Logo**:
    *   University of Waterloo logo in the bottom-right corner
    *   Yellow shield with a crest and the words "UNIVERSITY OF WATERLOO" in black text
*   **Background**:
    *   White background
    *   Yellow stripe at the top of the slide

The slide appears to be a lecture slide from a mathematics course, specifically discussing optimization problems with two constraints. The equations and explanations are presented in a clear and concise manner, making it easy to follow along.

### Slide 18

The slide is titled "Summary" and contains four bullet points. The first bullet point states, "We have learned two methods for solving optimization problems with constraints," followed by two sub-bullet points that list the methods:

*   The substitution method
*   The method of Lagrange multipliers

The second bullet point reads, "The substitution method requires the reduction of dimensionality and can get difficult if the constraint(s) are complicated."

The third bullet point says, "The method of Lagrange multipliers is a powerful method for finding extreme values of constrained functions and, among others, has applications in machine learning algorithms."

The bottom-right corner of the slide features the logo for the University of Waterloo.

The background of the slide is white, with a yellow stripe at the top.

