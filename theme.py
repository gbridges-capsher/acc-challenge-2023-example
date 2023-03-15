from enum import Enum

class Theme(Enum):
    BACKGROUND = (40, 40, 40)
    PRIMARY = (245, 255, 94)
    SECONDARY = (246, 250, 185)

    BUTTON_BASE = (122, 121, 121)
    BUTTON_HOVER = (171, 171, 171)
    BUTTON_CLICK = (140, 140, 140)
    BUTTON_TEXT = PRIMARY

class Font(Enum):
    PRIMARY = 'freesansbold.ttf'