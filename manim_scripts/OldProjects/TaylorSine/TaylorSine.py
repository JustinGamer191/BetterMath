from manim import *
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Proof that:}")
        textTop.color = GOLD
        textMid = MathTex(r"\text{sin} (x) = x - \frac{1}{3!} x^3 + \frac{1}{5!} x^5 ...")
        textMid[0][4:5].color = BLUE
        textMid[0][7:8].color = BLUE
        textMid[0][13:14].color = BLUE
        textMid[0][20:21].color = BLUE
        text = VGroup(textTop, textMid)
        text.scale(0.5)
        text.arrange(DOWN)
        self.play(Write(textTop))
        self.play(Write(textMid))
        self.play(FadeOut(text))
        self.wait(1)

class Second(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-3.15, 3.15, 0.63],
            y_range = [-2, 2, 0.4],
            x_length = 3,
            y_length = 5,
            tips = False
        )
        
        def func(x):
            return math.sin(x)
        
        sinG = axes.plot(
            func,
            x_range = [-3.1415,3.1415],
            color = RED
        )
        
        sinLabel = MathTex(r"f(x) = \text{sin} (x)")
        sinLabel.scale(0.5)
        sinLabel[0][2:3].color = RED
        sinLabel[0][9:10].color = RED
        
        sinBG = BackgroundRectangle(sinLabel, fill_opacity = 1)
        
        sinAll = VGroup(sinBG, sinLabel)
        
        self.play(Write(axes))
        self.play(Write(sinG))
        self.play(Write(sinAll))
        self.play(sinAll.animate.move_to([0,2,0]))    
        
        ##1111111111111111111111111111111111111111111
        def mac1(x):
            return x
        
        deg1 = axes.plot(
            mac1,
            x_range = [-2,2],
            color = BLUE
        )
        
        deg1L = MathTex(r"g(x) = x")
        deg1L.scale(0.5)
        deg1L[0][2:3].color = BLUE
        deg1L[0][5:6].color = BLUE
        
        deg1BG = BackgroundRectangle(deg1L, fill_opacity = 1)
        
        deg1All = VGroup(deg1BG, deg1L)
        
        self.play(Write(deg1))
        self.play(Write(deg1All))
        self.play(deg1All.animate.move_to([0,-2,0]))
        
        ##2222222222222222222222222222222222222222222
        def mac2(x):
            return x - (1/6)*x**3
        
        deg2 = axes.plot(
            mac2,
            x_range = [-3.13, 3.13],
            color = BLUE
        )
        
        deg2L = MathTex(
            r"g(x) = x - \frac{1}{3!} x^3",
            substrings_to_isolate = "x"
            )
        deg2L.scale(0.5)
        deg2L.set_color_by_tex("x", BLUE)
        
        deg2BG = BackgroundRectangle(deg2L, fill_opacity = 1)
        
        deg2All = VGroup(deg2BG, deg2L)
        deg2All.move_to([0,-2,0])
        
        self.play(Transform(deg1, deg2), Transform(deg1All, deg2All))
        
        ##3333333333333333333333333333333333333333333
        def mac3(x):
            return x - (1/6)*x**3 + (1/120)*x**5
        
        deg3 = axes.plot(
            mac3,
            x_range = [-3.1415, 3.1415],
            color = BLUE
        )
        
        deg3L = MathTex(
            r"g(x) = x - \frac{1}{3!} x^3 + \frac{1}{5!} x^5",
            substrings_to_isolate = "x"
            )
        deg3L.scale(0.5)
        deg3L.set_color_by_tex("x", BLUE)
        
        deg3BG = BackgroundRectangle(deg3L, fill_opacity = 1)
        
        deg3All = VGroup(deg3BG, deg3L)
        deg3All.move_to([0,-2,0])
        
        self.play(Transform(deg1, deg3), Transform(deg1All, deg3All))
        
        ##444444444444444444444444444444444444444444
        def mac4(x):
            return x - (1/6)*x**3 + (1/120)*x**5 - (1/5040)*x**7
        
        deg4 = axes.plot(
            mac4,
            x_range = [-3.1415, 3.1415],
            color = BLUE
        )
        
        deg4L = MathTex(
            r"g(x) = x - \frac{1}{3!} x^3 + \frac{1}{5!} x^5 ...",
            substrings_to_isolate = "x"
            )
        deg4L.scale(0.5)
        deg4L.set_color_by_tex("x", BLUE)
        
        deg4BG = BackgroundRectangle(deg4L, fill_opacity = 1)
        
        deg4All = VGroup(deg4BG, deg4L)
        deg4All.move_to([0,-2,0])
        
        self.play(Transform(deg1, deg4), Transform(deg1All, deg4All))
        
        ##555555555555555555555555555555555555555555
        def mac5(x):
            return math.sin(x)
        
        deg5 = axes.plot(
            mac5,
            x_range = [-3.1415, 3.1415],
            color = BLUE
        )
        
        deg5L = MathTex(
            r"g(x) = x - \frac{1}{3!} x^3 + \frac{1}{5!} x^5 ...",
            substrings_to_isolate = "x"
            )
        deg5L.scale(0.5)
        deg5L.set_color_by_tex("x", BLUE)
        
        deg5BG = BackgroundRectangle(deg5L, fill_opacity = 1)
        
        deg5All = VGroup(deg5BG, deg5L)
        deg5All.move_to([0,-2,0])
        
        
        self.play(Transform(deg1, deg5), Transform(deg1All, deg5All))
        self.wait(1)
        self.remove(sinG)
        self.play(FadeOut(deg1All, sinAll))
        self.play(FadeOut(deg1, axes))
        
