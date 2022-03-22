import pygame

pygame.init()

width = 960
height = 540
fps = 60

bgcolor = (0, 0, 0)
fgcolor = (255, 255, 255)

ended = 0

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hackathon")
window.fill(bgcolor)

clock = pygame.time.Clock()

#We should define a sprite class and all the types of stuff we have on the screen are subclasses of sprite

while not ended:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ended = 1
    pygame.display.update()
    clock.tick(fps) #Set FPS
pygame.quit()