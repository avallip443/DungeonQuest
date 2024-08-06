from constants import (
    FONT,
    FONT_SM,
    FONT_LG,
    WIDTH,
    HEIGHT,
    PANEL_HEIGHT,
)
from health_bar import HealthBar
from enemy import animate_enemy
from player import animate_player


# layout
PLAYER_X_POS = 0  # 150
PLAYER_Y_POS = HEIGHT * 0.67
ENEMY_BASE_X_POS = 700
ENEMY_Y_POS = HEIGHT * 0.66
ENEMY_SPACING = 150
HEALTHBAR_WIDTH = 250
HEALTHBAR_HEIGHT = 25
SCALE_PLAYER = 3.5
SCALE_ENEMY = 2.5


def draw_bg(screen, background_img) -> None:
    screen.blit(background_img, (0, 0))


def draw_panel(screen, panel_img, player, enemies, potion_button) -> None:
    screen.blit(panel_img, (0, HEIGHT - PANEL_HEIGHT))

    # player stats
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

    # enemy stats (len == 2 prints enemies in reverse)
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


def draw_text(screen, text, x, y, colour="white", size="med", position="center"):
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


def draw_health_bar(screen, hp, max_hp, x, y):
    health_bar = HealthBar(
        width=HEALTHBAR_WIDTH, height=HEALTHBAR_HEIGHT, hp=hp, max_hp=max_hp
    )
    health_bar.draw(screen, hp=hp, x=x, y=y)


def draw_characters(screen, player, enemies, animations):
    # player.x_pos = PLAYER_X_POS
    player.y_pos = PLAYER_Y_POS

    animate_player(screen, player, animations, scale=SCALE_PLAYER)

    for enemy in enemies:
        enemy.y_pos = ENEMY_Y_POS
        enemy.update_hitbox(enemy.x_pos - 50, ENEMY_Y_POS - 140)

        animate_enemy(
            screen=screen,
            animations=animations,
            enemy=enemy,
            scale=SCALE_ENEMY,
        )
