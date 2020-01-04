
#Unit test for the Ordinary class
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from classes.Ordinary import Ordinary

def test():
	#Initialize an Oridinary class
	oridinary = Ordinary()
	
	#Test getters
	print("Health:", oridinary.getHealth())
	print("Charisma:", oridinary.getCharisma())

	#Test setters
	oridinary.setHealth(20)
	print("New health:", oridinary.getHealth())

	oridinary.setCharisma(100)
	print("New charisma:", oridinary.getCharisma())
	
	oridinary.takeDamage(20)
	print(oridinary.getHealth())
	
	print(oridinary.getStrength())
	oridinary.attack("Pikachu")

def main():
	test()

main()
