from manim import *
import numpy as np

class Uncertainty(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Heisenberg's Uncertainty Principle}", color = GOLD)
        t1.move_to([0,0.5,0])
        t2 = MathTex(r"(\Delta x)(\Delta \rho) = \frac{h}{4 \pi}", color = RED)
        VGroup(t1,t2).scale(0.5)
        t2.next_to(t1, DOWN)
        
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2)
        