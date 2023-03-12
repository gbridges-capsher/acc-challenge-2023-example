import pygame as pg
from constants import *
from player_paddle import PlayerPaddle
from ai_paddle import AIPaddle
from ball import Ball
from colors import *
from gameplay_mgr import GameplayMgr
from start_screen_mgr import StartScreenMgr
from game_state import GameState

"""
Top-level game manager
"""
class GameMgr:
    def __init__(self):
        # pygame setup
        pg.init()

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        self.clock = pg.time.Clock()

        self.game_state = None
        self.active_game_state_mgr = None

        # gameplay elements
        self.ball = Ball()
        self.player_paddle = PlayerPaddle()
        self.ai_paddle = AIPaddle()

        self.player_score = 0
        self.ai_score = 0

    def run(self):
        self.activate_game_state(GameState.START_SCREEN)

        # main game loop
        while True:
            self.active_game_state_mgr.handle_events()
            self.active_game_state_mgr.update()
            self.active_game_state_mgr.draw()

            # sleep
            self.clock.tick(FPS)
    
    def activate_game_state(self, state):
        if self.game_state != state:
            print(f'Transitioning from game state {self.game_state} to {state.value}')
            self.game_state = state

            if self.active_game_state_mgr is not None:
               self.active_game_state_mgr.shutdown()
               self.active_game_state_mgr = None 

            if self.game_state == GameState.START_SCREEN:
                self.active_game_state_mgr = StartScreenMgr(self.screen)
            elif self.game_state == GameState.GAMEPLAY:
                self.active_game_state_mgr = GameplayMgr(self.screen)
            elif self.game_state == GameState.END_SCREEN:
                pass
            else:
                raise NotImplementedError(f'Unhandled game state transition: {state.value}')
