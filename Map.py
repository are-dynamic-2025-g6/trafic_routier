from car import Car
from intersection import Intersection

from StatObject import StatObject
from ParamObject import ParamObject

import random

class Map:
	SPAWN_SCORE_FACTOR = -2

	def __init__(self):
		self.intersections: list[Intersection] = []
		self.cars: list[Car] = []
		self.lx: float = 0
		self.ly: float = 0
		self.mx: float = 0
		self.my: float = 0
		self.stats = StatObject()
		self.params = ParamObject()
		self.lapCount = 0


	def createRandomFinalTarget(self) -> Intersection:
		x = random.uniform(self.lx, self.mx)
		y = random.uniform(self.ly, self.my)

		lowerScore = 3e38
		best = None

		for i in self.intersections:
			if i.spawnScore <= 0:
				continue

			sqDist = (i.x - x)**2 + (i.y - y)**2
			score = sqDist * (i.spawnScore ** Map.SPAWN_SCORE_FACTOR)
			if score < lowerScore:
				lowerScore = score
				best = i


		return best
	
	def setSize(self):
		lx = 0
		ly = 0
		mx = 0
		my = 0

		for i in self.intersections:
			if i.x < lx:
				lx = i.x
			
			if i.x > mx:
				mx = i.x

			if i.y < ly:
				ly = i.y
			
			if i.y > my:
				my = i.y

		self.lx = lx-100
		self.ly = ly-100
		self.mx = mx+100
		self.my = my+100
