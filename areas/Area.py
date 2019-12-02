
class Area:

    def __init__(self, areaName, previousArea, nextArea, enemies):
        self.__areaName = areaName
        self.__previousArea = previousArea
        self.__nextArea = nextArea
        self.__enemies = enemies

    def getAreaName(self):
        return self.__areaName


