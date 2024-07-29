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
    
    