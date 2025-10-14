from manim import *
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Proving}")
        textUnder = MathTex(r"\text{Inverse Trig Derivatives}")
        
        text = VGroup(textTop, textUnder)
        text.scale(0.5)
        text.color = GOLD
        text.arrange(DOWN)
        
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(textTop))
        self.play(textUnder.animate.shift(2.5*UP))

class Arcsin(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Proving}")
        textUnder = MathTex(r"\text{Inverse Trig Derivatives}")
        text = VGroup(textTop, textUnder).scale(0.5).arrange(DOWN).color = GOLD
        self.add(textUnder.shift(2.5*UP))
        
        ##New
        textSin = MathTex(r"\frac{d}{dx} (\text{sin}^{-1} (f(x))) = \frac{1}{\sqrt{1-f(x)^2}} * f'(x)")
        textSin.scale(0.9)
        ##self.add(textSin)
        ##self.add(index_labels(textSin[0]))
        
        textSin[0][11:15].set_color(RED)
        textSin[0][24:28].set_color(RED)
        textSin[0][30:35].set_color(RED)
        
        textWhy = MathTex(r"\text{Why?}")
        textWhy.color = GOLD
        
        ex1 = MathTex(r"\text{Let sin}^{-1} (f(x)) = y")
        ex1[0][0:3].set_color(GOLD)
        ex1[0][9:13].set_color(RED)
        ex1[0][15:16].set_color(BLUE)
        
        ex2 = MathTex(r"f(x) = \text{sin} (y)")
        ex2[0][0:4].set_color(RED)
        ex2[0][9:10].set_color(BLUE)
        
        ex3 = MathTex(r"f'(x) = \frac{dy}{dx} * \text{cos} (y)")
        ex3[0][0:5].set_color(RED)
        ex3[0][7:8].set_color(BLUE)
        ex3[0][16:17].set_color(BLUE)
        
        ex4 = MathTex(r"\frac{1}{\text{cos} (y)} * f'(x) = \frac{dy}{dx} ")
        ex4[0][6:7].set_color(BLUE)
        ex4[0][9:14].set_color(RED)
        ex4[0][16:17].set_color(BLUE)
        
        ex5 = MathTex(r"\frac{1}{\sqrt{1 - \text{sin}^2 (y)}} * f'(x) = \frac{dy}{dx}")
        ex5[0][11:12].set_color(BLUE)
        ex5[0][14:19].set_color(RED)
        ex5[0][21:22].set_color(BLUE)
        
        ##self.add(index_labels(ex1[0]), index_labels(ex2[0]), index_labels(ex3[0]), index_labels(ex4[0]))
        
        textFirst = VGroup(textSin, textWhy, ex1, ex2, ex3, ex4, ex5)
        textFirst.arrange(DOWN)
        textFirst.scale(0.5)
        textFirst.shift(0)
        
        ex = VGroup(ex1, ex2, ex3, ex4, ex5)
        ex.next_to(textSin, 0.75*DOWN)
        
        self.play(Write(textSin))
        self.play(Write(textWhy))
        self.wait(0.5)
        self.play(FadeOut(textWhy))
        self.play(Write(ex1))
        self.wait(0.5)
        self.play(Write(ex2))
        self.wait(0.5)
        self.play(Write(ex3))
        self.wait(0.5)
        self.play(Write(ex4))
        self.wait(1)
        self.play(FadeOut(ex2, ex3))
        self.play(ex4.animate.shift(1*UP))
        self.wait(0.5)
        self.play(Write(ex5.shift(1*UP)))
        self.wait(1)
        self.play(FadeOut(ex4))
        self.play(ex5.animate.shift(0.75*UP))
        self.wait(1)

