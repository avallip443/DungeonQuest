import pygame
from spritesheet import Spritesheet


class Animation:
    def __init__(self, spritesheet, frame_names, frame_width, frame_height):
        self.frames = [spritesheet.parse_sprite(name) for name in frame_names]
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.current_frame = 0
        self.animation_speed = 10  # Frames per second
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


def load_character_animations():
    frame_width, frame_height = 190, 250 
    animations = {}

    # Load sprite sheets
    berserker_attack = Spritesheet(
        "Characters/Berserker/Berserker_Attack.png", frame_width, frame_height
    )
    berserker_death = Spritesheet(
        "Characters/Berserker/Berserker_Death.png", frame_width, frame_height
    )
    berserker_hurt = Spritesheet(
        "Characters/Berserker/Berserker_Hurt.png", frame_width, frame_height
    )
    berserker_idle = Spritesheet(
        "Characters/Berserker/Berserker_Idle.png", frame_width, frame_height
    )
    berserker_special = Spritesheet(
        "Characters/Berserker/Berserker_Special.png", frame_width, frame_height
    )

    brute_attack = Spritesheet(
        "Characters/Brute/Brute_Attack.png", frame_width, frame_height
    )
    brute_death = Spritesheet(
        "Characters/Brute/Brute_Death.png", frame_width, frame_height
    )
    brute_hurt = Spritesheet(
        "Characters/Brute/Brute_hurt.png", frame_width, frame_height
    )
    brute_idle = Spritesheet(
        "Characters/Brute/Brute_Idle.png", frame_width, frame_height
    )
    brute_special = Spritesheet(
        "Characters/Brute/Brute_Special.png", frame_width, frame_height
    )

    huntress_attack = Spritesheet(
        "Characters/Huntress/Huntress_Attack.png", frame_width, frame_height
    )
    huntress_death = Spritesheet(
        "Characters/Huntress/Huntress_Death.png", frame_width, frame_height
    )
    huntress_hurt = Spritesheet(
        "Characters/Huntress/Huntress_Hurt.png", frame_width, frame_height
    )
    huntress_idle = Spritesheet(
        "Characters/Huntress/Huntress_Idle.png", frame_width, frame_height
    )
    huntress_special = Spritesheet(
        "Characters/Huntress/Huntress_Attack.png", frame_width, frame_height
    )

    rouge_attack = Spritesheet(
        "Characters/Rouge/Rouge_Attack.png", frame_width, frame_height
    )
    rouge_death = Spritesheet(
        "Characters/Rouge/Rouge_Death.png", frame_width, frame_height
    )
    rouge_hurt = Spritesheet(
        "Characters/Rouge/Rouge_Hurt.png", frame_width, frame_height
    )
    rouge_idle = Spritesheet(
        "Characters/Rouge/Rouge_Idle.png", frame_width, frame_height
    )
    rouge_special = Spritesheet(
        "Characters/Rouge/Rouge_Special.png", frame_width, frame_height
    )

    warrior_attack = Spritesheet(
        "Characters/Warrior/Warrior_Attack.png", frame_width, frame_height
    )
    warrior_death = Spritesheet(
        "Characters/Warrior/Warrior_Death.png", frame_width, frame_height
    )
    warrior_hurt = Spritesheet(
        "Characters/Warrior/Warrior_Hurt.png", frame_width, frame_height
    )
    warrior_idle = Spritesheet(
        "Characters/Warrior/Warrior_Idle.png", frame_width, frame_height
    )
    warrior_special = Spritesheet(
        "Characters/Warrior/Warrior_Special.png", frame_width, frame_height
    )

    # Define the frames for each animation
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

    # Store the animations in a dictionary
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

    return animations
