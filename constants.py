import pygame

pygame.init()

# colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# screen dimensions
WIDTH = 800
HEIGHT = 550
PANEL_HEIGHT = 150

# fonts
FONT_SM = pygame.font.SysFont("Times New Roman", 18)
FONT = pygame.font.SysFont("Times New Roman", 26)
FONT_LG = pygame.font.SysFont("Times New Roman", 36)

# game settings
FPS = 60
ACTION_WAIT_TIME = 90
POTION_EFFECT = 15
CLOCK = pygame.time.Clock()

# Pygame screen initialization
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DungeonQUEST")

# backgrounds
FOREST1 = pygame.image.load("graphics/backgrounds/forest1.png").convert_alpha()
FOREST2 = pygame.image.load("graphics/backgrounds/forest2.png").convert_alpha()
CASTLE1 = pygame.image.load("graphics/backgrounds/castle1.jpg").convert_alpha()
CASTLE2 = pygame.image.load("graphics/backgrounds/castle2.jpg").convert_alpha()
CASTLE3 = pygame.image.load("graphics/backgrounds/castle3.jpg").convert_alpha()

# icons
PANEL = pygame.image.load("graphics/icons/panel.png").convert_alpha()
SWORD = pygame.image.load("graphics/icons/sword.png").convert_alpha()
POTION = pygame.image.load("graphics/icons/potion.png").convert_alpha()
VICTORY = pygame.image.load("graphics/icons/victory.png").convert_alpha()
DEFEAT = pygame.image.load("graphics/icons/defeat.png").convert_alpha()

# buttons
RESTART = pygame.image.load("graphics/icons/restart.png").convert_alpha()
PLAY = pygame.image.load("graphics/buttons/play.png").convert_alpha()
CONTINUE = pygame.image.load("graphics/buttons/continue.png").convert_alpha()
TUTORIAL = pygame.image.load("graphics/buttons/tutorial.png").convert_alpha()
BACK = pygame.image.load("graphics/buttons/back.png").convert_alpha()
EXIT = pygame.image.load("graphics/buttons/exit.png").convert_alpha()
QUIT = pygame.image.load("graphics/buttons/quit.png").convert_alpha()

# character stats
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
        "description": "Powerful and reckless, but \nlacks armor.",
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
