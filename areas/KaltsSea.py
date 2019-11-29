import random

from areas.Area import Area
from enemies.Enemy import Enemy
from enemies.MermaidOfFrost import MermaidOfFrost
from menu.Menu import Menu
from tools.input_verification import switch


class KaltsSea(Area):

    def __init__(self, player):
        super().__init__("Kalts Sea", "The Depth", None)
        self.__firstTimeAtLightHouse = True
        self.__solomonIsDead = False
        self.__player = player
        self.__printArrival()

    def printArrival(self):
        print("You set out to find the source of those voices and set out to sea on a raft.")
        print("Days of travel have gotten you to a vast empty ocean, however this is no ordinary ocean.")
        print("Here, the water chills you to the bone, the only source of warmth is a nearby light house. ")
        print("You don't mind that, you hear the voice in the water.")
        choice = switch(input("You feel like: "), ["Diving in", "Going to the lighthouse"], self.diveIn, self.proceedToLightHouse())
        choice()

    def diveIn(self):
        print("You dive into the frigid waters and head to what lies beneath.")
        self.battleWithMermaids(self.__player)
        self.proceedToAbyss(self.__player)
        pass

    def proceedToLightHouse(self):
        #Here we need a script for branches as well as a way of telling if branch was taken
        if(not self.__solomonIsDead):
            print("At the light house, a wave of warmth hits your face as you enter.")
            if (self.__firstTimeAtLightHouse):
                print("You are greeted by a young man who calls himself Solomon.")
                print("Solomon: What do we have here? You must be a new arrival, as you have not yet lost hope.")
                print("You seek the lovely voices of the mermaids and eternal warmth, look elsewhere, you won't find that here.")
                print("You must go to the Abyss, there the queen of frost will grant your wished *laughs maniacally*")
                print("You make your way to sea.")
                self.battleWithMermaids(self.__player)
            else:
                print("You feel rage at having been defeated. You feel rage of not being warned about the mermaids of frost.")
                print("The essence of the Land of Ashes is getting to you. You feel rage as you lay your eyes upon Solomon.")
                fateOfSolomon = Menu(2, "Fate of Solomon", ["Killing Solomon", "Sparing Solomon"])
                fate = switch(input("You feel like: "), ["Killing Solomon", "Sparing Solomon"], self.battleWithSolomon, self.battleWithMermaids)
                fate()
        else:
            print("The lighthouse is now dark and cold. There is no use in being here.")
            self.battleWithMermaids()
        pass

    def battleWithMermaids(self):
        print("While searching for the voice, you lose yourself in the abyss of Kalts Sea, and a wave of frost hits you.")
        for i in range(3):
            mermaidOfFrost = MermaidOfFrost(self.__player.getExp())
            firstStrike = int(random.random() * 1 + 1)
            if (firstStrike == 1):
                print("Quick to your senses you slash the mermaid with your weapon")
                mermaidOfFrost.lowerHealth(self.__player.attack())
            else:
                print("The mermaid pierces you")
                self.__player.lowerHealth(mermaidOfFrost.attack())
            while (mermaidOfFrost.getHealth() > 0 and self.__player.getHealth() > 0):
                print("Your health: " + self.__player.getHealth())
                print("Mermaid's health: " + mermaidOfFrost.getHealth())
                input("Enter anything to continue")
                mermaidOfFrost.lowerHealth(self.__player.attack())
                self.__player.lowerHealth(mermaidOfFrost.attack())
            if (self.__player.getHealth < 0):
                print("The mermaid injures you gravely. You go back to the light house.")
                self.__player.setExp(self.__player.getExp() + 50)
                self.proceedToLightHouse()
            else:
                print("You have slain the mermaid, but she was not alone...")
                self.__player.setExp(self.__player.getExp() + 250)
                self.proceedToLightHouse()
        print("Having overcome the mermaids, you delve deeper into Kalts Sea and proceed to the Abyss bellow the sea.")

    def battleWithSolomon(self):
        print("Solomon: Have you gone mad?! Well I'm no push over! Prepare yourself!")
        solomon = Enemy(25, None)
        firstStrike = int(random.random() * 1 + 1)
        if (firstStrike == 1):
            print("Quick to your senses you slash Solomon with your weapon")
            solomon.lowerHealth(self.__player.attack())
        else:
            print("The mermaid pierces you")
            self.__player.lowerHealth(solomon.attack())
        while (solomon.getHealth() > 0 and self.__player.getHealth() > 0):
            print("Your health: " + self.__player.getHealth())
            print("Mermaid's health: " + solomon.getHealth())
            input("Enter anything to continue")
            solomon.lowerHealth(self.__player.attack())
            self.__player.lowerHealth(solomon.attack())
        if (self.__player.getHealth < 0):
            print("Solomon cripples you. You wake up from the trance.")
            self.__player.setExp(self.__player.getExp() + 50)
            self.proceedToLightHouse()
        else:
            print("Solomon's blood stains your blade and hands")
            print("You: My god, what have I done?")
            self.__player.setExp(self.__player.getExp() + 500)
            self.battleWithMermaids()

    def proceedToAbyss(self, player):
        #Implement code here, also end of area, next area is boss area
        pass