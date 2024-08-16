import pygame
import json


class Spritesheet:
    def __init__(self, filename: str, frame_width: int, frame_height: int):
        """
        Initializes the Spritesheet object by loading the image and corresponding metadata.

        Args:
            filename (str): Path to the spritesheet image file.
            frame_width (int): Width of each frame in the spritesheet.
            frame_height (int): The height of each frame in the spritesheet.
        """
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.meta_data = self.filename.replace("png", "json")
        self.frame_width = frame_width
        self.frame_height = frame_height
        with open(self.meta_data) as f:
            self.data = json.load(f)

    def get_sprite(self, x: int, y: int, w: int, h: int) -> pygame.Surface:
        """
        Extracts a single sprite from the spritesheet.

        Args:
            x (int): X-coordinate of the sprite on the spritesheet.
            y (int): Y-coordinate of the sprite on the spritesheet.
            w (int): Width of the sprite.
            h (int): Height of the sprite.

        Returns:
            pygame.Surface: Extracted sprite.
        """
        sprite = pygame.Surface((w, h), pygame.SRCALPHA)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, name: str) -> pygame.Surface:
        """
        Parses and fetches a specific sprite by name.

        Args:
            name (str): Name of the sprite.

        Returns:
            pygame.Surface: Extracted and size-adjusted sprite.
        """
        sprite_data = self.data["frames"][name]["frame"]
        x, y, w, h = (
            sprite_data["x"],
            sprite_data["y"],
            sprite_data["w"],
            sprite_data["h"],
        )
        sprite = self.get_sprite(x, y, w, h)
        fixed_size_sprite = self.fix_size(sprite, self.frame_width, self.frame_height)
        return fixed_size_sprite

    def add_outline(
        self, image: pygame.Surface, outline_color=(0, 0, 0), outline_thickness=10
    ) -> pygame.Surface:
        """
        Adds an outline to the given sprite image.

        Args:
            image (pygame.Surface): Sprite image to outline.
            outline_color (tuple): Colour of the outline. Defaults to black.
            outline_thickness (int): Thickness of the outline. Defaults to 10.

        Returns:
            pygame.Surface: Sprite image with an added outline.
        """
        mask = pygame.mask.from_surface(image)
        outline = mask.outline()
        outline_image = pygame.Surface(
            (
                image.get_width() + outline_thickness * 2,
                image.get_height() + outline_thickness * 2,
            ),
            pygame.SRCALPHA,
        )
        for point in outline:
            outline_image.set_at(
                (point[0] + outline_thickness, point[1] + outline_thickness),
                outline_color,
            )
        outline_image.blit(image, (outline_thickness, outline_thickness))
        return outline_image

    def fix_size(
        self, image: pygame.Surface, width: int, height: int
    ) -> pygame.Surface:
        """
        Adjusts the size of the sprite and centers it within a fixed surface.

        Args:
            image (pygame.Surface): Sprite image to adjust.
            width (int): Target width of the fixed surface.
            height (int): Target height of the fixed surface.

        Returns:
            pygame.Surface: Adjusted, centered sprite.
        """
        image_with_outline = self.add_outline(image)
        fixed_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        fixed_surface.fill((0, 0, 0, 0))
        x_offset = (width - image_with_outline.get_width()) // 2
        y_offset = height - image_with_outline.get_height()
        fixed_surface.blit(image_with_outline, (x_offset, y_offset))
        return fixed_surface
