import pygame
from random import randint
from constants import SCREEN, WIDTH, CLOCK, FPS
from utils import draw_text


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
            f"GAME: {selected_char}, ROUND: {round}",
            WIDTH // 2,
            100,
            "white",
            "lg",
            "center",
        )

        round += 1
        totalLevelEnemies = round + randint(6, 11)
        
        if totalLevelEnemies > 0:
            if totalLevelEnemies == 1:
                play_boss_round()
                totalLevelEnemies -= 1
            else:
                currentRoundEnemies = min(randint(1, 4), totalLevelEnemies - 1)
                play_round(numEnemies=currentRoundEnemies)
                totalLevelEnemies -= currentRoundEnemies
        else:
            draw_text(
                SCREEN,
                f"GAME: {selected_char}, ROUND: DONE",
                WIDTH // 2,
                100,
                "white",
                "lg",
                "center",
            )
            
            
        pygame.display.update()
        CLOCK.tick(FPS)


def play_round(numEnemies: int):
    pass


def play_boss_round():
    pass


if __name__ == "__main__":
    play_game(selected_char=0)