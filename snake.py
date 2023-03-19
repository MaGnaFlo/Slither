import numpy as np
import pygame as pg
from parameters import *


class SnakePart(pg.sprite.Sprite):
	''' Handles a single snake part sprite.'''
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
	''' Snake as a sum of its parts'''
	def __init__(self, n_start=3):
		super().__init__()

		self.direction = MOVE_DOWN

		for i in range(n_start):
			part = SnakePart((0,0), (DELTA_POS, DELTA_POS), RED)
			part.set_pos((240, 100-DELTA_POS*i))
			self.add(part)

	def add_part(self):
		''' Used to add a new element at the tail. '''
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

		part = SnakePart((0,0), (DELTA_POS, DELTA_POS), RED)
		part.set_pos((x,y))
		self.add(part)

	def get_head(self):
		''' Returns the first part of the snake. '''
		return self.sprites()[0]

	def get_tail(self):
		''' Returns the last part of the snake. '''
		return self.sprites()[-1]

	def update_pos(self, direction):
		''' Handles the update of the parts of the snake, depening
			on the current direction the head is going. 
		'''
		if self.direction == -direction:
			direction = -direction
		else:
			self.direction = direction

		for part in self:
			if part == self.get_head(): 
				# this is the head. just update its new direction and position.
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
				# successively update the next parts, one after the other
				# which become the next part, etc.
				temp_pos = part.get_pos()
				temp_dir = part.get_direction()
				part.set_pos(current_pos)
				part.set_direction(current_direction)
				current_pos = temp_pos
				current_direction = temp_dir

	def check_collisions(self):
		''' Checks if the head hits a wall or any other part of the snake. '''
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
		''' Checks if we hit a food. Returns a boolean
			according to whether or not the food must be 
			killed and a new food created.
		'''
		x, y = self.get_head().get_pos()
		x_food, y_food = food.get_pos()
		if x == x_food and y == y_food:
			return True
		else:
			return False


class Food(pg.sprite.Sprite):
	''' Class managing a single food element. '''
	def __init__(self, size=(DELTA_POS, DELTA_POS), color=YELLOW):
		self.image = pg.Surface(size)
		pg.draw.rect(self.image, color, pg.Rect(0, 0, *size))
		self.rect = self.image.get_rect()

		# the position is random within the lattice.
		self.rect.x = np.random.randint(WIDTH // DELTA_POS) * DELTA_POS
		self.rect.y = np.random.randint(HEIGHT // DELTA_POS) * DELTA_POS

	def get_pos(self):
		return (self.rect.x, self.rect.y)

	def draw(self, screen):
		screen.blit(self.image, self.rect)
