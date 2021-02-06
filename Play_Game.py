import Human_Character
import Battle
from Game_States import GAME_OVER, CHOOSING_PATH, IN_BATTLE, SHOPPING

battle_station = Battle.Battle()

enemy_character = Human_Character.HumanCharacter("Evil Harold", 5, 10, 5, 3)
player_character = Human_Character.HumanCharacter("Harold", 7, 10, 7, 2)

game_status = CHOOSING_PATH

while(game_status != GAME_OVER):
    choice = input('Enter Battle (b), or Shopping (s)').lower()
    if choice == 'b':
        game_status = IN_BATTLE        
        game_status, player_character = battle_station.combat(enemy_character, player_character, game_status)
    elif choice == 's':
        game_status = SHOPPING

# Shopping

