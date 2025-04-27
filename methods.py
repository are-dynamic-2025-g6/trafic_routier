from car import Car, CarInFront
from intersection import Intersection
from priority import Priority
from findPath import findPath

from math import sqrt, inf

from stats import *

import Q_rsqrt


INFINITY = inf


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



# TODO: this method
def Intersection_getMaxTurnSpeed(
	origin: Intersection,
	passedBy: Intersection,
	target: Intersection,
	dist: float
):
	maxTurnSpeed = 200000000

	return maxTurnSpeed



def Car_changeRoad(map: Map, car: Car, nextTarget: Intersection, nextPriority: Priority):
	car.fullDist = 0

	# Remove from carsApproching list
	carTarget: Intersection = car.target

	carTarget.carsApproching.remove(car)
	
	if map.params.keepSameDirection == -1:
		if not car.path:
			car.origin = carTarget
			Stat_onCarFinish(map, car)
			car.kill(map.params)
			return

		car.origin = carTarget
		Car_definePath(car)

	else:
		car.origin = carTarget
		target = carTarget.targets[0]
		car.target = target
		target.carsApproching.append(car)
		car.path = [0, 0, 0]

	# nextTarget = car.target

	# Add to next target
	# nextTarget.carsApproching.append(car)

	# Change car origin

	# Adjustements
	car.approchingTurnSpeed = -1 # load next max turn speed
	car.nextPriority = None # change priority
	
	car.keptCheckDist = -1.0



	# Consume next path
	# carTarget.targets[car.path[0]]
	# car.path.pop(0)
	
	




def Car_spawn(car: Car, finalTarget: Intersection):
	if finalTarget == None or finalTarget == car.origin:
		car.spawnCouldown = 3 # try another spawn
		return False

	car.finalTarget = finalTarget
	if Car_definePath(car):
		car.speed = 0
		return True
	
	car.spawnCouldown = 3 # try another spawn
	return False


def Car_definePath(car: Car):
	origin: Intersection = car.origin

	path = findPath(origin, car.finalTarget)	
	if not path:
		return False
	
	target: Intersection = origin.targets[path[0]]
	car.target = target
	target.carsApproching.append(car)

	path.pop(0)
	car.path = path


	return True



def Intersection_waitFor(priority: Priority, intersection: Intersection) -> list[Car]:
	ret: list[Car] = []
	for originIndex in priority.waitFor:
		for car in intersection.carsApproching:
			if intersection.origins[originIndex] == car.origin:
				ret.append(car)
				break
	
	return ret














def Car_frame(map: Map, car: Car):
	origin: Intersection = car.origin
	target: Intersection = car.target



	# Check path
	if car.path == None:
		if not Car_definePath(car):
			raise Exception("Cannot find path")
		
		target: Intersection = car.target



	# Check car valid
	if target == None:
		return


	# print(origin.x, target.targets[0].x, car.path)
	if car.path:
		nextTarget: Intersection = target.targets[car.path[0]]
	else:
		nextTarget: Intersection = None



	dx = target.x - origin.x
	dy = target.y - origin.y

	if car.fullDist == 0:
		fullDist = sqrt(dx*dx + dy*dy)
		car.fullDist = fullDist
	else:
		fullDist = car.fullDist

	leftDist = fullDist - car.dist

	# Get next priority
	if nextTarget:
		if car.nextPriority == None:
			nextPriority = Car_getNextPriority(car, nextTarget)
			car.nextPriority = nextPriority
		else:
			nextPriority: Priority = car.nextPriority
	else:
		nextPriority: Priority = None




	def Intersection_canPass():
		for originIndex in nextPriority.waitFor:
			for car in target.carsApproching:
				if target.origins[originIndex] == car.origin:
					nextDist = map.params.checkPassingDuration * car.speed
					if car.dist + nextDist >= car.fullDist:
						return False
		
		return True


		"""
		waitFor = Intersection_waitFor(nextPriority, target)
		
		if not waitFor:
			return True


		# TODO: Check if we can pass (using distances)

		return False
		"""
	



	def calculateIdealSpeed():
		checkDist = car.size * map.params.checkIntersectionDistFactor
		if leftDist >= checkDist:
			return car.speedLimit
		

		# For finishing cars
		if nextPriority == None:
			return ((leftDist/checkDist)*.5 + .5) * car.speedLimit




		# Check intersection
		if Intersection_canPass():
			return car.approchingTurnSpeed + (leftDist/checkDist) * (car.speedLimit - car.approchingTurnSpeed)

		minDist = car.size * map.params.stopDistFactor
		if leftDist <= minDist:
			return 0
		
		return ((leftDist - minDist) / (checkDist - minDist)) * car.speedLimit



			



	# Checks road of the car and the next road
	def getCarInFront(checkNextFront: bool) -> CarInFront:
		carDist = car.dist

		bestCar: Car = None
		bestDist = INFINITY

		# Search in direct front
		for i in target.carsApproching:
			if i.origin != origin:
				continue

			dist = i.dist - carDist
			if dist > 0 and dist < bestDist:
				bestDist = dist
				bestCar = i

		
		if nextTarget and checkNextFront:
			# Search in next road
			for i in nextTarget.carsApproching:
				if i.origin != target:
					continue

				dist = i.dist + leftDist
				if dist < bestDist:
					bestDist = dist
					bestCar = i


		return CarInFront(bestCar, bestDist)



	def getSpeed():
		# TODO: car.keptCheckDist != -1
		carInFront = getCarInFront(True)
		if carInFront.car == None:
			return calculateIdealSpeed()
		
	
		sizeSum = car.size + carInFront.car.size
		dist = carInFront.dist

		if dist <= sizeSum:
			return 0

		fullDist = car.getSafetyDist()
		if dist >= fullDist:
			return calculateIdealSpeed()
		
		return carInFront.car.speed * (dist - sizeSum) / fullDist
		

	if nextTarget and car.approchingTurnSpeed == -1:
		s = Intersection_getMaxTurnSpeed(origin, target, nextTarget, nextPriority.turnDist)
		if s <= car.speedLimit:
			car.approchingTurnSpeed = s
		else:
			car.approchingTurnSpeed = car.speedLimit





	# Get speed
	car.reachSpeed(getSpeed(), map.params)


	# Change road
	if (car.dist >= fullDist):
		car.dist -= fullDist
		Car_changeRoad(map, car, nextTarget, nextPriority)

	




# def Car_getNextPriorityValue(car: Car, target: Intersection) -> int:
# 	priority = Car_getNextPriority(car, target)
# 	if (priority == None):
# 		return Priority.UNDEFINED
	
	





