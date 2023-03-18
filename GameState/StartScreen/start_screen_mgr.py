import pygame as pg
from typing_extensions import override

from CommonUI.button import Button
from CommonUI.draw_util import DrawUtil
from constants import *
from GameState.base_game_state_mgr import BaseGameStateMgr
from GameState.game_event import GameEvent
from theme import Theme

class StartScreenMgr(BaseGameStateMgr):
    def __init__(self, screen):
        super().__init__(screen)

        self.btn_start = Button('start', self.on_start_btn_clicked)

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
        self.screen.fill(Theme.BACKGROUND.value)

        x_pos = SCREEN_WIDTH / 2
        y_pos = SCREEN_HEIGHT / 2 - 60

        DrawUtil.draw_text(self.screen, f'super pong', x_pos, y_pos, Theme.PRIMARY.value, 64)

        btn_width = 120
        btn_height = 50
        btn_x = x_pos - btn_width / 2 
        btn_y = y_pos + 120
        self.btn_start.draw(self.screen, btn_x, btn_y, btn_width, btn_height)

        pg.display.flip()

    """
    Callbacks
    """
    def on_start_btn_clicked(self):
        pg.event.post(pg.event.Event(GameEvent.ON_START_GAME.value))