from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, pos_x=0, pos_y=0, color="yellow", align="center", font=("Verdana", 30, "normal")):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.align = align
        self.font = font
        self.hideturtle()
        self.color(color)
        self.score = 0
        self.penup()
        self.goto(pos_x, pos_y)
        self.write("0", font=self.font, align=self.align)

    def increment_score(self):
        """Increments score by 1 point"""
        self.clear()
        self.score += 1
        self.goto(self.pos_x, self.pos_y)
        self.write(f"{self.score}", font=self.font, align=self.align)

    def update_score(self, new_score: int):
        """Updates scoreboard to show new score"""
        self.clear()
        self.score = new_score
        self.goto(self.pos_x, self.pos_y)
        self.write(f"Score: {self.score}", font=self.font, align=self.align)

    def game_over(self, text: str):
        """Prints string, followed by final score."""
        self.clear()
        self.goto(self.pos_x, self.pos_y)
        self.write(f"{text} Final Score: {self.score}", font=self.font, align=self.align)