import pygame
from constants import RED, GREEN


class HealthBar:
    """
    A class to represent a health bar for characters in the game.

    Attributes:
        width (int): Width of the health bar.
        height (int): Height of the health bar.
        max_hp (int): Maximum HP of the character.
        base_colour (tuple): RGB colour used for the base (empty) health bar.
        secondary_colour (tuple): RGB colour used for the current health bar.
    """

    def __init__(
        self,
        width: int,
        height: int,
        max_hp: int,
        base_colour=RED,
        secondary_colour=GREEN,
    ):
        """
        Initialize the HealthBar with the given dimensions and colours.

        Args:
            width (int): Width of the health bar.
            height (int): Height of the health bar.
            max_hp (int): Maximum health points of the character.
            base_colour (tuple): Color for the base (empty) health bar. Default is RED.
            secondary_colour (tuple): Color for the current health bar. Default is GREEN.
        """
        self.width = width
        self.height = height
        self.max_hp = max_hp
        self.base_colour = base_colour
        self.secondary_colour = secondary_colour

    def draw(self, screen: pygame.Surface, hp: int, x: int, y: int) -> None:
        """
        Draw the health bar on the screen.

        Args:
            screen (pygame.Surface): Surface to draw the health bar on.
            hp (int): Current health points of the character.
            x (int): X-coordinate for the top-left corner of the health bar.
            y (int): Y-coordinate for the top-left corner of the health bar.
        """
        pygame.draw.rect(screen, self.base_colour, (x, y, self.width, self.height))
        current_width = self.width * (hp / self.max_hp)
        pygame.draw.rect(
            screen, self.secondary_colour, (x, y, current_width, self.height)
        )
