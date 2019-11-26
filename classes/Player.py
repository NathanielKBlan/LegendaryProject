from classes.Ordinary import Ordinary
from classes.Combat_Arms_Expert import CombatArmsExpert
from classes.Hunter import Hunter
from classes.Silver_Tongue import SilverTongue
from tools.input_verification import *

from menu.CharacterCreationMenu import CharacterCreationMenu

def getCharacterClass():
    charCreationMenu = CharacterCreationMenu()
    characterClass = charCreationMenu.chooseClass()
    return characterClass

class Player(getCharacterClass()):

    def __init__(self):
        self.__playerClass = type

    def getClass(self):
        return self.__playerClass
