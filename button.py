import pygame as pg
from colors import *
from constants import *

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pg.Rect(x, y, width, height)

        self.base_color = dark_blue
        self.hover_color = white

    def hit_test(self, x, y):
        return self.rect.collidepoint(x, y)
    
    def draw(self, screen, mouse_x, mouse_y):
        if self.hit_test(mouse_x, mouse_y):
            pg.draw.rect(screen, self.hover_color, self.rect)
        else:
            pg.draw.rect(screen, self.base_color, self.rect)