import pygame
from constants import SWORD
from action_text import ActionText


# constants
PLAYER_COOLDOWN = 20
ENEMY_COOLDOWN = 25

# sprite groups
damage_text_group = pygame.sprite.Group()
heal_text_group = pygame.sprite.Group()
potion_text_group = pygame.sprite.Group()


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
    action_cooldown = max(0, action_cooldown - 1)

    if action_cooldown == 0:
        current_fighter, action_cooldown = execute_turn(
            screen, clicked, current_fighter, player, enemies, potion_button
        )

    return current_fighter, action_cooldown


def execute_turn(
    screen: pygame.Surface,
    clicked: bool,
    current_fighter: int,
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
        tuple[int, int]: Updated current_fighter index and action_cooldown.
    """
    if current_fighter == 0:  # player's turn
        if player_turn(screen, clicked, player, enemies, potion_button):
            return 1, PLAYER_COOLDOWN
    elif current_fighter == 1:  # first enemy's turn
        enemy_turn(enemies[0], player)
        return (2, ENEMY_COOLDOWN) if len(enemies) == 2 else (0, ENEMY_COOLDOWN - 10)
    elif current_fighter == 2:  # second enemy's turn
        enemy_turn(enemies[1], player)
        return 0, ENEMY_COOLDOWN - 10

    return current_fighter, 0


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
        potion_button (PotionButton): Potion button object.

    Returns:
        bool: True if the player's turn is done, False otherwise.
    """
    pos = pygame.mouse.get_pos()
    turn_done = False

    for enemy in enemies:
        if enemy.hitbox.collidepoint(pos) and enemy.alive:
            pygame.mouse.set_visible(False)
            screen.blit(SWORD, pos)

            if clicked and enemy.alive:
                perform_attack(player, enemy)
                turn_done = True

    if potion_button.rect.collidepoint(pos) and clicked:
        turn_done = use_potion_if_possible(player)

    return turn_done


def use_potion_if_possible(player) -> bool:
    """
    Uses a potion if the player has one available and can be healed.

    Args:
        player (Player): Player object.

    Returns:
        bool: True if the potion was used, False otherwise.
    """
    if player.potions > 0 and player.hp < player.max_hp:
        heal = player.heal()
        display_action_text(
            target=player, text_group=heal_text_group, text=heal, colour=(0, 255, 0)
        )
        return True
    return False


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
        attacker (Fighter): Attacking fighter.
        target (Fighter): Target fighter being attacked.
    """
    from player import Player  # avoid circular import

    damage = attacker.attack()
    target.take_damage(damage)
    target.update_animation()

    if target.hp - damage <= 0 and isinstance(attacker, Player):  # accounts for delayed damage
        potion_received = attacker.get_potion()
        if potion_received:
            display_action_text(
                target=attacker,
                text_group=potion_text_group,
                text="+1 Potion",
                colour=(0, 255, 0),
            )


def display_action_text(
    target, text: int, colour, text_group=damage_text_group
) -> None:
    """
    Displays action text on the screen for a given target.

    Args:
        target (Fighter): Target receiving action text.
        text (str): Action text to be displayed.
        colour (tuple[int, int, int]): RGB color for the text.
        text_group (pygame.sprite.Group): Sprite group to which the text belongs.
    """
    x, y = target.x_pos, target.y_pos - 210
    delay = 10 if "Potion" in str(text) else 0
    action_text = ActionText(x, y, str(text), colour, delay=delay)
    text_group.add(action_text)
