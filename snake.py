import pygame as pg

from pygame.locals import QUIT


WIDTH, HEIGHT = 640, 480 
RED = (255,0,0)
MOVE_LEFT = 0 
MOVE_RIGHT = 1 
MOVE_UP = 2 
MOVE_DOWN = 3

class SnakePart(pg.sprite.Sprite):
	def __init__(self, pos, size, color):
		super().__init__()

		self.image = pg.Surface(size)
		pg.draw.rect(self.image, color, pg.Rect(*pos, *size))
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

	def set_pos(self, pos):
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def get_pos(self):
		return (self.rect.x, self.rect.y)


class Snake(pg.sprite.Group):
	def __init__(self):
		super().__init__()

		self._dpos = 20
		self.pos_list = []

	def add_part(self, part):
		super().add(part)
		self.pos_list.append(part.get_pos())

	def update_pos(self, direction):
		current_pos = (0,0)
		for i, part in enumerate(self):
			if i == 0:
				current_pos = part.get_pos()
				if direction == MOVE_LEFT:
					part.set_pos((current_pos[0]-self._dpos, current_pos[1]))
				if direction == MOVE_RIGHT:
					part.set_pos((current_pos[0]+self._dpos, current_pos[1]))
				if direction == MOVE_UP:
					part.set_pos((current_pos[0], current_pos[1]-self._dpos))
				if direction == MOVE_DOWN:
					part.set_pos((current_pos[0], current_pos[1]+self._dpos))
				
			else:
				temp = part.get_pos()
				part.set_pos(current_pos)
				current_pos = temp




pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Slither")


# init the snake
snake = Snake()

part = SnakePart((0,0), (20, 20), RED)
part.set_pos((200,200))

part2 = SnakePart((0,0), (20, 20), RED)
part2.set_pos((220,200))

part3 = SnakePart((0,0), (20, 20), RED)
part3.set_pos((240,200))

snake.add_part(part)
snake.add_part(part2)
snake.add_part(part3)






clock = pg.time.Clock()


# main loop

move_left = False
move_right = False
move_up = False
move_down = False

running = True
while running:
	for event in pg.event.get():

		if event.type == QUIT:
			running = False
		elif event.type == pg.KEYDOWN:

			if event.key == pg.K_q:
				running = False

			if event.key == pg.K_LEFT:
				move_left = True
			elif event.key == pg.K_RIGHT:
				move_right = True
			elif event.key == pg.K_UP:
				move_up = True
			elif event.key == pg.K_DOWN:
				move_down = True

		elif event.type == pg.KEYUP:
			if event.key == pg.K_LEFT:
				move_left = False
			elif event.key == pg.K_RIGHT:
				move_right = False
			elif event.key == pg.K_UP:
				move_up = False
			elif event.key == pg.K_DOWN:
				move_down = False
				
	if move_left:
		snake.update_pos(MOVE_LEFT)
	elif move_right:
		snake.update_pos(MOVE_RIGHT)
	elif move_up:
		snake.update_pos(MOVE_UP)
	elif move_down:
		snake.update_pos(MOVE_DOWN)


	screen.fill((0,0,0))
	snake.update()
	snake.draw(screen)

	clock.tick(10)

	pg.display.flip()
pg.quit()



