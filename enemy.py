import pygame
from random import randint, random
import math


class Enemy:
    def __init__(
        self,
        name: str,
        max_hp: int,
        strength: int,
        crit_chance: int,
    ):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.crit_chance = crit_chance
        self.alive = True
        self.action = "idle"
        self.x_pos = 0
        self.y_pos = 0
        self.hitbox = pygame.Rect(0, 0, 100, 120)
        self.action_cooldown = 10

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def attack(self):
        damage = self.strength + randint(-5, 5)

        if random() < self.crit_chance / 100:
            damage += 1.5

        return math.floor(damage)

    def update_hitbox(self, x_pos, y_pos):
        self.hitbox.x = x_pos
        self.hitbox.y = y_pos


def create_enemy(index: int) -> Enemy:
    enemies = [
        ("Golem", 85, 15, 10),
        ("Wizard2", 130, 15, 2),
    ]

    if 0 <= index <= len(enemies):
        return Enemy(*enemies[index])
    else:
        raise ValueError(f"Invalid enemy index: {index}")


def create_boss(index: int, x_pos: int, y_pos: int) -> Enemy:
    frame_width, frame_height = 250, 300
    enemies = [
        ("Bringer of Death", 100, 20, 2, 3, x_pos, y_pos, frame_width, frame_height),
        ("Wizard1", 75, 30, 5, 3, x_pos, y_pos, frame_width, frame_height),
    ]

    if 0 <= index <= len(enemies):
        return Enemy(*enemies[index])
    else:
        raise ValueError(f"Invalid enemy index: {index}")


def animate_enemy(screen, enemy, animations, scale):
    name = "Bringer" if enemy.name == "Bringer of Death" else enemy.name

    change_scale = enemy.name in ["boss1", "boss2"]
    scale = scale - 0.5 if change_scale else scale

    current_animation = animations[name][enemy.action]
    current_frame = current_animation.get_current_frame(scale=scale)

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = enemy.x_pos - frame_width // 2
    y_pos = enemy.y_pos - frame_height

    screen.blit(current_frame, (x_pos, y_pos))
