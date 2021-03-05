from Item_List import *
import Human_Character
import Bat_Character
import random

Evil_Harold = Human_Character.HumanCharacter(
    "Evil Harold", 5, 10, 5, 3, 9, [SMOL_SWORD])

Bat = Bat_Character.BatCharacter(3)

TIER_ONE_ENEMIES = [Bat, Evil_Harold]


def returnEnemyByTier(pc_level):
    if pc_level == 1:
        return random.choice(TIER_ONE_ENEMIES)
    else:
        return
