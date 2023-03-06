from turtle import Turtle


class Scoreboard:

    def __init__(self,
                 pos_x=0,
                 pos_y=0,
                 color="yellow",
                 clear_color="black",
                 align="center",
                 font=("Verdana", 30, "normal")):
        self.clear_color = clear_color
        self.color = color
        self.align = align
        self.font = font
        self.scoreboard = Turtle(visible=False)
        self.scoreboard.color(color)
        self.score = 0
        self.scoreboard.penup()
        self.scoreboard.goto(pos_x, pos_y)
        self.scoreboard.write("0", font=self.font, align=self.align)

    def increment_score(self):
        """Increments score by 1 point"""
        self.scoreboard.color(self.clear_color)
        self.scoreboard.write(f"{self.score}", font=self.font, align=self.align)
        self.score += 1
        self.scoreboard.color(self.color)
        self.scoreboard.write(f"{self.score}", font=self.font, align=self.align)
