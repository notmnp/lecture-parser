# Lecture 21 - Absolute Maxima and Minima and Optimization

## Study Notes

# Extreme Value & Optimization in Two Variables  
*Exam‑ready, problem‑solving focused notes.*

---

## Core Formulas & Definitions  

| Formula / Definition | LaTeX | Key Symbols | When to Use |
|----------------------|-------|-------------|-------------|
| **Extreme Value Theorem** | $f$ continuous on closed, bounded $D \subset \mathbb R^2 \;\Longrightarrow\; f$ attains an absolute max/min on $D$ | $f$: function, $D$: domain | Before searching for candidates. |
| **Critical Point (interior)** | $\nabla f(x,y)=0\;\iff\;f_x(x,y)=0,\;f_y(x,y)=0$ | $f_x,f_y$: first partials | Interior extrema. |
| **Hessian Determinant** | $D = f_{xx}\,f_{yy}-f_{xy}^2$ | $f_{xx},f_{yy},f_{xy}$: second partials | Classify interior critical points. |
| **Hessian Test** | \[
\begin{cases}
D>0,\;f_{xx}>0 &\Rightarrow \text{local min}\\[2pt]
D>0,\;f_{xx}<0 &\Rightarrow \text{local max}\\[2pt]
D<0 &\Rightarrow \text{saddle}
\end{cases}
\] | | Apply after computing $D$ and ensuring the point lies inside $D$. |
| **Boundary parameterization** | Replace boundary equation in $f$ → single‑variable function $g(t)$ | $t$: parameter along the edge | Reduce to one‑dimensional extremum on each edge. |
| **Vertices** | Evaluate $f$ at each corner of $D$ | | Endpoints of 1‑D edge problems. |
| **Substitution (one constraint)** | Solve $g(x,y)=c$ for one variable, substitute → $h(\text{remaining vars})$ | $c$: constant | Reduce dimensionality before first‑derivative test. |
| **Lagrange multipliers** | $\nabla f = \lambda \nabla g,\;\; g(x,y)=c$ | $\lambda$: multiplier | When $D$ is defined by a smooth equality constraint. |

---

## Key Concepts & Intuition  

- **Domain matters**: Closed & bounded → EVT guarantees extrema.  
- **Interior vs. Boundary**: Extrema can occur anywhere; always check both.  
- **Gradient zero ≠ extremum**: Must classify with second derivatives or direct comparison.  
- **Boundary → 1‑D**: Treat remaining variable as independent; apply standard EVT.  
- **Vertices**: Always evaluate; they can hold extrema even if no edge critical points exist.  
- **Substitution**: Eliminates a variable but keep domain restrictions (e.g., $x\ge 0$).  
- **Second‑Derivative Test**: Definitive classification when $D>0$ and the point is interior.  

---

## Problem‑Solving Strategies  

### 1. Absolute Extremum on a Closed Polygon  

1. **Interior**  
   - Compute $f_x,\;f_y$.  
   - Solve $\nabla f=0$.  
   - Keep only solutions that lie inside $D$.  
2. **Each Edge**  
   - For a linear edge $a x + b y = c$, substitute the constraint into $f$ → $g(t)$ (one variable).  
   - Solve $g'(t)=0$; keep $t$ inside the edge’s interval.  
   - Evaluate $g$ at those critical points and at the edge’s endpoints.  
3. **Vertices**  
   - Evaluate $f$ at every corner point.  
4. **Collect & Compare**  
   - Largest value → absolute maximum; smallest → absolute minimum.  

**Checklist**  
- ☐ Partial derivatives found.  
- ☐ Interior critical points verified to be inside $D$.  
- ☐ Every edge reduced to a 1‑D problem and solved.  
- ☐ Endpoints of edges (vertices) evaluated.  
- ☐ All candidate values compared.  

---

### 2. Optimization with a Single Equality Constraint  

