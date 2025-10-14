from manim import *
import math

class Start(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Viewer Request:}")
        textTop.color = RED
        
        textMid = MathTex(r"\text{Solving Differential Equations}")
        textMid.color = GOLD
        
        text = VGroup(textTop, textMid)
        text.scale(0.5)
        text.arrange(DOWN)
        
        self.play(Write(textTop))
        self.play(Write(textMid))
        self.play(FadeOut(textTop))
        
        self.play(textMid.animate.shift(3*UP))
        
        dq1 = MathTex(r"\frac{dy}{dx} = \frac{4+9y^2}{e^{2x+1}}")
        dq1.color = RED
        step1 = MathTex(r"\text{Step 1: Seperation of Variables:}")
        step1.color = GOLD
        s1 = MathTex(r"\frac{1}{4+9y^2} dy = \frac{1}{e^{2x+1}} dx")
        s1.color = RED
        step2 = MathTex(r"\text{Step 2: Integrate Both Sides:}")
        step2.color = GOLD
        s2 = MathTex(r"\int \frac{1}{4+9y^2} dy = \int \frac{1}{e^{2x+1}} dx")
        s2.color = RED
                
        diffEq = VGroup(dq1, step1, s1, step2, s2)
        diffEq.arrange(DOWN)
        diffEq.scale(0.5)
        diffEq.shift(1.25*UP)
        
        self.play(Write(dq1))
        
        self.play(Write(step1))
        self.play(Write(s1))
        self.wait(1)
        
        self.play(Write(step2))
        self.play(Write(s2))
        self.wait(1)
        
        self.play(FadeOut(textMid, step1, s1, step2))
        self.play(dq1.animate.shift(0.25*UP), s2.animate.shift(1.5*UP))

