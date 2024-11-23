import sys
import json
import os
from GUIstuff import *

pygame.mixer.init()
pygame.init()
pygame.mixer.set_num_channels(32)

# Settings file for user preferences
settings_file = "user_settings.json"
default_settings = {
    "volume": 50,
    "fade_time": 600,
    "starting_octave": 2
}

def load_settings():
    if os.path.exists(settings_file):
        try:
            with open(settings_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Settings file corrupted. Using default.")
    return default_settings

def save_settings(settings):
    try:
        with open(settings_file, 'w') as file:
            json.dump(settings, file, indent=4)
    except Exception as e:
        print(f"Error saving settings: {e}")

# Load user settings
settings = load_settings()
current_volume = settings["volume"]
current_fade_time = settings["fade_time"]
current_octave = settings["starting_octave"]

print(f"Loaded settings: Volume = {current_volume}, Fade Time = {current_fade_time}, Starting Octave = {current_octave}")

# Pre-apply settings
volume.set_current_value(current_volume)
fade.set_current_value(current_fade_time)


#display = pygame.display.set_mode((640, 480))
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

octave1 = ["1", "!", "2", "@", "3", "4", "$", "5", "%", "6", "^", "7"]
octave2 = ["8", "*", "9", "(", "0", "q", "Q", "w", "W", "e", "E", "r"]
octave3 = ["t", "T", "y", "Y", "u", "i", "I", "o", "O", "p", "P", "a"]
octave4 = ["s", "S", "d", "D", "f", "g", "G", "h", "H", "j", "J", "k"]
octave5 = ["l", "L", "z", "Z", "x", "c", "C", "v", "V", "b", "B", "n"]
# one leftover key lmao
octave6 = "m"

# Initialize 5 octaves (C3 to C7) in the octave_sounds dictionary
octave_sounds = {}
current_octave = 2  # Start at 2 (C2-C7)

min_octave = 1  # Lowest octave (C1-C6)
max_octave = 3  # Highest octave (C3-C8)

# Initialize 32 mixer channels
num_channels = 32
pygame.mixer.set_num_channels(num_channels)
channels = [pygame.mixer.Channel(i) for i in range(num_channels)]
current_channel = 0

# Initialize sounds and GUI mappings
active_sounds = {}
active_button_sounds = {}
keys_to_GUI = {}

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

# Dictionaries to track active sounds (keys that are pressed down)
active_sounds = {}
active_button_sounds = {}

#Dictionary to map key presses to GUI buttons
keys_to_GUI = {}
tiles_to_GUI = {}


shift_pressed = False


def octaveHandler():
    if event.unicode in octave1:
        return current_octave
    elif event.unicode in octave2:
        return current_octave + 1
    elif event.unicode in octave3:
        return current_octave + 2
    elif event.unicode in octave4:
        return current_octave + 3
    elif event.unicode in octave5:
        return current_octave + 4
    elif event.unicode in octave6:
        return current_octave + 5


l = 0
square_l = 0
isPressed = False
# Main loop
clock = pygame.time.Clock()

while True:
    time_delta = clock.tick(60) / 1000.0
    pygame.time.delay(10)
    GUI_display.blit(background, (0, 0))
    square = pygame.draw.rect(GUI_display, 'blue', (100, 100, 100, square_l))
    if isPressed:
        square_l += 50

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save user settings on exit
            current_settings = {
                "volume": current_volume,
                "fade_time": current_fade_time,
                "starting_octave": current_octave
            }
            save_settings(current_settings)
            print(f"Saved settings: {current_settings}")
            pygame.quit()
            sys.exit()

        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            sound = None
            try:
                note = event.ui_element.text
                sound = pygame.mixer.Sound(f'media/samples/UIO/{note}.aiff')
                print(f"Playing natural note: {note}")
            except pygame.error as e:
                print(f"Failed to load {note} - {e}")
            except OSError as e:
                print(f"Failed to load {note} - {e}")
            if sound:
                for channel in channels:
                    if not channel.get_busy():
                        channel.play(sound)
                        active_button_sounds[event.ui_element.text] = channel
                        break


        # Track Shift key state
        if event.type == pygame.KEYDOWN:



            isPressed = True

            if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                shift_pressed = True

            # Play sound based on the current key and octave
            if event.key in key_mapping:
                sound = None
                note_index = key_mapping.index(event.key) % 7  # Only use natural notes
                note = notes[note_index]
                note_octave = octaveHandler()

                if shift_pressed:
                    # If Shift is pressed, check for sharp note and map to flat
                    sharp_note = f"{note}sharp"
                    if sharp_note in sharp_to_flat:
                        # Map sharp to flat (e.g., C# -> Db)
                        flat_note = sharp_to_flat.get(sharp_note)
                        sound_file = f'media/samples/UIO/{flat_note}{note_octave}.aiff'
                        try:
                            sound = pygame.mixer.Sound(sound_file)
                            print(f"Playing sharp/flat sound: {flat_note}{note_octave}")
                        except pygame.error as e:
                            print(f"Failed to load {sound_file} - {e}")
                        except OSError as e:
                            print(f"Failed to load {sound_file} - {e}")
                        try:
                            pressed = PressedFlatSprite('dimgrey', notes_to_keys[f'{note}{note_octave}']+50, 700)
                            keys_to_GUI[event.key] = pressed
                            allSprites.add(pressed)
                        except KeyError:
                            print("that ain't a key man")

                else:
                    # No Shift, only play natural notes (e.g., C4, D4, E4, etc.)
                    sound_file = f'media/samples/UIO/{note}{note_octave}.aiff'
                    try:
                        sound = pygame.mixer.Sound(sound_file)
                        sound.set_volume(volume.get_current_value() / 100)
                        print(volume.get_current_value())
                        print(f"Playing natural note: {note}{note_octave}")
                    except pygame.error as e:
                        print(f"Failed to load {sound_file} - {e}")
                    except OSError as e:
                        print(f"Failed to load {sound_file} - {e}")
                    try:
                        pressed = PressedSprite('dimgrey', notes_to_keys[f'{note}{note_octave}'] + 25, 725)
                        keys_to_GUI[event.key] = pressed
                        allSprites.add(pressed)
                    except KeyError:
                        print("that aint a key man")



                if sound:
                    for channel in channels:
                        if not channel.get_busy():
                            channel.play(sound)
                            active_sounds[event.key] = channel
                            break



        # Handle Shift release
        elif event.type == pygame.KEYUP:
            isPressed = False
            if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                shift_pressed = False

            # Stop the sound and fade out when the key is released
            if event.key in active_sounds:
                channel = active_sounds.pop(event.key)
                channel.fadeout(fade.get_current_value())

            for x in allSprites:
                keyButton = keys_to_GUI.get(event.key)
                if x == keyButton:
                    x.kill()
            for x in allTiles:
                keyButton = tiles_to_GUI.get(event.key)
                if x == keyButton:
                    x.kill()

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
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element.text in active_button_sounds:
                channel = active_button_sounds.pop(event.ui_element.text)
                channel.fadeout(600)

        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == volume:
                current_volume = volume.get_current_value()
            elif event.ui_element == fade:
                current_fade_time = fade.get_current_value()


        manager.process_events(event)

    manager.update(time_delta)
    labeldisp.set_text(str(volume.get_current_value()))
    labeldisp2.set_text(str(fade.get_current_value()))

    manager.draw_ui(GUI_display)
    allSprites.draw(GUI_display)

    pygame.display.update()