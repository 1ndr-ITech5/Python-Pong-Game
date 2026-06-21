from turtle import Turtle

class Padel1(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("normal")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(-650, 0)

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


class Padel2(Padel1):
    def __init__(self):
        super().__init__()
        self.goto(650, 0)
        self.direction = 1
        self.move = 40
        
    def patrol(self):
        if self.ycor() > 440:
            self.direction = -1
        elif self.ycor() < -360:
            self.direction = 1

        new_y = self.ycor() + (self.move * self.direction)
        self.goto(self.xcor(), new_y)