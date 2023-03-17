from abc import ABC, abstractmethod

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