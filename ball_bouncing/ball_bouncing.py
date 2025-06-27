import pygame
import sys

pygame.init()

speed = [6, 6]
background = (0, 0, 0)
width, height = 800, 400
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")

# Initial ball setup
ball_radius = 10
ball_color = (0, 0, 255)
ball_rect = pygame.Rect(5, 5, ball_radius*2, ball_radius*2)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_rect = ball_rect.move(speed)

    # Bounce off the walls
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    # Draw everything
    screen.fill(background)
    pygame.draw.circle(screen, ball_color, ball_rect.center, ball_radius)
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)
