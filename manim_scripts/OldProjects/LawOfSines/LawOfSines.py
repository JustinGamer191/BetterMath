from manim import *
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Law of Sines:}")
        textTop.color = GOLD
        
        textMid = MathTex(r"\frac{\text{sin} (a)}{\text{A}} = \frac{\text{sin} (b)}{\text{B}} = \frac{\text{sin} (c)}{\text{C}}")
        textMid[0][4:5].set_color(RED)
        textMid[0][7:8].set_color(RED)
        
        textMid[0][13:14].set_color(BLUE)
        textMid[0][16:17].set_color(BLUE)
        
        textMid[0][22:23].set_color(GREEN)
        textMid[0][25:26].set_color(GREEN)    
        
        textAll = VGroup(textTop, textMid)
        textAll.arrange(DOWN)
        textAll.scale(0.5)
        self.play(Write(textTop))
        self.play(Write(textMid))
        
        self.play(textAll.animate.shift(2.25*UP))
        
class Second(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Law of Sines:}")
        textTop.color = GOLD
        
        textMid = MathTex(r"\frac{\text{sin} (a)}{\text{A}} = \frac{\text{sin} (b)}{\text{B}} = \frac{\text{sin} (c)}{\text{C}}")
        textMid[0][4:5].set_color(RED)
        textMid[0][7:8].set_color(RED)
        
        textMid[0][13:14].set_color(BLUE)
        textMid[0][16:17].set_color(BLUE)
        
        textMid[0][22:23].set_color(GREEN)
        textMid[0][25:26].set_color(GREEN)    
        
        textAll = VGroup(textTop, textMid)
        textAll.arrange(DOWN)
        textAll.scale(0.5)
        self.add(textAll.shift(2.25*UP))
        
        
        
        ##NEW
        p1 = np.array([-0.75,1,0])
        p2 = np.array([-1.5,-2,0])
        p3 = np.array([1.5,-2,0])
        p4 = np.array([-0.75,-2,0])
        
        triangle = Polygon(p1, p2, p3)
        triangle.color = BLUE_A
        
        height = Line(p1, p4)
        height.color = BLUE_A
        
        lineA = Line(p1,p3)
        lineB = Line(p1,p2)
        
        angleA = Angle.from_three_points(p1,p2,p3, radius = 0.25, other_angle = True)
        angleA.color = RED
        aLabel = MathTex(r"a")
        aLabel.scale(0.5)
        aLabel.next_to(angleA, UR)
        aLabel.shift(0.2*DOWN, 0.2*LEFT)
        aLabel.color = RED
        
        sideA = MathTex(r"\text{A}")
        sideA.scale(0.5)
        sideA.next_to(lineA, UR)
        sideA.shift(1.25*DOWN, 1.25*LEFT)
        sideA.color = RED
        
        angleB = Angle.from_three_points(p1,p3,p2, radius = 0.4, other_angle = False)
        angleB.color = BLUE
        bLabel = MathTex(r"b")
        bLabel.scale(0.5)
        bLabel.next_to(angleB, UL)
        bLabel.shift(0.3*DOWN, 0.25*RIGHT)
        bLabel.color = BLUE
        
        sideB = MathTex(r"\text{B}")
        sideB.scale(0.5)
        sideB.next_to(lineB, UL)
        sideB.shift(1.25*DOWN, 0.4*RIGHT)
        sideB.color = BLUE
        
        labelH = MathTex(r"\text{h}")
        labelH.scale(0.5)
        labelH.next_to(height, RIGHT)
        labelH.shift(0.1*LEFT)
        labelH.color = BLUE_A
        
        allA = VGroup(angleA, aLabel, sideA)
        allB = VGroup(angleB, bLabel, sideB)
        allH = VGroup(height, labelH)
        
        self.play(Create(triangle))
        self.play(Create(height))
        self.play(Create(angleA), Write(aLabel))
        self.play(Write(sideA))
        self.play(Create(angleB), Write(bLabel))
        self.play(Write(sideB))
        self.play(Write(labelH))
        
        tDiagram = VGroup(triangle, height, allA, allB, allH)
        self.play(FadeOut(textAll))
        self.play(tDiagram.animate.scale(0.75).shift(2*UP))
        self.wait(1)
        
