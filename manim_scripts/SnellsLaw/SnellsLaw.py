from manim import *
from tqdm import tqdm
import pandas as pd

def getDiagram():
    medium2 = Rectangle(
        color = GRAY_E,
        fill_color = GRAY_E,
        height = 3.5,
        width = 2,
        fill_opacity = 1
    )
    medium2.move_to([1,-0.25,0])
    
    a_arrow = Arrow(
        [-1.5,1.5,0],
        [0,0,0],
        stroke_width = 3,
        tip_length = 0.2,
        buff = 0,
        color = YELLOW
    )
    
    surface = Line(
        start=[0, 1.5, 0],
        end=[0, -2, 0],
        color=WHITE
    )
    
    dotted_line = DashedLine(
        start=[-1.5, 0, 0],
        end=[2, 0, 0],
        dash_length=0.05,
        dashed_ratio=0.2,
        color=WHITE,
    )
    
    b_arrow = Arrow(
        [0,0,0],
        [2,-1,0],
        stroke_width = 3,
        tip_length = 0.2,
        buff = 0,
        color = YELLOW
    )
    
    theta1 = Angle.from_three_points(
        [0,1,0],
        [0,0,0],
        [-np.sqrt(2), np.sqrt(2), 0],
        other_angle = False,
        color = RED,
        radius = 0.5
    )
    label1 = MathTex(r"\theta_1")
    label1.color=RED
    label1.scale(0.5).move_to(theta1).shift(0.25*UP+0.1*LEFT)
    
    theta2 = Angle.from_three_points(
        [1,0,0],
        [0,0,0],
        [2*np.sqrt(1/5),-1*np.sqrt(1/5),0],
        other_angle = True,
        color = BLUE,
        radius = 0.5
    ) 
    label2 = MathTex(r"\theta_2")
    label2.color = BLUE
    label2.scale(0.5).move_to(theta2).shift(0.25*RIGHT + 0.05*DOWN)
    
    labeln1 = MathTex(r"\text{Medium 1}", r"\text{Index of Refraction: }n_1", color = RED)
    labeln1.arrange(DOWN)
    labeln2 = MathTex(r"\text{Medium 2}", r"\text{Index of Refraction: }n_2", color = BLUE)
    labeln2.arrange(DOWN)
    VGroup(labeln1, labeln2).scale(0.25)
    labeln1.move_to([-1,-1.5,0])
    labeln2.move_to([1,-1.5,0])
    
    return medium2, a_arrow, surface, dotted_line, b_arrow, VGroup(theta1, label1), VGroup(theta2, label2), labeln1, labeln2

def getLabels():
    linex = DoubleArrow(
        [0.25, 1.5, 0], 
        [0.25, 0, 0], 
        tip_length = 0.1, 
        buff = 0, 
        color = GREEN
    )
    labelx = MathTex(r"x", color = GREEN)
    labelx.scale(0.5).move_to(linex).shift(0.25*RIGHT)
    
    lineD = DoubleArrow(
        [2.25,1.5,0],
        [2.25,-1,0],
        tip_length = 0.1, 
        buff = 0, 
        color = PURPLE
    )
    labelD = MathTex(r"D", color = PURPLE)
    labelD.scale(0.5).move_to(lineD).shift(0.25*RIGHT)
    
    linea = DoubleArrow(
        [-1.5,1.75,0],
        [0,1.75,0],
        tip_length = 0.1, 
        buff = 0, 
        color = RED
    )
    labela = MathTex(r"a", color = RED)
    labela.scale(0.5).move_to(linea).shift(0.25*UP)
    
    lineb = DoubleArrow(
        [0,1.75,0],
        [2,1.75,0],
        tip_length = 0.1, 
        buff = 0, 
        color = BLUE
    )
    labelb = MathTex(r"b", color = BLUE)
    labelb.scale(0.5).move_to(lineb).shift(0.25*UP)
    
    return VGroup(linex, labelx), VGroup(lineD, labelD), VGroup(linea, labela), VGroup(lineb, labelb)

