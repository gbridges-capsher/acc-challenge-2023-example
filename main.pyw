import pygame as pg

from constants import *
from GameState.EndScreen.end_screen_mgr import EndScreenMgr
from GameState.game_event import GameEvent
from GameState.game_state import GameState
from GameState.Gameplay.gameplay_mgr import GameplayMgr
from GameState.StartScreen.start_screen_mgr import StartScreenMgr

class Main:
    def __init__(self):
        # pygame setup
        pg.init()

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        self.clock = pg.time.Clock()

        self.game_state = None
        self.active_game_state_mgr = None

    def run(self):
        self.transition_game_state(GameState.START_SCREEN)

        # main game loop
        while True:
            # get all events currently in the queue and handle
            for event in pg.event.get():
                match event.type:
                    case pg.QUIT:
                        pg.quit()
                        raise SystemExit
                    # --- input events ---
                    case pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.active_game_state_mgr.handle_mouse_left_btn_down(event)
                    case pg.MOUSEBUTTONUP:
                        if event.button == 1:
                            self.active_game_state_mgr.handle_mouse_left_btn_up(event)
                    # --- game transition events ---
                    case GameEvent.ON_START_GAME.value:
                        self.transition_game_state(GameState.GAMEPLAY)
                    case GameEvent.ON_GAME_OVER.value:
                        self.transition_game_state(GameState.GAME_OVER, event)
                    case GameEvent.ON_RETURN_TO_START.value:
                        self.transition_game_state(GameState.START_SCREEN)

            # tell active game state mgr to do work for this frame
            self.active_game_state_mgr.process_frame()
                
            # sleep
            self.clock.tick(FPS)
    
    def transition_game_state(self, new_state, event_data = None):
        if self.game_state != new_state:
            print(f'Transitioning from {self.game_state} to {new_state}')
            self.game_state = new_state

            if self.active_game_state_mgr is not None:
               self.active_game_state_mgr.shutdown()

            if self.game_state == GameState.START_SCREEN:
                self.active_game_state_mgr = StartScreenMgr(self.screen)
            elif self.game_state == GameState.GAMEPLAY:
                self.active_game_state_mgr = GameplayMgr(self.screen)
            elif self.game_state == GameState.GAME_OVER:
               self.active_game_state_mgr = EndScreenMgr(self.screen, event_data.player_score, event_data.ai_score)
            else:
                raise NotImplementedError(f'Unhandled game state transition: {new_state.value}')

# game entrypoint
Main().run()