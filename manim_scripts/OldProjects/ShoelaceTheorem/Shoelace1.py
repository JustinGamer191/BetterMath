from manim import*
import math

class Cover(Scene):
    def construct(self):
        x1 = np.array([-1,2,0])
        x2 = np.array([-1,1,0])
        x3 = np.array([-1,0,0])
        x4 = np.array([-1,-1,0])
        x5 = np.array([-1,-2,0])
        
        y1 = np.array([1,2,0])
        y2 = np.array([1,1,0])
        y3 = np.array([1,0,0])
        y4 = np.array([1,-1,0])
        y5 = np.array([1,-2,0])
        
        textTop = MathTex(r"\text{Shoelace Theorem:}")
        textBot = MathTex(r"\text{Area of a Simple Polygon}")
        
        text = VGroup(textTop, textBot)
        text.scale(0.5)
        text.arrange(DOWN)
        text.color = GOLD
        
        a1 = Line(x1, y2)
        b1 = Line(y1, x2)
        a2 = Line(x2, y3)
        b2 = Line(y2, x3)
        a3 = Line(x3, y4)
        b3 = Line(y3, x4)
        a4 = Line(x4, y5)
        b4 = Line(y4, x5)
        
        laces = VGroup(a1,b1,a2,b2,a3,b3,a4,b4)
        laces.color = GOLD
        
        self.play(Create(a1), Create(b1))
        self.play(Create(a2), Create(b2))
        self.play(Create(a3), Create(b3))
        self.play(Create(a4), Create(b4))
        self.play(Transform(laces, text))
        self.wait(1)
        self.play(laces.animate.move_to([0,2,0]))
        self.wait(1)

class Second(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Shoelace Theorem:}")
        textBot = MathTex(r"\text{Area of a Simple Polygon}")
        
        text = VGroup(textTop, textBot)
        text.scale(0.5)
        text.arrange(DOWN)
        text.color = GOLD
        text.move_to([0,2,0])
        
        self.add(text)
        
        exp = MathTex(r"\text{Given the coordiantes of the vertices of a simple polygon}")
        exp.color = GOLD
        exp1 = MathTex(r"(x_1,y_1), (x_2,y_2), \cdots , (x_n,y_n), \text{ listed in clockwise order}")
        exp1[0][1:3].color = RED
        exp1[0][9:11].color = RED
        exp1[0][21:23].color = RED
        
        exp1[0][4:6].color = BLUE
        exp1[0][12:14].color = BLUE
        exp1[0][24:26].color = BLUE
        
        exp1[0][28:50].color = GOLD
        exp2 = MathTex(r"\text{the area of the polygon is equal to:}")
        exp2.color = GOLD
        exp3 = MathTex(r"\frac{1}{2}|(x_1 y_2 + x_2 y_3 + \cdots + x_n y_1) - (y_1 x_2 + y_2 x_3 + \cdots + y_n x_1)|")
        exp3[0][5:7].color = RED
        exp3[0][10:12].color = RED
        exp3[0][19:21].color = RED
        exp3[0][28:30].color = RED
        exp3[0][33:35].color = RED
        exp3[0][42:44].color = RED
        
        exp3[0][7:9].color = BLUE
        exp3[0][12:14].color = BLUE
        exp3[0][21:23].color = BLUE
        exp3[0][26:28].color = BLUE
        exp3[0][31:33].color = BLUE
        exp3[0][40:42].color = BLUE
        
        expAll = VGroup(exp, exp1, exp2, exp3)
        expAll.scale(0.25)
        expAll.arrange(DOWN)
        expAll.shift(0.5*UP)
        
        everyting = VGroup(expAll, text)
        
        self.play(Write(exp))
        self.play(Write(exp1))
        self.play(Write(exp2))
        self.play(Write(exp3))
        self.play(everyting.animate.move_to([0,0,0]))
        self.wait(5)
