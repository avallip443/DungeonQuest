import pygame
from constants import (
    FONT,
    FONT_SM,
    FONT_LG,
    WIDTH,
    HEIGHT,
    PANEL_HEIGHT,
    POTION,
    CLOCK, 
    FPS
)
from health_bar import HealthBar
from button import Button
from animations import load_character_animations, animate_character


def draw_bg(screen, background_img):
    screen.blit(background_img, (0, 0))


def draw_panel(screen, panel_img, player, enemies):
    screen.blit(panel_img, (0, HEIGHT - PANEL_HEIGHT))

    draw_text(
        screen,
        f"{player.name} HP: {player.hp}",
        x=WIDTH // 4,
        y=HEIGHT - PANEL_HEIGHT + 30,
        colour='white',
    )

    player_healthbar = HealthBar(
        width=250, height=25, hp=player.hp, max_hp=player.max_hp
    )
    player_healthbar.draw(
        screen, hp=player.hp, x=WIDTH // 4 - 250 // 2, y=HEIGHT - PANEL_HEIGHT + 50
    )
    potion_button = Button(
        screen, x=120, y=HEIGHT - PANEL_HEIGHT * 0.25, image=POTION, width=55, height=55
    )

    potion_button.draw()
    draw_text(
        screen, str(player.potions), x=140, y=HEIGHT - PANEL_HEIGHT * 0.35, size="sm"
    )

    for i, enemy in enumerate(enemies):
        text_y = PANEL_HEIGHT // 2 - 20 if len(enemies) == 1 else 20 + i * 70
        bar_y = PANEL_HEIGHT // 2 if len(enemies) == 1 else 40 + i * 70
        
        draw_text(
            screen,
            f"{enemy.name}",
            x=WIDTH * 0.75,
            y=HEIGHT - PANEL_HEIGHT + text_y,
            colour='white',
        )
        enemy_healthbar = HealthBar(
            width=250, height=25, hp=enemy.hp, max_hp=enemy.max_hp
        )
        enemy_healthbar.draw(
            screen,
            hp=enemy.hp,
            x=WIDTH * 0.75 - 250 // 2,
            y=HEIGHT - PANEL_HEIGHT + bar_y,
        )


def draw_text(screen, text, x, y, colour="white", size="med", position="center"):
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


def draw_characters(screen, player, enemies, animations):
    for i, enemy in enumerate(enemies):
        animate_character(
            screen,
            animations,
            name=enemy.name,
            action=enemy.action,
            scale=2.5,
            x_pos=700 - i * 150,
            y_pos=HEIGHT * 0.65,
        )
        
    animate_character(
        screen,
        animations,
        name=player.name,
        action=player.action,
        scale=3.5,
        x_pos=200,
        y_pos=HEIGHT * 0.68,
    )
