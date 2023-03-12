from abc import ABC, abstractmethod
import pygame as pg

"""
Abstract base class for the mgrs of individual game states to derive from
"""
class BaseGameStateMgr(ABC):
    def __init__(self, screen):
        self.screen = screen

    def shutdown(self):
        raise NotImplementedError("Implement in derived classes")

    def handle_events(self):
        handled = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            
        return handled

    @abstractmethod
    def update(self):
        raise NotImplementedError("Implement in derived classes")

    @abstractmethod
    def draw(self):
        raise NotImplementedError("Implement in derived classes")
    
    """
    Utility for easily drawing text on screen
    """
    def draw_text(self, text, x, y, color, font_size):
        font = pg.font.Font('freesansbold.ttf', font_size)
        text_object = font.render(text, True, color)
        text_rect = text_object.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_object, text_rect)