import pygame
import sys
from network import *
from player import *
from constants import *
from Ball import *

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Client")


def redrawWindow(win,player, player2, ball):
        win.fill((0, 0, 0))
        pygame.draw.line(win, (0, 0, 255), (constants.SCREEN_WIDTH/2, 0), (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT), 10)
        player.draw(win)
        player2.draw(win)
        ball.draw(win)
        pygame.display.update()

def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2[0], p2[1])


def client():
    main()