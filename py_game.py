import pygame

pygame.init()

window = pygame.display.set_mode((600, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill('white')
    # Uncomment any of the following lines to test different shapes
    # pygame.draw.rect(window, 'blue', pygame.Rect(100, 100, 70, 70))
    # pygame.draw.rect(window, 'green', pygame.Rect(100, 100, 70, 70), width=10)
    # pygame.draw.circle(window, 'green', (400, 50), 70)
    # pygame.draw.line(window, 'red', (0, 225), (500, 225), 30)
    # pygame.draw.polygon(window, 'yellow', [(100, 100), (200, 50), (300, 100), (250, 200), (150, 200)])
    pygame.draw.polygon(window, 'red', [(250, 225), (350, 150), (450, 225), (450, 325), (350, 400), (250, 325)])
    pygame.display.update()

pygame.quit()
