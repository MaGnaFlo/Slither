import pygame as pg
from pygame.locals import QUIT
import numpy as np

WIDTH, HEIGHT = 640, 480 
RED = (255, 0 ,0)
YELLOW = (255, 255, 0)
MOVE_LEFT = -1
MOVE_RIGHT = 1 
MOVE_UP = -2
MOVE_DOWN = 2
INITIAL_PARTS = 8
DELTA_POS = 20


class SnakePart(pg.sprite.Sprite):
	def __init__(self, pos, size, color, direction=MOVE_DOWN):
		super().__init__()

		self.image = pg.Surface(size)
		pg.draw.rect(self.image, color, pg.Rect(*pos, *size))
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

		self._direction = direction

	def set_pos(self, pos):
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def get_pos(self):
		return (self.rect.x, self.rect.y)

	def set_direction(self, direction):
		self._direction = direction

	def get_direction(self):
		return self._direction


class Snake(pg.sprite.Group):
	def __init__(self, n_start=3):
		super().__init__()

		self.direction = MOVE_DOWN

		for i in range(n_start):
			part = SnakePart((0,0), (20, 20), RED)
			part.set_pos((240, 100-DELTA_POS*i))
			self.add(part)

	def add_part(self):
		tail = self.get_tail()
		if tail.get_direction() == MOVE_DOWN:
			x = tail.get_pos()[0] 
			y = tail.get_pos()[1] - DELTA_POS

		if tail.get_direction() == MOVE_UP:
			x = tail.get_pos()[0] 
			y = tail.get_pos()[1] + DELTA_POS

		if tail.get_direction() == MOVE_LEFT:
			x = tail.get_pos()[0] - DELTA_POS
			y = tail.get_pos()[1]

		if tail.get_direction() == MOVE_RIGHT:
			x = tail.get_pos()[0] 
			y = tail.get_pos()[1] + DELTA_POS

		part = SnakePart((0,0), (20, 20), RED)
		part.set_pos((x,y))
		self.add(part)

	def get_head(self):
		return self.sprites()[0]

	def get_tail(self):
		return self.sprites()[-1]

	def update_pos(self, direction):
		if self.direction == -direction:
			direction = -direction
		else:
			self.direction = direction

		for i, part in enumerate(self):
			if i == 0:
				current_pos = part.get_pos()
				current_direction = part.get_direction()
				if direction == MOVE_LEFT:
					part.set_pos((current_pos[0] - DELTA_POS, current_pos[1]))
				elif direction == MOVE_RIGHT:
					part.set_pos((current_pos[0] + DELTA_POS, current_pos[1]))
				elif direction == MOVE_UP:
					part.set_pos((current_pos[0], current_pos[1] - DELTA_POS))
				elif direction == MOVE_DOWN:
					part.set_pos((current_pos[0], current_pos[1] + DELTA_POS))
				part.set_direction(direction)

			else:
				temp_pos = part.get_pos()
				temp_dir = part.get_direction()
				part.set_pos(current_pos)
				part.set_direction(current_direction)
				current_pos = temp_pos
				current_direction = temp_dir

	def check_collisions(self, food):
		
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

	def swallow_food(self, food):
		x, y = self.get_head().get_pos()
		x_food, y_food = food.get_pos()
		if x == x_food and y == y_food:
			return True
		else:
			return False


class Food(pg.sprite.Sprite):
	def __init__(self, size=(20,20), color=YELLOW):
		self.image = pg.Surface(size)
		pg.draw.rect(self.image, color, pg.Rect(0, 0, *size))
		self.rect = self.image.get_rect()

		self.rect.x = np.random.randint(WIDTH // DELTA_POS) * DELTA_POS
		self.rect.y = np.random.randint(HEIGHT // DELTA_POS) * DELTA_POS

	def get_pos(self):
		return (self.rect.x, self.rect.y)

	def draw(self, screen):
		screen.blit(self.image, self.rect)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Slither")


# init the snake
snake = Snake(INITIAL_PARTS)

food = Food()
clock = pg.time.Clock()


move_left = False
move_right = False
move_up = False
move_down = True

food = Food()

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
	collide = snake.check_collisions(food)
	swallowed = snake.swallow_food(food)
	if swallowed:
		snake.add_part()
		food = Food()

	if collide:
		print("collided", snake.get_head().get_pos())
	snake.draw(screen)

	food.update()
	food.draw(screen)

	clock.tick(10)
	pg.display.flip()


pg.quit()



