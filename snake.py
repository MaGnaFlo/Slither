import pygame as pg

from pygame.locals import QUIT


WIDTH, HEIGHT = 640, 480 
RED = (255,0,0)

class SnakePart(pg.sprite.Sprite):
	def __init__(self, width, height, color):
		super().__init__()

		self.image = pg.Surface([width, height])
		pg.draw.rect(self.image, color, pg.Rect(0,0,width, height))
		self.rect = self.image.get_rect()



pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("The Snake")

snake = pg.sprite.Group()

part = SnakePart(20, 20, RED)
part.rect.x = 200
part.rect.y = 200

snake.add(part)


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
		for part in snake:
			part.rect.x -= 20
	elif move_right:
		for part in snake:
			part.rect.x += 20
	elif move_up:
		for part in snake:
			part.rect.y -= 20
	elif move_down:
		for part in snake:
			part.rect.y += 20

	screen.fill((0,0,0))
	snake.update()
	snake.draw(screen)

	clock.tick(10)

	pg.display.flip()
pg.quit()