class Third(Scene):
    def construct(self):
        fOf = MathTex(
            r"f(x) = \text{sin} (x)",
            )
        fOf[0][2:3].color = RED
        fOf[0][9:10].color = RED
        fOf.scale(0.5)
        fOf.move_to(2*UP)
        
        fP1 = MathTex(r"f(0) = 0")
        fP2 = MathTex(r"f'(0) = 1")
        fP3 = MathTex(r"f''(0) = 0")
        fP4 = MathTex(r"f'''(0) = -1")
        fDots = MathTex(r"\cdots")
        
        fAll = VGroup(fP1, fP2, fP3, fP4, fDots)
        fAll.color = GOLD
        fAll.scale(0.5)
        fAll.arrange(DOWN)
        fAll.next_to(fOf, 0.75*DOWN)
        
        self.play(Write(fOf))
        self.play(Write(fP1))
        self.play(Write(fP2))
        self.play(Write(fP3))
        self.play(Write(fP4))
        self.play(Write(fDots))
        self.play(FadeOut(fOf, fAll))
        
        gOf = MathTex(
            r"g(x) = x - \frac{1}{3!} x^3 + \frac{1}{5!} x^5 ...",
            substrings_to_isolate = "x"
            )
        gOf.set_color_by_tex("x", BLUE)
        gOf.scale(0.5).move_to([0,2,0])
        
        gP1 = MathTex(r"g(0) = 0")
        gP2 = MathTex(r"g'(0) = 1")
        gP3 = MathTex(r"g''(0) = 0")
        gP4 = MathTex(r"g'''(0) = -1")
        gDots = MathTex(r"\cdots")
        
        gAll = VGroup(gP1, gP2, gP3, gP4, gDots)
        gAll.color = GOLD
        gAll.scale(0.5)
        gAll.arrange(DOWN)
        gAll.next_to(gOf, 0.75*DOWN)
        
        self.play(Write(gOf))
        self.play(Write(gP1))
        self.play(Write(gP2))
        self.play(Write(gP3))
        self.play(Write(gP4))
        self.play(Write(gDots))
        self.play(FadeOut(gOf, gAll))
        
        eq1 = MathTex(r"f(0)=g(0)")
        eq2 = MathTex(r"f'(0)=g'(0)")
        eq3 = MathTex(r"f''(0)=g''(0)")
        eq4 = MathTex(r"f'''(0)=g'''(0)")
        dots = MathTex(r"...")
        eq5 = MathTex(
            r"f(x) = g(x)"
            )
        eq5[0][2:3].color = RED
        eq5[0][7:8].color = BLUE
        
        eqGold = VGroup(eq1, eq2, eq3, eq4, dots)
        eqGold.color = GOLD
        
        eqAll = VGroup(eq1, eq2, eq3, eq4, dots, eq5)
        eqAll.scale(0.5)
        eqAll.arrange(DOWN)
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))
        self.play(Write(eq4))
        self.play(Write(dots))
        self.play(Write(eq5))
        self.wait(1)