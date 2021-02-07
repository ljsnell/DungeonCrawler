from Game_States import IN_BATTLE, CHOOSING_PATH, GAME_OVER, DELIMITER
import random
from Clear_Screen import clear_display


class Battle:
    options = ['ra', 'c', 'la']

    def combat(self, enemy_character, player_character, game_status):
        while game_status == IN_BATTLE:
            print(DELIMITER)
            # Battle
            clear_display()

            enemy_character.display()
            player_character.display()

            target_location = input('Select Target Location: ')

            # Calculate Damage & HP
            enemy_character.determine_damage(
                target_location, player_character.items[0].damage)
            player_character.determine_damage(
                random.choice(self.options), enemy_character.items[0].damage)

            if (enemy_character.is_alive() == False) and (player_character.is_alive() == True):
                game_loop = CHOOSING_PATH
                clear_display()
                print('Victory!')
                enemy_character.display_defeat()
                player_character.display()
                player_character.gold += enemy_character.gold
                return game_loop, player_character

            if (player_character.is_alive() == False):
                game_loop = GAME_OVER
                clear_display()
                print('Gruesome Defeat')
                enemy_character.display()
                player_character.display_defeat()
                return game_loop, player_character
