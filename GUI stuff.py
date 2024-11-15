import pygame
import pygame_gui
from pygame_gui.core import ObjectID

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600), theme_path = 'theme.json')

C = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 300), (100, 300)),
                                            text='t',
                                            manager=manager)
D = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 300), (100, 300)),
                                            text='y',
                                            manager=manager)
E = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 300), (100, 300)),
                                            text='u',
                                            manager=manager)
F = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 300), (100, 300)),
                                            text='i',
                                            manager=manager)
G = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 300), (100, 300)),
                                            text='o',
                                            manager=manager)
A = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 300), (100, 300)),
                                            text='p',
                                            manager=manager)
B = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 300), (100, 300)),
                                            text='a',
                                            manager=manager)

Db = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((75, 300), (50, 150)), text = 'T', manager=manager,object_id=ObjectID(class_id='@black_button'))
Eb = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((175, 300), (50, 150)), text = 'Y', manager=manager,object_id=ObjectID(class_id='@black_button'))
Fb = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((375, 300), (50, 150)), text = 'I', manager=manager,object_id=ObjectID(class_id='@black_button'))
Gb = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((475, 300), (50, 150)), text = 'O', manager=manager,object_id=ObjectID(class_id='@black_button'))
Ab = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((575, 300), (50, 150)), text = 'P', manager=manager,object_id=ObjectID(class_id='@black_button'))

buttons = [C,D,E,F,G,A,B]






clock = pygame.time.Clock()
is_running = True

while is_running:
	time_delta = clock.tick(60) / 1000.0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False

		if event.type == pygame_gui.UI_BUTTON_PRESSED:
			if event.ui_element in buttons:
				print('This does nothing yet!')

		manager.process_events(event)

	manager.update(time_delta)

	window_surface.blit(background, (0, 0))
	manager.draw_ui(window_surface)

	pygame.display.update()