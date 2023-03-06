from turtle import Turtle

UP = 90
DOWN = 270


class Paddle:
    def __init__(self, starting_x, min_y=0, max_y=0, move_step=20):
        self.move_step = move_step
        self.min_y = min_y
        self.max_y = max_y
        self.paddle_square_size = 20
        self.paddle_length = 4
        if self.paddle_length % 2 == 0:
            y = int((self.paddle_length / 2) * self.paddle_square_size)
        else:
            y = int(((self.paddle_length - 1) / 2) * self.paddle_square_size)
        self.paddle = []
        for i in range(self.paddle_length):
            self.paddle.append(Turtle())
            self.paddle[i].shape("square")
            self.paddle[i].penup()
            self.paddle[i].color("white")
            self.paddle[i].speed(0)
            self.paddle[i].goto(x=starting_x, y=(y - (i * self.paddle_square_size)))

    def down(self):
        """Moves paddle down"""
        if self.paddle[-1].ycor() > self.min_y + self.paddle_square_size:
            for segment in self.paddle:
                segment.setheading(DOWN)
                segment.forward(self.move_step)

    def up(self):
        """Moves paddle up"""
        if self.paddle[0].ycor() < self.max_y:
            for segment in self.paddle:
                segment.setheading(UP)
                segment.forward(self.move_step)

    def ball_in_contact(self, ball, threshold=20):
        """Checks if ball is in contact with paddle"""
        for segment in self.paddle:
            if segment.distance(ball) < threshold:
                return True
        return False
