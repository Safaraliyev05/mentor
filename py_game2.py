# import pygame
#
# pygame.init()
# window = pygame.display.set_mode((1000, 1000))
#
# x = 250
# y = 225
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 x += 5
#             elif event.key == pygame.K_LEFT:
#                 x -= 5
#             elif event.key == pygame.K_UP:
#                 y += 5
#             else:
#                 y -= 5
#
#     window.fill('WHITE')
#     pygame.draw.rect(window, 'BLUE', (x, y, 50, 50))
#     pygame.display.update()
#
# pygame.quit()

import pygame

pygame.init()
window = pygame.display.set_mode((600, 600))

running = True
x = 250
y = 225

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    window.fill(('white'))
    pygame.draw.rect(window, ('blue'), (x, y, 50, 50))
    pygame.display.update()

pygame.quit()
