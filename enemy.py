import pygame
from random import randint, random
import math
from animations import load_character_animations
from enum import Enum


class Action(Enum):
    IDLE = "idle"
    ATTACK = "attack"
    SPECIAL = "special"
    HURT = "hurt"
    DEATH = "death"


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
        self.x_pos: int = 0
        self.y_pos: int = 0
        self.hitbox = pygame.Rect(0, 0, 100, 120)
        self.animation_timer: int = 0
        self.delay_counter: int = 0
        self.current_frame_index: int = 0
        self.animations = load_character_animations()

    def take_damage(self, damage: int) -> None:
        self.hp = max(self.hp - damage, 0)
        self.active = self.hp > 0
        self.delay_counter = 10 if self.alive else 0

    def attack(self) -> int:
        damage = self.strength + randint(-5, 5)
        self.action = Action.ATTACK

        if random() < self.crit_chance / 100:
            damage += 1.5

        return math.floor(damage)

    def update_hitbox(self, x_pos: int, y_pos: int) -> None:
        self.hitbox.x = x_pos
        self.hitbox.y = y_pos

    def update_animation(self) -> None:
        if self.delay_counter > 0:
            self.delay_counter -= 1
            if self.delay_counter == 0:
                self.action = Action.HURT if self.alive else Action.DEATH
            return

        current_animation = self.animations[self.name.lower()][self.action.value]
        animation_length = current_animation.get_frame_count()

        if self.action != Action.IDLE:
            self.animation_timer = (self.animation_timer + 1) % animation_length
            if self.animation_timer == 0:
                self.current_frame_index = 0
                if self.action in [Action.HURT, Action.ATTACK]:
                    self.action = Action.IDLE


def create_enemy(index: int) -> Enemy:
    enemies = [
        ("Golem", 85, 15, 10),
        ("Wizard2", 130, 15, 2),
    ]

    if 0 <= index <= len(enemies):
        return Enemy(*enemies[index])
    else:
        raise ValueError(f"Invalid enemy index: {index}")


def create_boss(index: int) -> Enemy:
    enemies = [
        ("Bringer of Death", 100, 20, 2, 3),
        ("Wizard1", 75, 30, 5, 3),
    ]

    if 0 <= index <= len(enemies):
        return Enemy(*enemies[index])
    else:
        raise ValueError(f"Invalid enemy index: {index}")


def animate_enemy(screen, enemy: Enemy, animations, scale: float) -> None:
    name = "Bringer" if enemy.name == "Bringer of Death" else enemy.name

    change_scale = enemy.name in ["boss1", "boss2"]
    scale = scale - 0.5 if change_scale else scale

    current_animation = animations[name.lower()][enemy.action.value]
    current_frame = current_animation.get_current_frame(scale=scale)

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = enemy.x_pos - frame_width // 2
    y_pos = enemy.y_pos - frame_height

    screen.blit(current_frame, (x_pos, y_pos))
