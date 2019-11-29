import sys
sys.path.append("../")

from tools.input_verification import *

def test():
	print(switch('1','1','Warrior'))
	print(switch('1','3','Warrior'))

def main():
	test()

main()
