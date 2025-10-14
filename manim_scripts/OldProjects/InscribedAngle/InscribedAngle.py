from manim import*
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Circles}")
        textTop.scale(0.5)
        textTop.color = GOLD
        
        circle = Circle(color = GOLD)
        
        self.play(Write(textTop))
        self.play(Create(circle))
        self.play(FadeOut(textTop))
        
class Second(Scene):
    def construct(self):
        circle = Circle(color = GOLD)
        self.add(circle)
        
        p1 = np.array([1/2, math.sqrt(3)/2, 0])
        p3 = np.array([-math.sqrt(2)/2, -math.sqrt(2)/2, 0])
        p2 = np.array([0, 1, 0])
        p4 = np.array([0,0,0])
        
        line12 = Line(p1, p2)
        line12.color = BLUE
        line23 = Line(p2, p3)
        line23.color = BLUE
        line34 = Line(p3, p4)
        line34.color = BLUE
        line41 = Line(p4, p1)
        line41.color = BLUE
        arc1 = ArcBetweenPoints(start = p3, end = p1, angle = 3.40329)
        arc1.color = BLUE
        
        p1L = MathTex(r"(\frac{1}{2}, \frac{\sqrt{3}}{2})")
        p1L.move_to([3.4, 4.25, 0])
        p2L = MathTex(r"(0,1)")
        p2L.move_to([0.5,4.5,0])
        p3L = MathTex(r"(\frac{-\sqrt{2}}{-\sqrt{2}}, \frac{-\sqrt{2}}{-\sqrt{2}})")
        p3L.move_to([-3,-4.25,0])
        p4L = MathTex(r"(0,0)")
        p4L.shift(0.75*RIGHT, 0.75*DOWN)
        
        labels = VGroup(p1L, p2L, p3L, p4L)
        labels.scale(0.25)
        
        angle341 = Angle.from_three_points(p3,p4,p1, radius = 0.15, other_angle = False)
        l341 = MathTex(r"195^{\circ}")
        l341.scale(0.25)
        l341.move_to(angle341)
        l341.shift(0.25*DOWN, 0.25*RIGHT)
        
        angle321 = Angle.from_three_points(p3, p2, p1, radius=0.15, other_angle = False)
        l321 = MathTex(r"97.5^{\circ}")
        l321.scale(0.25)
        l321.move_to(angle321)
        l321.shift(0.15*DOWN, 0.15*RIGHT)
        
        
        self.play(Create(line12))
        self.play(Create(line23))
        self.play(Create(line34))
        self.play(Create(line41))
        self.play(Create(arc1))
        self.wait(1)
        self.play(Write(labels))
        self.wait(1)
        self.play(FadeOut(labels))
        self.play(Create(angle341))
        self.play(Write(l341))
        self.wait(1)
        self.play(Create(angle321))
        self.play(Write(l321))
        self.wait(1)
        self.play(FadeOut(line12,line23,line34,line41,arc1,angle341,l341,angle321,l321, circle))

class Third(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Generalization:}")
        textTop.scale(0.5)
        textTop.move_to([0,2.5,0])
        textTop.color = GOLD
        
        circle = Circle()
        circle.color = GOLD
        
        p1 = np.array([12/13,5/13,0])
        p2 = np.array([-1,0,0])
        p3 = np.array([12/13, -5/13, 0])
        p4 = np.array([0,0,0])
        
        d1 = always_redraw(
            lambda: Dot(
                p1
            )
        )
        d2 = always_redraw(
            lambda: Dot(
                p2
            )
        )
        d3 = always_redraw(
            lambda: Dot(
                p3
            )
        )
        self.play(Write(textTop))
        self.play(Create(circle))
        self.wait(1)