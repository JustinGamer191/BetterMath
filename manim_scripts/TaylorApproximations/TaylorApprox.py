from manim import *


# --- SCENE 1: INTRODUCTION TO TAYLOR SERIES APPLICATIONS ---
# Introduces how Taylor series are used for real-world approximations
class Intro(Scene):
    def construct(self):
        # --- TITLE ---
        title = Text("Taylor Series Approximations")
        title.scale(0.5)
        title.color = BLUE

        # --- WHAT IS A TAYLOR SERIES APPROXIMATION? ---
        # A Taylor series expands a function as an infinite sum of polynomial terms
        # f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)²/2! + f'''(a)(x-a)³/3! + ...
        # For approximations, we truncate after a few terms
        text = MathTex(
            r"\text{A Taylor series of a function}",
            r"\text{can be used to approximate its value}",
            r"\text{near a given point.}",  # Key: approximation is LOCAL (near point a)
        )
        text.scale(0.5)
        text.arrange(DOWN)
        text.color = RED

        # --- FAMOUS APPLICATION: PENDULUM PERIOD ---
        # The simple pendulum formula: T = 2π√(L/g)
        # This elegant formula is actually an APPROXIMATION
        # Valid only for small angles (θ ≪ 1 radian)
        pendulum_formula = MathTex(
            r"T = 2\pi \sqrt{\frac{L}{g}}"  # Period of simple pendulum
        )
        pendulum_formula.scale(0.5)
        pendulum_formula.color = GREEN
        pendulum_formula.move_to([0, 0, 0])

        # --- KEY INSIGHT ---
        # The simple pendulum formula relies on the approximation sin(θ) ≈ θ
        # This comes from truncating the Taylor series of sin(θ) after the first term
        textp = MathTex(
            r"\text{A Taylor series approximation was used}",
            r"\text{to derive the formula for the period of a simple pendulum}",
            r"\text{for small angles } \theta \text{ (in radians)}",  # Crucial: RADIANS!
        )
        textp.scale(0.5)
        textp.arrange(DOWN)
        textp.color = ORANGE
        textp.move_to([0, -1.5, 0])

        # --- ANIMATION SEQUENCE ---
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        self.play(Write(text))
        self.play(text.animate.move_to([0, 1.5, 0]))
        self.wait(2)
        self.play(Write(pendulum_formula))
        self.wait(2)
        self.play(Write(textp))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(pendulum_formula), FadeOut(textp))
        self.wait(2)


