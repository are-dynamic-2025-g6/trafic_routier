INTERSECTION_SIZE = 10

from car import Car

PRIORITY_STOP = 0
PRIORITY_LET = 1
PRIORITY_PASS = 2

Intersection_idGenerator = 0


class Priority:
	def __init__(self, receivedIndex: int, priorityState: int):
		self.receivedIndex = receivedIndex
		self.priorityState = priorityState


class Intersection:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.prios: list[list[Priority]] = []
		self.carWaitingFor: list[Car] = [] # cars trying to go on the intersection
		self.directions: list[Intersection] = [] # intersections towards we can go
		self.received: list[Intersection] = [] # intersections 


	def getCarDirectionIndex(self, intersection):
		for i in range(len(self.directions)):
			if self.directions[i] == intersection:
				return i
		
		return -1
	
	def getCarReceivedIndex(self, intersection):
		for i in range(len(self.received)):
			if self.received[i] == intersection:
				return i
		
		return -1



