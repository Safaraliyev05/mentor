import pygame

pygame.init()
window_width, window_height = 1280, 800
window = pygame.display.set_mode((window_width, window_height))

ball = pygame.Rect(0, 0, 30, 30)
ball.center = (window_width / 2, window_height / 2)
ball_speed_x, ball_speed_y = 1, 1

running = True
while running:
    window.fill('black')

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.x >= window_width - ball.width:
        ball_speed_x *= -1

    pygame.draw.ellipse(window, 'white', ball)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(2)
    pygame.display.update()

pygame.quit()
