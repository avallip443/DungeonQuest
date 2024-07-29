import pygame
from random import randint
from constants import SCREEN, WIDTH, HEIGHT, CLOCK, FPS, FOREST1, PANEL
from utils import draw_text, draw_bg, draw_panel
from player import create_character
from enemy import create_enemy
from animations import load_character_animations, animate_character


def play_game(selected_char: int):
    pygame.init()
    player = create_character(selected_char)
    round = 0

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
                play_boss_round()
                total_level_enemies -= 1
            else:
                current_round_enemies = min(randint(1, 2), total_level_enemies - 1)
                enemies = [
                    create_enemy(randint(0, 1)) for _ in range(current_round_enemies)
                ]
                play_round(enemies=enemies, player=player)
                total_level_enemies -= current_round_enemies

        pygame.display.update()
        CLOCK.tick(FPS)


def play_round(enemies, player):
    run = True
    current_fighter = 1
    action_cooldown = 0
    clicked = False
    game_over = 0  # 1 = player win, -1 = player loss
    animations = load_character_animations()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

        draw_bg(SCREEN, FOREST1)
        draw_panel(SCREEN, PANEL, player, enemies)

        animate_character(
            SCREEN, animations, name=player.name, action="idle", scale=3.5, x_pos=200, y_pos=HEIGHT * 0.68
        )

        for i, enemy in enumerate(enemies):
            animate_character(
                SCREEN,
                animations,
                name=enemy.name,
                action="idle",
                scale=2.5,
                x_pos=650 - i * 150,
                y_pos=HEIGHT * 0.65,
            )

        pygame.display.update()
        CLOCK.tick(FPS)


def play_boss_round():
    pass


if __name__ == "__main__":
    play_game(selected_char=4)
