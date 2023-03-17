import pygame as pg
from theme import Theme, Font
from constants import *

class Button:
    def __init__(self, text, callback):
        self.text = text
        self.callback = callback

        self.font_size = 12
        self.font_family = Font.PRIMARY.value
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
    
    def draw(self, screen, x, y, width, height):
        mouse_x = pg.mouse.get_pos()[0]
        mouse_y = pg.mouse.get_pos()[1]
        
        color = Theme.BUTTON_BASE.value
        if self.hit_test(mouse_x, mouse_y):
            if self.is_pressed:
                color = Theme.BUTTON_CLICK.value
            else:
                color = Theme.BUTTON_HOVER.value
        
        self.rect = pg.Rect(x, y, width, height)
        pg.draw.rect(screen, color, self.rect)

        font = pg.font.Font(self.font_family, self.font_size)
        text_object = font.render(self.text, True, Theme.BUTTON_TEXT.value)
        screen.blit(text_object, self.rect)