from manim import *
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Proof that:}")
        textTop.color = GOLD
        textTop.scale(1.5)
        textLow = MathTex(
            r"\text{sin}(a+b) \text{ = } \text{sin}(a) \text{cos}(b) + \text{sin}(b) \text{cos}(a)",
            substrings_to_isolate = "a" + "b"
            )
        textLow.set_color_by_tex("a", RED)
        textLow.set_color_by_tex("b", BLUE)
        textLow.scale(0.9)
        
        text = VGroup(textTop, textLow)
        text.arrange(DOWN)
        text.scale(0.5)
        #textLow[0][5:6].set_color(RED)
        
        self.play(Write(text))
        self.wait(1.5)
        
class Triangle(Scene):
    def construct(self):
        p1 = np.array([0,2,0])
        p2 = np.array([-1.25,-2,0])
        p3 = np.array([2,-2,0])
        p4 = np.array([0,-2,0])
        
        line23 = Line(p2, p3)
        line = Line(p1,p4)
        line.color = GOLD
        
        triangle = Polygon(p1, p2, p3)
        triangle.color = GOLD
        
        angleA = Angle.from_three_points(p2,p1,p4, radius = 1)
        angleA.color = RED
        aLabel = MathTex(r"a")
        aLabel.scale(0.5)
        aLabel.next_to(angleA, DOWN)
        aLabel.shift(0.1*UP, 0.075*LEFT)
        aLabel.color = RED
        
        self.play(Create(triangle))
        self.play(Create(line))
        
        rightA = RightAngle(line, line23, length = 0.25, quadrant = (-1,-1))
        self.play(Create(rightA))
        rightB = RightAngle(line, line23, length = 0.25, quadrant = (-1,1))
        self.play(Create(rightB))
        
        self.play(Create(angleA), Write(aLabel))
        
        angleB = Angle.from_three_points(p3,p1,p4, radius = 1, other_angle = True)
        angleB.color = BLUE
        bLabel = MathTex(r"b")
        bLabel.scale(0.5)
        bLabel.next_to(angleB, DOWN)
        bLabel.shift(0.15*UP, 0.07*RIGHT)
        bLabel.color = BLUE
        
        self.play(Create(angleB), Write(bLabel))
        
        length = MathTex(r"1")
        length.scale(0.75)
        length.shift(0.2*RIGHT, 0.2*DOWN)
        
        self.play(Write(length))
        
        tanA = MathTex(r"\text{tan} (a)")
        tanA[0][4:5].set_color(RED)
        tanA.scale(0.5)
        tanA.shift(2.25*DOWN, 0.75*LEFT)
        
        tanB = MathTex(r"\text{tan} (b)")
        tanB[0][4:5].set_color(BLUE)
        tanB.scale(0.5)
        tanB.shift(2.25*DOWN, 1.15*RIGHT)
        
        self.play(Write(tanA))
        self.play(Write(tanB))
        
        cosA = MathTex(r"\frac{1}{\text{cos} (a)}")
        cosA[0][6:7].set_color(RED)
        cosA.scale(0.5)
        cosA.shift(0.5*UP, 1*LEFT)
        
        cosB = MathTex(r"\frac{1}{\text{cos} (b)}")
        cosB[0][6:7].set_color(BLUE)
        cosB.scale(0.5)
        cosB.shift(0.5*UP, 1.5*RIGHT)
        
        self.play(Write(cosA))
        self.play(Write(cosB))
        
        area = MathTex(
            r"\text{Area} = \frac{\text{tan}(a) + \text{tan}(b)}{2}",
            )
        area.scale(0.5)
        area.shift(2.5*UP)
        area[0][0:4].set_color(GOLD) 
        area[0][9:10].set_color(RED)
        area[0][16:17].set_color(BLUE)
        
        self.play(Write(area))
        self.wait(1)

