import os
import pygame

# UPDATE GITHUB
# git commit -m "Initial Commmit"
# ------------------------------------------
os.system('git add .')
os.system('git commit -m "Initial Commit"')
os.system('git push')
# ------------------------------------------

WIDTH = 750

WIN = pygame.display.set_mode((WIDTH, WIDTH))

class Spot:
	def __init__(self, row, col, total_rows):
		self.row = row
		self.col = col
		self.total_rows = total_rows
		self.gap = WIDTH // self.total_rows
		self.x = self.col * self.gap+1
		self.y = self.row * self.gap+1
		self.color = (255, 0, 0)

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.gap, self.gap), 0)

def get_grid(rows):
	grid = []

	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, rows)
			grid[i].append(spot)

	return grid

def draw_grid(win, rows):
	pass

def redraw_window(win, rows, grid):
	win.fill((255, 255, 255))
	draw_grid(win, rows)

	for row in grid:
		for spot in row:
			spot.draw(win)


def main(win):
	ROWS = 9
	grid = get_grid(ROWS)

	run = True

	while run:
		redraw_window(win, ROWS, grid)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

		pygame.display.update()

main(WIN)

