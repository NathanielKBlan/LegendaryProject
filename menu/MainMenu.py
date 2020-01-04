from menu.Menu import Menu
from tools.input_verification import *
from game.Game import Game

# This is the main menu class.
# This is where the game starts, whether it be a new one or a previous one
# noinspection PyMethodMayBeStatic,PyRedundantParentheses
class MainMenu(Menu):
    optionsList = ["New Game", "Credits", "Exit"]

    def newGame(self):
        newGame = Game(input("What is your name? "))
        newGame.startGame()

    def credits(self):
        print("Unit Tester: Lynn")
        print("Main unit writer: Nathaniel K. Blanquel")
        print("Story writer: Lynn")
        print("Tool developer: Nathaniel K. Blanquel")
        print("Areas developers: Nathaniel K. Blanquel & Lynn")
        print("This has been a CodingBeyond production")

    def exit(self):
        print("Exiting game...")
        quit()

    def getInput(self):
        selectedFunc = self.verifyInput(self.getOptionInput())
        selectedFunc()

    def verifyInput(self, chosenOption):
        return switch(chosenOption, self.optionsList, [self.newGame, self.credits, self.exit])



    # To be called upon initialization
	# Default number of menu options is set at 4
	# Default menu name is set to Main Menu
	# Default options are set to: New Game, Load Game, Credits, and Exit
    def __init__(self):
        super().__init__(3, "Main Menu", self.optionsList)
        self.printMenu(self.menu, self.menuTitle)



