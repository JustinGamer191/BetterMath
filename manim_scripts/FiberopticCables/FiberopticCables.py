from manim import *


# --- FIBER OPTIC DIAGRAM SETUP ---
# Creates a cross-section diagram of a fiber optic cable showing light ray path through multiple media
def getDiagram():
    # --- FIBER OPTIC CABLE LAYERS ---
    # Dark gray = cladding (outer protective layer)
    rect1 = Rectangle(
        width=3, height=2, color=DARK_GRAY, fill_opacity=1, fill_color=DARK_GRAY
    )

    # Light gray = outer core layer (medium 3)
    rect2 = Rectangle(
        width=3, height=1, color=LIGHT_GRAY, fill_opacity=1, fill_color=LIGHT_GRAY
    )

    # Red = inner core layer (medium 2, where light travels)
    rect3 = Rectangle(width=3, height=0.65, fill_opacity=1, fill_color=RED, color=RED)

    # Black circle = cross-section end view of cylindrical fiber
    circ = Circle(radius=3, color=BLACK, fill_color=BLACK, fill_opacity=1)
    circ.stretch(0.3, dim=0).shift(
        2 * RIGHT
    )  # Flatten to create ellipse, position at right edge

    # Position all cable layers together
    VGroup(rect1, rect2, rect3).shift(0.5 * RIGHT, 0.15 * UP)

    # --- LIGHT RAY PATH ---
    # Ray 1: Incoming light from air (medium 1) hitting the red core at angle θ₁
    ray1 = Arrow(
        [-2, -1, 0],  # Start point (from upper left, in air)
        [-1, 0, 0],  # End point (interface between air and red core)
        stroke_width=3,
        tip_length=0.2,
        buff=0,
        color=YELLOW,
    )

    # Horizontal reference line for measuring incident angle θ₁
    dotted_line = DashedLine(
        start=[-2, 0, 0],
        end=[-0.75, 0, 0],
        dash_length=0.05,
        dashed_ratio=0.2,
        color=WHITE,
    )

    # Ray 2: Light traveling through red core, approaching red-gray interface at angle θW
    ray2 = Arrow(
        [-1, 0, 0],  # Start from air-red interface
        [0, 0.5, 0],  # Travel to red-gray interface
        stroke_width=3,
        tip_length=0.2,
        buff=0,
        color=YELLOW,
    )

    # Vertical normal line at red-gray interface (perpendicular to surface)
    # Used to measure angle of incidence θW for total internal reflection
    vert_line = DashedLine(
        start=[0, -0.125, 0],
        end=[0, 0.75, 0],
        dash_length=0.05,
        dashed_ratio=0.2,
        color=WHITE,
    )

    # Ray 3: Light reflected back into red core (total internal reflection occurs)
    ray3 = Arrow(
        [0, 0.5, 0],  # Start from red-gray interface
        [1, 0, 0],  # Reflect back into red core
        stroke_width=3,
        tip_length=0.2,
        buff=0,
        color=YELLOW,
    )

    # --- ANGLE LABELS ---
    # θ₁: Incident angle at air-red interface (angle between incoming ray and normal)
    theta1 = Angle.from_three_points(
        [-2, -1, 0],  # Point on incoming ray
        [-1, 0, 0],  # Vertex (intersection point)
        [-2, 0, 0],  # Point on horizontal reference
        other_angle=True,
    )
    label1 = MathTex(r"\theta_1")
    label1.move_to(theta1).scale(0.5).shift(0.2 * LEFT, 0.1 * DOWN)

    # θW: Critical angle at red-gray interface for total internal reflection
    # "W" likely stands for "wall" or "waveguide"
    theta2 = Angle.from_three_points(
        [-1, 0, 0],  # Point on incident ray in red core
        [0, 0.5, 0],  # Vertex (red-gray interface)
        [0, -0.125, 0],  # Point on vertical normal
        other_angle=False,
    )
    label2 = MathTex(r"\theta_W")
    label2.move_to(theta2).scale(0.5).shift(0.2 * LEFT, 0.1 * DOWN)

    # --- REFRACTIVE INDEX LABELS ---
    # n₁ = refractive index of air (~1.0)
    # n₂ = refractive index of red core (higher, allows light to travel)
    # n₃ = refractive index of gray layer (lower than n₂, causes total internal reflection)
    nlabels = MathTex(r"n_1", r"n_2", r"n_3")
    nlabels.scale(0.5)
    nlabels[0].move_to([-2, 1, 0])  # Air label (above fiber)
    nlabels[1].move_to([-1.25, 0.35, 0])  # Red core label
    nlabels[1].color = RED
    nlabels[2].move_to([-1.25, 0.6, 0])  # Gray layer label
    nlabels[2].color = LIGHT_GRAY

    # Return all diagram components grouped for easy manipulation
    return (
        VGroup(rect1, rect2, rect3, circ),
        ray1,
        ray2,
        ray3,
        dotted_line,
        VGroup(theta1, label1),
        vert_line,
        VGroup(theta2, label2),
        nlabels,
    )


