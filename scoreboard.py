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
        self.clear()
        if self.score1 > self.score2:
            self.write(arg="Congrats! You won!", move=False, align="center", font=("Courier", 66, "bold"))
        elif self.score1 == self.score2:
            self.write(arg="Draw!", move=False, align="center", font=("Courier", 66, "bold"))
        else:
            self.write(arg="Sorry, you lost!", move=False, align="center", font=("Courier", 66, "bold"))

        self.write(arg="Final Score", move=False, align="center", font=("Courier", 66, "bold"))
        self.write(arg=f"{self.score1} {self.score2}", move=False, align="center", font=("Courier", 66, "bold"))

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