from manim import *
from tqdm import tqdm
import pandas as pd

def getDiagram():
    ray1 = Arrow(
        [-2 * np.sqrt(2), np.sqrt(2), 0],
        [0, 0, 0],
        stroke_width=3,
        tip_length=0.2,
        buff=0,
    )
    ray1.color = YELLOW

    surface1 = Line([-2 * np.sqrt(2), 0, 0], [2 * np.sqrt(2), 0, 0])

    ray2 = Arrow(
        [0, 0, 0],
        [2 * np.sqrt(2), np.sqrt(2), 0],
        stroke_width=3,
        tip_length=0.2,
        buff=0,
    )
    ray2.color = YELLOW

    dotted_line = DashedLine(
        start=[0, 1.5, 0],
        end=[0, -1.5, 0],
        dash_length=0.05,
        dashed_ratio=0.2,
        color=WHITE,
    )

    anglei = Angle.from_three_points(
        [-2 * np.sqrt(2), np.sqrt(2), 0],
        [0, 0, 0],
        [0, 1.5, 0],
        other_angle=True,
        color=RED,
    )
    angler = Angle.from_three_points(
        [0, 1.5, 0],
        [0, 0, 0],
        [2 * np.sqrt(2), np.sqrt(2), 0],
        other_angle=True,
        color=BLUE,
    )
    labeli = MathTex(r"i")
    labeli.color = RED
    labeli.move_to(anglei).shift(0.25 * UP + 0.25 * LEFT)

    labelr = MathTex(r"r")
    labelr.color = BLUE
    labelr.move_to(angler).shift(0.25 * UP + 0.25 * RIGHT)
    
    VGroup(labeli, labelr).scale(0.5)
    
    return ray1, surface1, ray2, dotted_line, anglei, angler, labeli, labelr

def getLabels():
    lineh1 = Line([-1*np.sqrt(2), 0, 0], [-1*np.sqrt(2), np.sqrt(2)/2, 0], color = RED)
    lineh2 = Line([np.sqrt(2)/2, 0, 0], [np.sqrt(2)/2, np.sqrt(2)/4, 0], color = BLUE)
    lineL = DoubleArrow([-1*np.sqrt(2), -0.25, 0], [np.sqrt(2)/2, -0.25, 0], tip_length = 0.1, buff = 0, color = PURPLE)
    linex = DoubleArrow([-1*np.sqrt(2), -0.25, 0], [0,-0.25,0], tip_length = 0.1, buff = 0, color = RED)
    linelx = DoubleArrow([0,-0.25,0], [np.sqrt(2)/2, -0.25, 0], tip_length = 0.1, buff = 0, color = BLUE)
    
    labelh1 = MathTex(r"h_1")
    labelh1.move_to(lineh1).shift(0.25*LEFT)
    labelh1.scale(0.5)
    labelh1.color = RED
    
    labelh2 = MathTex(r"h_2")
    labelh2.move_to(lineh2).shift(0.25*RIGHT)
    labelh2.scale(0.5)
    labelh2.color = BLUE
    
    labelL = MathTex(r"l")
    labelL.move_to(lineL).shift(0.25*DOWN)
    labelL.color = PURPLE
    
    labelx = MathTex(r"x")
    labelx.move_to(linex).shift(0.25*DOWN)
    labelx.color = RED
    labelx.scale(0.5)
    
    labellx = MathTex(r"l-x")
    labellx.move_to(linelx).shift(0.25*DOWN)
    labellx.color = BLUE
    labellx.scale(0.5)
    
    VGroup(lineL, labelL).shift(0.5*DOWN)
    
    return lineh1, lineh2, labelh1, labelh2, lineL, labelL, VGroup(linex, labelx), VGroup(linelx, labellx)

class LawOfReflection(Scene):
    def construct(self):
        ray1, surface1, ray2, dotted_line, anglei, angler, labeli, labelr = getDiagram()
        t1 = MathTex(r"\text{Law of Reflection}", r"\text{Part 1}")
        t1.scale(0.5)
        t1.arrange(DOWN)
        t1.color = YELLOW

        t2 = MathTex(
            r"\text{The law states that }",
            r"\angle i= \angle r",
            r"\text{when light reflects off a surface.}",
        )
        t2.scale(0.5)
        t2.arrange(DOWN)
        t2.move_to([0, -1, 0])
        t2[1][1].color = RED
        t2[1][4].color = BLUE
        bg2 = BackgroundRectangle(t2, fill_opacity=1)

        self.play(Write(t1))
        self.wait(1)

        self.play(t1.animate.move_to([0, 2, 0]))
        self.play(Create(ray1), Create(surface1), Create(dotted_line))
        self.play(Create(ray2))

        self.play(Create(anglei), Create(angler))
        self.play(Write(labeli), Write(labelr))

        self.add(bg2)
        self.play(Write(t2))

        self.wait(2)
        self.remove(bg2)
        self.play(FadeOut(t2,t1))
        self.wait(1)

