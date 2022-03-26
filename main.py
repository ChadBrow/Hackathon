import pygame
import guiFunctions, guiClasses
#import classes
#from backend import chosenEvent # the event object that you receive from backend (will be None until an event is chosen)

pygame.init()

chosenOption = None # the variable that backend.py will look for


width = 960
height = 540
fps = 60

bgcolor = (0, 0, 0)
fgcolor = (255, 255, 255)
if __name__ == "__main__":
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Our Dame")
    gameIcon = pygame.image.load("resources/deskJonkers.gif")
    pygame.display.set_icon(gameIcon)



    clock = pygame.time.Clock()


    #We should define a sprite class and all the types of stuff we have on the screen are subclasses of sprite
    officeImg =  pygame.image.load("resources/desk.jpg")
    officeImg =  pygame.transform.scale(officeImg, (width, height))
    menuImg =    pygame.image.load("resources/menu.png")
    menuImg =    pygame.transform.scale(menuImg, (int(width/12), int(width/12)))



    #window.blit(text, textRect)

    mainGameSprites =  [guiClasses.sprite(officeImg, (0, 0), (width, height),                "officeImg"),
                        guiClasses.sprite(menuImg,   (0, 0), (int(width/12), int(width/12)), "menuImg"),
                        #Top bar info
                        guiClasses.text("Hello", (width//2, height//2), (width//2, height//2))
                        #Proposals
                        #Focus Groups
                        ]

    menuBgImg =  pygame.image.load("resources/deskJonkers.jpg")
    menuBgImg =  pygame.transform.scale(menuBgImg, (width, height))
    playImg =    pygame.image.load("resources/play.png")
    playImg =    pygame.transform.scale(playImg, (int(height/6*playImg.get_width()/playImg.get_height()), int(height/6)))
    optionsImg = pygame.image.load("resources/options.png")
    optionsImg = pygame.transform.scale(optionsImg, (int(height/6*optionsImg.get_width()/optionsImg.get_height()), int(height/6)))
    exitImg =    pygame.image.load("resources/exit.png")
    exitImg =    pygame.transform.scale(exitImg, (int(height/6*exitImg.get_width()/exitImg.get_height()), int(height/6)))

    playImgHovered =    pygame.image.load("resources/playHovered.png")
    playImgHovered =    pygame.transform.scale(playImgHovered, (int(height/6*playImg.get_width()/playImg.get_height()), int(height/6)))
    optionsImgHovered = pygame.image.load("resources/optionsHovered.png")
    optionsImgHovered = pygame.transform.scale(optionsImgHovered, (int(height/6*optionsImg.get_width()/optionsImg.get_height()), int(height/6)))
    exitImgHovered =    pygame.image.load("resources/exitHovered.png")
    exitImgHovered =    pygame.transform.scale(exitImgHovered, (int(height/6*exitImg.get_width()/exitImg.get_height()), int(height/6)))

    menuSprites =  [guiClasses.sprite(menuBgImg,  (0,0),                    (width, height),                                                               "menuBgImg"),
                    guiClasses.sprite(playImg,    (1*width/2, 2*height/12), (int(height/6*playImg.get_width()/playImg.get_height()), int(height/6)),       "playImg"),
                    guiClasses.sprite(optionsImg, (1*width/2, 5*height/12), (int(height/6*optionsImg.get_width()/optionsImg.get_height()), int(height/6)), "optionsImg"),
                    guiClasses.sprite(exitImg,    (1*width/2, 8*height/12), (int(height/6*exitImg.get_width()/exitImg.get_height()), int(height/6)),       "exitImg")]

    mapImg =  pygame.image.load("resources/map.jpg")
    mapImg =  pygame.transform.scale(mapImg, (width, height))
    backImg = pygame.image.load("resources/back.png")
    backImg = pygame.transform.scale(backImg, (int(width/12), int(height/12)))

    mapSprites =   [guiClasses.sprite(mapImg,  (0, 0), (width, height),                "mapImg"),
                    guiClasses.sprite(backImg, (0, 0), (int(width/12), int(width/12)), "backImg")]

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
    gameVisuals = [None, None, menuSprites, mainGameSprites, mapSprites, None]


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


        for surface in gameVisuals[gameState]:
            if str(type(surface)) == "<class 'guiClasses.sprite'>":
                window.blit(surface.image, surface.position)
            elif str(type(surface)) == "<class 'guiClasses.text'":
                window.blit(surface.text, surface.position)
        if gameState == 1: #Game over screen
            pass
        elif gameState == 2: #Start screen/menu screen
            for item in clickedSprites:
                if item == "playImg":
                    gameState = 3
                elif item == "optionsImg":
                    gameState = 5
                elif item == "exitImg":
                    gameState = 0
            for item in hoveredSprites:
                for display in menuSprites:
                    if display.name == item and display.name == "playImg":
                        window.blit(playImgHovered, display.position)
                    elif display.name == item and display.name == "optionsImg":
                        window.blit(optionsImgHovered, display.position)
                    elif display.name == item and display.name == "exitImg":
                        window.blit(exitImgHovered, display.position)

        elif gameState == 3: #Main office scene
            for item in clickedSprites:
                if item == "menuImg":
                    gameState = 2
                elif item == "":
                    pass
        elif gameState == 4: #scene
            pass
        elif gameState == 5: #Options scene
            pass

        clickedSprites = []
        hoveredSprites = []
        pygame.display.update()
        clock.tick(fps) #Set FPS
    pygame.quit()