1. **Set up**: Identify objective $f$ and constraint $g(x,y)=c$.  
2. **Solve for one variable** (substitution) or use Lagrange.  
3. **Substitution method**  
   - Solve $g$ for a variable, e.g. $x=c-2y-2z$.  
   - Substitute into $f$ → reduced objective $h(\text{remaining vars})$.  
   - Compute first partials of $h$, set to zero, solve.  
   - Verify solutions satisfy the original constraint and any domain inequalities.  
   - Apply second‑derivative test to classify.  
4. **Lagrange method** (if substitution messy)  
   - Form $\mathcal{L}=f-\lambda(g-c)$.  
   - Solve $\partial\mathcal{L}/\partial x=\partial\mathcal{L}/\partial y=\partial\mathcal{L}/\partial\lambda=0$.  
5. **Boundary of the reduced domain**  
   - Check cases where a substituted variable equals a boundary value (e.g., $y=0$).  
   - Evaluate $f$ at these boundary points.  

**Checklist**  
- ☐ Correct substitution and simplification.  
- ☐ All partial derivatives correct.  
- ☐ Solutions respect the constraint and inequalities.  
- ☐ Second‑derivative test applied and interpreted.  
- ☐ Boundary cases examined.  

---

### 3. Lagrange Multiplier Method (general)  

1. **Set up**: $\mathcal{L}(x,y,\lambda)=f(x,y)-\lambda(g(x,y)-c)$.  
2. **Equations**:  
   - $f_x=\lambda g_x$  
   - $f_y=\lambda g_y$  
   - $g(x,y)=c$  
3. **Solve** for $x,y,\lambda$.  
4. **Verify** each solution lies in the domain.  
5. **Evaluate** $f$ at each solution.  
6. **Compare** to find the absolute max/min.  

---

## Common Pitfalls & Checks  

| Mistake | Reason | Fix |
|---------|--------|-----|
| Skipping boundary analysis | Belief that interior suffices | Parameterize every edge; check endpoints. |
| Forgetting vertices | Think edge analysis covers them | Explicitly evaluate all corners. |
| Using Hessian at a boundary point | Hessian test only for interior | Apply Hessian only when $\nabla f=0$ **and** point is interior. |
| Wrong domain after substitution | Ignored inequalities (e.g., $x\ge0$) | Keep inequalities; test all candidate points against them. |
| Sign errors in $D$ | Mistyping $f_{xx},f_{yy},f_{xy}$ | Double‑check signs; use $D=f_{xx}f_{yy}-f_{xy}^2$. |
| Ignoring 1‑D interval limits | Assume any critical point is valid | Verify each critical point lies within the reduced domain interval. |
| Omitted constraint equation in Lagrange | Forgot to solve $g=c$ | Always solve $\nabla f=\lambda\nabla g$ **and** $g=c$ together. |

---

## Quick Reference – Decision Tree  

```
┌─ Is f continuous on closed, bounded D? ──┐
│                                           │
│  No → No guaranteed extrema; check limits. │
│                                           │
└─────────────┬───────────────────────┘
              │
              ▼
┌─ Smooth equality constraint? ──┐
│                               │
│  Yes → Use Lagrange or Subst. │
│  No  → Find interior crit.    │
│                               │
└─────────────┬───────────────────────┘
              │
              ▼
┌─ Need boundary analysis? ──┐
│                             │
│  Yes → Parameterize edges,  │
│  reduce to 1‑D, solve,      │
│  evaluate endpoints.       │
│  No  → Skip.                │
│                             │
└─────────────┬───────────────────────┘
              │
              ▼
Evaluate vertices → Compare all candidates.
```

---

## Practice Problem (Box Optimization)

**Maximize** $V = xyz$  
**Subject to** $x+2y+2z = 108$, $x,y,z \ge 0$.

1. **Substitute** $x = 108-2y-2z$.  
2. **Objective** $V(y,z) = (108-2y-2z)yz$.  
3. **Partial derivatives**  
   \[
   V_y = 108z - 4yz - 2z^2,\qquad
   V_z = 108y - 4yz - 2y^2.
   \]
