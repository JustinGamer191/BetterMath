from manim import *


# --- SCENE 1: INTRODUCTION TO GRADIENT DESCENT ---
# Demonstrates the core optimization algorithm used in machine learning
class First(Scene):
    # Loss function to minimize (simple quadratic)
    # In real ML, this would be MSE, cross-entropy, etc.
    def func(self, x):
        return x**2  # Parabola with minimum at x=0

    def construct(self):
        # --- TITLE ---
        t = Text("How do Machine Learning algorithms learn?")
        t.scale(0.5)
        t.move_to([0, 3, 0])
        t.color = BLUE

        # --- MAIN CONCEPT: GRADIENT DESCENT ---
        t1 = Text("Gradient\nDescent")
        t1.scale(0.75)
        t1.move_to([0, 2, 0])
        t1.color = RED

        # --- LOSS FUNCTION VISUALIZATION ---
        # x-axis: model parameters (weights/biases)
        # y-axis: loss/error (what we want to minimize)
        axes = Axes(
            x_range=[-4, 4, 2], y_range=[-16, 16, 4], x_length=2, y_length=4, tips=False
        )
        axes.shift(DOWN)

        # Plot the loss function (convex parabola)
        # Real ML loss functions are often non-convex and high-dimensional
        graph = axes.plot(lambda x: x**2, color=BLUE)

        a = VGroup(axes, graph)

        self.play(Write(t))
        self.play(Write(t1))
        self.wait(1)

        # Show the loss landscape
        self.play(Create(a[0]))
        self.play(Create(a[1]))
        self.wait(1)

        # --- GRADIENT DESCENT ALGORITHM ---
        # Update rule: x_new = x_old - learning_rate * gradient
        # gradient = df/dx = 2x (derivative of x²)

        learning_rate = 0.3  # Step size (hyperparameter)

        # DEMONSTRATION 1: Starting from positive side
        x_val = 3.5  # Initial parameter value (far from optimum)
        dot = Dot(axes.c2p(x_val, self.func(x_val)), color=YELLOW)

        # Iteratively update parameters (4 steps)
        for _ in range(4):
            # Calculate gradient at current position
            grad = x_val * 2  # df/dx = 2x for f(x) = x²

            # Gradient descent update: move opposite to gradient direction
            x_new = x_val - learning_rate * grad  # Negative because we want to minimize

            new_dot = Dot(axes.c2p(x_new, self.func(x_new)), color=YELLOW)

            # Arrow shows direction and magnitude of update
            # Points "downhill" toward minimum
            arrow = Arrow(
                start=dot.get_center(), end=new_dot.get_center(), buff=0, color=RED
            )

            # Animate the parameter update
            self.play(GrowArrow(arrow), MoveAlongPath(dot, arrow), run_time=0.8)
            x_val = x_new  # Update for next iteration
            self.wait(0.25)
            self.remove(arrow)

        # DEMONSTRATION 2: Starting from negative side
        # Shows that gradient descent works from any starting point
        x_val = -3.5
        dot = Dot(axes.c2p(x_val, self.func(x_val)), color=YELLOW)

        for _ in range(4):
            grad = x_val * 2
            x_new = x_val - learning_rate * grad
            new_dot = Dot(axes.c2p(x_new, self.func(x_new)), color=YELLOW)

            arrow = Arrow(
                start=dot.get_center(), end=new_dot.get_center(), buff=0, color=RED
            )

            self.play(GrowArrow(arrow), MoveAlongPath(dot, arrow), run_time=0.8)
            x_val = x_new
            self.wait(0.25)
            self.remove(arrow)

        self.wait(1)

        # Both paths converge to x=0 (global minimum)
        # In practice, ML models have millions/billions of parameters!


