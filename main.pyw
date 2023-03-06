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

    # create text object
    font = pg.font.Font('freesansbold.ttf', 32)

    # set up paddles
    player_paddle = Paddle(40, SCREEN_HEIGHT / 2)

    ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # main game loop
    while True:
        # handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit

        # adjust movements
        player_paddle.set_y(pg.mouse.get_pos()[1])
        ball.update()

        # detect hit collisions and handle
        # TODO

        # draw everything
        # show blue screen with updating datetime in center 
        screen.fill(light_blue)

        player_paddle.draw(screen)
        ball.draw(screen)

        # refresh screen
        pg.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