4. **Solve** $V_y = 0$, $V_z = 0$ → $y = z = 18$.  
5. **Compute** $x = 108 - 2(18) - 2(18) = 36$.  
6. **Second‑derivative test**  
   \[
   V_{yy} = -4z,\; V_{zz} = -4y,\; V_{yz} = 108-4y-4z.
   \]
   At $(18,18)$: $V_{yy} = V_{zz} = -72$, $V_{yz} = -72$ → $D = V_{yz}^2 - V_{yy}V_{zz} = (-72)^2 - (-72)(-72) = -3888 < 0$ → local (and global) maximum.  
7. **Volume** $V = 36 \times 18 \times 18 = 11\,664$.  
8. **Boundary check**: If any variable is $0$, $V=0$ – smaller than $11\,664$.  

**Answer**: Largest volume $11\,664$ at dimensions $(36,\,18,\,18)$.  

---

---

## Raw Slide Summaries

### Slide 1

The slide is titled "Absolute Maximum and Minimum" and features a 3D graph with a grid surface plot. The title is prominently displayed in large black text at the top left of the slide.

**Key Elements:**

* **Title and Reference:** 
  - Title: "Absolute Maximum and Minimum"
  - Reference: "Trim Ch 11, S. 12.11" in a yellow box below the title.

* **3D Graph:**
  - The graph is a grid surface plot with a complex shape, featuring multiple peaks and valleys.
  - The graph has three axes: x, y, and z.
  - The z-axis is labeled, and the function being plotted is f(x,y).
  - Several points on the graph are highlighted with red dots and labeled as "Local Maximum" or "Local Minimum".

* **Outline:**
  - The outline is presented in two points:
    1. Extreme Value Theorem for z = f(x,y)
    2. Optimization problems with constraint(s)

* **University Logo:**
  - The University of Waterloo logo is displayed in the bottom-left corner of the slide.

Overall, the slide appears to be introducing the concept of absolute maximum and minimum values in multivariable calculus, with a focus on the Extreme Value Theorem and optimization problems.

### Slide 2

The image presents a slide from a presentation on the topic of "Why absolute maximum and minimum values?" The slide is divided into five main bullet points, each with subpoints that provide further information.

*   The first main bullet point reads: "One of the main uses of ordinary and partial derivatives is in finding maximum and minimum values"
    *   The subpoints under this heading are:
        *   "The minimum time to make a certain journey"
        *   "The dimensions of a box to maximize volume"
*   The second main bullet point states: "For y = f(x), the extreme value theorem says that if f(x) is continuous on a closed interval [a, b], then f(x) has an absolute minimum and absolute maximum values."
*   The third main bullet point asks: "How did we find these values?"
    *   The subpoints under this heading are:
        *   A mathematical equation: $\frac{df}{dx} = 0 \rightarrow cp$
        *   Another mathematical equation: $\frac{d^2f}{dx^2} = 0$
        *   The text "Check end Points" is written below these equations.
*   The fourth main bullet point explains: "There is a similar situation for functions of two variables. Just as a closed interval [a, b] contains its end points, a closed bounded set in $\mathbb{R}^2$ is one that contains all its boundary points."
*   A graph is displayed on the right side of the slide, illustrating the concept of critical points (cp) and how they relate to the maximum and minimum values of a function.

The slide provides a concise overview of the importance of absolute maximum and minimum values in calculus, highlighting their applications and the methods used to find them. The use of mathematical equations and a graph helps to clarify the concepts being discussed.

### Slide 3

The image is a slide from a presentation on the Extreme Value Theorem for multivariable calculus, specifically for functions of two variables, z = f(x,y). The slide is titled "Extreme Value Theorem for z = f(x,y)" and features a 3D graph with a colored surface representing the function f(x,y).

*   **Title**: 
    *   "Extreme Value Theorem for z = f(x,y)"
*   **3D Graph**:
    *   A 3D graph with a colored surface representing the function f(x,y).
    *   The graph has several labeled points:
        *   Absolute Maximum: f(x1,y1)
        *   Local Maximum
        *   Local Minimum
        *   Absolute Minimum: f(x2,y2)
    *   The graph is bounded by a region D in R^2.
