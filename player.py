from random import randint, random
from fighter import Fighter, Action


class Player(Fighter):
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
        super().__init__(name, max_hp, strength, crit_chance, x_pos=0, y_pos=0)
        self.double_chance: int = double_chance
        self.potion_chance: int = potion_chance
        self.potions: int = potions

    def heal(self) -> int:
        """
        Calculate the heal amount from the potion use.

        Returns:
            int: Heal amount to player's health.
        """

        heal_amount = 30 + randint(-5, 5)
        self.hp = min(self.hp + heal_amount, self.max_hp)
        self.potions -= 1
        return heal_amount

    def attack(self) -> int:
        """
        Calculate the damage dealt by the player.

        Returns:
            int: Damage value including potential critical hit.
        """
        damage = super().attack()

        if random() < self.double_chance / 100:
            damage *= 2
            self.action = Action.SPECIAL

        return damage

    def get_potion(self) -> None:
        """
        Increases the player's potion count based on potion_chance after an enemy dies.

        Returns:
            bool: True if a potion was received, False otherwise.
        """
        if random() < self.potion_chance / 100:
            self.potions += 1
            return True
        return False

    def walk(self, target_x: int) -> None:
        """
        Initiates the walking animation towards a target position.

        Args:
            target_x (int): x position to move to.
        """
        if self.x_pos < target_x:
            self.action = Action.WALK
            self.animation_timer = 0

    def update_walk_pos(self, target_x: int, speed: int = 5) -> None:
        """
        Updates the player's position for walking.

        Args:
            target_x (int): Target x position to reach.
            speed (int): Speed of movement.
        """

        if self.action == Action.WALK:
            if self.x_pos < target_x:
                self.x_pos = min(self.x_pos + speed, target_x)
                if self.x_pos >= target_x:
                    self.action = Action.IDLE


def create_character(index: int) -> Player:
    characters = [
        ("Warrior", 100, 20, 2, 2, 50, 3),
        ("Rouge", 85, 15, 10, 2, 55, 3),
        ("Berserker", 75, 30, 5, 10, 60, 3),
        ("Brute", 130, 15, 2, 2, 100, 3),
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

    if player.death_animation_done:
        current_frame = current_animation.get_last_death_frame(scale=scale)
    else:
        current_frame = current_animation.get_current_frame(scale=scale)

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = player.x_pos - frame_width // 2
    y_pos = player.y_pos - frame_height

    screen.blit(current_frame, (x_pos, y_pos))
