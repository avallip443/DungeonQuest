import pygame

pygame.init()

# colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# screen dimensions
WIDTH = 800
HEIGHT = 550
PANEL_HEIGHT = 150

# graphics settings
FONT_SM = pygame.font.SysFont("Times New Roman", 18)
FONT = pygame.font.SysFont("Times New Roman", 26)
FONT_LG = pygame.font.SysFont("Times New Roman", 36)

# settings
FPS = 60
CLOCK = pygame.time.Clock()

# game settings
ACTION_WAIT_TIME = 90
POTION_EFFECT = 15

#  initalize pygame
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DungeonQUEST")

# IMAGES
BACKGROUND = pygame.image.load("graphics/backgrounds/background.png").convert_alpha()
PANEL = pygame.image.load("graphics/Icons/panel.png").convert_alpha()
SWORD = pygame.image.load("graphics/Icons/sword.png").convert_alpha()
POTION = pygame.image.load("graphics/Icons/potion.png").convert_alpha()
VICTORY = pygame.image.load("graphics/Icons/victory.png").convert_alpha()
DEFEAT = pygame.image.load("graphics/Icons/defeat.png").convert_alpha()

# BUTTONS
RESTART = pygame.image.load("graphics/Icons/restart.png").convert_alpha()
PLAY = pygame.image.load('Buttons/Play.png').convert_alpha()
CONTINUE = pygame.image.load("Buttons/Continue.png").convert_alpha()
TUTORIAL = pygame.image.load("Buttons/Tutorial.png").convert_alpha()
BACK = pygame.image.load("Buttons/Back.png").convert_alpha()
EXIT = pygame.image.load("Buttons/Exit.png").convert_alpha()
QUIT = pygame.image.load("Buttons/Quit.png").convert_alpha()

# STATS
CHARACTERS = [
    {
        "name": "Warrior",
        "description": "Strong, tough, and good with \na sword. Well-rounded fighter.",
        "max_hp": 100,
        "attack": 20,
        "critical_chance": 2,
        "double_hit_chance": 2,
        "potion_drop_chance": 50,
        "potions": 3,
    },
    {
        "name": "Rouge",
        "description": "Quick and nimble, effective \nat landing critical attacks.",
        "max_hp": 85,
        "attack": 15,
        "critical_chance": 10,
        "double_hit_chance": 2,
        "potion_drop_chance": 55,
        "potions": 3,
    },
    {
        "name": "Berserker",
        "description": "Powerful and reckless, but \nlacks armour.",
        "max_hp": 75,
        "attack": 30,
        "critical_chance": 5,
        "double_hit_chance": 10,
        "potion_drop_chance": 60,
        "potions": 3,
    },
    {
        "name": "Brute",
        "description": "Hard-to-kill fighter, but packs \na weak punch.",
        "max_hp": 130,
        "attack": 15,
        "critical_chance": 2,
        "double_hit_chance": 2,
        "potion_drop_chance": 50,
        "potions": 3,
    },
    {
        "name": "Huntress",
        "description": "Precise ranged attacker, often \nlands multiple hits.",
        "max_hp": 85,
        "attack": 10,
        "critical_chance": 10,
        "double_hit_chance": 25,
        "potion_drop_chance": 45,
        "potions": 3,
    },
]
