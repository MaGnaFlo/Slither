import pygame as pg
from pygame.locals import QUIT
from parameters import *
from snake import Snake, Food


# from PyQt5.Widgets import QApplication, QWidget

# import sys
# app = QApplication(sys.argv)
# window = QWidget()
# window.show()
# app.exec()


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

		# key down means changing direction
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
	collide = snake.check_collisions()
	if collide:
		print("collided", snake.get_head().get_pos()) # todo

	swallowed = snake.swallow_food(food)
	if swallowed:
		snake.add_part()
		food = Food()
	food.update()

	# draw scene
	screen.fill((0,0,0))
	snake.draw(screen)
	food.draw(screen)

	# clock and flip
	clock.tick(FRAMES_PER_SECOND)
	pg.display.flip()

pg.quit()



