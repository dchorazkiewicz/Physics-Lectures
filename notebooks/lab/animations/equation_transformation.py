from manim import *

class EquationTransform(Scene):
    def construct(self):
        # Definiuje równania za pomocą MathTex
        eq1 = MathTex("E=mc^2")
        eq2 = MathTex("m=\\frac{E}{c^2}")

        # Ustawia początkowe równanie na środku ekranu
        self.play(Write(eq1))
        self.wait(1)

        # Przekształca pierwsze równanie w drugie
        self.play(Transform(eq1, eq2))
        self.wait(1)
