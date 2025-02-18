CAR_SIZE = 20


from math import sqrt

class Car:
	STANDARD_MAX_SPEED = .8
	
	def __init__(self, origin, aim):
		self.origin = origin
		self.aim = aim
		self.dist = 0.0
		self.speed = 0.0
		self.maxSpeed = Car.STANDARD_MAX_SPEED

	def accelerate(self):
		self.speed += .009
		if self.speed > self.maxSpeed:
			self.speed = self.maxSpeed



	def move(self):
		self.dist += self.speed

	def getCoord(self):
		dx = self.aim.x - self.origin.x
		dy = self.aim.y - self.origin.y
		r = self.dist / sqrt(dx*dx + dy*dy)
		return (
			self.origin.x + dx*r,
			self.origin.y + dy*r
		)
		



