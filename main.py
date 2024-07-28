import pygame
from constants import SCREEN, HEIGHT, WIDTH, PLAY, TUTORIAL, QUIT, BACK
from button import Button
from utils import draw_text
from character_selection import character_selection_screen
from game import play_game


def start_menu():
    play_button = Button(SCREEN, WIDTH // 2, HEIGHT // 2 - 50, PLAY, 92 * 2, 28 * 2)
    tutorial_button = Button(SCREEN, WIDTH // 2, HEIGHT // 2 + 30, TUTORIAL, 92 * 2, 28 * 2)
    quit_button = Button(SCREEN, WIDTH // 2, HEIGHT // 2 + 110, QUIT, 92 * 2, 28 * 2)

    while True:
        SCREEN.fill("black")
        draw_text(SCREEN, "DUNGEON QUEST", WIDTH // 2, 100, "white", "lg", "center")

        play_button.draw()
        tutorial_button.draw()
        quit_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()
                elif play_button.rect.collidepoint(event.pos):
                    selected_char = character_selection_screen()
                    if selected_char != -1:
                        game(selected_char=selected_char)
                elif tutorial_button.rect.collidepoint(event.pos):
                    tutorial()

        pygame.display.update()


def tutorial():
    back_button = Button(SCREEN, 50, 50, BACK, 31 * 1.5, 35 * 1.5)
    
    while True:
        SCREEN.fill("black")
        draw_text(SCREEN, "TUTORIAL", WIDTH // 2, 100, "white", "lg", "center")
        
        back_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    start_menu()
                    
        pygame.display.update()


def game(selected_char: int):
    play_game(selected_char=selected_char)


if __name__ == "__main__":
    start_menu()
