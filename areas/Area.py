
#This is the Area class, where the story took place
class Area:

    #The constructor method takes 4 instance variables: name of area, previous area, next area, & enemies inhabit in this area
    def __init__(self, areaName, previousArea, nextArea, enemies):
        self.__areaName = areaName
        self.__previousArea = previousArea
        self.__nextArea = nextArea
        self.__enemies = enemies
        #These private intances are used to inicate the state of an enemy's life, which are set to determine the branches of the story
        self.__solomonIsDead = False
        self.__sillIsDead = False
        self.__erthelIsDead = False

    #The accessor method which is used to get the name of the area
    def getAreaName(self):
        return self.__areaName