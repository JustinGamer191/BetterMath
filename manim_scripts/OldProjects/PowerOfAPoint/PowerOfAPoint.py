from manim import *
import math

class Start(Scene):
    def construct(self):
        textTOP = MathTex(r"\text{Proof of}")
        textTOP.shift(1.75*UP)
        
        p1 = np.array([1, math.sqrt(3), 0])
        p2 = np.array([-math.sqrt(2), -math.sqrt(2), 0])
        p3 = np.array([0, 2, 0])
        p4 = np.array([-1, -math.sqrt(3), 0])
        pInt = np.array([-0.647, -0.414, 0])
        
        line12 = Line(p2,p1)
        line12.color = BLUE
        line34 = Line(p3,p4)
        line34.color = RED
        
        circle = Circle(radius = 2, color = BLUE_A)
        
        wholePic = VGroup(circle, line12, line34)
        wholePic.scale(0.5)
        
        textBOTTOM = MathTex(r"\text{Power of a Point}")
        textBOTTOM.shift(1.75*DOWN)
        
        text = VGroup(textTOP, textBOTTOM)
        text.color = GOLD
        
        self.play(Write(textTOP))
        self.play(Create(circle))
        self.play(Create(line12), Create(line34))
        self.play(Write(textBOTTOM))
        self.play(FadeOut(text), run_time = 2)

class Enlarge(Scene):
    def construct(self):
        ##OLD STUFF
        p1 = np.array([1, math.sqrt(3), 0])
        p2 = np.array([-math.sqrt(2), -math.sqrt(2), 0])
        p3 = np.array([0, 2, 0])
        p4 = np.array([-1, -math.sqrt(3), 0])
        pInt = np.array([-0.647, -0.414, 0])
        
        line12 = Line(p2,p1)
        line12.color = BLUE
        line34 = Line(p3,p4)
        line34.color = RED
        
        lineAB = Line(p1, p3)
        lineCD = Line(p2, p4)
        
        circle = Circle(radius = 2, color = BLUE_A)
        
        wholePic = VGroup(circle, line12, line34)
        wholePic.scale(0.5)
        
        self.play(wholePic.animate.scale(2))
        
        d1 = Dot(p3, radius = 0.05)
        l1 = MathTex(r"\text{A}")
        l1.scale(0.5)
        l1.next_to(d1, UL)
        l1.shift(0.2*RIGHT, 0.2*DOWN)
        
        
        
        d2 = Dot(p1, radius = 0.05)
        l2 = MathTex(r"\text{B}")
        l2.scale(0.5)
        l2.next_to(d2, UR)
        l2.shift(0.2*LEFT, 0.2*DOWN)
        
        
        d3 = Dot(p2, radius = 0.05)
        l3 = MathTex(r"\text{C}")
        l3.scale(0.5)
        l3.next_to(d3, DL)
        l3.shift(0.2*RIGHT, 0.2*UP)
        
        
        d4 = Dot(p4, radius = 0.05)
        l4 = MathTex(r"\text{D}")
        l4.scale(0.5)
        l4.next_to(d4, DL)
        l4.shift(0.2*RIGHT, 0.2*UP)
        
        
        d5 = Dot(pInt, radius = 0.05)
        l5 = MathTex(r"\text{E}")
        l5.scale(0.5)
        l5.next_to(d5, UL)
        l5.shift(0.2*RIGHT, 0.2*DOWN)
        
        dotsAndLabels = VGroup(d1, l1, d2, l2, d3, l3, d4, l4, d5, l5)
        
        self.play(Create(d1), Write(l1), Create(d2), Write(l2), FadeIn(lineAB))
        self.play(Create(d3), Write(l3), Create(d4), Write(l4), FadeIn(lineCD))
        self.play(Create(d5), Write(l5))
        
        picWithLabel = VGroup(wholePic, dotsAndLabels, lineAB, lineCD)
        self.play(picWithLabel.animate.scale(0.5).shift(2*UP))
        
        textExp = MathTex(r"\text{Power of a Point:}")
        textExp.color = GOLD
        
        textThe = MathTex(r"\text{AE} * \text{DE} = \text{BE} * \text{CE}")
        textThe[0][0:2].set_color(RED)
        textThe[0][3:5].set_color(RED)
        textThe[0][6:8].set_color(BLUE)
        textThe[0][9:11].set_color(BLUE)
        
        textProof = MathTex(r"\text{Proof:}")
        textProof.color = GOLD
        
        text = VGroup(textExp, textThe, textProof)
        text.arrange(DOWN)
        text.scale(0.5)
        
        self.play(Write(textExp))
        self.play(Write(textThe))
        self.play(Write(textProof))
        self.play(FadeOut(textExp, textThe))
        
        self.play(textProof.animate.shift(3*UP).scale(1.5), picWithLabel.animate.scale(1.5).shift(1.25*DOWN))
        
        angleBAD = Angle.from_three_points(d5,d1,d2, radius = 0.25)
        angleBAD.color = GOLD
        angleDCB = Angle(lineCD, line12, radius = 0.25)
        angleDCB.color = GOLD
        self.play(Create(angleBAD), Create(angleDCB))
        
        congAngle = MathTex(r"\angle \text{BAD} = \angle \text{BCD}")
        congAngle.color = GOLD
        congExp = MathTex(r"\text{Reason: Both Share Arc BD} ")
        text = VGroup(congAngle, congExp)
        text.scale(0.5)
        text.arrange(DOWN)
        text.shift(1.25*DOWN)
        
        self.play(Write(text))
        self.play(FadeOut(congExp))
        
        oppIntAngle = MathTex(r"\angle \text{CED} = \angle \text{AEB}")
        oppIntAngle.color = GOLD
        oppIntExp = MathTex(r"\text{Reason: Opposite Interior Angles}")
        
        textNew = VGroup(oppIntAngle, oppIntExp)
        textNew.scale(0.5)
        textNew.arrange(DOWN)
        textNew.shift(1.75*DOWN)
        
        self.play(Write(textNew))
        
        self.play(FadeOut(oppIntExp))
        
        updatedAll = VGroup(congAngle, oppIntAngle, textProof, picWithLabel, angleDCB, angleBAD)
        self.play(updatedAll.animate.scale(0.75).shift(UP))
        
        expText = MathTex(r"\Delta \text{DEC} \sim \Delta \text{BEA} \text{ by AA similarity}")
        expText.color = GOLD
        
        textFinal = MathTex(r"\frac{\text{DE}}{\text{BE}} = \frac{\text{CE}}{\text{AE}}")
        textFinal[0][0:2].set_color(RED)
        textFinal[0][3:5].set_color(BLUE)
        textFinal[0][6:8].set_color(BLUE)
        textFinal[0][9:11].set_color(RED)
        
        textTrans = MathTex(r"\text{DE} * \text{AE} = \text{CE} * \text{BE}")
        textTrans[0][0:2].set_color(RED)
        textTrans[0][3:5].set_color(RED)
        textTrans[0][6:8].set_color(BLUE)
        textTrans[0][9:11].set_color(BLUE)
        
        textAll = VGroup(expText, textFinal, textTrans)
        textAll.scale(0.375)
        textAll.arrange(DOWN)
        textAll.shift(0.9*DOWN)
        
        self.play(Write(expText))
        self.play(Write(textFinal))
        self.play(Write(textTrans))
        
        self.wait(1)
        
        