import pygame
from constants import SWORD, FONT, SCREEN
from damage_text import DamageText

damage_text_group = pygame.sprite.Group()


def handle_actions(
    screen, clicked, current_fighter, player, enemies, potion_button, action_cooldown
):
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()

    if action_cooldown == 0:
        if current_fighter == 0:
            if player_turn(screen, clicked, pos, player, enemies, potion_button):
                current_fighter, action_cooldown = 1, 20
        elif current_fighter == 1:
            enemy_turn(enemies[0], player)
            current_fighter = 2 if len(enemies) == 2 else 0
            action_cooldown = 20
        else:
            enemy_turn(enemies[1], player)
            current_fighter, action_cooldown = 0, 20

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
        heal = player.heal()
        display_damage(player, heal, (0, 255, 0))
        turn_done = True

    return turn_done


def enemy_turn(enemy, player):
    if enemy.alive:
        perform_attack(enemy, player)


def perform_attack(attacker, target):
    damage = attacker.attack()
    target.take_damage(damage)
    display_damage(target, damage, (255, 0, 0))


def display_damage(target, damage, colour):
    x, y = target.x_pos, target.y_pos - 210
    damage_text = DamageText(x, y, str(damage), colour) 
    damage_text_group.add(damage_text)


def reset_actions(player, enemies):
    player.action = "idle"
    for enemy in enemies:
        enemy.action = "idle"
        enemy.action_cooldown = max(0, enemy.action_cooldown - 1)