class Explanation(Scene):
    def construct(self):
        ##OLD DIAGRAM
        p1 = np.array([0,2,0])
        p2 = np.array([-1.25,-2,0])
        p3 = np.array([2,-2,0])
        p4 = np.array([0,-2,0])
        
        line23 = Line(p2, p3)
        line = Line(p1,p4)
        line.color = GOLD
        
        triangle = Polygon(p1, p2, p3)
        triangle.color = GOLD
        
        angleA = Angle.from_three_points(p2,p1,p4, radius = 1)
        angleA.color = RED
        aLabel = MathTex(r"a")
        aLabel.scale(0.5)
        aLabel.next_to(angleA, DOWN)
        aLabel.shift(0.1*UP, 0.075*LEFT)
        aLabel.color = RED
        
        rightA = RightAngle(line, line23, length = 0.25, quadrant = (-1,-1))
        rightB = RightAngle(line, line23, length = 0.25, quadrant = (-1,1))
        
        
        angleB = Angle.from_three_points(p3,p1,p4, radius = 1, other_angle = True)
        angleB.color = BLUE
        bLabel = MathTex(r"b")
        bLabel.scale(0.5)
        bLabel.next_to(angleB, DOWN)
        bLabel.shift(0.15*UP, 0.07*RIGHT)
        bLabel.color = BLUE
        
        
        length = MathTex(r"1")
        length.scale(0.75)
        length.shift(0.2*RIGHT, 0.2*DOWN)
        
        
        tanA = MathTex(r"\text{tan} (a)")
        tanA[0][4:5].set_color(RED)
        tanA.scale(0.5)
        tanA.shift(2.25*DOWN, 0.75*LEFT)
        
        tanB = MathTex(r"\text{tan} (b)")
        tanB[0][4:5].set_color(BLUE)
        tanB.scale(0.5)
        tanB.shift(2.25*DOWN, 1.15*RIGHT)
        
        cosA = MathTex(r"\frac{1}{\text{cos} (a)}")
        cosA[0][6:7].set_color(RED)
        cosA.scale(0.5)
        cosA.shift(0.5*UP, 1*LEFT)
        
        cosB = MathTex(r"\frac{1}{\text{cos} (b)}")
        cosB[0][6:7].set_color(BLUE)
        cosB.scale(0.5)
        cosB.shift(0.5*UP, 1.5*RIGHT)
        
        area = MathTex(
            r"\text{Area} = \frac{\text{tan}(a) + \text{tan}(b)}{2}",
            )
        area.scale(0.5)
        area.shift(2.5*UP)
        area[0][0:4].set_color(GOLD) 
        area[0][9:10].set_color(RED)
        area[0][16:17].set_color(BLUE)

        diagram = VGroup(triangle, line, rightA, rightB, angleA, aLabel, angleB, bLabel, length, cosA, cosB, tanA, tanB, area)
        self.add(diagram)
        
        
        
        
        
        ##NEW STUFF
        self.play(diagram.animate.scale(0.5).shift(2*UP))
        
        areaF = MathTex(r"\text{Area of Triangle: } \frac{1}{2} * \text{a} * \text{b} * \text{sin}(C)")
        areaF.color = GREEN
        area1 = MathTex(
            r"\frac{1}{2} * \frac{1}{\text{cos}(a)} * \frac{1}{\text{cos}(b)} * \text{sin}(a+b)",
            )
        area1[0][10:11].set_color(RED)
        area1[0][19:20].set_color(BLUE)
        area1[0][26:27].set_color(RED)
        area1[0][28:29].set_color(BLUE)
        area2 = MathTex(
            r"\text{Area} = \frac{\text{sin} (a+b)}{2 \text{cos} (a) \text{cos} (b)}"
        )
        area2[0][0:4].set_color(GOLD)
        area2[0][9:10].set_color(RED)
        area2[0][11:12].set_color(BLUE)
        area2[0][19:20].set_color(RED)
        area2[0][25:26].set_color(BLUE)
        text = VGroup(areaF, area1, area2)
        text.arrange(DOWN)
        text.shift(0.5*DOWN)
        text.scale(0.5)
        
        self.play(Write(areaF))
        self.play(Write(area1))
        self.play(Write(area2))
        self.wait(1)
        self.play(FadeOut(triangle, line, rightA, rightB, angleA, aLabel, angleB, bLabel, length, cosA, cosB, tanA, tanB, areaF, area1))
        
        self.play(area2.animate.shift(3.75*UP), area.animate.scale(2).shift(0.05*LEFT))
        self.wait(1)
        
        eqArea = MathTex(r"\frac{\text{tan} (a) + \text{tan} (b)}{2} = \frac{\text{sin} (a+b)}{2 \text{cos} (a) \text{cos} (b)}")
        eqArea[0][4:5].set_color(RED)
        eqArea[0][11:12].set_color(BLUE)
        eqArea[0][20:21].set_color(RED)
        eqArea[0][22:23].set_color(BLUE)
        eqArea[0][30:31].set_color(RED)
        eqArea[0][36:37].set_color(BLUE)
        
        nextEq = MathTex(r"\frac{\text{sin} (a)}{\text{cos} (a)} + \frac{\text{sin} (b)}{\text{cos} (b)} = \frac{\text{sin} (a+b)}{\text{cos} (a) \text{cos} (b)}")
        nextEq[0][4:5].set_color(RED)
        nextEq[0][18:19].set_color(BLUE)
        nextEq[0][11:12].set_color(RED)
        nextEq[0][25:26].set_color(BLUE)
        nextEq[0][32:33].set_color(RED)
        nextEq[0][34:35].set_color(BLUE)
        nextEq[0][41:42].set_color(RED)
        nextEq[0][47:48].set_color(BLUE)
        
        finalEq = MathTex(
            r"\text{sin}(a+b) \text{ = } \text{sin}(a) \text{cos}(b) + \text{sin}(b) \text{cos}(a)",
            substrings_to_isolate = "a" + "b"
        )
        finalEq.set_color_by_tex("a", RED)
        finalEq.set_color_by_tex("b", BLUE)
        finalEq.scale(0.9)
        
        text = VGroup(eqArea, nextEq, finalEq)
        text.arrange(DOWN)
        text.scale(0.5)
        text.shift(1.25*UP)
        ##self.add(index_labels(eqArea[0]))
        ##self.add(index_labels(nextEq[0]))
        ##self.add(index_labels(finalEq[0]))
        
        self.play(Write(eqArea))
        self.play(Write(nextEq))
        self.play(Write(finalEq))
        self.wait(1)
        self.play(FadeOut(area, area2,eqArea,nextEq))