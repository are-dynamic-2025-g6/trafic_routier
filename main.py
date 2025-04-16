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

CAR_COUNT = 600



from Map import Map
from stats import *

mapList: list[Map] = []


def produceCars(m: Map):
	# return
	# time.sleep(3)

	length = len(m.intersections)-1
	for k in range(CAR_COUNT):
		
		if k > CAR_COUNT/3:
			time.sleep(2)
		elif k > 2*CAR_COUNT/3:
			time.sleep(4)
		else:
			time.sleep(1)

		print(k)


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
			Car(1, m.intersections[i], m.intersections[j]),
		)
		m.intersections[j].finalTargetCarCount += 1




for i in range(len(pointsList)):
	m = Map()
	m.intersections = generateMap(pointsList[i])
	m.cars = []
	m.setSize()
	mapList.append(m)

	threading.Thread(args=(m,), target=produceCars).start()



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
					finalTarget.finalTargetCarCount += 1
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
	def __init__(self, map: Map, dx, dy, zoom, drawArrow = True):
		pygame.init()
		pygame.display.set_caption("Traffic rider")
		self.map = map
		self.screen = pygame.display.set_mode((1200, 1200))
		self.font = pygame.font.Font(None, 20)
		self.clock = pygame.time.Clock()
		self.drawArrow = drawArrow

		self.offsetX = dx
		self.offsetY = dy
		self.zoom = zoom
		
	def __del__(self):
		pygame.quit()
	
	def drawGame(self):
		def applyZoom(x, y):
			# Applique le zoom et l'offset
			return (
				x * self.zoom + self.offsetX,
				y * self.zoom + self.offsetY
			)

		def drawArrow(color, start, end, percentage=0.8, arrow_size=10, thickness=1):
			# Appliquer zoom aux coordonnées
			start = applyZoom(*start)
			end = applyZoom(*end)

			# Calcul du point à "percentage%" du segment
			point_x = start[0] + percentage * (end[0] - start[0])
			point_y = start[1] + percentage * (end[1] - start[1])
			arrow_pos = (point_x, point_y)

			# Dessiner le segment
			pygame.draw.line(self.screen, color, start, end, thickness)


			if self.drawArrow:
				# Calcul de la direction du segment
				direction = pygame.math.Vector2(end) - pygame.math.Vector2(start)
				direction = direction.normalize()

				# Calcul des points pour la flèche
				left = pygame.math.Vector2(-direction.y, direction.x) * arrow_size * self.zoom
				right = pygame.math.Vector2(direction.y, -direction.x) * arrow_size * self.zoom
				back = pygame.math.Vector2(-direction.x, -direction.y) * arrow_size * self.zoom

				arrow_tip = pygame.math.Vector2(arrow_pos)
				arrow_left = arrow_tip + back + left
				arrow_right = arrow_tip + back + right

				# Dessiner la flèche
				pygame.draw.polygon(self.screen, color, [arrow_tip, arrow_left, arrow_right])
				
			


		# Effacer l’écran
		self.screen.fill((255, 255, 255))

		# Dessiner les routes
		for i in self.map.intersections:
			for d in i.targets:
				drawArrow((63, 63, 63), (i.x, i.y), (d.x, d.y))

		# Dessiner les intersections
		if self.drawArrow:
			for i in self.map.intersections:
				x, y = applyZoom(i.x, i.y)
				size = INTERSECTION_SIZE * self.zoom
				pygame.draw.rect(self.screen, (127, 0, 255), (x - size/2, y - size/2, size, size))

				# if i.finalTargetCarCount >= 1:
				if False:
					radius = i.finalTargetCarCount * 10 * self.zoom  # Tu peux changer 20 par un autre facteur si tu veux
					circle_color = (200, 200, 200, 100)  # Dernier paramètre = alpha (0-255)

					circle_surf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
					pygame.draw.circle(circle_surf, circle_color, (radius, radius), radius)
					self.screen.blit(circle_surf, (x - radius, y - radius))



		# Dessiner les voitures
		for car in self.map.cars:
			x, y = car.getCoord()
			x, y = applyZoom(x, y)
			size = car.size * self.zoom
			halfSize = size / 2

			if car.isAlive():
				if car.spawnLapCount == -1:
					color = (0, 127, 255)
				else:
					r = (self.map.lapCount - car.spawnLapCount)/car.angryDuration
					r = min(r, 1)
					color = (int(255*r), int(255*(1-r)), 0)
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

		# for _ in range(1):
			# runLap(draw.map)

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
	properties = ["wait", "maxWait", "sumDist"]  # Ajoute ici toutes les propriétés que tu veux afficher
	USE_BARS = False  # ou True selon ton besoin

	# Initialisation de dataList, une liste de tableaux de données
	dataList = [([0] * len(mapList)) for _ in properties]

	def fillList(index):
		for i in range(len(mapList)):
			dataList[index][i] = getattr(mapList[i].stats, properties[index]).list

	def mainFrame():
		runMapList()
		for i in range(len(properties)):
			fillList(i)

	# Création de la figure et des axes : un subplot par propriété
	num_props = len(properties)
	fig, axes = plt.subplots(num_props, 1, figsize=(8, 4 * num_props))
	if num_props == 1:
		axes = [axes]  # Pour que axes soit toujours itérable

	colors = ['r', 'g', 'b', 'c', 'm']
	# labels = ["r=400", "r=200", "r=60"]  # Adapte si besoin
	labels = ["su", "gir", "drt"]  # Adapte si besoin

	def update(frame):
		mainFrame()

		# if frame % 10 == 0:
			# print(dataList)

		for idx, ax in enumerate(axes):
			ax.clear()
			prop_data = dataList[idx]

			if USE_BARS:
				for i, data in enumerate(prop_data):
					ax.bar(np.arange(len(data)) + i * 0.2, data, width=0.2,
					       color=colors[i % len(colors)], label=f'Data {i+1}')
			else:
				for i, data in enumerate(prop_data):
					ax.plot(data, color=colors[i % len(colors)],
					        label=labels[i] if i < len(labels) else f'Data {i+1}')

			ax.set_title("Graph")
			ax.set_xlabel("Temps")
			ax.set_ylabel(f"{properties[idx]}")
			ax.legend()

	anim = FuncAnimation(fig, update, frames=1000000, interval=1, repeat=False)
	plt.tight_layout()
	plt.show()


threading.Thread(target=mathThread).start()

drawMapLoop(DrawObject(mapList[1], 50, 50, .6, False))
# drawMapLoop(DrawObject(mapList[1], 50, 50, .6, False))

# mathThread()

