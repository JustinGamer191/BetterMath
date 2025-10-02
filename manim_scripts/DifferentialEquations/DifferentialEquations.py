from manim import *



class Intro(Scene):
    def construct(self):
        m1 = MathTex(
            r"\text{Solving First-Order Differential Equations}", 
            r"\text{(and correcting my mistakes from the first video)}"
        )
        m1[0].color, m1[1].color = GOLD, RED
        m1.scale(0.5).arrange(DOWN)
        
        m2 = MathTex(
            r"\frac{dy}{dx} = \frac{4+9y^2}{e^{2x+1}}",
            r"\text{First Step: Separation of Variables}",
            r"\frac{1}{4+9y^2}dy = \frac{1}{e^{2x+1}}dx",
            r"\text{Second Step: Integrate Both Sides}",
            r"\int \frac{1}{4+9y^2}dy = \int \frac{1}{e^{2x+1}}dx",
            
        )
        m2.scale(0.5).arrange(DOWN)
        m2[0].color, m2[1].color, m2[2].color, m2[3].color, m2[4].color = RED, GOLD, RED, GOLD, RED
        
        m3 = MathTex(
            r"\text{To solve left side, we use u-substitution.}",
            r"\text{Let } u = \frac{3}{2}y, du = \frac{3}{2}dy",
            r"\text{We hope to place the expression in the form}",
            r"\frac{u'}{1+u^2} \text{ to match the integral form of arctan(u).}"
        )
        m3.scale(0.5).arrange(DOWN).move_to([0,1,0])
        m3[0].color, m3[1].color, m3[2].color, m3[3].color = GOLD, RED, GOLD, GOLD
        
        m4 = MathTex(
            r"\frac{2}{3} \int \frac{1}{4+4u^2} = \frac{1}{6} \int \frac{1}{1+u^2}",
            r"\frac{d}{du} arctan(u) = \frac{1}{1+u^2}",
            r"\frac{1}{6} \int \frac{1}{1+u^2} = \frac{arctan(u)}{6}",
            r"= \frac{arctan(\frac{3}{2}y)}{6}"
        )
        m4.color = GOLD
        m4.scale(0.5).arrange(DOWN)
        
        self.play(Write(m1), run_time = 2)
        self.wait(2)
        self.play(FadeOut(m1))
        self.play(Write(m2), run_time = 5)
        self.wait(5)
        self.play(FadeOut(m2[0:4]), m2[4].animate.move_to([0,2.5,0]))
        self.wait(2)
        self.play(Write(m3), run_time = 4)
        self.wait(4)
        self.play(FadeOut(m3[0], m3[2], m3[3]), m3[1].animate.move_to([0,2,0]))
        self.play(Write(m4), run_time = 4)
        self.wait(4)
        self.play(FadeOut(m4[0:3], m3[1]), m4[3].animate.move_to([0,-0.5,0]), m2[4].animate.move_to([0,0.5,0]))
        self.wait(2)
        
class Second(Scene):
    def construct(self):
        m0 = MathTex(
            r"\int \frac{1}{4+9y^2} dy = \int \frac{1}{e^{2x+1}}dx",
            r"= \frac{arctan(\frac{3}{2} y)}{6}"
        )
        m0[0].color = RED
        m0[0].scale(0.5).move_to([0,0.5,0])
        m0[1].color = GOLD
        m0[1].scale(0.5).move_to([0,-0.5,0])
        
        m1 = MathTex(
            r"\int \frac{1}{e^{2x+1}}dx = ", r"-\frac{1}{2} e^{-2x-1}", color = RED
        )
        m1.scale(0.5)
        
        m2 = MathTex(
            r"arctan(\frac{3}{2}y) = -\frac{3}{e^{2x+1}}",
            r"\frac{3}{2}y = tan(-\frac{3}{e^{2x+1}})",
            r"y = \frac{2}{3} tan(-\frac{3}{e^{2x+1}})"
        )
        m2.scale(0.5).arrange(DOWN)
        m2[0].color, m2[1].color = GOLD, GOLD
        m2[2].color = PURPLE
        
        self.add(m0)
        self.play(FadeOut(m0[0][0:10], m0[1][0]), m0[1][1:].animate.move_to(m0[0][2]))
        eq1 = VGroup(m0[1][1:], m0[0][10:])
        self.play(eq1.animate.move_to([0,1.5,0]))
        self.play(Write(m1))
        self.play(FadeOut(m1[0], eq1[1][1:]), m1[1].animate.move_to(eq1[1][2]).shift(0.2*DOWN))
        self.play(Write(m2))
        self.wait(4)
        self.play(FadeOut(m2[0], m2[1], eq1[0], m1[1], eq1[1][0]), m2[2].animate.move_to([0,0,0]))
        sorry = MathTex(r"\text{Sorry for the year-long delay!}", r"\text{You thought I forgot the integration constant!!!}")
        sorry.scale(0.5).arrange(DOWN).move_to([0,1,0])
        self.play(Write(sorry[0]))
        self.play(Write(sorry[1]))
        m4 = MathTex(r"y = \frac{2}{3} tan(-\frac{3}{e^{2x+1}}) + C", color = PURPLE)
        m4.scale(0.5)
        self.play(Transform(m2[2], m4))
        self.wait(2)
        