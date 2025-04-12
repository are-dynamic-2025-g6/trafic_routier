# clear && python3 "mapGenerator.py"


from intersection import *
from car import *
from priority import Priority
import numpy as np


TURN_DIST = 6

class SpawnPoint:
	def __init__(self, name: str, x: float, y: float, targets: list[str], spawnScore: int = 1, rightPriority=True):
		self.x = x
		self.y = y
		self.name = name
		self.targets = targets
		self.spawnScore = spawnScore
		self.rightPriority = rightPriority
		




pointsList = [
	[
		.5,

		#SpawnPoint("N0", 1100,  600, ["C0"]),
		#SpawnPoint("N1",  600,  100, ["C1"]),
		#SpawnPoint("N2",  100,  600, ["C2"]),
		#SpawnPoint("N3",  600, 1100, ["C3"]),

		#SpawnPoint("C0", 700, 500, ["C1" ,"N1"], 0, False),
		#SpawnPoint("C1", 500, 500, ["C2", "N2"], 0, False),
		#SpawnPoint("C2", 500, 700, ["C3", "N3"], 0, False),
		#SpawnPoint("C3", 700, 700, ["C0", "N0"], 0, False),


		SpawnPoint("T1", 700, 1250, ["T6"], 0),
		SpawnPoint("T2", 1600, 1250, [ "T7"], 0),
		SpawnPoint("T3", 700, 1400, [ "T5"], 0),
		SpawnPoint("T4", 1600, 1400, [ "T8"], 0),
		SpawnPoint("T5", 700, 1325, [ "Y5", "T1"], 0),
		SpawnPoint("T6", 1150, 1250, [ "T2", "D7"], 0),
		SpawnPoint("T7", 1600, 1325, [ "T4", "E7"], 0),
		SpawnPoint("T8", 1150, 1400, [ "T3", "F8"], 0),




		SpawnPoint("Y1", 300, 1250, [ "Y7", "Y8"]),
		SpawnPoint("Y2", 450, 1250, ["Y5", "Y7"]),
		SpawnPoint("Y3", 300, 1400, [ "Y6", "Y8"]),
		SpawnPoint("Y4", 450, 1400, [ "Y6", "Y5"] ),
		SpawnPoint("Y5", 450, 1325, [ "T5", "Y4", "Y2", "Y9"],0 , True),
		SpawnPoint("Y6", 375, 1400, [ "Y3","Y4", "Y9"], True),
		SpawnPoint("Y7", 375, 1250, [ "Y1","Y2", "Y9" ],True),
		SpawnPoint("Y8", 300, 1325, [ "Y3", "Y1", "Y9"], True),
		SpawnPoint("Y9", 375,1325, [ "Y5", "Y6", "Y7", "Y8"], 0, True),



		SpawnPoint("D1", 1075, 1000, [ "D7", "D8"] ),
		SpawnPoint("D2", 1225, 1000, ["D7", "D6"] ),
		SpawnPoint("D3", 1075, 825, [ "D5", "D8"] ),
		SpawnPoint("D4", 1225, 825, [ "D5", "D6"]),
		SpawnPoint("D5", 1150, 825, ["D3", "D4", "D9"] ),
		SpawnPoint("D6", 1225, 900, ["D2", "D4", "D9"] ),
		SpawnPoint("D7", 1150,1000,[ "T6", "D1", "D2", "D9" ],0),
		SpawnPoint("D8", 1075, 900, [ "D1", "D3", "D9"]),
		SpawnPoint("D9", 1150,900, [ "D5", "D6", "D7", "D8"], 0),


		SpawnPoint("E1", 1850, 1250, [ "E7", "E8"],  ),
		SpawnPoint("E2", 1850, 1400, ["E7", "E6"],  ),
		SpawnPoint("E3", 2000, 1250, [ "E8", "E5"],  ),
		SpawnPoint("E4", 2000, 1400, [ "E6", "E5"], ),
		SpawnPoint("E5", 2000, 1325, ["E3", "E4", "E9"],  ),
		SpawnPoint("E6", 1925, 1400, ["E2", "E4", "E9"], ),
		SpawnPoint("E7", 1850,1325,[ "T7", "E1", "E2", "E9" ],0),
		SpawnPoint("E8", 1925,1250 , [ "E1", "E3", "E9"]),
		SpawnPoint("E9", 1925,1325, [ "E5", "E6", "E7", "E8" ], 0),




		SpawnPoint("F1", 1075, 1600, [ "F8", "F7"]  ),
		SpawnPoint("F2", 1225, 1600, ["F8", "F5"] ),
		SpawnPoint("F3", 1075, 1750, [ "F7", "F6"]  ),
		SpawnPoint("F4", 1225, 1750, [ "F6", "F5"] ),
		SpawnPoint("F5", 1225,1675, ["F2", "F4", "F9"] ),
		SpawnPoint("F6", 1150, 1750, ["F3", "F4", "F9"]),
		SpawnPoint("F7", 1075,1675,[ "F3", "F1", "F9" ]),
		SpawnPoint("F8", 1150,1600 , [ "F1", "F2", "F9", "T8"], 0),
		SpawnPoint("F9", 1150,1675, ["F5", "F6", "F7", "F8"], 0),


		




		



	],

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


	return intersections

