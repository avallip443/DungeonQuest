import pygame
from spritesheet import Spritesheet

# constants
FRAME_WIDTH = 250
FRAME_HEIGHT = 300
ANIMATION_SPEED = 10


class Animation:
    def __init__(
        self,
        spritesheet: Spritesheet,
        frame_names: list[str],
        frame_width: int,
        frame_height: int,
    ):
        """
        Initializes the Animation object.

        Args:
            spritesheet (Spritesheet): Spritesheet containing the animation frames.
            frame_names (list[str]): List of frame to be used in the animation.
            frame_width (int): Width of each frame.
            frame_height (int): Height of each frame.
        """
        self.frames = [spritesheet.parse_sprite(name) for name in frame_names]
        self.frame_width: int = frame_width
        self.frame_height: int = frame_height
        self.current_frame: int = 0
        self.animation_speed: int = ANIMATION_SPEED
        self.clock = pygame.time.Clock()

    def get_current_frame(self, scale: float = 1) -> pygame.Surface:
        """
        Gets the current, scaled frame of the animation.

        Args:
            scale (float): Scale for the frame. Defaults to 1.

        Returns:
            pygame.Surface: The current animation frame.
        """
        frame = self.frames[self.current_frame]
        if scale != 1:
            frame = pygame.transform.scale(
                frame, (int(self.frame_width * scale), int(self.frame_height * scale))
            )
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.clock.tick(self.animation_speed)
        return frame

    def get_frame_count(self) -> int:
        """
        Returns the number of frames in the animation.

        Returns:
            int: Number of frames in the animation.
        """
        return len(self.frames)

    def get_last_death_frame(self, scale: float = 1) -> pygame.Surface:
        """
        Gets the last scaled frame of the death animation.

        Args:
            scale (float): Scale for the frame. Defaults to 1.

        Returns:
            pygame.Surface: Last frame of the death animation.
        """
        frame = self.frames[-1]
        if scale != 1:
            frame = pygame.transform.scale(
                frame, (int(self.frame_width * scale), int(self.frame_height * scale))
            )
        return frame


def load_character_animations() -> dict[str, dict[str, Animation]]:
    """
    Loads and returns a dictionary of character animations.

    Returns:
        dict: Dictionary where keys are character names and values are dictionaries of animations.
    """
    animations = {}

    def load_spritesheet(folder: str, name: str, action: str) -> Spritesheet:
        """
        Loads a spritesheet for a specific character action.

        Args:
            folder (str): Folder containing the character spritesheets.
            name (str): Name of the character.
            action (str): Action of the character.

        Returns:
            Spritesheet: Loaded spritesheet.
        """
        return Spritesheet(
            f"graphics/{folder}/{name}/{name}_{action}.png", FRAME_WIDTH, FRAME_HEIGHT
        )

    def create_animation_dict(
        name: str, frames_dict: dict[str, list[str]]
    ) -> dict[str, Animation]:
        """
        Creates a dictionary of animations for a character.

        Args:
            name (str): Name of the character.
            frames_dict (dict[str, list[str]]): Dictionary where keys are actions and values are lists of frames.

        Returns:
            dict: Dictionary where keys are actions and values are Animation objects.
        """
        return {
            action: Animation(
                load_spritesheet(folder, name, action),
                frames,
                FRAME_WIDTH,
                FRAME_HEIGHT,
            )
            for action, frames in frames_dict.items()
        }

    def generate_frame_names(count: int, reverse: bool = False) -> list[str]:
        """
        Generates a list of frame filenames.

        Args:
            count (int): Number of frames.
            reverse (bool): Whether to reverse the frame order. Defaults to False.

        Returns:
            list[str]: List of frames.
        """
        frames = [f"{i}.png" for i in range(1, count + 1)]
        return frames[::-1] if reverse else frames

    character_animations = {
        # players
        "berserker": {
            "attack": generate_frame_names(7),
            "death": generate_frame_names(7),
            "hurt": generate_frame_names(3),
            "idle": generate_frame_names(10),
            "special": generate_frame_names(8),
            "walk": generate_frame_names(8),
        },
        "brute": {
            "attack": generate_frame_names(7),
            "death": generate_frame_names(11),
            "hurt": generate_frame_names(4),
            "idle": generate_frame_names(11),
            "special": generate_frame_names(7),
            "walk": generate_frame_names(8),
        },
        "huntress": {
            "attack": generate_frame_names(6),
            "death": generate_frame_names(10),
            "hurt": generate_frame_names(3),
            "idle": generate_frame_names(10),
            "special": generate_frame_names(6),
            "walk": generate_frame_names(8),
        },
        "rogue": {
            "attack": generate_frame_names(4),
            "death": generate_frame_names(6),
            "hurt": generate_frame_names(4),
            "idle": generate_frame_names(8),
            "special": generate_frame_names(4),
            "walk": generate_frame_names(8),
        },
        "warrior": {
            "attack": generate_frame_names(4),
            "death": generate_frame_names(9),
            "hurt": generate_frame_names(3),
            "idle": generate_frame_names(10),
            "special": generate_frame_names(5),
            "walk": generate_frame_names(6),
        },
        # enemies
        "witch": {
            "attack": generate_frame_names(13, reverse=True),
            "death": generate_frame_names(18, reverse=True),
            "hurt": generate_frame_names(3, reverse=True),
            "idle": generate_frame_names(10, reverse=True),
            "walk": generate_frame_names(8, reverse=True),
        },
        "fireworm": {
            "attack": generate_frame_names(16, reverse=True),
            "death": generate_frame_names(8, reverse=True),
            "hurt": generate_frame_names(3, reverse=True),
            "idle": generate_frame_names(9, reverse=True),
            "walk": generate_frame_names(9, reverse=True),
        },
        "golem": {
            "attack": generate_frame_names(11, reverse=True),
            "death": generate_frame_names(13, reverse=True),
            "hurt": generate_frame_names(4, reverse=True),
            "idle": generate_frame_names(8, reverse=True),
            "walk": generate_frame_names(10, reverse=True),
        },
        # bosses
        "bringer": {
            "attack": generate_frame_names(10),
            "death": generate_frame_names(11),
            "hurt": generate_frame_names(3),
            "idle": generate_frame_names(8),
            "walk": generate_frame_names(8),
        },
        "oldking": {
            "attack": generate_frame_names(4, reverse=True),
            "death": generate_frame_names(6, reverse=True),
            "hurt": generate_frame_names(4, reverse=True),
            "idle": generate_frame_names(8, reverse=True),
            "walk": generate_frame_names(8, reverse=True),
        },
        "mage": {
            "attack": generate_frame_names(8, reverse=True),
            "death": generate_frame_names(7, reverse=True),
            "hurt": generate_frame_names(3, reverse=True),
            "idle": generate_frame_names(8, reverse=True),
        },
    }

    for name, frames in character_animations.items():
        folder = (
            "characters"
            if name in ["berserker", "brute", "huntress", "rogue", "warrior"]
            else "enemies"
        )
        animations[name] = create_animation_dict(name, frames)

    return animations
