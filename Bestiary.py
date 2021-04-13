from Item_List import *
from characters import Human_Character
from characters import Bat_Character
from characters import Rat_Character
from characters import Spider_Character
import random


def createEnemyList():
    Evil_Harold = Human_Character.HumanCharacter(
        "Evil Harold", 5, 10, 5, 3, 9, 8, [SMOL_SWORD])

    Bat = Bat_Character.BatCharacter(3)
    Rat = Rat_Character.RatCharacter(3, 5, 1)
    Spider = Spider_Character.SpiderCharacter(2)

    tier_one_enemies = [Bat, Evil_Harold, Rat, Spider]

    return tier_one_enemies


def returnEnemyByTier(pc_level):
    tier_one_enemies = createEnemyList()

    if pc_level == 1:
        return random.choice(tier_one_enemies)
    else:
        return
