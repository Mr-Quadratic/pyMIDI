import pygame
import sys
import time

from pygame import mixer
pygame.mixer.init()
pygame.init()

display = pygame.display.set_mode((640, 480)) #Keyboard inputs won't register without a screen

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				pygame.mixer.Channel(0).play(pygame.mixer.Sound('media/samples/UIO/A1.aiff'))
			if event.key == pygame.K_s:
				pygame.mixer.Channel(1).play(pygame.mixer.Sound('media/samples/UIO/A2.aiff'))
			if event.key == pygame.K_d:
				pygame.mixer.Channel(2).play(pygame.mixer.Sound('media/samples/UIO/A3.aiff'))
			if event.key == pygame.K_f:
				pygame.mixer.Channel(3).play(pygame.mixer.Sound('media/samples/UIO/A4.aiff'))
