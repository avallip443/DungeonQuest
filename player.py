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
        """
        Initialize a Player object with attributes for combat and movement.

        Args:
            name (str): Player's name.
            max_hp (int): Maximum health points.
            strength (int): Player's strength, affecting attack damage.
            crit_chance (int): Percentage chance for a critical hit.
            double_chance (int): Percentage chance to attack twice.
            potion_chance (int): Percentage chance to receive a potion after a battle.
            potions (int): Initial number of potions the player has.
        """
        super().__init__(name, max_hp, strength, crit_chance, x_pos=0, y_pos=0)
        self.double_chance: int = double_chance
        self.potion_chance: int = potion_chance
        self.potions: int = potions

    def heal(self) -> int:
        """
        Heals the player using a potion.

        Returns:
            int: Amount of health restored.
        """
        heal_amount = 30 + randint(-5, 5)
        self.hp = min(self.hp + heal_amount, self.max_hp)
        self.potions -= 1
        return heal_amount

    def attack(self) -> int:
        """
        Executes an attack and calculates the damage dealt.

        Returns:
            int: Total damage dealt, including any critical or double hit bonuses.
        """
        damage = super().attack()

        if random() < self.double_chance / 100:
            damage *= 2
            self.action = Action.SPECIAL

        return damage

    def get_potion(self) -> bool:
        """
        Determines if the player receives a potion after an enemy is defeated.

        Returns:
            bool: True if a potion was received, False otherwise.
        """
        if random() < self.potion_chance / 100:
            self.potions += 1
            return True
        return False

    def walk(self, target_x: int) -> None:
        """
        Initiates walking animation towards a target position.

        Args:
            target_x (int): X-coordinate to walk towards.
        """
        if self.x_pos < target_x:
            self.action = Action.WALK
            self.animation_timer = 0

    def update_walk_pos(self, target_x: int, speed: int = 5) -> None:
        """
        Updates the player's position while walking.

        Args:
            target_x (int): Target x-coordinate.
            speed (int): Movement speed. Defaults to 5.
        """
        if self.action == Action.WALK:
            self.x_pos = min(self.x_pos + speed, target_x)
            if self.x_pos >= target_x:
                self.action = Action.IDLE


def create_character(index: int) -> Player:
    """
    Creates a Player object based on the selected character index.

    Args:
        index (int): Index of the character in the list.

    Returns:
        Player: Created Player object.

    Raises:
        ValueError: If the index is invalid.
    """
    characters = [
        ("Warrior", 100, 20, 2, 2, 50, 3),
        ("Rogue", 85, 15, 10, 2, 55, 3),
        ("Berserker", 75, 30, 5, 10, 60, 3),
        ("Brute", 130, 15, 2, 2, 50, 3),
        ("Huntress", 85, 10, 10, 25, 45, 3),
    ]

    if 0 <= index < len(characters):
        return Player(*characters[index])
    else:
        raise ValueError(f"Invalid character index: {index}")


def animate_player(screen, player: Player, animations, scale: float) -> None:
    """
    Animates the player on the screen.

    Args:
        screen: Pygame surface to draw on.
        player (Player): Player character to animate.
        animations: Dictionary of animations keyed by character name and action.
        scale (float): Scale factor for the animation.
    """
    if player.name in ["Brute", "Berserker"]:
        scale -= 0.5

    current_animation = animations[player.name.lower()][player.action.value]

    if player.death_animation_done:
        current_frame = current_animation.get_last_death_frame(scale=scale)
    else:
        current_frame = current_animation.get_current_frame(scale=scale)

    # Calculate position for drawing
    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = player.x_pos - frame_width // 2
    y_pos = player.y_pos - frame_height

    screen.blit(current_frame, (x_pos, y_pos))
