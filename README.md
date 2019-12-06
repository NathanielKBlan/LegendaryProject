# LendaryProject
Final project for CS111

## Goal
To make a text based rpg game using object oriented programming.

## text adventure game

This is a text adventure game about a chosen human who goes on a journey to aleviate a curse. 

## Tools package

This package really only contains one module, input_verification.py which contains only one method, the switch method.
The switch method allows us to not only verify user input but also to bypass needing different if and else statements
to produce certain outputs with certain inputs. This is done by pairing inputs with outputs in a dictionary and retrieving the outputs based on the inputs. If the input is faulty then the user will be prompted to input again till the input is valid. The switch method takes in the following parameters in this order: value, keys, functions where value is the input, keys is the list of expected inputs, and functions is a list of outputs. 

## Test package

This is where all our unit tests are written for each object. Just to verify that everything is working accordingly. The tests are ran autonomously using pytest, which is a testing program used by github to run our tests whenever we push new code to the repository. We are then emailed if any test has failed. Each unit test follows this basic format, instantiate object, run all object methods and print results (sometimes), end test.

## Menu package
### Menu
The menu class is the default class for generating menu objects. It's constructor takes in a list of options, a title, and a list of options. The methods contained in the menu class are generateMenu, getOptionInput, and printMenu. generateMenu generates the menu and stores it in a list, getOptionInput takes in user input, and printMenu simply prints the menu.

### Main Menu
The main menu class serves as the game's main menu. The main menu has three methods, New Game, Credits, and Exit. Each of the method names really describes what they do, just with the exception of New Game. When selecting new game it starts a new game and prints a prologue and then takes the player directly to the character creation menu. The Main Menu iherits from the default menu object, and therefore has the same methods as menu.

### Character Creation Menu
The character creation menu, like the main menu, inherits from menu. The character creation menu has three methods, printIntroductionStory just prints another part of the lore of the game, then there's chooseClass which uses the switch function to allow for choosing a character class and veriying user input. Then there's get player which returns the character class of the player.

## Game Package
### Game
The game class get's the name of the player, prints the prologue and takes them directly to the character customization menu.
It then proceeds to take the player to the first level of the game.

### Land of Ashes
The Land of Ashes is the main startup script for the game and prints out the Main Menu.

## Enemies package
### Enemy
The default enemy class. All other enemy classes build off this. The main methods this class has are slashAttack, getHealth, lowerHealth, and getName. The other methods are depricated and therefore unused. All enemy classes are similar to this with the difference being health, and attack values.

## Classes package
All classes under this package are character classes, each class has different amount of health, charisma, intelligence, strength, resourcefullness, faith, and luck. The only stats that are of most importance throughout the game are health, intelligence, resourcefullness, and strength. Each has a getter and setter and there is also an attack and levelUp method. The levelUp method increases all of the player's stats by 2.5%. There is also an exp value with getters and setters. All character classes inherit from the dafualt Ordinary class.

## Areas package
Area is the deault area class and takes in a value of area name, previous area, next area, and a list of enemies in the area. An area is an in game level. Each area is different and has a different story and user interactions. There are combat/battle methods in each area where the user and enemy take turns attacking each other till one's hp reaches 0. After the combat/battle method, depending if successfull there is a boss fight method, which if passed leads to the next level, until the final level. If the boss in the final level is defeated the ending is printed.
