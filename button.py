import pygame as pg
from colors import *
from constants import *

class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pg.Rect(x, y, width, height)
        self.callback = callback

        self.base_color = (230, 92, 64)
        self.hover_color = (224, 144, 128)
        self.down_color = (184, 70, 48)
        self.text_color = black
        self.font_size = 12
        self.font_family = 'freesansbold.ttf'

        self.is_pressed = False

    def hit_test(self, x, y):
        return self.rect.collidepoint(x, y)

    def handle_mouse_left_btn_down(self, event):
        handled = False
        if self.hit_test(event.pos[0], event.pos[1]):
            self.is_pressed = True
            handled = True

        return handled

    def handle_mouse_left_btn_up(self, event):
        handled = False
        if self.is_pressed:
            if self.hit_test(event.pos[0], event.pos[1]):
                self.callback()
                handled = True

            self.is_pressed = False

        return handled
    
    def draw(self, screen, mouse_x, mouse_y):
        
        color = self.base_color
        if self.hit_test(mouse_x, mouse_y):
            if self.is_pressed:
                color = self.down_color
            else:
                color = self.hover_color
        
        pg.draw.rect(screen, color, self.rect)

        font = pg.font.Font(self.font_family, self.font_size)
        text_object = font.render(self.text, True, self.text_color)
        screen.blit(text_object, self.rect)