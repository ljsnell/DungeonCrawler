import Human_Character
from Game_States import GAME_OVER, CHOOSING_PATH, IN_BATTLE, SHOPPING
import random
import os

enemy_character = Human_Character.HumanCharacter("Evil Harold", 5, 10, 5, 3)
player_character = Human_Character.HumanCharacter("Harold", 7, 10, 7, 2)

game_loop = 1
options = ['ra', 'c', 'la']

while(game_loop != GAME_OVER):
    choice = input('Enter Battle (b), or Shopping (s)').lower()
    if choice == 'b':
        game_loop = IN_BATTLE
        print('**************************')
        while(game_loop == IN_BATTLE):
            # Battle                
            os.system('cls' if os.name == 'nt' else 'clear')

            enemy_character.display()
            player_character.display()

            target_location = input('Select Target Location: ')

            # Calculate Damage & HP
            enemy_character.determine_damage(target_location, player_character.damage)
            player_character.determine_damage(random.choice(options), enemy_character.damage)

            if (enemy_character.is_alive() == False) and (player_character.is_alive() == True):
                game_loop = CHOOSING_PATH
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Victory!')
                enemy_character.display_defeat()
                player_character.display()

            if (player_character.is_alive() == False):
                game_loop = GAME_OVER
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Gruesome Defeat')
                enemy_character.display()
                player_character.display_defeat()
    elif choice == 's':
        game_loop = SHOPPING

# Shopping

