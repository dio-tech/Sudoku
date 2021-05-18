import pygame

WIDTH = 750
WIN = pygame.display.set_mode((WIDTH, WIDTH))

def redraw_window(win):
    win.fill((255, 255, 255))

def main(win):
    run = True

    while run:
        redraw_window(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

main(WIN)