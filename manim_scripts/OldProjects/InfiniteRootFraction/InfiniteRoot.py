from manim import *
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\sqrt{2}")
        textTop[0][2:3].color = BLUE
        
        textMid = MathTex(r"=")
        textMid.color = GOLD
        
        textBot = MathTex(
            r"1 +", r"{1", r"\over", r"2 + " , r"{1", r"\over", r"2 +", r"{1", r"\over", r"2 + \cdots}}}",
            substrings_to_isolate = "1" + "2"
            )
        textBot.set_color_by_tex("1", RED)
        textBot.set_color_by_tex("2", BLUE)
        
        text = VGroup(textTop, textMid, textBot)
        text.scale(0.5)
        text.arrange(DOWN)
        
        self.play(Write(textTop))
        self.play(Write(textMid))
        self.play(Write(textBot))
        self.wait(1)
        
        self.play(FadeOut(textMid, textBot))
        self.play(textTop.animate.move_to([0,0,0]))
        self.wait(1)
        
class Second(Scene):
    def construct(self):
        textRoot = MathTex(r"\sqrt{2}")
        textRoot[0][2:3].color = BLUE
        textRoot.scale(0.5)
        self.add(textRoot)
        
        ##NEW
        eqAdd = MathTex(r"\sqrt{2} - 1 = ", r"\sqrt{2} - 1")
        eqAdd[0][2:3].color = BLUE
        eqAdd[1][2:3].color = BLUE
        eqAdd[0][4:5].color = RED
        eqAdd[1][4:5].color = RED
        eqAdd.scale(0.5)
        
        plus = MathTex(r"+").scale(0.5)
        
        inFrac = MathTex(r"\frac{1}{\sqrt{2}+1}")
        inFrac[0][4:5].color = BLUE
        inFrac[0][0:1].color = RED
        inFrac[0][6:7].color = RED
        inFrac.scale(0.5)
        
        repFrac = MathTex(r"\frac{1}{2+\sqrt{2}-1}")
        repFrac[0][0:1].color = RED
        repFrac[0][2:3].color = BLUE
        repFrac[0][6:7].color = BLUE
        repFrac[0][8:9].color = RED
        repFrac.scale(0.5)
        
        inFracOG = MathTex(r"\frac{1}{\sqrt{2}+1}")
        inFracOG[0][4:5].color = BLUE
        inFracOG[0][0:1].color = RED
        inFracOG[0][6:7].color = RED
        inFracOG.scale(0.5)
        
        dots = MathTex(r"2 + \cdots")
        dots[0][0:1].color = BLUE
        dots.scale(0.5)
        
        allStuff = VGroup(textRoot, eqAdd[0], repFrac, plus)
        
        self.play(textRoot.animate.move_to(eqAdd[0][0:2]))
        self.play(Write(eqAdd[0][3:6]), Write(eqAdd[1][0:5]))
        self.wait(1)
        self.play(FadeOut(eqAdd[0][3:4]), eqAdd[0][5:6].animate.move_to(eqAdd[0][3:4]), FadeIn(plus.move_to(eqAdd[0][5:6])))
        self.wait(1)
        self.play(Transform(eqAdd[1], inFrac.move_to(eqAdd[1]), replace_mobject_with_target_in_scene=True))
        self.wait(1)
        self.play(Transform(inFrac, repFrac.move_to([0.75,0,0]), replace_mobject_with_target_in_scene=True))
        self.wait(1)
        self.play(allStuff.animate.move_to([0,0,0]))
        self.play(Transform(repFrac[0][4:9], inFracOG.move_to(repFrac[0][4:9]).shift(0.2*DOWN), replace_mobject_with_target_in_scene=True))
        self.wait(1)
        self.play(Transform(inFracOG[0][2:7], dots.move_to(inFracOG[0][2:7])))
        self.wait(2)