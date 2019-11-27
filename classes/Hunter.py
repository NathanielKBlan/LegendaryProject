from classes.Ordinary import Ordinary

class Hunter(Ordinary):

    # Health = 25, Charisma = 10, Strength = 12, Intelligence = 20, Resourcefulness = 25, Faith = 10, Luck = 10
    def __init__(self, name):
        super().__init__(25, 10, 12, 20, 25, 10, 10, name)
        self.__inventory = ["Dagger", "Poison", "Binoculars", "Healing Flask", "Longbow", "Leather Armor", "Quiver (20 Arrows)"]

