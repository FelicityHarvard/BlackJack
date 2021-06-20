import pygame
from constants import * 
from calculations import *
from createButton import button
from resultScreen import score
import sys

def betting(doubledown,bet,dealer_hand,player_hand,hit):
	global running
	user_text = ''
	color_active = pygame.Color('lightskyblue3')
	color_passive = pygame.Color('chartreuse4')
	color = color_passive

	active = False

	display.fill(white)
	background_image = pygame.image.load("blackjackBackground2.png")
	display.blit(background_image, [0, 0])
	input_rect = pygame.Rect(250, 500, 140, 32)

	if doubledown == False:
		textsurface = font.render("What amount would you like to bet?", False, (0, 0, 0))
		display.blit(textsurface,(125,35))
		textsurface = font.render("Min: $100      Max: $50,000", False, (0, 0, 0))
		display.blit(textsurface,(185,60))

	if doubledown == True:
		textsurface = font.render("What amount would you like to double down?", False, (0, 0, 0))
		display.blit(textsurface,(125,35))
		textsurface = font.render("Min: $1      Max: $" + str(bet), False, (0, 0, 0))
		display.blit(textsurface,(185,60))

	textsurface = font.render("Please enter your bet in the green box", False, (0, 0, 0))
	display.blit(textsurface,(100,450))

	enter_button = button(575, 600, 'Enter',100, 70)

	pygame.display.flip()

	while True:

		for event in pygame.event.get():
	
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
	
			if event.type == pygame.MOUSEBUTTONDOWN:
				if input_rect.collidepoint(event.pos):
					active = True
				else:
					active = False
	
			if event.type == pygame.KEYDOWN:
	
				if event.key == pygame.K_BACKSPACE:
					input_rect.w = input_rect.w - 1
					user_text = user_text[:-1]

				if event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
					user_text += event.unicode

			if enter_button.draw_button() :

				if doubledown == False:
					if int(user_text) < 100:
						textsurface = font.render("Please enter a bid higher then 100", False, (0, 0, 0))
						display.blit(textsurface,(100,600))

					elif int(user_text) > 50000:
						textsurface = font.render("Please enter a bid under then 50000", False, (0, 0, 0))
						display.blit(textsurface,(100,550))
					
					else:
						basicround(user_text)

				if doubledown == True:
					if int(user_text) < 100:
						textsurface = font.render("Please enter a bid higher then 100", False, (0, 0, 0))
						display.blit(textsurface,(100,600))

					elif int(user_text) > 50000:
						textsurface = font.render("Please enter a bid under then 50000", False, (0, 0, 0))
						display.blit(textsurface,(100,550))
					
					else:
						bet = bet + int(user_text)
						seperate(dealer_hand)
						score(dealer_hand,player_hand,hit,bet)

				



	
		if active:
			color = color_active
		else:
			color = color_passive
			

		pygame.draw.rect(display, color, input_rect)
	
		text_surface = font.render(user_text, True, (255, 255, 255))
		

		display.blit(text_surface, (input_rect.x+5, input_rect.y+5))
		

		input_rect.w = max(1, text_surface.get_width()+10)
		

		pygame.display.flip()
		

		clock.tick(60)

def basicround(bet):
	
	global running
	global hit
	display.fill(white)
	background_image = pygame.image.load("blackjackBackground2.png")
	display.blit(background_image, [0, 0])

	player_hand = []
	dealer_hand = []
	hit = 0

	player_hand = init_hand(player_hand)
	dealer_hand = init_hand(dealer_hand)


	deal_num0 = dealer_hand[1]
	deal_num0 = suit_conversion(deal_num0)

	play_num0 = player_hand[0]
	play_num1 = player_hand[1]
	play_num_conv_0 = suit_conversion(play_num0)
	play_num_conv_1 = suit_conversion(play_num1)

	player_word_hand_num0 = [play_num_conv_0, play_num_conv_1]
	
	textsurface = font.render("The dealers hand is [X, " + str(deal_num0) + "]", False, (0, 0, 0))
	display.blit(textsurface,(185,35))

	
	textsurfaceplay = font.render("Your hand is " + str(player_word_hand_num0), False, (0, 0, 0))
	display.blit(textsurfaceplay,(200,485))

	textsurfaceplay = font.render("Your bet is :" + bet, False, (0, 0, 0))
	display.blit(textsurfaceplay,(150,100))
	
	back_button = button(575, 600, 'Back', 100, 70)
	hit_button = button(150,550, "Hit", 100, 70)
	stand_button = button (300,550, "Stand", 100, 70)
	double_down_button = button (450,550, "DD", 100, 70)
	split_button = button(50, 600,"Split",100, 70)


		
	while running:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if back_button.draw_button():
				from main import introducitonScreen
				(introducitonScreen)
				
			if hit_button.draw_button():
				pygame.display.flip()
				player_hand = draw_card(player_hand)
				hit = hit + 1

				amount_con = []
				word_con_list = []
				for i in player_hand:
					card = i 
					card_am = amount_conversion(card)
					amount_con.insert(0, card_am)

					word_con = suit_conversion(card)
					word_con_list.append(word_con)

					

				display.fill(white)
				background_image = pygame.image.load("blackjackBackground2.png")
				display.blit(background_image, [0, 0])
				textsurfaceplay = font.render("Your hand is " + str(word_con_list), False, (0, 0, 0))
				display.blit(textsurfaceplay,(200,500))
				textsurface = font.render("The dealers hand is [X, " + str(deal_num0) + "]", False, (0, 0, 0))
				display.blit(textsurface,(185,35))
				textsurfaceplay = font.render("Your bet is :" + bet, False, (0, 0, 0))
				display.blit(textsurfaceplay,(150,100))

				pygame.display.update()
				
				amount_con = []
				word_con_list = []
				for i in player_hand:
					card = i 
					card_am = amount_conversion(card)
					amount_con.insert(0, card_am)
				amount = sum(amount_con)

				if amount > 21:
					seperate(dealer_hand)
					score(dealer_hand,player_hand,hit,bet)
				
				if amount == 21:
					seperate(dealer_hand)
					score(dealer_hand,player_hand,hit,bet)


			if stand_button.draw_button():
				clicked = True
				seperate(dealer_hand)
				seperate(player_hand)
				score(dealer_hand,player_hand,hit,bet)
			
			if double_down_button.draw_button():

				if hit > 0:
					textsurfaceplay = font.render("You cant double down after you hit", False, (0, 0, 0))
					display.blit(textsurfaceplay,(150,300))

				if hit == 0:
					doubledown = True
					bet = int(bet) + int(bet)
					clicked = True
					player_hand = draw_card(player_hand)
					betting(doubledown, bet,dealer_hand,player_hand,hit)

		
		pygame.display.update()