*   **Text**:
    *   "Bounded set D in R^2" (referring to the region bounded by the graph).
    *   "If f(x,y) is continuous on a closed, bounded set D in R^2, then f(x,y) attains an absolute maximum f(x1,y1) and an absolute minimum value f(x2,y2) at some points (x1,y1) and (x2,y2) in D." (a statement of the Extreme Value Theorem).
*   **Logo**:
    *   University of Waterloo logo in the bottom-right corner.

The slide effectively illustrates the concept of the Extreme Value Theorem for functions of two variables, providing a visual representation of the theorem's application.

### Slide 4

The image presents a slide from a lecture on the Extreme Value Theorem for functions of two variables, specifically for $z = f(x,y)$. The slide is titled "Extreme Value Theorem for $z = f(x,y)$" and is attributed to the University of Waterloo.

*   **Title**: 
    *   The title is centered at the top of the slide.
    *   It reads "Extreme Value Theorem for $z = f(x,y)$".
    *   The text is in bold, black font.
*   **Introduction**:
    *   Below the title, there is a brief introduction that explains the purpose of the Extreme Value Theorem.
    *   The text states, "To find the absolute maximum and minimum values of a continuous function $f(x,y)$ on a closed, bounded set D:".
    *   The introduction is written in black text.
*   **Steps to Find Extreme Values**:
    *   The slide outlines four steps to find the extreme values of $f(x,y)$.
    *   Step 1: Find the values of $f(x,y)$ at the critical points of $f(x,y)$ in D.
    *   Step 2: Find the extreme values of $f(x,y)$ on the boundary of D.
    *   Step 3: The largest of the values from steps 1 and 2 is the absolute maximum value.
    *   Step 4: The smallest of the values from steps 1 and 2 is the absolute minimum value.
    *   These steps are numbered and written in black text.
*   **University Logo**:
    *   In the bottom-right corner of the slide, there is a logo for the University of Waterloo.
    *   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.

In summary, the slide provides a clear and concise overview of the Extreme Value Theorem for functions of two variables, outlining the necessary steps to find the absolute maximum and minimum values of a continuous function on a closed, bounded set.

### Slide 5

The image presents a mathematical problem and its solution, featuring two graphs and a detailed explanation.

*   **Problem Statement**
    *   The problem asks to find the absolute maximum and minimum values of the function f(x,y) = x^2 - 2xy + 2y on the rectangle D = {(x,y)|0 ≤ x ≤ 3, 0 ≤ y ≤ 2}.
*   **Solution**
    *   The solution is presented in two parts: a 3D representation of f(x,y) and a bounded set D in R^2.
    *   **3D Representation of f(x,y)**
        *   The 3D graph shows the surface defined by the function f(x,y).
        *   The x-axis ranges from 0 to 3, and the y-axis ranges from 0 to 2.
        *   The z-axis represents the value of the function f(x,y).
    *   **Bounded Set D in R^2**
        *   The graph illustrates the rectangular region D in the xy-plane.
        *   The region is defined by the inequalities 0 ≤ x ≤ 3 and 0 ≤ y ≤ 2.
        *   The vertices of the rectangle are labeled as (0,0), (3,0), (3,2), and (0,2).
        *   The boundaries of the rectangle are labeled as L1, L2, L3, and L4, corresponding to the equations y = 0, y = 2, x = 0, and x = 3, respectively.

In summary, the image provides a clear and concise presentation of a mathematical problem and its solution, utilizing visual aids to facilitate understanding. The 3D representation of the function and the graph of the bounded set D in R^2 effectively illustrate the concepts involved.

### Slide 6

The image displays a slide from a presentation about solving a mathematical problem. The title of the slide is "Problem - Solution" in large black text at the top.

*   **Title and Header**
    *   The title is centered and written in bold, black font.
    *   Below the title, there is a yellow bar that spans the width of the slide.
