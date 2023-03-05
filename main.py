import os
import pygame as pg
from datetime import datetime
from constants import *
from colors import *

# game entrypoint
def main():
    # initialization
    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption(GAME_TITLE)
    clock = pg.time.Clock()

    # create text object
    font = pg.font.Font('freesansbold.ttf', 32)

    # main game loop
    while True:
        # handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit

        # show blue screen with updating datetime in center 
        screen.fill(light_blue)

        text = font.render(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), True, dark_blue, None)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        
        screen.blit(text, textRect)

        pg.display.flip() # refresh
        clock.tick(FPS)

if __name__ == "__main__":
    main()
