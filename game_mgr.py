import pygame as pg
from constants import *
from paddle import Paddle
from ai_paddle import AIPaddle
from ball import Ball
from colors import *

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

        # gameplay elements
        self.ball = Ball()
        self.player_paddle = Paddle(PADDLE_DIST_FROM_EDGE)
        self.ai_paddle = AIPaddle(SCREEN_WIDTH - PADDLE_DIST_FROM_EDGE)

    def run(self):
        # main game loop
        while True:
            self.handle_events()
            self.update()
            self.draw()

            # sleep
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit

    def update(self):
        # adjust movements
        self.player_paddle.update(pg.mouse.get_pos()[1])
        self.ai_paddle.update(pg.mouse.get_pos()[1])
        self.ball.update()

        # detect hit collisions and handle
        if self.player_paddle.ball_collision_test(self.ball):
            self.ball.handle_paddle_hit(self.player_paddle)
        elif self.ai_paddle.ball_collision_test(self.ball):
            self.ball.handle_paddle_hit(self.ai_paddle)

    def draw(self):
        # show blue screen with updating datetime in center 
        self.screen.fill(light_blue)

        self.player_paddle.draw(self.screen)
        self.ai_paddle.draw(self.screen)
        self.ball.draw(self.screen)

        # text display
        if SHOW_DEBUG_METRICS:
            font = pg.font.Font('freesansbold.ttf', 12)
            text = font.render(f'Ball Vel: [{self.ball.x_vel:0.1f}, {self.ball.y_vel:0.1f}]', True, dark_blue)
            text_rect = text.get_rect()
            text_rect.topleft = (20, 20)
            self.screen.blit(text, text_rect)

        pg.display.flip()
