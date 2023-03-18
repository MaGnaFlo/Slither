import pygame as pg
from pygame.locals import QUIT

WIDTH, HEIGHT = 640, 480 
RED = (255,0,0)
MOVE_LEFT = -1
MOVE_RIGHT = 1 
MOVE_UP = -2
MOVE_DOWN = 2
INITIAL_PARTS = 8


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
	def __init__(self, n_start=3):
		super().__init__()

		self._dpos = 20
		self.direction = MOVE_DOWN

		for i in range(n_start):
			part = SnakePart((0,0), (20, 20), RED)
			part.set_pos((240, 100-self._dpos*i))
			self.add(part)

	def get_head(self):
		for part in self:
			break
		return part

	def update_pos(self, direction):
		if self.direction == -direction:
			direction = -direction
		else:
			self.direction = direction

		for i, part in enumerate(self):
			if i == 0:
				current_pos = part.get_pos()
				if direction == MOVE_LEFT:
					part.set_pos((current_pos[0]-self._dpos, current_pos[1]))
				elif direction == MOVE_RIGHT:
					part.set_pos((current_pos[0]+self._dpos, current_pos[1]))
				elif direction == MOVE_UP:
					part.set_pos((current_pos[0], current_pos[1]-self._dpos))
				elif direction == MOVE_DOWN:
					part.set_pos((current_pos[0], current_pos[1]+self._dpos))
				
			else:
				temp = part.get_pos()
				part.set_pos(current_pos)
				current_pos = temp

	def check_collisions(self):
		
		x, y = self.get_head().get_pos()

		# with borders
		collide = False
		if x >= WIDTH-1 or x < 0 or y >= HEIGHT-1 or y < 0:
			collide = True

		# with itself
		for part in self:
			if part == self.get_head():
				continue
			x_, y_ = part.get_pos()
			if x == x_ and y == y_:
				collide = True
				break

		return collide





pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Slither")


# init the snake
snake = Snake(INITIAL_PARTS)



clock = pg.time.Clock()


# main loop

move_left = False
move_right = False
move_up = False
move_down = True

running = True
while running:
	for event in pg.event.get():

		if event.type == QUIT:
			running = False
		elif event.type == pg.KEYDOWN:

			if event.key == pg.K_q:
				running = False

			if event.key == pg.K_LEFT:
				move_right = False
				move_up = False
				move_down = False
				move_left = True
			if event.key == pg.K_RIGHT:
				move_left = False
				move_up = False
				move_down = False
				move_right = True
			if event.key == pg.K_UP:
				move_left = False
				move_right = False
				move_down = False
				move_up = True
			if event.key == pg.K_DOWN:
				move_left = False
				move_right = False
				move_up = False
				move_down = True

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
	collide = snake.check_collisions()

	if collide:
		print("collided", snake.get_head().get_pos())

	snake.draw(screen)

	clock.tick(10)

	pg.display.flip()


pg.quit()



