from constants.Game_States import SHOPPING
import Item
from Item_List import TIER_ONE_ITEMS
from display_utilities.Clear_Screen import clear_display


class Shopping:
    # Show Wares
    def shop(self, game_status, player_character):
        clear_display()
        while game_status == SHOPPING:
            print('*** Items for sale: ***')
            for (index, weapon) in enumerate(TIER_ONE_ITEMS):
                print(index+1)
                weapon.display()

            selection = input(
                "What item # would you like to buy? 'n' for no purchase: ")

            new_gold_amount = -1

            if selection.isnumeric():
                item = TIER_ONE_ITEMS[int(selection)-1]
                new_gold_amount = player_character.gold - item.cost

            if new_gold_amount > -1:
                player_character.gold = new_gold_amount
                print('Purchased!')
                item.display()
                player_character.items.insert(0, item)

            if selection == 'n':
                game_status == 1
                return game_status, player_character
