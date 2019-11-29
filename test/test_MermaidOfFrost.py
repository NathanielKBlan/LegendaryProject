import sys
sys.path.append("../")

from enemies.MermaidOfFrost import MermaidOfFrost

def test():
    
    a = MermaidOfFrost(100)
    a.slashAttack()
    a.freezeAttack()
    a.entranceAttack("Wryn") #Test failed at here

def main():
    test()

main()

