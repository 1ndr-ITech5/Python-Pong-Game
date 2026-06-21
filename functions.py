from components.field import Field
from components.ball import Ball
from components.padels import Padel1, Padel2
from components.scoreboard import Scoreboard, Clock

def draw_post_game(ball:Ball, my_padel:Padel1, ai_padel:Padel2, scoreboard:Scoreboard, clock:Clock, field:Field):
    # clears all components of the game
    ball.hideturtle()
    field.clear()
    clock.clear()
    my_padel.hideturtle()
    ai_padel.hideturtle()

    # final result is shown
    scoreboard.clear()
    scoreboard.final_score()