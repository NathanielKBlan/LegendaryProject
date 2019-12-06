
#Unit test for the SilverTongue class
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from classes.Ordinary import Ordinary #Import the Ordinary class as the parent class
from classes.Silver_Tongue import SilverTongue #Import the SilverTongue class as subclass for testing

def test():
	#Initialize a SilverTongue class
	silverTongue = SilverTongue("Wryn")

	#Test the accessor methods
	print(silverTongue.getHealth())
	print(silverTongue.getCharisma())

def main():
	test()

main()
