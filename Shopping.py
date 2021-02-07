from Game_States import SHOPPING
import Item

smol_sword = Item.Item('smol sword', 3, [], 9)
medium_sword = Item.Item('medium sword', 5, [], 9)
htb_sword = Item.Item("'Honestly too big' sword", 9, [], 9)

weapon_list = []
weapon_list.append(smol_sword)
weapon_list.append(medium_sword)
weapon_list.append(htb_sword)


class Shopping:
    # Show Wares
    def shop(self, game_status, player_character):
        while game_status == SHOPPING:
            print('*** Items for sale: ***')
            for (index, weapon) in enumerate(weapon_list):
                print(index+1)
                weapon.display()

            selection = input(
                "What item # would you like to buy? 'n' for no purchase: ")

            new_gold_amount = -1

            if selection.isnumeric():
                item = weapon_list[int(selection)-1]
                new_gold_amount = player_character.gold - item.cost

            if new_gold_amount > -1:
                player_character.gold = new_gold_amount
                print('Purchased!')
                item.display()
                player_character.items.insert(0, item)

            if selection == 'n':
                game_status == 1
                return game_status, player_character
