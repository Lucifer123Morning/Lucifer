import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Pygame Lucifer")
icon = pygame.image.load('icon/icon.png')
pygame.display.set_icon(icon)



bg = pygame.image.load('icon/City4.png')

running = True
while running:

    screen.blit(bg, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


