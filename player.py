from random import randint, random
import math
from animations import load_character_animations


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
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.crit_chance = crit_chance
        self.double_chance = double_chance
        self.potion_chance = potion_chance
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.action = "idle"
        self.x_pos = 0
        self.y_pos = 0
        self.animation_timer = 0
        self.current_frame_index = 0
        self.animations = load_character_animations()
        self.delay_counter = 0

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            # self.action = "death"
        else:
            self.delay_counter = 10
        self.action = "idle"

    def heal(self):
        heal = 30 + randint(-5, 5)
        self.hp = min(self.hp + heal, self.max_hp)
        self.potions -= 1
        return heal

    def attack(self):
        special_attack = False
        damage = self.strength + randint(-5, 5)

        if random() < self.crit_chance / 100:
            damage += 1.5
            special_attack = True

        if random() < self.double_chance / 100:
            damage * 2
            special_attack = True

        self.action = "special" if special_attack else "attack"
        return math.floor(damage)

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


def create_character(index: int) -> Player:
    characters = [
        ("Warrior", 100, 20, 2, 2, 50, 3),
        ("Rouge", 85, 15, 10, 2, 55, 3),
        ("Berserker", 75, 30, 5, 10, 60, 3),
        ("Brute", 130, 15, 2, 2, 50, 3),
        ("Huntress", 85, 10, 10, 25, 45, 3),
    ]

    if 0 <= index <= len(characters):
        return Player(*characters[index])
    else:
        raise ValueError(f"Invalid character index: {index}")


def animate_player(screen, player, animations, scale):
    change_scale = player.name in ["Brute", "Berserker"]
    scale = scale - 0.5 if change_scale else scale

    current_animation = animations[player.name][player.action]
    current_frame = current_animation.get_current_frame(scale=scale)

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = player.x_pos - frame_width // 2
    y_pos = player.y_pos - frame_height

    screen.blit(current_frame, (x_pos, y_pos))
