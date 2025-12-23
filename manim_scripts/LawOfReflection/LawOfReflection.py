from manim import *
from tqdm import tqdm
import pandas as pd


# --- HELPER FUNCTION: CREATE REFLECTION DIAGRAM ---
# Draws incident ray, reflected ray, surface, and angle labels
def getDiagram():
    # INCIDENT RAY: Light approaching the surface
    # Comes from upper left at 45° angle
    ray1 = Arrow(
        [-2 * np.sqrt(2), np.sqrt(2), 0],  # Start point
        [0, 0, 0],  # End point (point of reflection)
        stroke_width=3,
        tip_length=0.2,
        buff=0,
    )
    ray1.color = YELLOW

    # REFLECTIVE SURFACE: Horizontal mirror/surface
    surface1 = Line([-2 * np.sqrt(2), 0, 0], [2 * np.sqrt(2), 0, 0])

    # REFLECTED RAY: Light bouncing off the surface
    # Goes to upper right at 45° angle (symmetric to incident ray)
    ray2 = Arrow(
        [0, 0, 0],  # Start point (point of reflection)
        [2 * np.sqrt(2), np.sqrt(2), 0],  # End point
        stroke_width=3,
        tip_length=0.2,
        buff=0,
    )
    ray2.color = YELLOW

    # NORMAL LINE: Perpendicular to surface at point of reflection
    # Used as reference for measuring angles
    dotted_line = DashedLine(
        start=[0, 1.5, 0],
        end=[0, -1.5, 0],
        dash_length=0.05,
        dashed_ratio=0.2,
        color=WHITE,
    )

    # ANGLE OF INCIDENCE (i): Angle between incident ray and normal
    # Measured from normal to incident ray
    anglei = Angle.from_three_points(
        [-2 * np.sqrt(2), np.sqrt(2), 0],  # Point on incident ray
        [0, 0, 0],  # Vertex (reflection point)
        [0, 1.5, 0],  # Point on normal
        other_angle=True,
        color=RED,
    )

    # ANGLE OF REFLECTION (r): Angle between normal and reflected ray
    # Law of reflection states: i = r
    angler = Angle.from_three_points(
        [0, 1.5, 0],  # Point on normal
        [0, 0, 0],  # Vertex (reflection point)
        [2 * np.sqrt(2), np.sqrt(2), 0],  # Point on reflected ray
        other_angle=True,
        color=BLUE,
    )

    # Angle labels
    labeli = MathTex(r"i")
    labeli.color = RED
    labeli.move_to(anglei).shift(0.25 * UP + 0.25 * LEFT)

    labelr = MathTex(r"r")
    labelr.color = BLUE
    labelr.move_to(angler).shift(0.25 * UP + 0.25 * RIGHT)

    VGroup(labeli, labelr).scale(0.5)

    return ray1, surface1, ray2, dotted_line, anglei, angler, labeli, labelr


# --- HELPER FUNCTION: CREATE GEOMETRIC LABELS ---
# Labels for Fermat's Principle derivation
def getLabels():
    # HEIGHT LINES
    # h₁: Vertical distance from incident ray origin to surface
    lineh1 = Line(
        [-1 * np.sqrt(2), 0, 0], [-1 * np.sqrt(2), np.sqrt(2) / 2, 0], color=RED
    )

    # h₂: Vertical distance from surface to reflected ray endpoint
    lineh2 = Line(
        [np.sqrt(2) / 2, 0, 0], [np.sqrt(2) / 2, np.sqrt(2) / 4, 0], color=BLUE
    )

    # HORIZONTAL DISTANCES
    # l: Total horizontal distance traveled
    lineL = DoubleArrow(
        [-1 * np.sqrt(2), -0.25, 0],
        [np.sqrt(2) / 2, -0.25, 0],
        tip_length=0.1,
        buff=0,
        color=PURPLE,
    )

    # x: Horizontal distance to reflection point from start
    linex = DoubleArrow(
        [-1 * np.sqrt(2), -0.25, 0], [0, -0.25, 0], tip_length=0.1, buff=0, color=RED
    )

    # l-x: Remaining horizontal distance after reflection
    linelx = DoubleArrow(
        [0, -0.25, 0], [np.sqrt(2) / 2, -0.25, 0], tip_length=0.1, buff=0, color=BLUE
    )

    # Labels for each measurement
    labelh1 = MathTex(r"h_1")
    labelh1.move_to(lineh1).shift(0.25 * LEFT)
    labelh1.scale(0.5)
    labelh1.color = RED

    labelh2 = MathTex(r"h_2")
    labelh2.move_to(lineh2).shift(0.25 * RIGHT)
    labelh2.scale(0.5)
    labelh2.color = BLUE

    labelL = MathTex(r"l")
    labelL.move_to(lineL).shift(0.25 * DOWN)
    labelL.color = PURPLE

    labelx = MathTex(r"x")
    labelx.move_to(linex).shift(0.25 * DOWN)
    labelx.color = RED
    labelx.scale(0.5)

    labellx = MathTex(r"l-x")
    labellx.move_to(linelx).shift(0.25 * DOWN)
    labellx.color = BLUE
    labellx.scale(0.5)

    VGroup(lineL, labelL).shift(0.5 * DOWN)

    return (
        lineh1,
        lineh2,
        labelh1,
        labelh2,
        lineL,
        labelL,
        VGroup(linex, labelx),
        VGroup(linelx, labellx),
    )


