import random

from enemies.Enemy import Enemy

class Pyrodin(Enemy):

	def __init__(self):
		super().__init__("Pyrodin, Lord of the Inferno", 60, ["Slash", "Flame Breath", "Radinant Plume", "Hellfire"])

		def attack(self, player, attackNum = int(random.random() * 15 + 1)):
			if (attackNum <= 4):
				self.slashAttack()
			elif (attackNum > 4 and <= 9):
				self.flameBreath(player)
			elif (attackNum > 9 and attackNum <= 13):
				self.radiantPlume(player)
			else:
				self.hellFire(player)

		#The contains of these abilities are tbc.

		def flameBreath(self, player):

		def radiantPlume(self, player):

		def hellFire(self, player):