
#Unit test for the MermaidOfFrost module
import sys
sys.path.append("../") #This function allows the module to be imported from different directories

from enemies.MermaidOfFrost import MermaidOfFrost

def test():
    #Inialize a MermaidOfFrost class
    mermaid = MermaidOfFrost(100)
    
    #Test the methods
    mermaid.slashAttack()
    mermaid.freezeAttack()
    mermaid.entranceAttack("Wryn")

def main():
    test()

main()

