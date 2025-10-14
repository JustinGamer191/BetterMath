from manim import *
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\text{The Binomial Theorem}")
        textTop.color = GOLD
        textMid = MathTex(r"(a-b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}")

        textMid[0][1:2].color = RED
        textMid[0][3:4].color = BLUE
        textMid[0][16:17].color = RED
        textMid[0][18:19].color = BLUE

        text = VGroup(textTop, textMid)
        text.scale(0.5)
        text.arrange(DOWN)
        
        self.play(Write(textTop))
        self.play(Write(textMid))
        self.wait(1)
        self.play(FadeOut(textTop))
        self.play(textMid.animate.move_to([0,2.5,0]))
        self.wait(1)
        
class Second(Scene):
    def construct(self):
        textMid = MathTex(r"(a-b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}")
        textMid.scale(0.5)
        textMid[0][1:2].color = RED
        textMid[0][3:4].color = BLUE
        textMid[0][16:17].color = RED
        textMid[0][18:19].color = BLUE
        
        textApp = MathTex(r"\text{Application:}")
        textApp.color = GOLD
        textApp.scale(0.5)
        textQ = MathTex(r"\text{Find the hundreds digit of } 2011^{2011}.")
        textQ.color = GOLD
        textQ.scale(0.32)
        
        text = VGroup(textMid, textApp, textQ)
        text.arrange(DOWN)
        text.move_to([0,2,0])
        
        self.add(textMid)
        self.play(Write(textApp))
        self.play(Write(textQ))
        self.wait(1)
        self.play(FadeOut(textApp))
        self.play(textQ.animate.move_to([0,1.75,0]))
        self.wait(1)
        
        textS1 = MathTex(r"\text{Step 1: Find the modulus 1000 congruence of } 4022^{2011}.")
        textS1.scale(0.8)
        textS1.color = GOLD
        textE1 = MathTex(r"\text{(We do this because we only need the hundreds digit)}")
        textE1.scale(0.8)
        textA1 = MathTex(r"2011^{2011} \equiv 11^{2011} (mod 1000)")
        textA1.color = RED
        text1 = VGroup(textS1, textE1, textA1)
        text1.scale(0.4)
        text1.arrange(DOWN)
        text1.move_to([0,1,0])
        self.play(Write(textS1))
        self.play(Write(textE1))
        self.play(Write(textA1))
        self.play(FadeOut(textE1))
        self.play(textA1.animate.move_to(textE1))
        
        textS2 = MathTex(r"\text{Step 2: Manipulate the expression:}")
        textS2.color = GOLD
        textS2.scale(0.8)
        textA2 = MathTex(r"11^{2011} = (10+1)^{2011}")
        
        textS3 = MathTex(r"\text{Using the Binomial Theorem:}")
        textS3.color = GOLD
        textS3.scale(0.8)
        textA3 = MathTex(r"(10+1)^{2011} = 1 + \binom{2011}{1} (10) + \binom{2011}{2} (10^2) \cdots")
        textA3.scale(0.8)
        textAll = VGroup(textS2, textA2, textS3, textA3)
        textAll.scale(0.4)
        textAll.arrange(DOWN)
        textAll.shift(0.15*DOWN)
        self.play(Write(textS2))
        self.play(Write(textA2))
        self.play(Write(textS3))
        self.play(Write(textA3))
        self.wait(1)
        self.play(FadeOut(textMid, textQ, textS1, textA1, textS2, textA2, textS3))
        self.play(textA3.animate.move_to([0,1,0]))
        self.wait(1)
        
class Final(Scene):
    def construct(self):
        textA3 = MathTex(r"(10+1)^{2011} = 1 + \binom{2011}{1} (10) + \binom{2011}{2} (10^2) \cdots")
        textA3.scale(0.32)
        textA3.move_to([0,1,0])
        
        textEx = MathTex(r"\text{All terms after the } 10^2 \text{ term don't impact the sum}")
        textEx.color = GOLD
        textEx2 = MathTex(r"\text{as they will all have a 0 in the hundreds place.}")
        textEx2.color = GOLD
        
        textF = MathTex(r"1 + 110 + 500 = 611")
        textEx3 = MathTex(r"\text{Hundreds Digit: 6}")
        textEx3[0][14:15].color = GOLD
        
        textFinal = VGroup(textEx, textEx2, textF, textEx3)
        textFinal.scale(0.32)
        textFinal.arrange(DOWN)
        
        self.add(textA3)
        self.play(Write(textEx))
        self.play(Write(textEx2))
        self.play(Write(textF))
        self.play(Write(textEx3))
        self.wait(1)