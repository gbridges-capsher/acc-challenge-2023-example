from typing_extensions import override
from base_game_state_mgr import BaseGameStateMgr
from constants import *
from colors import *
from button import Button
from game_event import GameEvent
import pygame as pg

class StartScreenMgr(BaseGameStateMgr):
    def __init__(self, screen):
        super().__init__(screen)

        btn_width = 60
        btn_height = 20
        self.btn_start = Button(
            'start', 
            SCREEN_WIDTH / 2 - btn_width / 2, 
            SCREEN_HEIGHT / 2 + 50 - btn_height / 2, 
            btn_width, 
            btn_height,
            self.on_start_btn_clicked
        )

    @override
    def shutdown(self):
        pass
    
    @override
    def process_frame(self):
        self.update()
        self.draw()
    
    @override
    def update(self):
        pass

    @override
    def handle_mouse_left_btn_down(self, event):
        handled = False

        if not handled:
            handled = self.btn_start.handle_mouse_left_btn_down(event)
        
        return handled

    @override
    def handle_mouse_left_btn_up(self, event):
        handled = False

        if not handled:
            handled = self.btn_start.handle_mouse_left_btn_up(event)
        
        return handled
    
    @override
    def draw(self):
        # background
        self.screen.fill(light_blue)

        self.draw_text(f'super pong', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50, dark_blue, 32)
        self.btn_start.draw(self.screen)

        pg.display.flip()

    """
    Callbacks
    """
    def on_start_btn_clicked(self):
        pg.event.post(pg.event.Event(GameEvent.ON_START_GAME.value))