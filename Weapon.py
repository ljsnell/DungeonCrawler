class Weapon:

    def __init__(self, name, damage, effects, cost):
        self.name = name
        self.damage = damage
        self.effects = effects
        self.cost = cost

    def display(self):
        print('Name: ' + self.name + ', Damage: ' + str(self.damage) +
              ', Effects: [' + str(self.effects).strip('[]') + '], Cost: ' + str(self.cost))
