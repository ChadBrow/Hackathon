import pygame

pygame.init()

width = 960
height = 540

bgcolor = (0, 0, 0)
fgcolor = (255, 255, 255)

ended = 0

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hackathon")
window.fill(bgcolor)

while not ended:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ended = 1
    pygame.display.update()

pygame.quit()