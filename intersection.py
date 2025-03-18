INTERSECTION_SIZE = 10

from enum import Enum
from car import Car

Intersection_idGenerator = 0

class Intersection:
	def __init__(self, x: float, y: float, spawnCapacity = 0: int, carCount: int):
		self.x = x
		self.y = y
		self.spawnCapacity = spawnCapacity
		self.carCount = carCount
		self.prios: list[list[Priority]] = []
		self.carsApproching: list[Car] = [] # cars trying to go on the intersection
		self.targets: list[Intersection] = [] # intersections towards we can go
		self.origins: list[Intersection] = [] # intersections 



	def getCarTargetIndex(self, intersection):
		for i in range(len(self.targets)):
			if self.targets[i] == intersection:
				return i
		
		return -1
	
	def getCarOriginIndex(self, intersection):		
		for i in range(len(self.origins)):
			if self.origins[i] == intersection:
				return i
		
		return -1
	
	


