import random
from characters.Effects import SLOW


class SpiderCharacter:
    spider_names = ['Baleful', "Steeple-Legged", "Glistening"]
    spider_name = random.choice(spider_names)

    def __init__(self, chest):
        self.name = self.spider_name + ' Spider'
        self.chest = chest
        self.exp = 5
        self.damage = 3
        self.damaging_effects = [SLOW]
        self.gold = 4

    def display(self):
        print('**************************')
        print('NAME: ' + self.name)
        print(r'   /\(0 c:' + str(self.chest) + ' 0)/\\')
        print('**************************')

    def display_defeat(self):
        print('**************************')
        print('NAME: ' + self.name)
        print('   __/(0 c:' + str(self.chest) + ' 0)\\__')
        print('**************************')

    def determine_damage(self, hit_location, damage):
        self.chest -= damage

    def is_alive(self):
        if(self.chest > 0):
            return True
        else:
            return False
