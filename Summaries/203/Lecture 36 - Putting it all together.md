# Lecture 36 - Putting it all together

## Study Notes

# Vector Calculus – Problem‑Solving Exam Notes

> **Audience** – Students preparing for exams on line, surface, and volume integrals, and on vector field properties (curl, divergence, conservative fields).

---

## Core Formulas & Definitions

| Formula | Symbols & Meaning | When to Use |
|---------|-------------------|-------------|
| **Fundamental Theorem of Calculus** | \(\displaystyle \int_{a}^{b} f'(x)\,dx = f(b)-f(a)\) | 1‑D definite integrals; evaluating antiderivatives at endpoints. |
| **Fundamental Theorem of Line Integrals** | \(\displaystyle \int_{C} \nabla f \cdot d\mathbf r = f(\mathbf r(b)) - f(\mathbf r(a))\) | Evaluate a line integral of a gradient field; shortcut if \(\mathbf F = \nabla f\). |
| **Normal Form of Green’s Theorem** | \(\displaystyle \iint_{R} \nabla\!\cdot\!\mathbf F\, dA = \oint_{C} \mathbf F \cdot \mathbf n \, ds\) | 2‑D divergence → line integral over the closed boundary. |
| **Tangential (Circulation) Form of Green’s Theorem** | \(\displaystyle \iint_{R} (\nabla \times \mathbf F)\cdot \mathbf k\, dA = \oint_{C} \mathbf F \cdot d\mathbf r\) | 2‑D curl → line integral around \(C\). |
| **Divergence Theorem (Gauss)** | \(\displaystyle \iiint_{E} \nabla\!\cdot\!\mathbf F\, dV = \iint_{S} \mathbf F \cdot \mathbf n\, d\sigma\) | 3‑D volume → surface integral over the boundary. |
| **Stokes’ Theorem** | \(\displaystyle \iint_{S} (\nabla \times \mathbf F)\cdot \mathbf n\, d\sigma = \oint_{C} \mathbf F \cdot d\mathbf r\) | 3‑D curl → line integral around the boundary curve \(C\). |
| **Curl of a Gradient** | \(\displaystyle \nabla \times \nabla f = \mathbf 0\) | Verify irrotationality; shows \(\mathbf F = \nabla f\) is conservative. |
| **Divergence of a Curl** | \(\displaystyle \nabla \cdot (\nabla \times \mathbf F) = 0\) | Identity used in proofs and to confirm vector identities. |
| **Conservative Field Criterion** | \(\displaystyle \nabla \times \mathbf F = \mathbf 0 \;\text{in a simply‑connected domain} \;\Rightarrow\; \mathbf F = \nabla f\) | Determine if a vector field is conservative; find a potential function. |
| **Irrotational Field** | \(\displaystyle \nabla \times \mathbf F = \mathbf 0\) | Field has no local “rotation”; useful for potential flow problems. |
| **Divergence Zero (Solenoidal) Field** | \(\displaystyle \nabla \cdot \mathbf F = 0\) | Indicates incompressible flow, magnetic fields, etc. |

---

## Key Concepts & Intuition

- **Orientation Matters**  
  - Boundary curve \(C\) orientation must match the normal \(\mathbf n\) on the surface via the right‑hand rule.  
  - For Green’s Theorem, a positively oriented (counter‑clockwise) boundary corresponds to outward normal on the region.

- **Domain Topology**  
  - Conservative ↔ irrotational **only** if the domain is simply connected.  
  - Non‑simply connected domains (e.g., punctured plane) can have non‑zero curl yet still be conservative on some subdomains.

- **Physical Interpretation**  
  - Divergence measures “outflow” of a field from a point.  
  - Curl measures local rotation or circulation.  
  - Surface/volume integrals capture global flux or circulation.

- **Identity Relationships**  
  - Curl of a gradient = 0; divergence of a curl = 0.  
  - These identities often simplify complex integrals or verify vector calculus theorems.

---

## Problem‑Solving Strategies

### 1. **Line Integral of a Vector Field**
| Cues | Checklist |
|------|-----------|
| “Line integral”, “curve \(C\)”, “parameterization” | 1. Write \(\mathbf r(t)\), \(a\le t \le b\).  <br>2. Compute \(d\mathbf r = \mathbf r'(t) dt\).  <br>3. Evaluate \(\int_{a}^{b} \mathbf F(\mathbf r(t)) \cdot \mathbf r'(t) \, dt\). |
| “Conservative field”, “potential function” | 1. Check if \(\nabla\times\mathbf F = 0\) on domain.  <br>2. If yes, find \(f\) such that \(\nabla f = \mathbf F\).  <br>3. Use Fundamental Theorem of Line Integrals: \(f(\mathbf r(b))-f(\mathbf r(a))\). |
| **Pitfall** | Forget to check domain connectivity; sign errors in parameterization. |

---

### 2. **Surface Integral (Flux)**
| Cues | Checklist |
|------|-----------|
| “Flux”, “\(\mathbf F \cdot \mathbf n\)” | 1. Parameterize the surface \(S\) via \(\mathbf r(u,v)\).  <br>2. Compute \(\mathbf r_u \times \mathbf r_v\) to obtain normal vector (pointing outward if specified).  <br>3. Integrate \(\int\int_S \mathbf F \cdot \mathbf n \, d\sigma = \int\int_D \mathbf F(\mathbf r(u,v)) \cdot (\mathbf r_u \times \mathbf r_v)\,du\,dv\). |
| “Use Divergence Theorem” | 1. Identify a volume \(E\) bounded by \(S\).  <br>2. Compute \(\iiint_E \nabla\!\cdot\!\mathbf F\, dV\).  <br>3. Result equals surface flux. |
| **Pitfall** | Mis‑direction of \(\mathbf n\); forgetting to include Jacobian when changing variables. |

---

### 3. **Applying Green’s Theorem (2‑D)**
| Cues | Checklist |
|------|-----------|
| “Closed curve \(C\)”, “\(\iint_R\)” | 1. Ensure \(C\) is positively oriented (counter‑clockwise).  <br>2. Choose the appropriate form (normal or tangential).  <br>3. Convert line integral to double integral:  
   - Normal form: \(\oint_C \mathbf F \cdot \mathbf n\, ds = \iint_R \nabla\!\cdot\!\mathbf F \, dA\).  
   - Tangential form: \(\oint_C \mathbf F \cdot d\mathbf r = \iint_R (\nabla \times \mathbf F)\cdot\mathbf k\, dA\). |
| **Pitfall** | Forgetting that \(\mathbf n\) for normal form points outward; sign errors for circulation. |

---

### 4. **Applying Stokes’ Theorem (3‑D)**
| Cues | Checklist |
|------|-----------|
| “Boundary curve \(C\)”, “Surface \(S\)” | 1. Verify orientation: \(\mathbf n\) chosen such that right‑hand rule matches \(C\).  <br>2. Compute \(\iint_S (\nabla \times \mathbf F)\cdot\mathbf n\, d\sigma\) or \(\oint_C \mathbf F \cdot d\mathbf r\). |
| **Pitfall** | Incorrect surface choice (e.g., using wrong portion of a sphere). |

---

### 5. **Checking Conservativeness**
| Cues | Checklist |
|------|-----------|
| “Curl zero”, “path independence” | 1. Compute \(\nabla \times \mathbf F\).  <br>2. If zero everywhere in the domain AND the domain is simply connected, then \(\mathbf F\) is conservative.  <br>3. Find potential \(f\) by integrating components and matching. |
| **Pitfall** | Assuming conservative on non‑simply connected domain; missing constant terms when integrating. |

---

### 6. **Verifying Vector Identities**
| Cues | Checklist |
|------|-----------|
| “Divergence of curl”, “Curl of gradient” | 1. Use standard identities directly: \(\nabla\!\cdot(\nabla\times\mathbf F)=0\), \(\nabla\times(\nabla f)=0\).  <br>2. If required, compute component-wise to confirm. |
| **Pitfall** | Forgetting that the identity holds under smoothness assumptions (continuous second‑order partials). |

---

## Common Pitfalls & Checks

1. **Orientation Checks**  
   - Use right‑hand rule for Stokes and Divergence Theorems.  
   - For Green’s normal form, boundary orientation must be counter‑clockwise for outward normal.

2. **Domain Connectivity**  
   - Verify simply connectedness before concluding conservativeness.  
   - For punctured regions, a non‑zero curl may still allow a potential on a restricted subdomain.

3. **Parameterization Direction**  
   - Re‑check the limits of integration after parameterizing curves or surfaces.  
   - A reversed parameterization flips the sign of the integral.

4. **Smoothness Conditions**  
   - Theorems assume continuous partial derivatives.  
   - Check if given fields meet these conditions; if not, the theorem may not apply.

5. **Units & Dimensions**  
   - Ensure consistency when interpreting physical applications (e.g., flux vs. circulation).  

6. **Zero Results**  
   - If the result is zero, verify whether it’s due to symmetry, identity, or a computational error.  

---

### Quick Reference: How to Choose a Theorem

| Situation | Pick |
|-----------|------|
| Evaluate \(\int_C \mathbf F\cdot d\mathbf r\) | Use Fundamental Theorem of Line Integrals (if \(\mathbf F=\nabla f\)), else use Stokes if 3‑D, Green’s tangential if 2‑D |
| Evaluate \(\oint_C \mathbf F\cdot \mathbf n\, ds\) | Use Green’s normal form (2‑D), Divergence Theorem (3‑D) |
| Compute \(\iint_S \mathbf F\cdot \mathbf n\, d\sigma\) | Divergence Theorem (if volume integral easier), else direct surface integration |
| Compute \(\iint_S (\nabla \times \mathbf F)\cdot \mathbf n\, d\sigma\) | Stokes’ Theorem (reduce to line integral) |
| Verify \(\mathbf F\) is conservative | Check curl; if zero and domain simply connected, then potential exists |

---

**End of Notes**

---

## Raw Slide Summaries

### Slide 1

The slide titled "Putting It All Together" contains the following elements:
* A title in large black text at the top.
* A yellow rectangle with the text "Trim Ch 14, 14.1-14.10" in black.
* An image of a sailboat on rough seas, with the caption "Pascal Oddo's Leopard 3 in rough seas during the 2017 Rolex Middle Sea Race" and a URL "(https://i.imgur.com/30iDYV3.jpg)" below it.
* The University of Waterloo logo in the bottom-left corner.

The image of the sailboat shows:
* A boat sailing on turbulent water with large waves.
* The boat is tilted to one side, with its sails raised.
* People are visible on the boat, likely the crew. 
* The overall atmosphere suggests a competitive sailing event, with the boat navigating through challenging sea conditions.

### Slide 2

The image presents a white slide with a title, "Green's and Divergence Theorem," in bold black text at the top. The slide is divided into two main sections, each containing a mathematical equation and an accompanying diagram.

**Equations and Diagrams**

*   **Left Section**
    *   Equation: ∫∫F·nds = ∫∫∇·FdA
    *   Diagram: A green oval shape labeled "R" with arrows pointing outward, surrounded by a blue coordinate system (x, y, z). The diagram is titled "Normal Form of Green's Theorem."
*   **Right Section**
    *   Equation: ∫∫F·nds = ∫∫∫∇·FdV
    *   Diagram: A green oval shape labeled "E" with arrows pointing outward, surrounded by a blue coordinate system (x, y, z). The diagram is titled "Divergence Theorem."

**Additional Elements**

*   A logo for the University of Waterloo is displayed in the bottom-right corner.
*   The slide features a yellow bar at the top, with a black bar above it.

**Summary**

The slide effectively illustrates the concepts of Green's Theorem and the Divergence Theorem, providing a clear visual representation of the mathematical equations and their applications.

### Slide 3

The image presents a lecture slide titled "Green's and Stokes' Theorem" in bold black text at the top, set against a white background with a yellow stripe underneath the title. The slide is divided into two main sections, each featuring a mathematical equation and accompanying diagrams.

* **Left Section:**
	+ Equation: $\oint_{C} \vec{F}.d\vec{r}=\iint_{S} (\vec{\nabla} \times \vec{F}) \cdot \hat{k}dA$
	+ Diagram: A 3D coordinate system with x, y, and z axes, featuring a green oval shape labeled "R" on the xy-plane, surrounded by purple arrows indicating the direction of the vector field $\vec{F}$. The diagram is annotated with various mathematical symbols and notations.
	+ Text: "Line Integral over C" and "Sum of Curls over R"
	+ Subtitle: "Circulation - Curl or Green's Tangential Form"
* **Right Section:**
	+ Equation: $\oint_{C} \vec{F}.d\vec{r}=\iint_{S} (\vec{\nabla} \times \vec{F}) \cdot \hat{n}d\sigma$
	+ Diagram: A 3D surface labeled "S" with a purple boundary curve "C", featuring a red arrow pointing outward from the surface, representing the normal vector $\hat{n}$. The diagram is annotated with various mathematical symbols and notations.
	+ Text: "Line Integral over C" and "Sum of Curls over S"
	+ Subtitle: "Stokes's Theorem"

The slide also features a logo for the University of Waterloo in the bottom-right corner, indicating the institution associated with the lecture.

In summary, the image presents a clear and concise explanation of Green's and Stokes' Theorems, using a combination of mathematical equations, diagrams, and annotations to illustrate the concepts. The slide provides a comprehensive overview of the theorems, highlighting their significance in vector calculus.

### Slide 4

The image presents a comprehensive overview of the "Unifying the Integral Theorems" in mathematics, specifically focusing on calculus. The title, prominently displayed at the top, sets the stage for an in-depth exploration of various integral theorems.

The content is organized into six main bullet points, each highlighting a distinct theorem:

*   **Fundamental Theorem of Calculus**: This theorem is represented by the equation ∫[a,b] f'(x) dx = f(b) - f(a), which illustrates the relationship between the derivative of a function and its antiderivative.
*   **Fundamental Theorem of Line Integrals**: The equation ∫C ∇f · d**r** = f(**r**(b)) - f(**r**(a)) demonstrates how the line integral of a gradient field can be evaluated using the function's values at the endpoints of the curve.
*   **Normal Form of Green's Theorem**: The equation ∬R ∇·**F** dA = ∮C **F** · **n** ds relates the double integral of the divergence of a vector field over a region to the line integral of the vector field around the boundary of that region.
*   **Divergence Theorem**: The equation ∭E ∇·**F** dV = ∬S **F** · **n** dσ connects the triple integral of the divergence of a vector field within a volume to the surface integral of the vector field over the enclosing surface.
*   **Tangential Form of Green's Theorem**: The equation ∬R (∇×**F**) · **k** dA = ∮C **F** · d**r** shows how the double integral of the curl of a vector field over a region is related to the line integral of the vector field around the boundary.
*   **Stokes' Theorem**: The equation ∬S (∇×**F**) · **n** dσ = ∮C **F** · d**r** generalizes the tangential form of Green's theorem to three dimensions, linking the surface integral of the curl of a vector field to the line integral around the boundary of the surface.

Each theorem is accompanied by a brief description or annotation, providing additional context and highlighting key aspects of the equations. The use of different colors for certain parts of the equations (e.g., yellow highlighting) draws attention to specific components, such as the dot product or cross product operations.

In the bottom-right corner, the logo of the University of Waterloo is displayed, indicating the academic institution associated with the presentation or resource. Overall, the image serves as a concise yet informative summary of fundamental theorems in calculus, making it a valuable reference for students and professionals alike.

### Slide 5

The image presents a slide from a lecture on vector calculus, specifically focusing on the concepts of curl and conservative fields. The title "Curl and Conservative Fields" is prominently displayed at the top.

**Title and Introduction**

*   The title "Curl and Conservative Fields" is written in large black text.
*   Below the title, a statement reads: "If a scalar function f(x,y,z) has continuous second-order partial derivatives, calculate," followed by the expression "curl(∇f)".

**Solution and Explanation**

*   The solution to the problem is presented in three lines of handwritten text:
    *   "curl (∇f) = ∇ × ∇f → curl (∇f) = 0"
    *   "If F = ∇f over an simply-connected domain → curl (F) = 0 irrotational F"
*   A note in blue text explains that "The curl(F) gives us a way to verify if F is a conservative field, and if it is equal to zero, F irrotational."

**Logo and Footer**

*   In the bottom-right corner, the logo for the University of Waterloo is displayed, featuring a shield with a red crest and the words "UNIVERSITY OF WATERLOO" in black text.

**Background and Design**

*   The background of the slide is white, with a yellow stripe at the top and a black stripe above it.

### Slide 6

The image presents a slide from a lecture on vector calculus, titled "Curl and Divergence" in bold black text at the top. The slide is divided into three sections: the title, the problem statement, and the solution.

*   **Title**
    *   "Curl and Divergence" in bold black text
*   **Problem Statement**
    *   For the vector field $\vec{F} = P\hat{i} + Q\hat{j} + R\hat{k}$, calculate the $\operatorname{Div}(\vec{\nabla} \times \vec{F})$.
*   **Solution**
    *   $\operatorname{Div}(\vec{\nabla} \times \vec{F}) = \vec{\nabla} \cdot (\vec{\nabla} \times \vec{F})$
    *   $\operatorname{Div}(\operatorname{curl} \vec{F}) = 0$
    *   "ZERO FLUX!!" with an arrow pointing to the equation
    *   A diagram illustrating the concept of curl and divergence, featuring blue arrows and red annotations
    *   "These results tell us that something that just circles around a point, has zero flux through it." in blue text
*   **Logo and University Name**
    *   The University of Waterloo logo is displayed in the bottom-right corner, accompanied by the university's name in black text.

In summary, the slide provides a step-by-step solution to the problem of calculating the divergence of the curl of a vector field, highlighting the result that the divergence of the curl is always zero. The accompanying diagram and text help to illustrate the concept and its implications.

### Slide 7

The image presents a summary slide from a presentation on vector calculus, featuring a white background with black text and a yellow stripe at the top. The title "Summary" is prominently displayed in large black font on the left side of the slide.

*   The del operator $\vec{\nabla}$ plays an important role in many fields of engineering
    *   If $\vec{\nabla} \times \vec{F} = 0$ at every point of a simply connected open region D in space, then $\vec{F}$ is conservative.
        *   $\operatorname{Div}(\vec{\nabla} \times \vec{F})$ is always zero
*   Green's circulation-curl or tangential form is the 2D version of Stoke's Theorem
*   Green's flux-divergence or normal form is the 2D version of the Divergence Theorem
*   All these theorems are all higher dimensional versions of the fundamental theorem of calculus

The slide effectively summarizes key concepts in vector calculus, highlighting the significance of the del operator and its applications in various engineering fields. It also provides a concise overview of important theorems, including Green's Theorem and the Divergence Theorem, and their relationships to Stoke's Theorem and the fundamental theorem of calculus.

