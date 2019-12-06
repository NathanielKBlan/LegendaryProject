
#This is the Mermaid of Frost class that is inherit from the Enemy class
import random
from enemies.Enemy import Enemy


class MermaidOfFrost(Enemy):
	#Initialize the subclass with three instances
	#This enemy has the ability to modify player's exp point therefore takes expModifier as a parameter
    def __init__(self, expModifier):
        super().__init__("Mermaid of Frost", 20 + (expModifier * 0.025), ["Slash"])

