import pygame
import sys
import time

from pygame import mixer

pygame.mixer.init()  #had trouble getting sound without these values
pygame.init()
pygame.mixer.set_num_channels(32)

display = pygame.display.set_mode((640, 480)) #Keyboard inputs won't register without a screen

notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
#notes = ["A", "Ab", "B", "Bb", "C", "D", "Db", "E", "Eb", "F", "G", "Gb"]

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

# Initialize dictionaries for lower and upper octaves
lower_octave_sounds = {}
upper_octave_sounds = {}

# Caps Lock state to toggle between lower and upper octaves
use_upper_octaves = False

min_octave = 0  # Starting octave
max_octave = 7  # Highest available octave

key_index = 0

# Load sounds into lower and upper dictionaries
while key_index < len(key_mapping):
    key = key_mapping[key_index]

    lower_octave = min(max(min_octave, 1 + (key_index // 8)), max_octave)
    upper_octave = min(max(min_octave, 4 + (key_index // 8)), max_octave)

    note_index = key_index % 8
    if note_index < len(notes):  # Ensure valid note indices (0-11)
        note = notes[note_index]

        # Construct file paths
        lower_sound_file = f'media/samples/UIO/{note}{lower_octave}.aiff'
        upper_sound_file = f'media/samples/UIO/{note}{upper_octave}.aiff'

        # Load lower octave sound
        try:
            lower_octave_sounds[key] = pygame.mixer.Sound(lower_sound_file)
            lower_octave_sounds[key].set_volume(1.0)
            print(f"Loaded sound: {lower_sound_file}")
        except pygame.error as e:
            print(f"Failed to load {lower_sound_file} - {e}")

        # Load upper octave sound
        try:
            upper_octave_sounds[key] = pygame.mixer.Sound(upper_sound_file)
            upper_octave_sounds[key].set_volume(1.0)
            print(f"Loaded sound: {upper_sound_file}")
        except pygame.error as e:
            print(f"Failed to load {upper_sound_file} - {e}")

    # Increment the key index manually
    key_index += 1

print("Please only use keys to the right and below the TILDE key, and to the left and above the RIGHT-SHIFT key")
# Main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_CAPSLOCK:
                use_upper_octaves = not use_upper_octaves
                print("Using upper octaves" if use_upper_octaves else "Using lower octaves")

            # Play sound based on current Caps Lock state
            if event.key in lower_octave_sounds:
                if use_upper_octaves and event.key in upper_octave_sounds:
                    pygame.mixer.Sound.play(upper_octave_sounds[event.key])
                    print(f"Playing upper octave sound for key: {pygame.key.name(event.key)}")   ###
                else:
                    pygame.mixer.Sound.play(lower_octave_sounds[event.key])
                    print(f"Playing lower octave sound for key: {pygame.key.name(event.key)}")   ###
