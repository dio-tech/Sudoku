import pygame
import time
from solver import solve
pygame.font.init()

WIDTH = 720
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Sudoku')

class Grid:
	board = [
		[7,8,0,4,0,0,1,2,0],
		[6,0,0,0,7,5,0,0,9],
		[0,0,0,6,0,1,0,7,8],
		[0,0,7,0,4,0,2,6,0],
		[0,0,1,0,5,0,9,3,0],
		[9,0,4,0,6,0,0,0,5],
		[0,7,0,3,0,0,0,1,2],
		[1,2,0,0,0,7,4,0,0],
		[0,4,9,2,0,6,0,0,7]
	]

	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.width = width
		self.total_rows = total_rows
		self.block_size = self.width//self.total_rows
	
def draw_lines(win, width, block_size):
	for i in range(block_size, width, block_size):
		pygame.draw.line(win, (0, 0, 0), (i, width), (width, i))
		pygame.draw.line(win, (0, 0, 0), (width, i), (i, width))

def redraw(win, width, block_size):
	win.fill((255, 255, 255))
	draw_lines(win, width, block_size)

def main(win, width):
	run = True
	ROWS = 9

	block_size = width//ROWS

	while run:
		redraw(win, width, block_size)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

main(WIN, WIDTH)