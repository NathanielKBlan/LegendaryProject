from random import random


class Enemy():

    def __init__(self, health, abilities):
        self.__health = health
        self.__abilities = abilities

    def getHealth(self):
        return self.__health

    def getAbilities(self):
        return self.__abilities

    def slashAttack(self):
        damage = int(random.random() * 5)
        print("You were attacked for: " + damage + " damage")
        return damage