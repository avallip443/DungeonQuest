from constants import (
    FONT,
    FONT_SM,
    FONT_LG,
    WIDTH,
    HEIGHT,
    PANEL_HEIGHT,
    SCREEN,
    CHARACTERS,
    CLOCK,
    FPS,
)
import pygame
from animations import load_character_animations
from health_bar import HealthBar


def draw_bg(screen, background_img):
    screen.blit(background_img, (0, 0))


def draw_panel(screen, panel_img, knight, bandit_list):
    screen.blit(panel_img, (0, HEIGHT - PANEL_HEIGHT))
    draw_text(screen, f"{knight.name} HP: {knight.hp}", 100, HEIGHT - PANEL_HEIGHT + 10)

    for count, bandit in enumerate(bandit_list):
        draw_text(
            screen,
            f"{bandit.name} HP: {bandit.hp}",
            520,
            (HEIGHT - PANEL_HEIGHT + 10) + count * 60,
        )


def draw_text(screen, text, x, y, colour, size="med", position="center"):
    if size == "sm":
        font = FONT_SM
    elif size == "med":
        font = FONT
    elif size == "lg":
        font = FONT_LG

    lines = text.split("\n")
    y_offset = 0
    for i, line in enumerate(lines):
        img = font.render(line, False, colour)
        img_rect = img.get_rect()

        if position == "center":
            img_rect.center = (x, y + y_offset)
        elif position == "topleft":
            img_rect.topleft = (x, y + y_offset)

        screen.blit(img, img_rect)
        y_offset += 20


def character_selection_screen():
    selected_index = -1  # initially no char selected
    hovered_index = -1

    animations = load_character_animations()

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                selected_index = hovered_index

        hovered_index = -1
        y_offset = 150

        # update hovered index based on mouse pos
        for index, character in enumerate(CHARACTERS):
            text_rect = FONT.render(character["name"], True, (100, 100, 100)).get_rect(
                center=(130, y_offset)
            )
            if text_rect.collidepoint(mouse_pos):
                hovered_index = index
            y_offset += 50

        draw_character_options(
            SCREEN, CHARACTERS, selected_index, hovered_index, animations
        )
        CLOCK.tick(FPS)


def draw_character_options(
    screen, characters, selected_index, hovered_index, animations
):
    screen.fill((0, 0, 0))
    y_offset = 150

    draw_text(screen, "Select Your Character", WIDTH // 2, y_offset // 2, "white", size="lg")

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


def animate_character(screen, animations, name, scale):
    current_animation = animations[name]["idle"]
    current_frame = current_animation.get_current_frame(scale=scale)

    scale_adjustment = 8 if name == "brute" else 0

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = WIDTH // 2 - frame_width // 1.75
    y_pos = HEIGHT // 2 - frame_height + 120 + scale_adjustment

    screen.blit(current_frame, (x_pos, y_pos))


def draw_character_stats(screen, index):
    hp = HealthBar(WIDTH * 0.69, 235, CHARACTERS[index]["max_hp"], 130)
    atk = HealthBar(WIDTH * 0.69, 265, CHARACTERS[index]["attack"], 30)
    
    draw_text(
        screen, CHARACTERS[index]["description"], WIDTH * 0.75, 160, "white", "sm"
    )
    draw_text(
        screen,
        "HP:",
        WIDTH * 0.62,
        230,
        "white",
        "sm",
        "topleft",
    )
    hp.draw(screen, CHARACTERS[index]["max_hp"], base='blue', secondary='white', width=140, height=10)
    
    draw_text(
        screen,
        "ATK:",
        WIDTH * 0.62,
        260,
        "white",
        "sm",
        "topleft",
    )
    atk.draw(screen, CHARACTERS[index]["attack"], base='blue', secondary='white', width=140, height=10)
    
    draw_text(
        screen,
        "Critial hit:  " + str(CHARACTERS[index]["critical_chance"]) + "%",
        WIDTH * 0.62,
        290,
        "white",
        "sm",
        "topleft",
    )
    draw_text(
        screen,
        "Double hit:  " + str(CHARACTERS[index]["double_hit_chance"]) + "%",
        WIDTH * 0.62,
        320,
        "white",
        "sm",
        "topleft",
    )


character_selection_screen()
