from manim import *
import math

class Start(Scene):
    def construct(self):
        textMid = MathTex(r"\text{Indeterminate Forms}")
        textF1 = MathTex(r"\frac{0}{0}")
        textF1.move_to([0,1.414,0])
        textF2 = MathTex(r"\frac{\infty}{\infty}")
        textF2.move_to([1.414,1.414,0])
        textF3 = MathTex(r"\infty - \infty")
        textF3.move_to([1.414,-1.414,0])
        textF4 = MathTex(r"0^0")
        textF4.move_to([0,-1.414,0])
        textF5 = MathTex(r"1^\infty")
        textF5.move_to([-1.414, -1.414,0])
        textF6 = MathTex(r"\infty ^ 0")
        textF6.move_to([-1.414,1.414,0])
        
        text = VGroup(textMid, textF1, textF2, textF3, textF4, textF5, textF6)
        text.color = GOLD
        text.scale(0.5)
        
        self.play(Write(text))
        self.wait(0.25)
        self.play(FadeOut(textMid, textF2, textF3, textF4, textF5, textF6))
        self.play(textF1.animate.move_to([0,0,0]))
        self.wait(1)
        
class Second(Scene):
    def construct(self):
        textOld = MathTex(r"\frac{0}{0}")
        textOld.color = GOLD
        textOld.scale(0.5)
        textOld.move_to([0,3,0])
        self.add(textOld)
        
        textEx = MathTex(r"\frac{100-100}{10-10}")
        textEx2 = MathTex(r"\frac{(10-10)(10+10)}{10-10}")
        textEx3 = MathTex(r"\frac{10+10}{1}")
        textEx4 = MathTex(r"\frac{10+10}{1} = 20?")
        
        textAll = VGroup(textEx, textEx2, textEx3, textEx4)
        textAll.color = GOLD
        textAll.scale(0.5)
        textAll.arrange(DOWN)
        self.play(Write(textAll), run_time = 4)
        self.wait(2)
        
        