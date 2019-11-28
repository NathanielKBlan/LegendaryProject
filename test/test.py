#This is the main module that will be used for QA testing of the game.
#I will add further methods for QA testing to this module
import sys

#Required in order to properly import modules from other folders in the project
sys.path.append("../")

from menu.Menu import Menu
from menu.MainMenu import MainMenu

#This method is for testing functionality of the various menu objects
def generateMenu():
    menu = MainMenu()
    return None

#Testing method, change when you wish to test certain aspects of game
def test():
    MainMenu.input = lambda: 'New Game'
    generateMenu()

#Main method of the QA testing module
def main():
    test()

main()
