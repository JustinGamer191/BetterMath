from manim import *


# --- SCENE 1: INTRODUCTION TO BLACK HOLES ---
# Opening scene introducing black holes with key equations and Hawking quote
# Brilliant.org Partnership Video #1
class Intro(Scene):
    def construct(self):
        # --- TITLE ---
        t1 = MathTex(r"\text{Black Holes}", r"\text{What are they?}", color=GOLD)
        t1.scale(0.5).arrange(DOWN)
        t1.move_to([0, 1.5, 0])

        # --- Brilliant BLACK HOLE IMAGE ---
        blackHole = ImageMobject("./photos/BlackHole.png")
        blackHole.scale(0.5).move_to([0, -0.5, 0])

        # --- KEY BLACK HOLE EQUATIONS ---

        # HAWKING TEMPERATURE: Temperature of black hole radiation
        # T_H = (ℏc)/(16π²k_B GM_H)
        # Shows that black holes emit thermal radiation (Hawking radiation)
        # Smaller black holes are hotter!
        eq1 = MathTex(r"T_H = \frac{hc}{16{\pi}^2K_BGM_H}")
        eq1.rotate(-45 * DEGREES).move_to([1.5, 2, 0]).scale(0.5)
        eq1.color = RED

        # SCHWARZSCHILD RADIUS: Mass-radius relationship for black holes
        # M = (Rc²)/(2G)
        # Rearranged from R_s = 2GM/c²
        # Defines the event horizon radius for a given mass
        eq2 = MathTex(r"M = \frac{Rc^2}{2G}")
        eq2.rotate(45 * DEGREES).move_to([-1.5, 2, 0]).scale(0.5)
        eq2.color = BLUE

        # ESCAPE VELOCITY: Speed needed to escape gravitational pull
        # v_esc = √(2GM/R)
        # At event horizon, v_esc = c (speed of light)
        # This is why nothing can escape a black hole!
        eq3 = MathTex(r"v_{esc} = \sqrt{\frac{2GM}{R}}")
        eq3.move_to([0, -2, 0]).scale(0.5)
        eq3.color = PURPLE

        # --- ANIMATION SEQUENCE ---
        self.play(Write(t1[0]))
        self.wait()
        self.play(Write(t1[1]))
        self.wait()
        self.play(FadeIn(blackHole))
        self.wait(1)

        # Show the three fundamental equations surrounding the black hole
        self.play(FadeIn(eq1))  # Hawking temperature (top right)
        self.wait()
        self.play(FadeIn(eq2))  # Schwarzschild radius (top left)
        self.wait()
        self.play(FadeIn(eq3))  # Escape velocity (bottom)
        self.wait()

        # Clear everything for quote
        self.play(FadeOut(t1, blackHole, eq1, eq2, eq3))
        self.wait()

        # --- HAWKING QUOTE ---
        # Famous quote about Hawking radiation - black holes aren't completely black!
        # They emit radiation and can eventually evaporate
        t2 = MathTex(
            r"\text{Black holes ain't as black}",
            r"\text{as they are painted.}",
            r"\text{-Stephen Hawking}",
        )
        t2.scale(0.5).arrange(DOWN)
        t2[0:2].color = GOLD
        t2[2].color = PURPLE
        self.play(FadeIn(t2))
        self.wait()


# --- SCENE 2: THE SPEED OF LIGHT ---
# Establishes c as the cosmic speed limit
class Second(Scene):
    def construct(self):
        # --- SPEED OF LIGHT CONSTANT ---
        # c = 3×10⁸ m/s
        # This is the maximum speed in the universe
        # Nothing with mass can reach this speed
        # At the event horizon, escape velocity equals c
        t1 = MathTex(r"c = 3\times10^8 \frac{m}{s}")
        t1.color = YELLOW
        t1.move_to([0, 2, 0])

        blackHole = ImageMobject("./photos/BlackHole.png")
        blackHole.scale(0.5).move_to([0, -0.5, 0])

        self.play(Write(t1), run_time=3)
        self.wait()
        self.play(FadeIn(blackHole))
        self.wait()