*   **Domain D**
    *   The domain D is defined as the set of all points (x,y) such that 0 ≤ x ≤ 3 and 0 ≤ y ≤ 2.
    *   This is represented by the equation: D = {(x,y) | 0 ≤ x ≤ 3, 0 ≤ y ≤ 2}
*   **Step 1: Finding Critical Points**
    *   The task is to find the critical points of the function f(x,y) = x^2 - 2xy + 2y within the domain D.
    *   To do this, we need to calculate the partial derivatives of f with respect to x and y.
    *   The partial derivative with respect to x is fx = 2x - 2y.
    *   The partial derivative with respect to y is fy = -2x + 2.
    *   We set both partial derivatives equal to zero to find the critical points: fx = 2x - 2y = 0 and fy = -2x + 2 = 0.
    *   Solving these equations simultaneously yields the critical point (1,1).
    *   Evaluating f at this critical point gives f(1,1) = 1.
*   **University Logo**
    *   In the bottom-right corner of the slide, there is a logo for the University of Waterloo.

The slide provides a clear and concise solution to the problem, following a step-by-step approach to find the critical points of the given function within the specified domain.

### Slide 7

The image presents a slide from a lecture on the topic of finding extreme values of a function on the boundary of a given domain. The title "Problem - Solution" is prominently displayed at the top, followed by the step-by-step solution to the problem.

**Title and Problem Statement**

*   **Title:** Problem - Solution
*   **Step 2:** Find the extreme values of $f(x,y) = x^2 - 2xy + 2y$ on the boundary of D

**Graphs and Equations**

The slide features two graphs, each representing a different part of the boundary of the domain D.

*   **Graph 1:**
    *   Equation: $L_1: x = 3; 0 \leq y \leq 2$
    *   Graph: A vertical line segment from (3,0) to (3,2)
    *   Function: $f(3,y) = 9 - 4y$
    *   Analysis: Decreasing function of y, with no critical points
    *   Endpoints: $y = 0 \rightarrow f(3,0) = 9$, $y = 2 \rightarrow f(3,2) = 1$
*   **Graph 2:**
    *   Equation: $L_2: y = 2; 0 \leq x \leq 3$
    *   Graph: A horizontal line segment from (0,2) to (3,2)
    *   Function: $f(x,2) = x^2 - 4x + 4$
    *   Analysis: Critical point at $x = 2$, where $f'(x,2) = 2x - 4 = 0$
    *   Critical Point: $x = 2 \rightarrow f(2,2) = 0$
    *   Endpoints: $x = 0 \rightarrow f(0,2) = 4$, $x = 3 \rightarrow f(3,2) = 1$

**University Logo**

*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

This detailed summary captures all the content present on the slide, including equations, formulas, definitions, bullet points, and written text, as well as descriptions of the graphs and their corresponding analyses.

### Slide 8

The image presents a mathematical problem and its solution, focusing on the analysis of a function f(x,y) = x^2 - 2xy + 2y over specific boundary conditions defined by lines L3 and L4.

**Problem-Solution Slide**

*   The title "Problem - Solution" is prominently displayed at the top.

**Line L3 Analysis**

*   L3 is defined by the equation x = 0, with y ranging from 0 to 2.
*   A graph illustrating L3 is shown, with the line segment highlighted in yellow on the y-axis.
*   The function f(x,y) is evaluated along L3, simplifying to f(0,y) = 2y.
*   The derivative of f(0,y) with respect to y is 2, indicating a constant rate of change.
*   The end points of L3 are analyzed:
    *   At y = 0, f(0,0) = 0.
    *   At y = 2, f(0,2) = 4.

**Line L4 Analysis**

*   L4 is defined by the equation y = 0, with x ranging from 0 to 3.
*   A graph illustrating L4 is shown, with the line segment highlighted along the x-axis.
*   The function f(x,y) is evaluated along L4, simplifying to f(x,0) = x^2.
*   The function f(x,0) is an increasing function of x.
*   The end points of L4 are analyzed:
    *   At x = 0, f(0,0) = 0.
    *   At x = 3, f(3,0) = 9.

