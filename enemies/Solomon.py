
#This is the Solomon class that is inherit from the Enemy class
class Solomon(Enemy):
	#Initialize the subclass with three instances
    def __init__(self):
        super().__init__("Solomon", 40, ["Slash"])