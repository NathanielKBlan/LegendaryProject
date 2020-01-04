#This is the default menu class which takes in two parameters upon initialization:
#itself and the amount of options the menu will contain
## TODO: Write the MainMenu class that inherits from this Menu class
from tools.input_verification import switch


class Menu:

    #Menu title will be stored here
    menuTitle = ""

    #Generates the default menu
    def generateMenu(self, menuList, options, optionsList):
        for i in range(options):
            menuList.append(str(i + 1) + ": " + optionsList[i])
        return menuList

    #Prints the menu out to the terminal
    def printMenu(self, menuList, menuTitle):
        print("----------" + menuTitle + "----------")
        for i in range(len(menuList)):
            print(menuList[i])

    def getOptionInput(self):
        chosenOption = input("Which path shall you take: ")
        return chosenOption


    #To be called upon initialization
    #Default number of menu options is set at 1
    def __init__(self, options = 1, menuTitle = "Default Menu", optionsList = ['']):
        self.menu = []
        self.options = options
        self.menuTitle = menuTitle
        self.menu = self.generateMenu(self.menu, options, optionsList)
        return None
