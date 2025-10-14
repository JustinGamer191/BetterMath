from manim import *
import math

class Cover(Scene):
    def construct(self):
        textAll = MathTex(r"\text{Common Math Identites}")
        textAll.scale(0.5)
        textAll.color = GOLD
        
        self.play(Write(textAll))
        self.play(textAll.animate.shift(2.5*UP))
        
        
        
        textCubes = MathTex(
            r"(a+b)^3 = a^3 + b^3",
            substrings_to_isolate = "a" + "b" + "3"
            )
        textCubes.set_color_by_tex("a", RED)
        textCubes.set_color_by_tex("b", BLUE)
        textCubes.set_color_by_tex("3", GOLD)
        textCubes.scale(0.5)
        
        bCube = SurroundingRectangle(textCubes, color = GOLD, buff = MED_LARGE_BUFF)
        
        self.play(Write(textCubes[0:6].shift(0.55*RIGHT)))
        self.wait(0.5)
        self.play(textCubes[0:6].animate.shift(0.55*LEFT))
        self.play(Write(textCubes[6:15]))
        self.play(Write(bCube))
        self.play(Unwrite(bCube))
        self.play(textCubes.animate.shift(2*UP))
        self.wait(1)
        
        
        
        textLogs = MathTex(
            r" {{\text{ln} (a) \text{ln} (b) }} {{= \text{ln} (a+b)}}",
            substrings_to_isolate = "a" + "b"
            )
        textLogs.set_color_by_tex("a", RED)
        textLogs.set_color_by_tex("b", BLUE)
        textLogs.scale(0.5)
        bLogs = SurroundingRectangle(textLogs, color = RED, buff = MED_LARGE_BUFF)
        
        self.play(Write(textLogs[0:6].shift(0.55*RIGHT)))
        self.wait(0.5)
        self.play(textLogs[0:6].animate.shift(0.55*LEFT))
        self.play(Write(textLogs[6:13]))
        self.play(Write(bLogs))
        self.play(Unwrite(bLogs))
        self.play(textLogs.animate.shift(1.5*UP))
        self.wait(1)
        
class Second(Scene):
    def construct(self):
        textAll = MathTex(r"\text{Common Math Identites}")
        textAll.scale(0.5)
        textAll.color = GOLD
        textAll.shift(2.5*UP)
        
        textCubes = MathTex(
            r"(a+b)^3 = a^3 + b^3",
            substrings_to_isolate = "a" + "b" + "3"
            )
        textCubes.set_color_by_tex("a", RED)
        textCubes.set_color_by_tex("b", BLUE)
        textCubes.set_color_by_tex("3", GOLD)
        textCubes.scale(0.5)
        textCubes.shift(2*UP)
        
        
        textLogs = MathTex(
            r" {{\text{ln} (a) \text{ln} (b) }} {{= \text{ln} (a+b)}}",
            substrings_to_isolate = "a" + "b"
            )
        textLogs.set_color_by_tex("a", RED)
        textLogs.set_color_by_tex("b", BLUE)
        textLogs.scale(0.5)
        textLogs.shift(1.5*UP)
        
        self.add(textAll, textCubes, textLogs)
        
        textLim = MathTex(
            r"{{\lim_{x\to\infty} (1 + \frac{1}{x})^x}} = 1"
        )
        textLim.scale(0.5)
        textLim[0][3:4].color = BLUE
        textLim[0][11:12].color = BLUE
        textLim[0][13:14].color = BLUE
        textLim[0][7:8].color = RED
        textLim[0][9:10].color = RED
        textLim[1][1:2].color = RED
        ##self.add(index_labels(textLim[0]))
        
        bLim = SurroundingRectangle(textLim, color = BLUE, buff = MED_LARGE_BUFF)
        
        self.play(Write(textLim[0:1].shift(0.2*RIGHT)))
        self.wait(0.5)
        self.play(textLim[0:1].animate.shift(0.2*LEFT))
        self.play(Write(textLim[1:3]))
        self.play(Write(bLim))
        self.play(Unwrite(bLim))
        self.play(textLim.animate.shift(UP))
        self.wait(1)
        
        textTan = MathTex(
            r"{{\text{cos} (a+b)}} = \text{cos} (a) + \text{cos} (b)",
            substrings_to_isolate = "a" + "b"
        )
        textTan.set_color_by_tex("a", RED)
        textTan.set_color_by_tex("b", BLUE)
        textTan.scale(0.5)
        
        bTan = SurroundingRectangle(textTan, color = WHITE, buff = MED_LARGE_BUFF)
        
        self.play(Write(textTan[0:5].shift(0.55*RIGHT)))
        self.wait(0.5)
        self.play(textTan[0:5].animate.shift(0.55*LEFT))
        self.play(Write(textTan[5:10]))
        self.play(Write(bTan))
        self.play(Unwrite(bTan))
        self.play(textTan.animate.shift(0.5*UP))
        self.wait(1)
        
        allStuff = VGroup(textAll, textCubes, textLogs, textLim, textTan)
        self.play(allStuff.animate.shift(1.5*DOWN))
        
        bAll = SurroundingRectangle(allStuff, color = GOLD, buff = MED_LARGE_BUFF)
        self.play(Write(bAll))
        self.wait(1)