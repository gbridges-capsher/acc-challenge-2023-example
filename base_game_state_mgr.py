from abc import ABC, abstractmethod
import pygame as pg

"""
Abstract base class for the mgrs of individual game states to derive from
"""
class BaseGameStateMgr(ABC):
    def __init__(self, screen):
        self.screen = screen

    """
    Called at end of lifecycle
    """
    def shutdown(self):
        raise NotImplementedError("Implement in derived classes")

    """
    Called once per frame of main loop - primary work method
    """
    @abstractmethod
    def process_frame(self):
        raise NotImplementedError("Implement in derived classes")

    """
    Makes any necessary updates to the model
    """
    @abstractmethod
    def update(self):
        raise NotImplementedError("Implement in derived classes")

    """
    Draw components on screen
    """
    @abstractmethod
    def draw(self):
        raise NotImplementedError("Implement in derived classes")
    
    def handle_mouse_left_btn_down(self, event):
        handled = True
        return handled
    
    def handle_mouse_left_btn_up(self, event):
        handled = True
        return handled
    
    """
    Utility for easily drawing text on screen
    TODO: Move this to a utility class
    """
    def draw_text(self, text, x, y, color, font_size):
        font = pg.font.Font('freesansbold.ttf', font_size)
        text_object = font.render(text, True, color)
        text_rect = text_object.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_object, text_rect)