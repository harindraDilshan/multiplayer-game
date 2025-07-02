import pygame
from constants import *


class Player():
    def __init__(self, x, y, width, height, color, side):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.side = side
        self.speed = SPEED

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        dy, dx = 0, 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1

        self.x += dx * self.speed
        self.y += dy * self.speed

        if self.side == 2:
            if self.x < SCREEN_WIDTH/2:
                self.x = SCREEN_WIDTH/2
            elif self.x + self.width > SCREEN_WIDTH:
                self.x = SCREEN_WIDTH - self.width

        if self.side == 1:
            if self.x > SCREEN_WIDTH/2 - self.width:
                self.x = SCREEN_WIDTH/2 - self.width
            elif self.x < 0:
                self.x = 0


        if self.y < 0:
            self.y = 0
        elif self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
        
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
