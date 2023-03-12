import pygame as pg
from constants import *
from player_paddle import PlayerPaddle
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
        self.player_paddle = PlayerPaddle()
        self.ai_paddle = AIPaddle()

        self.player_score = 0
        self.ai_score = 0

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
        self.ball.update()
        self.player_paddle.update(pg.mouse.get_pos()[1])
        self.ai_paddle.update(self.ball)

        # detect hit collisions and handle
        if self.ball.x_vel < 0 and self.player_paddle.ball_collision_test(self.ball):
            self.ball.handle_paddle_hit(self.player_paddle)
        elif self.ball.x_vel > 0 and self.ai_paddle.ball_collision_test(self.ball):
            self.ball.handle_paddle_hit(self.ai_paddle)

        # detect passing bounds and handle
        if self.ball.x_vel < 0 and self.ball.center_x < 0:
            self.handle_ai_score()
        elif self.ball.x_vel > 0 and self.ball.center_x > SCREEN_WIDTH:
            self.handle_player_score()

    def draw(self):
        # background
        self.screen.fill(light_blue)

        # center line
        pg.draw.line(self.screen, dark_blue, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT), 2)

        # gameplay elements
        self.player_paddle.draw(self.screen)
        self.ai_paddle.draw(self.screen)
        self.ball.draw(self.screen)

        # score text display
        self.draw_text(f'{self.player_score}', 20, 20, dark_blue, 12)
        self.draw_text(f'{self.ai_score}', SCREEN_WIDTH - 20, 20, dark_blue, 12)

        if SHOW_DEBUG_METRICS:
            self.draw_text(f'Ball Vel: [{self.ball.x_vel:0.1f}, {self.ball.y_vel:0.1f}]', 20, SCREEN_HEIGHT - 20, dark_blue, 12)

        pg.display.flip()

    def handle_ai_score(self):
        self.ball.reset(False)
        self.ai_score += 1

    def handle_player_score(self):
        self.ball.reset(True)
        self.player_score += 1

    """
    Utility for easily drawing text on screen
    """
    def draw_text(self, text, x, y, color, font_size):
        font = pg.font.Font('freesansbold.ttf', font_size)
        text_object = font.render(text, True, color)
        text_rect = text_object.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_object, text_rect)
