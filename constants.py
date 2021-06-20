import pygame

clock = pygame.time.Clock()
pygame.font.init()
clicked = False
black = (0,0,0)
white = (225,225,225)
width, height = 700, 700
display = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('Currier', 40)
running = True
hit = 0
displaying = True
doubledown = False
bet = 0
dealer_hand = []
player_hand = []
