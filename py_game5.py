import pygame

pygame.init()
window_size = 500
window = pygame.display.set_mode((window_size, window_size))
grid_size = window_size // 3
x = pygame.image.load("x.png")
x = pygame.transform.scale(x, (240, 250))

o = pygame.image.load('0.png')
o = pygame.transform.scale(o, (250, 250))
running = True
while running:
    for n in range(1, 3):
        pygame.draw.line(window, 'white', (0, n * grid_size), (window_size, n * grid_size), 2)
    for n in range(1, 3):
        pygame.draw.line(window, 'white', (n * grid_size, 0), (n * grid_size, window_size), 2)
    pygame.display.update()
pygame.quit()
