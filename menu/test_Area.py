
#Unit test for the Area module
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from areas.Area import Area #Import the Area module for testing

def test():
	#Initialize an Area class
	area = Area('KaltsSea', 'Lighthouse', 'Cottage By the Beach', 'Sea Witch')
	print(area.getAreaName()) #Test the accessor method 

def main():
	test()
	
main()