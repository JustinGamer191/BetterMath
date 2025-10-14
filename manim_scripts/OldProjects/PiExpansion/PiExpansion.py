from manim import *
import math

class CoverScene(Scene):
    def construct(self):
        textQ = Text(
            "Why does"
            )
        textQ.color = BLUE
        textQ.shift(0.75*UP)
        textQ.scale(0.4)
        
        textExp = MathTex(
            r"1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots = \frac{\pi}{4}?",
        )
        ##Color Pi Gold
        ##self.add(index_labels(textExp[0]))
        textExp[0][18:19].set_color(GOLD)
        
        ##Color 1's Red
        textExp[0][0:1].set_color(RED)
        textExp[0][2:3].set_color(RED)
        textExp[0][6:7].set_color(RED)
        textExp[0][10:11].set_color(RED)
        
        ##Color Denominators Blue
        textExp[0][4:5].set_color(BLUE)
        textExp[0][8:9].set_color(BLUE)
        textExp[0][12:13].set_color(BLUE)
        textExp[0][20:21].set_color(BLUE)
        
        textExp.scale(0.5)
        
        self.play(Write(textQ))
        self.play(Write(textExp))
        self.wait(1)
        self.play(FadeOut(textExp), FadeOut(textQ))

class GraphTan(Scene):
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
            return math.atan(x)
        
        tanGraph = axes.plot(
            func,
            x_range = [-xMax,xMax],
            color=BLUE,
        )
        dot = always_redraw(lambda : Dot(color = DARK_BLUE, fill_color = DARK_BLUE).scale(1).move_to(tanGraph.get_end()))
        
        graphLabel = MathTex(r"f(x) = \text{tan}^{-1} (\text{x})")
        graphLabel.scale(0.5)
        graphLabel.color = BLUE
        graphLabel.shift(DOWN)
        bgLabel = BackgroundRectangle(graphLabel, color = BLACK, fill_opacity = 1)
        
        self.play(Create(axes))
        self.add(dot)
        self.play(Create(tanGraph), run_time = 2, rate_func = smooth)
        self.play(FadeOut(dot))
        self.play(Create(bgLabel), Write(graphLabel))
        self.wait(1)
        self.wait(1)
        
        
class Expansion(Scene):
    def construct(self):
        textMS = MathTex(r"\text{Maclaurin Series for } \text{tan}^{-1} (\text{x}):")
        textMS.scale(0.4)
        textMS.shift(0.5*UP)
        
        textExp = MathTex(r"\text{tan}^{-1} (\text{x}) = \text{x} - \frac{1}{3}{\text{x}^3} + \frac{1}{5}{\text{x}^5} - \frac{1}{7}{\text{x}^7} \cdots")
        textExp.scale(0.4)
        
        textG = VGroup(textMS, textExp)
        textLabel = BackgroundRectangle(textG, color = BLACK, fill_opacity = 1)
        
        textMS[0][0:15].set_color(GOLD)
        textMS[0][24:25].set_color(RED)
        
        textExp[0][6:7].set_color(RED)
        textExp[0][9:10].set_color(RED)
        textExp[0][14:15].set_color(RED)
        textExp[0][20:21].set_color(RED)
        textExp[0][26:27].set_color(RED)
        
        self.add(textLabel)
        self.play(Write(textMS))
        self.play(Write(textExp))
        self.play(textG.animate.shift(2.5*UP), rate_func = smooth)
        
        ##SHOW GRAPH
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
            return math.atan(x)
        
        tanGraph = axes.plot(
            func,
            x_range = [-xMax,xMax],
            color=BLUE,
        )
        dot = always_redraw(lambda : Dot(color = DARK_BLUE, fill_color = DARK_BLUE).scale(1).move_to(tanGraph.get_end()))
        
        gLabel = MathTex(r"f(x) = \text{tan}^{-1} (\text{x})")
        gLabel.scale(0.5)
        gLabel.color = BLUE
        gLabel.shift(1.25*DOWN)
        bLabel = BackgroundRectangle(gLabel, color = BLACK, fill_opacity = 1)
        
        gAll = VGroup(axes,tanGraph,bLabel, gLabel)
        gAll.scale(0.9)
        gAll.shift(0.3*DOWN)
        
        self.play(Write(axes))
        self.add(dot)
        self.play(Create(tanGraph), run_time = 2, rate_func = smooth)
        self.play(FadeOut(dot))
        self.play(Create(bLabel), Write(gLabel))
        self.wait(1)
        
        ##First Term
        def func(x):
            return x
        
        newGraph = axes.plot(
            func,
            x_range = [-xMax, xMax],
            color = RED
        )
        
        dot = always_redraw(lambda : Dot(color = RED, fill_color = RED).scale(1).move_to(newGraph.get_end()))
        
        graphLabel = MathTex(r"f(x) = x")
        graphLabel.scale(0.4)
        graphLabel.color = RED
        graphLabel.shift(2*DOWN)
        bgLabel = BackgroundRectangle(graphLabel, color = BLACK, fill_opacity = 1)
        
        self.add(dot)
        self.play(Create(newGraph), run_time = 2, rate_func = smooth)
        self.play(FadeOut(dot))
        self.play(Create(bgLabel), Write(graphLabel))
        
        ##Second Term
        def func(x):
            return x - (1/3)*(x**3)
        rNewGraph = axes.plot(
            func,
            x_range = [-2.55414921, 2.55414921],
            color = RED
        )
        
        rNewLabel = MathTex(r"f(x) = x - \frac{1}{3} x^3")
        rNewLabel.scale(0.4)
        rNewLabel.color = RED
        rNewLabel.shift(2*DOWN)
        
        self.play(Transform(newGraph, rNewGraph))
        self.add(bLabel, gLabel)
        self.play(Create(bgLabel), Transform(graphLabel, rNewLabel))
        
        #Third Term
        def func(x):
            return x - (1/3)*(x**3) + (1/5)*(x**5)
        
        rNewGraph = axes.plot(
            func,
            x_range = [-1.71487692, 1.71487692],
            color = RED
        )
        
        rNewLabel = MathTex(r"f(x) = x - \frac{1}{3} x^3 + \frac{1}{5} x^5")
        rNewLabel.scale(0.4)
        rNewLabel.color = RED
        rNewLabel.shift(2*DOWN)
        
        self.play(Transform(newGraph, rNewGraph))
        self.add(bLabel, gLabel)
        self.play(Create(bgLabel), Transform(graphLabel, rNewLabel))
        
        #Fourth Term
        def func(x):
            return x - (1/3)*(x**3) + (1/5)*(x**5) - (1/7)*(x**7)
        
        rNewGraph = axes.plot(
            func,
            x_range = [-1.70225681, 1.70225681],
            color = RED
        )
        
        rNewLabel = MathTex(r"f(x) = x - \frac{1}{3} x^3 + \frac{1}{5} x^5 - \frac{1}{7} x^7")
        rNewLabel.scale(0.4)
        rNewLabel.color = RED
        rNewLabel.shift(2*DOWN)
        
        self.play(Transform(newGraph, rNewGraph))
        self.add(bLabel, gLabel)
        self.play(Create(bgLabel), Transform(graphLabel, rNewLabel))
        
        ##Final
        def func(x):
            return x - (1/3)*(x**3) + (1/5)*(x**5) - (1/7)*(x**7) + (1/9)*(x**9) - (1/11)*(x**11) + (1/13)*(x**13) - (1/15)*(x**15) + (1/17)*(x**17) - (1/19)*(x**19)
        
        rNewGraph = axes.plot(
            func,
            x_range = [-1.28881, 1.28881],
            color = RED
        )
        
        rNewLabel = MathTex(r"f(x) = x - \frac{1}{3} x^3 + \frac{1}{5} x^5 - \frac{1}{7} x^7 \cdots")
        rNewLabel.scale(0.4)
        rNewLabel.color = RED
        rNewLabel.shift(2*DOWN)
        
        self.play(Transform(newGraph, rNewGraph))
        self.add(bLabel, gLabel)
        self.play(Create(bgLabel), Transform(graphLabel, rNewLabel))
        self.wait(1)
        
