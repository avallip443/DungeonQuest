import pygame
from constants import SWORD


def handle_actions(
    screen, clicked, current_fighter, player, enemies, potion_button, action_cooldown
):
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()

    if current_fighter == 1 and action_cooldown == 0:
        
        for i, enemy in enumerate(enemies):
            if enemy.hitbox.collidepoint(pos):
                pygame.mouse.set_visible(False)
                screen.blit(SWORD, pos)
                
                if enemy.alive and clicked:
                    perform_attack(player, enemies[i])
                    current_fighter = 0
                    action_cooldown = 30
                    continue

            if potion_button.rect.collidepoint(pos) and clicked:
                if player.potions > 0:
                    player.hp += 30
                    if player.hp > player.max_hp:
                        player.hp = player.max_hp
                    player.potions -= 1
                    current_fighter = 0
                    action_cooldown = 30

    elif current_fighter == 0 and action_cooldown == 0:
        for enemy in enemies:
            if enemy.alive:
                perform_attack(enemy, player)
        current_fighter = 1
        action_cooldown = 30

    if action_cooldown > 0:
        action_cooldown -= 1

    player.action = "idle"
    for enemy in enemies:
        enemy.action = "idle"


def perform_attack(attacker, target):
    damage = attacker.strength
    if damage > 0:
        target.hp -= damage
    if target.hp < 0:
        target.hp = 0
        target.alive = False
