from manim import*
import math

class Cover(Scene):
    def construct(self):
        textTitle = MathTex(r"\text{Proving: The Binomial Theorem}")
        textTitle.color = GOLD
        textForm = MathTex(r"(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}")
        textForm[0][1:2].color = RED
        textForm[0][3:4].color = BLUE
        textForm[0][16:17].color = RED
        textForm[0][18:19].color = BLUE
        textForm.move_to([0,-0.375,0])
        
        text = VGroup(textTitle, textForm)
        text.scale(0.5)
        
        textInd = MathTex(r"\text{By Induction:}")
        textInd.color = GOLD
        step1 = MathTex(r"\text{Note: } n=0, 1 = \binom{0}{0} a^0 b^0 ")
        step1[0][15:16].color = RED
        step1[0][17:18].color = BLUE
        step2P1 = MathTex(r"\text{Assuming it works for n,}")
        step2P1.color = GOLD
        step2P2 = MathTex(r"\text{we must prove it works for n+1}")
        step2P2.color = GOLD
        step2dot5 = MathTex(
            r"(a+b)^n = a^n + {n \choose 1} a^{n-1}b \cdots {n \choose n-1} a b^{n-1} + b^n",
            substrings_to_isolate = "a" + "b"
            )
        step2dot5.set_color_by_tex("a", RED)
        step2dot5.set_color_by_tex("b", BLUE)
        step3P1 = MathTex(
            r"(a+b)^{n+1} = (a+b)(a+b)^n",
            substrings_to_isolate= "a" + "b"
            )
        step3P1.set_color_by_tex("a", RED)
        step3P1.set_color_by_tex("b", BLUE)
        step3P2 = MathTex(
            r"=(a+b)(a^n + {n \choose 1} a^{n-1}b \cdots {n \choose n-1} a b^{n-1} + b^n)",
            substrings_to_isolate= "a" + "b"
            )
        step3P2.set_color_by_tex("a", RED)
        step3P2.set_color_by_tex("b", BLUE)
        
        allSteps = VGroup(step1, textInd, step2P1, step2P2, step2dot5, step3P1, step3P2)
        allSteps.scale(0.3)
        allSteps.arrange(DOWN)
        allSteps.shift(0.4*UP)
        
        self.play(Write(textTitle))
        self.play(textTitle.animate.move_to([0,0.375,0]))
        self.play(Write(textForm))
        self.play(FadeOut(textTitle))
        self.play(textForm.animate.move_to([0,2.5,0]).scale(0.6))
        self.wait(1)
        self.play(Write(step1))
        self.play(Write(textInd))
        self.play(Write(step2P1))
        self.play(Write(step2P2))
        self.wait(1)
        self.play(Write(step2dot5))
        self.wait(1)
        self.play(Write(step3P1))
        self.play(Write(step3P2))
        self.wait(1)
        
