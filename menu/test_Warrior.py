
#Unit test for the Warrior class
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from classes.Ordinary import Ordinary #Import the Ordinary class as the parent class
from classes.Warrior import Warrior #Import the Warrior class as subclass for testing

def test():
	#Initialize a Warrior class for testing
	warrior = Warrior("Wryn")

	#Test the accessor methods
	print(warrior.getHealth())
	print(warrior.getCharisma())

def main():
	test()

main()
