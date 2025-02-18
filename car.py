CAR_SIZE = 300

class Car:
	def __init__(self, x, y, origin, aim):
		self.x = x
		self.y = y
		self.origin = origin
		self.aim = aim
	

	@staticmethod
	def spawnInIntersection(intersection):
		car = Car(intersection.x, intersection.y, intersection)
		return car










