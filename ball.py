from turtle import Turtle
import random
STARTING_POSITION = (0,0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.starting_position()

    # method that sets ball's starting position and randomizes the direction of the ball
    def starting_position(self):
        self.goto(STARTING_POSITION)
        direction_x = random.choice([-1, 1])
        direction_y = random.choice([-1, 1])
        self.x_move *= direction_x
        self.y_move *= direction_y

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # logic for the ball to bounce when it hits the top or bottom wall
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
        # adding a condition to prevent the paddel from moving out of the screen
        if self.ycor() < 440:
            new_y = self.ycor() + 40
            self.goto(self.xcor(), new_y)

    def move_down(self):   
        # same as move_up but in the opposite direction 
        if self.ycor() > -360:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)