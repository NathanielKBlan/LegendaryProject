
#Unit test for the input_verification module
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from tools.input_verification import * #Import the module for testing

def test():
	print(switch('1','1','Warrior'))
	print(switch('1','3','Warrior'))

def main():
	test()

main()
