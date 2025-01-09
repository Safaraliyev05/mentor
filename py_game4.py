import pygame

pygame.init()
window = pygame.display.set_mode((800, 800))
car_photo = pygame.image.load('car.png')
_photo = pygame.image.load('car.png')

running = True
while running:
    window.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
