# This program tests the functionality of the main menu module

import sys

sys.path.append("../")

from menu.Menu import Menu
from menu.MainMenu import MainMenu
from tools.input_verification import *
from game.Game import Game

def test():
	a = MainMenu()
	a.newGame() #failed to verify user's input correctly
	a.loadGame()
	a.credits()
	a.exit()
        
def main():
	test()

main()
