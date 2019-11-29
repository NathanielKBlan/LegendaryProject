import random

from areas.Area import Area
from enemies.MermaidOfFrost import MermaidOfFrost


class KaltsSea(Area):

    def __init__(self, player):
        super().__init__("Kalts Sea", "The Depth", None, None)
        self.__player = player

    def printArrival(self):
        print("You set out to find the source of those voices and set out to sea on a raft.")
        print("Days of travel have gotten you to a vast empty ocean, however this is no ordinary ocean.")
        print("Here, the water chills you to the bone, the only source of warmth is a nearby light house. ")
        print("You don't mind that, you hear the voice in the water.")

    def diveIn(self):
        print("You dive into the frigid waters and head to what lies beneath.")
        pass

    def proceedToLighHouse(self):
        #Here we need a script for branches as well as a way of telling if branch was taken
        pass

    def battleWithMermaid(self, player):
        print("While searching for the voice, you lose yourself in the abyss of Kalts Sea, and a wave of frost hits you.")
        mermaidOfFrost = MermaidOfFrost(player.getExp())
        firstStrike = int(random.random() * 1 + 1)
        if (firstStrike == 1):
            print("Quick to your senses you slash the mermaid with your weapon")
            mermaidOfFrost.lowerHealth(player.attack())
        else:
            print("The mermaid pierces you")
            player.lowerHealth(mermaidOfFrost.attack())
        while(mermaidOfFrost.getHealth() > 0 and player.getHealth() > 0):
            print("Your health: " + player.getHealth())
            print("Mermaid's health: " + mermaidOfFrost.getHealth())

