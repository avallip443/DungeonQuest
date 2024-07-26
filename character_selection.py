import pygame
from constants import (
    FONT,
    WIDTH,
    HEIGHT,
    SCREEN,
    CHARACTERS,
    CLOCK,
    FPS,
    PLAY,
    BACK
)
from animations import load_character_animations
from health_bar import HealthBar
from button import Button
from utils import draw_text


def character_selection_screen():
    from main import start_menu
    
    selected_index = -1  # initially no char selected
    hovered_index = -1

    animations = load_character_animations()
    play_button = Button(SCREEN, WIDTH // 2, HEIGHT * 0.85, PLAY, 92 * 2, 28 * 2)
    back_button = Button(SCREEN, 50, 50, BACK, 31 * 1.5, 35 * 1.5)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.rect.collidepoint(mouse_pos):
                    return selected_index 
                elif back_button.rect.collidepoint(event.pos):
                    start_menu()
                selected_index = hovered_index
                
        hovered_index = -1
        y_offset = 170

        # update hovered index based on mouse pos
        for index, character in enumerate(CHARACTERS):
            text_rect = FONT.render(character["name"], True, (100, 100, 100)).get_rect(
                center=(130, y_offset)
            )
            if text_rect.collidepoint(mouse_pos):
                hovered_index = index
            y_offset += 50

        draw_character_options(
            SCREEN, CHARACTERS, selected_index, hovered_index, animations, play_button, back_button
        )

        CLOCK.tick(FPS)


def draw_character_options(
    screen, characters, selected_index, hovered_index, animations, play_button, back_button
):
    screen.fill((0, 0, 0))
    y_offset = 170
    selected = False

    draw_text(screen, "Select Your Character", WIDTH // 2, 75, "white", size="lg")
    back_button.draw()

    for index, character in enumerate(characters):
        color = (
            (255, 255, 0)
            if index == selected_index
            else (255, 255, 255)
            if index == hovered_index
            else (100, 100, 100)
        )
        draw_text(screen, character["name"], 130, y_offset, color)
        y_offset += 50

    if selected_index != -1:
        selected_character = CHARACTERS[selected_index]["name"]

        if hovered_index == selected_index or hovered_index == -1:
            animate_character(
                screen,
                animations,
                selected_character,
                scale=3.7 if selected_character == "Brute" else 4.5,
            )
            draw_character_stats(screen, selected_index)
            play_button.draw()

    if hovered_index != -1 and hovered_index != selected_index:
        selected_character = CHARACTERS[hovered_index]["name"]
        animate_character(
            screen,
            animations,
            selected_character,
            scale=3.7 if selected_character == "Brute" else 4.5,
        )
        draw_character_stats(screen, hovered_index)

    pygame.display.flip()
    return selected


def animate_character(screen, animations, name, scale):
    current_animation = animations[name]["idle"]
    current_frame = current_animation.get_current_frame(scale=scale)

    scale_adjustment = 10 if name == "Brute" else 0

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = WIDTH // 2 - frame_width // 1.75
    y_pos = HEIGHT * 0.78 - frame_height - scale_adjustment

    screen.blit(current_frame, (x_pos, y_pos))


def draw_character_stats(screen, index):
    hp = HealthBar(WIDTH * 0.69, 255, CHARACTERS[index]["max_hp"], 130)
    atk = HealthBar(WIDTH * 0.69, 285, CHARACTERS[index]["attack"], 30)

    draw_text(
        screen, CHARACTERS[index]["description"], WIDTH * 0.75, 190, "white", "sm"
    )
    draw_text(
        screen,
        "HP:",
        WIDTH * 0.62,
        250,
        "white",
        "sm",
        "topleft",
    )
    hp.draw(
        screen,
        CHARACTERS[index]["max_hp"],
        base="blue",
        secondary="white",
        width=140,
        height=10,
    )

    draw_text(
        screen,
        "ATK:",
        WIDTH * 0.62,
        280,
        "white",
        "sm",
        "topleft",
    )
    atk.draw(
        screen,
        CHARACTERS[index]["attack"],
        base="blue",
        secondary="white",
        width=140,
        height=10,
    )

    draw_text(
        screen,
        "Critial hit:  " + str(CHARACTERS[index]["critical_chance"]) + "%",
        WIDTH * 0.62,
        310,
        "white",
        "sm",
        "topleft",
    )
    draw_text(
        screen,
        "Double hit:  " + str(CHARACTERS[index]["double_hit_chance"]) + "%",
        WIDTH * 0.62,
        340,
        "white",
        "sm",
        "topleft",
    )
