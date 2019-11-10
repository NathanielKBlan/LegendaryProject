#This is the default menu class which takes in two parameters upon initialization:
#itself and the amount of options the menu will contain
## TODO: Write the MainMenu class that inherits from this Menu class
class Menu:

    options = 0

    #Menu options will be contained in this list
    menu = []

    #To be called upon initialization
    def __init__(self, options):
        self.options = options
        menu = generateMenu(menu, options)
        return None

    #Generates the default menu
    def generateMenu(menuList, options):
        for i in range(options):
            menuList[i] = str(i + 1) + ": "
        return menuList
