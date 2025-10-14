from manim import*
import math

class Cover(Scene):
    def construct(self):
        textProof = MathTex(r"\text{Proving: Arc Length Formula}")
        textProof.color = GOLD
        
        textMath = MathTex(
            r"L = \int_a^b \sqrt{1+f'(x)} \text{ } dx",
            substrings_to_isolate = "a" + "b"
            )
        textMath.set_color_by_tex("a", RED)
        textMath.set_color_by_tex("b", BLUE)
        
        text = VGroup(textProof, textMath)
        text.scale(0.5)
        text.arrange(DOWN)
        
        self.play(Write(textProof))
        self.play(Write(textMath))
        self.play(FadeOut(text))

class Second(Scene):
    def construct(self):
        pA = np.array([-math.sqrt(2), math.sqrt(2), 0])
        pB = np.array([-math.sqrt(2), -math.sqrt(2), 0])
        pC = np.array([math.sqrt(2), -math.sqrt(2), 0])
        
        triangle = Polygon(pA, pB, pC)
        triangle.color = GOLD
        
        labelA = MathTex(r"a")
        labelA.color = RED
        labelA.move_to([-2.5, 0.35, 0])
        labelB = MathTex(r"b")
        labelB.color = BLUE
        labelB.move_to([0.35,-2.5,0])
        labelC = MathTex(r"c")
        labelC.color = GREEN
        labelC.move_to([1,1,0])
        
        labels = VGroup(labelA, labelB, labelC)
        labels.scale(0.5)
        
        pyText = MathTex(r"\text{Pythagorean Theorem:}")
        pyForm = MathTex(r"c = \sqrt{a^2 + b^2}")
        pyForm[0][0:1].color = GREEN
        pyForm[0][4:5].color = RED
        pyForm[0][7:8].color = BLUE
        
        py = VGroup(pyText, pyForm)
        py.scale(0.5)
        py.arrange(DOWN)
        py.move_to([0,2,0])
        
        self.play(Create(triangle))
        self.play(Write(labels))
        self.wait(1)
        self.play(Write(pyText))
        self.play(Write(pyForm))
        self.play(FadeOut(triangle, labels))
        self.play(py.animate.move_to([0,2.5,0]))
        self.wait(1)
