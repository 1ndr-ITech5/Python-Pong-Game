from turtle import Turtle
STARTING_POSITION = (0,0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(STARTING_POSITION)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1



class Padels(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        if self.ycor() < 440:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def move_down(self):    
        if self.ycor() > -360:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)