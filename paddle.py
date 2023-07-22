import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed
