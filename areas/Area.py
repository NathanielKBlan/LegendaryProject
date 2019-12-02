
class Area:

    def __init__(self, areaName, previousArea, nextArea, enemies):
        self.__areaName = areaName
        self.__previousArea = previousArea
        self.__nextArea = nextArea
        self.__enemies = enemies
        self.__solomonIsDead = False
        self.__sillIsDead = False
        self.__erthelIsDead = False

    def getAreaName(self):
        return self.__areaName


