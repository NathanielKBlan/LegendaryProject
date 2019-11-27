from menu.Menu import Menu
from tools.input_verification import switch


class BattleMenu(Menu):

    def __init__(self, player, abilities):
        super.__init__(len(abilities), "Combat Menu", abilities)
        self.printMenu(self.menu, self.menuTitle)
        self.__player = player
        self.__abilities = abilities

    def getInput(self):
        selectedFunc = self.verifyInput(self.getOptionInput())
        selectedFunc()

    def verifyInput(self, chosenOption):
        return switch(chosenOption, self.__abilities, self.__player.attack, self.__player.useItem, self.__player.parryAndReposte, self.__player.flee)