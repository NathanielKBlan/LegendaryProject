
#This is the first area of the game where the story begins, Kalt Sea.

import random

from areas.Area import Area #Import the Area module as the parent class
from areas.LandBetweenWorlds import LandBetweenWorlds #Import the module in which the story continues to the next area
from enemies.Enemy import Enemy #Import the Enemy module as the parent class for two enemy classes of this area
from enemies.Merider import Merider
from enemies.MermaidOfFrost import MermaidOfFrost
from menu.Menu import Menu
from tools.input_verification import switch #Import the switch method

class KaltsSea(Area):
    #This is the subclass inherit from the Area class
    #Which takes eight methods of events: printArrival, diveIn, proceedToLightHouse, battleWithMermaids, battleWithSolomon, proceedToAbyss
    #useFact, fightHeadOn
    
    #This is the constructor method that takes one instance variable, player
    def __init__(self, player):
        self.__firstTimeAtLightHouse = True
        self.__player = player
        self.__solomonIsDead = False
        self.printArrival() #Prints out the arrival story to the terminal
        super().__init__("Kalts Sea", "The Depth", None, [MermaidOfFrost(player.getExp())])  #Call the Area module w/ instance variables that are meaningful to this area

    def printArrival(self):
        print("----------The Land of Ashes----------")
        print("You set out to find the source of those voices and set out to sea on a raft.")
        print("Days of travel have gotten you to a vast empty ocean, however this is no ordinary ocean.")
        print("Here, the water chills you to the bone, the only source of warmth is a nearby light house. ")
        print("You don't mind that, you hear the voice in the water.")
        #Use the switch method to get the choice from player then call upon the corresponding function
        choice = switch(input("Do you feel like diving in, or going to the lighthouse? "), ["Diving in", "Going to the lighthouse"], [self.diveIn, self.proceedToLightHouse])
        choice()

    def diveIn(self):
        print("You dive into the frigid waters and head to what lies beneath.")
        self.battleWithMermaids(self.__player) #Call the battle function
        self.proceedToAbyss(self.__player) #Heading to the next area after battled with the enemies

    def proceedToLightHouse(self):
        if(not self.__solomonIsDead):
            print("---------LIGHTHOUSE---------")
            print("At the light house, a wave of warmth hits your face as you enter.")

            if (self.__firstTimeAtLightHouse):
                print("You are greeted by a young man who calls himself Solomon.")
                print("Solomon: What do we have here? You must be a new arrival, as you have not yet lost hope.")
                print("You seek the lovely voices of the mermaids and eternal warmth, look elsewhere, you won't find that here.")
                print("You must go to the Abyss, there the queen of frost will grant your wished *laughs maniacally*")
                print("You make your way to sea.")
                print("----------------------------") 
                self.battleWithMermaids(self.__player)
                self.__firstTimeAtLightHouse = False

            else:
                print("You feel rage at having been defeated. You feel rage of not being warned about the mermaids of frost.")
                print("The essence of the Land of Ashes is getting to you. You feel rage as you lay your eyes upon Solomon.")
                #Generate the menu of choice and print it out to the terminal
                fateOfSolomon = Menu(2, "Fate of Solomon", ["Killing Solomon", "Sparing Solomon"])
                #Use the switch method to get the choice from player then call upon the corresponding function
                fate = switch(input("You feel like: "), ["Killing Solomon", "Sparing Solomon"], [self.battleWithSolomon, self.battleWithMermaids])
                fate()

        else:
            print("---------LIGHTHOUSE---------")
            print("The lighthouse is now dark and cold. There is no use in being here.")
            print("----------------------------")
            self.battleWithMermaids()


    def battleWithMermaids(self, player):
        #This function generates the battle w/ the first enemy, Mermaids of Frost
        print("-------Kalts Sea-------")
        print("While searching for the voice, you lose yourself in the abyss of Kalts Sea, and a wave of frost hits you.")

        #The number of the enemies is three therefore the battle is looped for three times
        for i in range(3):

            mermaidOfFrost = MermaidOfFrost(self.__player.getExp())
            firstStrike = int(random.random() * 5 + 1)

            if (firstStrike == 1 or firstStrike == 3):
                print("Quick to your senses you slash the mermaid with your weapon")
                mermaidOfFrost.lowerHealth(self.__player.attack(mermaidOfFrost))

            else:
                print("The mermaid pierces you")
                self.__player.lowerHealth(mermaidOfFrost.slashAttack())

            while(int(mermaidOfFrost.getHealth()) > 0 and int(self.__player.getHealth() > 0)):
                print("Your health: " + str(self.__player.getHealth()))
                print("Mermaid's health: " + str(mermaidOfFrost.getHealth()))
                input("Enter anything to continue")
                mermaidOfFrost.lowerHealth(self.__player.attack(mermaidOfFrost))
                self.__player.lowerHealth(mermaidOfFrost.slashAttack())

            if (self.__player.getHealth() <= 0):
                print("The mermaid injures you gravely. You go back to the light house.")
                self.__player.setExp(self.__player.getExp() + 50)
                break

            else:
                print("You have slain the mermaid, but she was not alone...")
                self.__player.setExp(self.__player.getExp() + 250)
                self.__player.restoreHealth()

        if(self.__player.getHealth() <= 0):
            self.__player.restoreHealth()
            self.proceedToLightHouse()

        else:
            print("Having overcome the mermaids, you delve deeper into Kalts Sea and proceed to the Abyss bellow the sea.")
            self.__player.levelUp()
            print("-----------------------")
            self.proceedToAbyss(player)

    def battleWithSolomon(self):
        #This function generates the battle w/ the second enemy, Solomon
        print("Solomon: Have you gone mad?! Well I'm no push over! Prepare yourself!")

        solomon = Enemy(25, None)
        firstStrike = int(random.random() * 1 + 1)

        if (firstStrike == 1):
            print("Quick to your senses you slash Solomon with your weapon")
            solomon.lowerHealth(self.__player.attack(solomon))

        else:
            print("You attempt to make the first attack but Solomon parries it.")
            print("Solomon cuts you")
            self.__player.lowerHealth(solomon.slashAttack())

        while (int(solomon.getHealth()) > 0 and int(self.__player.getHealth()) > 0):
            print("Your health: " + str(self.__player.getHealth()))
            print("Solomon's health: " + str(solomon.getHealth()))
            input("Enter anything to continue")
            solomon.lowerHealth(self.__player.attack(solomon))
            self.__player.lowerHealth(solomon.slashAttack())

        if (self.__player.getHealth < 0):
            print("Solomon cripples you. You wake up from the trance.")
            self.__player.setExp(self.__player.getExp() + 50)
            self.proceedToLightHouse()

        else:
            print("Solomon's blood stains your blade and hands")
            print("You: My god, what have I done?")
            self.__solomonIsDead = True
            self.__player.setExp(self.__player.getExp() + 500)
            self.proceedToLightHouse()

    def proceedToAbyss(self, player):
        #This function generates the battle w/ the third enemy of this area, Merider
        merider = Merider()

        print("------The Abyss------")
        print("At the abyss, you find the source of the voice.")
        print("Merider: If it isn't a human, I haven't had a human to eat in quite a while now, I prefer them chilled.")
        print("You struggle to pull yourself from the trance and in doing so")
        print("you notice, that the Queen of Frost is blind, when she faces the wrong direction. You have two options, fight head on")
        print("Or use this fact to your advantage")
        choice = switch(input("Do you feel like using fact, or fighting head on? "), ["Using fact", "Fighting head on"], [self.useFact, self.fightHeadOn])
        choice(player, merider)


        firstStrike = int(random.random() * 1 + 1)

        if (firstStrike == 1):
            print("Quick to your senses you slash Merider with your weapon")
            merider.lowerHealth(self.__player.attack(merider))

        else:
            print("You attempt to make the first attack but Merider parries it.")
            print("Merider stabs you")
            self.__player.lowerHealth(merider.slashAttack())

        while (int(merider.getHealth()) > 0 and int(self.__player.getHealth()) > 0):
            print("Your health: " + str(self.__player.getHealth()))
            print("Mermaid's health: " + str(merider.getHealth()))
            input("Enter anything to continue")
            merider.lowerHealth(self.__player.attack(merider))
            self.__player.lowerHealth(merider.slashAttack())

        if (self.__player.getHealth() <= 0):
            print("The merider injures you gravely. You go back to the light house.")
            self.__player.setExp(self.__player.getExp() + 50)
            self.proceedToLightHouse()

        else:
            print("With a final breath Merider curses you, the only way that you know to remove a curse is to head to the skies")
            print("Of fire. The journey is a perilous one, but if the curse isn't alleviated you will die.")
            print("Welcome to the Land of Ashes!")
            self.__player.setExp(self.__player.getExp() + 500)
            self.__player.restoreHealth()
            self.__player.levelUp()
            nextLevel = LandBetweenWorlds(player) #Call the subclass to proceed to the next area

        pass

    def useFact(self, player, enemy):
        #This function checks the skill of the player at that moment then generates different outputs
        if(player.getResourcefulness() >= 15 and player.getIntelligence() >= 12):
            print("As quietly as possible you stab the Queen in the back for half her health!")
            enemy.lowerHealth(enemy.getHealth() / 2)
        else:
            print("Merider: I can still sense you!")
            print("Merider injures your arm in your attempt at stabbing her. As a result you loose 2 strength and 3 health")
            player.setStrength(player.getStrength - 2)
            player.lowerHealth(3)

    def fightHeadOn(self, player, enemy):
        print("Your courage gives you the extra strength necessary for this fight and onwards.")
        player.setStrength(player.getStrength() * 2)

