from turtle import Screen
from field import Field
from ball import Ball, Padels

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

screen.onkey(paddels[1].move_up, "Up")
screen.onkey(paddels[1].move_down, "Down")

screen.exitonclick()