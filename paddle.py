from abc import ABC, abstractmethod
from constants import *
from colors import *
import pygame as pg

"""
Base paddle class for player and AI paddles to derive from
"""
class Paddle(ABC):
    def __init__(self):
        self.center_x = 0
        self.center_y = SCREEN_HEIGHT / 2

        self.height = PADDLE_INITIAL_HEIGHT
        self.width = PADDLE_WIDTH
        self.color = dark_blue

    @abstractmethod
    def check_ball_passed(self, ball):
        raise NotImplementedError("Override in derived classes")

    def ball_collision_test(self, ball):
        if self.check_ball_passed(ball):
            # passed over our x position - see if it collided with paddle in y direction
            ball_y = ball.get_interpolated_y(self.center_x)
            if ball_y >= self.top_y() - ball.radius and ball_y <= self.bottom_y() + ball.radius:
                # smack!
                return True
            
        return False
    
    def top_y(self):
        return self.center_y - self.height / 2
    
    def bottom_y(self):
        return self.center_y + self.height / 2

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.get_rect())

    def bound_y_position(self):
        # adjust position to not go past screen bounds
        if self.center_y < self.height / 2:
            self.center_y = self.height / 2
        elif self.center_y > SCREEN_HEIGHT - self.height / 2:
            self.center_y = SCREEN_HEIGHT - self.height / 2

    def get_rect(self): # alternatively, "get_rekt"
        return pg.Rect(
            self.center_x - self.width / 2,
            self.center_y - self.height / 2,
            self.width,
            self.height
        )