from manim import *
import math

class First(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Shoelace Theorem}")
        textMid = MathTex(r"\text{The Proof: Part 2}")
        
        topic = VGroup(textTop, textMid)
        topic.scale(0.5)
        topic.arrange(DOWN)
        topic.color = GOLD
        topic.shift(UP)
        
        
        
        expPoly = Polygon([0,0.5,0], [1,1,0], [1,0,0], [0,-0.5,0], [-0.75,0,0])
        triL = Polygon([0,0.5,0], [-0.75,0,0], [0,-0.5,0])
        triL.color = GOLD
        polyL = Polygon([0,0.5,0], [1,1,0], [1,0,0], [0,-0.5,0])
        polyL.color = RED
        allPoly = VGroup(expPoly, triL, polyL)
        allPoly.scale(0.75)
        allPoly.shift(0.5*DOWN, 0.05*LEFT)
        
        self.play(Write(topic))
        
        self.play(Create(expPoly))
        self.play(Create(triL))
        self.play(Create(polyL))
        self.remove(expPoly)
        self.play(triL.animate.shift(0.25*DOWN, 0.15*LEFT), polyL.animate.shift(0.15*RIGHT, 0.1*UP))
        self.wait(0.5)
        self.play(FadeOut(topic), FadeOut(triL), FadeOut(polyL))
        self.wait(1)
class Second(Scene):
    def construct(self):
        textTop = MathTex(r"\text{From Part 1:}")
        textTop.color = RED
        textMid = MathTex(r"\text{Area of a Triangle:}")
        textMid.color = GOLD
        textBottom = MathTex(r"\frac{1}{2}|(x_3 y_2 + x_2 y_1 + x_1 y_3) - (x_2 y_3 - x_1 y_2 - x_3 y_1)|")
        textBottom.color = RED
        textLow = MathTex(r"\text{Where } (x_1,y_1), (x_2,y_2), (x_3,y_3) \text{ are the vertices.}")
        textLow.color = GOLD
        
        textAll = VGroup(textTop, textMid, textBottom, textLow)
        textAll.scale(0.25)
        textAll.arrange(DOWN)
        
        textnew1 = MathTex(r"\text{Now Proving with Induction:}")
        textnew1.color = RED
        textnew2 = MathTex(r"\text{A polygon with vertices } (x_1,y_1), ... , (x_n, y_n) \text{ has an area:}")
        textnew2.color = GOLD
        textnew3 = MathTex(r"A = \frac{1}{2} |\sum_{n=1}^{k}(x_n y_{n+1} - x_{i+1} y_n)|")
        textnew3.color = RED
        
        textnew = VGroup(textnew1, textnew2, textnew3)
        textnew.scale(0.25)
        textnew.arrange(DOWN)
        textnew.shift(0.5*DOWN)
        
        self.play(Write(textAll, run_time = 4))
        self.play(textAll.animate.shift(1*UP))
        self.play(Write(textnew), run_time = 3)
        self.wait(2)
        self.play(FadeOut(textAll), FadeOut(textnew))
class Third(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Base Case: k = 3}")
        t1.color = GOLD
        t2 = MathTex(r"A = \frac{1}{2} |\sum_{n=1}^{3}(x_n y_{n+1} - x_{i+1} y_n)|")
        t2.color = RED
        t3 = MathTex(r"A = \frac{1}{2}|(x_3 y_2 + x_2 y_1 + x_1 y_3) - (x_2 y_3 - x_1 y_2 - x_3 y_1)|")
        t3.color = GOLD
        
        t4 = MathTex(r"\text{Now we prove if k is true, k+1 is true:}")
        t4.color = RED
        t5 = MathTex(r"\text{Let } P_k \text{ be the point } (x_k, y_k)")
        t5.color = GOLD
        t6 = MathTex(r"\text{Split the polygon } P_1, P_2, ... P_{k+1} \text{ into two polygons: }")
        t6.color = RED
        t7 = MathTex(r"P_1, P_2, P_3, ... P_k \text{ and } P_1, P_k, P_{k+1}")
        t7.color = GOLD
        
        expPoly = Polygon([0,0.5,0], [1,1,0], [1,0,0], [0,-0.5,0], [-0.75,0,0])
        triL = Polygon([0,0.5,0], [-0.75,0,0], [0,-0.5,0])
        triL.color = GOLD
        polyL = Polygon([0,0.5,0], [1,1,0], [1,0,0], [0,-0.5,0])
        polyL.color = RED
        
        tAll = VGroup(t1,t2,t3,t4,t5,t6,t7)
        tAll.scale(0.25)
        tAll.arrange(DOWN)
        tAll.shift(UP)
        polyAll = VGroup(expPoly, triL, polyL)
        polyAll.shift(1.5*DOWN, 0.05*LEFT)
        polyAll.scale(0.75)
        
        t8 = MathTex(r"\text{Area of } P_1, P_2, ... ,P_k = \frac{1}{2} |\sum_{n=1}^{k}(x_n y_{n+1} - x_{i+1} y_n)|")
        t8.color = GOLD
        t9 = MathTex(r"\text{Area of } P_1,P_k, P_{k+1} = ")
        t9.color = RED
        t10 = MathTex(r"\frac{1}{2} |(x_1 y_k - x_k y_1 + x_k y_{k+1} - x_{k+1} y_k + x_{k+1} y_1 - x_1 y_{k+1})|")
        t10.color = GOLD
        
        u1 = MathTex(r"\text{Area of } P_1, P_2, ..., P_{k+1} = \text{Area of } P_1, P_2,...,P_k + \text{Area of } P_1,P_k,P_{k+1}")
        u1.color = RED
        u2 = MathTex(r"= \frac{1}{2} ((x_1 y_2 + ... + x_k y_1 -x_k y_1 + x_k y_{k+1} + x_{k+1} y_1)")
        u2.color = GOLD
        u3 = MathTex(r"-(x_2 y_1 + ... + x_1 y_k - x_1 y_k + x_{k+1} y_k + x_1 y_{k+1})")
        u3.color = RED
        u4 = MathTex(r"= \frac{1}{2} ((x_1 y_2 +...+x_k y_{k+1} + x_{k+1} y_1) - (x_2 y_1 + ... + x_{k+1}y_k + x_1 y_{k+1}))")
        u4.color = GOLD
        u5 = MathTex(r"= \frac{1}{2} |\sum_{n=1}^{k+1}(x_n y_{n+1} - x_{i+1} y_n)|")
        u5.color = RED
        
        uAll = VGroup(u1,u2,u3,u4,u5)
        uAll.scale(0.25)
        uAll.arrange(DOWN)
        uAll.shift(DOWN)
        
        tlater = VGroup(t8,t9,t10)
        tlater.scale(0.25)
        tlater.arrange(DOWN)
        tlater.shift(UP)
        
        
        
        self.play(Write(tAll))     
        self.play(Create(expPoly))
        self.play(Create(triL))
        self.play(Create(polyL))
        self.remove(expPoly)
        self.play(triL.animate.shift(0.25*DOWN, 0.15*LEFT), polyL.animate.shift(0.15*RIGHT, 0.1*UP))
        self.wait(1)
        tleft = VGroup(t4,t5,t6,t7)
        self.play(FadeOut(triL),FadeOut(polyL) , FadeOut(t1),FadeOut(t2),FadeOut(t3))
        self.play(tleft.animate.move_to([0,2.5,0]))
        self.play(Write(tlater), run_time = 3)
        self.play(Write(uAll), run_time = 5)
        self.wait(5)