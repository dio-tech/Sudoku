import os
import pygame

# UPDATE GITHUB
# git commit -m "Initial Commmit"
os.system('git add .')
os.system('git commit -m "Initial Commit"')
os.system('git push')

WIDTH = 750

WIN = pygame.display.set_mode((WIDTH, WIDTH))

class Spot:
	def __init__(self, row, col, total_rows):
		self.row = row
		self.col = col
		self.total_rows = total_rows
		self.gap = WIDTH // self.total_rows
		self.color = (255, 255, 255)

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.row, self.col, self.gap, self.gap), 0)

def main(win):
	ROWS = 9

	run = True

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

main(WIN)

