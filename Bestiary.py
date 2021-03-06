from Item_List import *
import Human_Character
import Bat_Character
import random


def createEnemyList():
    Evil_Harold = Human_Character.HumanCharacter(
        "Evil Harold", 5, 10, 5, 3, 9, 8, [SMOL_SWORD])

    Bat = Bat_Character.BatCharacter(3)

    tier_one_enemies = [Bat, Evil_Harold]
    return tier_one_enemies


def returnEnemyByTier(pc_level):
    tier_one_enemies = createEnemyList()

    if pc_level == 1:
        return random.choice(tier_one_enemies)
    else:
        return
