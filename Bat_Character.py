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
        print('   v^( c:' + str(self.chest) + ' )^v' )

    # def display_defeat(self):