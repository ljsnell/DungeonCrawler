from constants.Game_States import DELIMITER
import random


class HumanCharacter:

    def __init__(self, name, left_arm, chest, right_arm, damage, gold, exp, items=[]):
        self.name = name
        self.r_arm = right_arm
        self.chest = chest
        self.l_arm = left_arm
        self.damage = damage
        self.gold = gold
        self.items = items
        self.exp = exp
        self.level = 1
        self.status_effects = []

    def determine_damage(self, hit_location, damage, effects=[]):
        if hit_location == 'ra':
            self.r_arm_hit(damage)
        elif hit_location == 'c':
            self.c_hit(damage)
        elif hit_location == 'la':
            self.l_arm_hit(damage)

        # Determine if status effect is applied
        if len(effects) > 0:
            for effect in effects:
                if (effect.hit_percent > random.randint(1, 100))\
                        and (effect not in self.status_effects):
                    self.status_effects.append(effect)

    def r_arm_hit(self, damage):
        self.r_arm -= damage

    def c_hit(self, damage):
        self.chest -= damage

    def l_arm_hit(self, damage):
        self.l_arm -= damage

    def is_alive(self):
        lowest_hp_value = sorted([self.l_arm, self.chest, self.r_arm])[0]
        if(lowest_hp_value > 0):
            return True
        else:
            return False

    def display(self):
        print(DELIMITER)
        print('NAME: ' + self.name)
        print('   ________ { O  O } ________')
        print('  / la: ' + f"{self.l_arm:02d}" + '/|  c:' +
              f"{self.chest:02d}" + '  |\\ ra: ' + f"{self.r_arm:02d}" + '\\')
        print(' /       / |        | \\       \\')
        print('Status Effects: ' + str(self.status_effects))
        print(DELIMITER)

    def display_defeat(self):
        print(DELIMITER)
        print('NAME: ' + self.name)
        print(r'   ____\ x  x \____')
        print('  / ' + f"{self.l_arm:02d}" + '/|  ' +
              f"{self.chest:02d}" + '  |\\ ' + f"{self.r_arm:02d}" + '\\')
        print(' /   / |      | \\   \\')
        print(DELIMITER)
