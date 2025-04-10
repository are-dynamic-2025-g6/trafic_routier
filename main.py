# clear && python3 "main.py"

# mail: florentperez@sorbonne-universite.fr


from frameLaps import FRAME_LAPS


import pygame
import time

from intersection import INTERSECTION_SIZE
from methods import Car_getNextPriority
from methods import Car_frame
from methods import Car_spawn
from mapGenerator import generateMap, pointsList

import threading
import random
from math import sqrt

from car import Car

CAR_COUNT = 5


from Map import Map
from stats import *

mapList: list[Map] = []

for i in range(len(pointsList)):
	m = Map()
	m.intersections = generateMap(pointsList[i])
	m.cars = []

	length = len(m.intersections)-1
	for _ in range(CAR_COUNT):
		while True:
			i = random.randint(0, length)
			j = random.randint(0, length)

			if i == j:
				continue

			if m.intersections[i].spawnScore <= 0:
				continue

			if m.intersections[j].spawnScore <= 0:
				continue

			# i, j are valid
			break

		
		m.cars.append(
			Car(.1, m.intersections[i], m.intersections[j]),
		)


	m.setSize()
	mapList.append(m)




from stats import *

def runLap(map: Map):
	for car in map.cars:
		if car.isAlive(): # for debug
			Car_frame(map, car)
			car.move(map.params) # called every frame (because a car can't stop instantly)
			Stat_runLap(map)
		
		else:
			car.spawnCouldown -= 1
			if (car.spawnCouldown <= 0):
				car.spawnCouldown = -1
				finalTarget = map.createRandomFinalTarget()
				if Car_spawn(car, finalTarget):
					car.spawnLapCount = map.lapCount
					dx = finalTarget.x - car.origin.x
					dy = finalTarget.y - car.origin.y
					dist = sqrt(dx*dx + dy*dy)
					car.angryDuration = int(Car.ANGRY_UNIT * dist)



	map.lapCount += 1

	return None



def runMapList():
	for _ in range(FRAME_LAPS):
		for map in mapList:
			runLap(map)
			Stat_runLap(map)


	for map in mapList:
		for name in vars(map.stats):
			if name != "trajectDurations":
				getattr(map.stats, name).add()



class DrawObject:
	def __init__(self, map: Map):
		pygame.init()
		pygame.display.set_caption("Traffic rider")
		self.map = map
		self.screen = pygame.display.set_mode((1200, 1200))
		self.font = pygame.font.Font(None, 20)
		self.clock = pygame.time.Clock()
		
	def __del__(self):
		pygame.quit()


	def drawGame(self):
		# thanks chatgpt
		def drawArrow(color, start, end, percentage=0.8, arrow_size=10, thickness=1):
			# Calcul du point à "percentage%" du segment
			point_x = start[0] + percentage * (end[0] - start[0])
			point_y = start[1] + percentage * (end[1] - start[1])
			arrow_pos = (point_x, point_y)

			# Dessiner le segment
			pygame.draw.line(self.screen, color, start, end, thickness)

			# Calcul de la direction du segment
			direction = pygame.math.Vector2(end) - pygame.math.Vector2(start)
			direction = direction.normalize()

			# Calcul des points pour la flèche
			left = pygame.math.Vector2(-direction.y, direction.x) * arrow_size
			right = pygame.math.Vector2(direction.y, -direction.x) * arrow_size
			back = pygame.math.Vector2(-direction.x, -direction.y) * arrow_size

			arrow_tip = pygame.math.Vector2(arrow_pos)
			arrow_left = arrow_tip + back + left
			arrow_right = arrow_tip + back + right

			# Dessiner la flèche à 80% du segment
			pygame.draw.polygon(self.screen, color, [arrow_tip, arrow_left, arrow_right])



		

		# white background
		self.screen.fill((255, 255, 255))
		
		# draw roads (red)
		for i in self.map.intersections:
			for d in i.targets:
				drawArrow((63, 63, 63), (i.x, i.y), (d.x, d.y))
		
		# draw intersections (purple)
		for i in self.map.intersections:
			pygame.draw.rect(self.screen, (127, 0, 255), (i.x - INTERSECTION_SIZE/2, i.y - INTERSECTION_SIZE/2, INTERSECTION_SIZE, INTERSECTION_SIZE))



		# draw cars (green)
		for car in self.map.cars:
			x, y = car.getCoord()
			size = car.size
			halfSize = size/2

			if car.isAlive():
				if car.spawnLapCount == -1:
					color = (0, 127, 255)
				else:
					r = (self.map.lapCount - car.spawnLapCount)/car.angryDuration
					if r > 1:
						r = 1
					
					color = (
						int(255*r),
						int(255*(1-r)),
						0
					)

					
			else:
				color = (127, 127, 127)

			pygame.draw.rect(self.screen, color, (x - halfSize, y - halfSize, size, size))




running = True


def drawMapLoop(draw):
	global running
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for _ in range(2):
			runLap(draw.map)

		draw.drawGame()
		pygame.display.flip()  # Mettre à jour l'affichage
		draw.clock.tick(50)


	



# def loopAddCars():
# 	while running:
# 		time.sleep(.1)

# 		while True:
# 			i = random.randint(0, length)
# 			j = random.randint(0, length)

# 			if i != j:
# 				break
		
# 		map0.cars.append(
# 			Car(.1, map0.intersections[i], map0.intersections[j]),
# 		)

# threading.Thread(target=loopAddCars).start()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

USE_BARS = False

def mathThread():
	# Initialisation de dataList, une liste de tableaux de données
	dataList = [[0] for _ in range(len(mapList))]

	def fillList(propertyName):
		for i in range(len(mapList)):
			dataList[i] = getattr(mapList[i].stats, propertyName).list




	# Changement des donnees
	def mainFrame():
		runMapList()

		# TAG: runStatList
		# StatList_trajectDuration(mapList, dataList)
		# StatList_waitList(mapList, dataList)

		fillList("wait")
		



	# Fonction d'animation
	def update(frame):
		mainFrame()  # Met à jour les données dans dataList
		
		# Efface la figure actuelle avant de redessiner
		ax.clear()
		
		# Affiche chaque série de données dans dataList avec une couleur différente
		colors = ['r', 'g', 'b', 'c', 'm']  # Liste des couleurs à utiliser
		labels = [.5, .8, 1, 2, 3]

		if USE_BARS:
			for i, data in enumerate(dataList):
				ax.bar(np.arange(len(data)) + i * 0.2, data, width=0.2, color=colors[i % len(colors)], label=f'Data {i+1}')
		else:
			for i, data in enumerate(dataList):
				ax.plot(data, color=colors[i % len(colors)], label=f'Zoom {labels[i]}')
			

		# Réglages du graphique
		ax.set_title("Données en temps réel")
		ax.set_xlabel("Index")
		ax.set_ylabel("Valeur")
		ax.legend()

	# Création de la figure et des axes
	fig, ax = plt.subplots()

	# Animation avec FuncAnimation
	anim = FuncAnimation(fig, update, frames=1000, interval=100, repeat=False)

	# Affichage de l'animation
	plt.show()




# threading.Thread(target=mathThread).start()
drawMapLoop(DrawObject(mapList[0]))

# mathThread()

