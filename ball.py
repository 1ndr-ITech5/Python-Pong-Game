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

    def bounce_x(self):
        # logic for the ball to bounce when it hits the paddel
        self.x_move *= -1