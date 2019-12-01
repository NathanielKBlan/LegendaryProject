import sys

sys.path.append("../")

from areas.Area import Area
from areas.KaltsSea import KaltsSea
from enemies.MermaidOfFrost import MermaidOfFrost

def test():
	a = KaltsSea("Wryn")
	a.printArrival()
	a.battleWithMermaid("Wryn")

def main():
	test()

main()
