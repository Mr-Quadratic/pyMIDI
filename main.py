import pygame
import sys

from pygame import mixer

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=128)
pygame.init()

display = pygame.display.set_mode((640, 480))
pygame.key.set_repeat(0)  # Disable key repeat for accurate simultaneous key presses

# Correct natural notes
notes = ["C", "D", "E", "F", "G", "A", "B"]  # Natural notes only

# Map sharp notes to their equivalent flat notes (only if shift is pressed)
sharp_to_flat = {
    "Csharp": "Db",
    "Dsharp": "Eb",
    "Fsharp": "Gb",
    "Gsharp": "Ab",
    "Asharp": "Bb"
}

# Keyboard layout from virtualpiano.net (keys 1-0 and Q-M will be mapped)
key_mapping = [
    pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
    pygame.K_8, pygame.K_9, pygame.K_0, pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r,
    pygame.K_t, pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p, pygame.K_a,
    pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_j, pygame.K_k,
    pygame.K_l, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n,
    pygame.K_m
]

# Initialize 5 octaves (C3 to C7) in the octave_sounds dictionary
octave_sounds = {}
current_octave = 4  # Start at C4

min_octave = 3  # Lowest octave (C3)
max_octave = 7  # Highest octave (C7)

# Initialize 32 mixer channels
num_channels = 32
pygame.mixer.set_num_channels(num_channels)
channels = [pygame.mixer.Channel(i) for i in range(num_channels)]
current_channel = 0

# Preload sounds for all natural notes across octaves
for i, key in enumerate(key_mapping):
    note_index = i % 7  # Only use natural notes
    note = notes[note_index]

    sound_file = f'media/samples/UIO/{note}{current_octave}.aiff'

    try:
        octave_sounds[key] = pygame.mixer.Sound(sound_file)
        octave_sounds[key].set_volume(1.0)
        print(f"Loaded sound: {sound_file}")
    except pygame.error as e:
        print(f"Failed to load {sound_file} - {e}")

# Dictionary to track active sounds (keys that are pressed down)
active_sounds = {}
shift_pressed = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Track Shift key state
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                shift_pressed = True

            # Play sound based on the current key and octave
            if event.key in key_mapping:
                sound = None
                note_index = key_mapping.index(event.key) % 7  # Only use natural notes
                note = notes[note_index]

                if shift_pressed:
                    # If Shift is pressed, check for sharp note and map to flat
                    sharp_note = f"{note}sharp"
                    if sharp_note in sharp_to_flat:
                        # Map sharp to flat (e.g., C# -> Db)
                        flat_note = sharp_to_flat.get(sharp_note)
                        sound_file = f'media/samples/UIO/{flat_note}{current_octave}.aiff'
                        try:
                            sound = pygame.mixer.Sound(sound_file)
                            print(f"Playing sharp/flat sound: {flat_note}{current_octave}")
                        except pygame.error as e:
                            print(f"Failed to load {sound_file} - {e}")
                else:
                    # No Shift, only play natural notes (e.g., C4, D4, E4, etc.)
                    sound_file = f'media/samples/UIO/{note}{current_octave}.aiff'
                    try:
                        sound = pygame.mixer.Sound(sound_file)
                        print(f"Playing natural note: {note}{current_octave}")
                    except pygame.error as e:
                        print(f"Failed to load {sound_file} - {e}")

                # If a sound was successfully loaded, play it
                if sound:
                    # Find an available channel to play the sound
                    for channel in channels:
                        if not channel.get_busy():
                            channel.play(sound)
                            active_sounds[event.key] = channel
                            break

        # Handle Shift release
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                shift_pressed = False

            # Stop the sound and fade out when the key is released
            if event.key in active_sounds:
                channel = active_sounds.pop(event.key)
                channel.fadeout(600)

        # Change octave using ',' and '.'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_COMMA:  # Decrease octave
                if current_octave > min_octave:
                    current_octave -= 1
                    print(f"Octave decreased to {current_octave}")
            elif event.key == pygame.K_PERIOD:  # Increase octave
                if current_octave < max_octave:
                    current_octave += 1
                    print(f"Octave increased to {current_octave}")
