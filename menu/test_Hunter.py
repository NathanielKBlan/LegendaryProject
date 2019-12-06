
#Unit test for the Hunter module
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from classes.Ordinary import Ordinary #Import the Ordinary class as the parent class
from classes.Hunter import Hunter #Import the Hunter class for testing

def test():
	#Initialize a Hunter class
	hunter = Hunter("Wryn")

	#Test the accessor methods
	print(hunter.getHealth())
	print(hunter.getCharisma())

def main():
	test()

main()
