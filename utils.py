from constants import FONT, WIDTH, HEIGHT, PANEL_HEIGHT, RED, SCREEN, CHARACTERS
import pygame
from animations import load_character_animations


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


def draw_text(screen, text, x, y, colour=RED):
    img = FONT.render(text, False, colour)
    img_rect = img.get_rect(center=(x, y))
    screen.blit(img, img_rect)


def draw_character_options(
    screen, characters, selected_index, hovered_index, animations, scale=1.5
):
    screen.fill((0, 0, 0))
    y_offset = 150

    draw_text(screen, "Select Your Character", WIDTH // 2, y_offset // 2, "white")

    for index, character in enumerate(characters):
        if index == selected_index:
            color = (255, 255, 0)  # highlight selected char with diff color
        elif index == hovered_index:
            color = (255, 255, 255)  # highlight hovered char
        else:
            color = (100, 100, 100)

        draw_text(screen, character["name"], 200, y_offset, color)
        y_offset += 50

    if hovered_index != -1:
        selected_character = CHARACTERS[hovered_index]["name"]
        current_animation = animations[selected_character]["idle"]

        scale = 4 if selected_character == 'Brute' else 4.5
        
        current_frame = current_animation.get_current_frame(scale=scale)

        

        frame_width = current_frame.get_width()
        frame_height = current_frame.get_height()

        x_pos = WIDTH // 2 + 100 - frame_width // 2
        y_pos = HEIGHT // 2 - frame_height + 150

        # Blit the frame onto the {screen using the calculated position
        screen.blit(current_frame, (x_pos, y_pos))

    pygame.display.flip()


def character_selection_screen():
    selected_index = -1  # initially no char selected
    hovered_index = -1
    run = True
    clock = pygame.time.Clock()

    # Load the animations
    animations = load_character_animations()

    while run:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    selected_index = hovered_index

        hovered_index = -1
        y_offset = 150
        font_height = FONT.get_height()

        # update hovered index based on mouse pos
        for index, character in enumerate(CHARACTERS):
            text_rect = FONT.render(character["name"], True, (100, 100, 100)).get_rect(
                center=(200, y_offset + font_height // 2)
            )
            if text_rect.collidepoint(mouse_pos):
                hovered_index = index
            y_offset += 50

        draw_character_options(
            SCREEN, CHARACTERS, selected_index, hovered_index, animations, scale=1
        )
        clock.tick(60)  # Limit to 60 FPS


character_selection_screen()
