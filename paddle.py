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

    def draw(self, screen):
        rect = pg.Rect(
            self.center_x - self.width / 2,
            self.center_y - self.height / 2,
            self.width,
            self.height
        )
        pg.draw.rect(screen, self.color, rect)