# --- SCENE 2: MATHEMATICAL BACKGROUND ---
# Explains the gradient concept and shows gradient ASCENT
class Second(Scene):
    def func(self, x):
        return x**2

    def construct(self):
        # --- TITLE ---
        t1 = Text("Background:")
        t1.scale(0.5)
        t1.move_to([0, 3, 0])

        # --- GRADIENT DEFINITION ---
        # ∇f (del f or nabla f) is the gradient operator
        t2 = MathTex(r"\text{A gradient of a function f(x) is defined as}")
        t3 = MathTex(r"\text{a vector that points in the maximum}")
        t4 = MathTex(r"\text{ascent of the function and is denoted by }", r"\nabla f.")
        t4[1].color = GOLD  # Highlight gradient symbol ∇

        # --- PARTIAL DERIVATIVES ---
        # For multivariable functions f(x,y,z):
        # ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)
        # Each component is the rate of change in that direction
        t5 = MathTex(r"\text{It is found by taking the partial derivative}")
        t6 = MathTex(r"\text{with respect to each variable, treating the}")
        t7 = MathTex(r"\text{other variables as constant.}")

        t = VGroup(t2, t3, t4, t5, t6, t7)
        t.arrange(DOWN)
        t.scale(0.5)
        t.shift(1.75 * UP)

        self.play(Write(t1))
        self.play(Write(t2), Write(t3), Write(t4))
        self.play(Write(t5), Write(t6), Write(t7))
        self.wait(2)

        # --- VISUALIZATION: GRADIENT ASCENT ---
        axes = Axes(
            x_range=[-4, 4, 2], y_range=[-16, 16, 4], x_length=2, y_length=4, tips=False
        )
        axes.shift(1.75 * DOWN)
        graph = axes.plot(lambda x: x**2, color=BLUE)

        self.play(Create(axes))
        self.play(Create(graph))

        # --- GRADIENT ASCENT (UPHILL) ---
        # Shows what happens when following gradient instead of negative gradient
        learning_rate = 0.3
        x_val = 1  # Start near minimum
        dot = Dot(axes.c2p(x_val, self.func(x_val)), color=YELLOW)

        # Notice: x_new = x_val + learning_rate * grad (PLUS, not minus)
        # This climbs UP the function (opposite of what we want for optimization)
        for _ in range(3):
            grad = x_val * 2  # Gradient at current position

            # ASCENT: Move IN THE DIRECTION of gradient
            x_new = x_val + learning_rate * grad  # Positive = uphill

            new_dot = Dot(axes.c2p(x_new, self.func(x_new)), color=YELLOW)

            arrow = Arrow(
                start=dot.get_center(), end=new_dot.get_center(), buff=0, color=RED
            )

            # Arrow points uphill (toward maximum, away from minimum)
            self.play(GrowArrow(arrow), MoveAlongPath(dot, arrow), run_time=0.8)
            x_val = x_new
            self.wait(0.25)
            self.remove(arrow)

        self.wait(2)
        # Point: Gradient points uphill, so we need NEGATIVE gradient for optimization!


# --- SCENE 3: APPLICATION TO MACHINE LEARNING ---
# Connects gradient descent to actual ML training process
class Third(Scene):
    def construct(self):
        # --- GRADIENT DESCENT IN AI CONTEXT ---
        t1 = MathTex(r"\text{In the context of AI, rather than}")
        t2 = MathTex(r"\text{Gradient Ascent, Machine Learning models use}")

        # KEY POINT: We want to MINIMIZE loss, so we use negative gradient
        # Loss function measures how wrong the model's predictions are
        t3 = MathTex(r"\text{Gradient Descent, where taking the negative value}")
        t4 = MathTex(r"\text{of the gradient returns a vector of greatest descent.}")

        # LOSS FUNCTION: Measures prediction error
        # Common loss functions:
        # - Mean Squared Error (regression): L = (1/n)Σ(y_pred - y_true)²
        # - Cross-Entropy (classification): L = -Σy_true*log(y_pred)
        t5 = MathTex(r"\text{Usually, it's the gradient of some *loss function*.}")

        # --- LINEAR REGRESSION EXAMPLE ---
        # Model: y = mx + b (predict y given x)
        # Parameters to optimize: m (slope) and b (y-intercept)
        t6 = MathTex(r"\text{The most basic kind of Machine Learning model, a linear}")
        t7 = MathTex(r"\text{linear regression model, takes the gradient of the}")

        # MEAN SQUARED ERROR (MSE): L = (1/n)Σ(y_pred - y_true)²
        # Gradient tells us how to adjust m and b to reduce error
        # ∂L/∂m = how changing slope affects error
        # ∂L/∂b = how changing y-intercept affects error
        t8 = MathTex(r"\text{Mean Squared Error function and multiplies it by some}")

        # PARAMETER UPDATE RULE:
        # m_new = m_old - learning_rate * ∂L/∂m
        # b_new = b_old - learning_rate * ∂L/∂b
        # This iteratively improves the fit to training data
        t9 = MathTex(
            r"\text{learning rate to change the slope and y-intercept to reduce loss.}"
        )

        # Group and display gradient descent explanation
        t = VGroup(t1, t2, t3, t4, t5)
        t.arrange(DOWN)
        t.scale(0.5)
        t.shift(2.75 * UP)

        # Group and display linear regression example
        t1 = VGroup(t6, t7, t8, t9)
        t1.arrange(DOWN)
        t1.scale(0.5)
        t1.shift(1.125 * UP)

        self.play(Write(t))
        self.play(Write(t1))
        self.wait(1)

        # KEY TAKEAWAYS:
        # 1. Gradient descent is the fundamental optimization algorithm in ML
        # 2. It works by iteratively moving parameters opposite to the gradient
        # 3. Learning rate controls step size (too large = overshoot, too small = slow)
        # 4. Process: compute loss → compute gradient → update parameters → repeat
        # 5. Modern deep learning uses variants: SGD, Adam, RMSprop, etc.
