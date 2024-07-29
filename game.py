import pygame
from random import randint
from constants import SCREEN, WIDTH, CLOCK, FPS, FOREST1
from utils import draw_text, draw_bg
from player import create_character
from enemy import create_enemy


def play_game(selected_char: int):
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

        player = create_character(selected_char)
        round += 1
        totalLevelEnemies = round + randint(6, 11)
        enemies = []

        if totalLevelEnemies > 0:
            if totalLevelEnemies == 1:
                play_boss_round()
                totalLevelEnemies -= 1
            else:
                currentRoundEnemies = min(randint(1, 4), totalLevelEnemies - 1)

                for i in range(currentRoundEnemies):
                    enemy_index = randint(0, 5)
                    enemy = create_enemy(enemy_index)
                    enemies.append(enemy)
                    
                play_round(enemies=enemies, player=player)
                totalLevelEnemies -= currentRoundEnemies
        else:
            draw_text(
                SCREEN,
                text=f"GAME: {selected_char}, ROUND: DONE",
                x=WIDTH // 2,
                y=100,
                colour="white",
                size="lg",
                position="center",
            )

        pygame.display.update()
        CLOCK.tick(FPS)


def play_round(enemies, player):
    run = True
    current_fighter = 1
    action_cooldown = 0
    clicked = False
    game_over = 0  # 1 = player win, -1 = player loss
    
    while run:
        CLOCK.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False
                
        draw_bg(SCREEN, FOREST1)
        
                
def play_boss_round():
    pass


if __name__ == "__main__":
    play_game(selected_char=0)
