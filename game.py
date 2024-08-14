import pygame
from random import randint
from constants import (
    SCREEN,
    WIDTH,
    CLOCK,
    FPS,
    FOREST1,
    CASTLE2,
    CASTLE3,
    PANEL,
    HEIGHT,
    PANEL_HEIGHT,
    POTION,
    VICTORY,
    EXIT,
    DEFEAT,
)
from utils import draw_text, draw_bg, draw_panel, draw_characters
from player import create_character
from enemy import create_enemy, create_boss
from animations import load_character_animations
from battle import (
    handle_actions,
    damage_text_group,
    heal_text_group,
    potion_text_group,
    crit_text_group,
)
from button import Button
from enum import Enum, auto


display_round_over = True
round_display_duration = 25


class GameState(Enum):
    RUNNING = auto()
    NOT_RUNNING = auto()
    PLAYER_WIN = auto()
    PLAYER_LOSS = auto()
    GAME_OVER_PLAYER_WIN = auto()


def main(selected_char: int, on_exit):
    """
    Initialize the game and start the main game loop.
    """
    pygame.init()
    game = Game(selected_char, on_exit)
    game.run()


class Game:
    """
    Game class encapsulates all game logic and controls the main game loop.

    Attributes:
        player (Character): Player character instance.
        animations (dict): Dictionary containing character animations.
        round (int): Current round number.
        current_level (int): Current level of the game.
        backgrounds (list): List of background images for each level.
        player_target_position (int): Target x-coordinate for player's walk in.
        enemy_start_position (int): Starting x-coordinate for enemies before walk in.
        enemy_target_position (int): Target x-coordinate for enemies' walk in.
        game_state (GameState): Current state of the game depending on player actions.
        on_exit: Callback function when the game is over.
    """

    def __init__(self, selected_char: int, on_exit):
        self.player = create_character(selected_char)
        self.animations = load_character_animations()
        self.round: int = 1
        self.current_level: int = 1
        self.backgrounds = [FOREST1, CASTLE3, CASTLE2]
        self.player_target_position = 100
        self.enemy_start_position: int = WIDTH + 10
        self.enemy_target_position: int = 700
        self.game_state: GameState = GameState.RUNNING
        self.on_exit = on_exit

    def run(self) -> None:
        """
        Runs the main game loop for the three levels.
        """
        while self.current_level <= 3:
            self.play_level()

    def play_level(self) -> None:
        """
        Play a single level of the game, managing rounds and enemies.
        """
        total_level_enemies = self.round + randint(0, 0)

        while total_level_enemies >= 0:
            self.player_walk_in()

            if total_level_enemies <= 1:
                enemies = [create_boss(self.current_level - 1)]
                total_level_enemies = 0
                current_round_enemies = 1
            else:
                current_round_enemies = min(randint(1, 2), total_level_enemies - 1)
                enemies = [
                    create_enemy(randint(0, 1)) for _ in range(current_round_enemies)
                ]

            total_level_enemies -= current_round_enemies
            self.enemy_walk_in(enemies)
            self.play_round(enemies)
            self.round += 1

        self.current_level += 1

    def play_round(self, enemies) -> None:
        """
        Manage the game logic for a single round.

        Args:
            enemies (list): List of enemy instances for the round.
        """
        global display_round_over, round_display_duration
        current_fighter = 0
        action_cooldown = 0
        self.game_state = GameState.RUNNING

        while self.game_state == GameState.RUNNING:
            clicked = self.handle_events()

            self.draw_background()
            potion_button = self.draw_ui_elements(enemies)

            current_fighter, action_cooldown = handle_actions(
                SCREEN,
                clicked=clicked,
                current_fighter=current_fighter,
                player=self.player,
                enemies=enemies,
                potion_button=potion_button,
                action_cooldown=action_cooldown,
            )

            self.update_sprites(enemies=enemies)
            self.update_screen()

            if self.player.hp <= 0:
                if display_round_over:
                    self.display_round_over_message(is_success=True)
                else:
                    round_display_duration = 25
                    display_round_over = True
                    self.game_state = GameState.PLAYER_LOSS

            if all(enemy.hp <= 0 for enemy in enemies):
                if display_round_over:
                    self.display_round_over_message(is_success=False)
                else:
                    round_display_duration = 25
                    display_round_over = True

                    self.game_state = GameState.NOT_RUNNING
                    if enemies[0].type == "boss" and self.current_level == 1:
                        self.game_state = GameState.GAME_OVER_PLAYER_WIN

            pygame.display.update()
            CLOCK.tick(FPS)

        self.display_game_over_message()

        if self.game_state == GameState.PLAYER_WIN:
            self.player_walk_out(speed=20, is_boss=enemies[0].type == "boss")

    def display_game_over_message(self) -> None:
        """
        Display a message indicating the outcome of the game.
        """
        SCREEN.fill((0, 0, 0))

        if self.game_state == GameState.GAME_OVER_PLAYER_WIN:
            pygame.mouse.set_visible(True)
            running = True
            while running:
                SCREEN.fill((0, 0, 0))
                clicked = self.handle_events()

                victory_icon = Button(
                    SCREEN,
                    x=WIDTH // 2,
                    y=180,
                    image=VICTORY,
                    width=280,
                    height=64,
                )
                victory_icon.draw()

                draw_text(
                    SCREEN,
                    text="JOURNEY IS OVER",
                    x=WIDTH // 2,
                    y=250,
                    colour="white",
                    size="lg",
                    position="center",
                )

                exit_button = Button(
                    SCREEN,
                    x=WIDTH // 2,
                    y=380,
                    image=EXIT,
                    width=92 * 2,
                    height=28 * 2,
                )
                exit_button.draw()

                if clicked:
                    mouse_pos = pygame.mouse.get_pos()
                    if exit_button.rect.collidepoint(mouse_pos):
                        running = False
                        if self.on_exit:
                            self.on_exit()

                pygame.display.update()
                CLOCK.tick(FPS)

        elif self.game_state == GameState.PLAYER_LOSS:
            pygame.mouse.set_visible(True)
            running = True
            while running:
                SCREEN.fill((0, 0, 0))
                clicked = self.handle_events()

                defeat_icon = Button(
                    SCREEN,
                    x=WIDTH // 2,
                    y=180,
                    image=DEFEAT,
                    width=240,
                    height=64,
                )
                defeat_icon.draw()

                draw_text(
                    SCREEN,
                    text="JOURNEY IS OVER",
                    x=WIDTH // 2,
                    y=250,
                    colour="white",
                    size="lg",
                    position="center",
                )

                exit_button = Button(
                    SCREEN,
                    x=WIDTH // 2,
                    y=380,
                    image=EXIT,
                    width=92 * 2,
                    height=28 * 2,
                )
                exit_button.draw()

                if clicked:
                    mouse_pos = pygame.mouse.get_pos()
                    if exit_button.rect.collidepoint(mouse_pos):
                        running = False
                        if self.on_exit:
                            self.on_exit()

                pygame.display.update()
                CLOCK.tick(FPS)

    def display_round_over_message(self, is_success: bool = True) -> None:
        """
        Displays the round over message without blocking the game loop.

        Args:
            is_success (bool): True if player has defeated enemies, False otherwise.
        """
        global display_round_over, round_display_duration

        if round_display_duration > 0:
            text = (
                "SUCCESS! ENEMIES DEFEATED"
                if is_success
                else "FAILURE! YOU HAVE BEEN DEFEATED"
            )
            draw_text(
                SCREEN,
                text=text,
                x=WIDTH // 2,
                y=100,
                colour="white",
                size="lg",
                position="center",
            )
            round_display_duration -= 1
        else:
            display_round_over = False

    def handle_events(self) -> bool:
        """
        Handle player input and events.

        Returns:
            bool: True of the mouse button is clicked, False otherwise.
        """
        clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        return clicked

    def player_walk_in(self) -> None:
        """
        Handle the player's walking animation into the screen.
        """
        self.player.x_pos = 0
        self.player.walk(target_x=self.player_target_position)

        while self.player.x_pos < self.player_target_position:
            self.handle_events()
            SCREEN.fill((0, 0, 0))

            draw_text(
                SCREEN,
                text=f"LEVEL: {self.current_level} ROUND: {self.round}",
                x=WIDTH // 2,
                y=100,
                colour="white",
                size="lg",
                position="center",
            )

            self.player.update_walk_pos(target_x=self.player_target_position)
            self.player.update_animation()

            draw_characters(SCREEN, self.player, {}, self.animations)
            pygame.display.update()
            CLOCK.tick(FPS)

    def player_walk_out(self, speed: int = 5, is_boss=False) -> None:
        """
        Handle the player's walking animtion out of the screen.

        Args:
            speed (int): Speed of the player's walking animation.
        """
        target_x = WIDTH + 50
        self.player.walk(target_x=target_x)

        while self.player.x_pos < target_x:
            self.player.update_walk_pos(target_x=target_x, speed=speed)
            self.player.update_animation()

            SCREEN.fill((0, 0, 0))
            draw_characters(
                SCREEN, player=self.player, enemies=[], animations=self.animations
            )
            if is_boss:
                draw_text(
                    SCREEN,
                    text="BUT THE JOURNEY ISN'T OVER YET",
                    x=WIDTH // 2,
                    y=100,
                    colour="white",
                    size="lg",
                    position="center",
                )
            else:
                draw_text(
                    SCREEN,
                    text="SUCCESS! ENEMIES DEFEATED",
                    x=WIDTH // 2,
                    y=100,
                    colour="white",
                    size="lg",
                    position="center",
                )
            pygame.display.update()
            CLOCK.tick(FPS)

    def enemy_walk_in(self, enemies):
        """
        Handle the walking animation for enemies entering the screen.

        Args:
            enemies (list): List of enemy instances.
        """
        for i, enemy in enumerate(enemies):
            enemy.x_pos = self.enemy_start_position + (1 - i) * 130
            walk_target = (
                540
                if enemy.name == "Bringer"
                else self.enemy_target_position - (1 - i) * 130
            )
            target_x = (
                walk_target
                if enemy.name == "Bringer"
                else self.enemy_target_position - i * 130
            )
            enemy.walk(target_x=walk_target)

        enemies_moving = True
        while enemies_moving:
            enemies_moving = False
            for i, enemy in enumerate(enemies):
                enemy.update_walk_pos(target_x=target_x, speed=20)
                enemy.update_animation()
                if enemy.x_pos > target_x:
                    enemies_moving = True

            SCREEN.fill((0, 0, 0))
            draw_text(
                SCREEN,
                text=f"LEVEL: {self.current_level} ROUND: {self.round}",
                x=WIDTH // 2,
                y=100,
                colour="white",
                size="lg",
                position="center",
            )
            draw_characters(SCREEN, self.player, enemies, self.animations)
            pygame.display.update()
            CLOCK.tick(FPS)

    def draw_background(self) -> None:
        """
        Draw the background for the current_level.
        """
        background_img_scaled = pygame.transform.smoothscale(
            self.backgrounds[self.current_level - 1], (WIDTH, HEIGHT - PANEL_HEIGHT)
        )
        draw_bg(SCREEN, background_img_scaled)

    def draw_ui_elements(self, enemies) -> Button:
        """
        Draw UI elements, including the characters and panel

        Args:
            enemies(list): List of enemy instances for the round.

        Returns:
            Button: Potion button instance.
        """
        potion_button = Button(
            SCREEN,
            x=120,
            y=HEIGHT - PANEL_HEIGHT * 0.25,
            image=POTION,
            width=55,
            height=55,
        )
        draw_panel(SCREEN, PANEL, self.player, enemies, potion_button)
        draw_characters(
            SCREEN, self.player, enemies, self.animations, self.current_level
        )
        return potion_button

    def update_sprites(self, enemies) -> None:
        """
        Update and draw sprite groups for characters and action texts.

        Args:
            enemies (List): List of enemy instances.
        """
        damage_text_group.update()
        damage_text_group.draw(SCREEN)
        heal_text_group.update()
        heal_text_group.draw(SCREEN)
        crit_text_group.update()
        crit_text_group.draw(SCREEN)

        for sprite in potion_text_group:
            if sprite.counter >= 0:
                potion_text_group.draw(SCREEN)

        self.player.update_animation()

        for enemy in enemies:
            enemy.update_animation()

    def update_screen(self) -> None:
        """
        Update the display.
        """
        pygame.display.update()


if __name__ == "__main__":
    main()
