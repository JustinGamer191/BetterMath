from manim import*
import math

class Cover(Scene):
    def construct(self):
        textInd = MathTex(r"\text{Induction: A Proof Technique}")
        
        textExp = MathTex(r"\text{Induction closely resembles dominoes.}")
        textExp.scale(0.8)
        
        textFin = MathTex(r"\text{If each domino hits the next, they all fall.}")
        textFin.scale(0.8)
        
        textAll = VGroup(textInd, textExp, textFin)
        textAll.scale(0.5)
        textAll.color = GOLD
        textAll.arrange(DOWN)
        
        textExp.shift(1*UP)
        textFin.shift(1*UP)
        
        r1 = Rectangle(width = 0.5, height = 1.5)
        r1.move_to([-1.5,-1,0])
        r2 = Rectangle(width = 0.5, height = 1.5)
        r2.move_to([-0.5,-1,0])
        r3 = Rectangle(width = 0.5, height = 1.5)
        r3.move_to([0.5,-1,0])
        r4 = Rectangle(width = 0.5, height = 1.5)
        r4.move_to([1.5,-1,0])
        
        rects = VGroup(r1,r2,r3,r4)
        rects.color = GOLD
        
        self.play(Write(textInd))
        self.play(textInd.animate.shift(1*UP))
        self.play(Write(textExp))
        self.play(Write(textFin))
        
        self.play(Create(rects), run_time = 2)
        self.play(Rotate(r1, angle = -PI/4))
        self.play(Rotate(r2, angle = -PI/4))
        self.play(Rotate(r3, angle = -PI/4))
        self.play(Rotate(r4, angle = -PI/4))
        self.wait(1)
        
class Second(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Steps to using Induction:}")
        
        textS1 = MathTex(r"1: \text{Prove the base case.}")
        textS1.scale(0.8)
        textS2 = MathTex(r"2: \text{Assume the statement is true for n}")
        textS2.scale(0.8)
        textS3 = MathTex(r"3: \text{Prove the statement is true for n + 1}")
        textS3.scale(0.8)
        
        textAll = VGroup(textTop, textS1, textS2, textS3)
        textAll.scale(0.5)
        textAll.color = GOLD
        textAll.arrange(DOWN)
        
        self.play(Write(textTop))
        self.play(Write(textS1))
        self.play(Write(textS2))
        self.play(Write(textS3))
        self.wait(1)
        self.play(FadeOut(textAll))

class Third(Scene):
    def construct(self):
        textEx = MathTex(r"\text{Ex: Prove that:}")
        textEx.color = GOLD
        textEx2 = MathTex(r"1^2 + 2^2 + ... + n^2 = \frac{n(n+1)(2n+1)}{6}")
        textEx2.scale(0.6)
        
        s1 = MathTex(r"\text{1: When n = 1,}")
        s1.color = GOLD
        s1C = MathTex(r"1 = \frac{(1)(2)(3)}{6} = 1")
        s1C.scale(0.6)
        
        s2 = MathTex(r"\text{2: Assume the statement}")
        s2.color = GOLD
        s2C = MathTex(r"1^2 + 2^2 + ... + n^2 = \frac{n(n+1)(2n+1)}{6}")
        s2C.scale(0.6)
        s2CC = MathTex(r"\text{is true for n.}")
        s2CC.color = GOLD
        
        s3 = MathTex(r"\text{We now have to prove:}")
        s3.color = GOLD
        s3C = MathTex(r"\frac{(n+1)(n+2)(2n+3)}{6} = \frac{n(n+1)(2n+1)}{6} + (n+1)^2")
        s3C.scale(0.6)
        
        textAll = VGroup(textEx, textEx2, s1, s1C, s2, s2C, s2CC, s3, s3C)
        textAll.scale(0.5)
        textAll.arrange(DOWN)
        
        textNext = VGroup(s3, s3C)
        
        self.play(Write(textEx))
        self.play(Write(textEx2))
        self.play(Write(s1))
        self.play(Write(s1C))
        self.play(Write(s2))
        self.play(Write(s2C))
        self.play(Write(s2CC))
        self.play(Write(s3))
        self.play(Write(s3C))
        self.wait(1)
        self.play(FadeOut(textEx, textEx2, s1, s1C, s2, s2C, s2CC))
        self.play(textNext.animate.move_to([0,2,0]))
        self.wait(1)
        
        
        sF = MathTex(r"\frac{(n+1)(n+2)(2n+3)}{6} =")
        sFC = MathTex(r"\frac{2n^3 + 9n^2 + 13n + 6}{6}")
        
        sR = MathTex(r"\frac{n(n+1)(2n+1)}{6} + (n+1)^2 = ")
        sRC = MathTex(r"\frac{2n^3 + 9n^2 + 13n + 6}{6}")
        
        sAll = VGroup(sF, sFC, sR, sRC)
        sAll.scale(0.3)
        sAll.arrange(DOWN)
        sAll.shift(0.5*UP)
        
        self.play(Write(sF))
        self.play(Write(sFC))
        self.play(Write(sR))
        self.play(Write(sRC))
        self.play(FadeOut(sF, sR, textNext))
        self.play(sFC.animate.move_to([0,0,0]), sRC.animate.move_to([0,0,0]))
        sA = VGroup(sFC, sRC)
        self.play(Circumscribe(sA, color = GOLD))
        self.wait(1)