import pygame
from constants import FONT


class ActionText(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, action_text: str, colour: tuple[int, int, int], delay: int):
        """
        Initializes the ActionText sprite.

        Args:
            x (int): X-coordinate for the center of the text.
            y (int): Y-coordinate for the center of the text.
            action_text (str): Text to display.
            colour (Tuple[int, int, int]): RGB color for the text.
            delay (int): Number of frames to delay before displaying the text.
        """
        super().__init__()
        self.image = FONT.render(action_text, True, colour)
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = -delay  # start at negative
        self.delay = delay
        self.action_text = action_text
        self.can_render = False

    def update(self) -> bool:        
        self.counter += 1
        if self.counter >= 0:
            self.rect.y -= 2
        
        if self.counter > 15 + max(0, -self.counter):
            self.kill()
        
        

