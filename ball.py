from colors import *
from constants import *
from random import randint
import pygame as pg
from pygame import gfxdraw

class Ball:
    def __init__(self):
        self.center_x = 0
        self.center_y = 0
        self.x_vel = 0
        self.y_vel = 0

        self.color = dark_blue
        self.radius = BALL_RADIUS

        self.reset(False)

    def update(self):
        self.center_x += self.x_vel
        self.center_y += self.y_vel

        # bounds check
        if self.y_vel < 0 and self.center_y <= 0 or self.y_vel > 0 and self.center_y >= SCREEN_HEIGHT:
            self.y_vel *= -1

    def draw(self, screen):
        #pg.draw.circle(screen, self.color, (self.center_x, self.center_y), self.radius)
        gfxdraw.aacircle(screen, int(self.center_x), int(self.center_y), self.radius, self.color)
        gfxdraw.filled_circle(screen, int(self.center_x), int(self.center_y), self.radius, self.color)

    def reset(self, move_left):
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2

        self.x_vel = BALL_INITIAL_X_VEL * (-1 if move_left else 1)
        self.y_vel = randint(-1 * BALL_Y_VEL_RANGE / 2, BALL_Y_VEL_RANGE / 2)

    def apply_speed_limit(self):
        self.x_vel = min(max(self.x_vel, -BALL_MAX_X_VEL), BALL_MAX_X_VEL)

    def prev_x(self):
        return self.center_x - self.x_vel
    
    def prev_y(self):
        return self.center_y - self.y_vel

    def get_interpolated_y(self, x):
        # get y value at some x between our last point and current point
        x1 = self.center_x
        x2 = self.prev_x()
        y1 = self.center_y
        y2 = self.prev_y()

        # oh boy algebra!
        m = (y2 - y1)/(x2 - x1)
        b = y1 - m * x1

        return m*x + b
    
    def handle_paddle_hit(self, paddle):
        # hit paddle - reverse x direction and move a little faster
        self.x_vel *= -BALL_HIT_X_VEL_MULT
        self.apply_speed_limit()
        self.center_x += self.x_vel # update x to corrected position after boucnce

        # recompute y velocity based on where the ball hit the paddle
        self.y_vel = BALL_Y_VEL_RANGE * (paddle.center_y - self.center_y)/(paddle.top_y() - paddle.bottom_y()) 
