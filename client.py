import pygame
import sys
from network import *
from player import *
from constants import *
from Ball import *
import subprocess

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Client")

# tem = 0
pygame.font.init()
font = pygame.font.SysFont("Arial", 36)

def redrawWindow(win,player, player2, ball):
        win.fill((0, 0, 0))
        pygame.draw.line(win, (0, 0, 255), (constants.SCREEN_WIDTH/2, 0), (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT), 10)
        player.draw(win)
        player2.draw(win)
        ball.draw(win)

        # tem += 1
        # Move these two lines here so text updates each frame
        text_surface_1 = font.render(f"{ball.get_marks()[0]}", True, (255, 255, 255))
        text_rect_1 = text_surface_1.get_rect(center=(constants.SCREEN_WIDTH/2 - 50, 50))
        win.blit(text_surface_1, text_rect_1)

        text_surface_2 = font.render(f"{ball.get_marks()[1]}", True, (255, 255, 255))
        text_rect_2 = text_surface_2.get_rect(center=(constants.SCREEN_WIDTH/2 + 50, 50))
        win.blit(text_surface_2, text_rect_2)
        

        pygame.display.update()


def show_win_screen(winner):
    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 60)

    while True:
        win.fill((0, 0, 0))
        win_text = font.render(f"Player {winner} Wins!", True, (255, 255, 255))
        win_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        win.blit(win_text, win_rect)

        pygame.draw.rect(win, (0, 100, 255), button_rect)
        button_text = font.render("Play Again", True, (255, 255, 255))
        button_rect_text = button_text.get_rect(center=button_rect.center)
        win.blit(button_text, button_rect_text)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # Go back to main()

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
        if p2[1].get_marks()[0] >= 10:
            show_win_screen(constants.load_settings()[2])
            pygame.quit()
            sys.exit()
            return  # Exit main()
        elif p2[1].get_marks()[1] >= 10:
            show_win_screen(constants.load_settings()[2])
            pygame.quit()
            sys.exit()
            return
        
        redrawWindow(win, p, p2[0], p2[1])


def client():
    main()