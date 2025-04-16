# clear && python3 "mapGenerator.py"


from intersection import *
from car import *
from priority import Priority
import numpy as np

import math


TURN_DIST = 6

class SpawnPoint:
	def __init__(self, name: str, x: float, y: float, targets: list[str], spawnScore: int = 1, rightPriority=True):
		self.x = x
		self.y = y
		self.name = name
		self.targets = targets
		self.spawnScore = spawnScore
		self.rightPriority = rightPriority
		







# Exemple d'utilisation
pointsList = [
	[
		300,

		SpawnPoint('0.0', 0, 0, ['0.1'], 1, False),
		SpawnPoint('1.0', 1, 0, ['0.0'], 1, False),
		SpawnPoint('2.0', 2, 0, ['1.0', '2.1'], 1, False),
		SpawnPoint('3.0', 3, 0, ['2.0'], 1, False),
		SpawnPoint('4.0', 4, 0, ['3.0', '4.1'], 1, False),
		SpawnPoint('5.0', 5, 0, ['4.0'], 1, False),

		SpawnPoint('0.1', 0, 1, ['1.1', '0.2'], 1, True),
		SpawnPoint('1.1', 1, 1, ['1.0', '2.1'], 1, True),
		SpawnPoint('2.1', 2, 1, ['3.1', '2.2'], 1, True),
		SpawnPoint('3.1', 3, 1, ['3.0', '4.1'], 1, True),
		SpawnPoint('4.1', 4, 1, ['5.1', '4.2'], 1, True),
		SpawnPoint('5.1', 5, 1, ['5.0'], 1, True),

		SpawnPoint('0.2', 0, 2, ['0.3'], 1, False),
		SpawnPoint('1.2', 1, 2, ['0.2', '1.1'], 1, False),
		SpawnPoint('2.2', 2, 2, ['1.2', '2.3'], 1, False),
		SpawnPoint('3.2', 3, 2, ['2.2', '3.1'], 1, False),
		SpawnPoint('4.2', 4, 2, ['3.2', '4.3'], 1, False),
		SpawnPoint('5.2', 5, 2, ['4.2', '5.1'], 1, False),

		SpawnPoint('0.3', 0, 3, ['1.3', '0.4'], 1, True),
		SpawnPoint('1.3', 1, 3, ['1.2', '2.3'], 1, True),
		SpawnPoint('2.3', 2, 3, ['3.3', '2.4'], 1, True),
		SpawnPoint('3.3', 3, 3, ['3.2', '4.3'], 1, True),
		SpawnPoint('4.3', 4, 3, ['5.3', '4.4'], 1, True),
		SpawnPoint('5.3', 5, 3, ['5.2'], 1, True),

		SpawnPoint('0.4', 0, 4, ['0.5'], 1, False),
		SpawnPoint('1.4', 1, 4, ['0.4', '1.3'], 1, False),
		SpawnPoint('2.4', 2, 4, ['1.4', '2.5'], 1, False),
		SpawnPoint('3.4', 3, 4, ['2.4', '3.3'], 1, False),
		SpawnPoint('4.4', 4, 4, ['3.4', '4.5'], 1, False),
		SpawnPoint('5.4', 5, 4, ['4.4', '5.3'], 1, False),

		SpawnPoint('0.5', 0, 5, ['1.5'], 1, True),
		SpawnPoint('1.5', 1, 5, ['1.4', '2.5'], 1, True),
		SpawnPoint('2.5', 2, 5, ['3.5'], 1, True),
		SpawnPoint('3.5', 3, 5, ['3.4', '4.5'], 1, True),
		SpawnPoint('4.5', 4, 5, ['5.5'], 1, True),
		SpawnPoint('5.5', 5, 5, ['5.4'], 1, True),
	],

	[
		300,
		SpawnPoint('0.0.c0', -0.2, -0.2, ['0.0.c1'], 0, True),
		SpawnPoint('0.0.c1', -0.2, 0.2, ['0.0.f1'], 0, True),
		SpawnPoint('0.0.f1', -0.05, 0.2, ['0.1.i3', '0.0.i1'], 1, True),
		SpawnPoint('0.0.i1', 0.05, 0.2, ['0.0.c2'], 0, False),
		SpawnPoint('0.0.c2', 0.2, 0.2, ['0.0.f2'], 0, True),
		SpawnPoint('0.0.f2', 0.2, 0.05, ['1.0.i0', '0.0.i2'], 1, True),
		SpawnPoint('0.0.i2', 0.2, -0.05, ['0.0.c3'], 0, False),
		SpawnPoint('0.0.c3', 0.2, -0.2, ['0.0.c0'], 0, True),

		SpawnPoint('1.0.c0', 0.8, -0.2, ['1.0.f0'], 0, True),
		SpawnPoint('1.0.f0', 0.8, -0.05, ['0.0.i2', '1.0.i0'], 1, True),
		SpawnPoint('1.0.i0', 0.8, 0.05, ['1.0.c1'], 0, False),
		SpawnPoint('1.0.c1', 0.8, 0.2, ['1.0.f1'], 0, True),
		SpawnPoint('1.0.f1', 0.95, 0.2, ['1.1.i3', '1.0.i1'], 1, True),
		SpawnPoint('1.0.i1', 1.05, 0.2, ['1.0.c2'], 0, False),
		SpawnPoint('1.0.c2', 1.2, 0.2, ['1.0.f2'], 0, True),
		SpawnPoint('1.0.f2', 1.2, 0.05, ['2.0.i0', '1.0.i2'], 1, True),
		SpawnPoint('1.0.i2', 1.2, -0.05, ['1.0.c3'], 0, False),
		SpawnPoint('1.0.c3', 1.2, -0.2, ['1.0.c0'], 0, True),

		SpawnPoint('2.0.c0', 1.8, -0.2, ['2.0.f0'], 0, True),
		SpawnPoint('2.0.f0', 1.8, -0.05, ['1.0.i2', '2.0.i0'], 1, True),
		SpawnPoint('2.0.i0', 1.8, 0.05, ['2.0.c1'], 0, False),
		SpawnPoint('2.0.c1', 1.8, 0.2, ['2.0.f1'], 0, True),
		SpawnPoint('2.0.f1', 1.95, 0.2, ['2.1.i3', '2.0.i1'], 1, True),
		SpawnPoint('2.0.i1', 2.05, 0.2, ['2.0.c2'], 0, False),
		SpawnPoint('2.0.c2', 2.2, 0.2, ['2.0.f2'], 0, True),
		SpawnPoint('2.0.f2', 2.2, 0.05, ['3.0.i0', '2.0.i2'], 1, True),
		SpawnPoint('2.0.i2', 2.2, -0.05, ['2.0.c3'], 0, False),
		SpawnPoint('2.0.c3', 2.2, -0.2, ['2.0.c0'], 0, True),

		SpawnPoint('3.0.c0', 2.8, -0.2, ['3.0.f0'], 0, True),
		SpawnPoint('3.0.f0', 2.8, -0.05, ['2.0.i2', '3.0.i0'], 1, True),
		SpawnPoint('3.0.i0', 2.8, 0.05, ['3.0.c1'], 0, False),
		SpawnPoint('3.0.c1', 2.8, 0.2, ['3.0.f1'], 0, True),
		SpawnPoint('3.0.f1', 2.95, 0.2, ['3.1.i3', '3.0.i1'], 1, True),
		SpawnPoint('3.0.i1', 3.05, 0.2, ['3.0.c2'], 0, False),
		SpawnPoint('3.0.c2', 3.2, 0.2, ['3.0.f2'], 0, True),
		SpawnPoint('3.0.f2', 3.2, 0.05, ['4.0.i0', '3.0.i2'], 1, True),
		SpawnPoint('3.0.i2', 3.2, -0.05, ['3.0.c3'], 0, False),
		SpawnPoint('3.0.c3', 3.2, -0.2, ['3.0.c0'], 0, True),

		SpawnPoint('4.0.c0', 3.8, -0.2, ['4.0.f0'], 0, True),
		SpawnPoint('4.0.f0', 3.8, -0.05, ['3.0.i2', '4.0.i0'], 1, True),
		SpawnPoint('4.0.i0', 3.8, 0.05, ['4.0.c1'], 0, False),
		SpawnPoint('4.0.c1', 3.8, 0.2, ['4.0.f1'], 0, True),
		SpawnPoint('4.0.f1', 3.95, 0.2, ['4.1.i3', '4.0.i1'], 1, True),
		SpawnPoint('4.0.i1', 4.05, 0.2, ['4.0.c2'], 0, False),
		SpawnPoint('4.0.c2', 4.2, 0.2, ['4.0.f2'], 0, True),
		SpawnPoint('4.0.f2', 4.2, 0.05, ['5.0.i0', '4.0.i2'], 1, True),
		SpawnPoint('4.0.i2', 4.2, -0.05, ['4.0.c3'], 0, False),
		SpawnPoint('4.0.c3', 4.2, -0.2, ['4.0.c0'], 0, True),

		SpawnPoint('5.0.c0', 4.8, -0.2, ['5.0.f0'], 0, True),
		SpawnPoint('5.0.f0', 4.8, -0.05, ['4.0.i2', '5.0.i0'], 1, True),
		SpawnPoint('5.0.i0', 4.8, 0.05, ['5.0.c1'], 0, False),
		SpawnPoint('5.0.c1', 4.8, 0.2, ['5.0.f1'], 0, True),
		SpawnPoint('5.0.f1', 4.95, 0.2, ['5.1.i3', '5.0.i1'], 1, True),
		SpawnPoint('5.0.i1', 5.05, 0.2, ['5.0.c2'], 0, False),
		SpawnPoint('5.0.c2', 5.2, 0.2, ['5.0.c3'], 0, True),
		SpawnPoint('5.0.c3', 5.2, -0.2, ['5.0.c0'], 0, True),

		SpawnPoint('0.1.c0', -0.2, 0.8, ['0.1.c1'], 0, True),
		SpawnPoint('0.1.c1', -0.2, 1.2, ['0.1.f1'], 0, True),
		SpawnPoint('0.1.f1', -0.05, 1.2, ['0.2.i3', '0.1.i1'], 1, True),
		SpawnPoint('0.1.i1', 0.05, 1.2, ['0.1.c2'], 0, False),
		SpawnPoint('0.1.c2', 0.2, 1.2, ['0.1.f2'], 0, True),
		SpawnPoint('0.1.f2', 0.2, 1.05, ['1.1.i0', '0.1.i2'], 1, True),
		SpawnPoint('0.1.i2', 0.2, 0.95, ['0.1.c3'], 0, False),
		SpawnPoint('0.1.c3', 0.2, 0.8, ['0.1.f3'], 0, True),
		SpawnPoint('0.1.f3', 0.05, 0.8, ['0.0.i1', '0.1.i3'], 1, True),
		SpawnPoint('0.1.i3', -0.05, 0.8, ['0.1.c0'], 0, False),

		SpawnPoint('1.1.c0', 0.8, 0.8, ['1.1.f0'], 0, True),
		SpawnPoint('1.1.f0', 0.8, 0.95, ['0.1.i2', '1.1.i0'], 1, True),
		SpawnPoint('1.1.i0', 0.8, 1.05, ['1.1.c1'], 0, False),
		SpawnPoint('1.1.c1', 0.8, 1.2, ['1.1.f1'], 0, True),
		SpawnPoint('1.1.f1', 0.95, 1.2, ['1.2.i3', '1.1.i1'], 1, True),
		SpawnPoint('1.1.i1', 1.05, 1.2, ['1.1.c2'], 0, False),
		SpawnPoint('1.1.c2', 1.2, 1.2, ['1.1.f2'], 0, True),
		SpawnPoint('1.1.f2', 1.2, 1.05, ['2.1.i0', '1.1.i2'], 1, True),
		SpawnPoint('1.1.i2', 1.2, 0.95, ['1.1.c3'], 0, False),
		SpawnPoint('1.1.c3', 1.2, 0.8, ['1.1.f3'], 0, True),
		SpawnPoint('1.1.f3', 1.05, 0.8, ['1.0.i1', '1.1.i3'], 1, True),
		SpawnPoint('1.1.i3', 0.95, 0.8, ['1.1.c0'], 0, False),

		SpawnPoint('2.1.c0', 1.8, 0.8, ['2.1.f0'], 0, True),
		SpawnPoint('2.1.f0', 1.8, 0.95, ['1.1.i2', '2.1.i0'], 1, True),
		SpawnPoint('2.1.i0', 1.8, 1.05, ['2.1.c1'], 0, False),
		SpawnPoint('2.1.c1', 1.8, 1.2, ['2.1.f1'], 0, True),
		SpawnPoint('2.1.f1', 1.95, 1.2, ['2.2.i3', '2.1.i1'], 1, True),
		SpawnPoint('2.1.i1', 2.05, 1.2, ['2.1.c2'], 0, False),
		SpawnPoint('2.1.c2', 2.2, 1.2, ['2.1.f2'], 0, True),
		SpawnPoint('2.1.f2', 2.2, 1.05, ['3.1.i0', '2.1.i2'], 1, True),
		SpawnPoint('2.1.i2', 2.2, 0.95, ['2.1.c3'], 0, False),
		SpawnPoint('2.1.c3', 2.2, 0.8, ['2.1.f3'], 0, True),
		SpawnPoint('2.1.f3', 2.05, 0.8, ['2.0.i1', '2.1.i3'], 1, True),
		SpawnPoint('2.1.i3', 1.95, 0.8, ['2.1.c0'], 0, False),

		SpawnPoint('3.1.c0', 2.8, 0.8, ['3.1.f0'], 0, True),
		SpawnPoint('3.1.f0', 2.8, 0.95, ['2.1.i2', '3.1.i0'], 1, True),
		SpawnPoint('3.1.i0', 2.8, 1.05, ['3.1.c1'], 0, False),
		SpawnPoint('3.1.c1', 2.8, 1.2, ['3.1.f1'], 0, True),
		SpawnPoint('3.1.f1', 2.95, 1.2, ['3.2.i3', '3.1.i1'], 1, True),
		SpawnPoint('3.1.i1', 3.05, 1.2, ['3.1.c2'], 0, False),
		SpawnPoint('3.1.c2', 3.2, 1.2, ['3.1.f2'], 0, True),
		SpawnPoint('3.1.f2', 3.2, 1.05, ['4.1.i0', '3.1.i2'], 1, True),
		SpawnPoint('3.1.i2', 3.2, 0.95, ['3.1.c3'], 0, False),
		SpawnPoint('3.1.c3', 3.2, 0.8, ['3.1.f3'], 0, True),
		SpawnPoint('3.1.f3', 3.05, 0.8, ['3.0.i1', '3.1.i3'], 1, True),
		SpawnPoint('3.1.i3', 2.95, 0.8, ['3.1.c0'], 0, False),

		SpawnPoint('4.1.c0', 3.8, 0.8, ['4.1.f0'], 0, True),
		SpawnPoint('4.1.f0', 3.8, 0.95, ['3.1.i2', '4.1.i0'], 1, True),
		SpawnPoint('4.1.i0', 3.8, 1.05, ['4.1.c1'], 0, False),
		SpawnPoint('4.1.c1', 3.8, 1.2, ['4.1.f1'], 0, True),
		SpawnPoint('4.1.f1', 3.95, 1.2, ['4.2.i3', '4.1.i1'], 1, True),
		SpawnPoint('4.1.i1', 4.05, 1.2, ['4.1.c2'], 0, False),
		SpawnPoint('4.1.c2', 4.2, 1.2, ['4.1.f2'], 0, True),
		SpawnPoint('4.1.f2', 4.2, 1.05, ['5.1.i0', '4.1.i2'], 1, True),
		SpawnPoint('4.1.i2', 4.2, 0.95, ['4.1.c3'], 0, False),
		SpawnPoint('4.1.c3', 4.2, 0.8, ['4.1.f3'], 0, True),
		SpawnPoint('4.1.f3', 4.05, 0.8, ['4.0.i1', '4.1.i3'], 1, True),
		SpawnPoint('4.1.i3', 3.95, 0.8, ['4.1.c0'], 0, False),

		SpawnPoint('5.1.c0', 4.8, 0.8, ['5.1.f0'], 0, True),
		SpawnPoint('5.1.f0', 4.8, 0.95, ['4.1.i2', '5.1.i0'], 1, True),
		SpawnPoint('5.1.i0', 4.8, 1.05, ['5.1.c1'], 0, False),
		SpawnPoint('5.1.c1', 4.8, 1.2, ['5.1.f1'], 0, True),
		SpawnPoint('5.1.f1', 4.95, 1.2, ['5.2.i3', '5.1.i1'], 1, True),
		SpawnPoint('5.1.i1', 5.05, 1.2, ['5.1.c2'], 0, False),
		SpawnPoint('5.1.c2', 5.2, 1.2, ['5.1.c3'], 0, True),
		SpawnPoint('5.1.c3', 5.2, 0.8, ['5.1.f3'], 0, True),
		SpawnPoint('5.1.f3', 5.05, 0.8, ['5.0.i1', '5.1.i3'], 1, True),
		SpawnPoint('5.1.i3', 4.95, 0.8, ['5.1.c0'], 0, False),

		SpawnPoint('0.2.c0', -0.2, 1.8, ['0.2.c1'], 0, True),
		SpawnPoint('0.2.c1', -0.2, 2.2, ['0.2.f1'], 0, True),
		SpawnPoint('0.2.f1', -0.05, 2.2, ['0.3.i3', '0.2.i1'], 1, True),
		SpawnPoint('0.2.i1', 0.05, 2.2, ['0.2.c2'], 0, False),
		SpawnPoint('0.2.c2', 0.2, 2.2, ['0.2.f2'], 0, True),
		SpawnPoint('0.2.f2', 0.2, 2.05, ['1.2.i0', '0.2.i2'], 1, True),
		SpawnPoint('0.2.i2', 0.2, 1.95, ['0.2.c3'], 0, False),
		SpawnPoint('0.2.c3', 0.2, 1.8, ['0.2.f3'], 0, True),
		SpawnPoint('0.2.f3', 0.05, 1.8, ['0.1.i1', '0.2.i3'], 1, True),
		SpawnPoint('0.2.i3', -0.05, 1.8, ['0.2.c0'], 0, False),

		SpawnPoint('1.2.c0', 0.8, 1.8, ['1.2.f0'], 0, True),
		SpawnPoint('1.2.f0', 0.8, 1.95, ['0.2.i2', '1.2.i0'], 1, True),
		SpawnPoint('1.2.i0', 0.8, 2.05, ['1.2.c1'], 0, False),
		SpawnPoint('1.2.c1', 0.8, 2.2, ['1.2.f1'], 0, True),
		SpawnPoint('1.2.f1', 0.95, 2.2, ['1.3.i3', '1.2.i1'], 1, True),
		SpawnPoint('1.2.i1', 1.05, 2.2, ['1.2.c2'], 0, False),
		SpawnPoint('1.2.c2', 1.2, 2.2, ['1.2.f2'], 0, True),
		SpawnPoint('1.2.f2', 1.2, 2.05, ['2.2.i0', '1.2.i2'], 1, True),
		SpawnPoint('1.2.i2', 1.2, 1.95, ['1.2.c3'], 0, False),
		SpawnPoint('1.2.c3', 1.2, 1.8, ['1.2.f3'], 0, True),
		SpawnPoint('1.2.f3', 1.05, 1.8, ['1.1.i1', '1.2.i3'], 1, True),
		SpawnPoint('1.2.i3', 0.95, 1.8, ['1.2.c0'], 0, False),

		SpawnPoint('2.2.c0', 1.8, 1.8, ['2.2.f0'], 0, True),
		SpawnPoint('2.2.f0', 1.8, 1.95, ['1.2.i2', '2.2.i0'], 1, True),
		SpawnPoint('2.2.i0', 1.8, 2.05, ['2.2.c1'], 0, False),
		SpawnPoint('2.2.c1', 1.8, 2.2, ['2.2.f1'], 0, True),
		SpawnPoint('2.2.f1', 1.95, 2.2, ['2.3.i3', '2.2.i1'], 1, True),
		SpawnPoint('2.2.i1', 2.05, 2.2, ['2.2.c2'], 0, False),
		SpawnPoint('2.2.c2', 2.2, 2.2, ['2.2.f2'], 0, True),
		SpawnPoint('2.2.f2', 2.2, 2.05, ['3.2.i0', '2.2.i2'], 1, True),
		SpawnPoint('2.2.i2', 2.2, 1.95, ['2.2.c3'], 0, False),
		SpawnPoint('2.2.c3', 2.2, 1.8, ['2.2.f3'], 0, True),
		SpawnPoint('2.2.f3', 2.05, 1.8, ['2.1.i1', '2.2.i3'], 1, True),
		SpawnPoint('2.2.i3', 1.95, 1.8, ['2.2.c0'], 0, False),

		SpawnPoint('3.2.c0', 2.8, 1.8, ['3.2.f0'], 0, True),
		SpawnPoint('3.2.f0', 2.8, 1.95, ['2.2.i2', '3.2.i0'], 1, True),
		SpawnPoint('3.2.i0', 2.8, 2.05, ['3.2.c1'], 0, False),
		SpawnPoint('3.2.c1', 2.8, 2.2, ['3.2.f1'], 0, True),
		SpawnPoint('3.2.f1', 2.95, 2.2, ['3.3.i3', '3.2.i1'], 1, True),
		SpawnPoint('3.2.i1', 3.05, 2.2, ['3.2.c2'], 0, False),
		SpawnPoint('3.2.c2', 3.2, 2.2, ['3.2.f2'], 0, True),
		SpawnPoint('3.2.f2', 3.2, 2.05, ['4.2.i0', '3.2.i2'], 1, True),
		SpawnPoint('3.2.i2', 3.2, 1.95, ['3.2.c3'], 0, False),
		SpawnPoint('3.2.c3', 3.2, 1.8, ['3.2.f3'], 0, True),
		SpawnPoint('3.2.f3', 3.05, 1.8, ['3.1.i1', '3.2.i3'], 1, True),
		SpawnPoint('3.2.i3', 2.95, 1.8, ['3.2.c0'], 0, False),

		SpawnPoint('4.2.c0', 3.8, 1.8, ['4.2.f0'], 0, True),
		SpawnPoint('4.2.f0', 3.8, 1.95, ['3.2.i2', '4.2.i0'], 1, True),
		SpawnPoint('4.2.i0', 3.8, 2.05, ['4.2.c1'], 0, False),
		SpawnPoint('4.2.c1', 3.8, 2.2, ['4.2.f1'], 0, True),
		SpawnPoint('4.2.f1', 3.95, 2.2, ['4.3.i3', '4.2.i1'], 1, True),
		SpawnPoint('4.2.i1', 4.05, 2.2, ['4.2.c2'], 0, False),
		SpawnPoint('4.2.c2', 4.2, 2.2, ['4.2.f2'], 0, True),
		SpawnPoint('4.2.f2', 4.2, 2.05, ['5.2.i0', '4.2.i2'], 1, True),
		SpawnPoint('4.2.i2', 4.2, 1.95, ['4.2.c3'], 0, False),
		SpawnPoint('4.2.c3', 4.2, 1.8, ['4.2.f3'], 0, True),
		SpawnPoint('4.2.f3', 4.05, 1.8, ['4.1.i1', '4.2.i3'], 1, True),
		SpawnPoint('4.2.i3', 3.95, 1.8, ['4.2.c0'], 0, False),

		SpawnPoint('5.2.c0', 4.8, 1.8, ['5.2.f0'], 0, True),
		SpawnPoint('5.2.f0', 4.8, 1.95, ['4.2.i2', '5.2.i0'], 1, True),
		SpawnPoint('5.2.i0', 4.8, 2.05, ['5.2.c1'], 0, False),
		SpawnPoint('5.2.c1', 4.8, 2.2, ['5.2.f1'], 0, True),
		SpawnPoint('5.2.f1', 4.95, 2.2, ['5.3.i3', '5.2.i1'], 1, True),
		SpawnPoint('5.2.i1', 5.05, 2.2, ['5.2.c2'], 0, False),
		SpawnPoint('5.2.c2', 5.2, 2.2, ['5.2.c3'], 0, True),
		SpawnPoint('5.2.c3', 5.2, 1.8, ['5.2.f3'], 0, True),
		SpawnPoint('5.2.f3', 5.05, 1.8, ['5.1.i1', '5.2.i3'], 1, True),
		SpawnPoint('5.2.i3', 4.95, 1.8, ['5.2.c0'], 0, False),

		SpawnPoint('0.3.c0', -0.2, 2.8, ['0.3.c1'], 0, True),
		SpawnPoint('0.3.c1', -0.2, 3.2, ['0.3.f1'], 0, True),
		SpawnPoint('0.3.f1', -0.05, 3.2, ['0.4.i3', '0.3.i1'], 1, True),
		SpawnPoint('0.3.i1', 0.05, 3.2, ['0.3.c2'], 0, False),
		SpawnPoint('0.3.c2', 0.2, 3.2, ['0.3.f2'], 0, True),
		SpawnPoint('0.3.f2', 0.2, 3.05, ['1.3.i0', '0.3.i2'], 1, True),
		SpawnPoint('0.3.i2', 0.2, 2.95, ['0.3.c3'], 0, False),
		SpawnPoint('0.3.c3', 0.2, 2.8, ['0.3.f3'], 0, True),
		SpawnPoint('0.3.f3', 0.05, 2.8, ['0.2.i1', '0.3.i3'], 1, True),
		SpawnPoint('0.3.i3', -0.05, 2.8, ['0.3.c0'], 0, False),

		SpawnPoint('1.3.c0', 0.8, 2.8, ['1.3.f0'], 0, True),
		SpawnPoint('1.3.f0', 0.8, 2.95, ['0.3.i2', '1.3.i0'], 1, True),
		SpawnPoint('1.3.i0', 0.8, 3.05, ['1.3.c1'], 0, False),
		SpawnPoint('1.3.c1', 0.8, 3.2, ['1.3.f1'], 0, True),
		SpawnPoint('1.3.f1', 0.95, 3.2, ['1.4.i3', '1.3.i1'], 1, True),
		SpawnPoint('1.3.i1', 1.05, 3.2, ['1.3.c2'], 0, False),
		SpawnPoint('1.3.c2', 1.2, 3.2, ['1.3.f2'], 0, True),
		SpawnPoint('1.3.f2', 1.2, 3.05, ['2.3.i0', '1.3.i2'], 1, True),
		SpawnPoint('1.3.i2', 1.2, 2.95, ['1.3.c3'], 0, False),
		SpawnPoint('1.3.c3', 1.2, 2.8, ['1.3.f3'], 0, True),
		SpawnPoint('1.3.f3', 1.05, 2.8, ['1.2.i1', '1.3.i3'], 1, True),
		SpawnPoint('1.3.i3', 0.95, 2.8, ['1.3.c0'], 0, False),

		SpawnPoint('2.3.c0', 1.8, 2.8, ['2.3.f0'], 0, True),
		SpawnPoint('2.3.f0', 1.8, 2.95, ['1.3.i2', '2.3.i0'], 1, True),
		SpawnPoint('2.3.i0', 1.8, 3.05, ['2.3.c1'], 0, False),
		SpawnPoint('2.3.c1', 1.8, 3.2, ['2.3.f1'], 0, True),
		SpawnPoint('2.3.f1', 1.95, 3.2, ['2.4.i3', '2.3.i1'], 1, True),
		SpawnPoint('2.3.i1', 2.05, 3.2, ['2.3.c2'], 0, False),
		SpawnPoint('2.3.c2', 2.2, 3.2, ['2.3.f2'], 0, True),
		SpawnPoint('2.3.f2', 2.2, 3.05, ['3.3.i0', '2.3.i2'], 1, True),
		SpawnPoint('2.3.i2', 2.2, 2.95, ['2.3.c3'], 0, False),
		SpawnPoint('2.3.c3', 2.2, 2.8, ['2.3.f3'], 0, True),
		SpawnPoint('2.3.f3', 2.05, 2.8, ['2.2.i1', '2.3.i3'], 1, True),
		SpawnPoint('2.3.i3', 1.95, 2.8, ['2.3.c0'], 0, False),

		SpawnPoint('3.3.c0', 2.8, 2.8, ['3.3.f0'], 0, True),
		SpawnPoint('3.3.f0', 2.8, 2.95, ['2.3.i2', '3.3.i0'], 1, True),
		SpawnPoint('3.3.i0', 2.8, 3.05, ['3.3.c1'], 0, False),
		SpawnPoint('3.3.c1', 2.8, 3.2, ['3.3.f1'], 0, True),
		SpawnPoint('3.3.f1', 2.95, 3.2, ['3.4.i3', '3.3.i1'], 1, True),
		SpawnPoint('3.3.i1', 3.05, 3.2, ['3.3.c2'], 0, False),
		SpawnPoint('3.3.c2', 3.2, 3.2, ['3.3.f2'], 0, True),
		SpawnPoint('3.3.f2', 3.2, 3.05, ['4.3.i0', '3.3.i2'], 1, True),
		SpawnPoint('3.3.i2', 3.2, 2.95, ['3.3.c3'], 0, False),
		SpawnPoint('3.3.c3', 3.2, 2.8, ['3.3.f3'], 0, True),
		SpawnPoint('3.3.f3', 3.05, 2.8, ['3.2.i1', '3.3.i3'], 1, True),
		SpawnPoint('3.3.i3', 2.95, 2.8, ['3.3.c0'], 0, False),

		SpawnPoint('4.3.c0', 3.8, 2.8, ['4.3.f0'], 0, True),
		SpawnPoint('4.3.f0', 3.8, 2.95, ['3.3.i2', '4.3.i0'], 1, True),
		SpawnPoint('4.3.i0', 3.8, 3.05, ['4.3.c1'], 0, False),
		SpawnPoint('4.3.c1', 3.8, 3.2, ['4.3.f1'], 0, True),
		SpawnPoint('4.3.f1', 3.95, 3.2, ['4.4.i3', '4.3.i1'], 1, True),
		SpawnPoint('4.3.i1', 4.05, 3.2, ['4.3.c2'], 0, False),
		SpawnPoint('4.3.c2', 4.2, 3.2, ['4.3.f2'], 0, True),
		SpawnPoint('4.3.f2', 4.2, 3.05, ['5.3.i0', '4.3.i2'], 1, True),
		SpawnPoint('4.3.i2', 4.2, 2.95, ['4.3.c3'], 0, False),
		SpawnPoint('4.3.c3', 4.2, 2.8, ['4.3.f3'], 0, True),
		SpawnPoint('4.3.f3', 4.05, 2.8, ['4.2.i1', '4.3.i3'], 1, True),
		SpawnPoint('4.3.i3', 3.95, 2.8, ['4.3.c0'], 0, False),

		SpawnPoint('5.3.c0', 4.8, 2.8, ['5.3.f0'], 0, True),
		SpawnPoint('5.3.f0', 4.8, 2.95, ['4.3.i2', '5.3.i0'], 1, True),
		SpawnPoint('5.3.i0', 4.8, 3.05, ['5.3.c1'], 0, False),
		SpawnPoint('5.3.c1', 4.8, 3.2, ['5.3.f1'], 0, True),
		SpawnPoint('5.3.f1', 4.95, 3.2, ['5.4.i3', '5.3.i1'], 1, True),
		SpawnPoint('5.3.i1', 5.05, 3.2, ['5.3.c2'], 0, False),
		SpawnPoint('5.3.c2', 5.2, 3.2, ['5.3.c3'], 0, True),
		SpawnPoint('5.3.c3', 5.2, 2.8, ['5.3.f3'], 0, True),
		SpawnPoint('5.3.f3', 5.05, 2.8, ['5.2.i1', '5.3.i3'], 1, True),
		SpawnPoint('5.3.i3', 4.95, 2.8, ['5.3.c0'], 0, False),

		SpawnPoint('0.4.c0', -0.2, 3.8, ['0.4.c1'], 0, True),
		SpawnPoint('0.4.c1', -0.2, 4.2, ['0.4.f1'], 0, True),
		SpawnPoint('0.4.f1', -0.05, 4.2, ['0.5.i3', '0.4.i1'], 1, True),
		SpawnPoint('0.4.i1', 0.05, 4.2, ['0.4.c2'], 0, False),
		SpawnPoint('0.4.c2', 0.2, 4.2, ['0.4.f2'], 0, True),
		SpawnPoint('0.4.f2', 0.2, 4.05, ['1.4.i0', '0.4.i2'], 1, True),
		SpawnPoint('0.4.i2', 0.2, 3.95, ['0.4.c3'], 0, False),
		SpawnPoint('0.4.c3', 0.2, 3.8, ['0.4.f3'], 0, True),
		SpawnPoint('0.4.f3', 0.05, 3.8, ['0.3.i1', '0.4.i3'], 1, True),
		SpawnPoint('0.4.i3', -0.05, 3.8, ['0.4.c0'], 0, False),

		SpawnPoint('1.4.c0', 0.8, 3.8, ['1.4.f0'], 0, True),
		SpawnPoint('1.4.f0', 0.8, 3.95, ['0.4.i2', '1.4.i0'], 1, True),
		SpawnPoint('1.4.i0', 0.8, 4.05, ['1.4.c1'], 0, False),
		SpawnPoint('1.4.c1', 0.8, 4.2, ['1.4.f1'], 0, True),
		SpawnPoint('1.4.f1', 0.95, 4.2, ['1.5.i3', '1.4.i1'], 1, True),
		SpawnPoint('1.4.i1', 1.05, 4.2, ['1.4.c2'], 0, False),
		SpawnPoint('1.4.c2', 1.2, 4.2, ['1.4.f2'], 0, True),
		SpawnPoint('1.4.f2', 1.2, 4.05, ['2.4.i0', '1.4.i2'], 1, True),
		SpawnPoint('1.4.i2', 1.2, 3.95, ['1.4.c3'], 0, False),
		SpawnPoint('1.4.c3', 1.2, 3.8, ['1.4.f3'], 0, True),
		SpawnPoint('1.4.f3', 1.05, 3.8, ['1.3.i1', '1.4.i3'], 1, True),
		SpawnPoint('1.4.i3', 0.95, 3.8, ['1.4.c0'], 0, False),

		SpawnPoint('2.4.c0', 1.8, 3.8, ['2.4.f0'], 0, True),
		SpawnPoint('2.4.f0', 1.8, 3.95, ['1.4.i2', '2.4.i0'], 1, True),
		SpawnPoint('2.4.i0', 1.8, 4.05, ['2.4.c1'], 0, False),
		SpawnPoint('2.4.c1', 1.8, 4.2, ['2.4.f1'], 0, True),
		SpawnPoint('2.4.f1', 1.95, 4.2, ['2.5.i3', '2.4.i1'], 1, True),
		SpawnPoint('2.4.i1', 2.05, 4.2, ['2.4.c2'], 0, False),
		SpawnPoint('2.4.c2', 2.2, 4.2, ['2.4.f2'], 0, True),
		SpawnPoint('2.4.f2', 2.2, 4.05, ['3.4.i0', '2.4.i2'], 1, True),
		SpawnPoint('2.4.i2', 2.2, 3.95, ['2.4.c3'], 0, False),
		SpawnPoint('2.4.c3', 2.2, 3.8, ['2.4.f3'], 0, True),
		SpawnPoint('2.4.f3', 2.05, 3.8, ['2.3.i1', '2.4.i3'], 1, True),
		SpawnPoint('2.4.i3', 1.95, 3.8, ['2.4.c0'], 0, False),

		SpawnPoint('3.4.c0', 2.8, 3.8, ['3.4.f0'], 0, True),
		SpawnPoint('3.4.f0', 2.8, 3.95, ['2.4.i2', '3.4.i0'], 1, True),
		SpawnPoint('3.4.i0', 2.8, 4.05, ['3.4.c1'], 0, False),
		SpawnPoint('3.4.c1', 2.8, 4.2, ['3.4.f1'], 0, True),
		SpawnPoint('3.4.f1', 2.95, 4.2, ['3.5.i3', '3.4.i1'], 1, True),
		SpawnPoint('3.4.i1', 3.05, 4.2, ['3.4.c2'], 0, False),
		SpawnPoint('3.4.c2', 3.2, 4.2, ['3.4.f2'], 0, True),
		SpawnPoint('3.4.f2', 3.2, 4.05, ['4.4.i0', '3.4.i2'], 1, True),
		SpawnPoint('3.4.i2', 3.2, 3.95, ['3.4.c3'], 0, False),
		SpawnPoint('3.4.c3', 3.2, 3.8, ['3.4.f3'], 0, True),
		SpawnPoint('3.4.f3', 3.05, 3.8, ['3.3.i1', '3.4.i3'], 1, True),
		SpawnPoint('3.4.i3', 2.95, 3.8, ['3.4.c0'], 0, False),

		SpawnPoint('4.4.c0', 3.8, 3.8, ['4.4.f0'], 0, True),
		SpawnPoint('4.4.f0', 3.8, 3.95, ['3.4.i2', '4.4.i0'], 1, True),
		SpawnPoint('4.4.i0', 3.8, 4.05, ['4.4.c1'], 0, False),
		SpawnPoint('4.4.c1', 3.8, 4.2, ['4.4.f1'], 0, True),
		SpawnPoint('4.4.f1', 3.95, 4.2, ['4.5.i3', '4.4.i1'], 1, True),
		SpawnPoint('4.4.i1', 4.05, 4.2, ['4.4.c2'], 0, False),
		SpawnPoint('4.4.c2', 4.2, 4.2, ['4.4.f2'], 0, True),
		SpawnPoint('4.4.f2', 4.2, 4.05, ['5.4.i0', '4.4.i2'], 1, True),
		SpawnPoint('4.4.i2', 4.2, 3.95, ['4.4.c3'], 0, False),
		SpawnPoint('4.4.c3', 4.2, 3.8, ['4.4.f3'], 0, True),
		SpawnPoint('4.4.f3', 4.05, 3.8, ['4.3.i1', '4.4.i3'], 1, True),
		SpawnPoint('4.4.i3', 3.95, 3.8, ['4.4.c0'], 0, False),

		SpawnPoint('5.4.c0', 4.8, 3.8, ['5.4.f0'], 0, True),
		SpawnPoint('5.4.f0', 4.8, 3.95, ['4.4.i2', '5.4.i0'], 1, True),
		SpawnPoint('5.4.i0', 4.8, 4.05, ['5.4.c1'], 0, False),
		SpawnPoint('5.4.c1', 4.8, 4.2, ['5.4.f1'], 0, True),
		SpawnPoint('5.4.f1', 4.95, 4.2, ['5.5.i3', '5.4.i1'], 1, True),
		SpawnPoint('5.4.i1', 5.05, 4.2, ['5.4.c2'], 0, False),
		SpawnPoint('5.4.c2', 5.2, 4.2, ['5.4.c3'], 0, True),
		SpawnPoint('5.4.c3', 5.2, 3.8, ['5.4.f3'], 0, True),
		SpawnPoint('5.4.f3', 5.05, 3.8, ['5.3.i1', '5.4.i3'], 1, True),
		SpawnPoint('5.4.i3', 4.95, 3.8, ['5.4.c0'], 0, False),

		SpawnPoint('0.5.c0', -0.2, 4.8, ['0.5.c1'], 0, True),
		SpawnPoint('0.5.c1', -0.2, 5.2, ['0.5.c2'], 0, True),
		SpawnPoint('0.5.c2', 0.2, 5.2, ['0.5.f2'], 0, True),
		SpawnPoint('0.5.f2', 0.2, 5.05, ['1.5.i0', '0.5.i2'], 1, True),
		SpawnPoint('0.5.i2', 0.2, 4.95, ['0.5.c3'], 0, False),
		SpawnPoint('0.5.c3', 0.2, 4.8, ['0.5.f3'], 0, True),
		SpawnPoint('0.5.f3', 0.05, 4.8, ['0.4.i1', '0.5.i3'], 1, True),
		SpawnPoint('0.5.i3', -0.05, 4.8, ['0.5.c0'], 0, False),

		SpawnPoint('1.5.c0', 0.8, 4.8, ['1.5.f0'], 0, True),
		SpawnPoint('1.5.f0', 0.8, 4.95, ['0.5.i2', '1.5.i0'], 1, True),
		SpawnPoint('1.5.i0', 0.8, 5.05, ['1.5.c1'], 0, False),
		SpawnPoint('1.5.c1', 0.8, 5.2, ['1.5.c2'], 0, True),
		SpawnPoint('1.5.c2', 1.2, 5.2, ['1.5.f2'], 0, True),
		SpawnPoint('1.5.f2', 1.2, 5.05, ['2.5.i0', '1.5.i2'], 1, True),
		SpawnPoint('1.5.i2', 1.2, 4.95, ['1.5.c3'], 0, False),
		SpawnPoint('1.5.c3', 1.2, 4.8, ['1.5.f3'], 0, True),
		SpawnPoint('1.5.f3', 1.05, 4.8, ['1.4.i1', '1.5.i3'], 1, True),
		SpawnPoint('1.5.i3', 0.95, 4.8, ['1.5.c0'], 0, False),

		SpawnPoint('2.5.c0', 1.8, 4.8, ['2.5.f0'], 0, True),
		SpawnPoint('2.5.f0', 1.8, 4.95, ['1.5.i2', '2.5.i0'], 1, True),
		SpawnPoint('2.5.i0', 1.8, 5.05, ['2.5.c1'], 0, False),
		SpawnPoint('2.5.c1', 1.8, 5.2, ['2.5.c2'], 0, True),
		SpawnPoint('2.5.c2', 2.2, 5.2, ['2.5.f2'], 0, True),
		SpawnPoint('2.5.f2', 2.2, 5.05, ['3.5.i0', '2.5.i2'], 1, True),
		SpawnPoint('2.5.i2', 2.2, 4.95, ['2.5.c3'], 0, False),
		SpawnPoint('2.5.c3', 2.2, 4.8, ['2.5.f3'], 0, True),
		SpawnPoint('2.5.f3', 2.05, 4.8, ['2.4.i1', '2.5.i3'], 1, True),
		SpawnPoint('2.5.i3', 1.95, 4.8, ['2.5.c0'], 0, False),

		SpawnPoint('3.5.c0', 2.8, 4.8, ['3.5.f0'], 0, True),
		SpawnPoint('3.5.f0', 2.8, 4.95, ['2.5.i2', '3.5.i0'], 1, True),
		SpawnPoint('3.5.i0', 2.8, 5.05, ['3.5.c1'], 0, False),
		SpawnPoint('3.5.c1', 2.8, 5.2, ['3.5.c2'], 0, True),
		SpawnPoint('3.5.c2', 3.2, 5.2, ['3.5.f2'], 0, True),
		SpawnPoint('3.5.f2', 3.2, 5.05, ['4.5.i0', '3.5.i2'], 1, True),
		SpawnPoint('3.5.i2', 3.2, 4.95, ['3.5.c3'], 0, False),
		SpawnPoint('3.5.c3', 3.2, 4.8, ['3.5.f3'], 0, True),
		SpawnPoint('3.5.f3', 3.05, 4.8, ['3.4.i1', '3.5.i3'], 1, True),
		SpawnPoint('3.5.i3', 2.95, 4.8, ['3.5.c0'], 0, False),

		SpawnPoint('4.5.c0', 3.8, 4.8, ['4.5.f0'], 0, True),
		SpawnPoint('4.5.f0', 3.8, 4.95, ['3.5.i2', '4.5.i0'], 1, True),
		SpawnPoint('4.5.i0', 3.8, 5.05, ['4.5.c1'], 0, False),
		SpawnPoint('4.5.c1', 3.8, 5.2, ['4.5.c2'], 0, True),
		SpawnPoint('4.5.c2', 4.2, 5.2, ['4.5.f2'], 0, True),
		SpawnPoint('4.5.f2', 4.2, 5.05, ['5.5.i0', '4.5.i2'], 1, True),
		SpawnPoint('4.5.i2', 4.2, 4.95, ['4.5.c3'], 0, False),
		SpawnPoint('4.5.c3', 4.2, 4.8, ['4.5.f3'], 0, True),
		SpawnPoint('4.5.f3', 4.05, 4.8, ['4.4.i1', '4.5.i3'], 1, True),
		SpawnPoint('4.5.i3', 3.95, 4.8, ['4.5.c0'], 0, False),

		SpawnPoint('5.5.c0', 4.8, 4.8, ['5.5.f0'], 0, True),
		SpawnPoint('5.5.f0', 4.8, 4.95, ['4.5.i2', '5.5.i0'], 1, True),
		SpawnPoint('5.5.i0', 4.8, 5.05, ['5.5.c1'], 0, False),
		SpawnPoint('5.5.c1', 4.8, 5.2, ['5.5.c2'], 0, True),
		SpawnPoint('5.5.c2', 5.2, 5.2, ['5.5.c3'], 0, True),
		SpawnPoint('5.5.c3', 5.2, 4.8, ['5.5.f3'], 0, True),
		SpawnPoint('5.5.f3', 5.05, 4.8, ['5.4.i1', '5.5.i3'], 1, True),
		SpawnPoint('5.5.i3', 4.95, 4.8, ['5.5.c0'], 0, False),


	],

	[
		300,

		SpawnPoint('0.0.a', 0.1, 0.1, ['0.0.b', '1.0.d'], 1, False),
		SpawnPoint('0.0.b', 0.1, -0.1, ['0.0.c'], 1, False),
		SpawnPoint('0.0.c', -0.1, -0.1, ['0.0.d'], 1, False),
		SpawnPoint('0.0.d', -0.1, 0.1, ['0.0.a', '0.1.c'], 1, False),

		SpawnPoint('1.0.a', 1.1, 0.1, ['1.0.b', '2.0.d'], 1, False),
		SpawnPoint('1.0.b', 1.1, -0.1, ['1.0.c'], 1, False),
		SpawnPoint('1.0.c', 0.9, -0.1, ['1.0.d', '0.0.b'], 1, False),
		SpawnPoint('1.0.d', 0.9, 0.1, ['1.0.a', '1.1.c'], 1, False),

		SpawnPoint('2.0.a', 2.1, 0.1, ['2.0.b', '3.0.d'], 1, False),
		SpawnPoint('2.0.b', 2.1, -0.1, ['2.0.c'], 1, False),
		SpawnPoint('2.0.c', 1.9, -0.1, ['2.0.d', '1.0.b'], 1, False),
		SpawnPoint('2.0.d', 1.9, 0.1, ['2.0.a', '2.1.c'], 1, False),

		SpawnPoint('3.0.a', 3.1, 0.1, ['3.0.b', '4.0.d'], 1, False),
		SpawnPoint('3.0.b', 3.1, -0.1, ['3.0.c'], 1, False),
		SpawnPoint('3.0.c', 2.9, -0.1, ['3.0.d', '2.0.b'], 1, False),
		SpawnPoint('3.0.d', 2.9, 0.1, ['3.0.a', '3.1.c'], 1, False),

		SpawnPoint('4.0.a', 4.1, 0.1, ['4.0.b', '5.0.d'], 1, False),
		SpawnPoint('4.0.b', 4.1, -0.1, ['4.0.c'], 1, False),
		SpawnPoint('4.0.c', 3.9, -0.1, ['4.0.d', '3.0.b'], 1, False),
		SpawnPoint('4.0.d', 3.9, 0.1, ['4.0.a', '4.1.c'], 1, False),

		SpawnPoint('5.0.a', 5.1, 0.1, ['5.0.b'], 1, False),
		SpawnPoint('5.0.b', 5.1, -0.1, ['5.0.c'], 1, False),
		SpawnPoint('5.0.c', 4.9, -0.1, ['5.0.d', '4.0.b'], 1, False),
		SpawnPoint('5.0.d', 4.9, 0.1, ['5.0.a', '5.1.c'], 1, False),

		SpawnPoint('0.1.a', 0.1, 1.1, ['0.1.b', '1.1.d'], 1, False),
		SpawnPoint('0.1.b', 0.1, 0.9, ['0.1.c', '0.0.a'], 1, False),
		SpawnPoint('0.1.c', -0.1, 0.9, ['0.1.d'], 1, False),
		SpawnPoint('0.1.d', -0.1, 1.1, ['0.1.a', '0.2.c'], 1, False),

		SpawnPoint('1.1.a', 1.1, 1.1, ['1.1.b', '2.1.d'], 1, False),
		SpawnPoint('1.1.b', 1.1, 0.9, ['1.1.c', '1.0.a'], 1, False),
		SpawnPoint('1.1.c', 0.9, 0.9, ['1.1.d', '0.1.b'], 1, False),
		SpawnPoint('1.1.d', 0.9, 1.1, ['1.1.a', '1.2.c'], 1, False),

		SpawnPoint('2.1.a', 2.1, 1.1, ['2.1.b', '3.1.d'], 1, False),
		SpawnPoint('2.1.b', 2.1, 0.9, ['2.1.c', '2.0.a'], 1, False),
		SpawnPoint('2.1.c', 1.9, 0.9, ['2.1.d', '1.1.b'], 1, False),
		SpawnPoint('2.1.d', 1.9, 1.1, ['2.1.a', '2.2.c'], 1, False),

		SpawnPoint('3.1.a', 3.1, 1.1, ['3.1.b', '4.1.d'], 1, False),
		SpawnPoint('3.1.b', 3.1, 0.9, ['3.1.c', '3.0.a'], 1, False),
		SpawnPoint('3.1.c', 2.9, 0.9, ['3.1.d', '2.1.b'], 1, False),
		SpawnPoint('3.1.d', 2.9, 1.1, ['3.1.a', '3.2.c'], 1, False),

		SpawnPoint('4.1.a', 4.1, 1.1, ['4.1.b', '5.1.d'], 1, False),
		SpawnPoint('4.1.b', 4.1, 0.9, ['4.1.c', '4.0.a'], 1, False),
		SpawnPoint('4.1.c', 3.9, 0.9, ['4.1.d', '3.1.b'], 1, False),
		SpawnPoint('4.1.d', 3.9, 1.1, ['4.1.a', '4.2.c'], 1, False),

		SpawnPoint('5.1.a', 5.1, 1.1, ['5.1.b'], 1, False),
		SpawnPoint('5.1.b', 5.1, 0.9, ['5.1.c', '5.0.a'], 1, False),
		SpawnPoint('5.1.c', 4.9, 0.9, ['5.1.d', '4.1.b'], 1, False),
		SpawnPoint('5.1.d', 4.9, 1.1, ['5.1.a', '5.2.c'], 1, False),

		SpawnPoint('0.2.a', 0.1, 2.1, ['0.2.b', '1.2.d'], 1, False),
		SpawnPoint('0.2.b', 0.1, 1.9, ['0.2.c', '0.1.a'], 1, False),
		SpawnPoint('0.2.c', -0.1, 1.9, ['0.2.d'], 1, False),
		SpawnPoint('0.2.d', -0.1, 2.1, ['0.2.a', '0.3.c'], 1, False),

		SpawnPoint('1.2.a', 1.1, 2.1, ['1.2.b', '2.2.d'], 1, False),
		SpawnPoint('1.2.b', 1.1, 1.9, ['1.2.c', '1.1.a'], 1, False),
		SpawnPoint('1.2.c', 0.9, 1.9, ['1.2.d', '0.2.b'], 1, False),
		SpawnPoint('1.2.d', 0.9, 2.1, ['1.2.a', '1.3.c'], 1, False),

		SpawnPoint('2.2.a', 2.1, 2.1, ['2.2.b', '3.2.d'], 1, False),
		SpawnPoint('2.2.b', 2.1, 1.9, ['2.2.c', '2.1.a'], 1, False),
		SpawnPoint('2.2.c', 1.9, 1.9, ['2.2.d', '1.2.b'], 1, False),
		SpawnPoint('2.2.d', 1.9, 2.1, ['2.2.a', '2.3.c'], 1, False),

		SpawnPoint('3.2.a', 3.1, 2.1, ['3.2.b', '4.2.d'], 1, False),
		SpawnPoint('3.2.b', 3.1, 1.9, ['3.2.c', '3.1.a'], 1, False),
		SpawnPoint('3.2.c', 2.9, 1.9, ['3.2.d', '2.2.b'], 1, False),
		SpawnPoint('3.2.d', 2.9, 2.1, ['3.2.a', '3.3.c'], 1, False),

		SpawnPoint('4.2.a', 4.1, 2.1, ['4.2.b', '5.2.d'], 1, False),
		SpawnPoint('4.2.b', 4.1, 1.9, ['4.2.c', '4.1.a'], 1, False),
		SpawnPoint('4.2.c', 3.9, 1.9, ['4.2.d', '3.2.b'], 1, False),
		SpawnPoint('4.2.d', 3.9, 2.1, ['4.2.a', '4.3.c'], 1, False),

		SpawnPoint('5.2.a', 5.1, 2.1, ['5.2.b'], 1, False),
		SpawnPoint('5.2.b', 5.1, 1.9, ['5.2.c', '5.1.a'], 1, False),
		SpawnPoint('5.2.c', 4.9, 1.9, ['5.2.d', '4.2.b'], 1, False),
		SpawnPoint('5.2.d', 4.9, 2.1, ['5.2.a', '5.3.c'], 1, False),

		SpawnPoint('0.3.a', 0.1, 3.1, ['0.3.b', '1.3.d'], 1, False),
		SpawnPoint('0.3.b', 0.1, 2.9, ['0.3.c', '0.2.a'], 1, False),
		SpawnPoint('0.3.c', -0.1, 2.9, ['0.3.d'], 1, False),
		SpawnPoint('0.3.d', -0.1, 3.1, ['0.3.a', '0.4.c'], 1, False),

		SpawnPoint('1.3.a', 1.1, 3.1, ['1.3.b', '2.3.d'], 1, False),
		SpawnPoint('1.3.b', 1.1, 2.9, ['1.3.c', '1.2.a'], 1, False),
		SpawnPoint('1.3.c', 0.9, 2.9, ['1.3.d', '0.3.b'], 1, False),
		SpawnPoint('1.3.d', 0.9, 3.1, ['1.3.a', '1.4.c'], 1, False),

		SpawnPoint('2.3.a', 2.1, 3.1, ['2.3.b', '3.3.d'], 1, False),
		SpawnPoint('2.3.b', 2.1, 2.9, ['2.3.c', '2.2.a'], 1, False),
		SpawnPoint('2.3.c', 1.9, 2.9, ['2.3.d', '1.3.b'], 1, False),
		SpawnPoint('2.3.d', 1.9, 3.1, ['2.3.a', '2.4.c'], 1, False),

		SpawnPoint('3.3.a', 3.1, 3.1, ['3.3.b', '4.3.d'], 1, False),
		SpawnPoint('3.3.b', 3.1, 2.9, ['3.3.c', '3.2.a'], 1, False),
		SpawnPoint('3.3.c', 2.9, 2.9, ['3.3.d', '2.3.b'], 1, False),
		SpawnPoint('3.3.d', 2.9, 3.1, ['3.3.a', '3.4.c'], 1, False),

		SpawnPoint('4.3.a', 4.1, 3.1, ['4.3.b', '5.3.d'], 1, False),
		SpawnPoint('4.3.b', 4.1, 2.9, ['4.3.c', '4.2.a'], 1, False),
		SpawnPoint('4.3.c', 3.9, 2.9, ['4.3.d', '3.3.b'], 1, False),
		SpawnPoint('4.3.d', 3.9, 3.1, ['4.3.a', '4.4.c'], 1, False),

		SpawnPoint('5.3.a', 5.1, 3.1, ['5.3.b'], 1, False),
		SpawnPoint('5.3.b', 5.1, 2.9, ['5.3.c', '5.2.a'], 1, False),
		SpawnPoint('5.3.c', 4.9, 2.9, ['5.3.d', '4.3.b'], 1, False),
		SpawnPoint('5.3.d', 4.9, 3.1, ['5.3.a', '5.4.c'], 1, False),

		SpawnPoint('0.4.a', 0.1, 4.1, ['0.4.b', '1.4.d'], 1, False),
		SpawnPoint('0.4.b', 0.1, 3.9, ['0.4.c', '0.3.a'], 1, False),
		SpawnPoint('0.4.c', -0.1, 3.9, ['0.4.d'], 1, False),
		SpawnPoint('0.4.d', -0.1, 4.1, ['0.4.a', '0.5.c'], 1, False),

		SpawnPoint('1.4.a', 1.1, 4.1, ['1.4.b', '2.4.d'], 1, False),
		SpawnPoint('1.4.b', 1.1, 3.9, ['1.4.c', '1.3.a'], 1, False),
		SpawnPoint('1.4.c', 0.9, 3.9, ['1.4.d', '0.4.b'], 1, False),
		SpawnPoint('1.4.d', 0.9, 4.1, ['1.4.a', '1.5.c'], 1, False),

		SpawnPoint('2.4.a', 2.1, 4.1, ['2.4.b', '3.4.d'], 1, False),
		SpawnPoint('2.4.b', 2.1, 3.9, ['2.4.c', '2.3.a'], 1, False),
		SpawnPoint('2.4.c', 1.9, 3.9, ['2.4.d', '1.4.b'], 1, False),
		SpawnPoint('2.4.d', 1.9, 4.1, ['2.4.a', '2.5.c'], 1, False),

		SpawnPoint('3.4.a', 3.1, 4.1, ['3.4.b', '4.4.d'], 1, False),
		SpawnPoint('3.4.b', 3.1, 3.9, ['3.4.c', '3.3.a'], 1, False),
		SpawnPoint('3.4.c', 2.9, 3.9, ['3.4.d', '2.4.b'], 1, False),
		SpawnPoint('3.4.d', 2.9, 4.1, ['3.4.a', '3.5.c'], 1, False),

		SpawnPoint('4.4.a', 4.1, 4.1, ['4.4.b', '5.4.d'], 1, False),
		SpawnPoint('4.4.b', 4.1, 3.9, ['4.4.c', '4.3.a'], 1, False),
		SpawnPoint('4.4.c', 3.9, 3.9, ['4.4.d', '3.4.b'], 1, False),
		SpawnPoint('4.4.d', 3.9, 4.1, ['4.4.a', '4.5.c'], 1, False),

		SpawnPoint('5.4.a', 5.1, 4.1, ['5.4.b'], 1, False),
		SpawnPoint('5.4.b', 5.1, 3.9, ['5.4.c', '5.3.a'], 1, False),
		SpawnPoint('5.4.c', 4.9, 3.9, ['5.4.d', '4.4.b'], 1, False),
		SpawnPoint('5.4.d', 4.9, 4.1, ['5.4.a', '5.5.c'], 1, False),

		SpawnPoint('0.5.a', 0.1, 5.1, ['0.5.b', '1.5.d'], 1, False),
		SpawnPoint('0.5.b', 0.1, 4.9, ['0.5.c', '0.4.a'], 1, False),
		SpawnPoint('0.5.c', -0.1, 4.9, ['0.5.d'], 1, False),
		SpawnPoint('0.5.d', -0.1, 5.1, ['0.5.a'], 1, False),

		SpawnPoint('1.5.a', 1.1, 5.1, ['1.5.b', '2.5.d'], 1, False),
		SpawnPoint('1.5.b', 1.1, 4.9, ['1.5.c', '1.4.a'], 1, False),
		SpawnPoint('1.5.c', 0.9, 4.9, ['1.5.d', '0.5.b'], 1, False),
		SpawnPoint('1.5.d', 0.9, 5.1, ['1.5.a'], 1, False),

		SpawnPoint('2.5.a', 2.1, 5.1, ['2.5.b', '3.5.d'], 1, False),
		SpawnPoint('2.5.b', 2.1, 4.9, ['2.5.c', '2.4.a'], 1, False),
		SpawnPoint('2.5.c', 1.9, 4.9, ['2.5.d', '1.5.b'], 1, False),
		SpawnPoint('2.5.d', 1.9, 5.1, ['2.5.a'], 1, False),

		SpawnPoint('3.5.a', 3.1, 5.1, ['3.5.b', '4.5.d'], 1, False),
		SpawnPoint('3.5.b', 3.1, 4.9, ['3.5.c', '3.4.a'], 1, False),
		SpawnPoint('3.5.c', 2.9, 4.9, ['3.5.d', '2.5.b'], 1, False),
		SpawnPoint('3.5.d', 2.9, 5.1, ['3.5.a'], 1, False),

		SpawnPoint('4.5.a', 4.1, 5.1, ['4.5.b', '5.5.d'], 1, False),
		SpawnPoint('4.5.b', 4.1, 4.9, ['4.5.c', '4.4.a'], 1, False),
		SpawnPoint('4.5.c', 3.9, 4.9, ['4.5.d', '3.5.b'], 1, False),
		SpawnPoint('4.5.d', 3.9, 5.1, ['4.5.a'], 1, False),

		SpawnPoint('5.5.a', 5.1, 5.1, ['5.5.b'], 1, False),
		SpawnPoint('5.5.b', 5.1, 4.9, ['5.5.c', '5.4.a'], 1, False),
		SpawnPoint('5.5.c', 4.9, 4.9, ['5.5.d', '4.5.b'], 1, False),
		SpawnPoint('5.5.d', 4.9, 5.1, ['5.5.a'], 1, False),


	]

	

]





