#This module contains various methods that can be used for input verification

#This method acts as a switch statment and pairs certain values with cases
def switch(value, arg*):

    switchingCases = {}
    for i in range(len(arg)):
        switchingCases[i + 1] = arg[i]

    if(value > len(arg) or value < 1):
        newVal = int(input("That was invalid input, please enter a new option: "))
        return None
    else:
        case = switchingCases.get(value)
        return case
