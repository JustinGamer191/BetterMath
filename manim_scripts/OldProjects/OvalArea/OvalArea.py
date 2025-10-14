from manim import*
import math

class Oval(Scene):
    def construct(self):
        circle = Circle()
        circleOriginal = Circle()
        circleOriginal.stretch(2,1)
        textTop = MathTex(r"\text{Area:}")
        textTop.scale(0.5)
        textLow = MathTex(r"\text{Oval}")
        textLow.scale(0.5)
        
        textAll = VGroup(textTop, textLow)
        textAll.arrange(DOWN)        
        for letter in textAll:
            letter.set_color(random_bright_color())
        
        self.play(Create(circle))
        self.play(Write(textTop))
        self.play(circle.animate.stretch(2,1))
        self.play(Transform(circle, textLow[0][0]))
        self.play(Write(textLow[0][1:4]))
        self.play(FadeOut(textTop), FadeOut(textLow[0][1:4]))
        self.play(Transform(circle, circleOriginal))
        self.play(circle.animate.stretch(0.5,1))
        self.wait(1)

class Exp(Scene):
    def construct(self):
        circle = Circle()
        textFirst = Text("Take a Unit Circle")
        textFirst.scale(0.75)
        
        for letter in textFirst:
            letter.set_color(random_bright_color())
        
        textNext = MathTex(
            r"\text{Area} = \pi r^2 = \pi"
            )
        textNext[0][5:6].color = GOLD
        textNext[0][9:10].color = GOLD
        line = Line([0,0,0], [1,0,0])
        lineL = MathTex(r"1")
        lineL.move_to(line)
        lineL.shift(0.25*UP)
        lineL.scale(0.55)
        
        text = VGroup(textFirst, textNext)
        text.scale(0.4)
        text.arrange(DOWN)
        
        textHori = MathTex(r"\text{Horizontally Strecth: a}")
        for letter in textHori:
            letter.set_color(random_bright_color())
        textHori.scale(0.4)
        textHori.move_to([0,-1.5,0])
        
        textVert = MathTex(r"\text{Vertically Strecth: b}")
        for letter in textVert:
            letter.set_color(random_bright_color())
        textVert.scale(0.4)
        textVert.move_to([0,-2,0])
        
        lineVert = Line([0,0,0], [0,0.75,0])
        vertL = MathTex(r"\text{b}")
        vertL.scale(0.55)
        vertL.move_to([0.15,0.375,0])
        
        labelA = MathTex(r"a")
        labelA.scale(0.55)
        labelA.move_to([0.75,0.25,0])
        circL = VGroup(circle, line, lineL)
        
        area1 = MathTex(r"\text{Area} = a \pi")

        area2 = MathTex(r"\text{Area} = ab \pi")

        
        areaChange = VGroup(area1, area2)
        areaChange.scale(0.5)
        for letter in areaChange:
            letter.set_color(random_bright_color())
        
        self.add(circle)
        self.play(Write(textFirst))
        self.play(Write(textNext))
        self.play(text.animate.move_to([0,2,0]))
        self.play(Create(line))
        self.play(Write(lineL))
        
        area1.move_to(textNext)
        area2.move_to(textNext)
        
        self.play(Write(textHori))
        self.play(circL.animate.stretch(1.5,0), Transform(lineL, labelA))
        self.play(Transform(textNext, area1))
        self.play(Write(textVert))
        self.play(circle.animate.stretch(0.75,1), Create(lineVert), Write(vertL))
        self.play(Transform(textNext, area2))
        self.wait(1)