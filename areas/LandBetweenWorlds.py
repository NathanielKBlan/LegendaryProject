
#This is the second area of the game, Land between Worlds.

import random

from areas.Area import Area #Import the Area module as the parent class
from areas.TheSkiesOfFire import TheSkiesOfFire #Import the module in which the story continues to the next area
from enemies.Enemy import Enemy #Import the Enemy module as the parent class for two enemy classes of this area
from tools.input_verification import switch


class LandBetweenWorlds(Area):
    #This is the subclass inherit from the Area class
    #Which takes six methods of events: printArrival, battleWithErthel, proceedToLandOfDead, combatWithMortis, looseExperience, proceedToSkyGateWay

    #This is the constructor method that takes one instance variable, player
    def __init__(self, player):
        self.__player = player
        self.__erthelIsDead = False
        self.printArrival()

    def printArrival(self):
        print("To reach the skies of fire, you head off to the land between worlds, a trecherous path but a necessary one.")
        print("On the path, you meet an old man who calls himself Erthel")
        print("Erthel: well well, there are still some of you left. No matter, I will finish this. Prepare yourself!")

        #Check to see if the enemy of this area is dead, battle if not
        if(not self.__erthelIsDead):
            self.battleWithErthel()
        else:
            self.proceedToSkyGateWay()

    def battleWithErthel(self):
        #This function generates the battle w/ the enemy, Erthel
        erthel = Enemy("Erthel", 10000, None)
        firstStrike = int(random.random() * 1 + 1)

        if (firstStrike == 1):
            print("Quick to your senses you slash Erthel with your weapon")
            erthel.lowerHealth(self.__player.attack(erthel))

        else:
            print("You attempt to make the first attack but Erthel parries it.")
            print("Erthel cuts you")
            self.__player.lowerHealth(erthel.slashAttack())

        while (int(erthel.getHealth()) > 0 and int(self.__player.getHealth()) > 0):
            print("Your health: " + str(self.__player.getHealth()))
            print("Erthel's health: " + str(erthel.getHealth()))
            input("Enter anything to continue")
            erthel.lowerHealth(self.__player.attack(erthel))
            self.__player.lowerHealth(erthel.slashAttack())

        if (self.__player.getHealth() < 0):
            print("Erthel kills you. The world goes dark.")
            self.__player.setExp(self.__player.getExp() + 50)
            self.proceedToLandOfDead()

        else:
            print("You kill Erthel for his betrayal and move on to your destination")
            print("Malicious laughter is heard from a distance")
            self.__player.setExp(self.__player.getExp() + 500)
            self.__player.levelUp()
            self.__erthelIsDead = True
            self.proceedToSkyGateWay()

    def proceedToLandOfDead(self):
        #This method takes the choice of player of whether to combat or not
        print("As you awake, you meet a demon who calls himself Mortis")
        print("Mortis: I'll make you a deal, best me in combat or loose some valuable experience and I'll return you to the")
        print("world of the living.")
        #Use the switch method to get the choice from player then call upon the corresponding function
        path = switch(input("What say you? "), ["Combat", "Loose Experience"], self.combatWithMortis, self.looseExperience)
        path()

    def combatWithMortis(self):
        #This method generate the battle with the enemy, Mortis
        mortis = Enemy(30, None)
        firstStrike = int(random.random() * 1 + 1)

        if (firstStrike == 1):
            print("Quick to your senses you slash Mortis with your weapon")
            mortis.lowerHealth(self.__player.attack(mortis))

        else:
            print("You attempt to make the first attack but Mortis parries it.")
            print("Mortis cuts you")
            self.__player.lowerHealth(mortis.slashAttack())

        while (int(mortis.getHealth()) > 0 and int(self.__player.getHealth()) > 0):
            print("Your health: " + str(self.__player.getHealth()))
            print("Mortis' health: " + str(mortis.getHealth()))
            input("Enter anything to continue")
            mortis.lowerHealth(self.__player.attack(mortis))
            self.__player.lowerHealth(mortis.slashAttack())

        if (self.__player.getHealth < 0):
            print("Mortis laughs at your efforts")
            self.__player.setExp(self.__player.getExp() + 50)
            self.proceedToLandOfDead()

        else:
            print("You best Mortis in combat and he honors the deal")
            self.__player.setExp(self.__player.getExp() + 500)
            self.__player.levelUp()
            self.printArrival()

    def looseExperience(self):
        #This method reduce the exp of the player
        print("Mortis: Very well.")
        self.__player.setExp(self.__player.getExp() - 500)
        self.printArrival()

    def proceedToSkyGateWay(self):
        #This method generates the battle w/ the enemy, Sill
        print("Guarding the gates to the skies of Fire is none other than Sill, the best combatant of the land of ashes.")
        print("Sill: I have hunted all your people down before, and I shall avenge Erthel's death!")
        sill = Enemy("Sill", 75, None) #Generate an enemy subclass, Sill
        firstStrike = int(random.random() * 1 + 1)

        if (firstStrike == 1):
            print("Quick to your senses you slash Sill with your weapon")
            sill.lowerHealth(self.__player.attack(sill))

        else:
            print("You attempt to make the first attack but Sill parries it.")
            print("Sill cuts you")
            self.__player.lowerHealth(sill.slashAttack())

        while (int(sill.getHealth()) > 0 and int(self.__player.getHealth()) > 0):
            print("Your health: " + str(self.__player.getHealth()))
            print("Sill's health: " + str(sill.getHealth()))
            input("Enter anything to continue")
            sill.lowerHealth(self.__player.attack(sill))
            self.__player.lowerHealth(sill.slashAttack())

        if (self.__player.getHealth() < 0):
            print("Sill delivers the final blow.")
            self.__player.setExp(self.__player.getExp() + 50)
            self.proceedToLandOfDead()

        else:
            print("Sill: But how...")
            self.__player.setExp(self.__player.getExp() + 500)
            self.__player.levelUp()
            netLevel = TheSkiesOfFire(self.__player)
