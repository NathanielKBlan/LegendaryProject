
#Unit test for the KaltsSea module
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from areas.Area import Area #Import the Area module as parent class
from areas.KaltsSea import KaltsSea #Import the KaltsSea class as subclass for testing
from enemies.MermaidOfFrost import MermaidOfFrost #Import the enemy from the MermaidOfFrost class

def test():
	#Initialize a KaltsSea class
	kaltsSea = KaltsSea("Wryn")

	#Test the accessor methods
	kaltsSea.printArrival()
	kaltsSea.battleWithMermaid("Wryn")

def main():
	test()

main()
