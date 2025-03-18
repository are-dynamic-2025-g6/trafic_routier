CAR_SIZE = 20

from Q_rsqrt import Q_rsqrt
from math import log

class Car:
	STANDARD_MAX_SPEED = 4
	FRICTION_FACTOR = .176 / 1000
	TURN_BRAKING_TICK_DURATION = 30
	MAX_ACCELERATION = .08
	MAX_DECELERATION = .5
	
	id=0

	def __init__(self, size: int, reachSpeedFactor: float, origin, target):
		self.origin = origin
		self.target = target 
		self.dist = 0.0
		self.alive = True
		self.nextPriority = None
		self.id = Car.id
		self.size = size
		Car.id += 1

		self.reachSpeedFactor = reachSpeedFactor

		self.keptCheckDist = -1.0

		self.speed: float = 0
		self.speedLimit = Car.STANDARD_MAX_SPEED
		self.approchingTurnSpeed: float = -1

		# add car to target list
		target.carsApproching.append(self)


	def reachSpeed(self, aimSpeed):
		val = self.reachSpeedFactor * (aimSpeed - self.speed)
		if val > Car.MAX_ACCELERATION:
			val = Car.MAX_ACCELERATION
		elif val < -Car.MAX_DECELERATION:
			val = -Car.MAX_DECELERATION
	
		self.speed += val


	def getSafetyDist(self):
		s = self.speed

		if s <= 0:
			return 0
		
		return 4 * s * s / self.reachSpeedFactor


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


class CarInFront:
	def __init__(self, car: Car, dist: float):
		self.car = car
		self.dist = dist
