import pygame as pg
from enum import Enum

class GameEvent(Enum):
    # notifications from state mgrs
    ON_START_GAME = pg.event.custom_type()
    ON_GAME_OVER = pg.event.custom_type()
    ON_RETURN_TO_START = pg.event.custom_type()