
class Enemy():

    def __init__(self, health, abilities):
        self.__health = health
        self.__abilities = abilities

    def getHealth(self):
        return self.__health

    def getAbilities(self):
        return self.__abilities