from typing_extensions import override
import pygame as pg
from constants import *
from player_paddle import PlayerPaddle
from ai_paddle import AIPaddle
from ball import Ball
from theme import Theme
from base_game_state_mgr import BaseGameStateMgr
from game_event import GameEvent

"""
Manager for gameplay state
"""
class GameplayMgr(BaseGameStateMgr):
    def __init__(self, screen):
        super().__init__(screen)

        # gameplay elements
        self.ball = Ball()
        self.player_paddle = PlayerPaddle()
        self.ai_paddle = AIPaddle()

        self.player_score = 0
        self.ai_score = 0

    @override
    def shutdown(self):
        pass

    @override
    def process_frame(self):
        self.update()
        self.draw()

    @override
    def update(self):
        # adjust movements
        self.ball.update()
        self.player_paddle.update(pg.mouse.get_pos()[1])
        self.ai_paddle.update(self.ball)

        # detect hit ball collisions and handle
        if self.ball.x_vel < 0 and self.player_paddle.ball_collision_test(self.ball):
            self.ball.handle_paddle_hit(self.player_paddle)
        elif self.ball.x_vel > 0 and self.ai_paddle.ball_collision_test(self.ball):
            self.ball.handle_paddle_hit(self.ai_paddle)

        # detect ball passing paddle and handle
        if self.ball.x_vel < 0 and self.ball.center_x < 0:
            self.handle_ai_score()
        elif self.ball.x_vel > 0 and self.ball.center_x > SCREEN_WIDTH:
            self.handle_player_score()

        # handle either player hitting score limit
        if self.player_score >= MAX_SCORE or self.ai_score >= MAX_SCORE:
            pg.event.post(pg.event.Event(GameEvent.ON_GAME_OVER.value, {
                'player_score': self.player_score, 
                'ai_score': self.ai_score
                })
            )

    @override
    def draw(self):
        # background
        self.screen.fill(Theme.BACKGROUND.value)

        # center line
        pg.draw.line(self.screen, Theme.SECONDARY.value, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT), 2)

        # gameplay elements
        self.player_paddle.draw(self.screen)
        self.ai_paddle.draw(self.screen)
        self.ball.draw(self.screen)

        # score text display
        score_text_margin = 20
        self.draw_text(f'{self.player_score}', score_text_margin, score_text_margin, Theme.SECONDARY.value, 24)
        self.draw_text(f'{self.ai_score}', SCREEN_WIDTH - score_text_margin, score_text_margin, Theme.SECONDARY.value, 24)

        if SHOW_DEBUG_METRICS:
            self.draw_text(f'Ball Vel: [{self.ball.x_vel:0.1f}, {self.ball.y_vel:0.1f}]', 80, SCREEN_HEIGHT - 20, Theme.PRIMARY.value, 12)

        pg.display.flip()

    def handle_ai_score(self):
        self.ball.reset(False)
        self.ai_score += 1

    def handle_player_score(self):
        self.ball.reset(True)
        self.player_score += 1