# --- SCENE 1: INTRODUCTION TO LAW OF REFLECTION ---
# States the basic law: angle of incidence = angle of reflection
class LawOfReflection(Scene):
    def construct(self):
        ray1, surface1, ray2, dotted_line, anglei, angler, labeli, labelr = getDiagram()

        # Title
        t1 = MathTex(r"\text{Law of Reflection}", r"\text{Part 1}")
        t1.scale(0.5)
        t1.arrange(DOWN)
        t1.color = YELLOW

        # LAW STATEMENT
        # When light reflects off a surface:
        # ∠i (angle of incidence) = ∠r (angle of reflection)
        # Both measured from the normal (perpendicular to surface)
        t2 = MathTex(
            r"\text{The law states that }",
            r"\angle i= \angle r",  # The fundamental relationship
            r"\text{when light reflects off a surface.}",
        )
        t2.scale(0.5)
        t2.arrange(DOWN)
        t2.move_to([0, -1, 0])
        t2[1][1].color = RED  # Color angle i
        t2[1][4].color = BLUE  # Color angle r
        bg2 = BackgroundRectangle(t2, fill_opacity=1)  # Background for readability

        # --- ANIMATION SEQUENCE ---
        self.play(Write(t1))
        self.wait(1)

        self.play(t1.animate.move_to([0, 2, 0]))

        # Build the reflection diagram step by step
        self.play(
            Create(ray1), Create(surface1), Create(dotted_line)
        )  # Incident ray and surface
        self.play(Create(ray2))  # Reflected ray

        # Show the angles
        self.play(Create(anglei), Create(angler))
        self.play(Write(labeli), Write(labelr))

        # Display the law
        self.add(bg2)
        self.play(Write(t2))

        self.wait(2)
        self.remove(bg2)
        self.play(FadeOut(t2, t1))
        self.wait(1)


# --- SCENE 2: FERMAT'S PRINCIPLE ---
# Introduces the principle of least time and sets up the proof
class FermatPrinciple(Scene):
    def construct(self):
        diagram = VGroup(getDiagram())
        self.add(diagram)

        lineh1, lineh2, labelh1, labelh2, lineL, labelL, linelabelx, linelabellx = (
            getLabels()
        )
        VGroup(lineL, labelL).shift(0.5 * UP)

        # FERMAT'S PRINCIPLE (1662)
        # Light always takes the path that requires the least time
        # This is a fundamental principle in optics
        # From it, we can derive Snell's Law and the Law of Reflection
        t1 = MathTex(
            r"\text{Fermat's Principle:}",
            r"\text{Light always travels through}",
            r"\text{the path of least time.}",
        )
        t1.scale(0.5)
        t1.arrange(DOWN)
        t1.move_to([0, 2.75, 0])

        self.play(Write(t1))
        self.wait(1)

        # Add geometric labels needed for the proof
        # These define the path length as a function of x (reflection point location)
        self.play(Create(lineh1), Create(labelh1))  # Height h₁
        self.play(Create(lineh2), Create(labelh2))  # Height h₂
        self.play(Create(lineL), Create(labelL))  # Total distance l
        self.play(VGroup(lineL, labelL).animate.shift(0.5 * DOWN))
        self.play(Create(linelabelx))  # Distance x to reflection point
        self.play(Create(linelabellx))  # Remaining distance l-x
        self.play(FadeOut(t1))
        self.wait(1)


