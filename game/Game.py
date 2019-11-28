from areas.KaltsSea import KaltsSea
from menu.CharacterCreationMenu import CharacterCreationMenu

class Game:

    def __init__(self, playerName):
        self.__saveDirectory = "Set save directory here"
        self.__playerName = playerName

    def startGame(self):
        # Write implementation for code here
        self.__printPrologue()
        characterCreationMenu = CharacterCreationMenu(self.__playerName)
        self.__player = characterCreationMenu.getCharacterClass()
        self.__player.setName(self.__playerName)
        print(self.__player.getName() + " the " + self.__player.__class__.__name__ + ", welcome to the Land of Ashes")
        firstZone = KaltsSea(self.__player)
        pass

    def __printPrologue(self):
        print("---------Prologue----------")
        print("Centuries ago, humanity ruled the world. Lives were prosperous and everlasting.")
        print("Then from the abyss they came, the ancient rulers of the world awoke from their slumber.")
        print("The lord of flames, Pyrodin and his scorching knights.")
        print("The lord of combat, Sill and his faithful companions.")
        print("And the queen of the sea, Merider and her mermaids of frost")
        print("They waged war against the humans")
        print("Pyrodin rained hell upon Earth from the skies he ruled and destroyed human strongholds.")
        print("Sill, hunted them down till only few remained.")
        print("Merider unleashed a series of tidal waves that destroyed remaining hope.")
        print("And Erthel, betrayed the last that remained, and humanity was no more.")
        print("Or so they thought...")

    def getPlayerName(self):
        return self.__playerName

