import random

import self as self

from areas.Area import Area
from enemies.Pyrodin import Pyrodin
from menu.Menu import Menu
from tools.input_verification import switch


class TheSkiesOfFire(Area):

	def __init__(self, player):
		self.__player = player
		self.printArrival()

	def printArrival(self):
		print("Look around, now, and learn you of the fiery god of the skies of Fire. An omniscient and omnipotent angel wreathed in ever-shrieking flames,")
		print("Pyrodin's blistering talons turn iron into slag, His smoldering horns char the heavens,")
		print("and those who oppose his whimsical temper perish screaming in a hell of primal fire.")
		print("Pyrodin: Wanderer, I saw you dived into the deepest abyss of the sea.")
		print("Pyrodin: And crossed the land between two worlds.")
		print("Pyrodin: The road you have passed was flowed with blood.")
		print("Pyrodin: And now you are stepping into my world of fire.")
		print("You had a strong feeling that there is no way to get back.")
		print("Pyrodin: Come! Son of Lilith, man of Brave. Show me your faith!")
		self.battleWithPyrodin()

	def battleWithPyrodin(self):
		print("-------The Skies Of Fire-------")
		pyrodin = Pyrodin()
		firstStrike = int(random.random() * 1 + 1)

		if (firstStrike == 1):
			print("Quick to your senses you slash Pyrodin with your weapon.")
			pyrodin.lowerHealth(self.__player.attack(pyrodin))
			print("Pyrodin burst out an deafening monstrous roar.")
			print("Your feel your palms are sweating.")

		else:
			print("You attempt to make the first attack but Pyrodin parries it.")
			print("Pyrodin attacks you.")
			self.__player.lowerHealth(Pyrodin.slashAttack())

		while (int(pyrodin.getHealth()) > 0 and int(self.__player.getHealth()) > 0):
			print("Your health: " + str(self.__player.getHealth()))
			print("Pyrodin's health: " + str(pyrodin.getHealth()))
			input("Enter anything to continue")
			pyrodin.lowerHealth(self.__player.attack(pyrodin))
			self.__player.lowerHealth(pyrodin.slashAttack())

		if(int(pyrodin.getHealth() <= 10)):
			print("The Pyrodin was serious injured by you. You are ready to give him the last strike.")
			print("You clenches your weapon tightly. Your body trembles slightly with exitement by the smell of blood.")
			print("The Mermaid's curse before dead suddenly echos in your ears. You think the Pyrodin may be the one who can break the spell.")
			print("You deliver the final blow and see that Pyrodin's servants and noblemen now bow before you.")
			print("One who calls himself Thalus introduces himself to you.")
			print("If you wish to alleviate your curse, you must take his place")
			fate = switch(input("You feel like Killing Pyrodin or Sparing Pyrodin: "), ["Killing Pyrodin", "Sparing Pyrodin"], [self.furyPyrodin, self.endOfStory1])
			fate(pyrodin)

	def furyPyrodin(self, pyrodin):

		print("You strike at Pyrodin fiercely!")
		pyrodin.lowerHealth(self.__player.attack(pyrodin))

		if (int(pyrodin.getHealth()) > 0):
			print("Pyrodin went fury!")
			pyrodin.restoreHealth()

		while (int(pyrodin.getHealth()) > 0 and int(self.__player.getHealth()) > 0):
			print("Your health: " + str(self.__player.getHealth()))
			print("Pyrodin's health: " + str(pyrodin.getHealth()))
			input("Enter anything to continue")
			pyrodin.lowerHealth(self.__player.attack(pyrodin))
			self.__player.lowerHealth(pyrodin.slashAttack())

		if (self.__player.getHealth < 0):
			print("Pyrodin kills you. The world goes dark.")
			self.__player.setExp(self.__player.getExp() + 50)

		else:
			print("You finally killed Pyrodin!")
			self.__player.setExp(self.__player.getExp() + 800)
			self.__player.levelUp()
			print("---------------------------------------------")
			self.endOfStory2()

	def endOfStroy1(self):
		print("Thalus: My lord, bless thine safe journey here. We are here to serve your highness. Our lord hadst returnst")
		print("THE END")

	def endOfStory2(self):
		print("Pyrodin: You fool, you should've killed me when you had the chance.")
		print("Pyrodin: There are far worse things than death")
		print("The curse spreads and you see yourself disfigured into a horrible being beyond comprehension")
		print("THE END")
