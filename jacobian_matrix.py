class DrawLine(GraphScene,MovingCameraScene):
    CONFIG = {
        "fore_basis_cols": ["#d40b37","#d4b90b", "#d40b37"],
        "t_matrix": [["\\frac{\\partial f_{1} }{\\partial x}", " ","\\frac{\\partial f_{2} }{\\partial x}"], ["\\frac{\\partial f_{1} }{\\partial y} ", " ", "\\frac{\\partial f_{2} }{\\partial y} "]],
        "a_b_cols": [BLUE, WHITE,GREEN],
        "det_col": YELLOW_D,
    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        p1 = TextMobject("PENDAHULUAN").scale(2).set_color_by_gradient(TEAL, BLUE_C)
        p2 = TextMobject("JACOBIAN MATRIX").scale(2).set_color_by_gradient(TEAL, BLUE_C)

        p1.move_to(UP * 1)
        p2.next_to(p1, DOWN*2)

        pendahuluan = VGroup(p1, p2)
        self.play(ShowCreation(pendahuluan))
        self.wait()
        self.play(FadeOut(pendahuluan))
        self.wait()

        grid = NumberPlane()
        self.camera.frame.save_state()


        self.add(grid)  # Make sure title is on top of grid
        self.play(
            GrowFromPoint(grid,ORIGIN, run_time=2, lag_ratio=0.1)
        )
        arrow1 = Arrow(np.array([-3, 0, 0]), np.array([-2, 0, 0]), color=RED, buff=0)
        arrow2 = Arrow(np.array([-3, 0, 0]), np.array([-3, 1, 0]), color=BLUE, buff=0)
        self.add(arrow1,arrow2)
        self.wait()

        grid.prepare_for_nonlinear_transform()

        self.play(
        grid.apply_function,
        lambda p: p + np.array([
            np.sin(p[1]),
            np.sin(p[0]),
            0
        ]),
        arrow1.apply_function,
        lambda p: p + np.array([
            np.sin(p[1]),
            np.sin(p[0]),
            0
        ]),
        arrow2.apply_function,
        lambda p: p + np.array([
            np.sin(p[1]),
            np.sin(p[0]),
            0])
        )
        self.wait()
        self.play(
            self.camera_frame.scale, .5,
            self.camera_frame.shift, LEFT*3
        )
        self.wait()

        ##grid 2
        grid2 = NumberPlane().set_color(YELLOW_A)
        self.play(FadeIn(grid2))
        self.wait()

        ##arrow part 2
        arrow11 = Arrow(np.array([-3, -0.11, 0]), np.array([-2, -0.11, 0]), color=MAROON_A, buff=0)
        arrow22 = Arrow(np.array([-3, -0.11, 0]), np.array([-3, 0.9, 0]), color=BLUE_B, buff=0)


        #dashline
        df2 = DashedLine(np.array([-2, -0.9, 0]), np.array([-2, -0.11, 0]), color=GOLD_D, stroke_width=10)
        df1 = DashedLine(np.array([-2.17, 0.9, 0]), np.array([-3, 0.9, 0]), color=TEAL_B, stroke_width=10)


        ##text dx
        textdf2= TexMobject("\partial f2").scale(0.4).next_to(df2, RIGHT*0.5).set_color("#d40b37")
        textdf1= TexMobject("\partial f1").scale(0.4).next_to(arrow11, UP*0.01).set_color("#d40b37")
        textdx= TexMobject("\partial x").scale(0.4).next_to(arrow1, DOWN*0.1).set_color("#d40b37")

        ##text
        textdf2_2 = TexMobject("\partial f2").scale(0.4).next_to(arrow22, LEFT*0.1).set_color("#d4b90b")
        textdf1_2 = TexMobject("\partial f1").scale(0.4).next_to(arrow2, RIGHT*0.5+UP*0.1).set_color("#d4b90b")
        textdy = TexMobject("\partial y").scale(0.4).next_to(df1, UP*0.1).set_color("#d4b90b")


        #matrix
        a_equals = TextMobject("A", "=")
        a_equals[0].set_color(self.a_b_cols[2]).scale(0.7)
        matrix = (
            Matrix(
                np.array(self.t_matrix).transpose(), include_background_rectangle=True
            )
                .scale(0.5)
                .set_column_colors(*self.fore_basis_cols)
        )
        a_matrix = VGroup(a_equals, matrix).arrange_submobjects().shift( 5 * LEFT)

        self.play(
            Write(a_equals), FadeIn(matrix.background_rectangle), Write(matrix.brackets)
        )
        self.play(FadeOut(grid2))
        self.wait()
        self.wait()
        self.play(Write(textdx))
        self.play(Write(VGroup(arrow11, df2)))
        self.wait()
        self.play(Write(VGroup(textdf2, textdf1)))
        self.wait()
        self.play(Write(matrix.get_columns()[0]),WiggleOutThenIn(VGroup(textdf2,textdf1,textdx)))
        self.wait(1)
        self.play(Write(VGroup(arrow22,textdy,df1)))
        self.play(Write(VGroup(textdf2_2, textdf1_2)))
        self.play(Write(matrix.get_columns()[1]))


        self.play(FadeOut(VGroup(grid , arrow1, arrow2,arrow11,arrow22 , df1 ,
                                 df2 , textdf2 , textdf1 , textdx , textdf2_2,
                                 textdf1_2 , textdy)))
        self.play(Restore(self.camera.frame))
        jacob_matrix = VGroup(a_equals,matrix)

        self.play(
            jacob_matrix.shift,RIGHT*3,
            jacob_matrix.scale,1.5
        )
        brace = Brace(jacob_matrix, RIGHT).set_color_by_gradient(MAROON_C)
        jacobian = TextMobject("Jacobian Matrix").scale(1).set_color_by_gradient(MAROON_C, TEAL)
        jacobian.next_to(brace, RIGHT)
        self.play(Write(VGroup(brace,jacobian)),lag_ratio=0.25)
        self.wait()