class Second(Scene):
    def construct(self):
        textForm = MathTex(r"(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}")
        textForm[0][1:2].color = RED
        textForm[0][3:4].color = BLUE
        textForm[0][16:17].color = RED
        textForm[0][18:19].color = BLUE
        textForm.move_to([0,2.5,0]).scale(0.3)
        
        textInd = MathTex(r"\text{By Induction:}")
        textInd.color = GOLD
        step1 = MathTex(r"\text{Note: } n=0, 1 = \binom{0}{0} a^0 b^0 ")
        step1[0][15:16].color = RED
        step1[0][17:18].color = BLUE
        step2P1 = MathTex(r"\text{Assuming it works for n,}")
        step2P1.color = GOLD
        step2P2 = MathTex(r"\text{we must prove it works for n+1}")
        step2P2.color = GOLD
        step2dot5 = MathTex(
            r"(a+b)^n = a^n + {n \choose 1} a^{n-1}b \cdots {n \choose n-1} a b^{n-1} + b^n",
            substrings_to_isolate = "a" + "b"
            )
        step2dot5.set_color_by_tex("a", RED)
        step2dot5.set_color_by_tex("b", BLUE)
        step3P1 = MathTex(
            r"(a+b)^{n+1} = (a+b)(a+b)^n",
            substrings_to_isolate= "a" + "b"
            )
        step3P1.set_color_by_tex("a", RED)
        step3P1.set_color_by_tex("b", BLUE)
        step3P2 = MathTex(
            r"=(a+b)(a^n + {n \choose 1} a^{n-1}b \cdots {n \choose n-1} a b^{n-1} + b^n)",
            substrings_to_isolate= "a" + "b"
            )
        step3P2.set_color_by_tex("a", RED)
        step3P2.set_color_by_tex("b", BLUE)
        
        allSteps = VGroup(step1, textInd, step2P1, step2P2, step2dot5, step3P1, step3P2)
        allSteps.scale(0.3)
        allSteps.arrange(DOWN)
        allSteps.shift(0.4*UP)
        
        self.add(allSteps, textForm)
        
        ##NEW
        self.play(FadeOut(textForm, step1, textInd, step2P1, step2P2, step2dot5, step3P1))
        self.play(step3P2.animate.move_to([0,2.5,0]))
        self.wait(1)
        
        step4PA = MathTex(
            r"= a^{n+1} + [1 + {n \choose 1}] a^n b + [{n \choose 1} + {n \choose 2}]a^{n-1} b^2 + \cdots",
            substrings_to_isolate = "a" + "b"
            )
        step4PA.set_color_by_tex("a", RED)
        step4PA.set_color_by_tex("b", BLUE)
        step4PB = MathTex(
            r"\cdots + [{n \choose r-1} + {n \choose r}] a^{n-r+1} b^r + \cdots",
            substrings_to_isolate = "a" + "b"
            )
        step4PB.set_color_by_tex("a", RED)
        step4PB.set_color_by_tex("b", BLUE)
        step4PC = MathTex(
            r"\cdots + [{n \choose {n-1}} + 1] a b^k + b^{k+1}",
            substrings_to_isolate = "a" + "b"
            )
        step4PC.set_color_by_tex("a", RED)
        step4PC.set_color_by_tex("b", BLUE)
        
        stepPascal = MathTex(r"\text{Pascal's Identity: } {n \choose k-1} + {n \choose k} = {n+1 \choose k}")
        stepPascal.color = GOLD
        
        stepFinal = MathTex(
            r"=a^{n+1} + {n+1 \choose 1} a^n b +  \cdots + {n+1 \choose n}ab^n + b^{n+1}",
            substrings_to_isolate = "a" + "b"
            )
        stepFinal.set_color_by_tex("a", RED)
        stepFinal.set_color_by_tex("b", BLUE)
        
        stepSummation = MathTex(
            r"= \sum_{k=0}^{n+1} a^k b^{n+1-k}",
            substrings_to_isolate = "a" + "b")
        stepSummation.set_color_by_tex("a", RED)
        stepSummation.set_color_by_tex("b", BLUE)
        
        stepAll = VGroup(step4PA, step4PB, step4PC, stepPascal, stepFinal, stepSummation)
        stepAll.scale(0.3)
        stepAll.arrange(DOWN)
        stepAll.shift(0.375*UP)
        stepSummation.move_to(stepFinal)
        step4 = VGroup(step4PA, step4PB, step4PC)
        
        
        self.play(Write(step4))
        self.wait(1)
        self.play(Write(stepPascal))
        self.wait(1)
        self.play(FadeOut(stepPascal))
        self.play(Write(stepFinal.move_to(stepPascal)))
        self.wait(1)
        self.play(Write(stepSummation))
        self.wait(1)
        self.play(FadeOut(step3P2, step4PA, step4PB, step4PC, stepFinal))
        self.play(stepSummation.animate.move_to([0,0,0]))
        self.play(Circumscribe(stepSummation, color = GOLD))
        self.wait(1)
