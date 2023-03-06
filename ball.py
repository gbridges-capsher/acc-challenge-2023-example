from colors import *
from constants import *
import pygame as pg

class Ball:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y

        self.x_vel = 10
        self.y_vel = 10

        self.color = dark_blue

        # width and height
        self.size = 4

    def update(self):
        new_x = self.center_x + self.x_vel
        new_y = self.center_y + self.y_vel

        if new_x < 0:
            new_x = 0
            self.x_vel *= -1
        elif new_x > SCREEN_WIDTH:
            new_x = SCREEN_WIDTH
            self.x_vel *= -1

        # adjust y position to not go past screen bounds (bounce)
        if self.y_vel < 0 and new_y < self.size / 2:
            new_y += (self.size / 2) - new_y
            self.y_vel *= -1
        elif self.y_vel > 0 and new_y > (SCREEN_HEIGHT - self.size):
            new_y -= (SCREEN_HEIGHT - self.size) - (new_y + self.size)
            self.y_vel *= -1

        self.center_x = new_x
        self.center_y = new_y

    def draw(self, screen):
        rect = pg.Rect(
            self.center_x - self.size / 2,
            self.center_y - self.size / 2,
            self.size,
            self.size
        )
        pg.draw.rect(screen, self.color, rect)
