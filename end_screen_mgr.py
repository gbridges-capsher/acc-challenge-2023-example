from typing_extensions import override
from base_game_state_mgr import BaseGameStateMgr
from constants import *
from colors import *
from button import Button
from game_event import GameEvent
import pygame as pg

class EndScreenMgr(BaseGameStateMgr):
    def __init__(self, screen, final_player_score, final_ai_score):
        super().__init__(screen)

        self.final_player_score = final_player_score
        self.final_ai_score = final_ai_score

        btn_width = 80
        btn_height = 20
        self.btn_exit = Button(
            'main menu', 
            SCREEN_WIDTH / 2 - btn_width / 2, 
            SCREEN_HEIGHT / 2 + 80 - btn_height / 2, 
            btn_width, 
            btn_height,
            self.on_exit_btn_clicked
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
        self.screen.fill(light_blue)

        end_text = 'you win!' if self.final_player_score > self.final_ai_score else 'you lost'
        self.draw_text(end_text, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75, dark_blue, 64)

        self.draw_text('final score', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 10, dark_blue, 24)
        self.draw_text(f'{self.final_player_score} - {self.final_ai_score}', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20, dark_blue, 24)

        self.btn_exit.draw(self.screen)

        pg.display.flip()

    """
    Callbacks
    """
    def on_exit_btn_clicked(self):
        pg.event.post(pg.event.Event(GameEvent.ON_RETURN_TO_START.value))