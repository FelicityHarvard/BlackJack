import pygame
from constants import *
class button():

	button_color = (247, 200, 70)
	hover_color = (225, 128, 0)
	click_color = (153, 76, 0)
	text_color = black

	def __init__(self, x, y, text, width, height):
		self.x = x
		self.y = y
		self.text = text
		self.width = width
		self.height = height

	def draw_button(button):
		global clicked
		action = False

		pos = pygame.mouse.get_pos()


		button_rect = pygame.Rect(button.x, button.y, button.width, button.height)
		
		if displaying: 
			if button_rect.collidepoint(pos):
				if pygame.mouse.get_pressed()[0] == 1:
					clicked = True
					pygame.draw.rect(display, button.click_color, button_rect)
				elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
					clicked = False
					action = True
				else:
					pygame.draw.rect(display, button.hover_color, button_rect)
			else:
				pygame.draw.rect(display, button.button_color, button_rect)
		

		text_img = font.render(button.text, True, button.text_color)
		display.blit(text_img, (button.x + int(button.width / 2)-30, button.y +int(button.height / 2) ))
		return action

	def delete():
		displaying = False