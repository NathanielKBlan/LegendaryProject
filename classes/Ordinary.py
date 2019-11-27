#This is the default player class, can be chosen if so wished
class Ordinary:

    def __init__(self, health = 25, charisma = 10, strength = 10, intelligence = 10, resourcefulness = 10, faith = 10, luck = 10):
        self.__health = health
        self.__charisma = charisma
        self.__strength = strength
        self.__intelligence = intelligence
        self.__resourcefulness = resourcefulness
        self.__faith = faith
        self.__luck = luck
        self.__inventory = []

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

    def addToInventory(self, item):
        self.__inventory.append(item)