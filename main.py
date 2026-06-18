from turtle import Screen
from field import Field
from ball import Ball
from padels import Padel1, Padel2
from scoreboard import Scoreboard, Clock
from functions import draw_post_game
import time

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

# controls if the player wants a new game
restart_game = True


while restart_game:

    # controls the game itself
    game_on = True

    #set all components
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

    # call the post game process
    draw_post_game(ball, my_paddel, ai_paddel, scoreboard, clock, fieldw)
    screen.update()

    restart_game = False

    # write in the screen for the start of the new game
    # event listener if clicked
    # event listener if clicked the other button => go out of the game
    


screen.exitonclick()