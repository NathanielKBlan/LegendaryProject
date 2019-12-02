import random

from enemies.Enemy import Enemy


class MermaidOfFrost(Enemy):

    def __init__(self, expModifier):
        super().__init__("Mermaid of Frost", 20 + (expModifier * 0.025), ["Slash"])

