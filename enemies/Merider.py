import random

from enemies.Enemy import Enemy


class Merider(Enemy):

    def __init__(self):
        super().__init__("Merider, Queen of Frost", 40, ["Slash", "Freeze", "Entrance"])

    def attack(self, player,  attackNum = int(random.random() * 9 + 1)):
        if(attackNum <= 5):
            self.slashAttack()
        elif(attackNum > 5 and attackNum <= 8):
            self.freeze(player)
        else:
            self.entrance(player)

    def freeze(self, player):
        print("Merider hits you with a wave of cold, chilling you to the bone.")
        print("As a result you loose a turn.")
        self.attack(player, 1)
        self.attack(player, 1)

    def entrance(self, player):
        print("One again you are entranced by Merider's voice.")
        print("You stab yourself!")
        player.lowerHealth(player.attack(player))
        print("You come out of the trance.")