
#This is the combat arms expert module that inherit from the Ordinary class
#& One of the battle character for player to chooce at the beginning of the game 

from classes.Ordinary import Ordinary

class CombatArmsExpert(Ordinary):

    #Health = 30, Charisma = 9, Strength = 18, Intelligence = 10, Resourcefulness = 15, Faith = 10, Luck = 10
    def __init__(self, name):
        super().__init__(name, 30, 9, 18, 10, 15, 10, 10)
