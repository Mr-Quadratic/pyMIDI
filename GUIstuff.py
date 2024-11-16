import pygame
import pygame_gui
from pygame_gui.core import ObjectID

pygame.init()

#Initialize GUI window
pygame.display.set_caption('PYANO Dev GUI')
window_surface = pygame.display.set_mode((1600, 800))
background = pygame.Surface((1600, 600))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((1600, 1000), theme_path = 'theme.json')



#Lists for mapping notes to keys
notes = ['C','D','E','F','G','A','B']
flats_first = ['Db','Eb']
flats_second = ['Gb','Ab','Bb']
flat_position = [1,2]
init_key_coord = 0
init_flat_coord = 0
octave = 1


##Generate interactive piano key buttons
#Generate white keys
while octave <= 5:
	for key in notes:
		key = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((init_key_coord, 650), (50, 150)),
		                                   text= f'{key}{octave}',
		                                   manager=manager)
		init_key_coord += 50
	octave += 1

black_keys = pygame.sprite.Group()
octave = 1
#Generate black keys (annoying because of the sort-of inconsistent spacing)
while octave <= 5:
	for pos in flat_position:
		if pos == 1:
			for key in flats_first:
				init_flat_coord = 0
				init_flat_coord += (37.5 + 50 * 7 * (octave-1))
				init_flat_coord += (50 * flats_first.index(key))
				key = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((init_flat_coord, 650), (25, 100)),
				                                   text = f'{key}{octave}',
				                                   manager=manager,
				                                   object_id=ObjectID(class_id='@black_button'))
				black_keys.add(key)
		if pos == 2:
			for key in flats_second:
				init_flat_coord = 0
				init_flat_coord += (187.5 + 50 * 7 * (octave-1))
				init_flat_coord += 50 * flats_second.index(key)
				key = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((init_flat_coord, 650), (25, 100)),
				                                   text = f'{key}{octave}',
				                                   manager=manager,
				                                   object_id=ObjectID(class_id='@black_button'))
				black_keys.add(key)
	octave += 1

