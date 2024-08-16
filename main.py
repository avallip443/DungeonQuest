import pygame
from constants import SCREEN, HEIGHT, WIDTH, PLAY, TUTORIAL, QUIT, BACK
from button import Button
from utils import draw_text
from character_selection import character_selection_screen
from game import main


def start_menu() -> None:
    """
    Displays the start menu where players can choose to play the game, view the tutorial, or quit.
    """
    # button 
    button_scale = 2
    button_width = 92 * button_scale
    button_height = 28 * button_scale

    play_button = Button(
        SCREEN,
        x=WIDTH // 2,
        y=HEIGHT // 2 - 50,
        image=PLAY,
        width=button_width,
        height=button_height,
    )
    tutorial_button = Button(
        SCREEN,
        x=WIDTH // 2,
        y=HEIGHT // 2 + 30,
        image=TUTORIAL,
        width=button_width,
        height=button_height,
    )
    quit_button = Button(
        SCREEN,
        x=WIDTH // 2,
        y=HEIGHT // 2 + 110,
        image=QUIT,
        width=button_width,
        height=button_height,
    )

    while True:
        SCREEN.fill((0, 0, 0))
        draw_text(SCREEN, text="DUNGEON QUEST", x=WIDTH // 2, y=100, size="lg")

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
                        main(selected_char=selected_char, on_exit=start_menu)
                elif tutorial_button.rect.collidepoint(event.pos):
                    tutorial()

        pygame.display.update()


def tutorial() -> None:
    """
    Displays the tutorial screen with instructions on how to play the game.
    """
    # Scaling factor for the back button
    back_button_scale = 1.5
    back_button_width = 31 * back_button_scale
    back_button_height = 35 * back_button_scale

    back_button = Button(
        SCREEN,
        x=50,
        y=50,
        image=BACK,
        width=back_button_width,
        height=back_button_height,
    )

    while True:
        SCREEN.fill("black")
        draw_text(SCREEN, text="TUTORIAL", x=WIDTH // 2, y=100, size="lg")

        draw_text(SCREEN, text="STATS", x=WIDTH // 2, y=170, size="md")
        draw_text(
            SCREEN,
            text="1. Critical hit: Chance to deal 200% damage.",
            x=WIDTH // 2,
            y=200,
            size="sm",
        )
        draw_text(
            SCREEN,
            text="2. Double hit: Chance to strike twice in one attack.",
            x=WIDTH // 2,
            y=225,
            size="sm",
        )

        draw_text(SCREEN, text="POTIONS", x=WIDTH // 2, y=280, size="md")
        draw_text(
            SCREEN,
            text="Potions are used to heal HP. All defeated enemies have a chance to drop potions.",
            x=WIDTH // 2,
            y=310,
            size="sm",
        )

        draw_text(SCREEN, text="BATTLE", x=WIDTH // 2, y=365, size="md")
        draw_text(
            SCREEN,
            text="1. All players take turns attacking.",
            x=WIDTH // 2,
            y=395,
            size="sm",
        )
        draw_text(
            SCREEN,
            text="2. Click the enemy to attack or potion button to heal.",
            x=WIDTH // 2,
            y=425,
            size="sm",
        )
        draw_text(
            SCREEN,
            text="3. Once all enemies are defeated in the level, the boss appears. Prepare well!",
            x=WIDTH // 2,
            y=455,
            size="sm",
        )

        back_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    start_menu()

        pygame.display.update()


if __name__ == "__main__":
    start_menu()
