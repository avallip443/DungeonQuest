import pygame
from fighter import Fighter, Action


class Enemy(Fighter):
    def __init__(
        self,
        name: str,
        max_hp: int,
        strength: int,
        crit_chance: int,
    ):
        super().__init__(name, max_hp, strength, crit_chance, x_pos=800, y_pos=0)
        self.hitbox = pygame.Rect(0, 0, 100, 120)

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

    def update_hitbox(self, x_pos: int, y_pos: int) -> None:
        """
        Update the position of the enemy's hitbox.

        Args:
            x_pos (int): x-coordinate of the hitbox.
            y_pos (int): y-coordinate of the hitbox.
        """

        self.hitbox.topleft = (x_pos, y_pos)


def create_enemy(index: int) -> Enemy:
    """
    Create an enemy instance based on a predefined list in game.py.

    Args:
        index (int): Index of the enemy to create.

    Returns:
        Enemy: ANew enemy instance.

    Raises:
        ValueError: If the provided index is out of range.
    """

    enemies = [
        ("Golem", 1, 1, 10),
        ("Wizard2", 1, 1, 2),
    ]

    if 0 <= index <= len(enemies):
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
        ("Bringer", 100, 20, 2),
        ("Wizard1", 75, 30, 5),
    ]

    if 0 <= index <= len(bosses):
        return Enemy(*bosses[index])
    else:
        raise ValueError(f"Invalid enemy index: {index}")


def animate_enemy(screen, enemy: Enemy, animations, scale: float) -> None:
    """
    Render the enemy's current animation frame to the screen.

    Args:
        screen (pygame.Surface): The surface to render on.
        enemy (Enemy): The enemy to animate.
        animations (dict): The dictionary containing animations.
        scale (float): Scaling factor for the animation.
    """

    name = "Bringer" if enemy.name == "Bringer of Death" else enemy.name

    change_scale = enemy.name in ["boss1", "boss2"]
    scale = scale - 0.5 if change_scale else scale

    current_animation = animations[name.lower()][enemy.action.value]

    if enemy.death_animation_done:
        current_frame = current_animation.get_last_death_frame(scale=scale)
    else:
        current_frame = current_animation.get_current_frame(scale=scale)

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = enemy.x_pos - frame_width // 2
    y_pos = enemy.y_pos - frame_height

    screen.blit(current_frame, (x_pos, y_pos))
