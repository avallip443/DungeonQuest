import pygame
from constants import SWORD
from damage_text import DamageText


# constants
PLAYER_COOLDOWN = 10
ENEMY_COOLDOWN_SINGLE = 10
ENEMY_COOLDOWN_DOUBLE = 20

damage_text_group = pygame.sprite.Group()


def handle_actions(
    screen: pygame.Surface,
    clicked: bool,
    current_fighter: int,
    player,
    enemies,
    potion_button,
    action_cooldown: int,
) -> tuple[int, int]:
    """
    Handles the game actions based on the current state and user inputs.

    Args:
        screen (pygame.Surface): Game screen surface.
        clicked (bool): Whether the mouse was clicked.
        current_fighter (int): Indicates which character is the current fighter.
        player (Player): Player object.
        enemies (List[Enemy]): List of enemy objects.
        potion_button (PotionButton): Potion button object.
        action_cooldown (int): Cooldown timer for actions.

    Returns:
        tuple[int, int]: Updated current_fighter index and action_cooldown.
    """

    pygame.mouse.set_visible(True)

    if action_cooldown == 0:
        current_fighter, action_cooldown = execute_turn(
            screen, clicked, current_fighter, player, enemies, potion_button
        )

    action_cooldown = max(0, action_cooldown - 1)
    return current_fighter, action_cooldown


def execute_turn(
    screen: pygame.Surface,
    clicked: bool,
    current_figher: int,
    player,
    enemies,
    potion_button,
) -> tuple[int, int]:
    """
    Executes the current turn based on the current fighter.

    Args:
        screen (pygame.Surface): Game screen surface.
        clicked (bool): Whether the mouse was clicked.
        current_fighter (int): Indicates which character is the current fighter.
        player (Player): Player object.
        enemies (List[Enemy]): List of enemy objects.
        potion_button (PotionButton): Potion button object.

    Returns:
        Tuple[int, int]: Updated current_fighter index and action_cooldown.
    """

    if current_figher == 0:  # player turn
        if player_turn(screen, clicked, player, enemies, potion_button):
            return 1, PLAYER_COOLDOWN
    elif current_figher == 1:  # 1st enemy turn
        enemy_turn(enemies[0], player)
        if len(enemies) == 2:
            return 2, ENEMY_COOLDOWN_DOUBLE
        else:
            return 0, ENEMY_COOLDOWN_SINGLE
    elif current_figher == 2:  # 2nd enemy turn
        enemy_turn(enemies[1], player)
        return 0, ENEMY_COOLDOWN_SINGLE

    return current_figher, 0


def player_turn(
    screen: pygame.Surface, clicked: bool, player, enemies, potion_button
) -> bool:
    """
    Handles the player's turn actions.

    Args:
        screen (pygame.Surface): Game screen surface.
        clicked (bool): Whether the mouse was clicked.
        player (Player): Player object.
        enemies (List[Enemy]): List of enemy objects.
        potion_button: Potion button object.

    Returns:
        bool: True if the player's turn is done, False otherwise.
    """

    pos = pygame.mouse.get_pos()
    turn_done = False

    for enemy in enemies:
        if enemy.hitbox.collidepoint(pos):
            pygame.mouse.set_visible(False)
            screen.blit(SWORD, pos)

            if enemy.alive and clicked:
                perform_attack(player, enemy)
                turn_done = True

    if (
        potion_button.rect.collidepoint(pos)
        and clicked
        and player.potions > 0
        and player.max_hp > player.hp
    ):
        heal = player.heal()
        display_damage(player, heal, (0, 255, 0))
        turn_done = True

    return turn_done


def enemy_turn(enemy, player) -> None:
    """
    Handles an enemy's turn actions.

    Args:
        enemy (Enemy): Enemy taking the turn.
        player (Player): Player being attacked.
    """

    if enemy.alive:
        perform_attack(enemy, player)


def perform_attack(attacker, target) -> None:
    """
    Performs an attack from the attacker to the target.

    Args:
        attacker (Enemy/Player): Attacking fighter.
        target (Enemy/Player): Target fighter being attacked.
    """

    damage = attacker.attack()
    target.take_damage(damage)
    target.update_animation()
    # display_damage(target, damage, (255, 0, 0))


def display_damage(target, damage: int, colour) -> None:
    """
    Displays damage text on the screen for a given target.

    Args:
        target (Fighter): Target receiving damage.
        damage (int): Amount of damage dealt.
        color (Tuple[int, int, int]): RGB color for the damage text.
    """

    x, y = target.x_pos, target.y_pos - 210
    damage_text = DamageText(x, y, str(damage), colour)
    damage_text_group.add(damage_text)
