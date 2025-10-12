from manim import *

class First(Scene):
    def func(self, x):
        return x**2
    
    def construct(self):
        t = Text("How do Machine Learning algorithms learn?")
        t.scale(0.5)
        t.move_to([0,3,0])
        t.color = BLUE
        
        t1 = Text("Gradient\nDescent")
        t1.scale(0.75)
        t1.move_to([0,2,0])
        t1.color = RED
        
        axes = Axes(
            x_range = [-4,4,2],
            y_range = [-16,16,4],
            x_length = 2,
            y_length = 4,
            tips = False
        )
        axes.shift(DOWN)
        graph = axes.plot(lambda x:x**2, color = BLUE)            
        
        a=VGroup(axes,graph)
        
        self.play(Write(t))
        self.play(Write(t1))
        self.wait(1)
        
        self.play(Create(a[0]))
        self.play(Create(a[1]))
        self.wait(1)
        
        
        
        learning_rate = 0.3
        x_val = 3.5
        dot = Dot(axes.c2p(x_val, self.func(x_val)), color=YELLOW)
        for _ in range(4):
            grad = x_val * 2
            x_new = x_val - learning_rate * grad
            new_dot = Dot(axes.c2p(x_new, self.func(x_new)), color=YELLOW)

            arrow = Arrow(
                start=dot.get_center(),
                end=new_dot.get_center(),
                buff=0,
                color=RED
            )

            self.play(GrowArrow(arrow), MoveAlongPath(dot, arrow), run_time=0.8)
            x_val = x_new
            self.wait(0.25)
            self.remove(arrow)
        
        x_val = -3.5
        dot = Dot(axes.c2p(x_val, self.func(x_val)), color=YELLOW)
        for _ in range(4):
            grad = x_val * 2
            x_new = x_val - learning_rate * grad
            new_dot = Dot(axes.c2p(x_new, self.func(x_new)), color=YELLOW)

            arrow = Arrow(
                start=dot.get_center(),
                end=new_dot.get_center(),
                buff=0,
                color=RED
            )

            self.play(GrowArrow(arrow), MoveAlongPath(dot, arrow), run_time=0.8)
            x_val = x_new
            self.wait(0.25)
            self.remove(arrow)
            
        self.wait(1)

class Second(Scene):
    def func(self, x):
        return x**2
    def construct(self):
        t1 = Text("Background:")
        t1.scale(0.5)
        t1.move_to([0,3,0])
        
        t2 = MathTex(r"\text{A gradient of a function f(x) is defined as}")
        t3 = MathTex(r"\text{a vector that points in the maximum}")
        t4 = MathTex(r"\text{ascent of the function and is denoted by }", r"\nabla f.")
        t4[1].color = GOLD
        
        t5 = MathTex(r"\text{It is found by taking the partial derivative}")
        t6 = MathTex(r"\text{with respect to each variable, treating the}")
        t7 = MathTex(r"\text{other variables as constant.}")
        
        t=VGroup(t2,t3,t4,t5,t6,t7)
        t.arrange(DOWN)
        t.scale(0.5)
        t.shift(1.75*UP)
        
        self.play(Write(t1))
        self.play(Write(t2), Write(t3), Write(t4))
        self.play(Write(t5), Write(t6), Write(t7))
        self.wait(2)
        
        axes = Axes(
            x_range = [-4,4,2],
            y_range = [-16,16,4],
            x_length = 2,
            y_length = 4,
            tips = False
        )
        axes.shift(1.75*DOWN)
        graph = axes.plot(lambda x:x**2, color = BLUE)       
        
        self.play(Create(axes))
        self.play(Create(graph))     
        
        learning_rate = 0.3
        x_val = 1
        dot = Dot(axes.c2p(x_val, self.func(x_val)), color=YELLOW)
        for _ in range(3):
            grad = x_val * 2
            x_new = x_val + learning_rate * grad
            new_dot = Dot(axes.c2p(x_new, self.func(x_new)), color=YELLOW)

            arrow = Arrow(
                start=dot.get_center(),
                end=new_dot.get_center(),
                buff=0,
                color=RED
            )

            self.play(GrowArrow(arrow), MoveAlongPath(dot, arrow), run_time=0.8)
            x_val = x_new
            self.wait(0.25)
            self.remove(arrow)
        
        self.wait(2)
        
class Third(Scene):
    def construct(self):
        t1 = MathTex(r"\text{In the context of AI, rather than}")
        t2 = MathTex(r"\text{Gradient Ascent, Machine Learning models use}")
        t3 = MathTex(r"\text{Gradient Descent, where taking the negative value}")
        t4 = MathTex(r"\text{of the gradient returns a vector of greatest descent.}")
        t5 = MathTex(r"\text{Usually, it's the gradient of some *loss function*.}")
        
        t6 = MathTex(r"\text{The most basic kind of Machine Learning model, a linear}")
        t7 = MathTex(r"\text{linear regression model, takes the gradient of the}")
        t8 = MathTex(r"\text{Mean Squared Error function and multiplies it by some}")
        t9 = MathTex(r"\text{learning rate to change the slope and y-intercept to reduce loss.}")
        
        t=VGroup(t1,t2,t3, t4, t5)
        t.arrange(DOWN)
        t.scale(0.5)
        t.shift(2.75*UP)
        
        t1=VGroup(t6,t7,t8,t9)
        t1.arrange(DOWN)
        t1.scale(0.5)
        t1.shift(1.125*UP)
        
        self.play(Write(t))
        self.play(Write(t1))
        self.wait(1)