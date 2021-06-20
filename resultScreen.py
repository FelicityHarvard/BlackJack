import pygame
from constants import *
from calculations import *
from createButton import *
import sys

def score(dealer_hand,player_hand,hit,bet):

	display.fill(white)
	background_image = pygame.image.load("blackjackBackground2.png")
	display.blit(background_image, [0, 0])


	amount_con = []
	word_con_list = []
	for i in player_hand:
		card = i 
		card_am = amount_conversion(card)
		amount_con.insert(0, card_am)

		word_con = suit_conversion(card)
		word_con_list.append(word_con)

	deal_amount_con = []
	deal_word_con_list = []
	for i in dealer_hand:
		card = i 
		card_am = amount_conversion(card)
		deal_amount_con.insert(0, card_am)

	dealer_count = sum(deal_amount_con)

	while dealer_count < 17:
		dealer_hand = draw_card(dealer_hand)
		new_card = dealer_hand[0]
		card_am = amount_conversion(new_card)
		dealer_count = dealer_count + card_am

	deal_amount_con = []
	deal_word_con_list = []
	for i in dealer_hand:
		card = i 
		card_am = amount_conversion(card)
		deal_amount_con.insert(0, card_am)

		word_con = suit_conversion(card)
		deal_word_con_list.append(word_con)


	ace_present_play = 'A' in word_con_list
	ace_present_deal = 'A' in deal_word_con_list
	print(ace_present_play)
	print(ace_present_deal)

	if ace_present_deal == True:
		if dealer_count < 21:
			index = deal_amount_con.index(1)
			deal_amount_con.pop(index)
			deal_amount_con.append(11)
			amount = sum(deal_amount_con)
			dealer_count = sum(deal_amount_con)
			if amount > 21:
				index = deal_amount_con.index(11)
				deal_amount_con.pop(index)
				deal_amount_con.append(1)
			dealer_count = sum(deal_amount_con)

	player_count = sum(amount_con)

	if ace_present_play == True:
		if player_count < 21:
			index = amount_con.index(1)
			amount_con.pop(index)
			amount_con.append(11)
			player_count = sum(amount_con)
			if amount > 21:
				index = amount_con.index(11)
				amount_con.pop(index)
				amount_con.append(1)
				player_count = sum(amount_con)

	dealtext = font.render("The dealers hand is " + str(deal_word_con_list), False, (0, 0, 0))
	display.blit(dealtext,(125,23))
	playtext = font.render("Your hand was " + str(word_con_list), False, (0, 0, 0))
	display.blit(playtext,(125,49))
	textsurfaceplay = font.render("Your final bet was :" + str(bet), False, (0, 0, 0))
	display.blit(textsurfaceplay,(150,100))

	back_button = button(250, 350, 'Go Another Round', 250, 70)
	start_button = button(250, 500, 'Go To Start Menu', 250, 70)
	Exit_button = button(250, 600, 'Exit Game', 250, 70)

	if player_count == 21:
		textsurface = font.render("You got BlackJack and won!", False, (0, 0, 0))
		display.blit(textsurface,(150,475))
		quotient = 150 / 100
		bet = int(bet) + (int(bet))*(quotient)
		textsurfaceplay = font.render("You won: $" + str(bet), False, (0, 0, 0))
		display.blit(textsurfaceplay,(150,125))
		pygame.display.update()
		


	if player_count > dealer_count and player_count < 22:
		textsurface = font.render("You beat the dealer and won!", False, (0, 0, 0))
		display.blit(textsurface,(150,475))
		textsurfaceplay = font.render("You won: $" + str(bet), False, (0, 0, 0))
		display.blit(textsurfaceplay,(150,125))
		pygame.display.update()
		player_count = []
		dealer_count = []

	if player_count < dealer_count and dealer_count < 22:
		textsurface = font.render("The dealer beat you and you lost!", False, (0, 0, 0))
		display.blit(textsurface,(150,475))
		textsurfaceplay = font.render("You lost: $" + str(bet), False, (0, 0, 0))
		display.blit(textsurfaceplay,(150,125))
		pygame.display.update()

	if player_count > 21:
		textsurface = font.render("You busted and lost!", False, (0, 0, 0))
		display.blit(textsurface,(150,475)) 
		textsurfaceplay = font.render("You lost: $" + str(bet), False, (0, 0, 0))
		display.blit(textsurfaceplay,(150,125))
		pygame.display.update()


	if player_count == dealer_count:
		textsurface = font.render("You pushed and tied with dealer.", False, (0, 0, 0))
		display.blit(textsurfaceplay,(150,475))
		textsurfaceplay = font.render("You kept: $" + str(bet), False, (0, 0, 0))
		display.blit(textsurface,(150,125)) 
		pygame.display.update()

	while running:

		from round import basicround
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if back_button.draw_button():
				display.fill(white)
				pygame.display.flip()
				doubledown = False
				bet = 0
				dealer_hand = []
				player_hand = []
				hit = 0
				from round import betting
				betting(doubledown,bet,dealer_hand,player_hand,hit)

			if Exit_button.draw_button():
				pygame.quit()
				sys.exit()
			if start_button.draw_button():
				from main import introducitonScreen
				introducitonScreen()

		pygame.display.update()