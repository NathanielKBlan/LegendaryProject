
import random


class Enemy():
    #This is the defalt enmey class that can be inherit by other modules of the game
    def __init__(self, name, health, abilities):
        #This is the constructor that takes three instance variables: name, health, and abilities
        self.__name = name
        self.__health = health
        self.__maxHealth = health
        self.__abilities = abilities

    #These are the accessor & mutator methods of the class
    def getHealth(self):
        return self.__health

    def getAbilities(self):
        return self.__abilities

    def slashAttack(self):
        damage = int(random.random() * 5)
        print("You were attacked for: " + str(damage) + " damage")
        return damage

    def lowerHealth(self, damageTaken):
        self.__health = self.__health - damageTaken

    def getName(self):
        return self.__name

    def restoreHealth(self):
        self.__health = self.__maxHealth