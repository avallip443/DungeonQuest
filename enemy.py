import pygame
from fighter import Fighter, Action


class Enemy(Fighter):
    def __init__(
        self,
        name: str,
        display_name: str,
        max_hp: int,
        strength: int,
        crit_chance: int,
        type: str,
        x_pos: int = 800,
        y_pos: int = 0,
    ):
        super().__init__(name, max_hp, strength, crit_chance, x_pos, y_pos)
        self.hitbox = pygame.Rect(0, 0, 100, 120)
        self.type = type
        self.display_name = display_name

    def walk(self, target_x: int) -> None:
        """
        Initiates the walking animation towards a target position.

        Args:
            target_x (int): x position to move to.
        """
        if self.x_pos > target_x:
            self.action = Action.WALK
            self.animation_timer = 0

    def update_walk_pos(self, target_x: int, speed: int = 10) -> None:
        """
        Updates the player's position for walking.

        Args:
            target_x (int): Target x position to reach.
            speed (int): Speed of movement.
        """
        if self.action == Action.WALK:
            if self.x_pos > target_x:
                self.x_pos = max(self.x_pos - speed, target_x)
                if self.x_pos <= target_x:
                    self.action = Action.IDLE

    def update_hitbox(
        self, x_pos: int, y_pos: int, width: int = 100, height: int = 120
    ) -> None:
        """
        Update the position of the enemy's hitbox.

        Args:
            x_pos (int): X-coordinate of the hitbox.
            y_pos (int): Y-coordinate of the hitbox.
            width (int): Width of the hitbox (default 100).
            height (int): Height of the hitbox (default 120).
        """
        if self.type == "boss":
            self.hitbox = pygame.Rect(0, 0, width, height)
        self.hitbox.topleft = (x_pos, y_pos)


def create_enemy(index: int) -> Enemy:
    """
    Create an enemy instance based on a predefined list.

    Args:
        index (int): Index of the enemy to create.

    Returns:
        Enemy: New enemy instance.

    Raises:
        ValueError: If the provided index is out of range.
    """
    enemies = [
        ("Golem", "Crystal Golem", 1, 1, 10, "enemy"),
        ("Wizard2", "Great Mage", 1, 1, 2, "enemy"),
        ("Fireworm", "Fireworm", 1, 1, 2, "enemy"),
    ]

    if 0 <= index < len(enemies):
        return Enemy(*enemies[index])
    else:
        raise ValueError(f"Invalid enemy index: {index}")


def create_boss(index: int) -> Enemy:
    """
    Create a boss enemy instance based on a predefined list.

    Args:
        index (int): Index of the boss to create.

    Returns:
        Enemy: A new boss enemy instance.

    Raises:
        ValueError: If the provided index is out of range.
    """
    bosses = [
        ("Bringer", "Bringer of Death", 100, 20, 2, "boss"),
        ("Wizard1", "Dark Mage", 75, 30, 5, "boss"),
        ("Oldking", "Old King", 75, 30, 5, "boss"),
    ]

    if 0 <= index < len(bosses):
        return Enemy(*bosses[index])
    else:
        raise ValueError(f"Invalid boss index: {index}")


def animate_enemy(
    screen: pygame.Surface, enemy: Enemy, animations: dict, scale: float
) -> None:
    """
    Render the enemy's current animation frame to the screen.

    Args:
        screen (pygame.Surface): The surface to render on.
        enemy (Enemy): The enemy to animate.
        animations (dict): The dictionary containing animations.
        scale (float): Scaling factor for the animation.
    """
    current_animation = animations[enemy.name.lower()][enemy.action.value]

    if enemy.death_animation_done:
        current_frame = current_animation.get_last_death_frame(scale=scale)
    else:
        current_frame = current_animation.get_current_frame(scale=scale)

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = enemy.x_pos - frame_width // 2
    y_pos = enemy.y_pos - frame_height

    screen.blit(current_frame, (x_pos, y_pos))
