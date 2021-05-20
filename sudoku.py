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
        self.selected = None
        self.selected_list = []
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x+1, self.y+1, self.block_size-1, self.block_size-1))
    
    def select(self, pos, win):
        self.selected = pos
        self.selected_list = self.selected
        # self.draw_selected(win)
    
    '''def draw_selected(self, win):
        pygame.draw.rect(win, self.selected_color, (self.selected[0], self.selected[1], self.block_size, self.block_size), 2)'''

def get_grid(total_rows, width):
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

def get_click(pos, rows, width):
    x, y = pos
    block_size = width//rows

    row = y // block_size
    col = x // block_size

    return row, col, x, y

def redraw_window(win, width, total_rows, grid):
    win.fill((255, 255, 255))
    draw_lines(win, total_rows, width)
    block_size = width//total_rows

    for row in grid:
        for spot in row:
            spot.draw(win)
    for i in range(total_rows):
        for j in range(total_rows):
            for block in grid[i][j].selected_list:
                x = 0
                y = 0
                print(block)
                pygame.draw.rect(win, (255, 0, 0), (x, y, block_size, block_size), 2)

def main(win, width):
    run = True
    ROWS = 9

    grid = get_grid(ROWS, width)

    while run:
        redraw_window(win, width, ROWS, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    row, col, real_x, real_y = get_click(pos, ROWS, width)
                    grid[row][col].select(pos, win)

        pygame.display.update()

main(WIN, WIDTH)