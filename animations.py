import pygame
from spritesheet import Spritesheet
from constants import WIDTH, HEIGHT


class Animation:
    def __init__(self, spritesheet, frame_names, frame_width, frame_height):
        self.frames = [spritesheet.parse_sprite(name) for name in frame_names]
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.current_frame = 0
        self.animation_speed = 10  # fps
        self.clock = pygame.time.Clock()

    def get_current_frame(self, scale=1):
        frame = self.frames[self.current_frame]
        if scale != 1:
            frame = pygame.transform.scale(
                frame, (int(self.frame_width * scale), int(self.frame_height * scale))
            )
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.clock.tick(self.animation_speed)
        return frame


def animate_character(screen, animations, name, action, scale, x_pos, y_pos):
    
    if name == 'Enemy':
        name = 'Bringer'
    if name == 'Bringer of Death':
        name = 'Bringer'
        
    scale = scale-0.5 if name == "Brute" else scale
    current_animation = animations[name][action]
    current_frame = current_animation.get_current_frame(scale=scale)

    frame_width = current_frame.get_width()
    frame_height = current_frame.get_height()
    x_pos = x_pos - frame_width // 1.75
    y_pos = y_pos - frame_height 

    screen.blit(current_frame, (x_pos, y_pos))
    

def load_character_animations():
    frame_width, frame_height = 250, 300 
    animations = {}

    # load sprite sheets
    berserker_attack = Spritesheet(
        "graphics/characters/berserker/berserker_attack.png", frame_width, frame_height
    )
    berserker_death = Spritesheet(
        "graphics/characters/berserker/berserker_death.png", frame_width, frame_height
    )
    berserker_hurt = Spritesheet(
        "graphics/characters/berserker/berserker_hurt.png", frame_width, frame_height
    )
    berserker_idle = Spritesheet(
        "graphics/characters/berserker/berserker_idle.png", frame_width, frame_height
    )
    berserker_special = Spritesheet(
        "graphics/characters/berserker/berserker_special.png", frame_width, frame_height
    )

    brute_attack = Spritesheet(
        "graphics/characters/brute/brute_attack.png", frame_width, frame_height
    )
    brute_death = Spritesheet(
        "graphics/characters/brute/brute_death.png", frame_width, frame_height
    )
    brute_hurt = Spritesheet(
        "graphics/characters/brute/brute_hurt.png", frame_width, frame_height
    )
    brute_idle = Spritesheet(
        "graphics/characters/brute/brute_idle.png", frame_width, frame_height
    )
    brute_special = Spritesheet(
        "graphics/characters/brute/brute_special.png", frame_width, frame_height
    )

    huntress_attack = Spritesheet(
        "graphics/characters/huntress/huntress_attack.png", frame_width, frame_height
    )
    huntress_death = Spritesheet(
        "graphics/characters/huntress/huntress_death.png", frame_width, frame_height
    )
    huntress_hurt = Spritesheet(
        "graphics/characters/huntress/huntress_hurt.png", frame_width, frame_height
    )
    huntress_idle = Spritesheet(
        "graphics/characters/huntress/huntress_idle.png", frame_width, frame_height
    )
    huntress_special = Spritesheet(
        "graphics/characters/huntress/huntress_attack.png", frame_width, frame_height
    )

    rouge_attack = Spritesheet(
        "graphics/characters/rouge/rouge_attack.png", frame_width, frame_height
    )
    rouge_death = Spritesheet(
        "graphics/characters/rouge/rouge_death.png", frame_width, frame_height
    )
    rouge_hurt = Spritesheet(
        "graphics/characters/rouge/rouge_hurt.png", frame_width, frame_height
    )
    rouge_idle = Spritesheet(
        "graphics/characters/rouge/rouge_idle.png", frame_width, frame_height
    )
    rouge_special = Spritesheet(
        "graphics/characters/rouge/rouge_special.png", frame_width, frame_height
    )

    warrior_attack = Spritesheet(
        "graphics/characters/warrior/warrior_attack.png", frame_width, frame_height
    )
    warrior_death = Spritesheet(
        "graphics/characters/warrior/warrior_death.png", frame_width, frame_height
    )
    warrior_hurt = Spritesheet(
        "graphics/characters/warrior/warrior_hurt.png", frame_width, frame_height
    )
    warrior_idle = Spritesheet(
        "graphics/characters/warrior/warrior_idle.png", frame_width, frame_height
    )
    warrior_special = Spritesheet(
        "graphics/characters/warrior/warrior_special.png", frame_width, frame_height
    )
    
    wizard1_attack = Spritesheet(
        "graphics/enemies/wizard1/wizard1_attack.png", frame_width, frame_height
    )
    wizard1_death = Spritesheet(
        "graphics/enemies/wizard1/wizard1_death.png", frame_width, frame_height
    )
    wizard1_hurt = Spritesheet(
        "graphics/enemies/wizard1/wizard1_hurt.png", frame_width, frame_height
    )
    wizard1_idle = Spritesheet(
        "graphics/enemies/wizard1/wizard1_idle.png", frame_width, frame_height
    )
    
    golem_attack = Spritesheet(
        "graphics/enemies/golem/golem_attack.png", frame_width, frame_height
    )
    golem_death = Spritesheet(
        "graphics/enemies/golem/golem_death.png", frame_width, frame_height
    )
    golem_hurt = Spritesheet(
        "graphics/enemies/golem/golem_hurt.png", frame_width, frame_height
    )
    golem_idle = Spritesheet(
        "graphics/enemies/golem/golem_idle.png", frame_width, frame_height
    )

    wizard2_attack = Spritesheet(
        "graphics/enemies/wizard2/wizard2_attack.png", frame_width, frame_height
    )
    wizard2_death = Spritesheet(
        "graphics/enemies/wizard2/wizard2_death.png", frame_width, frame_height
    )
    wizard2_hurt = Spritesheet(
        "graphics/enemies/wizard2/wizard2_hurt.png", frame_width, frame_height
    )
    wizard2_idle = Spritesheet(
        "graphics/enemies/wizard2/wizard2_idle.png", frame_width, frame_height
    )
    
    bringer_attack = Spritesheet(
        "graphics/enemies/bringer_of_death/bringer_attack.png", frame_width, frame_height
    )
    bringer_death = Spritesheet(
        "graphics/enemies/bringer_of_death/bringer_death.png", frame_width, frame_height
    )
    bringer_hurt = Spritesheet(
        "graphics/enemies/bringer_of_death/bringer_hurt.png", frame_width, frame_height
    )
    bringer_idle = Spritesheet(
        "graphics/enemies/bringer_of_death/bringer_idle.png", frame_width, frame_height
    )
    

    # frames for each animation
    berserker_attack_frames = [f"{i}.png" for i in range(1, 8)]
    berserker_death_frames = [f"{i}.png" for i in range(1, 8)]
    berserker_hurt_frames = [f"{i}.png" for i in range(1, 4)]
    berserker_idle_frames = [f"{i}.png" for i in range(1, 11)]
    berserker_special_frames = [f"{i}.png" for i in range(1, 9)]

    brute_attack_frames = [f"{i}.png" for i in range(1, 8)]
    brute_death_frames = [f"{i}.png" for i in range(1, 12)]
    brute_hurt_frames = [f"{i}.png" for i in range(1, 5)]
    brute_idle_frames = [f"{i}.png" for i in range(1, 12)]
    brute_special_frames = [f"{i}.png" for i in range(1, 8)]

    huntress_attack_frames = [f"{i}.png" for i in range(1, 7)]
    huntress_death_frames = [f"{i}.png" for i in range(1, 11)]
    huntress_hurt_frames = [f"{i}.png" for i in range(1, 4)]
    huntress_idle_frames = [f"{i}.png" for i in range(1, 11)]
    huntress_special_frames = [f"{i}.png" for i in range(1, 7)]

    rouge_attack_frames = [f"{i}.png" for i in range(1, 5)]
    rouge_death_frames = [f"{i}.png" for i in range(1, 7)]
    rouge_hurt_frames = [f"{i}.png" for i in range(1, 5)]
    rouge_idle_frames = [f"{i}.png" for i in range(1, 9)]
    rouge_special_frames = [f"{i}.png" for i in range(1, 5)]

    warrior_attack_frames = [f"{i}.png" for i in range(1, 5)]
    warrior_death_frames = [f"{i}.png" for i in range(1, 10)]
    warrior_hurt_frames = [f"{i}.png" for i in range(1, 4)]
    warrior_idle_frames = [f"{i}.png" for i in range(1, 11)]
    warrior_special_frames = [f"{i}.png" for i in range(1, 6)]
    
    # generate frame in reverse 
    wizard1_attack_frames = [f"{i}.png" for i in range(8, 0, -1)]  
    wizard1_death_frames = [f"{i}.png" for i in range(7, 0, -1)]
    wizard1_hurt_frames = [f"{i}.png" for i in range(3, 0, -1)]    
    wizard1_idle_frames = [f"{i}.png" for i in range(8, 0, -1)]
    
    wizard2_attack_frames = [f"{i}.png" for i in range(13, 0, -1)]
    wizard2_death_frames = [f"{i}.png" for i in range(18, 0, -1)]
    wizard2_hurt_frames = [f"{i}.png" for i in range(3, 0, -1)]
    wizard2_idle_frames = [f"{i}.png" for i in range(10, 0, -1)]
    
    golem_attack_frames = [f"{i}.png" for i in range(11, 0, -1)]
    golem_death_frames = [f"{i}.png" for i in range(13, 0, -1)]
    golem_hurt_frames = [f"{i}.png" for i in range(4, 0, -1)]
    golem_idle_frames = [f"{i}.png" for i in range(8, 0, -1)]
    
    bringer_attack_frames = [f"{i}.png" for i in range(1, 11)]
    bringer_death_frames = [f"{i}.png" for i in range(1, 12)]
    bringer_hurt_frames = [f"{i}.png" for i in range(1, 4)]
    bringer_idle_frames = [f"{i}.png" for i in range(1, 9)]

    
    # store animations dictionary to access
    animations["Berserker"] = {
        "attack": Animation(
            berserker_attack, berserker_attack_frames, frame_width, frame_height
        ),
        "death": Animation(
            berserker_death, berserker_death_frames, frame_width, frame_height
        ),
        "hurt": Animation(
            berserker_hurt, berserker_hurt_frames, frame_width, frame_height
        ),
        "idle": Animation(
            berserker_idle, berserker_idle_frames, frame_width, frame_height
        ),
        "special": Animation(
            berserker_special, berserker_special_frames, frame_width, frame_height
        ),
    }

    animations["Brute"] = {
        "attack": Animation(
            brute_attack, brute_attack_frames, frame_width, frame_height
        ),
        "death": Animation(brute_death, brute_death_frames, frame_width, frame_height),
        "hurt": Animation(brute_hurt, brute_hurt_frames, frame_width, frame_height),
        "idle": Animation(brute_idle, brute_idle_frames, frame_width, frame_height),
        "special": Animation(
            brute_special, brute_special_frames, frame_width, frame_height
        ),
    }

    animations["Huntress"] = {
        "attack": Animation(
            huntress_attack, huntress_attack_frames, frame_width, frame_height
        ),
        "death": Animation(
            huntress_death, huntress_death_frames, frame_width, frame_height
        ),
        "hurt": Animation(
            huntress_hurt, huntress_hurt_frames, frame_width, frame_height
        ),
        "idle": Animation(
            huntress_idle, huntress_idle_frames, frame_width, frame_height
        ),
        "special": Animation(
            huntress_special, huntress_special_frames, frame_width, frame_height
        ),
    }

    animations["Rouge"] = {
        "attack": Animation(
            rouge_attack, rouge_attack_frames, frame_width, frame_height
        ),
        "death": Animation(rouge_death, rouge_death_frames, frame_width, frame_height),
        "hurt": Animation(rouge_hurt, rouge_hurt_frames, frame_width, frame_height),
        "idle": Animation(rouge_idle, rouge_idle_frames, frame_width, frame_height),
        "special": Animation(
            rouge_special, rouge_special_frames, frame_width, frame_height
        ),
    }

    animations["Warrior"] = {
        "attack": Animation(
            warrior_attack, warrior_attack_frames, frame_width, frame_height
        ),
        "death": Animation(
            warrior_death, warrior_death_frames, frame_width, frame_height
        ),
        "hurt": Animation(warrior_hurt, warrior_hurt_frames, frame_width, frame_height),
        "idle": Animation(warrior_idle, warrior_idle_frames, frame_width, frame_height),
        "special": Animation(
            warrior_special, warrior_special_frames, frame_width, frame_height
        ),
    }
    
    animations["Wizard1"] = {
        "attack": Animation(
            wizard1_attack, wizard1_attack_frames, frame_width, frame_height
        ),
        "death": Animation(
            wizard1_death, wizard1_death_frames, frame_width, frame_height
        ),
        "hurt": Animation(wizard1_hurt, wizard1_hurt_frames, frame_width, frame_height),
        "idle": Animation(wizard1_idle, wizard1_idle_frames, frame_width, frame_height),
    }
    
    animations["Wizard2"] = {
        "attack": Animation(
            wizard2_attack, wizard2_attack_frames, frame_width, frame_height
        ),
        "death": Animation(
            wizard2_death, wizard2_death_frames, frame_width, frame_height
        ),
        "hurt": Animation(wizard2_hurt, wizard2_hurt_frames, frame_width, frame_height),
        "idle": Animation(wizard2_idle, wizard2_idle_frames, frame_width, frame_height),
    }

    animations["Golem"] = {
        "attack": Animation(
            golem_attack, golem_attack_frames, frame_width, frame_height
        ),
        "death": Animation(
            golem_death, golem_death_frames, frame_width, frame_height
        ),
        "hurt": Animation(golem_hurt, golem_hurt_frames, frame_width, frame_height),
        "idle": Animation(golem_idle, golem_idle_frames, frame_width, frame_height),
    }

    animations["Bringer"] = {
        "attack": Animation(
            bringer_attack, bringer_attack_frames, frame_width, frame_height
        ),
        "death": Animation(bringer_death, bringer_death_frames, frame_width, frame_height),
        "hurt": Animation(bringer_hurt, bringer_hurt_frames, frame_width, frame_height),
        "idle": Animation(bringer_idle, bringer_idle_frames, frame_width, frame_height),
    }

    return animations
