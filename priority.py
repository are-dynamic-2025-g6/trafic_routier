from car import Car
from intersection import Intersection

# Priority means: I can go to $targetIndex,
# but I have to be carful about $waitFor intersections


class Priority:
	UNDEFINED = -1
	FORBIDDEN = 0
	STOP = 1
	LET = 2
	PASS = 3

	def __init__(self, targetIndex: int, turnDist: float, waitFor: list[int]):
		self.targetIndex = targetIndex # read in target list
		self.turnDist = turnDist
		self.waitFor = waitFor # read in origin list










