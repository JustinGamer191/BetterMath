from manim import*
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\text{Euler's Identity}")
        textTop.color = GOLD
        
        textBot = MathTex(r"e^{\pi i} + 1 = 0")
        textBot[0][1:2].color = GOLD
        textBot[0][4:5].color = RED
        textBot[0][6:7].color = BLUE
        
        text = VGroup(textTop, textBot)
        text.scale(0.5)
        text.arrange(DOWN)
        
        textWhy = MathTex(r"\text{Why?}")
        textWhy.color = GOLD
        textWhy.scale(0.5)
        
        self.play(Write(text))
        self.play(FadeOut(text))
        self.play(Write(textWhy))
        self.play(FadeOut(textWhy))
        self.wait(0.5)

class Second(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Let } z = a+bi")
        t2 = MathTex(r"\text{In polar:}")
        t2.color = GOLD
        t3 = MathTex(r"z = r(\text{cos}(\theta) + i\text{sin}(\theta))")
        t3[0][8:9].color = GOLD
        t3[0][16:17].color = GOLD
        
        tAll = VGroup(t1,t2,t3)
        tAll.scale(0.5)
        tAll.arrange(DOWN)
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(FadeOut(t1,t2))
        self.play(t3.animate.move_to([0,2.5,0]))
        self.wait(1)

class Third(Scene):
    def construct(self):
        t3 = MathTex(r"z = r(\text{cos}(\theta) + i\text{sin}(\theta))")
        t3[0][8:9].color = GOLD
        t3[0][16:17].color = GOLD
        t3.scale(0.5)
        t3.move_to([0,2.5,0])
        
        t4 = MathTex(r"\text{Taylor Series for cos} (\theta)")
        t4[0][19:20].color = GOLD
        t5 = MathTex(r"1 - \frac{{\theta}^2}{2!} + \frac{{\theta}^4}{4!} - \cdots")
        t5[0][2:3].color = GOLD
        t5[0][8:9].color = GOLD
        
        t6 = MathTex(r"\text{Taylor Series for } i \text{sin} (\theta)")
        t6[0][20:21].color = GOLD
        t7 = MathTex(r"\theta i - \frac{{\theta}^3}{3!} i + \frac{{\theta}^5}{5!} i - \cdots")
        t7[0][0:1].color = GOLD
        t7[0][3:4].color = GOLD
        t7[0][10:11].color = GOLD
        
        t8 = MathTex(r"\text{cos}(\theta) + i\text{sin}(\theta) =")
        t8[0][4:5].color = GOLD
        t8[0][12:13].color = GOLD
        t9 = MathTex(r"1 + \theta i - \frac{{\theta}^2}{2!} - \frac{{\theta}^3}{3!} + ...")
        t9[0][2:3].color = GOLD
        t9[0][5:6].color = GOLD
        t9[0][11:12].color = GOLD
        
        tAll = VGroup(t4,t5,t6,t7,t8,t9)
        tAll.scale(0.5)
        tAll.arrange(DOWN)
        tAll.shift(0.25*UP)
        
        f1 = VGroup(t4,t5)
        f2 = VGroup(t6,t7)
        f3 = VGroup(t8,t9)
        
        self.add(t3)
        self.play(Write(f1))
        self.play(Write(f2))
        self.play(Write(f3))
        self.wait(1)
        self.play(FadeOut(t3,t4,t5,t6,t7))
        self.play(f3.animate.move_to([0,2.5,0]))
        self.wait(1)

class Final(Scene):
    def construct(self):
        t8 = MathTex(r"\text{cos}(\theta) + i\text{sin}(\theta) =")
        t8[0][4:5].color = GOLD
        t8[0][12:13].color = GOLD
        t9 = MathTex(r"1 + \theta i - \frac{{\theta}^2}{2!} - \frac{{\theta}^3}{3!} + ...")
        t9[0][2:3].color = GOLD
        t9[0][5:6].color = GOLD
        t9[0][11:12].color = GOLD
        f3 = VGroup(t8,t9)
        f3.scale(0.5)
        f3.arrange(DOWN)
        f3.move_to([0,2.5,0])
        
        t10 = MathTex(r"\text{Taylor Series for } e^x")
        t10[0][16:17].color = GOLD
        t11 = MathTex(
            r"1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + ..."
            )
        t11[0][2:3].color = GOLD
        t11[0][4:5].color = GOLD
        t11[0][10:11].color = GOLD
        t12 = MathTex(r"e^{i \theta} =")
        t12[0][2:3].color = GOLD
        t13 = MathTex(r"1 + \theta i - \frac{{\theta}^2}{2!} - \frac{{\theta}^3}{3!} + ...")
        t13[0][2:3].color = GOLD
        t13[0][5:6].color = GOLD
        t13[0][11:12].color = GOLD
        t14 = MathTex(r"= \text{cos} (\theta) + i \text{sin} (\theta)")
        t14[0][5:6].color = GOLD
        t14[0][13:14].color = GOLD
        
        tAll = VGroup(t10,t11,t12,t13,t14)
        tAll.scale(0.5)
        tAll.arrange(DOWN)
        tAll.shift(0.25*UP)
        
        f1 = VGroup(t10,t11)
        f2 = VGroup(t12,t13,t14)
        
        t15 = MathTex(r"e^{i \theta} = \text{cos}(\theta) + i\text{sin}(\theta)")
        t15[0][2:3].color = GOLD
        t15[0][8:9].color = GOLD
        t15[0][16:17].color = GOLD
        
        t16 = MathTex(r"e^{\pi i} = \text{cos}(\pi) + i \text{sin} (\pi)")
        t16[0][1:2].color = GOLD
        t16[0][8:9].color = GOLD
        t16[0][16:17].color = GOLD
        
        t17 = MathTex(r"e^{\pi i} = -1")
        t17[0][1:2].color = GOLD
        t17[0][4:6].color = RED
        
        t18 = MathTex(r"e^{\pi i} + 1 = 0")
        t18[0][1:2].color = GOLD
        t18[0][4:5].color = RED
        t18[0][6:7].color = BLUE
        
        ff = VGroup(t15,t16,t17,t18)
        ff.scale(0.5)
        ff.arrange(DOWN)
        ff.shift(0.5*DOWN)
        
        self.add(f3)
        self.play(Write(f1))
        self.wait(1)
        self.play(Write(f2))
        self.wait(1)
        self.play(FadeOut(f3, f1))
        self.play(f2.animate.move_to([0,1.5,0]))
        self.wait(1)
        self.play(Write(t15))
        self.play(Write(t16))
        self.play(Write(t17))
        self.play(Write(t18))
        self.wait(1)
        self.play(FadeOut(f2,t15,t16,t17))
        self.play(t18.animate.move_to([0,0,0]))
        self.play(Circumscribe(t18, color = GOLD))
        self.wait(1)