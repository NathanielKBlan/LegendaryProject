class Game:

    def __init__(self, gameName, playerName):
        self.__gameName = gameName
        self.__saveDirectory = "Set save directory here"
        self.__playerName = playerName

    def startGame(self):
        # Write implementation for code here
        self.printPrologue()
        pass

    def printPrologue(self):
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

