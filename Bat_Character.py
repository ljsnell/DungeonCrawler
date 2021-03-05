import random


class BatCharacter:
    bat_names = ['Hairy', "Bloodsucking", "Sleepy"]
    bat_name = random.choice(bat_names)

    def __init__(self, chest):
        self.name = self.bat_name + ' Bat'
        self.chest = chest

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
