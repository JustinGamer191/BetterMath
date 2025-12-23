from manim import *


# --- SCENE 1: CLASSIFICATION DEMO ---
# Simple demonstration of binary classification (dog vs cat)
# Brilliant.org Partnership Video #3
class Classification(Scene):
    def construct(self):
        # Introduction
        t1 = MathTex(r"\text{Dog}", r"\text{Cat}")
        t1.scale(0.5)

        t1[0].move_to([-1, 2, 0])  # Dog label (left)
        t1[1].move_to([1, 2, 0])  # Cat label (right)

        self.add(t1)

        # Picture of cat
        Image = ImageMobject("./Cat.png")

        # Hard for computers, easy for humans.
        t2 = MathTex(r"?")
        t2.scale(10)
        t2.color = RED

        # --- ANIMATION: CLASSIFICATION PROCESS ---
        self.add(Image)
        self.play(Write(t1))
        self.wait()
        self.play(Circumscribe(t1[1]))
        self.wait()
        self.play(Write(t2))
        self.wait()


# --- SCENE 2: CLUSTERING VS CLASSIFICATION ---
# Comprehensive demonstration of two fundamental machine learning paradigms
class ClusteringAndClassification(Scene):
    def construct(self):
        # --- TITLE ---
        title = Text("Data Analysis: Clustering vs Classification", font_size=40)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Part 1: Demonstrate CLUSTERING (unsupervised)
        self.clustering_demo()
        self.wait(2)
        self.clear()

        # Part 2: Demonstrate CLASSIFICATION (supervised)
        self.classification_demo()

    # --- CLUSTERING: UNSUPERVISED LEARNING ---
    # Goal: Discover hidden structure in unlabeled data
    # Algorithm finds natural groupings without being told what to look for
    def clustering_demo(self):
        # --- TITLE ---
        cluster_title = Text("Clustering: Unsupervised Learning", font_size=36)
        cluster_title.to_edge(UP)
        self.play(Write(cluster_title))

        # Subtitle explaining the concept
        subtitle = Text("Finding natural groups in data", font_size=24, color=YELLOW)
        subtitle.next_to(cluster_title, DOWN)
        self.play(FadeIn(subtitle))
        self.wait(1)

        # --- GENERATE SYNTHETIC DATA ---
        # Create 3 distinct clusters in 2D space
        np.random.seed(42)  # For reproducibility

        # Cluster 1: Center at (-2, 1)
        cluster1 = np.random.randn(15, 2) * 0.5 + np.array([-2, 1])

        # Cluster 2: Center at (2, 1.5)
        cluster2 = np.random.randn(15, 2) * 0.5 + np.array([2, 1.5])

        # Cluster 3: Center at (0, -1.5)
        cluster3 = np.random.randn(15, 2) * 0.5 + np.array([0, -1.5])

        # Combine all data points
        all_points = np.vstack([cluster1, cluster2, cluster3])  # 45 total points

        # --- VISUALIZE UNLABELED DATA ---
        # Initially, all points are gray (unlabeled)
        # The algorithm doesn't know which points belong together
        dots = VGroup(
            *[Dot(point=[x, y, 0], color=GRAY, radius=0.08) for x, y in all_points]
        )

        self.play(FadeIn(dots), run_time=2)
        self.wait(1)

        # --- CLUSTERING ALGORITHM RUNS ---
        # Common algorithms: K-means, DBSCAN, Hierarchical Clustering
        # Here we simulate the result of K-means with k=3
        explanation = Text("Algorithm discovers 3 distinct groups", font_size=24)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))

        # Assign colors to represent discovered clusters
        colors = [RED, BLUE, GREEN]

        # Animate the clustering process
        # In reality, this happens iteratively:
        # 1. Initialize cluster centers
        # 2. Assign points to nearest center
        # 3. Update centers based on assignments
        # 4. Repeat until convergence
        for i, (cluster_data, color) in enumerate(
            zip([cluster1, cluster2, cluster3], colors)
        ):
            cluster_dots = dots[i * 15 : (i + 1) * 15]  # Select dots for this cluster
            self.play(
                *[dot.animate.set_color(color) for dot in cluster_dots], run_time=1
            )

        # --- VISUALIZE CLUSTER BOUNDARIES ---
        # Draw circles around each cluster to show separation
        circles = VGroup()
        for cluster_data, color in zip([cluster1, cluster2, cluster3], colors):
            # Calculate cluster center (centroid)
            center = cluster_data.mean(axis=0)

            # Calculate radius to encompass all points in cluster
            radius = np.max(np.linalg.norm(cluster_data - center, axis=1)) + 0.3

            circle = Circle(radius=radius, color=color, stroke_width=3)
            circle.move_to([center[0], center[1], 0])
            circles.add(circle)

        self.play(Create(circles), run_time=2)
        self.wait(2)

    # --- CLASSIFICATION: SUPERVISED LEARNING ---
    # Goal: Learn a decision boundary from labeled training data
    # Then use it to predict labels for new, unseen data
    def classification_demo(self):
        # --- CREATE COORDINATE SYSTEM ---
        # Typically represents feature space (e.g., height vs weight, price vs quality)
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=6, tips=False
        ).shift(DOWN * 0.5)

        # --- TRAINING DATA ---
        # In supervised learning, we have labeled examples
        # Each point has features (x, y) and a label (Class A or Class B)
        np.random.seed(42)

        # Class A: Points centered at (-1.2, -1.2) - LABELED RED
        class_a = np.random.randn(20, 2) * 0.6 + np.array([-1.2, -1.2])

        # Class B: Points centered at (1.2, 1.2) - LABELED BLUE
        class_b = np.random.randn(20, 2) * 0.6 + np.array([1.2, 1.2])

        # --- VISUALIZE LABELED TRAINING DATA ---
        # Create labeled training points
        # RED = Class A, BLUE = Class B
        dots_a = VGroup(
            *[Dot(axes.c2p(x, y), color=RED, radius=0.08) for x, y in class_a]
        )
        dots_b = VGroup(
            *[Dot(axes.c2p(x, y), color=BLUE, radius=0.08) for x, y in class_b]
        )

        # Class labels
        label_a = Text("Class A", font_size=20, color=RED).move_to(axes.c2p(-2, -2.5))
        label_b = Text("Class B", font_size=20, color=BLUE).move_to(axes.c2p(2, 2.5))

        self.play(Create(axes))
        self.play(
            FadeIn(dots_a),
            FadeIn(dots_b),
            Write(label_a),
            Write(label_b),
        )
        self.wait(2)

        # --- DECISION BOUNDARY ---
        # The model learns to separate the two classes
        # For linearly separable data, this could be:
        # - Linear SVM (Support Vector Machine)
        # - Logistic Regression
        # - Perceptron
        # The boundary is where the model's prediction changes from A to B
        boundary = Line(
            axes.c2p(-2.5, 2.5),  # Top-left
            axes.c2p(2.5, -2.5),  # Bottom-right
            color=YELLOW,
            stroke_width=4,
        )

        boundary_text = Text("Decision Boundary", font_size=20, color=YELLOW)
        boundary_text.move_to(axes.c2p(0, 0.5))

        self.play(Create(boundary), Write(boundary_text))
        self.wait(1)

        # --- PREDICTION ON NEW DATA ---
        # The real test: Can the model classify unseen data?
        # Test point at (0.5, 0.8) - initially unknown class
        test_point = Dot(axes.c2p(0.5, 0.8), color=GREEN, radius=0.12)
        test_label = Text("New Point?", font_size=20, color=GREEN)
        test_label.next_to(test_point, RIGHT)

        # --- MODEL MAKES PREDICTION ---
        # Point (0.5, 0.8) is above the decision boundary
        # Therefore, model predicts: Class B (BLUE)
        prediction_text = Text("Model predicts: Class B", font_size=24, color=BLUE)
        prediction_text.to_edge(DOWN)

        self.play(FadeIn(test_point), Write(test_label))
        self.wait(1)

        # Show prediction and update point color
        self.play(Write(prediction_text))
        self.play(test_point.animate.set_color(BLUE))  # Classify as Class B
        self.wait(3)
