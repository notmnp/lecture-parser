# Lecture 35 - Stoke's Theorem

## Study Notes

# Curl & Stokes’s Theorem – Problem‑Solving Exam Notes

---

## Core Formulas & Definitions

| Formula | What the symbols mean | When you use it |
|---------|-----------------------|-----------------|
| **Curl (vector)** | $$\nabla \times \mathbf{F}= \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k}\\ \partial_x & \partial_y & \partial_z\\ P & Q & R \end{vmatrix}$$ | Find local rotation density of \(\mathbf{F}=P\,\mathbf{i}+Q\,\mathbf{j}+R\,\mathbf{k}\). |
| **Expanded curl** | $$\nabla \times \mathbf{F}= (\partial_y R-\partial_z Q)\,\mathbf{i}
+(\partial_z P-\partial_x R)\,\mathbf{j}
+(\partial_x Q-\partial_y P)\,\mathbf{k}$$ | When the determinant is cumbersome; compute component‑wise. |
| **Zero‑curl (irrotational)** | $$\nabla \times \mathbf{F}=\mathbf{0}$$ | If everywhere true in a simply‑connected region, \(\mathbf{F}\) is conservative. |
| **Stokes’s Theorem** | $$\oint_C \mathbf{F}\!\cdot d\mathbf{r}
   =\iint_S (\nabla \times \mathbf{F})\!\cdot \mathbf{n}\,d\sigma$$ | Convert a closed‑curve line integral to a surface integral over any oriented surface \(S\) bounded by \(C\). |
| **Orientation rule** | *Positive (right‑hand) orientation*: walk along \(C\) with \(\mathbf{n}\) pointing outward; the surface must be to your left. | Determines the sign of the surface integral and the resulting line integral. |
| **Green’s Theorem** | $$\oint_C (P\,dx+Q\,dy)=\iint_D\!\left(\partial_x Q-\partial_y P\right)\,dA$$ | Special case of Stokes for planar curves in the \(xy\)-plane; useful for 2‑D line integrals. |

---

## Key Concepts & Intuition

- **Curl** quantifies *local* circulation density; non‑zero curl does **not** imply global circulation.
- **Irrotational** fields satisfy \(\nabla \times \mathbf{F}=\mathbf{0}\) everywhere in a simply‑connected region → conservative, path‑independent integrals.
- **Stokes’s Theorem** equates *global* circulation around a boundary to the *net* rotation over the enclosed surface.
- **Orientation** is critical: flipping the normal \(\mathbf{n}\) or the traversal direction of \(C\) changes the sign.
- **Green’s Theorem** is Stokes in the plane; it replaces a line integral with an area integral of \(\partial_x Q-\partial_y P\).

---

## Problem‑Solving Strategies

| Problem type | Typical cues | Step‑by‑step checklist |
|--------------|--------------|------------------------|
| **Compute curl of \(\mathbf{F}\)** | “Find \(\nabla\times\mathbf{F}\)” | 1. Write \(\mathbf{F}=P\mathbf{i}+Q\mathbf{j}+R\mathbf{k}\). 2. Use determinant or expanded formula. 3. Simplify. |
| **Check if \(\mathbf{F}\) is irrotational** | “Is \(\mathbf{F}\) irrotational?”, “\(\nabla\times\mathbf{F}=\mathbf{0}\)?” | 1. Compute curl. 2. Verify zero everywhere in the region. 3. Ensure the region is simply connected (else further checks needed). |
| **Determine if \(\mathbf{F}\) is conservative** | “Is \(\mathbf{F}\) a gradient?” | 1. Verify irrotationality. 2. Confirm the domain is simply connected. |
| **Apply Stokes to evaluate a line integral** | “Evaluate \(\oint_C\mathbf{F}\!\cdot d\mathbf{r}\)” | 1. Identify \(C\) and choose a convenient bounding surface \(S\). 2. Confirm \(S\) is smooth and oriented to give *positive* boundary. 3. Compute \(\nabla\times\mathbf{F}\). 4. Set up \(\iint_S (\nabla\times\mathbf{F})\!\cdot\mathbf{n}\,d\sigma\). 5. Evaluate the double integral. |
| **Use Stokes for a surface integral** | “Compute \(\iint_S (\nabla\times\mathbf{F})\!\cdot\mathbf{n}\,d\sigma\)” | 1. Recognize it equals \(\oint_{\partial S}\mathbf{F}\!\cdot d\mathbf{r}\). 2. Evaluate the line integral instead (often easier). |
| **Apply Green’s Theorem** | “Planar curve \(C\) in \(xy\)-plane”, “\(P\,dx+Q\,dy\)” | 1. Compute \(\partial_x Q-\partial_y P\). 2. Sketch region \(D\) bounded by \(C\). 3. Set up \(\iint_D (\partial_x Q-\partial_y P)\,dA\). 4. Evaluate. |
| **Check orientation** | “Positive orientation”, “right‑hand rule” | 1. Choose \(\mathbf{n}\). 2. Use right‑hand rule to verify traversal of \(C\). 3. If reversed, flip the sign of the result. |

