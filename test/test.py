#This is the main module that will be used for QA testing of the game.
#I will add further methods for QA testing to this module
import sys

#Required in order to properly import modules from other folders in the project
sys.path.append("../")

from menu.Menu import Menu

#This method is for testing functionality of the various menu objects
def testMenu(options, title):
    menu = Menu(options, title)
    menu.printMenu(menu.menu, menu.menuTitle)
    return None

#Main method of the QA testing module
def main():
    testMenu(12, "NEW MENU")

main()
