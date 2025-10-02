from manim import *

class Intro(Scene):
    def construct(self):
        t1 = MathTex(r"\text{King's Property of Integration}", r"\int_{a}^{b}f(x)dx = \int_{a}^{b}f(a+b-x)dx", r"\text{(and correcting mistakes made in prior video.)}")
        t1.scale(0.5).arrange(DOWN)
        t1[0].color = GOLD
        t1[1].color = PURPLE
        t1[2].color = GOLD
        
        t2 = MathTex(
            r"\text{First, the proof:}", 
            r"\text{Let } u = a + b - x, du = -dx", 
            r"\text{When } x = a \rightarrow u = b, \text{when } x = b \rightarrow u = a", 
            r"\int_{a}^{b} f(a+b-x)dx = \int_{b}^{a} f(u) (-du)", 
            r"= \int_{a}^{b} f(u) du = \int_{a}^{b} f(x) dx"
        )
        t2.scale(0.5).arrange(DOWN)
        t2[0].color = GOLD
        t2[1:5].color = PURPLE
        
        t3 = MathTex(
            r"\text{Next, the applications:}"
        )
        t3.scale(0.5).move_to([0,1.5,0])
        t3.color = GOLD
        
        axes = Axes(
            x_range=[1, 4, 1],
            y_range=[0, 64, 16],
            x_length=2,
            y_length=3,
            tips = False
        )
        
        graph1 = axes.plot(lambda x: x**3, x_range = [1,4], color=RED)
        label1 = MathTex(r"\int_{1}^{4} x^3 dx", color = RED)
        label1.move_to([2,-1,0]).scale(0.5)
        
        graph2 = axes.plot(lambda x: (5-x)**3, x_range = [1,4], color = BLUE)
        label2 = MathTex(r"\int_{1}^{4} (5-x)^3 dx", color = BLUE)
        label2.move_to([-2,-1,0]).scale(0.5)
        
        VGroup(axes, graph1, graph2).shift(0.5*DOWN)
        
        area1 = axes.get_area(graph1, x_range=[1, 4], color=RED, opacity=0.3)
        area2 = axes.get_area(graph2, x_range=[1, 4], color=BLUE, opacity=0.3)
        
        t4 = MathTex(r"\text{They are both equal to }", r"\frac{255}{4}.")
        t4.scale(0.5).arrange(DOWN)
        t4.color = PURPLE
        
        self.play(Write(t1), run_time = 3)
        self.wait(2)
        self.play(FadeOut(t1[0], t1[2]), t1[1].animate.move_to([0,2,0]))
        self.play(Write(t2), run_time = 5)
        self.wait(5)
        self.play(FadeOut(t2))
        self.play(Write(t3))
        self.play(Create(axes), Create(VGroup(graph1, area1, label1)), Create(VGroup(graph2, area2, label2)))
        self.wait(3)
        self.play(FadeOut(VGroup(axes, graph1, graph2, area1, area2, t3, t1[1])), VGroup(label1, label2).animate.arrange(DOWN).move_to([0,2,0]))
        self.play(Write(t4))
        self.wait(2)