---

## Common Pitfalls & Checks

| Pitfall | How to avoid/check |
|---------|--------------------|
| Wrong normal vector | Verify \(\mathbf{n}\) points outward and matches the chosen orientation of \(C\). |
| Surface vs. boundary confusion | Remember: Stokes relates the line integral around *\(C\)* to the surface integral over *\(S\)* bounded by *\(C\)*. |
| Ignoring domain connectivity | If \(\nabla\times\mathbf{F}=\mathbf{0}\) but the domain is not simply connected, the field may still be non‑conservative. |
| Incorrect limits | Sketch the region first; use appropriate bounds for \(x,y,z\). |
| Sign errors from orientation | After integration, double‑check the orientation; reverse sign if necessary. |
| Mixing up curl and divergence | Curl gives rotation; divergence gives flux. |
| Over‑simplifying the surface | Any \(S\) bounded by \(C\) works; choose the one that makes the integrand easiest (often a plane). |

---

---

## Raw Slide Summaries

### Slide 1

The image is a slide from a presentation about the concept of curl and Stoke's Theorem, likely for a university course. The slide is titled "Curl and the Stokes's Theorem" in large black text at the top.

*   **Title and Reference**
    *   The title is followed by a yellow box with the text "Trim Ch 14, 14.1, 14.10" in black.
*   **Image**
    *   To the right of the title, there is an image of a sailboat on rough seas.
    *   The image shows Pascal Oddo's Leopard 3 in rough seas during the 2017 Rolex Middle Sea Race.
    *   The URL for the image is provided below the image: https://i.imgur.com/30iDYV3.jpg
*   **Outline**
    *   Below the title, there is an outline of the topics to be covered:
        *   The Concept of Curl
        *   Stoke's Theorem
*   **University Logo**
    *   At the bottom-left corner of the slide, there is a logo for the University of Waterloo.
    *   The logo features a shield with a red and yellow design, accompanied by the university's name in black text.

The slide provides a clear and concise overview of the topics to be covered, along with a relevant image to engage the audience.

### Slide 2

The image presents a slide from a presentation on the concept of curl, featuring two graphs and explanatory text. The title "The Concept of Curl" is prominently displayed at the top-left corner.

*   **Title and Subtitle**
    *   The title "The Concept of Curl" is written in large black font.
    *   Below the title, the subtitle "Suppose we have a velocity field F = y^2 i" is written in smaller black font.
*   **Graphs**
    *   Two graphs are presented side-by-side, each with a blue x-axis and y-axis.
    *   The left graph features arrows pointing to the right, increasing in length as they move up the y-axis.
    *   The right graph displays arrows pointing to the left and right, with those on the left side pointing left and those on the right side pointing right.
*   **Text Below Graphs**
    *   The text "The curl (F) is a measure of how much F is rotating" is written in black font below the graphs.
*   **University Logo**
    *   The University of Waterloo logo is displayed in the bottom-right corner, featuring a shield with a red and yellow design and the university's name in black font.

In summary, the image effectively illustrates the concept of curl through visual representations and concise explanatory text, providing a clear understanding of the topic.

### Slide 3

The image is a slide from a presentation on vector calculus, specifically defining the curl of a vector field. The slide is titled "Definition of Curl" and features the University of Waterloo logo in the bottom-right corner.

**Title and Content**

* The title "Definition of Curl" is prominently displayed in large black text at the top of the slide.
* Below the title, a definition is provided: "For a vector field $\vec{F} = P\hat{i} + Q\hat{j} + R\hat{k}$, the curl is defined as, $\operatorname{CURL}(\vec{F}) = \vec{\nabla} \times \vec{F}$."
* The slide then explains how to compute the curl using a determinant: "To compute the $\operatorname{CURL}(\vec{F})$, we perform the determinant, $\operatorname{CURL}(\vec{F}) = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ P & Q & R \end{vmatrix}$."

**Mathematical Formula**

