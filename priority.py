from car import Car
from intersection import Intersection

class Priority:
	def __init__(self, receivedIndex: int, waitFor: list[int]):
		self.receivedIndex = receivedIndex # read in received list
		self.waitFor = waitFor # read in direction list



def getDirectionsToCheck(car: Car):
	aim: Intersection = car.aim
	origin = car.origin
	
    # search origin 







