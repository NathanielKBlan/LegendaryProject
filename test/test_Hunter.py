import sys
sys.path.append("../")
from classes.Ordinary import Ordinary
from classes.Hunter import Hunter

def test():
	a = Hunter("Wryn")

	print(a.getHealth())
	print(a.getCharisma())

	a.addToInventory("Golden armour")

def main():
	test()

main()
