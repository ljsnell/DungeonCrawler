import Human_Character
import Battle
import Item
import Shopping
from Game_States import GAME_OVER, CHOOSING_PATH, IN_BATTLE, SHOPPING
from GraveStone import displayGrave

shopping_station = Shopping.Shopping()
battle_station = Battle.Battle()
smol_sword = Item.Item('smol sword', 3, [], 9)
medium_sword = Item.Item('medium sword', 5, [], 9)
htb_sword = Item.Item("'Honestly too big' sword", 9, [], 9)

enemy_character = Human_Character.HumanCharacter(
    "Evil Harold", 5, 10, 5, 3, 9, [smol_sword])
player_character = Human_Character.HumanCharacter(
    "Harold", 7, 10, 7, 2, 11, [medium_sword])

game_status = CHOOSING_PATH

while(game_status != GAME_OVER):
    print('Current Gold: ' + str(player_character.gold))
    choice = input(
        'Enter Battle (b), Shopping (s), or Inventory (i): ').lower()
    if choice == 'b':
        # Battle
        game_status = IN_BATTLE
        game_status, player_character = battle_station.combat(
            enemy_character, player_character, game_status)
    elif choice == 's':
        # Shopping
        game_status = SHOPPING
        game_status, player_character = shopping_station.shop(
            game_status, player_character)
    elif choice == 'i':
        # Inventory
        print('Current inventory: ')
        for item in player_character.items:
            item.display()

displayGrave()
