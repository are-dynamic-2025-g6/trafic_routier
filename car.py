CAR_SIZE = 20

from Q_rsqrt import Q_rsqrt


class Car:
	STANDARD_MAX_SPEED = .8
	FRICTION_FACTOR = .176 / 1000
	
	def __init__(self, origin, target):
		self.origin = origin
		self.target = target 
		self.dist = 0.0
		self.alive = True

		self.speed = 0.0
		self.maxSpeed = Car.STANDARD_MAX_SPEED

		# add car to target list
		target.carsApproching.append(self)


	def accelerate(self):
		self.speed += .01
		if self.speed > self.maxSpeed:
			self.speed = self.maxSpeed



	def move(self):
		self.dist += self.speed
		self.speed -= Car.FRICTION_FACTOR * self.speed * self.speed

	def getCoord(self):
		dx = self.target.x - self.origin.x
		dy = self.target.y - self.origin.y
		r = self.dist * Q_rsqrt(dx*dx + dy*dy)

		return (
			self.origin.x + dx*r,
			self.origin.y + dy*r
		)
		



