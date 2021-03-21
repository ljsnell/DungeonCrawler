import sys
import os
dir_path = os.path.dirname(os.path.normpath(__file__))
sys.path.append(os.path.dirname(dir_path))
from characters import Rat_Character


batChar = Rat_Character.RatCharacter(4, 5, 1)

batChar.display()
batChar.display_defeat()
