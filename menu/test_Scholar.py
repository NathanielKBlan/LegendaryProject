
#Unit test for the Scholar class

import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from classes.Ordinary import Ordinary #Import the Ordinary class as the parent class
from classes.Scholar import Scholar #Import the Scholar class as subclass for testing

def test():
	#Initialize a Scholar class
	scholar = Scholar("Wryn")

	#Test the accessor methods
	print(scholar.getHealth())
	print(scholar.getCharisma())

def main():
	test()

main()
