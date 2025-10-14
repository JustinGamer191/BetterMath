from manim import *
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\frac{\text{d}}{\text{dr}} \pi \text{r}^2 = 2 \pi \text{r}")
        textTop.scale(0.5)
        
        textTop[0][5:6].set_color(BLUE)
        textTop[0][10:11].set_color(BLUE)
        
        textTop[0][4:5].set_color(GOLD)
        textTop[0][9:10].set_color(GOLD)
        
        textTop[0][6:7].set_color(RED)
        textTop[0][8:9].set_color(RED)
        
        ##self.add(index_labels(textTop[0]))
        
        self.play(Write(textTop))
        self.play(textTop.animate.scale(4))
        self.play(textTop.animate.scale(0.25))
        self.play(textTop.animate.shift(2.5*UP))
        
        textArea = MathTex(r"\text{Derivate of Area of Circle}")
        textArea.color = GOLD
        eqSign = MathTex(r"=")
        textCircum = MathTex(r"\text{Circumference of Circle?}")
        textCircum.color = GOLD
        
        text = VGroup(textArea, eqSign, textCircum)
        text.scale(0.5)
        text.arrange(DOWN)
        text.shift(1.5*UP)
        
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(textTop, text))
        self.wait(0.25)
class Second(Scene):
    def construct(self):
        circle = Circle(color = RED)
        pO = np.array([0,0,0])
        pC = np.array([1,0,0])
        pdA = np.array([1.25,0,0])
        line = Line(pO, pC, color = BLUE)
        
        radius = MathTex(r"\text{r}")
        radius.scale(0.5)
        radius.next_to(line, 0.5*UP)
        
        self.play(Create(circle))
        self.play(Create(line), Write(radius))
        self.wait(0.25)
        
        diagram = VGroup(circle, line, radius)
        self.play(diagram.animate.shift(1.5*UP))
        
        eqArea = MathTex(r"\text{A} = \pi \text{r} ^2 ")
        eqArea[0][2:3].color = GOLD
        
        eqCirc = MathTex(r"\text{C} = 2 \pi \text{r}")
        eqCirc[0][3:4].color = GOLD
        
        eq = VGroup(eqArea, eqCirc)
        eq.scale(0.5)
        eq.arrange(DOWN)
        
        self.play(Write(eq))
        self.wait(1)
        
        self.play(eq.animate.shift(2*UP), diagram.animate.shift(1.5*DOWN))
        self.wait(1)
        
        textNew = MathTex(
            r"\text{Now imagine an infinitesimally length, dr}"
            )
        textNew[0][0:33].color = GOLD
        textNew[0][33:35].color = GREEN
        self.play(Write(textNew.scale(0.4).shift(1.5*DOWN)))
        
        lineA = Line(pC, pdA, color = BLUE)
        dr = MathTex(r"\text{dr}")
        dr.scale(0.25)
        dr.next_to(lineA, 0.5*UP)
        dr.color = GREEN
        circleDr = Circle(radius = 1.25, color = RED)
        
        self.play(Create(circleDr))
        self.play(Create(lineA), Write(dr))
        
        self.play(FadeOut(textNew))
        self.wait(1)
        
        textA = MathTex(r"\text{Change in Area} = 2 \pi \text{r} * \text{dr}")
        textA[0][0:12].color = GOLD
        textA[0][14:15].color = GOLD
        textA[0][17:19].color = GREEN
        textA.scale(0.5)
        textA.shift(1.5*DOWN)
        self.play(Write(textA))
        self.wait(1)
        
        textReplace = MathTex(r"\text{dA}")
        textReplace.color = GOLD
        textReplace.scale(0.5).shift(1.5*DOWN)
        self.play(Transform(textA[0][0:12], textReplace))
        self.play(textA.animate.shift(0.65*LEFT))
        self.wait(1)
        self.play(FadeOut(textA, diagram, circleDr, lineA, dr, eqArea, eqCirc))
        
class Third(Scene):
    def construct(self):
        finalT = MathTex(r"\text{dA} = 2 \pi \text{r} * \text{dr}")
        finalT[0][0:2].color = GOLD
        finalT[0][4:5].color = GOLD
        finalT[0][7:9].color = GREEN
        
        finalSimp = MathTex(r"\frac{\text{dA}}{\text{dr}} = 2 \pi \text{r} ")
        finalSimp[0][0:2].color = GOLD
        finalSimp[0][3:5].color = GREEN
        finalSimp[0][7:8].color = GOLD
        
        finalFinal = MathTex(r"\frac{\text{d}}{\text{dr}} \text{A} = 2 \pi \text{r}")
        finalFinal[0][0:1].color = GOLD
        finalFinal[0][2:4].color = GREEN
        finalFinal[0][4:5].color = GOLD
        finalFinal[0][7:8].color = GOLD
        
        finalFF = MathTex(r"\frac{\text{d}}{\text{dr}} \pi \text{r}^2 = 2 \pi \text{r}")
        finalFF[0][0:1].color = GOLD
        finalFF[0][2:4].color = GREEN
        finalFF[0][4:5].color = GOLD
        finalFF[0][9:10].color = GOLD
        
        text = VGroup(finalT, finalSimp, finalFinal, finalFF)
        text.scale(0.5)
        text.arrange(DOWN)
        
        self.play(Write(finalT))
        self.play(Write(finalSimp))
        self.play(Write(finalFinal))
        self.play(Write(finalFF))
        self.wait(1)
        self.play(FadeOut(finalT, finalSimp, finalFinal))
        self.play(finalFF.animate.shift(UP))
        self.play(finalFF.animate.scale(4))
        self.play(finalFF.animate.scale(0.25))