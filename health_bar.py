import pygame
from constants import RED, GREEN


class HealthBar:
    def __init__(self, width: int, height: int, hp: int, max_hp: int):
        self.width = width
        self.height = height
        self.hp = hp
        self.max_hp = max_hp
        

    def draw(self, screen, hp: int, x, y, base=RED, secondary=GREEN):
        self.hp = hp
        
        pygame.draw.rect(screen, base, (x, y, self.width, self.height))
        pygame.draw.rect(
            screen, secondary, (x, y, self.width * (self.hp / self.max_hp), self.height)
        )
        
