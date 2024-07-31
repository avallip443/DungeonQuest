class Player:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
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


def create_character(index: int) -> Player:
    characters = [
        (100, 150, 'Warrior', 100, 20, 2, 2, 50, 3),
        (100, 150, 'Rouge', 85, 15, 10, 2, 55, 3),
        (100, 150, "Berserker", 75, 30, 5, 10, 60, 3),
        (100, 150, "Brute", 130, 15, 2, 2, 50, 3),
        (100, 150, "Huntress", 85, 10, 10, 25, 45, 3),
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
