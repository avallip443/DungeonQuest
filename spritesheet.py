import pygame
import json


class Spritesheet:
    def __init__(self, filename, frame_width, frame_height):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.meta_data = self.filename.replace("png", "json")
        self.frame_width = frame_width
        self.frame_height = frame_height
        with open(self.meta_data) as f:
            self.data = json.load(f)

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h), pygame.SRCALPHA)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, name):
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

    def add_outline(self, image, outline_color=(0, 0, 0), outline_thickness=10):
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

    def fix_size(self, image, width, height):
        image_with_outline = self.add_outline(image)
        fixed_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        fixed_surface.fill((0, 0, 0, 0))
        x_offset = (width - image_with_outline.get_width()) // 2
        y_offset = height - image_with_outline.get_height()
        fixed_surface.blit(image_with_outline, (x_offset, y_offset))
        return fixed_surface
