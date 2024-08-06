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


class Player:
    def __init__(
        self,
        name: str,
        max_hp: int,
        strength: int,
        crit_chance: int,
        double_chance: int,
        potion_chance: int,
        potions: int,
    ):
        self.name: str = name
        self.max_hp: int = max_hp
        self.hp: int = max_hp
        self.strength: int = strength
        self.crit_chance: int = crit_chance
        self.double_chance: int = double_chance
        self.potion_chance: int = potion_chance
        self.potions: int = potions

        self.alive: bool = True
        self.action: Action = Action.IDLE
        self.x_pos: int = 0
        self.y_pos: int = 0
        self.animation_timer: int = 0
        self.delay_counter: int = 0
        self.current_frame_index: int = 0
        self.animations = load_character_animations()
        self.delayed_damage = 0

    def take_damage(self, damage: int) -> None:
        self.delayed_damage = damage
        self.active = self.hp > 0
        self.delay_counter = 10

    def heal(self) -> int:
        heal_amount = 30 + randint(-5, 5)
        self.hp = min(self.hp + heal_amount, self.max_hp)
        self.potions -= 1
        return heal_amount

    def attack(self) -> int:
        damage = self.strength + randint(-5, 5)
        self.action = Action.ATTACK

        if random() < self.crit_chance / 100:
            damage += 1.5
            self.action = Action.SPECIAL

        if random() < self.double_chance / 100:
            damage *= 2
            self.action = Action.SPECIAL

        return math.floor(damage)

    def walk(self, target_x: int) -> None:
        """
        Initiates the walking animation towards a target position.

        Args:
            target_x (int): x position to move to.
        """
        if self.x_pos < target_x:
            self.action = Action.WALK

    def update_walk_pos(self, target_x: int, speed: int = 5) -> None:
        """
        Updates the player's position for walking.

        Args:
            target_x (int): Target x position to reach.
            speed (int): Speed of movement.
        """

        if self.action == Action.WALK:
            if self.x_pos < target_x:
                self.x_pos += speed
                if self.x_pos >= target_x:
                    self.x_pos = target_x
                    self.action = Action.IDLE

    def update_animation(self) -> None:
        """
        Updates the player's animation and processes delayed actions like applying damage.

        Args:
            screen (pygame.Surface): Surface to render damage texts.
        """
        if self.delay_counter > 0:
            self.delay_counter -= 1
            if self.delay_counter == 0:
                self.hp = max(self.hp - self.delayed_damage, 0)
                self.alive = self.hp > 0
                self.action = Action.HURT if self.alive else Action.DEATH
                display_damage(self, self.delayed_damage, (255, 0, 0))
                self.delayed_damage = 0
            return

        current_animation = self.animations[self.name.lower()][self.action.value]
        animation_length = current_animation.get_frame_count()

        if self.action != Action.IDLE:
            self.animation_timer = (self.animation_timer + 1) % animation_length
            if self.animation_timer == 0:
                self.current_frame_index = 0
                if self.action in [Action.HURT, Action.SPECIAL]: #, Action.ATTACK]:
                    self.action = Action.IDLE


def create_character(index: int) -> Player:
    characters = [
        ("Warrior", 100, 20, 2, 2, 50, 3),
        ("Rouge", 85, 15, 10, 2, 55, 3),
        ("Berserker", 75, 30, 5, 10, 60, 3),
        ("Brute", 130, 15, 2, 2, 50, 3),
        ("Huntress", 85, 10, 10, 25, 45, 3),
    ]

    if 0 <= index < len(characters):
        return Player(*characters[index])
    else:
        raise ValueError(f"Invalid character index: {index}")


def animate_player(screen, player: Player, animations, scale: float) -> None:
    change_scale = player.name in ["Brute", "Berserker"]
    scale = scale - 0.5 if change_scale else scale

    current_animation = animations[player.name.lower()][player.action.value]
    current_frame = current_animation.get_current_frame(scale=scale)

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = player.x_pos - frame_width // 2
    y_pos = player.y_pos - frame_height

    screen.blit(current_frame, (x_pos, y_pos))
