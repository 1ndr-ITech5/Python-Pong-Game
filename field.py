from turtle import Turtle

class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.pensize(5)
        self.goto(x=0, y=500)
        self.setheading(270)

    def midfield(self):
        while self.ycor() > -500:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)