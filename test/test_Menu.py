# This program tests the functionality of the menu module

import sys

sys.path.append("../")

from menu.Menu import Menu
from game.Game import Game

def test():
	a = Menu()
	a.printMenu(['New Game', 'Resume', 'Credit', 'Exit'], 'The Song of Ice & Fire')
	a.getOptionInput()

def main():
	test()

main()
