from manim import *
import math

class Cover(Scene):
    def construct(self):
        textTop = MathTex(r"\text{King's Property of Integration}")
        textTop.color = GOLD
        
        textMid = MathTex(
            r"\int_{a}^{b} f(x) = \int_{a}^{b} f(a+b-x)"
            )
        textMid[0][1:2].color = BLUE
        textMid[0][2:3].color = RED
        textMid[0][5:6].color = GREEN
        
        textMid[0][9:10].color = BLUE
        textMid[0][10:11].color = RED
        textMid[0][13:14].color = RED
        textMid[0][15:16].color = BLUE
        textMid[0][17:18].color = GREEN
        
        text = VGroup(textTop, textMid)
        text.scale(0.5)
        text.arrange(DOWN)
        self.play(Write(text))
        self.play(FadeOut(textTop))
        self.play(textMid.animate.move_to([0,2.75,0]))
        self.wait(1)

class Second(Scene):
    def construct(self):
        textOld = MathTex(r"\int_{a}^{b} f(x) = \int_{a}^{b} f(a+b-x)").scale(0.5)
        textOld[0][1:2].color = BLUE
        textOld[0][2:3].color = RED
        textOld[0][5:6].color = GREEN
        textOld[0][9:10].color = BLUE
        textOld[0][10:11].color = RED
        textOld[0][13:14].color = RED
        textOld[0][15:16].color = BLUE
        textOld[0][17:18].color = GREEN
        textOld.move_to([0,2.75,0])
        
        self.add(textOld)
        
        ##NEW
        grid = Axes(
            x_range = [1,4,1],
            y_range = [0,64,16],
            x_length = 2.5,
            y_length = 4,
            tips = False
        )
        
        parentF = grid.plot(
            lambda x: x**3,
            x_range = [1,4],
            color = RED
        )
        
        parentL = MathTex(
            r"f(x) = x^3",
            substrings_to_isolate= "x"
            )
        parentL.set_color_by_tex("x", RED)
        
        parentInt = MathTex(
            r"\int_{1}^{4} x^3 dx",
            substrings_to_isolate= "x"
            )
        parentInt.set_color_by_tex("x", RED)
        
        parentLabel = VGroup(parentL, parentInt)
        parentLabel.scale(0.5)
        parentLabel.arrange(DOWN)
        parentLabel.move_to([0,1.5,0])
        
        labelBgL = BackgroundRectangle(parentL, color = BLACK)
        labelBgInt = BackgroundRectangle(parentInt, color = BLACK)
        
        p1 = VGroup(labelBgL, parentL)
        p2 = VGroup(labelBgInt, parentInt)
        
        parentArea = grid.get_area(graph = parentF, x_range = [1,4], color = RED)
        
        
        
        kingF = grid.plot(
            lambda x: (5-x)**3,
            x_range = [1,4],
            color = BLUE
        )
        kingL = MathTex(
            r"f(x) = (5-x)^3",
            substrings_to_isolate= "x"
            )
        kingL.set_color_by_tex("x", BLUE)
        
        kingInt = MathTex(
            r"\int_{1}^{4} (5-x)^3 dx",
            substrings_to_isolate= "x"
            )
        kingInt.set_color_by_tex("x", BLUE)
        
        kingLabel = VGroup(kingL, kingInt)
        kingLabel.scale(0.5)
        kingLabel.arrange(DOWN)
        kingLabel.move_to([0,0,0])
        
        labelKL = BackgroundRectangle(kingL, color = BLACK, fill_opacity = 1)
        labelKInt = BackgroundRectangle(kingInt, color = BLACK, fill_opacity= 1)
        
        pK1 = VGroup(labelKL, kingL)
        pK2 = VGroup(labelKInt, kingInt)
        
        kingArea = grid.get_area(graph = kingF, x_range = [1,4], color = BLUE)
        
        self.play(Write(grid))
        self.play(Create(parentF))
        self.play(Write(parentArea))
        self.play(Write(p1))
        self.play(Write(p2))
        
        self.play(Create(kingF))
        self.play(Write(kingArea))
        self.play(Write(pK1))
        self.play(Write(pK2))
        self.wait(2)
        
