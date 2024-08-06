import pygame
from random import randint
from constants import (
    SCREEN,
    WIDTH,
    CLOCK,
    FPS,
    FOREST1,
    PANEL,
    HEIGHT,
    PANEL_HEIGHT,
    POTION,
)
from utils import draw_text, draw_bg, draw_panel, draw_characters
from player import create_character
from enemy import create_enemy
from animations import load_character_animations
from battle import handle_actions, damage_text_group
from button import Button


def play_game(selected_char: int) -> None:
    """
    Main game loop that manages game rounds and character selection.

    Args:
        selected_char (int): Index of the selected character.
    """

    pygame.init()
    player = create_character(selected_char)
    round = 0
    animations = load_character_animations()

    player_target_position = 100
    enemy_start_position = WIDTH + 10
    enemy_target_position = 700
    player.walk(target_x=player_target_position)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        SCREEN.fill((0, 0, 0))
        draw_text(
            SCREEN,
            text=f"ROUND: {round+1}",
            x=WIDTH // 2,
            y=100,
            colour="white",
            size="lg",
            position="center",
        )

        player.update_walk_pos(target_x=player_target_position)
        player.update_animation()

        draw_characters(SCREEN, player, [], animations)
        pygame.display.update()
        CLOCK.tick(FPS)

        if player.x_pos >= player_target_position:
            break

    round += 1
    total_level_enemies = round + randint(4, 6)

    while total_level_enemies > 0:
        if total_level_enemies == 1:
            play_boss_round(player, animations)
            total_level_enemies -= 1
        else:
            current_round_enemies = min(randint(1, 2), total_level_enemies - 1)
            enemies = [
                create_enemy(randint(0, 1)) for _ in range(current_round_enemies)
            ]

            for i, enemy in enumerate(enemies):
                enemy.x_pos = enemy_start_position + (1 - i) * 130
                enemy.walk(target_x=enemy_target_position - (1-i) * 130)

            # enemy walking sequence
            enemies_moving = True
            while enemies_moving:
                enemies_moving = False
                for i, enemy in enumerate(enemies):
                    enemy.update_walk_pos(
                        target_x=enemy_target_position - i * 130
                    )
                    enemy.update_animation()
                    if enemy.x_pos > enemy_target_position - i * 130:
                        enemies_moving = True

                SCREEN.fill((0, 0, 0))
                draw_text(
                    SCREEN,
                    text=f"ROUND: {round}",
                    x=WIDTH // 2,
                    y=100,
                    colour="white",
                    size="lg",
                    position="center",
                )
                draw_characters(SCREEN, player, enemies, animations)
                pygame.display.update()
                CLOCK.tick(FPS)

            play_round(enemies=enemies, player=player, animations=animations)
            total_level_enemies -= current_round_enemies


def play_round(enemies, player, animations) -> None:
    """
    Manages the game logic for a single round of combat.

    Args:
        enemies (list): List of enemy instances for the round.
        player (Character): Player character instance.
        animations (dict): Dictionary containing animations for characters.
    """

    run = True
    current_fighter = 0  # 1: player, 0: computer
    action_cooldown = 0
    game_over = 0  # 1: player win, -1: player loss
    clicked = False

    while run:
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

        draw_bg(SCREEN, FOREST1)

        potion_button = Button(
            SCREEN,
            x=120,
            y=HEIGHT - PANEL_HEIGHT * 0.25,
            image=POTION,
            width=55,
            height=55,
        )
        draw_panel(SCREEN, PANEL, player, enemies, potion_button)
        draw_characters(SCREEN, player, enemies, animations)

        current_fighter, action_cooldown = handle_actions(
            SCREEN,
            clicked,
            current_fighter,
            player,
            enemies,
            potion_button,
            action_cooldown,
        )

        damage_text_group.update()
        damage_text_group.draw(SCREEN)
        player.update_animation()

        for enemy in enemies:
            enemy.update_animation()

        if player.hp <= 0:
            game_over = -1
            run = False
        if all(enemy.hp <= 0 for enemy in enemies):
            game_over = 1
            run = False

        pygame.display.update()
        CLOCK.tick(FPS)

    display_game_over_message(game_over)


def play_boss_round(player, animations):
    pass


def display_game_over_message(game_over: int) -> None:
    """
    Displays a message indicating the outcome of the game.

    Args:
        gam
        e_over (int): The result of the game round (-1 for loss, 1 for win).
    """
    if game_over == 1:
        print("Player wins!")
    elif game_over == -1:
        print("Player loses!")


if __name__ == "__main__":
    play_game(selected_char=3)
