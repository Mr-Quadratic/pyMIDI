import pygame
import sys
import time

from pygame import mixer

pygame.mixer.init()
sound = pygame.mixer.Sound('media/samples/UIO/C4.aiff')
sound.play()
time.sleep(10)