class FinalScene(Scene):
    def construct(self):
        textMS = MathTex(r"\text{Maclaurin Series for } \text{tan}^{-1} (\text{x}):")
        textMS.scale(0.4)
        textMS.shift(2*UP)
        
        textExp = MathTex(r"\text{tan}^{-1} (\text{x}) = \text{x} - \frac{1}{3}{\text{x}^3} + \frac{1}{5}{\text{x}^5} - \frac{1}{7}{\text{x}^7} \cdots")
        textExp.scale(0.4)
        textExp.shift(1.25*UP)
        
        textSub = MathTex(r"\text{tan}^{-1} (1) = 1 - \frac{1}{3}{1^5} + \frac{1}{5}{1^5} - \frac{1}{7}{1^7} \cdots")
        textSub.scale(0.4)
        textSub.shift(0.5*UP)
        
        textRep = MathTex(r"\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} \cdots")
        textRep.scale(0.4)
        textRep.shift(0.5*UP)
        
        ##Coloring
        textMS[0][0:15].set_color(GOLD)
        
        textExp[0][6:7].set_color(RED)
        textExp[0][9:10].set_color(RED)
        textExp[0][14:15].set_color(RED)
        textExp[0][20:21].set_color(RED)
        textExp[0][26:27].set_color(RED)
        
        textSub[0][6:7].set_color(RED)
        textSub[0][9:10].set_color(RED)
        textSub[0][14:15].set_color(RED)
        textSub[0][20:21].set_color(RED)
        textSub[0][26:27].set_color(RED)
        
        textRep[0][0:3].set_color(GOLD)
        textRep[0][4:5].set_color(RED)
        textRep[0][6:7].set_color(RED)
        textRep[0][10:11].set_color(RED)
        textRep[0][14:15].set_color(RED)
        
        textRep[0][8:9].set_color(BLUE)
        textRep[0][12:14].set_color(BLUE)
        textRep[0][16:17].set_color(BLUE)
        
        ##self.add(index_labels(textRep[0]))
        self.play(Write(textMS))
        self.play(Write(textExp))
        self.play(Write(textSub))
        self.wait(1)
        self.play(Transform(textSub, textRep))
        self.wait(1)
        self.play(FadeOut(textMS, textExp, textSub, textRep))