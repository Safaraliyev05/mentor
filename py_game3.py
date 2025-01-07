import pygame

pygame.init()
cat_photo = pygame.image.load('cat.png')
cat_photo = pygame.transform.scale(cat_photo, (750, 750))
# cat_photo = pygame.transform.rotate(cat_photo, 120)
cat_photo = pygame.transform.flip(cat_photo, True, False)
window = pygame.display.set_mode((750, 750))

running = True
while running:
    window.fill('white')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.blit(cat_photo, (0, 0))
    pygame.display.update()

pygame.quit()
