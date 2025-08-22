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
		







pointsList = [[
 	SpawnPoint("A1",  50, 50, ["B1"], 1, False),
 	SpawnPoint("A2",  50, 400, ["A1"]),

 	SpawnPoint("B1", 300, 50, ["C1", "B2"]),
 	SpawnPoint("B2", 250, 200, ["A2", "A1"]),
 	SpawnPoint("B3", 300, 400, ["A2", "B2"]),

 	SpawnPoint("C1", 750, 50, ["C2"]),
 	SpawnPoint("C2", 750, 200, ["B3", "B2"]),
 ]]









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

