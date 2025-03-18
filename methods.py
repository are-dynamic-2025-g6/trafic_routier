from car import Car, CarInFront
from intersection import Intersection
from priority import Priority
from findPath import findPath


from math import sqrt, inf

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



# TODO: this method, cf. https://chatgpt.com/share/67cc026d-09bc-8003-8296-f8737da12049
def Intersection_getMaxTurnSpeed(
	origin: Intersection,
	passedBy: Intersection,
	target: Intersection,
	dist: float
):
	maxTurnSpeed = .1
	return maxTurnSpeed



def Car_changeRoad(car: Car, nextTarget: Intersection, nextPriority: Priority):
	# Remove from carsApproching list
	carTarget: Intersection = car.target

	carTarget.carsApproching.remove(car)
	
	# Add to next target
	nextTarget.carsApproching.append(car)

	# Change car origin
	car.origin = carTarget
	car.target = nextTarget

	# Adjustements
	car.approchingTurnSpeed = -1 # load next max turn speed
	car.nextPriority = None # change priority
	
	car.keptCheckDist = -1.0

	# TODO: speed limit ~ priority


	
	# TODO: to remove, cf main.py:13
	car.alive = False




def Car_definePath(car: Car):
	origin: Intersection = car.origin

	path = findPath(origin, car.finalTarget)	
	if path == None:
		return False
	
	# TODO: remove (bug!!)
	path = [0, 0, 0] 
	print("TODO: rm_bug")

	target: Intersection = origin.targets[path[0]]
	car.target = target
	target.carsApproching.append(car)

	
	car.path = path
	path.pop(0)


	return True



def Intersection_waitFor(priority: Priority, intersection: Intersection) -> list[Car]:
	ret: list[Car] = []
	for car in intersection.carsApproching:
		origin: Intersection = car.origin
		for dirIndex in priority.waitFor:
			if intersection.targets[dirIndex] == origin:
				ret.append(car)
				break
	
	return ret














def Car_frame(car: Car):
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

	print(car.path)
	nextTarget: Intersection = target.targets[car.path[0]]

	dx = target.x - origin.x
	dy = target.y - origin.y

	# TODO: optimization
	fullDist = sqrt(dx*dx + dy*dy)
	leftDist = fullDist - car.dist

	# Get next priority
	if car.nextPriority == None:
		nextPriority = Car_getNextPriority(car, nextTarget)
		car.nextPriority = nextPriority
	else:
		nextPriority: Priority = car.nextPriority




	def Intersection_canPass():
		waitFor = Intersection_waitFor(nextPriority, target)
		
		if not waitFor:
			return True


		# Check if we can pass (using distances)

		return False
	



	def calculateIdealSpeed():
		keptDist = car.keptCheckDist


		# Check dist not yet reached
		if keptDist == -1.0:
			checkDist = car.speed * Car.TURN_BRAKING_TICK_DURATION

			if leftDist > checkDist:
				return car.speedLimit

			car.keptCheckDist = checkDist
			keptDist = checkDist


		# If here, Check dist reached

		# Check intersection
		if not Intersection_canPass():
			return 0
		
		# Slow turn for turn
		return car.approchingTurnSpeed + (leftDist/keptDist) * (car.speedLimit - car.approchingTurnSpeed)




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

		
		if checkNextFront:
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
		carInFront = getCarInFront(car.keptCheckDist != -1)
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
		

	if car.approchingTurnSpeed == -1:
		s = Intersection_getMaxTurnSpeed(origin, target, nextTarget, nextPriority.turnDist)
		if s <= car.speedLimit:
			car.approchingTurnSpeed = s
		else:
			car.approchingTurnSpeed = car.approchingTurnSpeed





	# Get speed
	car.reachSpeed(getSpeed())


	# Change road
	if (car.dist >= fullDist):
		car.dist -= fullDist
		Car_changeRoad(car, nextTarget, nextPriority)

	




# def Car_getNextPriorityValue(car: Car, target: Intersection) -> int:
# 	priority = Car_getNextPriority(car, target)
# 	if (priority == None):
# 		return Priority.UNDEFINED
	
	





