import sys
sys.path.append("../")
from classes.Ordinary import Ordinary
from classes.Warrior import Warrior

def test():
	a = Warrior("Wryn")

	print(a.getHealth())
	print(a.getCharisma())

	a.addToInventory("Golden armour")

def main():
	test()

main()
