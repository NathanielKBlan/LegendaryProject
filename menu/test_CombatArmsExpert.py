
#Unit test for the CombatArmsExpert module
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from classes.Ordinary import Ordinary #Import the Ordinary class as the parent class
from classes.Combat_Arms_Expert import CombatArmsExpert #Import the CombatArmsExpert class for testing

def test():
	#Initialize a CombatArmsExpert class
	combatArmsExpert = CombatArmsExpert("Wryn")

	#Test the accessor methods
	print(combatArmsExpert.getHealth())
	print(combatArmsExpert.getCharisma())

def main():
	test()

main()
