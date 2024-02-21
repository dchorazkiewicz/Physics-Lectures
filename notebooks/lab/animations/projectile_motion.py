from manim import *

class ProjectileMotion(Scene):
    def construct(self):
        # Definiuje równania ruchu i umieszcza je po prawej stronie
        equations = VGroup(
            MathTex("x = v_0 \\cos(\\theta) t"),
            MathTex("y = v_0 \\sin(\\theta) t - \\frac{1}{2} g t^2"),
            MathTex("t_{max} = \\frac{v_0 \\sin(\\theta)}{g}"),
            MathTex("R = \\frac{v_0^2 \\sin(2\\theta)}{g}")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.7).to_edge(RIGHT, buff=0.5)

        self.play(Write(equations))
        self.wait(1)

        # Tworzy trajektorię rzutu po lewej stronie ekranu
        trajectory = ParametricFunction(
            lambda t: np.array([
                4*np.cos(np.pi/4)*t,  # x = v_0 cos(θ) t
                4*np.sin(np.pi/4)*t - 0.5*9.8*t**2,  # y = v_0 sin(θ) t - 1/2 g t^2
                0
            ]), t_range = np.array([0, 2, 0.01]), color=YELLOW
        ).shift(LEFT*3)

        self.play(Create(trajectory), run_time=3)
        self.wait(1)

        # Dodaje opis trajektorii i wzorów
        description = Text("Rzut ukośny", font_size=24).to_edge(UP)
        self.play(Write(description))
        self.wait(1)

        self.play(FadeOut(trajectory), FadeOut(equations), FadeOut(description))