# --- SCENE 3: MATHEMATICAL PROOF ---
# Derives the Law of Reflection from Fermat's Principle using calculus
class Proof(Scene):
    def construct(self):
        diagram = VGroup(getDiagram(), getLabels())
        self.add(diagram)

        # STEP 1: TOTAL TIME AS FUNCTION OF x
        # Time = Distance/Speed
        # Distance₁ = √(x² + h₁²) (incident ray, by Pythagorean theorem)
        # Distance₂ = √((l-x)² + h₂²) (reflected ray)
        # Total time: t(x) = [√(x² + h₁²) + √((l-x)² + h₂²)] / c
        m1 = MathTex(
            r"\frac{\sqrt{x^2 + {h_1}^2} + \sqrt{(l-x)^2 + {h_2}^2}}{c} = t",
            r"\text{where c is the speed of light,}",
            r"\text{t is the time light takes to travel a distance D.}",
        )
        m1.scale(0.5)
        m1.arrange(DOWN)

        # STEP 2: MINIMIZE TIME USING CALCULUS
        # To find minimum time, take derivative dt/dx and set = 0
        # dt/dx = (1/c)[x/√(x²+h₁²) + (x-l)/√((x-l)²+h₂²)]
        m2 = MathTex(
            r"\frac{dt}{dx} = \frac{1}{c} (\frac{x}{\sqrt{x^2 + {h_1}^2}} + \frac{x-l}{\sqrt{(x-l)^2 + {h_2}^2}}})"
        )
        m2.scale(0.5)
        VGroup(m1[0], m2).arrange(DOWN)

        # STEP 3: RECOGNIZE TRIGONOMETRIC RELATIONSHIPS
        # From the geometry of the diagram:
        # sin(i) = opposite/hypotenuse = x/√(x²+h₁²)
        # sin(r) = (l-x)/√((l-x)²+h₂²)
        h1 = MathTex(
            r"sin(i) = \frac{x}{\sqrt{x^2 + {h_1}^2}},",
            r"sin(r) = \frac{l-x}{\sqrt{(x-l)^2 + {h_1}^2}}",
        )
        h1.scale(0.5)

        # STEP 4: SUBSTITUTE TRIG RELATIONSHIPS
        # dt/dx = (1/c)[sin(i) - sin(r)]
        m3 = MathTex(
            r"\frac{dt}{d \theta} \frac{d \theta}{dx} = \frac{1}{c} (sin(i) - sin(r))"
        )
        m3.scale(0.5)
        m3.arrange(DOWN)

        # STEP 5: APPLY MINIMUM CONDITION
        # At the minimum (fastest path), derivative = 0
        m4 = MathTex(
            r"\frac{dt}{d \theta} \text{ is equal to 0 at minimum time travelled}"
        )
        m4.scale(0.5)

        # STEP 6: SOLVE FOR ANGLES
        # 0 = sin(i) - sin(r)
        # sin(i) = sin(r)
        # Therefore: i = r (Law of Reflection!)
        m5 = MathTex(r"0 = sin(i) - sin(r)", r"sin(i) = sin(r)", r"i = r")
        m5[0][6].color = RED  # Color angle i
        m5[1][4].color = RED
        m5[2][0].color = RED
        m5[0][13].color = BLUE  # Color angle r
        m5[1][11].color = BLUE
        m5[2][2].color = BLUE
        m5.scale(0.5)
        m5.arrange(DOWN)

        # --- ANIMATION: STEP-BY-STEP DERIVATION ---
        self.play(diagram.animate.move_to([0, 2.5, 0]).scale(0.75))

        # Show total time equation
        self.play(Write(m1))
        self.wait(2)

        # Take derivative
        self.play(FadeOut(m1[1:]))
        self.play(Write(m2))
        self.wait(2)

        # Clean up
        self.play(FadeOut(m1[0]))
        self.play(m2.animate.move_to(m1[0]))
        self.wait(2)

        # Show trig substitutions
        VGroup(m2, h1).arrange(DOWN)
        self.play(Write(h1))
        self.wait(2)

        # Substitute into derivative
        self.play(FadeOut(h1))
        m3.move_to(h1)
        self.play(Write(m3))
        self.wait(2)

        # Apply minimum condition
        self.play(FadeOut(m2))
        self.play(m3.animate.move_to(m2))
        VGroup(m3, m4).arrange(DOWN)
        self.play(Write(m4))
        self.wait(2)

        # Solve for the result
        m5.move_to([0, -0.75, 0])
        self.play(FadeOut(m4))
        self.play(Write(m5))
        self.wait(2)

        # Show final result: i = r
        self.play(FadeOut(m3, m5[0], m5[1]))
        self.play(
            diagram.animate.move_to([0, 0, 0]).scale(1 / 0.75),
            m5[2].animate.move_to([0, 2, 0]),
        )
        self.wait(1)

        # Conclude with title
        t1 = MathTex(r"\text{Law of Reflection}")
        t1.scale(0.5)
        t1.color = YELLOW
        t1.move_to([0, 2.5, 0])

        self.play(Write(t1))
        self.wait(5)
