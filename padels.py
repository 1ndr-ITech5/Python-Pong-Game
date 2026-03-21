from turtle import Turtle
import random

class Padels(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        # adding a condition to prevent the paddel from moving out of the screen
        if self.ycor() < 440:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def move_down(self):   
        # same as move_up but in the opposite direction 
        if self.ycor() > -360:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)

    def AI_move(self):
        directions = [-40, 40]
        move_amount = random.choice(directions)

        if self.ycor() > 440:
            move_amount = -40
        elif self.ycor() < -360:
            move_amount = 40

        y_move = self.ycor() + move_amount
        self.goto(self.xcor(), y_move)