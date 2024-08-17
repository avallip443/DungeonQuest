## WarriorQuest: A Text-Based Adventure Game

Welcome to [WarriorQuest](https://avallip.itch.io/warriorquest)! Immerse yourself in this single-player, 2D turn-based RPG where you battle as one of five unique fighter characters, facing off against powerful enemies to become the ultimate warrior!

## Table of Contents

- [Game Overview](#game-overview)
- [Character Classes](#character-classes)
- [Installation](#installation)
- [How to Play](#how-to-play)

## Game Overview

This 2D RPG was built with Python and the Pygame library. In this game, players progress through levels, encountering enemies and engaging in turn-based battles. The goal is to survive through each level, defeat enemies, and ultimately conquer all foes.

## Character Classes

Player can choose from the following character classes:

1. **Warrior:** Strong, tough, and good with \na sword. Well-rounded fighter.
2. **Rouge:** Quick and nimble, effective at landing critical attacks.
3. **Berserker:** Powerful and reckless, but lacks armour for defense.
4. **Brute:** Hard-to-kill, but packs a weak punch.
5. **Huntress:**: Precise ranged attacker, often \nlands multiple hits.

Each class has a unique stat for maximum hitpoints, attack strength, critical hit chance, double hit chance, and potion drop chance from slain enemies.

## Installation
1. Clone this repository and run:
```sh
python3 -m pip install -U pygame --user
```
2. Run the game:
```sh
python main.py
```

## How to Play

To run the game, download all the files and run the main.py file in your terminal. 

Before the game begins, players will be prompted to selected a character. Then, for each round, a randomly-generated number of enemies will appear for the player to battle. For each turn, the player can either attack or heal (there is no running away). The game will run until either the player defeats all the enemies in the dungeon or dies trying. 

