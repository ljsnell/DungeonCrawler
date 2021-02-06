import Human_Character

import random
import os

enemy_character = Human_Character.HumanCharacter(5, 10, 5, 3)
player_character = Human_Character.HumanCharacter(7, 10, 7, 2)

game_loop = 1
options = ['ra', 'c', 'la']

print('**************************')
while(game_loop == 1):
    os.system('cls' if os.name == 'nt' else 'clear')

    enemy_character.display()
    player_character.display()

    target_location = input('Select Target Location: ')

    # Calculate Damage & HP
    enemy_character.determine_damage(target_location, player_character.damage)
    player_character.determine_damage(random.choice(options), enemy_character.damage)

    if (enemy_character.is_alive() == False) and (player_character.is_alive() == True):
        game_loop = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Victory!')
        enemy_character.display()
        player_character.display()

    if (enemy_character.is_alive() == False) and (game_loop == 1):
        game_loop = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Gruesome Defeat')
        enemy_character.display()
        player_character.display()