from classes.Scholar import Scholar
from classes.Warrior import Warrior
from menu.Menu import Menu
from classes.Ordinary import Ordinary
from classes.Combat_Arms_Expert import CombatArmsExpert
from classes.Hunter import Hunter
from classes.Silver_Tongue import SilverTongue
from tools.input_verification import *

class CharacterCreationMenu(Menu):

    def __init__(self, name):
        self.optionsList = ["Ordinary", "Combat Arms Expert", "Hunter", "Silver Tongue", "Scholar", "Warrior"]
        super().__init__(6, "Character Creation Menu", self.optionsList)
        self.printIntroductionToStory()
        self.printMenu(self.menu, self.menuTitle)
        self.__player = self.chooseClass(name)



    def printIntroductionToStory(self):
        print("You are one of the last remaining humans in this now desolate and dark world")
        print("There is a story that when night falls, on the edge of the beaches, one can hear the lovely calls from")
        print("the various mermaids of frost that reside there, wishing to attract those who listen into the sea. You hear the voice")
        print("and craving love you wander out to the sea bellow zero, as some call it: Kalts Sea. Hoping that within the cold, you may find")
        print("companionship. Knowing full well that what ever stands in your way will be defeated as you are a: ")

    def chooseClass(self, name):
        chosenOption = input("Choose your character class: ")
        return switch(chosenOption, self.optionsList, [Ordinary(name), CombatArmsExpert(name), Hunter(name), SilverTongue(name), Scholar(name), Warrior(name)])

    def getPlayer(self):
        return self.__player