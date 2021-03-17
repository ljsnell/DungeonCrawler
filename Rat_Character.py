import random


class RatCharacter:
    rat_names = ['Emaciated', "Disease Ridden", "Yellow Toothed"]
    rat_name = random.choice(rat_names)

    def __init__(self, head, chest, tail):
        self.name = self.rat_name + ' Rat'
        self.head = head
        self.chest = chest
        self.tail = tail
        self.exp = 7
        self.damage = 2
        self.gold = 4

    def display(self):
        print('**************************')
        print('NAME: ' + self.name)
        print('   ()---().----.          .')
        print(r'    \h:' + str(self.head) + '/  c:' +
              str(self.chest) + '  ;     t:' + str(self.tail) + '  .')
        print(r'     \ /\ ___  ;________.')
        print(r'      ` ^^   ^^')
        print('**************************')

    def display_defeat(self):
        print('**************************')
        print('NAME: ' + self.name)
        print('   ()---().----.          .')
        print(r'    \h:' + str(self.head) + '/  c:' +
              str(self.chest) + '  ;     t:' + str(self.tail) + '  .')
        print(r'     \ /\ ___  ;________.')
        print(r'      ` ^^   ^^')
        print('**************************')

    def determine_damage(self, hit_location, damage):
        self.chest -= damage

    def is_alive(self):
        if(self.chest > 0):
            return True
        else:
            return False
