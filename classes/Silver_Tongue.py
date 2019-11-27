from classes.Ordinary import Ordinary

class SilverTongue(Ordinary):

    # Health = 20, Charisma = 20, Strength = 10, Intelligence = 15, Resourcefulness = 15, Faith = 10, Luck = 10
    def __init__(self, name):
        super().__init__(20, 20, 10, 15, 15, 10, 10, name)
        self.__inventory = ["Dagger", "Vial of Ricin", "Book of Lies", "Forbidden Word (2 uses only)", "Eyeglass of malicious intent", "Ragged Business Suit"]

