
#Unit test for the CharacterCreationMenu module
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from menu.Menu import Menu #Import the Menu module as the parent class
from menu.CharacterCreationMenu import CharacterCreationMenu #Import the CharacterCreation class for testing

def test():
	#Initialize a CharacterCreationMenu class
    characterMenu = CharacterCreationMenu('Wryn')

def main():
    test()

main()