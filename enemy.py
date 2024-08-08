import pygame
from random import randint, random
import math
from animations import load_character_animations
from enum import Enum
from battle import display_damage


class Action(Enum):
    IDLE = "idle"
    ATTACK = "attack"
    SPECIAL = "special"
    HURT = "hurt"
    DEATH = "death"
    WALK = "walk"


class Enemy:
    def __init__(
        self,
        name: str,
        max_hp: int,
        strength: int,
        crit_chance: int,
    ):
        self.name: str = name
        self.max_hp: int = max_hp
        self.hp: int = max_hp
        self.strength: int = strength
        self.crit_chance: int = crit_chance

        self.alive: bool = True
        self.action: Action = Action.IDLE
        self.delayed_damage: int = 0

        self.x_pos: int = 800
        self.y_pos: int = 0
        self.hitbox = pygame.Rect(0, 0, 100, 120)

        self.animation_timer: int = 0
        self.delay_counter: int = 0
        self.current_frame_index: int = 0
        self.animations = load_character_animations()

        self.death_animation_done: bool = False
        self.death_animation_timer: int = 0

    def take_damage(self, damage: int) -> None:
        """
        Apply delayed damage to the enemy.

        Args:
            damage (int): Amount of damage to be taken.
        """

        self.delayed_damage = damage
        self.active = self.hp > 0
        self.delay_counter = 10

    def attack(self) -> int:
        """
        Calculate the damage dealt by the enemy.

        Returns:
            int: Damage value including potential critical hit.
        """

        damage = self.strength + randint(-5, 5)
        self.action = Action.ATTACK

        if random() < self.crit_chance / 100:
            damage += 1.5

        return math.floor(damage)

    def appy_damage(self) -> None:
        """
        Apply damage and update the action based on remaining HP
        """

        self.hp = max(self.hp - self.delayed_damage, 0)
        self.alive = self.hp > 0
        self.action = Action.HURT if self.alive else Action.DEATH
        display_damage(self, self.delayed_damage, (255, 0, 0))
        self.delayed_damage = 0

    def walk(self, target_x: int) -> None:
        """
        Initiates the walking animation towards a target position.

        Args:
            target_x (int): x position to move to.
        """
        if self.x_pos > target_x:
            self.action = Action.WALK

    def update_walk_pos(self, target_x: int, speed: int = 10) -> None:
        """
        Updates the player's position for walking.

        Args:
            target_x (int): Target x position to reach.
            speed (int): Speed of movement.
        """

        if self.action == Action.WALK:
            if self.x_pos > target_x:
                self.x_pos -= speed
                if self.x_pos <= target_x:
                    self.x_pos = target_x
                    self.action = Action.IDLE

    def update_hitbox(self, x_pos: int, y_pos: int) -> None:
        """
        Update the position of the enemy's hitbox.

        Args:
            x_pos (int): x-coordinate of the hitbox.
            y_pos (int): y-coordinate of the hitbox.
        """

        self.hitbox.x = x_pos
        self.hitbox.y = y_pos

    def update_animation(self) -> None:
        """
        Update the enemy's animation based on the current action and timers.
        """

        if self.delay_counter > 0:
            self.delay_counter -= 1
            if self.delay_counter == 0:
                self.appy_damage()
            return

        current_animation = self.animations[self.name.lower()][self.action.value]
        animation_length = current_animation.get_frame_count()

        if self.action == Action.DEATH:
            self.update_death_animation(animation_length)
        else:
            self.update_regular_animation(animation_length)

    def update_death_animation(self, animation_length: int) -> None:
        """
        Update death animation to ensure it runs only once.
        """

        if not self.death_animation_done:
            self.death_animation_timer += 1
            if self.death_animation_timer >= animation_length:
                self.death_animation_done = True

    def update_regular_animation(self, animation_length: int) -> None:
        """
        Update animations for actions other than death.
        """

        if self.action != Action.IDLE:
            self.animation_timer += 1
            if self.animation_timer >= animation_length:
                self.animation_timer = 0
                self.current_frame_index = 0
                if self.action in [Action.HURT, Action.ATTACK, Action.SPECIAL]:
                    self.action = Action.IDLE


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
        ("Bringer of Death", 100, 20, 2, 3),
        ("Wizard1", 75, 30, 5, 3),
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
