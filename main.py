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
				mixer.music.load('media/samples/UIO/A1.aiff')
				mixer.music.play()
			if event.key == pygame.K_s:
				mixer.music.load('media/samples/UIO/A2.aiff')
				mixer.music.play()
			if event.key == pygame.K_d:
				mixer.music.load('media/samples/UIO/A3.aiff')
				mixer.music.play()
			if event.key == pygame.K_f:
				mixer.music.load('media/samples/UIO/A4.aiff')
				mixer.music.play()
