import Human_Character
import Battle
import Weapon
from Game_States import GAME_OVER, CHOOSING_PATH, IN_BATTLE, SHOPPING
from GraveStone import displayGrave

battle_station = Battle.Battle()
weapon_for_sale1 = Weapon.Weapon('smol sword', 5, [], 9)
weapon_for_sale2 = Weapon.Weapon('medium sword', 5, [], 9)
weapon_for_sale3 = Weapon.Weapon("'Honestly too big' sword", 5, [], 9)

weapon_list = []
weapon_list.append(weapon_for_sale1)
weapon_list.append(weapon_for_sale2)
weapon_list.append(weapon_for_sale3)

enemy_character = Human_Character.HumanCharacter("Evil Harold", 5, 10, 5, 3, 9)
player_character = Human_Character.HumanCharacter("Harold", 7, 10, 7, 2, 0)

game_status = CHOOSING_PATH

while(game_status != GAME_OVER):
    print('Current Gold: ' + str(player_character.gold))
    choice = input('Enter Battle (b), or Shopping (s)').lower()
    if choice == 'b':
        # Battle
        game_status = IN_BATTLE
        game_status, player_character = battle_station.combat(
            enemy_character, player_character, game_status)
    elif choice == 's':        
        # Shopping
        game_status = SHOPPING
        for (index, weapon) in enumerate(weapon_list):
            print(index+1)
            weapon.display()


displayGrave()