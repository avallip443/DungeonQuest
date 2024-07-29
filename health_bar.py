import pygame
from constants import RED, GREEN, WIDTH, HEIGHT, PANEL_HEIGHT


class HealthBar:
    def __init__(self, x_offset: int, y_offset: int, hp: int, max_hp: int):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, screen, hp: int, base=RED, secondary=GREEN, width=230, height=20):
        self.hp = hp
        x_pos = WIDTH // 4 - width // 2 + self.x_offset
        y_pos = HEIGHT - PANEL_HEIGHT + self.y_offset
        
        pygame.draw.rect(screen, base, (x_pos, y_pos, width, height))
        
        pygame.draw.rect(
            screen, secondary, (x_pos, y_pos, width * (self.hp / self.max_hp), height)
        )
        
