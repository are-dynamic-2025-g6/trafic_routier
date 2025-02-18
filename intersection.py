


PRIORITY_STOP = 0
PRIORITY_LET = 1
PRIORITY_PASS = 2

Intersection_idGenerator = 0

class Intersection:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.prios = [] # (receivedIndex, priorityState)
		self.carWaitingFor = [] # cars trying to go on the intersection
		self.directions = [] # intersections towards we can go
		self.received = [] # intersections 

	
	def getPrio(self, a, b):
		return a
	



