import pygame
from constants import FONT, WIDTH, HEIGHT, SCREEN, CHARACTERS, CLOCK, FPS, PLAY, BACK
from animations import load_character_animations
from health_bar import HealthBar
from button import Button
from utils import draw_text


def character_selection_screen() -> int:
    """
    Displays the character selection screen where the player can choose a character.

    Returns:
        int: Index of the selected character.
    """

    from main import start_menu

    selected_index = 0
    hovered_index = -1

    animations = load_character_animations()
    play_button = Button(
        SCREEN, x=WIDTH // 2, y=HEIGHT * 0.85, image=PLAY, width=92 * 2, height=28 * 2
    )
    back_button = Button(
        SCREEN, x=50, y=50, image=BACK, width=31 * 1.5, height=35 * 1.5
    )

    while True:
        selected_index, play_clicked = handle_events(
            play_button, back_button, hovered_index, selected_index, start_menu
        )
        
        if play_clicked:
            return selected_index
        
        mouse_pos = pygame.mouse.get_pos()
        hovered_index = get_hovered_index(mouse_pos)

        draw_character_options(
            SCREEN,
            CHARACTERS,
            selected_index,
            hovered_index,
            animations,
            play_button,
            back_button,
        )

        CLOCK.tick(FPS)


def handle_events(
    play_button, back_button, hovered_index: int, selected_index: int, start_menu
) -> int:
    """
    Handles events such as quitting, clicking buttons, and selecting characters.

    Args:
        play_button (Button): Play button instance.
        back_button (Button): Back button instance.
        hovered_index (int): Index of the currently hovered character.
        selected_index (int): Index of the currently selected character.
        start_menu (function): Function to call to return to the start menu.

    Returns:
        int: Index of the selected character.
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_pos):
                return selected_index, True
            if back_button.rect.collidepoint(event.pos):
                start_menu()
            selected_index = hovered_index
    return selected_index, False


def get_hovered_index(mouse_pos) -> int:
    """
    Determines which character is currently hovered over by the mouse.

    Args:
        mouse_pos (tuple): Current position of the mouse.

    Returns:
        int: Index of the hovered character, or -1 if none are hovered.
    """

    hovered_index = -1
    y_offset = 170

    # update hovered index from mouse position
    for index, character in enumerate(CHARACTERS):
        text_rect = FONT.render(character["name"], True, (100, 100, 100)).get_rect(
            center=(130, y_offset)
        )
        if text_rect.collidepoint(mouse_pos):
            hovered_index = index
        y_offset += 50
    return hovered_index


def draw_character_options(
    screen,
    characters,
    selected_index: int,
    hovered_index: int,
    animations,
    play_button,
    back_button,
) -> None:
    """
    Draws the character options on the screen, highlighting the selected and hovered characters.

    Args:
        screen (pygame.Surface): Surface to draw on.
        characters (list): List of character data.
        selected_index (int): Index of the currently selected character.
        hovered_index (int): Index of the currently hovered character.
        animations (dict): Loaded animations for characters.
        play_button (Button): Play button instance.
        back_button (Button): Back button instance.
    """

    screen.fill((0, 0, 0))
    y_offset = 170

    draw_text(
        screen,
        text="Select Your Character",
        x=WIDTH // 2,
        y=75,
        colour="white",
        size="lg",
    )
    back_button.draw()

    for index, character in enumerate(characters):
        colour = (
            (255, 255, 0)  # yellow
            if index == selected_index
            else (255, 255, 255)  # white
            if index == hovered_index
            else (100, 100, 100)  # black
        )
        draw_text(screen, text=character["name"], x=130, y=y_offset, colour=colour)
        y_offset += 50

    if selected_index != -1:
        draw_selected_character(
            screen, animations, selected_index, hovered_index, play_button
        )

    if hovered_index != -1 and hovered_index != selected_index:
        draw_hovered_character(screen, animations, hovered_index)

    pygame.display.flip()


def draw_selected_character(
    screen, animations, selected_index, hovered_index, play_button
) -> None:
    """
    Draws the selected character's animation and stats on the screen.

    Args:
        screen (pygame.Surface): Surface to draw on.
        animations (dict): Loaded animations for characters.
        selected_index (int): Index of the currently selected character.
        hovered_index (int): Index of the currently hovered character.
        play_button (Button): Play button instance.
    """

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


def draw_hovered_character(screen, animations, hovered_index) -> None:
    """
    Draws the hovered character's animation and stats on the screen.

    Args:
        screen (pygame.Surface): Surface to draw on.
        animations (dict): Loaded animations for characters.
        hovered_index (int): Index of the currently hovered character.
    """

    hovered_character = CHARACTERS[hovered_index]["name"]
    animate_character(
        screen,
        animations,
        hovered_character,
        scale=3.7 if hovered_character == "Brute" else 4.5,
    )
    draw_character_stats(screen, hovered_index)


def animate_character(screen, animations, name: str, scale: float) -> None:
    """
    Animates the character on the screen based on the provided animation data.

    Args:
        screen (pygame.Surface): Surface to draw on.
        animations (dict): Loaded animations for characters.
        name (str): Name of the character to animate.
        scale (float): Scaling factor for the animation.
    """

    current_animation = animations[name.lower()]["idle"]
    current_frame = current_animation.get_current_frame(scale=scale)

    scale_adjustment = 10 if name == "Brute" else 0

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = WIDTH // 2 - frame_width // 1.75
    y_pos = HEIGHT * 0.78 - frame_height - scale_adjustment

    screen.blit(current_frame, (x_pos, y_pos))


def draw_character_stats(screen, index) -> None:
    """
    Draws the character stats on the screen.

    Args:
        screen (pygame.Surface): Surface to draw on.
        index (int): Index of the character to draw stats for.
    """

    hp = HealthBar(140, 10, CHARACTERS[index]["max_hp"], 130)
    atk = HealthBar(140, 10, CHARACTERS[index]["attack"], 30)

    draw_text(
        screen,
        text=CHARACTERS[index]["description"],
        x=WIDTH * 0.75,
        y=190,
        colour="white",
        size="sm",
    )
    draw_text(
        screen,
        text="HP:",
        x=WIDTH * 0.62,
        y=250,
        colour="white",
        size="sm",
        position="topleft",
    )
    hp.draw(
        screen,
        CHARACTERS[index]["max_hp"],
        base="blue",
        secondary="white",
        x=WIDTH * 0.69,
        y=255,
    )

    draw_text(
        screen,
        text="ATK:",
        x=WIDTH * 0.62,
        y=280,
        colour="white",
        size="sm",
        position="topleft",
    )
    atk.draw(
        screen,
        CHARACTERS[index]["attack"],
        base="blue",
        secondary="white",
        x=WIDTH * 0.69,
        y=285,
    )

    draw_text(
        screen,
        text="Critial hit:  " + str(CHARACTERS[index]["critical_chance"]) + "%",
        x=WIDTH * 0.62,
        y=310,
        colour="white",
        size="sm",
        position="topleft",
    )
    draw_text(
        screen,
        text="Double hit:  " + str(CHARACTERS[index]["double_hit_chance"]) + "%",
        x=WIDTH * 0.62,
        y=340,
        colour="white",
        size="sm",
        position="topleft",
    )