class Third(Scene):
    def construct(self):
        axes = Axes(
            x_range = [0, 3.15, 0.63],
            y_range = [0, 2, 0.4],
            x_length = 3,
            y_length = 5,
            tips = False
        )
        
        def func(x):
            return math.sin(x)
        
        sinG = axes.plot(
            func,
            x_range = [0, 3.14],
            color = GOLD
        )
        
        gLabelText = MathTex(r"\text{f(x) = sin(x)}")
        gLabelText.scale(0.5)
        gLabelText.color = GOLD
        gLabelText.move_to([0,-1,0])
        labelBack = BackgroundRectangle(gLabelText, color = BLACK, fill_opacity = 1)
        
        gLabel = VGroup(labelBack, gLabelText)
        
        pyText = MathTex(r"\text{Pythagorean Theorem:}")
        pyForm = MathTex(r"c = \sqrt{a^2 + b^2}")
        pyForm[0][0:1].color = GREEN
        pyForm[0][4:5].color = RED
        pyForm[0][7:8].color = BLUE
        
        py = VGroup(pyText, pyForm)
        py.scale(0.5)
        py.arrange(DOWN)
        py.move_to([0,2.5,0])
        
        def hori(x):
            return math.sin(0)
        
        horiLine = axes.plot(
            hori,
            x_range = [0,0.25],
            color = RED
        )
        point = axes.c2p(0.25, 0.2474)
        vertLine = axes.get_vertical_line(point, line_func = Line)
        vertLine.color = BLUE
        
        horiL = MathTex("dx")
        horiL.color = RED
        horiL.scale(0.5)
        horiL.next_to(horiLine, DOWN)
        horiL.shift(0.15*UP)
        vertL = MathTex("dy")
        vertL.color = BLUE
        vertL.scale(0.5)
        vertL.next_to(vertLine, RIGHT)
        vertL.shift(0.15*LEFT)
        
        coverRectA = Rectangle(width = 4, height = 5)
        coverRectA.color = BLACK
        coverRectA.set_fill(BLACK, 1)
        coverRectA.shift(UP)
        
        coverRectB = Rectangle(width = 3.5, height = 2)
        coverRectB.color = BLACK
        coverRectB.set_fill(BLACK, 1)
        coverRectB.shift(1.5*RIGHT, 1.6*DOWN)
        
        
        afterFade = VGroup(py, axes, sinG, gLabel, horiLine, vertLine, horiL, vertL, coverRectA, coverRectB)
        
        arcS = MathTex(r"\text{Arc Length of Small Piece:}")
        arcS.color = GOLD
        arcE = MathTex(r"L = \sqrt{dx^2 + dy^2}")
        arcE[0][4:6].color = RED
        arcE[0][8:10].color = BLUE
        
        arcSmall = VGroup(arcS, arcE)
        arcSmall.scale(0.5)
        arcSmall.arrange(DOWN)
        arcSmall.move_to([0,1.5,0])
        
        rectFinal = Rectangle(width = 1.55, height = 1.5)
        rectFinal.color = BLACK
        rectFinal.set_fill(BLACK, 1)
        
        self.add(py)
        self.play(Create(axes))
        self.play(Create(sinG))
        self.play(Write(gLabel))
        self.play(gLabel.animate.move_to([0,1,0]))
        self.play(Create(horiLine))
        self.play(Create(vertLine))
        self.play(Write(horiL), Write(vertL))
        self.wait(1)
        self.play(FadeIn(coverRectA, coverRectB))
        self.wait(1)
        self.play(afterFade.animate.shift(2*UP, 1*RIGHT))
        self.wait(1)
        self.play(Write(arcS))
        self.play(Write(arcE))
        self.play(FadeIn(rectFinal))
        self.wait(1)

class Fourth(Scene):
    def construct(self):
        arcS = MathTex(r"\text{Arc Length of Small Piece:}")
        arcS.color = GOLD
        arcE = MathTex(r"L = \sqrt{dx^2 + dy^2}")
        arcE[0][4:6].color = RED
        arcE[0][8:10].color = BLUE
        
        arcSmall = VGroup(arcS, arcE)
        arcSmall.scale(0.5)
        arcSmall.arrange(DOWN)
        arcSmall.move_to([0,1.5,0])
        
        intText = MathTex(r"\text{Integration: Infinite Addition of Small Pieces}")
        intText.color = GOLD
        intText.scale(0.75)
        intForm = MathTex(r"\int_a^b \sqrt{dx^2 + dy^2}")
        intForm[0][5:7].color = RED
        intForm[0][9:11].color = BLUE
        intFormFinal = MathTex(r"\int_a^b \sqrt{1+(\frac{dy}{dx})^2} \text{ } dx")
        intFormFinal[0][11:13].color = RED
        intFormFinal[0][8:10].color = BLUE
        intFormFinal[0][15:18].color = RED
        intFFF = MathTex(r"\int_a^b \sqrt{1 + (f'(x))^2} \text{ } dx")
        intFFF[0][15:18].color = RED
        
        intAll = VGroup(intText, intForm, intFormFinal, intFFF)
        intAll.scale(0.5)
        intAll.arrange(DOWN)
        intAll.shift(0.5*DOWN)
        
        self.add(arcSmall)
        self.play(Write(intText))
        self.play(Write(intForm))
        self.play(Write(intFormFinal))
        self.play(Write(intFFF))
        self.wait(1)
        self.play(FadeOut(intText, intForm, intFormFinal, arcSmall))
        self.play(intFFF.animate.move_to([0,0,0]))
        self.play(Circumscribe(intFFF, color = GOLD))