* The formula for the curl is expanded as: "$\operatorname{CURL}(\vec{F}) = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}\right)\hat{i} + \left(\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}\right)\hat{j} + \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\hat{k}$."

**Visual Elements**

* The slide features a white background with a yellow and black border at the top.
* The University of Waterloo logo is displayed in the bottom-right corner, consisting of a shield with a red and yellow design, accompanied by the university's name in black text.

Overall, the slide provides a clear and concise definition of the curl of a vector field, along with the necessary mathematical formulas to compute it.

### Slide 4

The image presents a slide from a presentation on the topic of "Making Sense of the Curl," which appears to be related to vector calculus. The slide features two diagrams and accompanying text, providing a detailed explanation of the concept.

* **Title and Text**
	+ The title "Making Sense of the Curl" is prominently displayed at the top of the slide in large black font.
	+ Below the title, a paragraph of text explains that the slide will calculate the total counter-clockwise circulation of a vector field along closed paths.
	+ The text is written in black font and includes mathematical notation, specifically the integral symbol and the dot product of two vectors.
* **Diagrams**
	+ Two identical diagrams are presented side by side, each consisting of a green surface with purple arrows indicating the direction of the vector field.
	+ The diagrams are labeled with x, y, and z axes, providing a clear visual representation of the 3D coordinate system.
	+ The surfaces are oriented in different directions, with the left diagram showing the surface facing upwards and the right diagram showing it facing downwards.
* **University Logo**
	+ In the bottom-right corner of the slide, the logo of the University of Waterloo is displayed, featuring a yellow shield with a red cross and a black border.
	+ The university's name is written in black font next to the logo.

In summary, the slide provides a clear and concise explanation of the concept of curl in vector calculus, using visual diagrams and mathematical notation to illustrate the idea. The inclusion of the University of Waterloo logo suggests that the presentation is part of a course or lecture series at the institution.

### Slide 5

The image is a slide from a presentation on vector calculus, specifically focusing on the concept of curl.

*   The title of the slide is "Making Sense of the Curl" in large black text at the top.
*   Below the title, there is a paragraph of text that reads: "Let us suppose that we want to calculate the total counter-clockwise circulation $\oint_{C} \vec{F} \cdot d\vec{r}$ on the following closed paths."
*   A 3D diagram is shown below the text, illustrating a green-outlined surface with purple arrows indicating the direction of the vector field $\vec{F}$ on the surface. The surface is oriented in 3D space, with x, y, and z axes labeled.
    *   The x-axis is pointing to the left and down.
    *   The y-axis is pointing to the right.
    *   The z-axis is pointing upwards.
*   The diagram is accompanied by the University of Waterloo logo in the bottom-right corner, indicating the institution associated with the presentation.

In summary, the image presents a visual representation of a vector field and its circulation around a closed path, which is a fundamental concept in vector calculus. The diagram provides a clear illustration of the vector field's direction and magnitude on the surface, while the text provides context and explanation for the concept being discussed.

### Slide 6

The image presents a slide from a presentation on Stokes's Theorem, featuring a white background with black text and a yellow bar at the top.

*   **Title**: 
    *   "Stokes's Theorem" is written in large black font.
*   **Text**:
    *   The first paragraph defines S as an oriented piece-wise smooth surface bounded by a simple, close, piecewise smooth boundary curve C with positive orientation.
    *   The second paragraph introduces F as a vector field whose components have continuous partial derivatives on an open region containing S.
    *   The third paragraph states that the line integral of F around C equals the double integral of the curl of F over S.
*   **Mathematical Equation**:
    *   The equation is presented as: ∮C F · dr = ∬S (∇ × F) · n dσ
*   **Diagram**:
    *   A green curved surface is depicted, bounded by a green curve.
    *   Purple arrows are scattered across the surface, representing the vector field F.
    *   A blue arrow labeled "x" points to the left, while another blue arrow labeled "y" points to the right.
    *   A blue arrow labeled "z" points upwards.
    *   The diagram illustrates the concept of Stokes's Theorem, showing how the line integral around the boundary curve relates to the surface integral over the enclosed surface.
*   **Logo**:
    *   The University of Waterloo logo is displayed in the bottom-right corner, featuring a shield with a red and yellow design and the university's name in black text.

In summary, the image effectively conveys the concept of Stokes's Theorem through a clear and concise explanation, accompanied by a visual representation that helps to illustrate the theorem's application.

### Slide 7

The image is a slide from a presentation about Stokes's Theorem and Surface Orientation. 

