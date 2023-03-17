import pygame as pg
from theme import Font

class DrawUtil:
    """
    Simple utility for drawing text on screen
    """
    @staticmethod
    def draw_text(screen, text, center_x, center_y, color, font_size):
        font = pg.font.Font(Font.PRIMARY.value, font_size)
        text_object = font.render(text, True, color)
        text_rect = text_object.get_rect()
        text_rect.center = (center_x, center_y)
        screen.blit(text_object, text_rect)