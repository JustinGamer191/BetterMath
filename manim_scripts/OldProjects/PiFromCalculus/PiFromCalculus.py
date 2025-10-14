from manim import *
import math
class StartScene(Scene):
    def construct(self):
        textTop = MathTex(r"\text{How to derive}")
        textTop.color = BLUE
        
        textMid = MathTex(r"\pi")
        textMid.scale(1.5)
        textMid.color = GOLD
        
        textLow = MathTex(r"\text{using calculus.}")
        textLow.color = BLUE
        
        text = VGroup(textTop, textMid, textLow)
        text.scale(0.75)
        text.arrange(DOWN)
        
        self.add(text)
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)

class DrawCircle(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        
        textC = MathTex(r"\text{Circumference of Circle = C}")
        textC.color = RED
        textC.scale(0.5)
        textC.shift(1.5*UP)
        self.play(Write(textC))
        
        
        line = Line()
        line.color = BLUE
        self.play(Create(line))
        
        textD = MathTex(r"\text{Diameter of Circle = D}")
        textD.color = BLUE
        textD.scale(0.5)
        textD.shift(1.5*DOWN)
        self.play(Write(textD))
        self.wait(1)
        
        groupAll = VGroup(circle, textC, line, textD)
        self.play(groupAll.animate.scale(0.5).shift(2*UP))
        
        textPi = MathTex(r"\pi = \frac{C}{D} \text{ (By Definition)} ")
        textPi.scale(0.5)
        
        ##self.add(index_labels(textPi[0]))
        textPi[0][0:1].set_color(GOLD)
        textPi[0][2:3].set_color(RED)
        textPi[0][4:5].set_color(BLUE)
        
        self.play(Write(textPi))
        self.wait(1)
        self.play(FadeOut(groupAll, textPi))
        

class GraphScene(Scene):
    def construct(self):
        xMax = 3
        yMax = 5
        axes = Axes(
            x_range = [-xMax, xMax, 1],
            y_range = [-yMax, yMax, 1],
            x_length = 3,
            y_length = 5,
            tips = False
        )
        
        def func(x):
            return (1-x**2)**0.5
        
        exp_graph = axes.plot(
            func,
            x_range = [-1,1],
            color=RED,
        )
        
        label = MathTex(r"f(x) = \sqrt{1 - x^2}")
        label.scale(0.5)
        label.shift(0.8*UP, 1.1*RIGHT)
        label.color = RED
        
        self.play(Create(axes))
        self.play(Create(exp_graph))
        self.play(Write(label))
        self.wait(1)
        
class ExplainScene(Scene):
    def construct(self):
        arcLength = MathTex(r"\text{Arc Length Formula:}")
        intArc = MathTex(r"\int_{a}^{b} \sqrt{1+f'(x)}\,dx")
        intArc.color = RED
        
        totalText = VGroup(arcLength, intArc)
        totalText.scale(0.5)
        totalText.arrange(DOWN)
        totalText.shift(1*UP)
        
        self.play(Write(totalText))
        self.wait(1)
        
        textPi = MathTex(r"\pi = \frac{C}{D}")
        textPi.scale(0.5)
        textPi[0][0:1].set_color(GOLD)
        textPi[0][2:3].set_color(RED)
        textPi[0][4:5].set_color(BLUE)
        
        textPiNew = MathTex(r"\pi = \frac{C}{D} = \frac{\int_{a}^{b} \sqrt{1+f'(x)}\,dx}{D}")
        textPiNew.scale(0.5)
        textPiNew[0][0:1].set_color(GOLD)
        textPiNew[0][2:3].set_color(RED)
        textPiNew[0][4:5].set_color(BLUE)
        textPiNew[0][6:20].set_color(RED)
        textPiNew[0][21:22].set_color(BLUE)
        
        self.play(Write(textPi))
        self.wait(0.5)
        self.play(Transform(textPi, textPiNew))
        self.wait(1)
        
        
        
class CalcScene(Scene):
    def construct(self):
        findArcTop = MathTex(r"\text{To Find } \pi:")
        findArcTop[0][6:7].set_color(GOLD)
        
        findArcBot = MathTex(r"f(x) = \sqrt{1-x^2}")
        findArcBot.color = BLUE
        
        intDeriv = MathTex(r"f'(x) = - \frac{x}{\sqrt{1-x^2}}")
        intDeriv.color = BLUE
        
        intText = MathTex(r"\pi = \frac{2 \int_{-1}^{1} \sqrt{1+f'(x)^2}\,dx}{2}")
        intText[0][0:1].set_color(GOLD)
        intText[0][3:11].set_color(RED)
        intText[0][11:17].set_color(BLUE)
        intText[0][17:19].set_color(RED)
        intText[0][20:21].set_color(BLUE)
        
        intTextNew = MathTex(r"\pi = \int_{-1}^{1} \sqrt{1+\frac{x^2}{1-x^2}} \,dx")
        intTextNew[0][0:1].set_color(GOLD)
        intTextNew[0][2:20].set_color(RED)
        intTextNew[0][21:22].set_color(BLUE)
        
        pi = MathTex("= 3.141592653589...")
        pi.color = GOLD
        
        intGroup = VGroup(intText, intTextNew)
        
        piGroup = VGroup(findArcTop, findArcBot, intDeriv, intGroup, pi)
        piGroup.arrange(DOWN)
        piGroup.scale(0.5)
        
        self.play(Write(findArcTop))
        self.play(Write(findArcBot))
        self.play(Write(intDeriv))
        self.play(Write(intText))
        self.wait(1)
        self.play(Transform(intText, intTextNew))
        self.wait(1)
        self.play(Write(pi))
        self.wait(1)
        
        
        
        
        