**University Logo**

*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

### Slide 9

The image presents a slide from a lecture on multivariable calculus, specifically focusing on finding the absolute extrema of a function. The slide is titled "Problem - Solution" and is attributed to the University of Waterloo.

*   **Title and Step 3**
    *   The title "Problem - Solution" is prominently displayed at the top.
    *   Below the title, "Step 3:" is written in blue, followed by a description of the step in black text.
*   **Text Describing Step 3**
    *   The text explains that the task is to compare all values of $f(x,y)$ at critical points (CP) and boundaries of $f(x,y)$ in D to determine absolute extrema.
*   **List of Function Values**
    *   A list of six function values is provided, with corresponding annotations:
        *   $f(1,1) = 1$
        *   $f(3,0) = 9 \rightarrow$ ABS MAX
        *   $f(3,2) = 1$
        *   $f(2,2) = 0 \rightarrow$ ABS MIN
        *   $f(0,2) = 4$
        *   $f(0,0) = 0 \rightarrow$ ABS MIN
*   **3D Graph**
    *   A 3D graph is shown, illustrating the function $f(x,y)$ over the region D.
    *   The graph features a grid pattern on its surface and is colored with a gradient effect.
    *   The x-axis ranges from 0 to 3, the y-axis from 0 to 2, and the z-axis from 0 to 9.
    *   The region D is highlighted in beige within the graph.
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner of the slide.

In summary, the slide outlines the third step in solving a problem involving the determination of absolute extrema for a given function $f(x,y)$ within a specified region D. It provides a list of function values at critical points and boundaries, along with annotations indicating the absolute maximum and minimum values. The accompanying 3D graph visualizes the function's behavior over the region D.

### Slide 10

The image is a slide from a presentation about optimization problems with constraints. The title of the slide is "Solving Optimization Problems with Constraints" in large black text at the top center.

*   **Title and Subtitle**
    *   Title: Solving Optimization Problems with Constraints
    *   Subtitle: Trim Ch 11, S. 12.11
*   **Image**
    *   A drone flying in the sky
    *   The drone has four propellers and a white box attached to it
    *   The background is a blue sky with some clouds and trees below
*   **University Logo and URL**
    *   University of Waterloo logo on the bottom left
    *   URL: https://www.voanews.com/silicon-valley-technology/600000-commercial-drones-could-fill-us-skies-next-year on the bottom right
*   **Background**
    *   White background with a yellow bar at the top

The slide appears to be part of a course or lecture on optimization problems, and the image of the drone suggests that the topic may be related to real-world applications such as drone technology.

### Slide 11

The image presents a slide from a lecture on the substitution method, specifically focusing on a problem involving a delivery company's use of an unmanned aerial drone to transport packages. The slide is divided into sections, each with its own distinct content.

**Title and Problem Statement**

*   The title "Substitution Method - One Constraint" is prominently displayed in black text against a yellow background.
*   Below the title, a problem statement is presented in black text, describing the scenario: A delivery company uses a drone to pick up packages from their warehouse and deliver them to clients. The drone can only carry rectangular boxes with a combined length and girth (perimeter of a cross-section) not exceeding 108 inches. The task is to find the dimensions of an acceptable box of the largest volume that the drone can pick up.

**Solution**

*   The solution is outlined in two steps, with the first step being "Setup the objective and constraint(s) functions describing the physics of the problem."
*   A diagram of a rectangular box is shown, labeled with dimensions x, y, and z.
*   The volume of the box is represented by the equation V(x,y,z) = xyz.
*   The girth is defined as 2y + 2z.
*   The constraint is given as x + 2y + 2z = 108.
*   The objective is to maximize the volume under this constraint.

**Additional Information**

*   The University of Waterloo logo is displayed in the bottom-right corner of the slide.
*   The background of the slide is white, providing a clean and neutral backdrop for the content.

Overall, the slide effectively communicates the problem and its solution, using a clear and concise format to guide the viewer through the steps involved in applying the substitution method to optimize the volume of a rectangular box under a given constraint.

