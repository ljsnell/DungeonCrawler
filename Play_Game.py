from characters import Human_Character
import Battle
import Item
import Shopping
from Game_States import GAME_OVER, CHOOSING_PATH, IN_BATTLE, SHOPPING
from GraveStone import displayGrave
from Bestiary import returnEnemyByTier
import pickle

shopping_station = Shopping.Shopping()
battle_station = Battle.Battle()
smol_sword = Item.Item('smol sword', 3, [], 9)
medium_sword = Item.Item('medium sword', 5, [], 9)
htb_sword = Item.Item("'Honestly too big' sword", 9, [], 9)

player_name = input('Enter Character Name: ')

player_character = Human_Character.HumanCharacter(
    player_name, 7, 10, 7, 2, 11, 0, [medium_sword])

game_status = CHOOSING_PATH

while(game_status != GAME_OVER):
    print('Current Gold: ' + str(player_character.gold))
    print('Current Exp: ' + str(player_character.exp))
    choice = input(
        'Enter Battle (b), Shopping (s), Save (sg), Load (lg) or Inventory (i): ').lower()
    if choice == 'b':
        # Battle
        game_status = IN_BATTLE
        # returnEnemyByTier
        enemy_character = returnEnemyByTier(1)
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
    elif choice == 'sg':
        # Save Game
        # Pickle player character
        with open(player_character.name + '.pkl', 'wb') as output:
            pickle.dump(player_character, output, pickle.HIGHEST_PROTOCOL)
        print('Game saved successfully!')
    elif choice == 'lg':
        # Load Game
        with open(player_character.name + '.pkl', 'rb') as player_pickle:
            player_character = pickle.load(player_pickle)
            print(player_character.name)

displayGrave()
