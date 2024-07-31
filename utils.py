from constants import (
    FONT,
    FONT_SM,
    FONT_LG,
    WIDTH,
    HEIGHT,
    PANEL_HEIGHT,
)
from health_bar import HealthBar
from animations import animate_character
from enemy import animate_enemy
from player import animate_player


def draw_bg(screen, background_img):
    screen.blit(background_img, (0, 0))


def draw_panel(screen, panel_img, player, enemies, potion_button):
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
    player.x_pos = 200
    player.y_pos = HEIGHT * 0.68
    
    animate_player(
        screen,
        player,
        animations,
        scale=3.5
    )

    for i, enemy in enumerate(enemies):
        x_pos = 700 - i * 150
        y_pos = HEIGHT * 0.65
        enemy.x_pos = x_pos
        enemy.y_pos = y_pos
        enemy.update_hitbox(x_pos - 50, y_pos - 140)
        
        animate_enemy(
            screen=screen,
            animations=animations,
            enemy=enemy,
            scale=2.5,
        )
        
    
        