class SnellsLaw(Scene):
    def construct(self):
        medium2, a_arrow, surface, dotted_line, b_arrow, thetalabel1, thetalabel2, labeln1, labeln2 = getDiagram()
        
        diagram = VGroup(medium2, a_arrow, surface, dotted_line, b_arrow, thetalabel1, thetalabel2, labeln1, labeln2)
        
        t1 = MathTex(r"\text{Snell's Law}", r"\text{Part 2(Watch Part 1 First)}")
        t1.scale(0.5)
        t1.arrange(DOWN)
        t1.color = PURPLE
        
        t2 = MathTex(r"\text{This law states that}", r"n_1 sin(\theta_1) = n_2 sin(\theta_2)", r"\text{where } n_i \text{ is the index of refraction for medium } i.")
        t2.scale(0.5)
        t2.arrange(DOWN)
        t2[1][0:2].color = RED
        t2[1][6:8].color = RED
        t2[1][10:12].color = BLUE
        t2[1][16:18].color = BLUE
        
        t3 = MathTex(r"\text{What is an index of refraction?}", r"\text{An index of refraction } n_i \text{ is defined as:}", r"n_i = \frac{c}{v_i}", r"\text{where } c \text{ is the speed of light and } v_i \text{ is}", r"\text{the velocity of light through a medium } i.")
        t3.scale(0.5)
        t3.arrange(DOWN)
        t3.move_to([0,1,0])
        t3.color = PURPLE
        
        self.play(Write(t1))
        self.play(t1.animate.move_to([0,2,0]))
        self.play(FadeIn(medium2), Create(a_arrow), Create(surface), Create(dotted_line))
        self.play(Create(b_arrow))
        self.play(Create(thetalabel1), Create(thetalabel2), Write(labeln1), Write(labeln2))
        self.play(t1.animate.move_to([0,3.5,0]))
        
        t2.move_to(t1).shift(1.15*DOWN)
        self.play(Write(t2))
        
        self.wait(2)
        
        self.play(FadeOut(t1[1], t2[0], diagram))
        self.play(VGroup(t1[0], t2[1], t2[2]).animate.arrange(DOWN).move_to([0,3,0]))
        self.play(Write(t3[0]))
        self.play(Write(t3[1:]), run_time = 4)
        self.wait(3)
        self.play(FadeOut(t3,t1[0], t2[1],t2[2]))
        self.wait(1)
        
class FermatPrinciple(Scene):
    def construct(self):
        diagram = VGroup(getDiagram())
        
        linex, lineD, linea, lineb = getLabels()
        
        t1 = MathTex(r"\text{Fermat's Principle:}", r"\text{Light always travels through}", r"\text{the path of least time.}")
        t1.scale(0.5)
        t1.arrange(DOWN)
        t1.move_to([0,3,0])
        
        t2 = MathTex(r"t = \frac{\sqrt{a^2 + x^2}}{\frac{c}{n_1}} + \frac{\sqrt{b^2 + (d-x)^2}}{\frac{c}{n_2}}")
        t2.scale(0.5)
        t2.move_to([0,3,0])
        
        t3 = MathTex(r"\frac{dt}{dx} = \frac{1}{c}(\frac{n_1(x)}{\sqrt{a^2+x^2}} + \frac{n_2(x-d)}{\sqrt{b^2 + (d-x)^2}})")
        
        t4 = MathTex(r"\frac{dt}{d \theta} \frac{d \theta}{dx} = \frac{1}{c}(n_1 sin(\theta_1) - n_2 sin(\theta_2))")
        
        t5 = MathTex(r"\frac{dt}{d \theta} = 0 \rightarrow 0 = n_1 sin(\theta_1) - n_2 sin(\theta_2)")
        t6 = MathTex(r"n_1 sin(\theta_1) = n_2 sin(\theta_2)")
        t6[0][0:2].color = RED
        t6[0][6:8].color = RED
        t6[0][10:12].color = BLUE
        t6[0][16:18].color = BLUE
        VGroup(t3,t4,t5,t6).scale(0.5).move_to([0,2,0])
        
        self.play(Create(diagram))
        self.play(Create(linex), Create(lineD))
        self.play(Create(linea), Create(lineb))
        self.wait(2)
        
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(t1))
        
        self.play(Write(t2))
        self.play(VGroup(diagram, linex, lineD, linea, lineb).animate.shift(DOWN))
        self.play(Write(t3))
        self.play(FadeOut(t2), t3.animate.move_to(t2))
        self.play(Write(t4))
        self.play(FadeOut(t3), t4.animate.move_to(t3))
        self.play(Write(t5))
        self.play(FadeOut(t4), t5.animate.move_to(t4))
        self.play(Write(t6))
        self.play(FadeOut(t5))
        
        t7 = MathTex(r"\text{Snell's Law}")
        t7.scale(0.5)
        t7.color = PURPLE
        
        self.play(VGroup(t7, t6).animate.arrange(DOWN).move_to([0,2.5,0]), VGroup(diagram, linex, lineD, linea, lineb).animate.shift(UP))
        self.wait(5)
        
        