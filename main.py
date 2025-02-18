# clear && python3 "main.py"

import pygame

from data import *

def run_lap():


	return None



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

	run_lap()



pygame.quit()

