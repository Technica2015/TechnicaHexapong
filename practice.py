import pygame
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

player_image = pygame.image.load("TechnicaBlue.png").convert()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


pygame.display.flip()
clock.tick(60)
pygame.quit()
