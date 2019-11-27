from classes.Ordinary import Ordinary

class CombatArmsExpert(Ordinary):

    #Health = 30, Charisma = 9, Strength = 18, Intelligence = 10, Resourcefulness = 15, Faith = 10, Luck = 10
    def __init__(self, name):
        super().__init__(30, 9, 18, 10, 15, 10, 10, name)
        self.__inventory = ["Broadsword", "Poison", "Acid", "Bomb", "Crossbow", "Plated Armor", "Shield of Valor"]
    

