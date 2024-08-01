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


def play_game(selected_char: int):
    pygame.init()
    player = create_character(selected_char)
    round = 0
    animations = load_character_animations()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        SCREEN.fill("black")
        draw_text(
            SCREEN,
            text=f"GAME: {selected_char}, ROUND: {round}",
            x=WIDTH // 2,
            y=100,
            colour="white",
            size="lg",
            position="center",
        )

        round += 1
        total_level_enemies = round + randint(4, 6)

        while total_level_enemies > 0:
            if total_level_enemies == 1:
                play_boss_round(player, animations)
                total_level_enemies -= 1
            else:
                current_round_enemies = min(randint(1, 2), total_level_enemies - 1)
                enemies = [
                    create_enemy(randint(0, 1)) for i in range(current_round_enemies)
                ]
                play_round(enemies=enemies, player=player, animations=animations)
                total_level_enemies -= current_round_enemies

        pygame.display.update()
        CLOCK.tick(FPS)


def play_round(enemies, player, animations):
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

    if game_over == 1:
        print("Player wins!")
    elif game_over == -1:
        print("Player loses!")


def play_boss_round(player, animations):
    pass


if __name__ == "__main__":
    play_game(selected_char=3)
