import pygame
import sys
import time

from pygame import mixer

###
# Please look into mixer, as it will be the best library we can currently
# use to play audio correctly in sync with keyboard inputs. Remember that
# the naming scheme of the audio files are by octave.
# Therefore, A1 is lower pitched than A2, and F3 is higher pitched than B3.
# Example: Ab1 A1 Bb1 B1 C1 Db1 D1 Eb1 E1 F1 Gb1 G1 Ab2 A2 etc...
###