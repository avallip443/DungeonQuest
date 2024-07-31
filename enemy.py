import pygame

class Enemy:
    def __init__(
        self,
        name: str,
        max_hp: int,
        strength: int,
        crit_chance: int,
        potions: int,
    ):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.crit_chance = crit_chance
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.action = 'idle'
        self.x_pos = 0
        self.y_pos = 0
        self.hitbox = pygame.Rect(0, 0, 100, 120)


    def take_damage(self, amount: int):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.alive = False


    def heal(self, amount: int):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp


    def attack(self):
        pass
    

    def update_hitbox(self, x_pos, y_pos):
        self.hitbox.x = x_pos
        self.hitbox.y = y_pos


def create_enemy(index: int) -> Enemy:
    enemies = [
        ("Golem", 85, 15, 10, 3),
        ("Wizard2", 130, 15, 2, 3),
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

    change_scale = enemy.name in ["Brute", "Berserker"]
    scale = scale - 0.5 if change_scale else scale

    current_animation = animations[name][enemy.action]
    current_frame = current_animation.get_current_frame(scale=scale)

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    
    
    screen.blit(current_frame, (enemy.x_pos - frame_width // 2, enemy.y_pos - frame_height))
    