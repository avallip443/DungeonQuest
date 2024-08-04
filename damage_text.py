import pygame
from constants import FONT


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, damage: str, colour: tuple[int, int, int]):
        super().__init__()
        self.image = FONT.render(damage, True, colour)
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0

    def update(self) -> None:
        self.rect.y -= 1
        self.counter += 1

        if self.counter > 10:
            self.kill()


damage_text_group = pygame.sprite.Group()
