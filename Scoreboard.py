from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        with open("highscore.txt") as file:
            self.highscore = file.read()
        self.write(f"Score 0   High Score {self.highscore}", False, align="center", font=("Arial", 16, "normal"))

    def update(self, score):
        self.clear()
        if score > int(self.highscore):
            with open("highscore.txt", "w") as file:
                file.write(str(score))
                self.highscore = str(score)

        self.write(f"Score: {score}   High Score {self.highscore}", False, align="center", font=("Arial", 16, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align="center", font=("Arial", 16, "normal"))