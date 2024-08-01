import pygame
from random import randint, random
import math
from animations import load_character_animations


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
        self.animation_timer = 0
        self.current_frame_index = 0
        self.animations = load_character_animations()
        self.delay_counter = 0

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        else:
            self.delay_counter = 8
        self.action = "idle"

    def attack(self):
        special_attack = False
        damage = self.strength + randint(-5, 5)

        if random() < self.crit_chance / 100:
            damage += 1.5
            special_attack = True

        self.action = "special" if special_attack else "attack"
        return math.floor(damage)
    
    def death(self):
        self.action = "death"
        self.alive = False

    def update_hitbox(self, x_pos, y_pos):
        self.hitbox.x = x_pos
        self.hitbox.y = y_pos
        
    def update_animation(self):
        current_animation = self.animations[self.name][self.action]
        animation_length = current_animation.get_frame_count()

        if self.delay_counter > 0:
            self.delay_counter -= 1
            if self.delay_counter == 0 and self.hp > 0:
                self.action = "hurt"
            elif self.delay_counter == 0 and self.hp == 0:
                self.action = "death"
            return
        
        if self.action != "idle":
            self.animation_timer += 1

            if self.animation_timer > (animation_length):
                self.animation_timer = 0
                self.current_frame_index = 0
                
                if self.action in ["hurt", "special", "attack"]:
                    self.action = "idle"


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
