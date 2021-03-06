import random


class BatCharacter:
    bat_names = ['Hairy', "Bloodsucking", "Sleepy"]
    bat_name = random.choice(bat_names)

    def __init__(self, chest):
        self.name = self.bat_name + ' Bat'
        self.chest = chest
        self.exp = 5
        self.damage = 3
        self.gold = 4

    def display(self):
        print('**************************')
        print('NAME: ' + self.name)
        print(r'   \/( c:' + str(self.chest) + r' )\/')
        print('**************************')

    def display_defeat(self):
        print('**************************')
        print('NAME: ' + self.name)
        print('   /*( c:' + str(self.chest) + ' )*\\')
        print('**************************')

    def determine_damage(self, hit_location, damage):
        self.chest -= damage

    def is_alive(self):
        if(self.chest > 0):
            return True
        else:
            return False
