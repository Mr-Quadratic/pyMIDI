import pygame
import pygame_gui
from pygame_gui.core import ObjectID

pygame.init()

#Initialize GUI window
pygame.display.set_caption('PYANO Dev GUI')
GUI_display = pygame.display.set_mode((1600, 800))
background = pygame.Surface((1600, 800))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((1600, 1000), theme_path = 'theme.json')


class PressedSprite(pygame.sprite.Sprite):
	def __init__(self,color,x,y):
		super().__init__()
		self.image = pygame.Surface((45,145))
		self.image.fill(color)
		self.rect = self.image.get_rect(center = (x,y))

class Tile(pygame.sprite.Sprite):
	def __init__(self,color,x,y,w,l):
		super().__init__()
		self.image = pygame.Surface((w,l))
		self.image.fill(color)
		self.rect = self.image.get_rect(center = (x,y))

allSprites = pygame.sprite.Group()
allTiles = pygame.sprite.Group()

#Lists for mapping notes to keys
notes = ['C','D','E','F','G','A','B']
flats_first = ['Db','Eb']
flats_second = ['Gb','Ab','Bb']
flat_position = [1,2]
init_key_coord = 0
init_flat_coord = 0
octave = 1

notes_to_keys = {}

l = 0

##Generate interactive piano key buttons
#Generate white keys
while octave <= 7:
	for key in notes:
		key = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((init_key_coord, 650), (50, 150)),
		                                   text= f'{key}{octave}',
		                                   manager=manager)
		notes_to_keys[key.text] = init_key_coord
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

vol_rect = pygame.Rect(100, 100, 200, 30)
volume = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=vol_rect,
    start_value=50,
    value_range = (0,100),
    manager=manager
)
fade_rect = pygame.Rect(100, 150, 200, 30)
fade = pygame_gui.elements.UIHorizontalSlider(
relative_rect=fade_rect,
    start_value=600,
    value_range = (0,1500),
    manager=manager
)

label = pygame_gui.elements.UILabel(
	relative_rect = vol_rect,
	text = 'Volume'
)
label2 = pygame_gui.elements.UILabel(
	relative_rect = fade_rect,
	text = 'Release time (ms)'
)

display_rect = pygame.Rect(225,100,200,30)
labeldisp = pygame_gui.elements.UILabel(
	relative_rect = display_rect,
	text = str(volume.get_current_value())
)
display_rect2 = pygame.Rect(225,150,200,30)
labeldisp2 = pygame_gui.elements.UILabel(
	relative_rect = display_rect2,
	text = str(fade.get_current_value())
)