from manim import *

class Scene1(Scene):
    def construct(self):
        t1 = MathTex(r"\text{A Connection Between}")
        t1.color = GOLD_A
        t2 = MathTex(r"\text{Probability}")
        t2.color = RED_A
        t3 = MathTex(r"\text{and}")
        t3.color = GOLD_A
        t4 = MathTex(r"\text{Geometry}")
        t4.color = BLUE_A
        
        tAll = VGroup(t1,t2,t3,t4)
        tAll.scale(0.5)
        tAll.arrange(DOWN)
        
        self.play(Write(tAll), run_time = 4)
        self.play(FadeOut(tAll))
        self.wait(1)

class Scene2(Scene):
    def construct(self):
        #First Slide of Text
        t1 = MathTex(r"\text{Example Problem:}")
        t1.color = GOLD_A
        t2 = MathTex(r"\text{Adam and Bill both choose a number between 0 and 1}")
        t2[0][0:4].color = BLUE_A
        t2[0][4:7].color = GOLD_A
        t2[0][7:11].color = BLUE_A
        t2[0][11:35].color = GOLD_A
        t2[0][35:36].color = BLUE_A
        t2[0][36:39].color = GOLD_A
        t2[0][39:40].color = BLUE_A
        t2.scale(0.75)
        t3 = MathTex(r"\text{What is the probability that Adam's plus Bill's number}")
        t3[0][0:25].color = GOLD_A
        t3[0][24:30].color = BLUE_A
        t3[0][31:35].color = GOLD_A
        t3[0][34:40].color = BLUE_A
        t3[0][41:46].color = GOLD_A
        t3.scale(0.75)
        t4 = MathTex(r"\text{is less than 0.75?}")
        t4.color = GOLD_A
        t4.scale(0.75)
        
        tAll = VGroup(t1,t2,t3,t4)
        tAll.scale(0.4)
        tAll.arrange(DOWN)
        
        self.play(Write(tAll), run_time = 4)
        self.wait(1)
        self.play(tAll.animate.move_to([0,2,0]))
        self.wait(1)
        
class Scene3(Scene):
    def construct(self):
        o1 = MathTex(r"\text{Example Problem:}")
        o1.color = GOLD_A
        o2 = MathTex(r"\text{Adam and Bill both choose a number between 0 and 1}")
        o2[0][0:4].color = BLUE_A
        o2[0][4:7].color = GOLD_A
        o2[0][7:11].color = BLUE_A
        o2[0][11:35].color = GOLD_A
        o2[0][35:36].color = BLUE_A
        o2[0][36:39].color = GOLD_A
        o2[0][39:40].color = BLUE_A
        o2.scale(0.75)
        o3 = MathTex(r"\text{What is the probability that Adam's plus Bill's number}")
        o3[0][0:25].color = GOLD_A
        o3[0][24:30].color = BLUE_A
        o3[0][31:35].color = GOLD_A
        o3[0][34:40].color = BLUE_A
        o3[0][41:46].color = GOLD_A
        o3.scale(0.75)
        o4 = MathTex(r"\text{is less than 0.75?}")
        o4.color = GOLD_A
        o4.scale(0.75)
        
        oAll = VGroup(o1,o2,o3,o4)
        oAll.scale(0.4)
        oAll.arrange(DOWN)
        oAll.move_to([0,2,0])
        
        #NEW CODE
        
        sepLine = Line([-3,1,0], [3,1,0])
        
        
        t1 = MathTex(r"\text{Let Adam's number be }", r"a")
        t1[0][0:20].color = GRAY_A
        t1[1][0].color = RED_A
        t2 = MathTex(r"\text{and Bill's number be }", r"b")
        t2[0][0:20].color = GRAY_A
        t2[1][0].color = BLUE_A
        t3 = MathTex(r"0 < a < 1,")
        t3[0][2].color = RED_A
        t4 = MathTex(r"0 < b < 1")
        t4[0][2].color = BLUE_A
        t5 = MathTex(r"a", r"+", r"b", r"<", r"0.75")
        t5[0][0].color = RED_A
        t5[2][0].color = BLUE_A
        
        
        t = VGroup(t1,t2,t3,t4,t5)
        t.scale(0.3)
        t.arrange(DOWN)
        
        self.add(oAll)
        self.play(Create(sepLine))
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))
        self.play(Write(t5))
        self.wait(1)
        self.play(FadeOut(oAll), FadeOut(sepLine), FadeOut(t1), FadeOut(t2))
        
        tNext = VGroup(t3,t4,t5)
        self.play(tNext.animate.move_to([0,2,0]))
        self.wait(1)
        
