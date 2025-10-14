from manim import *

class Scene(Scene):
    def construct(self):
        t1 = MathTex(r"c_0 + c_1 ", r"z", r" + c_2 z^2 + ... + c_n z^n = 0")
        t1[1].color = GOLD
        t2 = MathTex(r"\text{Complex Conjugate Root Theorem}")
        t3 = MathTex(r"\text{A Proof}")
        t = VGroup(t1,t2,t3)
        t.scale(0.5)
        t.arrange(DOWN)
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(1)
        self.play(FadeOut(t1[0]), FadeOut(t1[2]), FadeOut(t2), FadeOut(t3))
        self.play(t1[1].animate.move_to([0,2,0]).scale(2))
        self.wait(1)
class Scene1(Scene):
    def construct(self):
        t1 = MathTex(r"z")
        t1.color = GOLD
        t1.move_to([0,2,0])
        t2 = MathTex(r"\text{Basis: Let } \lambda = a + bi")
        t25 = MathTex(r"\overline{\lambda} = a - bi")
        t3 = MathTex(r"\overline{\lambda^n} = (\overline{\lambda})^n")
        t4 = MathTex(r"c(\overline{\lambda}) = \overline{c\lambda}")
        t5 = MathTex(r"\overline{\lambda_1} + \overline{\lambda_2} = \overline{\lambda_1 + \lambda_2}")
        t = VGroup(t2,t25, t3,t4, t5)
        t.arrange(DOWN)
        t.scale(0.5)
        t.move_to([0,0.75,0])
        self.add(t1)
        self.play(Write(t), run_time = 5)
        self.play(FadeOut(t1))
        self.play(t.animate.move_to([0,2.5,0]))
        self.wait(1)

class Scene2(Scene):
    def construct(self):
        t2 = MathTex(r"\text{Basis: Let } \lambda = a + bi")
        t25 = MathTex(r"\overline{\lambda} = a - bi")
        t3 = MathTex(r"\overline{\lambda^n} = (\overline{\lambda})^n")
        t4 = MathTex(r"c(\overline{\lambda}) = \overline{c\lambda}")
        t5 = MathTex(r"\overline{\lambda_1} + \overline{\lambda_2} = \overline{\lambda_1 + \lambda_2}")
        t = VGroup(t2,t25, t3,t4, t5)
        t.arrange(DOWN)
        t.scale(0.5)
        t.move_to([0,2.5,0])
        self.add(t)
        
        t6 = MathTex(r"\text{Let }", r"\text{z}" , r"\text{ be the solution to the equation}")
        t6[1].color = GOLD
        t7 = MathTex(r"c_0 + c_1", r"z", r" + c_2 z^2 + ... + c_n z^n = 0")
        t7[1].color = GOLD
        
        tt = VGroup(t6, t7)
        
        tt.scale(0.35)
        tt.arrange(DOWN)
        tt.move_to([0,1,0])
        
        x1 = MathTex(r"\sum_{0}^{n} c_n z^n = 0")
        x2 = MathTex(r"\sum_{0}^{n} c_n \overline{z}^n", r" = \sum_{0}^{n} c_n \overline{z^n}")
        x4 = MathTex(r"\sum_{0}^{n} \overline{c_n z^n}= ", r"\overline{\sum_{0}^{n} c_n z^n}")
        x5 = MathTex(r" = \overline{0}", r" = 0")
        
        x = VGroup(x1,x2,x4,x5)
        x.arrange(DOWN)
        x.scale(0.5)
        
        x.move_to([0,-1,0])
        
        self.play(Write(tt), run_time = 2)
        self.wait(1)
        
        self.play(Write(x1))
        self.play(Write(x2[0]))
        self.play(Circumscribe(t3), run_time = 2)
        self.play(Write(x2[1]))
        self.play(Circumscribe(t4), run_time = 2)
        self.play(Write(x4[0]))
        self.play(Circumscribe(t5), run_time = 2)
        self.play(Write(x4[1]))
        self.wait(2)
        self.play(FadeOut(t,tt,x1,x2))
        self.play(x4.animate.move_to([0,2,0]))
        x5.move_to([0,1.25,0])
        self.play(Write(x5))
        self.wait(1)
        
        conclusion = MathTex(r"\overline{z} \text{ is also a root of }")
        conclusion2 = MathTex(r"c_0 + c_1", r"z", r" + c_2 z^2 + ... + c_n z^n = 0")
        
        c = VGroup(conclusion, conclusion2)
        c.arrange(DOWN)
        c.scale(0.35)
        c.move_to([0,0,0])
        self.play(Write(c), run_time = 3)
        self.play(Circumscribe(c))
        self.wait(2)