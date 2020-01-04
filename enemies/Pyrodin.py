
#This is the Pyrodin class that is inherit from the Enemy class
import random
from enemies.Enemy import Enemy

class Pyrodin(Enemy):

	def __init__(self):
		super().__init__("Pyrodin, Lord of the Inferno", 60, ["Slash", "Radinant Plume", "Hell Flame"])

		def attack(self, player, attackNum = int(random.random() * 9 + 1)):
			if (attackNum <= 5):
				self.slashAttack()
			elif (attackNum > 5 and attackNum <= 7):
				self.radiantPlume(player)
			else:
				self.hellFlame(player)

		def radiantPlume(self, player):
			print("Pyrodin brandished his wand, numerous plume strewn over the sky.")
			print("You are entangled in the glory plume of flame. You feel soft and weak.")
			player.setStrength(player.getStrength() - player.getStrength() * 0.1)

		#def hellFlame(self, player):
			#print("Pyrodin: In the name of the eighteenth hell and the God of the Ever-lasting Flame. Me, Pyrodin, Lord of the Inferno, grant you the death!")
			#The contains of this skill is tbc.