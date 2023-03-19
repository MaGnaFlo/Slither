import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
from pygame.locals import QUIT
from parameters import *
from snake import Snake, Food
from gui import *

# First display GUI.
active = start_window() # controls the outer loop: application as a whole.

while active:

	pg.init()
	screen = pg.display.set_mode((WIDTH, HEIGHT))
	pg.display.set_caption("Slither")

	# init the snake
	snake = Snake(INITIAL_PARTS)

	# first food
	food = Food()

	# init movements, starting with going down.
	move_left = False
	move_right = False
	move_up = False
	move_down = True

	clock = pg.time.Clock()

	score = 0

	running = True # controls the game loop.
	while running:

		for event in pg.event.get():

			if event.type == QUIT:
				running = False
				active = False

			# key down means changing direction
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_q:
					running = False
					active = False

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

		# update position according to the current direction.
		if move_left:
			snake.update_pos(MOVE_LEFT)
		elif move_right:
			snake.update_pos(MOVE_RIGHT)
		elif move_up:
			snake.update_pos(MOVE_UP)
		elif move_down:
			snake.update_pos(MOVE_DOWN)

		# update the snake, check for collisions and swallowing food.
		snake.update()
		if snake.check_collisions():
			active = collide_window(score)
			running = False

		swallowed = snake.swallow_food(food)
		if swallowed:
			snake.add_part()
			food = Food()
			score += 1
		food.update()

		# draw scene
		screen.fill(BLACK)
		snake.draw(screen)
		food.draw(screen)

		# clock and flip
		clock.tick(FRAMES_PER_SECOND)
		pg.display.flip()

	pg.quit()