### Slide 12

The image presents a slide from a presentation on the "Substitution Method - One Constraint" topic, likely from a mathematics or optimization course at the University of Waterloo.

*   **Title and Step 2**
    *   The title is "Substitution Method - One Constraint."
    *   Step 2: Solve the constraint equation for one variable and substitute into the objective function.
        *   The constraint equation is solved for x: $x = 108 - 2y - 2z$
        *   The objective function V(y,z) is then expressed in terms of y and z: $V(y,z) = (108 - 2y - 2z)(y)(z)$
        *   Simplifying, we get: $V(y,z) = 108yz - 2y^2z - 2z^2y$
*   **Step 3**
    *   Step 3: Find the critical points within the domain (apply first derivative test).
        *   The partial derivative of V with respect to y is calculated: $V_y(y,z) = 108z - 4yz - 2z^2$
        *   Setting $V_y(y,z) = 0$, we have: $z(108 - 4y - 2z) = 0$ --- (1)
*   **Definition of Critical Point**
    *   A point (a,b) in the domain of f(x,y) is said to be a critical point if:
        *   $\frac{\partial f}{\partial x}|_{a,b} = 0$ and $\frac{\partial f}{\partial y}|_{a,b} = 0$
        *   Or if one (or both) of these derivatives does not exist at (a,b).
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner.

In summary, the slide outlines the steps for applying the substitution method to optimize a function subject to one constraint. It provides detailed calculations for Step 2 and Step 3, including the derivation of the objective function in terms of two variables and the computation of its partial derivative. Additionally, it defines what constitutes a critical point for a multivariable function.

### Slide 13

The lecture slide is titled "Substitution Method - One Constraint" and contains the following information:

*   The equation: $V_3 (y,z) = 108y - 2y^2 - 4yz$
    *   Simplified to: $= y(108-2y-4z) = 0 \cdots (2)$
*   The text: "Solving (1) AND (2)" 
    *   Followed by four points: 
        *   $(0,0)$
        *   $(0,54)$
        *   $(54,0)$
        *   $(18,18)$
*   The annotation: "{ VOWNE FUNCTION ZERO! }" next to the first three points.

In the bottom-right corner, there is a logo for the "UNIVERSITY OF WATERLOO." The background of the slide is white, with a black and yellow bar at the top. The title is written in large, bold, black font, while the rest of the text is handwritten in blue.

### Slide 14

The image depicts a lecture slide titled "Substitution Method - One Constraint" in large black text at the top. The slide is divided into sections, with the main content presented below the title.

**Section 1: Step 4 and Equations**

*   The first section states, "Step 4: Apply the second derivative test to show that x = 18 and y = 18 gives us a local maximum of V."
*   A series of handwritten equations in blue ink follows:
    *   From (1) → A = Vyy = -4z
    *   (2) → C = Vzz = -4y
    *   (1) → B = Vyz = 108 - 4y - 4z
    *   D = (108 - 4y - 4z)^2 - 16yz
    *   D|(18,18) = -3888 < 0
    *   A|(18,18) = -72 < 0 → V(18,18) is a MAX. !

**Section 2: Definitions and Conditions**

*   A yellow-outlined box contains four definitions and conditions for determining the nature of a critical point (a, b) using the second derivative test:
    *   A = fxx(a,b), B = fxy(a,b), C = fyy(a,b), D = B^2 - AC = fxy^2 - fxxfyy
    *   Four conditions are listed:
        i.   If D < 0 and A < 0, then (a,b) is a relative maximum.
        ii.  If D < 0 and A > 0, then (a,b) is a relative minimum.
        iii. If D > 0, then (a,b) is a saddle point.
        iv.  If D = 0, no conclusion can be made.

**Section 3: University Logo**

*   In the bottom-right corner, the University of Waterloo logo is displayed, featuring a shield with a red and yellow design, accompanied by the university's name in black text.

The slide provides a clear and concise explanation of the substitution method with one constraint, including the application of the second derivative test to determine the nature of a critical point.

