import sys
sys.path.append("../")
from classes.Ordinary import Ordinary
from classes.Combat_Arms_Expert import CombatArmsExpert

def test():
	a = CombatArmsExpert() #Test failed at here

	print(a.getHealth())
	print(a.getCharisma())

	a.addToInventory("Golden armour")

def main():
	test()

main()