class FermatPrinciple(Scene):
    def construct(self):
        diagram = VGroup(getDiagram())
        self.add(diagram)
        
        lineh1, lineh2, labelh1, labelh2, lineL, labelL, linelabelx, linelabellx = getLabels()
        VGroup(lineL, labelL).shift(0.5*UP)
        
        t1 = MathTex(r"\text{Fermat's Principle:}", r"\text{Light always travels through}", r"\text{the path of least time.}")
        t1.scale(0.5)
        t1.arrange(DOWN)
        t1.move_to([0,2.75,0])
        
        self.play(Write(t1))
        self.wait(1)
        
        self.play(Create(lineh1), Create(labelh1))
        self.play(Create(lineh2), Create(labelh2))
        self.play(Create(lineL), Create(labelL))
        self.play(VGroup(lineL, labelL).animate.shift(0.5*DOWN))
        self.play(Create(linelabelx))
        self.play(Create(linelabellx))
        self.play(FadeOut(t1))
        self.wait(1)
        
class Proof(Scene):
    def construct(self):
        diagram = VGroup(getDiagram(), getLabels())
        self.add(diagram)
        
        m1 = MathTex(r"\frac{\sqrt{x^2 + {h_1}^2} + \sqrt{(l-x)^2 + {h_2}^2}}{c} = t", r"\text{where c is the speed of light,}", r"\text{t is the time light takes to travel a distance D.}")
        m1.scale(0.5)
        m1.arrange(DOWN)
        
        m2 = MathTex(r"\frac{dt}{dx} = \frac{1}{c} (\frac{x}{\sqrt{x^2 + {h_1}^2}} + \frac{x-l}{\sqrt{(x-l)^2 + {h_2}^2}}})")
        m2.scale(0.5)
        VGroup(m1[0], m2).arrange(DOWN)
        
        h1 = MathTex(r"sin(i) = \frac{x}{\sqrt{x^2 + {h_1}^2}},", r"sin(r) = \frac{l-x}{\sqrt{(x-l)^2 + {h_1}^2}}")
        h1.scale(0.5)
        
        m3 = MathTex(r"\frac{dt}{d \theta} \frac{d \theta}{dx} = \frac{1}{c} (sin(i) - sin(r))")
        m3.scale(0.5)
        m3.arrange(DOWN)
        
        m4 = MathTex(r"\frac{dt}{d \theta} \text{ is equal to 0 at minimum time travelled}")
        m4.scale(0.5)
        
        m5 = MathTex(r"0 = sin(i) - sin(r)", r"sin(i) = sin(r)", r"i = r")
        m5[0][6].color = RED
        m5[1][4].color = RED
        m5[2][0].color = RED
        m5[0][13].color = BLUE
        m5[1][11].color = BLUE
        m5[2][2].color = BLUE
        m5.scale(0.5)
        m5.arrange(DOWN)
        
        self.play(diagram.animate.move_to([0,2.5,0]).scale(0.75))
        self.play(Write(m1))
        self.wait(2)
        
        self.play(FadeOut(m1[1:]))
        self.play(Write(m2))
        self.wait(2)
        
        self.play(FadeOut(m1[0]))
        self.play(m2.animate.move_to(m1[0]))
        self.wait(2)
        
        VGroup(m2, h1).arrange(DOWN)
        self.play(Write(h1))
        self.wait(2)
        
        self.play(FadeOut(h1))
        
        m3.move_to(h1)
        self.play(Write(m3))
        self.wait(2)
        
        self.play(FadeOut(m2))
        self.play(m3.animate.move_to(m2))
        
        VGroup(m3, m4).arrange(DOWN)
        
        self.play(Write(m4))
        self.wait(2)
        
        m5.move_to([0,-0.75,0])
        
        self.play(FadeOut(m4))
        self.play(Write(m5))
        self.wait(2)
        self.play(FadeOut(m3, m5[0], m5[1]))
        self.play(diagram.animate.move_to([0,0,0]).scale(1/0.75), m5[2].animate.move_to([0,2,0]))
        self.wait(1)
        
        t1 = MathTex(r"\text{Law of Reflection}")
        t1.scale(0.5)
        t1.color = YELLOW
        t1.move_to([0,2.5,0])
        
        self.play(Write(t1))
        self.wait(5) 