# --- SCENE 2: DERIVING THE PENDULUM FORMULA ---
# Shows how Taylor series approximation leads to the simple pendulum equation
class TaylorApprox(Scene):
    def construct(self):
        # --- PENDULUM SETUP PARAMETERS ---
        origin = [0, 1.5, 0]  # Pivot point
        length = 3  # Pendulum length L
        max_angle = PI / 6  # Initial displacement (30 degrees)

        # --- PIVOT AND SUPPORT ---
        pivot = Dot(origin, radius=0.09, color=GRAY)
        support = Line(
            [origin[0] - 0.5, origin[1], 0],
            [origin[0] + 0.5, origin[1], 0],
            color=GRAY,
            stroke_width=4,
        )

        # --- EQUILIBRIUM REFERENCE LINE ---
        # Vertical line showing equilibrium position (θ = 0)
        equilibrium_point = [origin[0], origin[1] - length, 0]
        dotted_line = DashedLine(
            start=[equilibrium_point[0], equilibrium_point[1], 0],
            end=[equilibrium_point[0], equilibrium_point[1] + 3, 0],
            color=GRAY,
            dash_length=0.15,
            stroke_width=2,
        )

        # --- ANGLE MARKER (θ) ---
        # Shows the angular displacement from vertical
        arc = Arc(
            start_angle=-PI / 2,  # Start from downward vertical
            angle=max_angle,  # Sweep through displacement angle
            radius=0.7,
            arc_center=origin,
            color=YELLOW,
        )
        theta_label = MathTex(r"\theta", color=YELLOW).scale(0.7)
        theta_label.move_to(
            [
                0.7 * np.cos(-PI / 2 + max_angle / 2),
                origin[1] + 0.7 * np.sin(-PI / 2 + max_angle / 2),
                0,
            ]
        )

        # --- PENDULUM BOB AND STRING ---
        # Helper function to create pendulum at any angle
        def get_bob_and_string(angle):
            # Calculate bob position using polar coordinates
            bob_pos = [
                origin[0] + length * np.sin(angle),  # x = L sin(θ)
                origin[1] - length * np.cos(angle),  # y = -L cos(θ)
                0,
            ]
            string = Line(origin, bob_pos, color=WHITE, stroke_width=3)
            bob = Circle(radius=0.22, color=BLUE, fill_opacity=1).move_to(bob_pos)
            return VGroup(string, bob)

        pendulum = get_bob_and_string(max_angle)

        # Label the length L
        length_label = MathTex(r"L", color=WHITE).scale(0.7)
        string_midpoint = [
            (origin[0] + pendulum[0].get_end()[0]) / 2,
            (origin[1] + pendulum[0].get_end()[1]) / 2,
            0,
        ]
        length_label.move_to(string_midpoint + np.array([0.3, 0, 0]))

        # --- ARC LENGTH (s) ---
        # s = Lθ (for angle in radians)
        # This is the actual distance traveled along the arc
        arc_s = Arc(
            start_angle=-PI / 2,
            angle=max_angle,
            radius=length,  # Arc at radius L
            arc_center=origin,
            color=GREEN,
            stroke_width=4,
        )
        s_label = MathTex(r"s", color=GREEN).scale(0.7)
        s_label.move_to(arc_s.get_center() + DOWN * 0.3)

        # Group all visual elements and shift up
        all_elements = VGroup(
            pendulum,
            length_label,
            theta_label,
            support,
            pivot,
            arc,
            dotted_line,
            arc_s,
            s_label,
        )
        all_elements.shift(2 * UP)
        theta_label.shift(DOWN * 0.25)

        # --- BUILD THE PENDULUM DIAGRAM ---
        self.play(Create(support), Create(pivot), Create(dotted_line))
        self.play(Create(arc_s), Write(s_label))  # Arc length
        self.play(Create(pendulum), Write(length_label))  # String and bob
        self.play(Create(arc), Write(theta_label))  # Angle
        self.wait(1)

        # --- FORCE ANALYSIS ---
        # The restoring force on the pendulum is the tangential component of gravity
        # F = -mg sin(θ) (negative because it opposes displacement)
        text3 = MathTex(r"F = mg\sin(\theta)", color=RED).scale(0.7)

        # --- TAYLOR SERIES APPROXIMATION ---
        # sin(θ) = θ - θ³/3! + θ⁵/5! - θ⁷/7! + ...
        # For small θ (θ ≪ 1 radian): sin(θ) ≈ θ
        # This is the first-order Taylor approximation around θ = 0
        text4 = MathTex(
            r"\text{Small angle approximation using Taylor Series:}", color=RED
        ).scale(0.7)
        text5 = MathTex(r"\sin(\theta) \approx \theta", color=RED).scale(
            0.7
        )  # KEY APPROXIMATION!

        # Apply approximation to force equation
        text6 = MathTex(r"\Rightarrow F \approx mg\theta", color=RED).scale(0.7)

        # --- RELATE ANGLE TO ARC LENGTH ---
        # For circular motion: s = rθ (arc length = radius × angle)
        # Here: s = Lθ (L is the radius)
        text7 = MathTex(r"\theta = \frac{s}{L}", color=RED).scale(0.7)

        # Substitute into force equation
        text8 = MathTex(r"\Rightarrow F \approx mg \frac{s}{L}", color=RED).scale(0.7)

        # --- KEY INSIGHT: HOOKE'S LAW ---
        # F = -(mg/L)s
        # This is in the form F = -kx (Hooke's Law!)
        # Where k = mg/L is the "effective spring constant"
        text9 = MathTex(
            r"\text{Force is proportional to displacement } s", color=RED
        ).scale(0.7)

        # CONCLUSION: This is Simple Harmonic Motion (SHM)
        # Any system with F ∝ -x exhibits SHM
        text10 = MathTex(r"\Rightarrow \text{Simple Harmonic Motion}", color=RED).scale(
            0.7
        )

        # Position text elements
        text4.next_to(text3, DOWN, buff=0.1)
        text5.next_to(text4, DOWN, buff=0.1)
        text6.next_to(text5, DOWN, buff=0.1)
        text7.next_to(text3, DOWN, buff=0.1)
        text8.next_to(text7, DOWN, buff=0.1)
        text9.next_to(text8, DOWN, buff=0.1)
        text10.next_to(text9, DOWN, buff=0.1)
        text9.next_to(text8, DOWN, buff=0.1)

        # --- DERIVATION ANIMATION ---
        self.play(Write(text3))  # F = mg sin(θ)
        self.wait(1)
        self.play(Write(text4))  # Introduce Taylor approximation
        self.wait(1)
        self.play(Write(text5))  # sin(θ) ≈ θ
        self.wait(1)
        self.play(Write(text6))  # F ≈ mgθ
        self.wait(1)

        # Clean up
        self.play(FadeOut(text3), FadeOut(text4), FadeOut(text5))
        self.play(text6.animate.move_to(text3))

        # Relate angle to arc length
        self.play(Write(text7))  # θ = s/L
        self.wait(1)
        self.play(Write(text8))  # F ≈ mg(s/L)
        self.wait(1)
        self.play(Write(text9))  # F ∝ s
        self.wait(1)
        self.play(Write(text10))  # This is SHM!
        self.wait(1)

        # Clean up for final derivation
        self.play(FadeOut(text6), FadeOut(text7), FadeOut(text9), FadeOut(all_elements))
        self.play(
            text8.animate.move_to([0, 2, 0]),
            text10.animate.move_to([0, 2, 0]).shift(DOWN),
        )

        # --- DERIVE THE PERIOD FORMULA ---
        # For SHM: F = -kx
        # Effective spring constant: k = mg/L
        text11 = MathTex(r"F = kx", color=RED).scale(0.7)
        text11.move_to([0, 2, 0]).shift(1.5 * DOWN)

        text12 = MathTex(
            r"\Rightarrow \text{SHM with } k = \frac{mg}{L}", color=RED
        ).scale(0.7)
        text12.next_to(text11, DOWN, buff=0.1)

        # STANDARD SHM PERIOD FORMULA: T = 2π√(m/k)
        # This comes from solving the differential equation: m(d²x/dt²) = -kx
        text13 = MathTex(r"T = 2\pi \sqrt{\frac{m}{k}}", color=RED).scale(0.7)
        text13.next_to(text12, DOWN, buff=0.1)

        # SUBSTITUTE k = mg/L:
        # T = 2π√(m/(mg/L)) = 2π√(mL/mg) = 2π√(L/g)
        # Notice: mass m cancels! Period is independent of mass!
        text14 = MathTex(r"\Rightarrow T = 2\pi \sqrt{\frac{L}{g}}", color=RED).scale(
            0.7
        )
        text14.next_to(text13, DOWN, buff=0.1)

        self.play(Write(text11))  # F = kx (Hooke's Law)
        self.wait(1)
        self.play(Write(text12))  # k = mg/L
        self.wait(1)
        self.play(Write(text13))  # T = 2π√(m/k)
        self.wait(1)
        self.play(Write(text14))  # T = 2π√(L/g) - THE FORMULA!
        self.wait(2)

        # --- KEY TAKEAWAYS ---
        # 1. The "simple" pendulum formula requires sin(θ) ≈ θ
        # 2. This Taylor approximation is valid for θ < 0.2 rad (≈ 11°)
        # 3. For larger angles, the period depends on amplitude (nonlinear)
        # 4. The approximation converts nonlinear motion into linear SHM
        # 5. Period is independent of mass (unique to gravity-driven oscillators)
