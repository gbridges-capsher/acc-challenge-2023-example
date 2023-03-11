import os
import pygame as pg
from datetime import datetime
from constants import *
from colors import *
from paddle import Paddle
from ball import Ball

# game entrypoint
def main():
    # initialization
    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption(GAME_TITLE)
    clock = pg.time.Clock()

    # set up paddles
    player_paddle = Paddle(40, SCREEN_HEIGHT / 2)

    ball = Ball()

    # main game loop
    while True:
        # handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit

        # adjust movements
        player_paddle.update(pg.mouse.get_pos()[1])
        ball.update()

        # detect hit collisions and handle
        if player_paddle.ball_collision_test(ball):
            ball.handle_paddle_hit(player_paddle)

        # draw everything
        # show blue screen with updating datetime in center 
        screen.fill(light_blue)

        player_paddle.draw(screen)
        ball.draw(screen)

        # text display
        if SHOW_DEBUG_METRICS:
            font = pg.font.Font('freesansbold.ttf', 12)
            text = font.render(f'Ball Vel: [{ball.x_vel:0.1f}, {ball.y_vel:0.1f}]', True, dark_blue)
            text_rect = text.get_rect()
            text_rect.topleft = (20, 20)
            screen.blit(text, text_rect)

        # refresh screen
        pg.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
