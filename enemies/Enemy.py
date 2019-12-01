import random


class Enemy():

    def __init__(self, name, health, abilities):
        self.__name = name
        self.__health = health
        self.__abilities = abilities

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