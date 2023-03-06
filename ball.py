from turtle import Turtle
import random


class Ball:
    def __init__(self, min_x=0, max_x=0, min_y=0, max_y=0):
        self.min_y = min_y
        self.max_y = max_y
        self.min_x = min_x
        self.max_x = max_x
        self.ball = Turtle(shape="circle")
        self.ball.penup()
        self.ball.color("white")
        self.ball.speed(0)
        self.ball.goto(x=0, y=random.randint(min_y, max_y))
        direction = random.randint(0, 1)
        if direction == 0:
            self.ball.setheading(random.randint(-50, 50))
        else:
            self.ball.setheading(random.randint(120, 230))

    def reset_ball(self):
        self.ball.goto(x=0, y=random.randint(self.min_y, self.max_y))
        direction = random.randint(0, 1)
        if direction == 0:
            self.ball.setheading(random.randint(-50, 50))
        else:
            self.ball.setheading(random.randint(120, 230))

    def move_ball(self, num_steps=10, step=1):
        """Moves ball a total of distance of num steps * step.
        If within 1.5 * step of wall ball angle will be mirrored, and motion continued"""
        for _ in range(int(num_steps / step)):
            if (self.ball.distance(x=self.ball.xcor(), y=self.min_y) >= step * 5) and \
                    (self.ball.distance(x=self.ball.xcor(), y=self.max_y) >= step * 5):
                self.ball.forward(step)
            else:
                self.mirror_heading()
                self.ball.forward(step)

    def mirror_heading(self):
        """Changes ball heading to angle of incidence"""
        heading = -(self.ball.heading() % 360)
        self.ball.setheading(heading)

    def paddle_heading(self):
        heading = 0
        if 0 <= self.ball.heading() < 90:
            diff = 90 - self.ball.heading()
            heading = 90 + diff
        elif 270 < self.ball.heading() <= 360:
            diff = 270 - self.ball.heading()
            heading = 270 + diff
        elif 90 < self.ball.heading() <= 180:
            diff = 90 - self.ball.heading()
            heading = 90 + diff
        elif 180 <= self.ball.heading() < 270:
            diff = 270 - self.ball.heading()
            heading = 270 + diff
        self.ball.setheading(heading)

    def check_wall_contact(self, threshold=5):
        if self.ball.distance(x=self.min_x, y=self.ball.ycor()) <= threshold:
            return 2
        elif self.ball.distance(x=self.max_x, y=self.ball.ycor()) <= threshold:
            return 1
        else:
            return 0
