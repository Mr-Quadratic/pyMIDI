## COP1500 - Python Project Group 1
# "PyANO"
Pyano is a program that takes a keypress from a typical computer keyboard and outputs the corresponding audio from a sound file.
It features a UI that displays a typical piano keyboard layout. Each key is labeled with its corresponding note.​
Pyano is a Python recreation of virtualpiano.net, a popular online piano, using the pygame suite of libraries.
Pyano features adjustable volume and release time for played keys, and a greater range of playable octaves than virtualpiano.
Volume and release time settings are saved when the application closes. Reopening the program will return the last saved settings.
Additionally, Pyano can be played offline since it is stored locally as a collection of Python scripts, whereas virtualpiano requires an internet connection.

Issues:​
- GUI is not scalable. To fit all keys, octaves 1 and 7 are hidden on the GUI. They are still accessible through keyboard input.​
- There were several features that we wanted to add, such as different sound banks, MIDI file support and recording, and a note visualizer (which was almost finished) but that we ran out of time to implement​
- Additionally, the GUI does not look as nice as it could​
- These stretch goals, plus better GUI theming and layout, would be added in future versions of Pyano

Workload Distributions:​

- TJsnapdrag: keyboard input, audio output, demo 1 pseudocode, setting save functions​
- Mr-Quadratic: GUI setup, key creation, audio output for key press, volume and release time sliders​
- asterSSH: project management, task assignment, optimization, octave handling, bug fixing, sound banks​

References:​

- Pygame GUI documentation: https://pygame-gui.readthedocs.io/en/latest/quick_start.html​
- Pygame Sprite documentation: https://www.pygame.org/docs/ref/sprite.html​
