import pygame

WIDTH = 765
WIN = pygame.display.set_mode((WIDTH, WIDTH))

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.width = width
        self.total_rows = total_rows
        self.block_size = self.width//self.total_rows
        self.row = row
        self.col = col
        self.x = self.col * self.block_size
        self.y = self.row * self.block_size
        self.color = (255, 255, 255)
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.block_size, self.block_size))

def grid(total_rows, width):
    grid = []
    for i in range(total_rows):
        grid.append([])
        for j in range(total_rows):
            spot = Spot(i, j, width, total_rows)
            grid[i].append(spot)
    
    return grid

def draw_lines(win, total_rows, width):
    block_size = width//total_rows
    for i in range(0, width, block_size):
        pygame.draw.line(win, (0, 0, 0), (i, 0), (i, width))
        pygame.draw.line(win, (0, 0, 0), (0, i), (width, i))

def redraw_window(win, width, total_rows, grid):
    win.fill((255, 255, 255))
    draw_lines(win, total_rows, width)

    for row in grid:
        for spot in row:
            spot.draw(win)

def main(win, width):
    run = True
    ROWS = 9

    grid = grid(ROWS, width)

    while run:
        redraw_window(win, width, ROWS, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

main(WIN, WIDTH)