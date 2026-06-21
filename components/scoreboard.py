from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 330)
        self.score1 = 0
        self.score2 = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.pendown()
        self.pencolor("white")
        self.write(arg=f"{self.score1} {self.score2}", move=False, align="center", font=("Courier", 88, "bold"))

    def update_score1(self):
        self.score1 += 1
        self.clear()
        self.write(arg=f"{self.score1} {self.score2}", move=False, align="center", font=("Courier", 88, "bold"))

    def update_score2(self):
        self.score2 += 1
        self.clear()
        self.write(arg=f"{self.score1} {self.score2}", move=False, align="center", font=("Courier", 88, "bold"))

    def final_score(self):
        self.penup()
        self.goto(0, 150)
        self.pendown()
        if self.score1 > self.score2:
            self.write(arg="Congrats! You won!", move=False, align="center", font=("Courier", 70, "bold"))
        elif self.score1 == self.score2:
            self.write(arg="Draw!", move=False, align="center", font=("Courier", 70, "bold"))
        else:
            self.write(arg="Sorry, you lost!", move=False, align="center", font=("Courier", 70, "bold"))

        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write(arg="Final Score", move=False, align="center", font=("Courier", 60, "bold"))
        self.penup()
        self.goto(0, -150)
        self.pendown()
        self.write(arg=f"{self.score1} {self.score2}", move=False, align="center", font=("Courier", 60, "bold"))
        self.penup()
        self.goto(0, -300)
        self.write(arg="Tap here to restart", move=False, align="center", font=("Courier", 56, "bold"))
        self.goto(0, -400)
        self.write(arg="Click here to Exit", move=False, align="center", font=("Courier", 50, "bold"))

class Clock(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-360, 390)
        self.timer = 20
        self.create_timer()

    def create_timer(self):
        self.pendown()
        self.pencolor("white")
        self.write(arg=f"Time:{int(self.timer)} secs", move=False, align="center", font=("Courier", 20, "bold"))

    def update_timer(self):
        self.timer -= 0.03
        self.clear()
        self.write(arg=f"Time:{int(self.timer)} secs", move=False, align="center", font=("Courier", 20, "bold"))