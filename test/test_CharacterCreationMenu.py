#This program tests the functionality of the character creation menu module.

import sys

sys.path.append("../")

from menu.Menu import Menu
from menu.CharacterCreationMenu import CharacterCreationMenu
from classes.Ordinary import Ordinary
from classes.Combat_Arms_Expert import CombatArmsExpert
from classes.Hunter import Hunter
from classes.Silver_Tongue import SilverTongue
from tools.input_verification import *

def test():
    a = CharacterCreationMenu('Wryn')

def main():
    test()

main()
