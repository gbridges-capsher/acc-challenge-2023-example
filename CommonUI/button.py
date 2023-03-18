import pygame as pg
from theme import Theme
from constants import *
from CommonUI.draw_util import DrawUtil

class Button:
    def __init__(self, text, callback, font_size = 24):
        self.text = text
        self.callback = callback

        self.font_size = font_size
        self.rect = None # defined on "draw"; saved so we can do hit tests

        self.is_pressed = False

    def hit_test(self, x, y):
        if self.rect is None:
            return False

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
    
    def draw(self, screen, left_x, top_y, width, height):
        mouse_x = pg.mouse.get_pos()[0]
        mouse_y = pg.mouse.get_pos()[1]
        
        color = Theme.BUTTON_BASE.value
        if self.hit_test(mouse_x, mouse_y):
            if self.is_pressed:
                color = Theme.BUTTON_CLICK.value
            else:
                color = Theme.BUTTON_HOVER.value
        
        self.rect = pg.Rect(left_x, top_y, width, height)
        pg.draw.rect(screen, color, self.rect)

        center_x = left_x + width / 2
        center_y = top_y + height / 2
        DrawUtil.draw_text(screen, self.text, center_x, center_y, Theme.BUTTON_TEXT.value, self.font_size)