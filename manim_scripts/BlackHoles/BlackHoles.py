from manim import *


class Intro(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Black Holes}", r"\text{What are they?}", color=GOLD)
        t1.scale(0.5).arrange(DOWN)
        t1.move_to([0, 1.5, 0])

        blackHole = ImageMobject("./photos/BlackHole.png")
        blackHole.scale(0.5).move_to([0, -0.5, 0])

        eq1 = MathTex(r"T_H = \frac{hc}{16{\pi}^2K_BGM_H}")
        eq1.rotate(-45 * DEGREES).move_to([1.5, 2, 0]).scale(0.5)
        eq1.color = RED
        eq2 = MathTex(r"M = \frac{Rc^2}{2G}")
        eq2.rotate(45 * DEGREES).move_to([-1.5, 2, 0]).scale(0.5)
        eq2.color = BLUE
        eq3 = MathTex(r"v_{esc} = \sqrt{\frac{2GM}{R}}")
        eq3.move_to([0, -2, 0]).scale(0.5)
        eq3.color = PURPLE

        self.play(Write(t1[0]))
        self.wait()
        self.play(Write(t1[1]))
        self.wait()
        self.play(FadeIn(blackHole))
        self.wait(1)
        self.play(FadeIn(eq1))
        self.wait()
        self.play(FadeIn(eq2))
        self.wait()
        self.play(FadeIn(eq3))
        self.wait()
        self.play(FadeOut(t1, blackHole, eq1, eq2, eq3))
        self.wait()
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


class Second(Scene):
    def construct(self):
        t1 = MathTex(r"c = 3\times10^8 \frac{m}{s}")
        t1.color = YELLOW
        t1.move_to([0, 2, 0])

        blackHole = ImageMobject("./photos/BlackHole.png")
        blackHole.scale(0.5).move_to([0, -0.5, 0])

        self.play(Write(t1), run_time=3)
        self.wait()
        self.play(FadeIn(blackHole))
        self.wait()


class Third(Scene):
    def construct(self):
        t1 = MathTex(r"v_{esc}", r"= \sqrt{\frac{2GM}{R}}}", color=GOLD)
        t2 = MathTex(r"c", color=GOLD)
        t2.move_to(t1[0])
        t3 = MathTex(
            r"\frac{M}{R} = \frac{c^2}{2G}",
            r"G = 6.67\times10^{-11} \frac{N*m^2}{kg^2}",
            color=GOLD,
        )
        t3.arrange(DOWN)
        self.play(Write(t1))
        self.wait()
        self.play(Transform(t1[0], t2))
        self.wait()
        self.play(t1.animate.move_to([0, 2, 0]))
        self.wait()
        self.play(Write(t3[0]))
        self.wait()
        self.play(Write(t3[1]))
        self.wait()


class Fourth(Scene):
    def construct(self):
        black_hole = Circle(radius=0.8, color=BLACK, fill_opacity=1)
        black_hole.set_stroke(color=WHITE, width=2)

        event_horizon = Circle(radius=1.5, color=YELLOW, fill_opacity=0)
        event_horizon.set_stroke(color=YELLOW, width=3, opacity=0.6)

        bh_label = Text("Black Hole", font_size=24).next_to(black_hole, DOWN)
        eh_label = Text("Event Horizon", font_size=20, color=YELLOW).next_to(
            event_horizon, UP
        )

        self.play(Create(black_hole), Create(event_horizon))
        self.play(Write(bh_label), Write(eh_label))
        self.wait(0.5)

        num_rays = 12
        light_rays = []

        for i in range(num_rays):
            angle = i * TAU / num_rays
            start_pos = np.array([np.cos(angle) * 5, np.sin(angle) * 5, 0])

            light_dot = Dot(start_pos, color=YELLOW, radius=0.08)
            light_dot.set_sheen(-0.5, DOWN)

            trail = TracedPath(
                light_dot.get_center,
                stroke_color=YELLOW,
                stroke_width=2,
                dissipating_time=0.5,
            )

            light_rays.append((light_dot, trail, angle))

        self.play(*[FadeIn(dot) for dot, _, _ in light_rays])

        for _, trail, _ in light_rays:
            self.add(trail)

        animations = []
        for dot, trail, angle in light_rays:

            def curve_path(t, start_angle=angle):
                r = 5 * (1 - t) + 0.8 * t
                theta = start_angle + t * PI / 2
                return np.array([np.cos(theta) * r, np.sin(theta) * r, 0])

            animations.append(
                MoveAlongPath(
                    dot,
                    ParametricFunction(
                        lambda t, sa=angle: curve_path(t, sa), t_range=[0, 1]
                    ),
                    rate_func=rush_into,
                    run_time=3,
                )
            )

        self.play(*animations)

        self.play(*[FadeOut(dot) for dot, _, _ in light_rays])
