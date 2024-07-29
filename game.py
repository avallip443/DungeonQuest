import pygame
from random import randint
from constants import SCREEN, WIDTH, CLOCK, FPS, FOREST1
from utils import draw_text, draw_bg
from player import create_character
from enemy import create_enemy


def play_game(selected_char: int):
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
        total_level_enemies = round + randint(6, 11)

        while total_level_enemies > 0:
            if total_level_enemies == 1:
                play_boss_round()
                total_level_enemies -= 1
            else:
                current_round_enemies = min(randint(1, 4), total_level_enemies - 1)
                enemies = [create_enemy(randint(0, 4)) for _ in range(current_round_enemies)]    
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
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

                
        draw_bg(SCREEN, FOREST1)
        pygame.display.update()
        CLOCK.tick(FPS)


def play_boss_round():
    pass


if __name__ == "__main__":
    play_game(selected_char=0)
