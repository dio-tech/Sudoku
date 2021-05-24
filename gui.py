import pygame
import time
from solver import solve
pygame.font.init()

WIDTH = 720
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Sudoku')

BOARD = [
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

COPY_BOARD = [
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

solved = solve(COPY_BOARD)

class Grid:
	def __init__(self, width, total_rows, board):
		self.board = board
		self.width = width
		self.total_rows = total_rows
		self.block_size = self.width//self.total_rows
		self.the_selected = []
		self.grid = self.get_actual_grid()
		self.choices = []
		self.copy_board = self.board
		self.number_pos = []
		self.tries = 3
	
	def get_actual_grid(self):
		grid = []
		for i in range(self.total_rows):
			grid.append([])
			for j in range(self.total_rows):
				font = pygame.font.SysFont('comicsans', 60)
				text = font.render('0', True, (255, 255, 255))
				x = j * self.block_size
				y = i * self.block_size
				grid[i].append([text, (x, y), (text.get_width(), text.get_height()), [i, j]])
		
		return grid

	
	def get_selected(self, pos):
		self.the_selected.clear()
		row, col = pos
		x = col * self.block_size
		y = row * self.block_size
		self.the_selected.append((x, y))
	
	def draw_selected(self, win):
		if len(self.the_selected) > 0:
			row = self.the_selected[0][1] // self.block_size
			col = self.the_selected[0][0] // self.block_size 
			self.selected = (row, col)
		else:
			self.selected = None
		for pos in self.the_selected:
			pygame.draw.rect(win, (255, 0, 0), (pos[0], pos[1], self.block_size, self.block_size), 2)
	
	def draw_board(self):
		font = pygame.font.SysFont('comicsans', 60)
		for row in self.board:
			n = 0
			for number in self.board[self.board.index(row)]:
				if number != 0:
					text = font.render(str(number), True, (0, 0, 0))
					x = n * self.block_size
					y = self.board.index(row) * self.block_size
					self.grid[self.board.index(row)][n] = [text, (x, y), (text.get_width(), text.get_height()),
						(self.board.index(row), n)]
				n += 1
	
	def get_choice(self, choice):
		x = self.selected[1] * self.block_size
		y = self.selected[0] * self.block_size
		if (x, y) in self.number_pos:
			self.choices[self.number_pos.index((x, y))] = [choice, (x, y)]
		if [choice, (x, y)] not in self.choices:
			self.choices.append([choice, (x, y)])
			self.number_pos.append((x, y))
	
	def blit_choices(self, win):
		font = pygame.font.SysFont('comicsans', 40)
		for choice in self.choices:
			text = font.render(str(choice[0]), True, (128, 128, 128))
			win.blit(text, (choice[1][0] + 2, choice[1][1] + 2))
	
	def delete_choices(self):
		x = self.selected[1] * self.block_size
		y = self.selected[0] * self.block_size
		for choice in self.choices:
			if choice[1] == (x, y):
				self.choices.remove(choice)
				self.number_pos.remove(self.number_pos[self.number_pos.index((x, y))])
	
	def update_board(self):
		font = pygame.font.SysFont('comicsans', 60)
		x = self.selected[1] * self.block_size
		y = self.selected[0] * self.block_size
		if (x, y) in self.number_pos:
			choice = self.choices[self.number_pos.index((x, y))]
		else:
			choice = None
		if choice:
			if choice[0] == COPY_BOARD[self.selected[0]][self.selected[1]]:
				text = font.render(str(choice[0]), True, (0, 255, 0))
			else:
				text = font.render(str(choice[0]), True, (255, 0, 0))
				self.tries -= 1
			self.grid[self.selected[0]][self.selected[1]] = [text, (x, y), (text.get_width(), text.get_height()), self.selected]
			self.choices.remove(self.choices[self.number_pos.index((x, y))])
			self.number_pos.remove(self.number_pos[self.number_pos.index((x, y))])
	
	def delete_from_board(self):
		font = pygame.font.SysFont('comicsans', 60)
		x = self.selected[1] * self.block_size
		y = self.selected[0] * self.block_size
		text = font.render('0', True, (255, 255, 255))
		self.grid[self.selected[0]][self.selected[1]] = [text, (x, y), (text.get_width(), text.get_height()), self.selected]
	
	def lost(self):
		if self.tries == 0:
			return True
		return False

	
def draw_lines(win, width, block_size):
	for i in range(block_size, width, block_size):
		pygame.draw.line(win, (0, 0, 0), (i, width), (i, 0))
		pygame.draw.line(win, (0, 0, 0), (width, i), (0, i))
	for i in range(3 * block_size, width, 3 * block_size):
		pygame.draw.line(win, (0, 0, 0), (i, width), (i, 0), 5)
		pygame.draw.line(win, (0, 0, 0), (width, i), (0, i), 5)

def click(pos, block_size):
	x, y = pos
	row = y // block_size
	col = x // block_size

	return row, col

def redraw(win, width, block_size, grid):
	win.fill((255, 255, 255))
	draw_lines(win, width, block_size)
	for row in grid.grid:
		for spot in row:
			win.blit(spot[0], ((spot[1][0] + block_size) // 2 - spot[2][0]//2 + (spot[3][1] * block_size//2),
				(spot[1][1] + block_size) // 2 - spot[2][1] // 2 + (spot[3][0] * block_size//2)))
	grid.draw_board()
	grid.blit_choices(win)

	grid.draw_selected(win)

def main(win, width, board):
	run = True
	ROWS = 9

	grid = Grid(width, ROWS, board)

	block_size = width//ROWS

	while run:
		redraw(win, width, block_size, grid)
		if grid.lost():
			print('you lost')
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					pos = pygame.mouse.get_pos()
					row, col = click(pos, block_size)
					grid.get_selected((row, col))
					# print(grid.board[row][col])
			keys = pygame.key.get_pressed()
			if keys[pygame.K_1]:
				grid.get_choice(1)
			if keys[pygame.K_2]:
				grid.get_choice(2)
			if keys[pygame.K_3]:
				grid.get_choice(3)
			if keys[pygame.K_4]:
				grid.get_choice(4)
			if keys[pygame.K_5]:
				grid.get_choice(5)
			if keys[pygame.K_6]:
				grid.get_choice(6)
			if keys[pygame.K_7]:
				grid.get_choice(7)
			if keys[pygame.K_8]:
				grid.get_choice(8)
			if keys[pygame.K_9]:
				grid.get_choice(9)
			if keys[pygame.K_BACKSPACE]:
				grid.delete_choices()
				grid.delete_from_board()
			if keys[pygame.K_RETURN]:
				grid.update_board()
		pygame.display.update()

main(WIN, WIDTH, BOARD)