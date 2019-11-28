import sys
sys.path.append("../")
from classes.Ordinary import Ordinary
from classes.Scholar import Scholar

def test():
	a = Scholar("Wryn")

	print(a.getHealth())
	print(a.getCharisma())

	a.addToInventory("Golden armour")

def main():
	test()

main()
