#This module contains various methods that can be used for input verification

#This method acts as a switch statment and pairs certain values with cases
def switch(value, keys, *arg):

	switchingCases = {}
	switchingCasesNums = {}

	for i in range(len(arg)):
		switchingCases[keys[i]] = arg[i]

	for i in range(len(arg)):
		switchingCasesNums[i] = arg[i]

	if(value not in keys):
		try:
			if (int(value) <= 0 or int(value) > len(arg)):
				newVal = input("That was invalid input, please enter a new option: ")
				return switch(newVal, keys, arg)
			else:
				case = switchingCasesNums.get(int(value) - 1)
				return case
		except ValueError:
			newVal = input("That was invalid input, please enter a new option: ")
			return switch(newVal, keys, arg)
	else:
		case = switchingCases.get(value)
		return case