#pointst = [
 #	SpawnPoint("A1",  50, 50, ["B1"]),
 #	SpawnPoint("A2",  50, 400, ["A1", "B2"]),
#
 #	SpawnPoint("B1", 300, 50, ["C1", "B2"]),
 #	SpawnPoint("B2", 250, 200, ["A2", "A1"]),
 #	SpawnPoint("B3", 300, 400, ["A2", "B2"], 3),
#
 #	SpawnPoint("C1", 750, 50, ["C2"]),
 #	SpawnPoint("C2", 750, 200, ["B3", "B2"]),
 #]









# Thanks chatgpt
def angle_oriente(A, O, B):
	# Vecteurs OA et OB
	OA = np.array([A.x - O.x, A.y - O.y])
	OB = np.array([B.x - O.x, B.y - O.y])
	
	# Produit scalaire et norme des vecteurs
	dot_product = np.dot(OA, OB)
	norm_OA = np.linalg.norm(OA)
	norm_OB = np.linalg.norm(OB)
	
	# Calcul de l'angle en radians
	cos_theta = dot_product / (norm_OA * norm_OB)
	theta = np.arccos(np.clip(cos_theta, -1.0, 1.0))
	
	# Déterminer le signe de l'angle avec le produit vectoriel
	cross_product = np.cross(OA, OB)
	if cross_product < 0:
		theta = 2 * np.pi - theta  # Ajuster l'angle pour qu'il soit dans [0, 2π[
	
	return theta



