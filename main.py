from turtle import Screen
from field import Field
from ball import Ball
from padels import Padels

POSITIONS = [(650, 0), (-650, 0)]

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()

field = Field()
field.midfield()
ball = Ball()

paddels = []
for pos in POSITIONS:
    padel = Padels()
    padel.goto(pos)
    paddels.append(padel)

# event listeners for the paddels
screen.onkey(paddels[1].move_up, "w")
screen.onkey(paddels[1].move_down, "s")

game_on = True

# controls the flow of the game
while game_on:
    ball.move()

    # detect if ball is its danger zone
    if abs(paddels[0].ycor() - ball.ycor()) < 60:
        if paddels[0].ycor() > ball.ycor():
            move_amount = -40
        elif paddels[0].ycor() < ball.ycor():
            move_amount = 40

    y_move = paddels[0].ycor() + move_amount
    paddels[0].goto(paddels[0].xcor(), y_move)

    if ball.ycor() > 420 or ball.ycor() < -420:
        ball.bounce_y()

    # detect collison with the paddels and bounce the ball
    if ball.distance(paddels[0]) < 50 or ball.distance(paddels[1]) < 50:
        ball.bounce_x()

screen.exitonclick()