# --- SCENE 3: DERIVING THE SCHWARZSCHILD RADIUS ---
# Shows the mathematical relationship defining black hole event horizons
class Third(Scene):
    def construct(self):
        # --- ESCAPE VELOCITY FORMULA ---
        # v_esc = √(2GM/R)
        # G = gravitational constant
        # M = mass of object
        # R = radius from center
        t1 = MathTex(r"v_{esc}", r"= \sqrt{\frac{2GM}{R}}}", color=GOLD)

        # Replace v_esc with c (the defining condition for a black hole)
        t2 = MathTex(r"c", color=GOLD)
        t2.move_to(t1[0])

        # --- SCHWARZSCHILD RADIUS DERIVATION ---
        # Setting v_esc = c and solving for M/R:
        # c = √(2GM/R)
        # c² = 2GM/R
        # M/R = c²/(2G)
        #
        # For a given mass M, this determines the radius R of the event horizon
        # R_s = 2GM/c² (Schwarzschild radius)
        t3 = MathTex(
            r"\frac{M}{R} = \frac{c^2}{2G}",  # Mass-to-radius ratio for event horizon
            r"G = 6.67\times10^{-11} \frac{N*m^2}{kg^2}",  # Gravitational constant value
            color=GOLD,
        )
        t3.arrange(DOWN)

        # --- ANIMATION: DERIVATION STEPS ---
        self.play(Write(t1))
        self.wait()

        # Replace escape velocity with speed of light
        self.play(Transform(t1[0], t2))
        self.wait()

        # Move equation to top
        self.play(t1.animate.move_to([0, 2, 0]))
        self.wait()

        # Show derived mass-radius relationship
        self.play(Write(t3[0]))
        self.wait()

        # Show gravitational constant value
        self.play(Write(t3[1]))
        self.wait()


# --- SCENE 4: VISUALIZING LIGHT CAPTURE ---
# Demonstrates how light gets trapped at the event horizon
class Fourth(Scene):
    def construct(self):
        # --- BLACK HOLE STRUCTURE ---
        black_hole = Circle(radius=0.8, color=BLACK, fill_opacity=1)
        black_hole.set_stroke(color=WHITE, width=2)

        # EVENT HORIZON (Schwarzschild radius)
        # The "point of no return"
        # Once past this boundary, even light cannot escape
        # Located at R_s = 2GM/c²
        event_horizon = Circle(radius=1.5, color=YELLOW, fill_opacity=0)
        event_horizon.set_stroke(color=YELLOW, width=3, opacity=0.6)

        # Labels
        bh_label = Text("Black Hole", font_size=24).next_to(black_hole, DOWN)
        eh_label = Text("Event Horizon", font_size=20, color=YELLOW).next_to(
            event_horizon, UP
        )

        self.play(Create(black_hole), Create(event_horizon))
        self.play(Write(bh_label), Write(eh_label))
        self.wait(0.5)

        # --- LIGHT RAYS APPROACHING BLACK HOLE ---
        # Create 12 light rays coming from all directions
        num_rays = 12
        light_rays = []

        for i in range(num_rays):
            angle = i * TAU / num_rays  # Evenly distributed around circle

            # Starting position (far from black hole)
            start_pos = np.array([np.cos(angle) * 5, np.sin(angle) * 5, 0])

            # Light particle (photon)
            light_dot = Dot(start_pos, color=YELLOW, radius=0.08)
            light_dot.set_sheen(-0.5, DOWN)  # Add slight glow effect

            # Light trail showing path
            trail = TracedPath(
                light_dot.get_center,
                stroke_color=YELLOW,
                stroke_width=2,
                dissipating_time=0.5,  # Fade out after 0.5 seconds
            )

            light_rays.append((light_dot, trail, angle))

        # Show all light rays starting positions
        self.play(*[FadeIn(dot) for dot, _, _ in light_rays])

        # Add trails to track light paths
        for _, trail, _ in light_rays:
            self.add(trail)

        # --- ANIMATE LIGHT BEING PULLED INTO BLACK HOLE ---
        animations = []
        for dot, trail, angle in light_rays:

            # CURVED PATH: Light follows geodesics (curved spacetime)
            # Spacetime curvature increases near massive objects
            # Path curves more sharply as it approaches event horizon
            def curve_path(t, start_angle=angle):
                # r: radius decreases from 5 to 0.8 (approaches black hole)
                r = 5 * (1 - t) + 0.8 * t

                # theta: angular position changes (spiral path due to frame-dragging)
                theta = start_angle + t * PI / 2  # 90-degree rotation during approach

                return np.array([np.cos(theta) * r, np.sin(theta) * r, 0])

            # Create animation following the curved path
            animations.append(
                MoveAlongPath(
                    dot,
                    ParametricFunction(
                        lambda t, sa=angle: curve_path(t, sa), t_range=[0, 1]
                    ),
                    rate_func=rush_into,  # Accelerate as approaching (gravitational acceleration)
                    run_time=3,
                )
            )

        # Execute all light ray animations simultaneously
        self.play(*animations)

        # Light disappears at event horizon (trapped forever)
        self.play(*[FadeOut(dot) for dot, _, _ in light_rays])