### Slide 15

The image presents a slide from a presentation on the "Substitution Method - One Constraint" topic, likely from a mathematics or optimization course at the University of Waterloo. The slide is divided into two main sections: Step 5 and Step 6.

**Step 5: Solve the constraint equation for the remaining variable of the point of interest**

*   The equation is given as $x = 108 - 24 - 2(18)$, which simplifies to $x = 36$.
*   This step involves substituting the value of $y = 18$ and $z = 18$ into the equation to solve for $x$, resulting in $x = 36$.
*   The solution is indicated by an arrow pointing to the point $(36, 18, 18)$ with a checkmark.

**Step 6: Determine the value of the objective function at that point**

*   The objective function is defined as $V = xyz$.
*   Substituting the values $x = 36$, $y = 18$, and $z = 18$ into the objective function yields $V = (36)(18)(18)$.
*   The calculation results in $V = 11,664 \, m^3$.

**Additional Information**

*   The slide features the University of Waterloo logo in the bottom-right corner.
*   The background of the slide is white, with black text and blue handwriting-style annotations.
*   A yellow bar is visible at the top of the slide, adding a touch of color to the design.

Overall, the slide provides a clear and concise explanation of the substitution method for solving optimization problems with one constraint, using a specific example to illustrate the steps involved.

### Slide 16

The image presents a slide from a presentation on the "Substitution Method - One Constraint" in a clear and structured format. The title, prominently displayed at the top, is followed by six numbered steps that outline the method.

*   **Title**
    *   The title, "Substitution Method - One Constraint," is centered at the top of the slide in large black text.
*   **Six Steps**
    *   The six steps are listed below the title, each with a brief description:
        1.  Determine the objective and constraint(s) function
        2.  Solve the constraint(s) equation for one of the variables and then substitute into the objective function.
        3.  Look for the critical points of the resulting function of two variables and verify that these points agree with the domain
        4.  Apply the second derivative test to determine what kind of critical points you have
        5.  Solve the constraint equation for the remaining variable
        6.  Solve for the corresponding value of the objective function to answer what you have been asked for
*   **University Logo**
    *   In the bottom-right corner, the University of Waterloo logo is displayed, featuring a shield with a red and yellow design, accompanied by the university's name in black text.

In summary, the image provides a concise and step-by-step guide to the Substitution Method - One Constraint, making it a valuable resource for students or professionals seeking to understand this mathematical technique.

### Slide 17

The image displays a slide from a presentation, titled "Summary and Conclusions" in large black text at the top. The title is underlined by a yellow bar that spans the width of the slide.

Below the title, three bullet points are listed in smaller black text:

*   The extreme value theorem translates into a method to find the absolute maximum and minimum values of a continuous function f(x,y), bounded by a set D
*   We have learned the substitution method for solving optimization problems with constraints
*   The substitution method requires the reduction of dimensionality and can get difficult if the constraint(s) are complicated

In the bottom-right corner, a logo features a shield with a red and yellow design, accompanied by the text "UNIVERSITY OF WATERLOO" in black. The background of the slide is white, with a black bar at the top.

### Slide 18

The image is a presentation slide from the University of Waterloo, featuring a white background with a black and yellow border at the top.

*   The University of Waterloo logo is prominently displayed on the left side of the slide.
    *   The logo consists of a shield with a yellow background and a red lion on either side.
    *   A black chevron is positioned in the center of the shield, pointing upwards.
    *   To the right of the shield, the words "UNIVERSITY OF WATERLOO" are written in bold, black font.
*   Below the logo and university name, the text "Thank you" is displayed in large, bold, black font.
*   The slide's background is white, providing a clean and simple backdrop for the content.
*   A thin black and yellow border runs along the top edge of the slide, adding a touch of color and visual interest.

In summary, the image is a straightforward presentation slide that effectively conveys a message of appreciation from the University of Waterloo. The use of the university's logo and branding elements helps to establish credibility and authenticity, while the simple design ensures that the focus remains on the message being conveyed.

