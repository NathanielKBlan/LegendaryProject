import random

#This is the default player class, can be chosen if so wished

class Ordinary:

    def __init__(self, health = 25, charisma = 10, strength = 10, intelligence = 10, resourcefulness = 10, faith = 10, luck = 10, name = "player"):
        self.__health = health
        self.__charisma = charisma
        self.__strength = strength
        self.__intelligence = intelligence
        self.__resourcefulness = resourcefulness
        self.__faith = faith
        self.__luck = luck
        self.__name = name
        self.__inventory = []
        self.__exp = 0

    #The following methods are getters and setters, all of these will be inherited by other classes
    #Can be overwritten if so wished
    def getHealth(self):
        return self.__health

    def getCharisma(self):
        return self.__charisma

    def getStrength(self):
        return self.__strength

    def getIntelligence(self):
        return self.__intelligence

    def getResourcefulness(self):
        return self.__resourcefulness

    def getLuck(self):
        return self.__luck

    def getFaith(self):
        return self.__faith

    def getName(self):
        return self.__name

    def getExp(self):
        return self.__exp

    def setHealth(self, newHealth):
        self.__health = newHealth

    def setCharisma(self, newCharmisma):
        self.__charisma = newCharmisma

    def setStrength(self, newStrength):
        self.__strength = newStrength

    def setIntelligence(self, newIntelligence):
        self.__intelligence = newIntelligence

    def setResourcefulness(self, newResourcefulness):
        self.__resourcefulness = newResourcefulness

    def setLuck(self, newLuck):
        self.__luck = newLuck

    def setFaith(self, newFaith):
        self.__faith = newFaith

    def setName(self, newName):
        self.__name = newName

    def addToInventory(self, item):
        self.__inventory.append(item)

    def takeDamage(self, demage):
        self.__health -= demage

    def attack(self, enemy):
        value = random.randint(1, (5 + self.__strength / 2))
        print('You attacked', enemy + '.')
        print(enemy, 'got', value, 'demage.')
        return value


