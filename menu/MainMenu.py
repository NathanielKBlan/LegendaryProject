from menu.Menu import Menu

#This is the main menu class.
#This is where the game starts, wether it be a new one or a previous one
class MainMenu(Menu):

    #To be called upon initialization
    #Default number of menu options is set at 4
    #Default menu name is set to Main Menu
    #Default options are set to: New Game, Load Game, Credits, and Exit
    def __init__(self):
        super().__init__(4, "Main Menu", ["New Game", "Load Game", "Credits","Exit"])
