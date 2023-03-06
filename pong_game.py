from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

DOWN = 270


class PongGame:
    def __init__(self):
        # Setup board
        self.screen = Screen()
        self.screen_x = 1000
        self.screen_y = 1000
        self.wall_buffer = 20
        self.screen.setup(self.screen_x, self.screen_y)
        self.screen.bgcolor("black")
        self.screen.title("Pong Game")
        self.time_per_move = 25  # ms
        self.screen.tracer(0)

        # Setup paddles
        self.paddle1 = Paddle(starting_x=(self.screen_x / -2 + self.wall_buffer),
                              min_y=self.screen_y / -2,
                              max_y=self.screen_y / 2,
                              move_step=self.screen_y / 20)
        self.paddle2 = Paddle(starting_x=(self.screen_x / 2 - self.wall_buffer * 1.5),
                              min_y=self.screen_y / -2,
                              max_y=self.screen_y / 2,
                              move_step=self.screen_y / 20)
        self.screen.onkey(self.paddle1.up, "w")
        self.screen.onkey(self.paddle1.down, "s")
        self.screen.onkey(self.paddle2.up, "Up")
        self.screen.onkey(self.paddle2.down, "Down")

        # Setup scoreboards
        self.score1 = Scoreboard(pos_x=-50, pos_y=(self.screen_y / 2 - 50))
        self.score2 = Scoreboard(pos_x=50, pos_y=(self.screen_y / 2 - 50))

        # Setup center line
        self.center_line = Turtle()
        self.center_line.hideturtle()
        self.center_line.penup()
        self.center_line.pencolor("white")
        self.center_line.pensize(width=int(self.screen_x / 200))
        self.center_line.goto(x=0, y=self.screen_y / 2)
        self.center_line.setheading(DOWN)
        dashes = 30
        distance = self.screen_y / dashes
        for i in range(dashes):
            if i % 2 == 0:
                self.center_line.pendown()
            else:
                self.center_line.penup()
            self.center_line.forward(distance=distance)

        # Create ball at random location on center-line, launch at random angle
        self.ball = Ball(min_x=self.screen_x / -2,
                         max_x=self.screen_x / 2,
                         min_y=self.screen_y / -2,
                         max_y=self.screen_y / 2)

    def play_game(self, max_score=3):
        """Initiates pong game until max score is reached."""
        game_active = True
        debounce_cycles = 0

        while game_active:
            self.screen.update()
            self.ball.move_ball(num_steps=8, step=1)
            if debounce_cycles > 0:
                debounce_cycles -= 1

            if self.paddle1.ball_in_contact(ball=self.ball.ball, threshold=25) and debounce_cycles == 0:
                self.ball.paddle_heading()
                debounce_cycles = 10
            elif self.paddle2.ball_in_contact(ball=self.ball.ball, threshold=25) and debounce_cycles == 0:
                self.ball.paddle_heading()
                debounce_cycles = 10

            if self.ball.check_wall_contact(threshold=10) == 1:
                self.score1.increment_score()
                self.ball.reset_ball()
                self.screen.update()
                time.sleep(3)
            elif self.ball.check_wall_contact(threshold=10) == 2:
                self.score2.increment_score()
                self.ball.reset_ball()
                self.screen.update()
                time.sleep(3)

            if self.score1.score >= max_score or self.score2.score >= max_score:
                game_active = 0

            self.screen.listen()
            time.sleep(self.time_per_move / 1000)

        self.screen.exitonclick()
