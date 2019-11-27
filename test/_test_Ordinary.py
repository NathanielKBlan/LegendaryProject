# This module tests the functionality of the ordinary class
import sys
sys.path.append("../")
from classes.Ordinary import Ordinary

def test():
	a = Ordinary()
	
	#Test getters
	print("Health:", a.getHealth())
	print("Charisma:", a.getCharisma())

	#Test setters
	a.setHealth(20)
	print("New health:", a.getHealth())
	a.setCharisma(100)
	print("New charisma:", a.getCharisma())
	a.addToInventory("Golden armour")

def main():
	test()

main()