def generateWaitFor(center: Intersection, origin: Intersection, target: Intersection, rightPriority):
	waitFor = []

	for index in range(len(center.origins)):
		i: Intersection = center.origins[index]
		if i == origin or i == target:
			continue


		angle = angle_oriente(origin, center, i)

		if rightPriority:
			if angle > np.pi:
				waitFor.append(index)
			elif angle == np.pi:
				# Case of equality
				if origin.x < i.x or (origin.x == i.x and origin.y > i.y):
					waitFor.append(index)
		
		else:
			if angle < np.pi:
				waitFor.append(index)
			elif angle == np.pi:
				# Case of equality
				if origin.x > i.x or (origin.x == i.x and origin.y < i.y):
					waitFor.append(index)
		
			

	return waitFor




def generateMap(points):
	zoom = points[0]
	if isinstance(zoom, (int, float)):
		points.pop(0)
	else:
		zoom = 1

	length = len(points)
	intersections: list[Intersection] = []


	# Generate intersections
	for i in points:
		intersections.append(Intersection(
			i.x * zoom,
			i.y * zoom,
			i.spawnScore
		))

	def getIndex(name: str):
		for i in range(length):
			if points[i].name == name:
				return i
		
		return -1
	
	
	# Fill targets
	for i in range(length):
		for toAdd in points[i].targets:
			index = getIndex(toAdd)
			if index == -1:
				print("WARNING: cannot find:", toAdd)
				raise "Cannot find token"
			
			intersections[i].targets.append(intersections[index])
			intersections[index].origins.append(intersections[i])
	

	# Generate priorities
	for centerIndex in range(len(intersections)):
		center = intersections[centerIndex]
		originLength = len(center.origins)
		targetLength = len(center.targets)
		
		for originIndex in range(originLength):
			arr: list[Priority] = []
			for targetIndex in range(targetLength):
				# Priorities to check
				if originLength < 2:
					waitFor = []
				else:
					waitFor = generateWaitFor(
						center,
						center.origins[originIndex],
						center.targets[targetIndex],
						points[centerIndex].rightPriority
					)
				

				# Create priority
				arr.append(Priority(targetIndex, TURN_DIST, waitFor))

			center.prios.append(arr)

	print("Map generated!")
	return intersections

