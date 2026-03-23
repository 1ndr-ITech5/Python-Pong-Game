from turtle import Screen
from field import Field
from ball import Ball
from padels import Padel1, Padel2
import time

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

field = Field()
field.midfield()
ball = Ball()

# creating both paddels
my_paddel = Padel1()
ai_paddel = Padel2()

# event listeners for the paddels
screen.onkey(my_paddel.move_up, "w")
screen.onkey(my_paddel.move_down, "s")

game_on = True

# controls the flow of the game
while game_on:
    screen.update()
    time.sleep(0.03)
    ai_paddel.patrol()
    ball.move()

    if ball.ycor() > 420 or ball.ycor() < -420:
        ball.bounce_y()

    # detect collison with the paddels and bounce the ball
    if ball.distance(my_paddel) < 50 or ball.distance(ai_paddel) < 50:
        ball.bounce_x()

screen.exitonclick()