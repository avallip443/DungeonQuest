import pygame
from spritesheet import Spritesheet

# constants
FRAME_WIDTH = 250
FRAME_HEIGHT = 300
ANIMATION_SPEED = 10


class Animation:
    def __init__(self, spritesheet, frame_names, frame_width, frame_height):
        self.frames = [spritesheet.parse_sprite(name) for name in frame_names]
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.current_frame = 0
        self.animation_speed = ANIMATION_SPEED
        self.clock = pygame.time.Clock()

    def get_current_frame(self, scale=1):
        frame = self.frames[self.current_frame]
        if scale != 1:
            frame = pygame.transform.scale(
                frame, (int(self.frame_width * scale), int(self.frame_height * scale))
            )
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.clock.tick(self.animation_speed)
        return frame

    def get_frame_count(self):
        return len(self.frames)


def load_character_animations():
    animations = {}

    def load_spritesheet(folder, name, action):
        return Spritesheet(
            f"graphics/{folder}/{name}/{name}_{action}.png", FRAME_WIDTH, FRAME_HEIGHT
        )

    def create_animation_dict(name, frames_dict):
        return {
            action: Animation(
                load_spritesheet(folder, name, action),
                frames,
                FRAME_WIDTH,
                FRAME_HEIGHT,
            )
            for action, frames in frames_dict.items()
        }

    def generate_frame_names(count, reverse=False):
        frames = [f"{i}.png" for i in range(1, count + 1)]
        return frames[::-1] if reverse else frames

    character_animations = {
        "berserker": {
            "attack": generate_frame_names(7),
            "death": generate_frame_names(7),
            "hurt": generate_frame_names(3),
            "idle": generate_frame_names(10),
            "special": generate_frame_names(8),
        },
        "brute": {
            "attack": generate_frame_names(7),
            "death": generate_frame_names(11),
            "hurt": generate_frame_names(4),
            "idle": generate_frame_names(11),
            "special": generate_frame_names(7),
        },
        "huntress": {
            "attack": generate_frame_names(6),
            "death": generate_frame_names(10),
            "hurt": generate_frame_names(3),
            "idle": generate_frame_names(10),
            "special": generate_frame_names(6),
        },
        "rouge": {
            "attack": generate_frame_names(4),
            "death": generate_frame_names(6),
            "hurt": generate_frame_names(4),
            "idle": generate_frame_names(8),
            "special": generate_frame_names(4),
        },
        "warrior": {
            "attack": generate_frame_names(4),
            "death": generate_frame_names(9),
            "hurt": generate_frame_names(3),
            "idle": generate_frame_names(10),
            "special": generate_frame_names(5),
        },
        "wizard1": {
            "attack": generate_frame_names(8, reverse=True),
            "death": generate_frame_names(7, reverse=True),
            "hurt": generate_frame_names(3, reverse=True),
            "idle": generate_frame_names(8, reverse=True),
        },
        "wizard2": {
            "attack": generate_frame_names(13, reverse=True),
            "death": generate_frame_names(18, reverse=True),
            "hurt": generate_frame_names(3, reverse=True),
            "idle": generate_frame_names(10, reverse=True),
        },
        "golem": {
            "attack": generate_frame_names(11, reverse=True),
            "death": generate_frame_names(13, reverse=True),
            "hurt": generate_frame_names(4, reverse=True),
            "idle": generate_frame_names(8, reverse=True),
        },
        "bringer": {
            "attack": generate_frame_names(10),
            "death": generate_frame_names(11),
            "hurt": generate_frame_names(3),
            "idle": generate_frame_names(8),
        },
    }

    for name, frames in character_animations.items():
        folder = (
            "characters"
            if name in ["berserker", "brute", "huntress", "rouge", "warrior"]
            else "enemies"
        )
        animations[name] = create_animation_dict(name, frames)

    return animations
