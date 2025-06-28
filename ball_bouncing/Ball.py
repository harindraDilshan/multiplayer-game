import pygame

class Ball():
    def __init__(self):
        self.radius = 10
        self.speed = [4, 2]
        self.height = 600
        self.width = 600
        self.color = (0, 0, 255)
        self.ball_rect = pygame.Rect(5, 5, self.radius*2, self.radius*2)

    def draw(self, win):
        self.ball_rect = self.ball_rect.move(self.speed)

        # Bounce off the walls
        if self.ball_rect.left < 0 or self.ball_rect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.ball_rect.top < 0 or self.ball_rect.bottom > self.height:
            self.speed[1] = -self.speed[1]

        pygame.draw.circle(win, self.color, self.ball_rect.center, self.radius)