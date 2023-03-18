import pygame as pg
from typing_extensions import override

from CommonUI.button import Button
from CommonUI.draw_util import DrawUtil
from constants import *
from GameState.base_game_state_mgr import BaseGameStateMgr
from GameState.game_event import GameEvent
from theme import Theme


class EndScreenMgr(BaseGameStateMgr):
    def __init__(self, screen, final_player_score, final_ai_score):
        super().__init__(screen)

        self.final_player_score = final_player_score
        self.final_ai_score = final_ai_score

        self.btn_exit = Button('main menu', self.on_exit_btn_clicked)

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
            handled = self.btn_exit.handle_mouse_left_btn_down(event)
        
        return handled

    @override
    def handle_mouse_left_btn_up(self, event):
        handled = False

        if not handled:
            handled = self.btn_exit.handle_mouse_left_btn_up(event)
        
        return handled
    
    @override
    def draw(self):
        # background
        self.screen.fill(Theme.BACKGROUND.value)

        x_pos = SCREEN_WIDTH / 2
        y_pos = SCREEN_HEIGHT / 2 - 75

        end_text = 'you win! :D' if self.final_player_score > self.final_ai_score else 'you lost :('
        DrawUtil.draw_text(self.screen, end_text, x_pos, y_pos, Theme.PRIMARY.value, 64)

        y_pos += 65
        DrawUtil.draw_text(self.screen, 'final score', x_pos, y_pos, Theme.PRIMARY.value, 24)
        y_pos += 30
        DrawUtil.draw_text(self.screen, f'{self.final_player_score} - {self.final_ai_score}', x_pos, y_pos, Theme.PRIMARY.value, 24)

        btn_width = 160
        btn_height = 50
        btn_x = x_pos - btn_width / 2
        btn_y = y_pos + 70
        self.btn_exit.draw(self.screen, btn_x, btn_y, btn_width, btn_height)

        pg.display.flip()

    """
    Callbacks
    """
    def on_exit_btn_clicked(self):
        pg.event.post(pg.event.Event(GameEvent.ON_RETURN_TO_START.value))