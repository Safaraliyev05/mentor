import random

import pygame

pygame.init()

window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width, window_height))

# Set up the road parameters
road_width = int(window_width / 1.6)
right_line = window_width / 2 + road_width / 4
left_line = window_width / 2 - road_width / 4

car = pygame.image.load("player.png")
car = pygame.transform.scale(car, (240, 250))
car_rect = car.get_rect()
car_rect.center = (left_line, 650)

police_car = pygame.image.load("police.png")
police_car = pygame.transform.scale(police_car, (190, 300))
police_car_rect = police_car.get_rect()
police_car_rect.center = (right_line, 80)

speed = 1

running = True
while running:
    window.fill("green")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and car_rect.centerx > left_line + road_width / 4:
                car_rect = car_rect.move([-int(road_width / 2), 0])
            elif event.key == pygame.K_RIGHT and car_rect.centerx < right_line - road_width / 4:
                car_rect = car_rect.move([int(road_width / 2), 0])

    pygame.draw.rect(window, "#666666", (150, 0, road_width, window_height))
    pygame.draw.rect(window, "yellow", (400, 0, 10, window_height))
    pygame.draw.rect(window, "white", (165, 0, 10, window_height))
    pygame.draw.rect(window, "white", (625, 0, 10, window_height))

    window.blit(car, car_rect)
    window.blit(police_car, police_car_rect)

    # police_car_rect[1] sababi enemy_car_rect[y] ga teng. y o'qi bo'yicha mashina tepadan
    # pastga tushadi
    police_car_rect[1] += speed
    if police_car_rect[1] > window_height:
        if random.randint(0, 1) == 0:
            police_car_rect.center = (left_line, 80)
        else:
            police_car_rect.center = (right_line, 80)

    # toxnashish
    if car_rect.colliderect(police_car_rect):
        running = False
        print("Game over")

    pygame.display.update()

pygame.quit()
