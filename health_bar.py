import pygame
from constants import RED, GREEN


class HealthBar:
    """
    A class to represent a health bar for characters in the game.

    Attributes:
        width (int): Width of the health bar.
        height (int): Height of the health bar.
        max_hp (int): Maximum HP of the character.
        base_color (tuple): RGB color used for the base (empty) health bar.
        secondary_color (tuple): RGB color used for the current health bar.
    """

    def __init__(
        self,
        width: int,
        height: int,
        max_hp: int,
        base_color=RED,
        secondary_color=GREEN,
    ):
        """
        Initialize the HealthBar with the given dimensions and colors.

        Args:
            width (int): Width of the health bar.
            height (int): Height of the health bar.
            max_hp (int): Maximum health points of the character.
            base_color (tuple): Color for the base (empty) health bar. Default is RED.
            secondary_color (tuple): Color for the current health bar. Default is GREEN.
        """
        self.width = width
        self.height = height
        self.max_hp = max_hp
        self.base_color = base_color
        self.secondary_color = secondary_color

    def draw(self, screen: pygame.Surface, hp: int, x: int, y: int) -> None:
        """
        Draw the health bar on the screen.

        Args:
            screen (pygame.Surface): Surface to draw the health bar on.
            hp (int): Current health points of the character.
            x (int): X-coordinate for the top-left corner of the health bar.
            y (int): Y-coordinate for the top-left corner of the health bar.
        """
        pygame.draw.rect(screen, self.base_color, (x, y, self.width, self.height))
        current_width = self.width * (hp / self.max_hp)
        pygame.draw.rect(
            screen, self.secondary_color, (x, y, current_width, self.height)
        )
