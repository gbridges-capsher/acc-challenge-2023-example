from typing_extensions import override
from constants import *
from paddle import Paddle

"""
Player-controlled paddle - uses mouse input to position
"""
class PlayerPaddle(Paddle):
    def __init__(self):
        super().__init__()

        self.center_x = PADDLE_DIST_FROM_EDGE

    @override
    def check_ball_passed(self, ball):
        return ball.x_vel < 0 and ball.prev_x() > self.center_x and ball.center_x <= self.center_x

    def update(self, mouse_y):
        self.center_y = mouse_y

        self.bound_y_position()