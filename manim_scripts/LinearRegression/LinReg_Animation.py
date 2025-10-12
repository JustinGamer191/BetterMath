from manim import*
import numpy as np

class LinearRegressionScene(Scene):
    def construct(self):
        t1 = MathTex(r"\text{Linear Regression}")
        t1.move_to([0,2.5,0])
        t1.color = RED
        self.play(Write(t1))

        axes = Axes(
            x_range=[0, 2],
            y_range=[0, 2],
            tips = False,
            y_length = 4,
            x_length = 5
        )
        
        self.play(Write(axes))

        ##np.random.seed(42)
        X = 2 * np.random.rand(100, 1)
        y = 4 + 3 * X + np.random.randn(100, 1)

        X = X.flatten()
        y = y.flatten()
        
        X_scaled = 4 * (X - np.min(X)) / (np.max(X) - np.min(X)) - 2
        y_scaled = 3 * (y - np.min(y)) / (np.max(y) - np.min(y)) - 1.5

        points = VGroup(*[
            Dot(point=np.array([X_scaled[i], y_scaled[i], 0]), color=BLUE)
            for i in range(len(X))
        ])

        self.play(Create(points))

        line = Line(start=np.array([-3, 0, 0]), end=np.array([3, 0, 0]), color=RED)
        line.stroke_width = 8
        self.play(Create(line))

        m, b = np.random.randn(), np.random.randn()
        learning_rate = 0.1
        epochs = 30
        
        for _ in range(epochs):
            y_pred = m * X_scaled + b
            dm = (2 / len(X)) * np.sum((y_pred - y_scaled) * X)
            db = (2 / len(X)) * np.sum(y_pred - y_scaled)
            m -= learning_rate * dm
            b -= learning_rate * db

            new_start = np.array([-3, m * -3 + b, 0])
            new_end = np.array([3, m * 3 + b, 0])
            self.play(line.animate.put_start_and_end_on(new_start, new_end), run_time=0.3)

        self.wait(2)