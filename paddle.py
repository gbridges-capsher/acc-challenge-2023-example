from constants import *
from colors import *
import pygame as pg

class Paddle:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y

        self.height = 40
        self.width = 4
        self.color = dark_blue

    def set_y(self, y):
        self.center_y = y

        # adjust position to not go past screen bounds
        if self.center_y < self.height / 2:
            self.center_y = self.height / 2
        elif self.center_y > SCREEN_HEIGHT - self.height / 2:
            self.center_y = SCREEN_HEIGHT - self.height / 2

    def get_rect(self): # alternatively, "get_rekt"
        return pg.Rect(
            self.center_x - self.width / 2,
            self.center_y - self.height / 2,
            self.width,
            self.height
        )

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.get_rect())

    def test_hit_ball(ball):
        # draw rect from ball's old position to new position, then test for intersection with our paddle
        # ball center to ball center is sufficient
        pass