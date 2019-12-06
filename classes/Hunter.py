
#This is the hunter module that inherit from the Ordinary class
#& One of the battle character for player to chooce at the beginning of the game

from classes.Ordinary import Ordinary

class Hunter(Ordinary):

    # Health = 25, Charisma = 10, Strength = 12, Intelligence = 20, Resourcefulness = 25, Faith = 10, Luck = 10
    def __init__(self, name):
        super().__init__(name, 25, 10, 12, 20, 25, 10, 10)