# --- SCENE 1: INTRODUCTION ---
# Introduces total internal reflection and sets up the fiber optic diagram
class Preview(Scene):
    def construct(self):
        # --- TITLE ---
        t1 = MathTex(
            r"\text{Total Internal Reflection:}",
            r"\text{An application of Snell's Law}",
        )
        t1.color = PURPLE
        t1.scale(0.5).arrange(DOWN)

        # --- EXPLANATORY TEXT ---
        # Explain the practical application (fiber optic cables)
        t2 = MathTex(
            r"\text{Total internal reflection allows for light}",
            r"\text{to travel through a fiber-optic cable.}",
        )

        # Define the three media involved
        t3 = MathTex(
            r"\text{Let } n_1, n_2, n_3 \text{ be the index of refraction of}",
            r"\text{the air, the red layer, and the gray layer, respectively.}",
        )
        VGroup(t2, t3).scale(0.5)
        VGroup(t2, t3).color = PURPLE
        t2.arrange(DOWN)
        t2.move_to([0, 2, 0])  # Position at top
        t3.arrange(DOWN)
        t3.move_to([0, -2, 0])  # Position at bottom

        # --- BUILD DIAGRAM ---
        background, ray1, ray2, ray3, dLine, theta1, vert_line, theta2, nlabels = (
            getDiagram()
        )

        # Animation sequence
        self.play(Write(t1), run_time=2)
        self.wait(2)
        self.play(FadeOut(t1))

        # Build fiber optic cable structure
        self.play(Write(background))

        # Show light ray path step by step
        self.play(Create(ray1))  # Incoming light from air
        self.play(
            Create(ray2), Create(dLine), Create(theta1)
        )  # Light enters red core, show incident angle
        self.play(
            Create(ray3), Create(vert_line), Create(theta2)
        )  # Light reflects at red-gray interface

        # Label the media
        self.play(Write(nlabels))

        # Add explanatory text
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(2)


# --- SCENE 2: MATHEMATICAL DERIVATION ---
# Derives the condition for total internal reflection using Snell's Law
class Proof(Scene):
    def construct(self):
        # --- RESTORE DIAGRAM FROM PREVIOUS SCENE ---
        diagram = VGroup(getDiagram())

        # Restore explanatory text
        t2 = MathTex(
            r"\text{Total internal reflection allows for light}",
            r"\text{to travel through a fiber-optic cable.}",
        )
        t3 = MathTex(
            r"\text{Let } n_1, n_2, n_3 \text{ be the index of refraction of}",
            r"\text{the air, the red layer, and the gray layer, respectively.}",
        )
        VGroup(t2, t3).scale(0.5)
        VGroup(t2, t3).color = PURPLE
        t2.arrange(DOWN)
        t2.move_to([0, 2, 0])
        t3.arrange(DOWN)
        t3.move_to([0, -2, 0])

        # --- STEP 1: APPLY SNELL'S LAW AT AIR-RED INTERFACE ---
        # Snell's Law: n₁sin(θ₁) = n₂sin(θ₂)
        # Here θ₂ = 90° - θW (complementary angle)
        # Using trig identity: sin(90° - θW) = cos(θW) = √(1 - sin²(θW))
        m1 = MathTex(
            r"\text{Using Snell's Law:}",
            r"n_1 sin(\theta_1) = n_2 sin(90 - \theta_W)",
            r"n_1 sin(\theta_1) = n_2 \sqrt{1 - sin^2(\theta_W)}",
        )
        m1.scale(0.5).arrange(DOWN).move_to([0, 2.25, 0])
        m1.color = PURPLE

        # --- STEP 2: CONDITION FOR TOTAL INTERNAL REFLECTION ---
        # At red-gray interface, for total internal reflection to occur:
        # sin(θW) must exceed the critical angle
        # Critical angle condition: sin(θW) > n₃/n₂
        m2 = MathTex(
            r"\text{Using Snell's Law:}",
            r"\text{In order for reflection, }",
            r"sin(\theta_W) > \frac{n_3}{n_2}",
        )
        m2.scale(0.5).arrange(DOWN).move_to([0, 2.25, 0])
        m2.color = PURPLE

        # --- STEP 3: SOLVE FOR θ₁ ---
        # Substitute the critical angle condition into Snell's Law equation
        # Solve for sin(θ₁) to find the maximum incident angle
        m3 = MathTex(r"sin(\theta_1) < \frac{n_2}{n_1}\sqrt{1-\frac{{n_3}^2}{{n_2}^2}")
        m3.scale(0.5).move_to([0, 2, 0])
        m3.color = PURPLE

        # --- STEP 4: SIMPLIFY FOR AIR (n₁ ≈ 1) ---
        # Since air has refractive index ≈ 1, the equation simplifies
        # Final condition: sin(θ₁) < √(n₂² - n₃²)
        # This is the "numerical aperture" condition for fiber optics
        m4 = MathTex(
            r"\text{Since } n_1, \text{the index of refraction}",
            r"\text{of air, usually equals 1}",
            r"sin(\theta_1) < \sqrt{{n_2}^2 - {n_3}^2}",
            r"\text{Light will only travel throughout the wire}",
            r"\text{when } \theta_1 \text{ satisfies this inequality.}",
        )
        m4.scale(0.5).arrange(DOWN).move_to([0, 2, 0])
        m4.color = PURPLE

        # --- ANIMATION SEQUENCE ---
        self.add(diagram, t2, t3)

        # Step 1: Apply Snell's Law
        self.play(FadeOut(t2))
        self.play(Write(m1), run_time=3)
        self.wait(2)

        # Keep only the simplified Snell's Law equation
        self.play(FadeOut(m1[0:2]), m1[2].animate.move_to([0, 3.5, 0]))

        # Step 2: Introduce critical angle condition
        self.play(Write(m2), run_time=3)
        self.wait(2)

        # Keep only the critical angle inequality
        self.play(FadeOut(m2[0:2]), m2[2].animate.move_to([0, 2.75, 0]))

        # Step 3: Show the combined inequality
        self.play(Write(m3))
        self.wait(2)

        # Step 4: Simplify and conclude
        self.play(FadeOut(m2[2], m1[2]))
        self.play(diagram.animate.shift(0.5 * DOWN), m3.animate.shift(1.5 * UP))
        self.play(Write(m4), run_time=5)
        self.wait(5)
