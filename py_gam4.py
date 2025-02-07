# import pygame
# pygame.init()
# window = pygame.display.set_mode((750, 750))
#
# font = pygame.font.SysFont('Tahoma', 40, 'bold')
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     window.fill('black')
#     score = 0
#     text = font.render(f'{score}', True, 'yellow')
#
#     window.blit(text, (300, 50))
#
#     pygame.display.update()
#
# pygame.quit()

# a = int(input('Sonni kiriting'))
# if a > 0:
#     print(f"{a} soni musbat")
# else:
#     print(f"{a} soni manfiy")

# a = int(input('1-sonni kiriting: '))
# b = int(input('2-sonni kiriting: '))
# print(type(a - b))
# string - matn " "
# integer - butun son 1 2 3 4

name = input('Ismingizni kiritng: ')
print(type(name))