class Second(Scene):
    def construct(self):
        ##OLD
        textTop = MathTex(r"\text{Viewer Request:}")
        textTop.color = RED
        
        textMid = MathTex(r"\text{Solving Differential Equations}")
        textMid.color = GOLD
        
        text = VGroup(textTop, textMid)
        text.scale(0.5)
        text.arrange(DOWN)
        textMid.shift(3*UP)
        
        dq1 = MathTex(r"\frac{dy}{dx} = \frac{4+9y^2}{e^{2x+1}}")
        dq1.color = RED
        step1 = MathTex(r"\text{Step 1: Seperation of Variables:}")
        step1.color = GOLD
        s1 = MathTex(r"\frac{1}{4+9y^2} dy = \frac{1}{e^{2x+1}} dx")
        s1.color = RED
        step2 = MathTex(r"\text{Step 2: Integrate Both Sides:}")
        step2.color = GOLD
        s2 = MathTex(r"\int \frac{1}{4+9y^2} dy = \int \frac{1}{e^{2x+1}} dx")
        s2.color = RED
                
        diffEq = VGroup(dq1, step1, s1, step2, s2)
        diffEq.arrange(DOWN)
        diffEq.scale(0.5)
        diffEq.shift(1.25*UP)
        
        dq1.shift(0.25*UP)
        s2.shift(1.5*UP)
        self.add(dq1, s2)
        
        ##NEW
        step3 = MathTex(r"\text{Focusing on the left side:}")
        step3.color = GOLD
        s3 = MathTex(r"\int \frac{1}{4+9y^2} dy = \int \frac{1}{4+(3y)^2} dy")
        s3.color = RED
        
        step4 = MathTex(r"\text{Let } u = \frac{3}{2} y, du = \frac{3}{2} dy")
        step4.color = GOLD
        step4Yap = MathTex(r"\text{We do this because we want to put the expression}")
        step4Yap.scale(0.8)
        step4YapCont = MathTex(r"\text{in the form of } \frac{u'}{1 + u^2} \text{ to integrate using arctan.}")
        step4YapCont.scale(0.8)
        
        s4 = MathTex(r"\frac{2}{3} \int \frac{1}{4 + 9 (\frac{2}{3} u)^2} du")
        s4.color = RED
        s4Simp = MathTex(r"\frac{1}{6} \int \frac{1}{1 + u^2} du")
        s4Simp.color = RED
        
        step5 = MathTex(r"\text{The integral of } \frac{1}{1+u^2} \text{ is arctan(u)}")
        step5.color = GOLD
        s5 = MathTex(r"\frac{\text{arctan(u)}}{6}")
        s5.color = RED
        
        diffEqAll = VGroup(step3, s3, step4, step4Yap, step4YapCont)
        diffEqAll.arrange(DOWN)
        diffEqAll.scale(0.5)
        
        step4YapTotal = VGroup(step4Yap, step4YapCont)
        
        diffEqStep2 = VGroup(s4, s4Simp, step5, s5)
        diffEqStep2.arrange(DOWN)
        diffEqStep2.scale(0.5)
        diffEqStep2.shift(1.75*DOWN)
        
        self.play(Write(step3))
        self.play(Write(s3))
        self.wait(1)
        self.play(Write(step4))
        self.play(Write(step4YapTotal))
        self.wait(2)
        self.play(FadeOut(step4YapTotal))
        self.play(Write(s4))
        self.wait(1)
        self.play(Write(s4Simp))
        self.wait(1)
        self.play(Write(step5))
        self.wait(1)
        self.play(FadeOut(step5))
        self.play(Write(s5.shift(0.75*UP)))
        self.wait(2)
        
        self.play(FadeOut(step3, s3, s4, s4Simp))
        self.play(step4.animate.shift(UP), s5.animate.shift(2.25*UP))
        self.wait(2)
        
        finalEq = MathTex(r"\frac{\text{arctan} (\frac{3}{2} y)}{6}")
        finalEq.scale(0.5)
        finalEq.color = RED
        finalEq.shift(0.5*DOWN)
        self.play(Write(finalEq))
        self.wait(1)
        
        self.play(FadeOut(s2[0][0:10], step4, s5))
        self.play(finalEq.animate.shift(2.28*UP, 0.675*LEFT))
        self.wait(1)
        
        
        ##LEFT
        left1 = MathTex(r"\text{Now the right side:}")
        left1.color = GOLD
        
        step1 = MathTex(r"\int \frac{1}{e^{2x+1}} dx = \frac{1}{e} \int e^{-2x} dx")
        step1.color = RED
        
        step2 = MathTex(r"\text{The integral of } u' * e^u = e^u")
        step2.color = GOLD
        
        st2 = MathTex(r"- \frac{1}{2e} \int -2 e^{-2x} dx")
        st2.color = RED
        
        s3 = MathTex(r"- \frac{1}{2e} e^{-2x}")
        s3.color = RED
        
        s4 = MathTex(r"- \frac{1}{2} e^{-2x-1}")
        s4.color = RED
        
        leftAll = VGroup(left1, step1, step2, st2, s3, s4)
        leftAll.scale(0.5)
        leftAll.arrange(DOWN)
        leftAll.shift(0.75*DOWN)
        
        self.play(Write(left1))
        self.play(Write(step1))
        self.wait(1)
        self.play(Write(step2))
        self.play(Write(st2))
        self.wait(1)
        self.play(Write(s3))
        self.wait(1)
        self.play(Write(s4))
        self.wait(1)
        
        self.play(FadeOut(s2[0][11:21], s3, st2, step2, step1, left1))
        self.play(s4.animate.shift(4.16*UP, 0.85*RIGHT))
        self.wait(2)
        
class Third(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Simplifying:}")
        textTop.color = GOLD
        textNext = MathTex(r"\frac{\text{arctan} (\frac{3}{2} y)}{6} = - \frac{1}{2} e^{-2x-1}")
        textNext.color = RED
        step1 = MathTex(r"\text{arctan} (\frac{3}{2} y) = - \frac{3}{e^{2x-1}}")
        step1.color = RED
        step2 = MathTex(r" \frac{3}{2} y = \text{tan} (- \frac{3}{e^{2x-1}})")
        step2.color = RED
        step3 = MathTex(r"y = \frac{2}{3} \text{tan} (- \frac{3}{e^{2x-1}})")
        step3.color = RED
        all = VGroup(textTop, textNext, step1, step2, step3)
        all.scale(0.5)
        all.arrange(DOWN)
        self.play(Write(textTop))
        self.play(Write(textNext))
        self.wait(1)
        self.play(Write(step1))
        self.wait(1)
        self.play(Write(step2))
        self.wait(1)
        self.play(Write(step3))
        self.wait(1)
        
        self.play(FadeOut(textTop, textNext, step1, step2))
        self.play(step3.animate.shift(1.5*UP))
        
        box = SurroundingRectangle(step3, color = GOLD, buff = MED_LARGE_BUFF)
        self.play(Create(box))
        self.wait(2)