class Scene4(Scene):
    def construct(self):
        o1 = MathTex(r"0 < a < 1,")
        o1[0][2].color = RED_A
        o2 = MathTex(r"0 < b < 1")
        o2[0][2].color = BLUE_A
        o3 = MathTex(r"a", r"+", r"b", r"<", r"0.75")
        o3[0][0].color = RED_A
        o3[2][0].color = BLUE_A
        
        oAll = VGroup(o1,o2,o3)
        oAll.scale(0.3)
        oAll.arrange(DOWN)
        oAll.move_to([0,2,0])
        
        #NEW
        t1 = MathTex(r"\text{Now let ", r"a", r"\text{ be the x-axis}")
        t1[1][0].color = RED_A
        t2 = MathTex(r"\text{and }", r"b", r"\text{ be the y-axis}")
        t2[1][0].color = BLUE_A
        
        t = VGroup(t1,t2)
        t.scale(0.3)
        t.arrange(DOWN)
        t.move_to([0,1.1,0])
        
        axes = Axes(
            x_range = [-1, 2, 1],
            y_range = [-1, 2, 1],
            x_length = 3,
            y_length = 3,
            tips = False
        )
        
        def func(x):
            return 0.75-x
        
        ab = axes.plot(
            func,
            x_range = [-1, 1.75],
            color = GOLD
        )
        
        labelA = MathTex(r"a")
        labelA.color = RED_A
        labelA.scale(0.75)
        labelA.move_to([-0.15,1.5,0])
        labelB = MathTex(r"b")
        labelB.color = BLUE_A
        labelB.scale(0.75)
        labelB.move_to([1.5,-0.2,0])
        
        abArea = axes.get_area(graph=ab, x_range=(0,0.75))
        abArea.color = GOLD
         
        wPlot = VGroup(axes, ab,labelA, labelB, abArea)
        wPlot.scale(0.75)
        wPlot.shift(0.75*DOWN)
        
        l1 = MathTex(r"\text{Area bounded by }", r"a=0, ", r"b=0,", r" a+b < 0.75")
        l1[1][0].color = RED_A
        l1[2][0].color = BLUE_A
        l1[3][0].color = RED_A
        l1[3][2].color = BLUE_A
        l2 = MathTex(r"\text{Divided by sample space bounded by 0 }< ",r"a < 1 \text{ and } 0 < ",r"b < 1")
        l2[1][0].color = RED_A
        l2[2][0].color = BLUE_A
        l3 = MathTex(r"\text{= probability that }", r"a + b < 0.75")
        l3[1][0].color = RED_A
        l3[1][2].color = BLUE_A
        
        l = VGroup(l1,l2,l3)
        l.scale(0.25)
        l.arrange(DOWN)
        
        f1 = MathTex(r"\text{Area: } \frac{1}{2}(0.75)(0.75) =", r"\frac{9}{32}")
        f1[1][0:10].color = GOLD
        f2 = MathTex(r"\text{Dividing that by the sample space: 1x1 = 1}")
        f3 = MathTex(r"\text{Probability: }", r"\frac{9}{32}")
        f3[1][0:10].color = GOLD
        
        f=VGroup(f1,f2,f3)
        f.scale(0.3)
        f.arrange(DOWN)
        f.move_to([0,-1.25,0])
        
        self.add(oAll)
        self.play(Write(t), run_time = 2)
        self.play(Write(axes), Write(labelA), Write(labelB))
        self.play(Create(ab))
        self.play(FadeOut(t), FadeOut(oAll))
        self.play(FadeIn(abArea))
        self.play(wPlot.animate.move_to([0,2,0]))
        self.play(Write(l), run_time = 3)
        self.play(Write(f), run_time = 3)
        self.wait(1)
        
        