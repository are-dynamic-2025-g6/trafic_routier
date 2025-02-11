# clear && python3 "main.py"

import pygame

# import filesp
from intersection import *
from car import *


intersections = [Intersection(20, 20)]

cars = [Car(800, 450, intersections[0])]



x = Intersection(10, 20)

pygame.init()
screen = pygame.display.set_mode((1000, 400))
pygame.display.set_caption("Dessin avec Pygame")

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	
	for car in cars:
		screen.fill((255, 255, 255))  # Fond blanc
		pygame.draw.rect(screen, (0, 0, 255), (car.x - CAR_SIZE/2, car.y - CAR_SIZE/2, CAR_SIZE, CAR_SIZE))  # Cercle bleu


	pygame.display.flip()  # Mettre à jour l'affichage

pygame.quit()

