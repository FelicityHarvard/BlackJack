import pygame
from calculations import *
from constants import *
from round import basicround, betting
from createButton import button
import sys


running = True

def introducitonScreen():
	global running
	display.fill(white)

	background_image = pygame.image.load("blackjackBackground.png")
	display.blit(background_image, [0, 0])

	pygame.display.set_caption('Blackjack Star Edition')
	textsurface = font.render("          ~-~-~  Welcome to BlackJack ~-~-~", False, (0, 0, 0))
	display.blit(textsurface,(0,100))
	
	exit_button = button(375, 600, 'Exit', 100, 70)
	play_button = button(150, 600, 'Play?', 100, 70)

	pygame.display.flip()

	while running:

		for event in pygame.event.get():
			if exit_button.draw_button():
				pygame.quit()
				sys.exit()
			if play_button.draw_button():
				(betting(doubledown,bet,dealer_hand,player_hand,hit))
			if event.type == pygame.QUIT:
				running = False
		
		pygame.display.flip()

introducitonScreen()