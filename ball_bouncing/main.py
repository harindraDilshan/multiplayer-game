import pygame
from Ball import *
import sys

win = pygame.display.set_mode((600, 600))

def main(win, ball):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        win.fill((0, 0, 0))
        ball.draw(win)
        pygame.display.update()

if __name__ == "__main__":
    ball = Ball()
    main(win, ball)