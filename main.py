from turtle import Screen, Turtle
from field import Field
from ball import Ball
from padels import Padel1, Padel2
from scoreboard import Scoreboard, Clock
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
scoreboard = Scoreboard()
clock = Clock()

# creating both paddels
my_paddel = Padel1()
ai_paddel = Padel2()

# event listeners for the paddels
screen.onkey(my_paddel.move_up, "w")
screen.onkey(my_paddel.move_down, "s")

# controls the game itself
game_on = True

# controls if the player wants a new game
restart_game = True

# variable that keeps the user's answer
restart_requested = False


while restart_game:
    # controls the flow of the game
    while game_on:
        screen.update()
        time.sleep(0.03)
        clock.update_timer()
        ai_paddel.patrol()
        ball.move()

        if ball.ycor() > 420 or ball.ycor() < -420:
            ball.bounce_y()

        # detect collison with the paddels and bounce the ball
        if ball.distance(my_paddel) < 50 or ball.distance(ai_paddel) < 50:
            ball.bounce_x()

        # update the score after a goal is scored
        if ball.xcor() > 800:
            scoreboard.update_score1()
            ball.starting_position()
        elif ball.xcor() < -800:
            scoreboard.update_score2()
            ball.starting_position() 

        if clock.timer < 0:
            game_on = False

    # clears all components of the game
    ball.clear()
    field.clear()
    clock.clear()
    my_paddel.clear()
    ai_paddel.clear()

    # final result is shown
    scoreboard.clear()
    scoreboard.final_score()
    screen.update()

    # write in the screen for the start of the new game
    # event listener if clicked
    # event listener if clicked the other button => go out of the game
    


screen.exitonclick()