class Arcsin2(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Proving}")
        textUnder = MathTex(r"\text{Inverse Trig Derivatives}")
        text = VGroup(textTop, textUnder).scale(0.5).arrange(DOWN).color = GOLD
        textUnder.shift(2.5*UP)
        
        textSin = MathTex(r"\frac{d}{dx} (\text{sin}^{-1} (f(x))) = \frac{1}{\sqrt{1-f(x)^2}} * f'(x)")
        textSin.scale(0.9)
        textSin[0][11:15].set_color(RED)
        textSin[0][24:28].set_color(RED)
        textSin[0][30:35].set_color(RED)
        
        textWhy = MathTex(r"\text{Why?}")
        textWhy.color = GOLD
        
        ex1 = MathTex(r"\text{Let sin}^{-1} (f(x)) = y")
        ex1[0][0:3].set_color(GOLD)
        ex1[0][9:13].set_color(RED)
        ex1[0][15:16].set_color(BLUE)
        
        ex2 = MathTex(r"f(x) = \text{sin} (y)")
        ex2[0][0:4].set_color(RED)
        ex2[0][9:10].set_color(BLUE)
        
        ex3 = MathTex(r"f'(x) = \frac{dy}{dx} * \text{cos} (y)")
        ex3[0][0:5].set_color(RED)
        ex3[0][7:8].set_color(BLUE)
        ex3[0][16:17].set_color(BLUE)
        
        ex4 = MathTex(r"\frac{1}{\text{cos} (y)} * f'(x) = \frac{dy}{dx} ")
        ex4[0][6:7].set_color(BLUE)
        ex4[0][9:14].set_color(RED)
        ex4[0][16:17].set_color(BLUE)
        
        ex5 = MathTex(r"\frac{1}{\sqrt{1 - \text{sin}^2 (y)}} * f'(x) = \frac{dy}{dx}")
        ex5[0][11:12].set_color(BLUE)
        ex5[0][14:19].set_color(RED)
        ex5[0][21:22].set_color(BLUE)
        
        textFirst = VGroup(textSin, textWhy, ex1, ex2, ex3, ex4, ex5)
        textFirst.arrange(DOWN)
        textFirst.scale(0.5)
        textFirst.shift(0)
        
        ex = VGroup(ex1, ex2, ex3, ex4, ex5)
        ex.next_to(textSin, 0.75*DOWN)
        ex4.shift(UP)
        ex5.shift(1.75*UP)
        
        self.add(textUnder, textSin, ex1, ex5)
        
        ##NEW
        ex6 = MathTex(r"\text{sin}^2 (\text{sin}^{-1} (u)) = u^2")
        ex6[0][11:12].set_color(RED)
        ex6[0][15:16].set_color(RED)
        ex7 = MathTex(r"\frac{1}{\sqrt{1-f(x)^2}} * f'(x) = \frac{dy}{dx}")
        ex7[0][6:10].set_color(RED)
        ex7[0][12:17].set_color(RED)
        ex7[0][19:20].set_color(BLUE)
        ex8 = MathTex(r"\frac{d}{dx} (\text{sin}^{-1} (f(x))) = \frac{1}{\sqrt{1-f(x)^2}} * f'(x)")
        ex8[0][11:15].set_color(RED)
        ex8[0][24:28].set_color(RED)
        ex8[0][30:35].set_color(RED)
        ex8.scale(0.9)
        
        exFinal = VGroup(ex6, ex7, ex8)
        exFinal.scale(0.5)
        exFinal.arrange(DOWN)
        exFinal.next_to(ex5, 0.75*DOWN)
        
        self.play(Write(ex6))
        self.wait(0.5)
        self.play(Write(ex7))
        self.wait(0.5)
        self.play(Write(ex8))
        self.wait(0.5)
        self.play(FadeOut(ex1, ex5, ex6, ex7))
        self.play(ex8.animate.next_to(textSin, 0*DOWN))
        self.wait(0.5)
        
        finalText = VGroup(textUnder, textSin, ex8)
        self.play(finalText.animate.shift(2*DOWN))
        self.play(Circumscribe(finalText, color = GOLD))
        self.wait(0.5)
        textF = MathTex(r"\text{(All Other Inverse Trig Derivatives}")
        textU = MathTex(r"\text{Can Be Derived in Similar Ways)}")
        
        textAll = VGroup(textF, textU)
        textAll.color = GOLD
        textAll.scale(0.4)
        textAll.arrange(DOWN)
        textAll.shift(1.5*UP)
        self.play(Write(textAll))
        self.wait(1)
        self.play(FadeOut(textAll))
        self.wait(1)
        
        