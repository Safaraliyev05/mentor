import pygame
pygame.init()
window = pygame.display.set_mode((750, 750))

font = pygame.font.SysFont('Tahoma', 40, 'bold')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill('black')
    score = 0
    text = font.render(f'{score}', True, 'yellow')

    window.blit(text, (300, 50))

    pygame.display.update()

pygame.quit()
