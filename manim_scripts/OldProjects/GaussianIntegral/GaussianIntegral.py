from manim import*
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Gaussian Integral:}")
        textTop.color = GOLD
        textMid = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx")
        textMid[0][1:3].color = RED
        textMid[0][3:4].color = RED
        textMid[0][6:7].color = BLUE
        textMid[0][9:10].color = BLUE
        
        text = VGroup(textTop, textMid)
        text.scale(0.5)
        text.arrange(DOWN)
        
        self.play(Write(textTop))
        self.play(Write(textMid))
        self.wait(1)
        
class Second(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-4, 4, 2],
            y_range = [-2, 2, 0.5],
            x_length = 3,
            y_length = 5,
            tips = False
        )
        
        e = 2.71828
        
        def func(x):
            return e**(-(x**2))
        
        exp = axes.plot(
            func,
            x_range = [-4,4],
            color = BLUE
        )
        
        expLabel = MathTex(
            r"e^{-x^2}",
            substrings_to_isolate = "x"
            )
        expLabel.move_to([0,1,0])
        expLabel.set_color_by_tex("x", BLUE)
        expBack = BackgroundRectangle(expLabel, fill_opacity = 1)
        expAll = VGroup(expBack, expLabel)
        
        self.play(Create(axes))
        self.play(Create(exp))
        self.play(Create(expAll))
        self.play(expAll.animate.move_to([0,2,0]))
        self.wait(1)
        self.play(FadeOut(axes, exp, expAll))

class Third(Scene):
    def construct(self):
        expTop = MathTex(r"\int e^{-x^2} dx")
        expTop[0][3:4].color = BLUE
        expMid = MathTex(r"\text{Not integrable}")
        expMid.color = RED
        expLow = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx")
        expLow[0][1:3].color = RED
        expLow[0][3:4].color = RED
        expLow[0][6:7].color = BLUE
        expLow[0][9:10].color = BLUE
        eq = MathTex(r"= \sqrt{\pi}")
        eq.color = GOLD
        finalAll = VGroup(expTop, expMid, expLow, eq)
        finalAll.scale(0.5)
        finalAll.arrange(DOWN)
        
        self.play(Write(expTop))
        self.play(Write(expMid))
        self.play(Write(expLow))
        self.play(Write(eq))
        self.wait(1)