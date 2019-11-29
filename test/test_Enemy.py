import sys
sys.path.append("../")

from enemies.Enemy import Enemy

def test():
    pikachu = Enemy(10, 'Thunderbolt')
    print(pikachu.getHealth())
    print(pikachu.getAbilities())


def main():
    test()

main()
