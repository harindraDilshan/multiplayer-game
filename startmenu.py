import pygame
import sys
import constants
import subprocess
import threading
import re
from client import client
from server import server

def is_port_listening(port):
    try:
        result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
        pattern = f':{port}.*LISTEN'
        return bool(re.search(pattern, result.stdout))
    except:
        return False

# Init Pygame
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Multiplayer Game Menu")
clock = pygame.time.Clock()

# Colors and Font
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
font = pygame.font.SysFont(None, 50)

# Button size
button_width, button_height = 200, 80

# Main menu buttons
button_rect_start = pygame.Rect(constants.SCREEN_WIDTH // 2 - button_width // 2, constants.SCREEN_HEIGHT // 2 - 120, button_width, button_height)
button_rect_exit = pygame.Rect(constants.SCREEN_WIDTH // 2 - button_width // 2, constants.SCREEN_HEIGHT // 2 + 20, button_width, button_height)

# Difficulty buttons
button_rect_easy = pygame.Rect(constants.SCREEN_WIDTH // 2 - button_width // 2, constants.SCREEN_HEIGHT // 2 - 140, button_width, button_height)
button_rect_normal = pygame.Rect(constants.SCREEN_WIDTH // 2 - button_width // 2, constants.SCREEN_HEIGHT // 2 - 40, button_width, button_height)
button_rect_hard = pygame.Rect(constants.SCREEN_WIDTH // 2 - button_width // 2, constants.SCREEN_HEIGHT // 2 + 60, button_width, button_height)

def draw_button(rect, text_str):
    pygame.draw.rect(screen, BLACK, rect)
    text = font.render(text_str, True, WHITE)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

def draw_menu():
    screen.fill(GRAY)
    draw_button(button_rect_start, "Start Game")
    draw_button(button_rect_exit, "Exit Game")
    pygame.display.flip()

def draw_difficulty_menu():
    screen.fill(GRAY)
    draw_button(button_rect_easy, "Easy")
    draw_button(button_rect_normal, "Normal")
    draw_button(button_rect_hard, "Hard")
    pygame.display.flip()

def run_game(difficulty):
    if not is_port_listening(5557):
        print(f"Starting game with difficulty: {difficulty}")
        if difficulty == "Easy":
            constants.BALL_SPEED = [1, 1]
        elif difficulty == "Normal":
            constants.BALL_SPEED = [6, 6]
        elif difficulty == "Hard":
            constants.BALL_SPEED = [10, 10]

        threading.Thread(target=server, daemon=True).start()
    client()

def difficulty_menu_loop():
    while True:
        draw_difficulty_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect_easy.collidepoint(event.pos):
                    run_game("Easy")
                    return
                elif button_rect_normal.collidepoint(event.pos):
                    run_game("Normal")
                    return
                elif button_rect_hard.collidepoint(event.pos):
                    run_game("Hard")
                    return

def main():
    while True:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect_start.collidepoint(event.pos): 
                    if not is_port_listening(5557):
                        difficulty_menu_loop()
                    else:
                        run_game("")
                elif button_rect_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

main()
