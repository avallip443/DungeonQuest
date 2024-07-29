class Enemy:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        name: str,
        max_hp: int,
        strength: int,
        crit_chance: int,
        potions: int,
    ):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.crit_chance = crit_chance
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


def create_enemy(index: int) -> Enemy:
    enemies = [
        (200, 150, "Bringer of Death", 100, 20, 2, 3),
        (300, 150, "Golem", 85, 15, 10, 3),
        (400, 150, "Wizard1", 75, 30, 5, 3),
        (500, 150, "Wizard2", 130, 15, 2, 3),
        (600, 150, "Enemy", 85, 10, 10, 3),
    ]

    if 0 <= index <= len(enemies):
        return Enemy(*enemies[index])
    else:
        raise ValueError(f"Invalid enemy index: {index}")
