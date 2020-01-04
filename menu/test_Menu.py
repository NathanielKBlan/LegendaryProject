
#Unit test for the Menu module
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from menu.Menu import Menu
from game.Game import Game

def test():
	#Initialize a Menu class
	manu = Menu()
	
	#Test the accessor methods
	mane.printMenu(['New Game', 'Resume', 'Credit', 'Exit'], 'The Song of Ice & Fire')
	mane.getOptionInput()

def main():
	test()

main()