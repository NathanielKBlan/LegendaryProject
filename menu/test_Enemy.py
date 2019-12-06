
#Unit test for the Enemy module
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from enemies.Enemy import Enemy #Import the Enemy module for testing

def test():
	#Initialize an Enemy class
    enemy = enemy("Pikachu", 10, "Thunderbolt")

    #Test the accessor methods
    print(enemy.getHealth())
    print(enemy.getAbilities())

def main():
    test()

main()
