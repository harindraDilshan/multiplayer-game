import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Box propertics
BOX_SIZE = 50
BOX_SPEED = 5

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BOX_SIZE
        self.height = BOX_SIZE
        self.color = RED
        self.speed = BOX_SPEED

    def move(self, dx, dy):
        # Move the object and keep it withing screen boundaries
        self.x += dx * self.speed
        self.y += dy * self.speed

        # Boundary checking 
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width

        if self.y < 0:
            self.y = 0
        elif self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))



def main():
    # Create the display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("******* MULTIPLAYE GAME *******")

    # Create clock object to control frame rate
    clock = pygame.time.Clock()

    # Create a box object
    box = Box(SCREEN_WIDTH // 2 - BOX_SIZE // 2, SCREEN_HEIGHT // 2 - BOX_SIZE // 2)

    # Main game loop
    running = True
    while running:
        # Handel events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Get pressed keys for continuous movement
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = 1

        # Update game objects
        box.move(dx, dy)
        
         # Draw everything
        screen.fill(BLACK)  # Clear screen with black background
        box.draw(screen)

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

    # Quit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()