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
