from car import Car
from intersection import Intersection

from StatObject import StatObject
from ParamObject import ParamObject

import random


MAP_SEED = 42

class Map:
	SPAWN_SCORE_FACTOR = -2
	INDEX = 0

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
		self.rand = random.Random(MAP_SEED)
		self.index = Map.INDEX
		Map.INDEX += 1


	def createRandomFinalTarget(self, forbidden: Intersection = None) -> Intersection:
		x = self.rand.uniform(self.lx, self.mx)
		y = self.rand.uniform(self.ly, self.my)


		lowerScore = 3e38
		best = None

		for i in self.intersections:
			if i.spawnScore <= 0 or i == forbidden:
				continue

			sqDist = (i.x - x)**2 + (i.y - y)**2
			score = sqDist * (i.spawnScore ** Map.SPAWN_SCORE_FACTOR)
			if score < lowerScore:
				lowerScore = score
				best = i


		return best
	
	def setSize(self):
		# TODO: remove return

		# self.lx = -160.0
		# self.ly = -160.0
		# self.mx = 1660.0
		# self.my = 1660.0
		# return


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

		print("Map size:", self.lx, self.ly, self.mx, self.my)
