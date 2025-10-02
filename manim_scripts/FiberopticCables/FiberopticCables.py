from manim import *

def getDiagram():
    rect1 = Rectangle(width = 3, height = 2, color = DARK_GRAY, fill_opacity = 1, fill_color = DARK_GRAY)
    rect2 = Rectangle(width = 3, height = 1, color = LIGHT_GRAY, fill_opacity = 1, fill_color = LIGHT_GRAY)
    rect3 = Rectangle(width = 3, height = 0.65, fill_opacity = 1, fill_color = RED, color = RED)
    circ = Circle(radius = 3, color = BLACK, fill_color = BLACK, fill_opacity = 1)
    circ.stretch(0.3, dim = 0).shift(2*RIGHT)
    VGroup(rect1, rect2, rect3).shift(0.5*RIGHT, 0.15*UP)
    
    ray1 = Arrow(
        [-2,-1,0], 
        [-1,0,0], 
        stroke_width = 3,
        tip_length = 0.2,
        buff = 0,
        color = YELLOW
    )
    
    dotted_line = DashedLine(
        start=[-2, 0, 0],
        end=[-0.75, 0, 0],
        dash_length=0.05,
        dashed_ratio=0.2,
        color=WHITE,
    )
    
    ray2 = Arrow(
        [-1,0,0],
        [0,0.5,0],
        stroke_width = 3,
        tip_length = 0.2,
        buff = 0,
        color = YELLOW
    )
    
    vert_line = DashedLine(
        start=[0, -0.125, 0],
        end=[0, 0.75, 0],
        dash_length=0.05,
        dashed_ratio=0.2,
        color=WHITE,
    )
    
    ray3 = Arrow(
        [0,0.5,0],
        [1,0,0],
        stroke_width = 3,
        tip_length = 0.2,
        buff = 0,
        color = YELLOW
    )
    
    theta1 = Angle.from_three_points(
        [-2,-1,0],
        [-1,0,0],
        [-2, 0, 0],
        other_angle = True
    )
    label1 = MathTex(r"\theta_1")
    label1.move_to(theta1).scale(0.5).shift(0.2*LEFT, 0.1*DOWN)
    
    theta2 = Angle.from_three_points(
        [-1,0,0],
        [0,0.5,0],
        [0, -0.125, 0],
        other_angle = False
    )
    label2 = MathTex(r"\theta_W")
    label2.move_to(theta2).scale(0.5).shift(0.2*LEFT, 0.1*DOWN)
    
    nlabels = MathTex(r"n_1",r"n_2",r"n_3")
    nlabels.scale(0.5)
    nlabels[0].move_to([-2,1,0])
    nlabels[1].move_to([-1.25,0.35,0])
    nlabels[1].color = RED
    nlabels[2].move_to([-1.25,0.6,0])
    nlabels[2].color = LIGHT_GRAY
    
    return VGroup(rect1, rect2, rect3, circ), ray1, ray2, ray3, dotted_line, VGroup(theta1, label1), vert_line, VGroup(theta2, label2), nlabels

class Preview(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Total Internal Reflection:}", r"\text{An application of Snell's Law}")
        t1.color = PURPLE
        t1.scale(0.5).arrange(DOWN)
        
        t2 = MathTex(r"\text{Total internal reflection allows for light}", r"\text{to travel through a fiber-optic cable.}")
        t3 = MathTex(r"\text{Let } n_1, n_2, n_3 \text{ be the index of refraction of}", r"\text{the air, the red layer, and the gray layer, respectively.}")
        VGroup(t2,t3).scale(0.5)
        VGroup(t2,t3).color = PURPLE
        t2.arrange(DOWN)
        t2.move_to([0,2,0])
        t3.arrange(DOWN)
        t3.move_to([0,-2,0])
        
        background, ray1, ray2, ray3, dLine, theta1, vert_line, theta2, nlabels = getDiagram()
        
        self.play(Write(t1), run_time = 2)
        self.wait(2)
        self.play(FadeOut(t1))
        
        self.play(Write(background))
        self.play(Create(ray1))
        self.play(Create(ray2), Create(dLine), Create(theta1))
        self.play(Create(ray3), Create(vert_line), Create(theta2))
        self.play(Write(nlabels))
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(2)
        
class Proof(Scene):
    def construct(self):
        diagram = VGroup(getDiagram())
        t2 = MathTex(r"\text{Total internal reflection allows for light}", r"\text{to travel through a fiber-optic cable.}")
        t3 = MathTex(r"\text{Let } n_1, n_2, n_3 \text{ be the index of refraction of}", r"\text{the air, the red layer, and the gray layer, respectively.}")
        VGroup(t2,t3).scale(0.5)
        VGroup(t2,t3).color = PURPLE
        t2.arrange(DOWN)
        t2.move_to([0,2,0])
        t3.arrange(DOWN)
        t3.move_to([0,-2,0])
        
        m1 = MathTex(r"\text{Using Snell's Law:}", r"n_1 sin(\theta_1) = n_2 sin(90 - \theta_W)", r"n_1 sin(\theta_1) = n_2 \sqrt{1 - sin^2(\theta_W)}")
        m1.scale(0.5).arrange(DOWN).move_to([0,2.25,0])
        m1.color = PURPLE
        
        m2 = MathTex(r"\text{Using Snell's Law:}", r"\text{In order for reflection, }", r"sin(\theta_W) > \frac{n_3}{n_2}")
        m2.scale(0.5).arrange(DOWN).move_to([0,2.25,0])
        m2.color = PURPLE
        
        m3 = MathTex(r"sin(\theta_1) < \frac{n_2}{n_1}\sqrt{1-\frac{{n_3}^2}{{n_2}^2}")
        m3.scale(0.5).move_to([0,2,0])
        m3.color = PURPLE
        
        m4 = MathTex(r'\text{Since } n_1, \text{the index of refraction}', r"\text{of air, usually equals 1}", r"sin(\theta_1) < \sqrt{{n_2}^2 - {n_3}^2}", r"\text{Light will only travel throughout the wire}", r"\text{when } \theta_1 \text{ satisfies this inequality.}" )
        m4.scale(0.5).arrange(DOWN).move_to([0,2,0])
        m4.color = PURPLE
        
        self.add(diagram, t2, t3)
        self.play(FadeOut(t2))
        self.play(Write(m1), run_time = 3)
        self.wait(2)
        self.play(FadeOut(m1[0:2]), m1[2].animate.move_to([0,3.5,0]))
        self.play(Write(m2), run_time = 3)
        self.wait(2)
        self.play(FadeOut(m2[0:2]), m2[2].animate.move_to([0,2.75,0]))
        self.play(Write(m3))
        self.wait(2)
        self.play(FadeOut(m2[2], m1[2]))
        self.play(diagram.animate.shift(0.5*DOWN), m3.animate.shift(1.5*UP))
        self.play(Write(m4), run_time = 5)
        self.wait(5)
        
        