class Third(Scene):
    def construct(self):
        p1 = np.array([-0.75,1,0])
        p2 = np.array([-1.5,-2,0])
        p3 = np.array([1.5,-2,0])
        p4 = np.array([-0.75,-2,0])
        
        triangle = Polygon(p1, p2, p3)
        triangle.color = BLUE_A
        
        height = Line(p1, p4)
        height.color = BLUE_A
        
        lineA = Line(p1,p3)
        lineB = Line(p1,p2)
        
        angleA = Angle.from_three_points(p1,p2,p3, radius = 0.25, other_angle = True)
        angleA.color = RED
        aLabel = MathTex(r"a")
        aLabel.scale(0.5)
        aLabel.next_to(angleA, UR)
        aLabel.shift(0.2*DOWN, 0.2*LEFT)
        aLabel.color = RED
        
        sideA = MathTex(r"\text{A}")
        sideA.scale(0.5)
        sideA.next_to(lineA, UR)
        sideA.shift(1.25*DOWN, 1.25*LEFT)
        sideA.color = RED
        
        angleB = Angle.from_three_points(p1,p3,p2, radius = 0.4, other_angle = False)
        angleB.color = BLUE
        bLabel = MathTex(r"b")
        bLabel.scale(0.5)
        bLabel.next_to(angleB, UL)
        bLabel.shift(0.3*DOWN, 0.25*RIGHT)
        bLabel.color = BLUE
        
        sideB = MathTex(r"\text{B}")
        sideB.scale(0.5)
        sideB.next_to(lineB, UL)
        sideB.shift(1.25*DOWN, 0.4*RIGHT)
        sideB.color = BLUE
        
        labelH = MathTex(r"\text{h}")
        labelH.scale(0.5)
        labelH.next_to(height, RIGHT)
        labelH.shift(0.1*LEFT)
        labelH.color = BLUE_A
        
        allA = VGroup(angleA, aLabel, sideA)
        allB = VGroup(angleB, bLabel, sideB)
        allH = VGroup(height, labelH)

        tDiagram = VGroup(triangle, height, allA, allB, allH)
        self.add(tDiagram.scale(0.75).shift(2*UP))
        
        
        ##NEW
        textA = MathTex(r"\text{sin} (a) = \frac{\text{h}}{\text{B}}")
        textA[0][4:5].set_color(RED)
        textA[0][9:10].set_color(BLUE)
           
        textAH = MathTex(r"\text{sin} (a) * \text{B} = \text{h}")
        textAH[0][4:5].set_color(RED)
        textAH[0][7:8].set_color(BLUE)
        
        textB = MathTex(r"\text{sin} (b) = \frac{\text{h}}{\text{A}}")
        textB[0][4:5].set_color(BLUE)
        textB[0][9:10].set_color(RED)
        
        textBH = MathTex(r"\text{sin} (b) * \text{A} = \text{h}")
        textBH[0][4:5].set_color(BLUE)
        textBH[0][7:8].set_color(RED)
        
        textAll = VGroup(textA, textAH, textB, textBH)
        textAll.scale(0.5)
        textAll.arrange(DOWN)
        textAll.shift(DOWN)
        self.play(Write(textA))
        self.play(Write(textAH))
        self.play(Write(textB))
        self.play(Write(textBH))
        self.wait(0.5)
        
        self.play(FadeOut(textA), FadeOut(textB))
        self.play(textAH.animate.shift(0.75*UP), textBH.animate.shift(1.5*UP))
        
        textCombine = MathTex(r"\text{sin} (a) * \text{B} = \text{sin} (b) * \text{A}")
        textCombine[0][4:5].set_color(RED)
        textCombine[0][7:8].set_color(BLUE)
        textCombine[0][13:14].set_color(BLUE)
        textCombine[0][16:17].set_color(RED)
        textCombine.scale(0.5)
        
        textFinal = MathTex(r"\frac{\text{sin} (a)}{\text{A}} = \frac{\text{sin} (b)}{\text{B}}")
        textFinal.scale(0.5)
        textFinal[0][4:5].set_color(RED)
        textFinal[0][7:8].set_color(RED)

        textFinal[0][13:14].set_color(BLUE)
        textFinal[0][16:17].set_color(BLUE)
        
        textAllFinal = VGroup(textCombine, textFinal)
        textAllFinal.arrange(DOWN)
        textAllFinal.shift(1.5*DOWN)
        self.play(Write(textCombine))
        self.play(Write(textFinal))
        
        self.play(FadeOut(tDiagram, textCombine, textAH, textBH))
        self.play(textFinal.animate.shift(2*UP))
        
        textC = MathTex(r"= \frac{\text{sin} (c)}{\text{C}}")
        textC[0][5:6].set_color(GREEN)
        textC[0][8:9].set_color(GREEN)
        textC.scale(0.5)
        self.play(textFinal.animate.shift(0.5*LEFT))
        self.play(Write(textC.next_to(textFinal, RIGHT).shift(0.1*LEFT)))
        self.wait(2)
        self.play(FadeOut(textFinal, textC))
        
        
        