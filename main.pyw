import pygame as pg
from constants import *
from colors import *
from start_screen_mgr import StartScreenMgr
from gameplay_mgr import GameplayMgr
from game_state import GameState
from game_event import GameEvent

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
        self.activate_game_state(GameState.START_SCREEN)

        # main game loop
        while True:
            # get all events currently in the queue and handle
            for event in pg.event.get():
                match event.type:
                    case pg.QUIT:
                        pg.quit()
                        raise SystemExit
                    # --- user input events ---
                    case pg.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.active_game_state_mgr.handle_mouse_left_btn_down(event)
                    case pg.MOUSEBUTTONUP:
                        if event.button == 1:
                            self.active_game_state_mgr.handle_mouse_left_btn_up(event)
                    # --- game events ---
                    case GameEvent.ON_START_GAME.value:
                        self.activate_game_state(GameState.GAMEPLAY)

            # tell active game state mgr to do work for this frame
            self.active_game_state_mgr.process_frame()
                
            # sleep
            self.clock.tick(FPS)
    
    def activate_game_state(self, state):
        if self.game_state != state:
            print(f'Transitioning from game state {self.game_state} to {state.value}')
            self.game_state = state

            if self.active_game_state_mgr is not None:
               self.active_game_state_mgr.shutdown()

            if self.game_state == GameState.START_SCREEN:
                self.active_game_state_mgr = StartScreenMgr(self.screen)
            elif self.game_state == GameState.GAMEPLAY:
                self.active_game_state_mgr = GameplayMgr(self.screen)
            #elif self.game_state == GameState.END_SCREEN:
            #    pass
            else:
                raise NotImplementedError(f'Unhandled game state transition: {state.value}')

# game entrypoint
Main().run()