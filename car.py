CAR_SIZE = 10

from Q_rsqrt import Q_rsqrt
import random

from ParamObject import ParamObject

class Car:
	id=0

	INIT_MAX_SPEED = 25
	ANGRY_UNIT = 2
	DEFAULT_SIZE = 12

	def __init__(self, reachSpeedFactor: float, origin, finalTarget, size: int=DEFAULT_SIZE):
		self.origin = origin
		self.target = None
		self.finalTarget = finalTarget
		self.dist = 0.0
		self.fullDist = 0
		self.spawnCouldown: int = -1
		self.nextPriority = None
		self.id = Car.id
		self.size = size
		self.path: list[int] = None
		Car.id += 1

		self.reachSpeedFactor = reachSpeedFactor

		self.keptCheckDist = -1.0

		self.speed: float = 0
		self.speedLimit = Car.INIT_MAX_SPEED
		self.approchingTurnSpeed: float = -1


		# Stats data
		self.spawnLapCount: int = -1
		self.angryDuration = 1


	def isAlive(self):
		return self.spawnCouldown < 0

	def kill(self, params: ParamObject):
		self.fullDist = 0
		self.spawnCouldown = round(
			params.respawnCouldownAverage 
			+ random.uniform(-1, 1) * params.respawnCouldownGap
		)

	def reachSpeed(self, aimSpeed, params: ParamObject):
		val = self.reachSpeedFactor * (aimSpeed - self.speed)
		if val > params.maxAcceleration:
			val = params.maxAcceleration
		elif val < -params.maxBraking:
			val = -params.maxBraking
	
		self.speed += val


	def getSafetyDist(self):
		s = self.speed

		if s <= 0:
			return 0
		
		return 4 * s * s / self.reachSpeedFactor


	def move(self, params: ParamObject):
		self.dist += self.speed
		self.speed -= params.frictionFactor * self.speed * self.speed


	def getCoord(self):
		if not self.target:
			return (-1, -1)
		
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
