from constants import FONT, FONT_SM, FONT_LG, WIDTH, HEIGHT, PANEL_HEIGHT
from health_bar import HealthBar
from enemy import animate_enemy
from player import animate_player


# layout
PLAYER_X_POS = 0
PLAYER_Y_POS = HEIGHT * 0.67
ENEMY_Y_POS = HEIGHT * 0.66
BOSS_Y_POS = HEIGHT * 0.68
HEALTHBAR_WIDTH = 250
HEALTHBAR_HEIGHT = 25
SCALE_PLAYER = 3.5
SCALE_ENEMY = 2.5
SCALE_BOSS_SMALL = 4
SCALE_BOSS_LARGE = 3.2

BOSS_HITBOX = [(140, 220), (100, 190), (100, 210)]
BOSS_HITBOX_OFFSET = [(-65, 260), (70, 230), (80, 260)]  # Bringer, Wizard1, Oldking
BOSS_SCALE = [4, 3.2, 4.3]  # Bringer, Wizard, OldKing


def draw_bg(screen, background_img) -> None:
    """
    Draws the background image on the screen.

    Args:
        screen (pygame.Surface): Game screen surface.
        background_img (pygame.Surface): Background image to be drawn.
    """
    screen.blit(background_img, (0, 0))


def draw_panel(screen, panel_img, player, enemies, potion_button) -> None:
    """
    Draws the game panel, including player and enemy stats.

    Args:
        screen (pygame.Surface): Game screen surface.
        panel_img (pygame.Surface): Panel image to be drawn.
        player (Player): Player object containing stats.
        enemies (list): List of enemy objects.
        potion_button (Button): Potion button to be drawn.
    """
    screen.blit(panel_img, (0, HEIGHT - PANEL_HEIGHT))

    # draw player stats
    draw_text(
        screen,
        f"{player.name} HP: {player.hp}",
        x=WIDTH // 4,
        y=HEIGHT - PANEL_HEIGHT + 30,
        colour="white",
    )
    draw_health_bar(
        screen,
        player.hp,
        player.max_hp,
        WIDTH // 4 - HEALTHBAR_WIDTH // 2,
        HEIGHT - PANEL_HEIGHT + 50,
    )
    potion_button.draw()
    draw_text(
        screen, str(player.potions), x=140, y=HEIGHT - PANEL_HEIGHT * 0.35, size="sm"
    )

    # draw enemy stats
    panel_offsets = [(90, 110), (20, 40)] if len(enemies) == 2 else [(30, 50)]

    for i, (text_offset, bar_offset) in enumerate(panel_offsets):
        x = WIDTH * 0.75
        text_y = HEIGHT - PANEL_HEIGHT + text_offset
        bar_y = HEIGHT - PANEL_HEIGHT + bar_offset

        draw_text(
            screen,
            f"{enemies[i].name}",
            x=x,
            y=text_y,
            colour="white",
        )
        draw_health_bar(
            screen, enemies[i].hp, enemies[i].max_hp, x - HEALTHBAR_WIDTH // 2, bar_y
        )


def draw_text(
    screen, text, x, y, colour="white", size="med", position="center"
) -> None:
    """
    Renders and draws text on the screen.

    Args:
        screen (pygame.Surface): Game screen surface.
        text (str): Text to be drawn.
        x (int): X-coordinate for the text position.
        y (int): Y-coordinate for the text position.
        colour (str): Colourof the text. Defaults to "white".
        size (str): Font size ("sm", "med", "lg"). Defaults to "med".
        position (str): Position of the text ("center", "topleft"). Defaults to "center".
    """
    font = {"sm": FONT_SM, "med": FONT, "lg": FONT_LG}.get(size, FONT)
    lines = text.split("\n")
    y_offset = 0

    for line in lines:
        img = font.render(line, False, colour)
        img_rect = img.get_rect()

        if position == "center":
            img_rect.center = (x, y + y_offset)
        elif position == "topleft":
            img_rect.topleft = (x, y + y_offset)

        screen.blit(img, img_rect)
        y_offset += img_rect.height


def draw_health_bar(screen, hp: int, max_hp: int, x: int, y: int) -> None:
    """
    Draws a health bar on the screen.

    Args:
        screen (pygame.Surface): G screen surface.
        hp (int): Current health of the character.
        max_hp (int): Maximum health of the character.
        x (int): X-coordinate for the health bar position.
        y (int): Y-coordinate for the health bar position.
    """
    health_bar = HealthBar(
        width=HEALTHBAR_WIDTH, height=HEALTHBAR_HEIGHT, hp=hp, max_hp=max_hp
    )
    health_bar.draw(screen, hp=hp, x=x, y=y)


def draw_characters(screen, player, enemies, animations, current_level: int) -> None:
    """
    Draws the player and enemies on the screen.

    Args:
        screen (pygame.Surface): Game screen surface.
        player (Player): Player object to be drawn.
        enemies (list): List of enemy objects to be drawn.
        animations (dict): Dictionary of animations for the characters.
        current_level (int): Current level of the game, used for boss scaling and hitbox.
    """
    player.y_pos = PLAYER_Y_POS
    animate_player(screen, player, animations, scale=SCALE_PLAYER)

    for enemy in enemies:
        if enemy.type == "boss":
            width, height = BOSS_HITBOX[current_level - 1]
            x_pos_offset, y_pos_offset = BOSS_HITBOX_OFFSET[current_level - 1]
            enemy.y_pos = BOSS_Y_POS
            enemy.update_hitbox(
                x_pos=enemy.x_pos - x_pos_offset,
                y_pos=BOSS_Y_POS - y_pos_offset,
                width=width,
                height=height,
            )
            scale = BOSS_SCALE[current_level - 1]
        else:
            enemy.y_pos = ENEMY_Y_POS
            enemy.update_hitbox(enemy.x_pos - 50, ENEMY_Y_POS - 140)
            scale = SCALE_ENEMY

        animate_enemy(
            screen=screen,
            animations=animations,
            enemy=enemy,
            scale=scale,
        )
