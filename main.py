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
		self.x = self.col * self.gap+2
		self.y = self.row * self.gap+2
		self.color = (255, 255, 255)

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
	BLACK_ROWS = 3
	for i in range(WIDTH//rows, WIDTH - WIDTH//rows, WIDTH//rows):
		pygame.draw.line(win, (0, 0, 0), (i, 0), (i, WIDTH), 1)
		pygame.draw.line(win, (0, 0, 0), (0, i), (WIDTH, i), 1)
	for i in range(WIDTH//BLACK_ROWS, WIDTH, WIDTH//BLACK_ROWS):
		pygame.draw.line(win, (0, 0, 0), (i, 0), (i, WIDTH), 3)
		pygame.draw.line(win, (0, 0, 0), (0, i), (WIDTH, i), 3)

def redraw_window(win, rows, grid):
	win.fill((255, 255, 255))

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows)

def click(pos, rows):
	x = pos[0]
	y = pos[1]

	row = y // WIDTH // rows
	col = x // WIDTH // rows

	return row, col

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
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				row, col = click(pos, ROWS)
				print(row, col)

		pygame.display.update()

main(WIN)

