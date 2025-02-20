# clear && python3 "main.py"

import pygame

from data import *
from priority import *

def runLap():
	for i in cars:
		i.accelerate()
		i.move()	

	return None






def drawGame():
	# thanks chatgpt
	def drawArrow(color, start, end, percentage=0.8, arrow_size=10, thickness=5):
		# Calcul du point à "percentage%" du segment
		point_x = start[0] + percentage * (end[0] - start[0])
		point_y = start[1] + percentage * (end[1] - start[1])
		arrow_pos = (point_x, point_y)

		# Dessiner le segment
		pygame.draw.line(screen, color, start, end, thickness)

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
		pygame.draw.polygon(screen, color, [arrow_tip, arrow_left, arrow_right])




	# white background
	screen.fill((255, 255, 255))
	
	# draw roads (red)
	for i in intersections:
		for d in i.directions:
			drawArrow((255, 0, 63), (i.x, i.y), (d.x, d.y))
	
	# draw intersections (purple)
	for i in intersections:
		pygame.draw.rect(screen, (127, 0, 255), (i.x - INTERSECTION_SIZE/2, i.y - INTERSECTION_SIZE/2, INTERSECTION_SIZE, INTERSECTION_SIZE))



	# draw cars (green)
	for car in cars:
		x, y = car.getCoord()
		pygame.draw.rect(screen, (0, 255, 127), (x - CAR_SIZE/2, y - CAR_SIZE/2, CAR_SIZE, CAR_SIZE))



pygame.init()
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Dessin avec Pygame")


pygameClock = pygame.time.Clock()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	
	drawGame()

	pygame.display.flip()  # Mettre à jour l'affichage

	pygameClock.tick(50)
	runLap()




pygame.quit()

