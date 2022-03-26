import pygame
import guiFunctions, guiObjects

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



clock = pygame.time.Clock()


#We should define a sprite class and all the types of stuff we have on the screen are subclasses of sprite
officeImg = pygame.image.load("resources/desk.jpg")
officeImg = pygame.transform.scale(officeImg, (width, height))
menuImg = pygame.image.load("resources/menu.png")
menuImg = pygame.transform.scale(menuImg, (int(width/12), int(width/12)))
mapImg = pygame.image.load("resources/map.png")
mapImg = pygame.transform.scale(mapImg, (int(width/12), int(width/12)))

mainGameSprites = [guiObjects.sprite(officeImg, (0, 0), (width, height), "officeImg"), guiObjects.sprite(menuImg, (0,0), (int(width/12), int(width/12)), "menuImg"), guiObjects.sprite(mapImg, (width - mapImg.get_width(),0), (int(width/12), int(width/12)), "mapImg")]

menuBgImg = pygame.image.load("resources/deskJonkers.jpg")
menuBgImg = pygame.transform.scale(menuBgImg, (width, height))


menuSprites = [guiObjects.sprite(menuBgImg, (0,0), (width, height), "menuBgImg")]

clickedSprites = []
hoveredSprites = []

#Alright, boys pay attention
#Game state is teeling what scene to load and how the gui will interact with the user.
    #0 is when the game is gonna be closed
    #1 is when the game is game over screen
    #2 is menu/start screen
    #3 is main game screen
    #4 is map scene
gameState = 2 #Technicaly should start with 2
gameVisuals = [None, None, menuSprites, mainGameSprites, None]


while gameState:
    window.fill(bgcolor)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameState = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            #pos = pygame.mouse.get_pos()
            clickedSprites = []
            for theSprite in gameVisuals[gameState]:
                if theSprite.detectCollision(pos):
                    clickedSprites.append(theSprite.name)
            #Do something with the clicked sprites

    for theSprite in gameVisuals[gameState]:
        if theSprite.detectCollision(pos):
            hoveredSprites.append(theSprite.name)

    print("Clicked Sprites: " + str(clickedSprites))
    print("Hovered Spries: " + str(hoveredSprites))

    for surface in gameVisuals[gameState]:
        window.blit(surface.image, surface.position)
    """
    if gameState == 1: #Game over screen
        pass
    elif gameState == 2: #Start screen/menu screen
        pass
    elif gameState == 3: #Main office scene
        for surface in mainGameSprites:
            window.blit(surface.image, surface.position)
    elif gameState == 4: #Map scene
        pass
    """
    clickedSprites = []
    hoveredSprites = []
    pygame.display.update()
    clock.tick(fps) #Set FPS
pygame.quit()