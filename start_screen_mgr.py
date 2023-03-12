from typing_extensions import override
from base_game_state_mgr import BaseGameStateMgr
from constants import *
from colors import *
from button import Button
import pygame as pg

class StartScreenMgr(BaseGameStateMgr):
    def __init__(self, screen):
        super().__init__(screen)

        btn_width = 60
        btn_height = 20
        self.btn_start = Button('start', SCREEN_WIDTH / 2 - btn_width / 2, SCREEN_HEIGHT / 2 + 50 - btn_height / 2, btn_width, btn_height)

    @override
    def shutdown(self):
        pass
    
    @override
    def handle_events(self):
        return super().handle_events()
    
    @override
    def update(self):
        pass
    
    @override
    def draw(self):
        # background
        self.screen.fill(light_blue)

        self.draw_text(f'super pong', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50, dark_blue, 32)
        self.btn_start.draw(self.screen, pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])

        pg.display.flip()