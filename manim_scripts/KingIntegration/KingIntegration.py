from manim import *


# --- INTRODUCTION TO KING'S PROPERTY OF INTEGRATION ---
# Also known as the "Property of Symmetry" or "Substitution Rule for Definite Integrals"
# This powerful technique simplifies many complex integrals
class Intro(Scene):
    def construct(self):
        # --- TITLE AND THEOREM STATEMENT ---
        t1 = MathTex(
            r"\text{King's Property of Integration}",
            r"\int_{a}^{b}f(x)dx = \int_{a}^{b}f(a+b-x)dx",  # The key identity
            r"\text{(and correcting mistakes made in prior video.)}",
        )
        t1.scale(0.5).arrange(DOWN)
        t1[0].color = GOLD
        t1[1].color = PURPLE  # The main theorem
        t1[2].color = GOLD

        # --- PROOF OF KING'S PROPERTY ---
        # Uses u-substitution to show the equivalence
        t2 = MathTex(
            r"\text{First, the proof:}",
            # STEP 1: U-SUBSTITUTION
            # Let u = a + b - x (reflects x around the midpoint (a+b)/2)
            # This transforms the function argument while preserving the integral's value
            r"\text{Let } u = a + b - x, du = -dx",
            # STEP 2: CHANGE OF LIMITS
            # When x = a: u = a + b - a = b (upper limit becomes lower limit)
            # When x = b: u = a + b - b = a (lower limit becomes upper limit)
            # The limits SWAP!
            r"\text{When } x = a \rightarrow u = b, \text{when } x = b \rightarrow u = a",
            # STEP 3: SUBSTITUTE AND SIMPLIFY
            # Original: ∫[a to b] f(a+b-x)dx
            # After substitution: ∫[b to a] f(u)(-du)
            r"\int_{a}^{b} f(a+b-x)dx = \int_{b}^{a} f(u) (-du)",
            # STEP 4: REVERSE LIMITS AND REMOVE NEGATIVE
            # ∫[b to a] f(u)(-du) = -∫[b to a] f(u)du = ∫[a to b] f(u)du
            # Swapping limits introduces a negative sign, which cancels with -du
            # Since u is a dummy variable, we can replace it with x
            r"= \int_{a}^{b} f(u) du = \int_{a}^{b} f(x) dx",
        )
        t2.scale(0.5).arrange(DOWN)
        t2[0].color = GOLD
        t2[1:5].color = PURPLE

        # --- APPLICATION SECTION TITLE ---
        t3 = MathTex(r"\text{Next, the applications:}")
        t3.scale(0.5).move_to([0, 1.5, 0])
        t3.color = GOLD

        # --- VISUAL EXAMPLE: COMPARING TWO INTEGRALS ---
        # Here a=1, b=4, so a+b-x = 5-x

        axes = Axes(
            x_range=[1, 4, 1],  # From x=1 to x=4
            y_range=[0, 64, 16],
            x_length=2,
            y_length=3,
            tips=False,
        )

        # GRAPH 1: f(x) = x³
        # Regular cubic function
        graph1 = axes.plot(lambda x: x**3, x_range=[1, 4], color=RED)
        label1 = MathTex(r"\int_{1}^{4} x^3 dx", color=RED)
        label1.move_to([2, -1, 0]).scale(0.5)

        # GRAPH 2: f(a+b-x) = (5-x)³
        # Reflected version of x³ around x = 2.5 (midpoint of [1,4])
        # When x=1: (5-1)³ = 4³ = 64
        # When x=4: (5-4)³ = 1³ = 1
        # This is the "mirror image" of x³ over the interval
        graph2 = axes.plot(lambda x: (5 - x) ** 3, x_range=[1, 4], color=BLUE)
        label2 = MathTex(r"\int_{1}^{4} (5-x)^3 dx", color=BLUE)
        label2.move_to([-2, -1, 0]).scale(0.5)

        VGroup(axes, graph1, graph2).shift(0.5 * DOWN)

        # Shaded areas under both curves
        # King's Property guarantees these areas are EQUAL
        area1 = axes.get_area(graph1, x_range=[1, 4], color=RED, opacity=0.3)
        area2 = axes.get_area(graph2, x_range=[1, 4], color=BLUE, opacity=0.3)

        # --- NUMERICAL RESULT ---
        # Both integrals evaluate to:
        # ∫[1 to 4] x³ dx = [x⁴/4] from 1 to 4 = 256/4 - 1/4 = 255/4 = 63.75
        # ∫[1 to 4] (5-x)³ dx = same by King's Property!
        t4 = MathTex(r"\text{They are both equal to }", r"\frac{255}{4}.")
        t4.scale(0.5).arrange(DOWN)
        t4.color = PURPLE

        # --- ANIMATION SEQUENCE ---
        # Introduce theorem with correction note
        self.play(Write(t1), run_time=3)
        self.wait(2)

        # Keep only the main formula visible
        self.play(FadeOut(t1[0], t1[2]), t1[1].animate.move_to([0, 2, 0]))

        # Show the formal proof
        self.play(Write(t2), run_time=5)
        self.wait(5)

        # Clear proof, introduce application
        self.play(FadeOut(t2))
        self.play(Write(t3))

        # Show both functions and their areas simultaneously
        # The visual symmetry demonstrates the algebraic property
        self.play(
            Create(axes),
            Create(VGroup(graph1, area1, label1)),
            Create(VGroup(graph2, area2, label2)),
        )
        self.wait(3)

        # Clean up graphs, keep labels for comparison
        self.play(
            FadeOut(VGroup(axes, graph1, graph2, area1, area2, t3, t1[1])),
            VGroup(label1, label2).animate.arrange(DOWN).move_to([0, 2, 0]),
        )

        # Reveal that both integrals have the same value
        self.play(Write(t4))
        self.wait(2)
