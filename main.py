# clear && python3 "main.py"

import pygame

from data import *

from methods import Car_getNextPriority
from methods import Car_frame

def runLap():
	for car in cars:
		if car.alive: # for debug
			Car_frame(car, intersections[3])

		car.move() # called every frame (because a car can't stop instantly)

	return None



pygame.init()
pygame.display.set_caption("Traffic rider")

class DrawObject:
	def __init__(self):
		self.screen = pygame.display.set_mode((800, 450))
		self.font = pygame.font.Font(None, 20)
		self.clock = pygame.time.Clock()
		
	def drawGame(self):
		# thanks chatgpt
		def drawArrow(color, start, end, percentage=0.8, arrow_size=10, thickness=5):
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
		for i in intersections:
			for d in i.targets:
				drawArrow((255, 0, 63), (i.x, i.y), (d.x, d.y))
		
		# draw intersections (purple)
		for i in intersections:
			pygame.draw.rect(self.screen, (127, 0, 255), (i.x - INTERSECTION_SIZE/2, i.y - INTERSECTION_SIZE/2, INTERSECTION_SIZE, INTERSECTION_SIZE))



		# draw cars (green)
		for car in cars:
			x, y = car.getCoord()
			size = car.size
			halfSize = size/2

			color = (0, 255, 127) if car.alive else (127, 127, 127)
			pygame.draw.rect(self.screen, color, (x - halfSize, y - halfSize, size, size))


draw = DrawObject()




running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	
	draw.drawGame()

	pygame.display.flip()  # Mettre à jour l'affichage

	draw.clock.tick(50)
	runLap()




pygame.quit()

