import sys
sys.path.append("../")
from classes.Ordinary import Ordinary
from classes.Hunter import Hunter

def test():
	a = Hunter() #Test failed at here

	print(a.getHealth())
	print(a.getCharisma())

	a.addToInventory("Golden armour")

def main():
	test()

main()
