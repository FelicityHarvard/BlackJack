import pygame
import random
from constants import *

 
deck = [2,3,4,5,6,7,8,9,10,33,44,55,66,2,3,4,5,6,7,8,9,10,33,44,55,66,2,3,4,5,6,7,8,9,10,33,44,55,66,2,3,4,5,6,7,8,9,10,33,44,55,66]

i = 0
if i == 0:
    random.shuffle(deck)
    i = 1


dealer_hand = []
player_hand = []

def init_hand(blankhand):
    blankhand.insert(0, deck.pop(deck.index(random.choice(deck))))
    blankhand.insert(0, deck.pop(deck.index(random.choice(deck))))
    return blankhand
    
def draw_card(hand):
    hand.insert(0, deck.pop(deck.index(random.choice(deck))))
    return hand

def amount_conversion(card):

	card = int(card)

	if 33 is card:
		newcard = 10
		return(newcard)
		
	if 44 is card:
		newcard = 10
		return(newcard)

	if 55 is card:
		newcard = 10
		return(newcard)

	if 66 is card:
		newcard = 1
		return(newcard)
	
	else:
		newcard = card
		return(newcard)

def suit_conversion(card):
	card = int(card) 

	if 33 is card:
		newcard = 'J'
		return(newcard)
		
	if 44 is card:
		newcard = 'Q'
		return(newcard)

	if 55 is card:
		newcard = 'K'
		return(newcard)

	if 66 is card:
		newcard = 'A'
		return(newcard)
	
	else:
		newcard = int(card)
		return(newcard)
	

def createNewScreen():
	display.fill(white)
	pygame.display.set_caption('Blackjack Star Edition')
	pygame.display.flip()

def seperate(hand):
	
	amount = len(hand)

	if amount < 3:
		Card_1 = hand[0]
		Card_2 = hand[1]
		amount_conversion(Card_1)
		amount_conversion(Card_2)

		hand = [Card_1,Card_2,]
		return(hand)

	if amount < 4:
		Card_1 = hand[0]
		Card_2 = hand[1]
		Card_3 = hand[2]
		amount_conversion(Card_1)
		amount_conversion(Card_2)
		amount_conversion(Card_3)

		hand = [Card_1,Card_2,Card_3]
		return(hand)

	for i in hand: 
		Card_1 = hand[i]
		Card_2 = hand[1]
		Card_3 = hand[2]
		Card_4 = hand[3]
		amount_conversion(Card_1)
		amount_conversion(Card_2)
		amount_conversion(Card_3)
		amount_conversion(Card_4)

		hand = [Card_1,Card_2,Card_3,Card_4]
		return(hand)

	if amount < 6:
		Card_1 = hand[0]
		Card_2 = hand[1]
		Card_3 = hand[2]
		Card_4 = hand[3]
		Card_5 = hand[4]
		amount_conversion(Card_1)
		amount_conversion(Card_2)
		amount_conversion(Card_3)
		amount_conversion(Card_4)
		amount_conversion(Card_5)

		hand = [Card_1,Card_2,Card_3,Card_4,Card_5]
		return(hand)

	if amount < 7:
		Card_1 = hand[0]
		Card_2 = hand[1]
		Card_3 = hand[2]
		Card_4 = hand[3]
		Card_5 = hand[4]
		Card_6 = hand[5]
		amount_conversion(Card_1)
		amount_conversion(Card_2)
		amount_conversion(Card_3)
		amount_conversion(Card_4)
		amount_conversion(Card_5)
		amount_conversion(Card_6)

		hand = [Card_1,Card_2,Card_3,Card_4,Card_5,Card_6]
		return(hand)

	if amount < 8:
		Card_1 = hand[0]
		Card_2 = hand[1]
		Card_3 = hand[2]
		Card_4 = hand[3]
		Card_5 = hand[4]
		Card_6 = hand[5]
		Card_7 = hand[6]
		amount_conversion(Card_1)
		amount_conversion(Card_2)
		amount_conversion(Card_3)
		amount_conversion(Card_4)
		amount_conversion(Card_5)
		amount_conversion(Card_6)
		amount_conversion(Card_7)

		hand = [Card_1,Card_2,Card_3,Card_4,Card_5,Card_6,Card_7]
		return(hand)
