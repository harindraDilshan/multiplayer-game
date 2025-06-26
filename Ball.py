import pygame
from constants import *
from math import *

class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.ball = (x, y)
        self.speed = SPEED

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.ball, self.radius)

    def simulateCollition(init_x, init_y, curr_x, curr_y):
        # when collition x has value 0 <= x <= window_width 
        # when collition y = 0 or y = window_hight
        thita = atan(abs((init_y - curr_y)/(init_x - curr_x)))
        print(thita)
        pass


    def move(self, dx, dy):
        self.x += dx
        self.y += dy

        # if self.x < 0:
        #     self.x = 0
        # elif self.x + self.radius > SCREEN_WIDTH:
        #     self.x = SCREEN_WIDTH - self.radius

        if self.y < 0:
            self.y = 0
        elif self.y + self.radius > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.radius

        self.update()

    def update(self):
        self.ball = (self.x, self.y)
