INTERSECTION_SIZE = 10

from enum import Enum
from car import Car
from math import sqrt


Intersection_idGenerator = 0

class Intersection:
	id = 0

	def __init__(self, x: float, y: float, spawnScore: int = 1):
		self.x = x
		self.y = y
		self.id = Intersection.id
		self.spawnScore = spawnScore
		self.prios: list[list[Priority]] = []
		self.carsApproching: list[Car] = [] # cars trying to go on the intersection
		self.targets: list[Intersection] = [] # intersections towards we can go
		self.origins: list[Intersection] = [] # intersections 
		self.finalTargetCarCount = 0
		
		Intersection.id += 1



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
	

def Intersection_getWeight(origin: Intersection, target: Intersection):
	dx = origin.x - target.x
	dy = origin.y - target.y
	dist = sqrt(dx*dx + dy*dy)

	# get average speed
	carCount = 0
	sum = 0

	for car in target.carsApproching:
		if car.origin == origin:
			carCount += 1
			sum += car.speed

	if carCount:
		if sum <= 0:
			sum = 1
		
		return dist * carCount / sum
	
	return dist / Car.INIT_MAX_SPEED
	


