from turtle import Turtle
STARTING_POSITION = (0,0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(STARTING_POSITION)



class Padels(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + 60
        self.goto(self.xcor(), new_y)

    def move_down(self):    
        new_y = self.ycor() - 60
        self.goto(self.xcor(), new_y)
        