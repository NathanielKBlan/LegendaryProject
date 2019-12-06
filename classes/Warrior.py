from classes.Ordinary import Ordinary

class Warrior(Ordinary):

    # Health = 30, Charisma = 15, Strength = 25, Intelligence = 10, Resourcefulness = 10, Faith = 10, Luck = 10
    def __init__(self, name):
        super().__init__(name, 30, 15, 25, 10, 10, 10, 10)
