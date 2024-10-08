import pygame


class Button:
    def __init__(
        self,
        surface: pygame.Surface,
        x: int,
        y: int,
        image: pygame.Surface,
        width: int,
        height: int,
    ):
        """
        Initialize a Button object.

        Args:
            surface (pygame.Surface): Surface on which the button will be drawn.
            x (int): X-coordinate for the button's center position.
            y (int): Y-coordinate for the button's center position.
            image (pygame.Surface): Image representing the button.
            width (int): Width of the button.
            height (int): Height of the button.
        """
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.clicked = False
        self.surface = surface

    def draw(self) -> bool:
        """
        Draw the button on the surface and handle click events.

        Returns:
            bool: True if the button was clicked, False otherwise.
        """
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
