from manim import *
import numpy as np


# --- LINEAR REGRESSION VISUALIZATION ---
# Demonstrates the gradient descent algorithm fitting a line to data points
# This is the foundation of machine learning - finding patterns in data
class LinearRegressionScene(Scene):
    def construct(self):
        # --- TITLE ---
        t1 = MathTex(r"\text{Linear Regression}")
        t1.move_to([0, 2.5, 0])
        t1.color = RED
        self.play(Write(t1))

        # --- COORDINATE SYSTEM ---
        # x-axis: independent variable (features)
        # y-axis: dependent variable (target/prediction)
        axes = Axes(x_range=[0, 2], y_range=[0, 2], tips=False, y_length=4, x_length=5)

        self.play(Write(axes))

        # --- GENERATE SYNTHETIC DATASET ---
        # Creating artificial data that follows a linear relationship with noise
        # True relationship: y = 4 + 3x + noise
        # This simulates real-world data where there's a linear trend plus random variation

        ##np.random.seed(42)  # Uncomment for reproducible results

        # Generate 100 random x values between 0 and 2
        X = 2 * np.random.rand(100, 1)

        # Generate y values following linear relationship y = 4 + 3x
        # np.random.randn adds Gaussian noise (simulates measurement error)
        y = 4 + 3 * X + np.random.randn(100, 1)

        # Flatten arrays for easier indexing
        X = X.flatten()
        y = y.flatten()

        # --- SCALE DATA TO FIT SCREEN ---
        # Transform data points to visible coordinate range
        # Maps data to [-2, 2] for x and [-1.5, 1.5] for y
        # This is feature scaling (normalization)
        X_scaled = 4 * (X - np.min(X)) / (np.max(X) - np.min(X)) - 2
        y_scaled = 3 * (y - np.min(y)) / (np.max(y) - np.min(y)) - 1.5

        # Create visual representation of data points
        points = VGroup(
            *[
                Dot(point=np.array([X_scaled[i], y_scaled[i], 0]), color=BLUE)
                for i in range(len(X))
            ]
        )

        # Display the scatter plot
        self.play(Create(points))

        # --- INITIALIZE REGRESSION LINE ---
        # MODEL: y = mx + b
        # m = slope (how much y changes per unit change in x)
        # b = y-intercept (value of y when x = 0)
        # Start with a horizontal line (m=0, b=0) - a poor initial guess
        line = Line(start=np.array([-3, 0, 0]), end=np.array([3, 0, 0]), color=RED)
        line.stroke_width = 8
        self.play(Create(line))

        # --- GRADIENT DESCENT PARAMETERS ---
        # Initialize parameters randomly (could also use zeros)
        m, b = np.random.randn(), np.random.randn()  # Random starting point

        # LEARNING RATE (α): Controls step size in parameter updates
        # Too large → overshooting/divergence
        # Too small → slow convergence
        learning_rate = 0.1

        # EPOCHS: Number of complete passes through the data
        # More epochs → better fit (up to a point, then overfitting can occur)
        epochs = 30

        # --- GRADIENT DESCENT TRAINING LOOP ---
        # Iteratively improves the line fit by minimizing Mean Squared Error (MSE)
        for _ in range(epochs):
            # STEP 1: FORWARD PASS - Make predictions
            # y_pred = mx + b for all data points
            y_pred = m * X_scaled + b

            # STEP 2: COMPUTE GRADIENTS - How to adjust parameters
            # LOSS FUNCTION: MSE = (1/n)Σ(y_pred - y_true)²
            #
            # Gradient of MSE with respect to slope m:
            # ∂(MSE)/∂m = (2/n)Σ(y_pred - y_true) * x
            # This tells us how changing m affects the error
            dm = (2 / len(X)) * np.sum((y_pred - y_scaled) * X)

            # Gradient of MSE with respect to intercept b:
            # ∂(MSE)/∂b = (2/n)Σ(y_pred - y_true)
            # This tells us how changing b affects the error
            db = (2 / len(X)) * np.sum(y_pred - y_scaled)

            # STEP 3: UPDATE PARAMETERS - Gradient descent step
            # Move parameters in opposite direction of gradient (downhill)
            # New value = Old value - learning_rate × gradient
            m -= learning_rate * dm  # Update slope
            b -= learning_rate * db  # Update intercept

            # --- ANIMATE THE LINE MOVING TO NEW POSITION ---
            # Calculate new line endpoints using updated parameters
            # Line equation: y = mx + b
            # At x = -3: y = m(-3) + b
            # At x = 3: y = m(3) + b
            new_start = np.array([-3, m * -3 + b, 0])
            new_end = np.array([3, m * 3 + b, 0])

            # Smoothly transition the line to the new position
            # This visualizes the learning process in real-time
            self.play(
                line.animate.put_start_and_end_on(new_start, new_end), run_time=0.3
            )

        # Final fitted line minimizes the sum of squared distances to all points
        self.wait(2)