*   The title of the slide is "Stokes's Theorem and Surface Orientation" in large black text at the top.
*   Below the title, there is a sentence that reads, "To use Stoke's Theorem correctly we need to make sure that we are using the correct orientation."
*   There are two diagrams on the slide, both showing a green surface labeled "S" with a purple curve labeled "C" around it.
    *   The diagrams are identical except for the direction of the curve C.
    *   The surface S is a dome-shaped surface with a curved boundary C.
    *   The normal vector n is shown pointing outward from the surface.
*   Below the diagrams, there is a paragraph of text that explains how to induce positive orientation on the curve C.
    *   It states that if we pick n as the normal vector, we need to "walk" along C in a way so that our head is pointing in the direction of n, and the surface S is to our left.
*   In the bottom-right corner of the slide, there is a logo for the University of Waterloo.

Overall, the slide appears to be discussing the importance of orientation when applying Stokes's Theorem, and how to determine the correct orientation for a given surface and curve.

### Slide 8

The image presents a slide from a presentation on Stokes's Theorem and Green's Theorem, featuring a white background with black text and various mathematical equations and diagrams.

**Title**
The title, "Stokes's Theorem and Green's Theorem," is prominently displayed in large, bold black font at the top of the slide.

**Text and Equations**

* Below the title, the text "Stokes's Theorem is given by" is written in smaller black font.
* The equation for Stokes's Theorem is presented: ∮C F · d**r** = ∬S (∇ × F) · **n** dσ
* The text "Let us look at a curve C in the x-y plane" is written below the equation.

**Diagram**

* A 3D coordinate system is illustrated, with the x, y, and z axes labeled.
* A green oval shape is drawn in the x-y plane, representing the curve C.
* Blue arrows are scattered throughout the diagram, indicating the direction of the vector field F.
* The equation F = P**i** + Q**j** is written next to the diagram, with P and Q being functions of x and y.
* The curve C is parameterized by the equation **r**(t) = x(t)**i** + y(t)**j**, where t is a parameter.

**Logo and Institution**

* In the bottom-right corner of the slide, the logo for the University of Waterloo is displayed, accompanied by the institution's name in black text.

Overall, the slide provides a clear and concise introduction to Stokes's Theorem and Green's Theorem, along with a visual representation of the concepts using a 3D coordinate system and a diagram illustrating the curve C in the x-y plane.

### Slide 9

The image presents a slide from a presentation on Stokes's Theorem and Green's Theorem, featuring the title "Stokes's Theorem and Green's Theorem" in large black text at the top. The slide is divided into two sections: the top section contains the title, while the bottom section provides additional information.

**Top Section:**

*   Title: "Stokes's Theorem and Green's Theorem" in large black text
*   Yellow bar below the title, spanning the width of the slide
*   Black bar above the yellow bar, also spanning the width of the slide

**Bottom Section:**

*   Text in blue font: "Green's Circulation-Curl or Tangential form is the 2D version of Stokes's Theorem!"
*   University of Waterloo logo in the bottom-right corner, consisting of a shield with a red and yellow design, accompanied by the university's name in black text.

The background of the slide is white, providing a clean and neutral backdrop for the content. Overall, the slide effectively conveys the main topic of the presentation and provides a clear visual representation of the relationship between Stokes's Theorem and Green's Theorem.

### Slide 10

The image presents a summary slide from a presentation on vector calculus, specifically focusing on the concept of curl and Stokes' Theorem. The title "Summary" is prominently displayed at the top left, followed by four bullet points that outline key aspects of the topic.

*   **The curl of a vector field is a measure of how much the vector field is rotating**
    *   This statement introduces the concept of curl as a measure of rotation in a vector field.
*   **If the curl of a vector field is zero, the vector field is called "irrotational"**
    *   This point defines an irrotational vector field as one with zero curl, indicating no rotation.
*   **The Stokes' Theorem states that the value of a line integral involving vector fields along a closed curve C (also called circulation), is equal to the sum of all the curls over the surface S bounded by that curve.**
    *   Stokes' Theorem relates the line integral around a closed curve to the surface integral of the curl over the enclosed surface.
*   **For the Stoke's Theorem to apply, S should be a smooth surface oriented so that it induces a positive orientation of its boundary C**
    *   This condition specifies that the surface S must be smooth and oriented correctly for Stokes' Theorem to be applicable.

In summary, the slide provides a concise overview of the curl of a vector field and Stokes' Theorem, highlighting their significance in understanding vector calculus. The University of Waterloo logo is displayed in the bottom right corner, indicating the academic context of the presentation.

