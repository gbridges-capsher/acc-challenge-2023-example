import os
import pygame as pg
from datetime import datetime
from constants import *
from colors import *
from paddle import Paddle
from ball import Ball
from game_mgr import GameMgr

# game entrypoint
if __name__ == "__main__":
    game_mgr = GameMgr()
    game_mgr.run()