import pygame
from constants import RED, GREEN


class HealthBar:
    def __init__(self, x: int, y: int, hp: int, max_hp: int):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, screen, hp: int, base=RED, secondary=GREEN, width=150, height=20):
        self.hp = hp
        pygame.draw.rect(screen, base, (self.x, self.y, width, height))
        pygame.draw.rect(
            screen, secondary, (self.x, self.y, width * (self.hp / self.max_hp), height)
        )
