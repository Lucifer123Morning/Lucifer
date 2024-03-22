import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Pygame Lucifer")
icon = pygame.image.load('icon/icon.png')
pygame.display.set_icon(icon)


player = pygame.image.load('icon/120x80_gifs/__Idle.gif')
bg = pygame.image.load('icon/City4.png')

running = True
while running:

    screen.blit(bg, (0, 0))
    screen.blit(player, (500, 400))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


