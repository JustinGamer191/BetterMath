from manim import *
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Area of Triangle}")
        textTop.color = GOLD
        
        textMid = MathTex(r"=")
        
        textLow = MathTex(r"\frac{1}{2} \text{A} \text{B} \text{sin} (c)?")
        textLow[0][3:4].color = RED
        textLow[0][4:5].color = BLUE
        textLow[0][9:10].color = GREEN
        
        text = VGroup(textTop, textMid, textLow)
        text.scale(0.5)
        text.arrange(DOWN)
        
        self.play(Write(text))
        self.wait(0.5)
        self.play(FadeOut(textMid, textLow))
        self.play(textTop.animate.shift(2*UP))
        self.wait(0.5)
        
        p1 = np.array([-0.5, 1.5, 0])
        p2 = np.array([-1.5, -1, 0])
        p3 = np.array([1.5, -1, 0])
        p4 = np.array([-0.5, -1, 0])
        lineh = Line(p1,p4)
        lineh.color = GOLD
        labelh = MathTex(r"h").scale(0.5)
        labelh.next_to(lineh, 0.5*RIGHT)
        linehOver = Line(p1,p4)
        linehOver.color = WHITE
        
        lineA = Line(p1,p2)
        lineA.color = RED
        labelA = MathTex(r"\text{A}").scale(0.5)
        labelA.shift(1.25*LEFT, 0.45*UP)
        labelA.color = RED
        
        lineB = Line(p2,p3)
        lineB.color = BLUE
        labelB = MathTex(r"\text{B}").scale(0.5)
        labelB.next_to(lineB, DOWN)
        labelB.color = BLUE
        
        angleC = Angle.from_three_points(p1, p2, p3, other_angle = True)
        angleC.color = GREEN
        labelC = MathTex(r"\text{c}").scale(0.5)
        labelC.shift(1.05*LEFT, 0.65*DOWN)
        labelC.color = GREEN
        
        triangle = Polygon(p1,p2,p3)
        triangle.color = GOLD
        
        self.play(Create(triangle))
        self.play(Write(lineh))
        
        self.play(Write(labelA), Write(lineA))
        self.play(Write(labelB), Write(lineB))
        self.play(Write(labelC), Create(angleC))
        self.play(Write(labelh), Write(linehOver))
        self.wait(1)
        
        area = MathTex(r"\frac{1}{2} * \text{B} * h")
        area[0][4:5].color = BLUE
        area.scale(0.5)
        area.next_to(textTop, 0.5*DOWN)
        
        self.play(Write(area))
        self.wait(1)
        
class Second(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Area of Triangle}")
        textTop.color = GOLD
        
        textMid = MathTex(r"=")
        
        textLow = MathTex(r"\frac{1}{2} * \text{A} * \text{B} * \text{sin} (c)?")
        textLow[0][4:5].color = RED
        textLow[0][6:7].color = BLUE
        textLow[0][12:13].color = GREEN
        
        text = VGroup(textTop, textMid, textLow)
        text.scale(0.5)
        text.arrange(DOWN)
        
        textTop.shift(2*UP)
        
        p1 = np.array([-0.5, 1.5, 0])
        p2 = np.array([-1.5, -1, 0])
        p3 = np.array([1.5, -1, 0])
        p4 = np.array([-0.5, -1, 0])
        lineh = Line(p1,p4)
        lineh.color = GOLD
        labelh = MathTex(r"h").scale(0.5)
        labelh.next_to(lineh, 0.5*RIGHT)
        linehOver = Line(p1,p4)
        linehOver.color = WHITE
        
        lineA = Line(p1,p2)
        lineA.color = RED
        labelA = MathTex(r"\text{A}").scale(0.5)
        labelA.shift(1.25*LEFT, 0.45*UP)
        labelA.color = RED
        
        lineB = Line(p2,p3)
        lineB.color = BLUE
        labelB = MathTex(r"\text{B}").scale(0.5)
        labelB.next_to(lineB, DOWN)
        labelB.color = BLUE
        
        angleC = Angle.from_three_points(p1, p2, p3, other_angle = True)
        angleC.color = GREEN
        labelC = MathTex(r"\text{c}").scale(0.5)
        labelC.shift(1.05*LEFT, 0.65*DOWN)
        labelC.color = GREEN
        
        triangle = Polygon(p1,p2,p3)
        triangle.color = GOLD
        
        area = MathTex(r"\frac{1}{2} * \text{B} * h")
        area[0][4:5].color = BLUE
        area.scale(0.5)
        area.next_to(textTop, 0.5*DOWN)
        diagram = VGroup(triangle, lineA, labelA, lineB, labelB, angleC, labelC, labelh, linehOver)
        oldG = VGroup(textTop, diagram, area)
        self.add(oldG)
        
        ##NEW
        self.play(diagram.animate.scale(0.5).shift(0.75*UP))
        textArea = MathTex(r"\text{sin} (c) = \frac{h}{\text{A}}")
        textArea[0][4:5].color = GREEN
        textArea[0][9:10].color = RED
        
        textCont = MathTex(r"\text{A} * \text{sin} (c) = h")
        textCont[0][0:1].color = RED
        textCont[0][6:7].color = GREEN
        
        textAll = VGroup(textArea, textCont)
        textAll.scale(0.5)
        textAll.arrange(DOWN)
        textAll.shift(0.5*DOWN)
        
        self.play(Write(textAll))
        self.play(Uncreate(diagram))
        self.play(textAll.animate.shift(1.75*UP))
        
        textAreaFinal = MathTex(r"\frac{1}{2} * \text{A} * \text{B} * \text{sin} (c)")
        textAreaFinal[0][4:5].color = RED
        textAreaFinal[0][6:7].color = BLUE
        textAreaFinal[0][12:13].color = GREEN
        textAreaFinal.scale(0.5)
        textAreaFinal.shift(0.25*UP)
        
        self.play(Write(textAreaFinal))
        self.play(FadeOut(area, textAll))
        self.play(textTop.animate.shift(2*DOWN), textAreaFinal.animate.shift(0.25*DOWN))
        
        final = VGroup(textTop, textAreaFinal)
        self.play(final.animate.scale(2))
        self.play(final.animate.scale(0.5))
        self.wait(1)
        