import pygame
import sys
import time

from pygame import mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)  #had trouble getting sound without these values
pygame.init()

display = pygame.display.set_mode((640, 480)) #Keyboard inputs won't register without a screen


notes = ["A", "Ab", "B", "Bb", "C", "D", "Db", "E", "Eb", "F", "G", "Gb"]

#for some reason the keys are not in the order I was expecting, or at least the corresponding sounds arent, will fix soon
key_mapping = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9,
			pygame.K_0, pygame.K_MINUS, pygame.K_EQUALS,
# first set 1234567890-=
			pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o,
			pygame.K_p, pygame.K_LEFTBRACKET, pygame.K_RIGHTBRACKET,
# second set QWERTYUIOP[]
			pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_j, pygame.K_k, pygame.K_l,
			pygame.K_SEMICOLON, pygame.K_QUOTE,
# third set ASDFGHJKL;'
			pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n, pygame.K_m, pygame.K_COMMA,
			pygame.K_PERIOD, pygame.K_SLASH]
# fourth set ZXCVBNM,./


lower_sounds = {}
upper_sounds = {}

#im relativley sure this format allows for other instrument files to be filled in
for octave in range(1, 4):
    for i, note in enumerate(notes):
        key_index = (octave - 1) * len(notes) + i
        if key_index < len(key_mapping):
            key = key_mapping[key_index]
            sound_file = f'media/samples/UIO/{note}{octave}.aiff'
            print(f"Loading sound: {sound_file}")
            try: # necessary
                lower_sounds[key] = pygame.mixer.Sound(sound_file)
            except pygame.error as e:
                print(f"Error loading sound: {sound_file} - {e}")


for octave in range(4, 8):
    for i, note in enumerate(notes):
        key_index = (octave - 4) * len(notes) + i
        if key_index < len(key_mapping):
            key = key_mapping[key_index]
            sound_file = f'media/samples/UIO/{note}{octave}.aiff'
            print(f"Loading sound: {sound_file}")
            try:
                upper_sounds[key] = pygame.mixer.Sound(sound_file)
            except pygame.error as e:
                print(f"Error loading sound: {sound_file} - {e}")


for sound in lower_sounds.values():
    sound.set_volume(1.0)
for sound in upper_sounds.values():
    sound.set_volume(1.0)


use_upper_octaves = False  # Keep track of Caps Lock state

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_CAPSLOCK:
                use_upper_octaves = not use_upper_octaves
                print("Using upper octaves" if use_upper_octaves else "Using lower octaves")

            # Check if the key is mapped to a sound
            if use_upper_octaves and event.key in upper_sounds:
                print(f"Playing upper octave sound for key: {pygame.key.name(event.key)}")  # Debugging
                pygame.mixer.Channel(0).play(upper_sounds[event.key])
            elif event.key in lower_sounds:
                print(f"Playing lower octave sound for key: {pygame.key.name(event.key)}")  # Debugging
                pygame.mixer.Channel(0).play(lower_sounds[event.key])