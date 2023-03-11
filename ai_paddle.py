from typing_extensions import override
from constants import *
from paddle import Paddle

"""
AI-controlled opponent paddle - calculates its own position based on ball position
"""
class AIPaddle(Paddle):
    def __init__(self):
        super().__init__()

        self.center_x = SCREEN_WIDTH - PADDLE_DIST_FROM_EDGE

    @override
    def check_ball_passed(self, ball):
        return ball.x_vel > 0 and ball.prev_x() <= self.center_x and ball.center_x > self.center_x

    def update(self, ball):
        self.center_y = ball.center_y

        self.bound_y_position()