from Game_States import IN_BATTLE, CHOOSING_PATH, GAME_OVER
import os
import random


class Battle:
    options = ['ra', 'c', 'la']

    def combat(self, enemy_character, player_character, game_status):
        while game_status == IN_BATTLE:
            print('**************************')
            # Battle
            os.system('cls' if os.name == 'nt' else 'clear')

            enemy_character.display()
            player_character.display()

            target_location = input('Select Target Location: ')

            # Calculate Damage & HP
            enemy_character.determine_damage(
                target_location, player_character.damage)
            player_character.determine_damage(
                random.choice(self.options), enemy_character.damage)

            if (enemy_character.is_alive() == False) and (player_character.is_alive() == True):
                game_loop = CHOOSING_PATH
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Victory!')
                enemy_character.display_defeat()
                player_character.display()
                player_character.gold += enemy_character.gold
                return game_loop, player_character

            if (player_character.is_alive() == False):
                game_loop = GAME_OVER
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Gruesome Defeat')
                enemy_character.display()
                player_character.display_defeat()
                return game_loop, player_character
