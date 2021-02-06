import Human_Character
import Battle
import Item
from Game_States import GAME_OVER, CHOOSING_PATH, IN_BATTLE, SHOPPING
from GraveStone import displayGrave

battle_station = Battle.Battle()
weapon_for_sale1 = Item.Item('smol sword', 5, [], 9)
weapon_for_sale2 = Item.Item('medium sword', 5, [], 9)
weapon_for_sale3 = Item.Item("'Honestly too big' sword", 5, [], 9)

weapon_list = []
weapon_list.append(weapon_for_sale1)
weapon_list.append(weapon_for_sale2)
weapon_list.append(weapon_for_sale3)

enemy_character = Human_Character.HumanCharacter("Evil Harold", 5, 10, 5, 3, 9)
player_character = Human_Character.HumanCharacter("Harold", 7, 10, 7, 2, 11)

game_status = CHOOSING_PATH

while(game_status != GAME_OVER):
    print('Current Gold: ' + str(player_character.gold))
    choice = input('Enter Battle (b), or Shopping (s): ').lower()
    if choice == 'b':
        # Battle
        game_status = IN_BATTLE
        game_status, player_character = battle_station.combat(
            enemy_character, player_character, game_status)
    elif choice == 's':
        # Shopping
        game_status = SHOPPING

        # Show Wares
        for (index, weapon) in enumerate(weapon_list):
            print(index+1)
            weapon.display()

        selection = input(
            "What item # would you like to buy? 'n' for no purchase: ")

        item = weapon_list[int(selection)-1]
        new_gold_amount = player_character.gold - item.cost

        if selection.isnumeric and new_gold_amount > -1:
            player_character.gold = new_gold_amount
            print('Purchased!')
            item.display()

displayGrave()
