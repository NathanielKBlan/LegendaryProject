
#This module calls the main menu of the game and get the player's input of name, character choices
#This is where the game "Land of Ashes" first starts

from menu.MainMenu import MainMenu

def main():
    mainMenu = MainMenu()
    mainMenu.getInput()

main()