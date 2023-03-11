from constants import *
from colors import *
import pygame as pg

class Paddle:
    def __init__(self, center_x):
        self.center_x = center_x
        self.center_y = SCREEN_HEIGHT / 2

        self.height = PADDLE_INITIAL_HEIGHT
        self.width = PADDLE_WIDTH
        self.color = dark_blue

    def update(self, y):
        self.center_y = y

        # adjust position to not go past screen bounds
        if self.center_y < self.height / 2:
            self.center_y = self.height / 2
        elif self.center_y > SCREEN_HEIGHT - self.height / 2:
            self.center_y = SCREEN_HEIGHT - self.height / 2

    def ball_collision_test(self, ball):
        if ball.x_vel < 0 and ball.prev_x() > self.center_x and ball.center_x <= self.center_x:
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

    def get_rect(self): # alternatively, "get_rekt"
        return pg.Rect(
            self.center_x - self.width / 2,
            self.center_y - self.height / 2,
            self.width,
            self.height
        )