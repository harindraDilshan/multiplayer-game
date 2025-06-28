import pygame
from constants import *
from math import *

class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        # self.ball = (x, y)
        self.speed = BALL_SPEED
        self.ball_rect = pygame.Rect(5, 5, self.radius*2, self.radius*2)

    def draw(self, win):
        # self.ball_rect = self.ball_rect.move(self.speed)

        # # Bounce off the walls
        # if self.ball_rect.left < 0 or self.ball_rect.right > self.width:
        #     self.speed[0] = -self.speed[0]
        # if self.ball_rect.top < 0 or self.ball_rect.bottom > self.height:
        #     self.speed[1] = -self.speed[1]

        pygame.draw.circle(win, self.color, self.ball_rect.center, self.radius)
        # pygame.draw.circle(win, self.color, self.ball, self.radius)
        

    def move(self, players):
        # self.x += dx
        # self.y += dy

        # # if self.x < 0:
        # #     self.x = 0
        # # elif self.x + self.radius > SCREEN_WIDTH:
        # #     self.x = SCREEN_WIDTH - self.radius
        
        # # thita = atan(abs((dy)/(dx)))
        # # print(f"<<<<<<<<< {thita} >>>>>>>>>>")

        # if self.y < 0:
        #     self.y = 0

        # elif self.y + self.radius > SCREEN_HEIGHT:
        #     self.y = SCREEN_HEIGHT - self.radius

        # self.update()

        # print(f"{players[0].x} ---- {players[1].x}")

        self.ball_rect = self.ball_rect.move(self.speed)

        # Bounce off the walls
        if self.ball_rect.left < 0 or self.ball_rect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.ball_rect.top < 0 or self.ball_rect.bottom > self.height:
            self.speed[1] = -self.speed[1]

        # if players[0].x > self.ball_rect.left or players[0].y < self.ball_rect.top:
        #     self.speed[0] = -self.speed[0]
        

    def update(self):
         self.ball = (self.x, self.y)
