from car import Car
from intersection import Intersection
from priority import Priority

from math import sqrt

def Car_getNextPriorityList(car: Car) -> list[Priority]:
	originIndex = car.target.getCarOriginIndex(car.origin)

	if (originIndex == -1):
		return None

	return car.target.prios[originIndex]



def Car_getNextPriority(car: Car, target: Intersection) -> Priority :
	originIndex = car.target.getCarOriginIndex(car.origin)

	if (originIndex == -1):
		return None
	

	targetIndex = car.target.getCarTargetIndex(target)
	if (targetIndex == -1):
		return None

	for i in car.target.prios[originIndex]:
		if i.targetIndex == targetIndex:
			return i

	return None



# TODO: this method, cf. https://chatgpt.com/share/67cc026d-09bc-8003-8296-f8737da12049
def Intersection_getMaxTurnSpeed(
	origin: Intersection,
	passedBy: Intersection,
	target: Intersection,
	dist: float
):
	return .2 


def Car_changeRoad(car: Car, nextTarget: Intersection, nextPriority: Priority):
	# Remove from carsApproching list
	carTarget: Intersection = car.target

	carTarget.carsApproching.remove(car)
	
	
	# TODO: to remove, cf main.py:13
	car.alive = False





def Car_frame(car: Car, nextTarget: Intersection):
	dx = car.target.x - car.origin.x
	dy = car.target.y - car.origin.y

	fullDist = sqrt(dx*dx + dy*dy)

	# TODO: handle acceleration
	car.accelerate()

	nextPriority = Car_getNextPriority(car, nextTarget)



	# Change road
	if (car.dist >= fullDist):
		car.dist -= fullDist
		Car_changeRoad(car, nextTarget, nextPriority)

	





"""
def Car_getNextPriorityValue(car: Car, target: Intersection) -> int:
	priority = Car_getNextPriority(car, target)
	if (priority == None):
		return Priority.UNDEFINED
	
"""

	



