import pygame

pygame.init()

cat_photo = pygame.image.load('ball.png')
cat_photo = pygame.transform.scale(cat_photo, (50, 50))
# cat_photo = pygame.transform.rotate(cat_photo, 120)
# cat_photo = pygame.transform.flip(cat_photo, True, False)

window = pygame.display.set_mode((750, 750))

x = 0
y = 0
jump = False
jump_speed = 15

running = True
while running:
    window.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1

    if jump is False and keys[pygame.K_SPACE]:
        jump = True
    if jump is True:
        y += 1
    window.blit(cat_photo, (x, y))

    pygame.display.update()

pygame.quit()
