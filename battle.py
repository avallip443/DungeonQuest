import pygame
from constants import SWORD


def handle_actions(
    screen, clicked, current_fighter, player, enemies, potion_button, action_cooldown
):
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    print(f"current fighter battle: {current_fighter}")

    if action_cooldown == 0:
        if current_fighter == 1:
            if player_turn(screen, clicked, pos, player, enemies, potion_button):
                current_fighter, action_cooldown = 0, 10
        elif current_fighter == 0:
            enemy_turn(enemies, player)
            current_fighter, action_cooldown = 1, 10

    action_cooldown = max(0, action_cooldown - 1)
    reset_actions(player, enemies)
    return current_fighter, action_cooldown


def player_turn(screen, clicked, pos, player, enemies, potion_button):
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
        player.heal()
        turn_done = True

    return turn_done


def enemy_turn(enemies, player):
    for enemy in enemies:
        if enemy.alive:
            perform_attack(enemy, player)


def perform_attack(attacker, target):
    damage = attacker.attack()
    target.take_damage(damage)


def reset_actions(player, enemies):
    player.action = "idle"
    for enemy in enemies:
        enemy.action = "idle"
