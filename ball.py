from colors import *
from constants import *
from random import randint
import pygame as pg

class Ball:
    def __init__(self):
        self.center_x = 0
        self.center_y = 0
        self.x_vel = 0
        self.y_vel = 0

        self.color = dark_blue
        self.radius = 4

        self.reset(False)

    def update(self):
        self.center_x += self.x_vel
        self.center_y += self.y_vel

        # bounds check
        if self.x_vel < 0 and self.center_x <= 0 or self.x_vel > 0 and self.center_x >= SCREEN_WIDTH:
            self.x_vel *= -1
        if self.y_vel < 0 and self.center_y <= 0 or self.y_vel > 0 and self.center_y >= SCREEN_HEIGHT:
            self.y_vel *= -1

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.center_x, self.center_y), self.radius)

    def reset(self, move_left):
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2

        self.x_vel = 20 * (1 if move_left else -1)
        self.y_vel = randint(-15, 15)

    def apply_speed_limit(self):
        max_speed = 50
        self.x_vel = min(max(self.x_vel, -max_speed), max_speed)

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
