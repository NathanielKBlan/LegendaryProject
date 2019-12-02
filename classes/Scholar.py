from classes.Ordinary import Ordinary

class Scholar(Ordinary):

    # Health = 15, Charisma = 9, Strength = 15, Intelligence = 30, Resourcefulness = 25, Faith = 25, Luck = 10
    def __init__(self, name):
        super().__init__(name, 15, 9, 15, 30, 25, 25, 10)
        self.__inventory = ["Tetrabiblos", "Mortarboard", "Silver Spectacles", "Blessed Gown", "Culottes", "Ring of Divine Wisdom", "Ring of Divine War"]

