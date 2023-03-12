from typing_extensions import override
from constants import *
from paddle import Paddle
from random import random

"""
AI-controlled opponent paddle - calculates its own position based on ball position
"""
class AIPaddle(Paddle):
    def __init__(self):
        super().__init__()

        self.center_x = SCREEN_WIDTH - PADDLE_DIST_FROM_EDGE

        self.target_spot_ratio = None # the spot we're aiming for the ball to hit on our paddle, as a ratio of height

    @override
    def check_ball_passed(self, ball):
        return ball.x_vel > 0 and ball.prev_x() <= self.center_x and ball.center_x > self.center_x

    def update(self, ball):
        if ball.x_vel > 0:
            if self.target_spot_ratio is None:
                self.compute_target_spot_ratio()

            target_spot_y = self.top_y() + self.target_spot_ratio * self.height

            ball_is_below_paddle = ball.center_y > target_spot_y - self.height / 5
            ball_is_above_paddle = ball.center_y < target_spot_y + self.height / 5

            if ball_is_below_paddle or ball_is_above_paddle:
                # ease towards the ball
                move_speed = ball.center_y - target_spot_y
                move_speed = min(move_speed, AI_PADDLE_MAX_SPEED)
                move_speed = max(move_speed, -AI_PADDLE_MAX_SPEED)

                self.center_y += move_speed
        else:
            # clear out, recompute when ball is heading towards us again
            self.target_spot_ratio = None

        self.bound_y_position()

    def compute_target_spot_ratio(self):
        self.target_spot_ratio = .15 + random()*.70