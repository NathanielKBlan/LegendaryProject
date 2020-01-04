
#This is the scholar module that inherit from the Ordinary class
#& One of the battle character for player to chooce at the beginning of the game

from classes.Ordinary import Ordinary

class Scholar(Ordinary):

    # Health = 15, Charisma = 9, Strength = 15, Intelligence = 30, Resourcefulness = 25, Faith = 25, Luck = 10
    def __init__(self, name):
        super().__init__(name, 15, 9, 15, 30, 25, 25, 10)

