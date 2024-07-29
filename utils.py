from constants import (
    SCREEN, 
    FONT,
    FONT_SM,
    FONT_LG,
    WIDTH,
    HEIGHT,
    PANEL_HEIGHT,
    RED,
)


def draw_bg(screen, background_img):
    screen.blit(background_img, (0, 0))


def draw_panel(screen, panel_img, player, player_healthbar, enemies=0):
    screen.blit(panel_img, (0, HEIGHT - PANEL_HEIGHT))
    
    draw_text(
        screen,
        f"{player.name} HP: {player.hp}",
        WIDTH // 4,
        HEIGHT - PANEL_HEIGHT + 30,
        colour=RED,
    )
    
    player_healthbar.draw(SCREEN, player.hp)

    """
    for count, enemy in enumerate(enemies):
        draw_text(
            screen,
            f"{enemy.name} HP: {enemy.hp}",
            520,
            (HEIGHT - PANEL_HEIGHT + 10) + count * 60,
            colour=RED,
        )
    """


def draw_text(screen, text, x, y, colour='white', size="med", position="center"):
    if size == "sm":
        font = FONT_SM
    elif size == "med":
        font = FONT
    elif size == "lg":
        font = FONT_LG

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