class Third(Scene):
    def construct(self):
        textOld = MathTex(r"\int_{a}^{b} f(x) = \int_{a}^{b} f(a+b-x)").scale(0.5)
        textOld[0][1:2].color = BLUE
        textOld[0][2:3].color = RED
        textOld[0][5:6].color = GREEN
        textOld[0][9:10].color = BLUE
        textOld[0][10:11].color = RED
        textOld[0][13:14].color = RED
        textOld[0][15:16].color = BLUE
        textOld[0][17:18].color = GREEN
        textOld.move_to([0,2.75,0])
        
        grid = Axes(
            x_range = [1,4,1],
            y_range = [0,64,16],
            x_length = 2.5,
            y_length = 4,
            tips = False
        )
        
        parentF = grid.plot(
            lambda x: x**3,
            x_range = [1,4],
            color = RED
        )
        
        parentL = MathTex(
            r"f(x) = x^3",
            substrings_to_isolate= "x"
            )
        parentL.set_color_by_tex("x", RED)
        
        parentInt = MathTex(
            r"\int_{1}^{4} x^3 dx",
            substrings_to_isolate= "x"
            )
        parentInt.set_color_by_tex("x", RED)
        
        parentLabel = VGroup(parentL, parentInt)
        parentLabel.scale(0.5)
        parentLabel.arrange(DOWN)
        parentLabel.move_to([0,1.5,0])
        
        labelBgL = BackgroundRectangle(parentL, color = BLACK)
        labelBgInt = BackgroundRectangle(parentInt, color = BLACK)
        
        p1 = VGroup(labelBgL, parentL)
        p2 = VGroup(labelBgInt, parentInt)
        
        parentArea = grid.get_area(graph = parentF, x_range = [1,4], color = RED)
        
        
        
        kingF = grid.plot(
            lambda x: (5-x)**3,
            x_range = [1,4],
            color = BLUE
        )
        kingL = MathTex(
            r"f(x) = (5-x)^3",
            substrings_to_isolate= "x"
            )
        kingL.set_color_by_tex("x", BLUE)
        
        kingInt = MathTex(
            r"\int_{1}^{4} (5-x)^3 dx",
            substrings_to_isolate= "x"
            )
        kingInt.set_color_by_tex("x", BLUE)
        
        kingLabel = VGroup(kingL, kingInt)
        kingLabel.scale(0.5)
        kingLabel.arrange(DOWN)
        kingLabel.move_to([0,0,0])
        
        labelKL = BackgroundRectangle(kingL, color = BLACK, fill_opacity = 1)
        labelKInt = BackgroundRectangle(kingInt, color = BLACK, fill_opacity= 1)
        
        pK1 = VGroup(labelKL, kingL)
        pK2 = VGroup(labelKInt, kingInt)
        
        kingArea = grid.get_area(graph = kingF, x_range = [1,4], color = BLUE)
        
        allStuff = VGroup(textOld, grid, parentF, parentArea, p1, p2, kingF, kingArea, pK1, pK2)
        allAnim = VGroup(grid, parentF, parentArea, p1, p2, kingF, kingArea, pK1, pK2)
        self.add(allStuff)
        
        ##NEW
        pInt = MathTex(
            r"\int_{1}^{4} x^3 dx = \frac{255}{4}",
            )
        pInt[0][3:4].color = RED
        pInt[0][6:7].color = RED
        pInt[0][8:13].color = GOLD
        
        kInt = MathTex(
            r"\int_{1}^{4} (5-x)^3 dx = \frac{255}{4}",
        )
        kInt[0][6:7].color = BLUE
        kInt[0][10:11].color = BLUE
        kInt[0][12:17].color = GOLD
        
        textAll = VGroup(pInt, kInt)
        textAll.scale(0.5)
        textAll.arrange(DOWN)
        textAll.move_to([0,-1,0])
        
        textConc = MathTex(r"\text{In Conclusion:}")
        textFinal = MathTex(r"\text{Area under curve is same regardless if}")
        textFinal2 = MathTex(r"\text{calculating left to right or right to left.}")
        
        textFin = VGroup(textConc, textFinal, textFinal2)
        textFin.scale(0.4)
        textFin.arrange(DOWN)
        textFin.color = GOLD
        
        self.play(allAnim.animate.scale(0.5).shift(UP))
        self.play(Write(pInt))
        self.play(Write(kInt))
        self.play(FadeOut(allAnim))
        self.play(textAll.animate.move_to([0,1.5,0]))
        self.wait(1)
        self.play(Write(textFin))
        self.play(FadeOut(kInt[0][0:12]), FadeOut(pInt[0][0:8]))
        self.play(pInt[0][8:13].animate.move_to([0,1.25,0]), kInt[0][12:17].animate.move_to([0,1.25,0]))
        self.play(FadeOut(pInt[0][8:13]), FadeOut(kInt[0][12:17]), FadeOut(textOld))
        self.play(Circumscribe(textFin, color = GOLD))
        self.wait(1)