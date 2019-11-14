from menu.Menu import Menu
from tools.input_verification import *

#This is the main menu class.
#This is where the game starts, wether it be a new one or a previous one
class MainMenu(Menu):

	optionsList = ["New Game", "Load Game", "Credits","Exit"]

	def verifyInput(self, chosenOption):
		switch(chosenOption, self.optionsList, self.newGame(), self.loadGame(), self.credits(), self.exit())

	def newGame(self):
		print("New game started")

	def loadGame(self):
		print("Game loaded")

	def credits(self):
		print("The credits go here")

	def exit(self):
		print("This should be a one liner here")

    #To be called upon initialization
    #Default number of menu options is set at 4
    #Default menu name is set to Main Menu
    #Default options are set to: New Game, Load Game, Credits, and Exit
	def __init__(self):
		super().__init__(4, "Main Menu", self.optionsList)

		while(True):
			self.printMenu(self.menu, self.menuTitle)
			self.verifyInput(self.getOptionInput())



