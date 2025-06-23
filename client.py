import pygame
import sys
from network import *

'''
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

    def move(self):

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

        return self.x, self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))



def main():
    # Create the display window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("******* MULTIPLAYE GAME *******")

    # Create clock object to control frame rate
    clock = pygame.time.Clock()

    n = Network()
    start_pos = n.getPos()

    # Create a box object
    init_x = int((str(start_pos).strip('()')).split(",")[0])
    init_y = int((str(start_pos).strip('()')).split(",")[1])
    box = Box(init_x, init_y)
    box2 = Box(100, 100)

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

        

        # Update game objects
        current_pos = box.move()
        p2Pos = n.send(f"{current_pos}")
        print(f"==== {p2Pos}")
        # box2.x = p2Pos[0]
        # box2.y = p2Pos[1]

        
        
        # Draw everything
        screen.fill(BLACK)  # Clear screen with black background
        box.draw(screen)
        box2.draw(screen) #####################

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(FPS)

    # Quit
    pygame.quit()
    sys.exit()

'''

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(win,player, player2):
    win.fill((0, 0, 0))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def read_pos(str):
    str = str.strip("()").split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,0,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)


if __name__ == "__main__":
    main()