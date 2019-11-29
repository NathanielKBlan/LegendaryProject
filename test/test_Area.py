import sys

sys.path.append("../")

from areas.Area import Area

def test():
	a = Area('KaltsSea', 'Lighthouse', 'Cottage By the Beach', 'Sea Witch')
	print(a.getAreaName())

def main():
	test()
	
main()
