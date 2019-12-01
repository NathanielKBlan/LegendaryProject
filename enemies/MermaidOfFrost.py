import random

from enemies.Enemy import Enemy


class MermaidOfFrost(Enemy):

    def __init__(self, expModifier):
        super().__init__("Mermaid of Frost", 20 + (expModifier * 0.025), ["Slash", "Freeze", "Entrance"])


    def slashAttack(self):
        damage = int(random.random() * 5)
        print("The mermaid slashes at you for:", damage, "damage")
        return damage


    def freezeAttack(self):
        print("You can't move, it's too cold.")
        totalDamage = self.slashAttack()
        totalDamage += self.slashAttack()
        print("You feel warm enough now to move.")
        return totalDamage

    def entranceAttack(self, player):
        print("You feel entranced by the mermaid's beauty, you would do anything for her.")
        totalDamage = player.attack()
        print("You stab yourself for: ", totalDamage, " damage!")
        return totalDamage