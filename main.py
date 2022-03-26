import pygame
import guiFunctions

pygame.init()

width = 960
height = 540
fps = 60

bgcolor = (0, 0, 0)
fgcolor = (255, 255, 255)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Our Dame")
gameIcon = pygame.image.load("resources/deskJonkers.gif")
pygame.display.set_icon(gameIcon)
window.fill(bgcolor)

clock = pygame.time.Clock()


#We should define a sprite class and all the types of stuff we have on the screen are subclasses of sprite
officeImg = pygame.image.load("resources/desk.jpg")
officeImg = pygame.transform.scale(officeImg, (width, height))
menuImg = pygame.image.load("resources/menu.png")
menuImg = pygame.transform.scale(menuImg, (int(width/12), int(width/12)))
mapImg = pygame.image.load("resources/map.png")
mapImg = pygame.transform.scale(mapImg, (int(width/12), int(width/12)))

mainGameSprites = [[officeImg, menuImg, mapImg], [(0, 0), (0, 0), (width - mapImg.get_width(), 0)]]

#Alright, boys pay attention
#Game state is teeling what scene to load and how the gui will interact with the user.
#0 is when the game is gonna be closed
#1 is when the game is game over screen
#2 is menu/start screen
#3 is main game screen
#4 is map scene
gameState = 3 #Technicaly should start with 2
gameVisuals = [None, None, None, mainGameSprites, None]


while gameState:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameState = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clickedSprites = []
            for visual in gameVisuals[gameState]:
                if guiFunctions.detectCollision(visual, pos):
                    clickedSprites.append(visual)
            #Do something with the clicked sprites

    window.fill(bgcolor)

    

    if gameState == 1: #Game over
        pass
    elif gameState == 2: #Start screen/menu scree
        pass
    elif gameState == 3: #Main office scene
        for i in range(len(mainGameSprites[0])):
            window.blit(mainGameSprites[0][i], mainGameSprites[1][i])
    elif gameState == 4: #Map scene
        pass

    pygame.display.update()
    clock.tick(fps) #Set FPS
pygame.quit()