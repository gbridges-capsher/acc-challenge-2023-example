"""
This file serves as a kind of dashboard to easily adjust all game mechanics in one spot

Note: All velocity values are measured in "pixels per frame"
"""

# game constants
FPS = 24
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_TITLE = "Super Pong"
SHOW_DEBUG_METRICS = False

# gameplay constants
MAX_SCORE = 3

# ball constants
BALL_RADIUS = 4
BALL_INITIAL_X_VEL = 15
BALL_MAX_X_VEL = 30
BALL_HIT_X_VEL_MULT = 1.1
BALL_Y_VEL_RANGE = 30

# paddle constants
PADDLE_INITIAL_HEIGHT = 60
PADDLE_WIDTH = 6
PADDLE_DIST_FROM_EDGE = 40

# ai paddle constants
AI_PADDLE_MAX_SPEED = 10