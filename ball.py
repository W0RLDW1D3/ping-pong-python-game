import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, speed):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.dx = random.choice([-1, 1]) * speed
        self.dy = random.choice([-1, 1]) * speed

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def check_collision(self, paddles):
        if self.rect.top <= 0 or self.rect.bottom >= pygame.display.get_surface().get_height():
            self.dy *= -1
        if pygame.sprite.spritecollide(self, paddles, False):
            self.dx *= -1

    def reset(self):
        self.rect.x = pygame.display.get_surface().get_width() // 2
        self.rect.y = pygame.display.get_surface().get_height() // 2
        self.dx = random.choice([-1, 1]) * self.speed
        self.dy = random.choice([-1, 1]) * self.speed
