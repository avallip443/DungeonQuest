from random import randint, random
import math
from animations import load_character_animations
from enum import Enum
from battle import display_action_text


class Action(Enum):
    IDLE = "idle"
    ATTACK = "attack"
    SPECIAL = "special"
    HURT = "hurt"
    DEATH = "death"
    WALK = "walk"


class Fighter:
    def __init__(
        self,
        name: str,
        max_hp: int,
        strength: int,
        crit_chance: int,
        x_pos: int,
        y_pos: int,
    ):
        self.name: str = name
        self.max_hp: int = max_hp
        self.hp: int = max_hp
        self.strength: int = strength
        self.crit_chance: int = crit_chance

        self.alive: bool = True
        self.action: Action = Action.IDLE
        self.delayed_damage: int = 0

        self.x_pos: int = x_pos
        self.y_pos: int = y_pos

        self.animation_timer: int = 0
        self.delay_counter: int = 0
        self.current_frame_index: int = 0
        self.animations = load_character_animations()

        self.death_animation_done: bool = False
        self.death_animation_timer: int = 0

    def take_damage(self, damage: int) -> None:
        """
        Apply delayed damage to the fighter.

        Args:
            damage (int): Amount of damage to be taken.
        """
        self.delayed_damage = damage
        self.alive = self.hp > 0
        self.delay_counter = 10

    def attack(self) -> int:
        """
        Calculate the damage dealt by the fighter.

        Returns:
            int: Damage value including potential critical hit.
        """
        damage = self.strength + randint(-5, 5)
        self.action = Action.ATTACK
        self.animation_timer = 0

        if random() < self.crit_chance / 100:
            damage *= 1.5
            display_action_text(target=self, text="Critical hit!", colour=(0, 0, 255))

        return math.floor(damage)

    def apply_damage(self) -> None:
        """
        Apply damage and update the action based on remaining HP.
        """
        self.hp = max(self.hp - self.delayed_damage, 0)
        self.alive = self.hp > 0

        self.action = Action.HURT if self.alive else Action.DEATH
        self.animation_timer = 0

        display_action_text(target=self, text=self.delayed_damage, colour=(255, 0, 0))
        self.delayed_damage = 0

    def update_animation(self) -> None:
        """
        Update the fighter's animation and process delayed actions like applying damage.
        """
        if self.delay_counter > 0:
            self.delay_counter -= 1
            if self.delay_counter == 0:
                self.apply_damage()
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
                self.current_frame_index = (
                    self.current_frame_index + 1
                ) % animation_length
                if self.action != Action.WALK:
                    self.action = Action.IDLE
