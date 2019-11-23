#This is the default player class, can be chosen if so wished
class Ordinary:

    def __init__(self):
        self.__health = 25
        self.__charisma = 10
        self.__strength = 10
        self.__intelligence = 10
        self.__resourcefulness = 10
        self.__luck = 10

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

