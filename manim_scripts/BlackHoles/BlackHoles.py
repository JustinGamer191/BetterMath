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
