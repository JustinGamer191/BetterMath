from manim import *


class Infinity(ThreeDScene):
    def construct(self):
        t1 = (
            MathTex(r"\text{Infinity}", r"\text{What are you?}", color=GOLD)
            .scale(0.5)
            .arrange(DOWN)
        )

        self.play(Write(t1[0]))
        self.play(t1[0].animate.scale(1000))
        self.play(t1[0].animate.scale(0.001))
        self.play(Write(t1[1]))
        self.wait()
        self.play(FadeOut(t1[1]), Transform(t1[0], Circle()))
        self.wait()
        
        
