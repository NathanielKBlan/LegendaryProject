
#Unit test for the MainMenu module
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from menu.Menu import Menu
from menu.MainMenu import MainMenu
from tools.input_verification import *
from game.Game import Game

def test():
	#Initialize a MainMenu class
	mainMenu = MainMenu()

	#Test the methods
	mainMenu.newGame()
	mainMenu.loadGame()
	mainMenu.credits()
	mainMenu.exit()
        
def main():
	test()

main()
