import pygame, random
from pygame.locals import FULLSCREEN
import guiFunctions, guiClasses

from classes import *
from data import *
# from backend import chosenEvent # the event object that you receive from backend (will be None until an event is chosen)
#import classes
#from backend import chosenEvent # the event object that you receive from backend (will be None until an event is chosen)

############## PYGAME ##############

pygame.init()
fontSize = 16

############## CONSTANTS ##############

chosenOption = None # the variable that backend.py will look for
chosenEvent = None

fps = 60

bgcolor = (12, 23, 40) #blue
bgcolorHovered = (6, 12, 20) #darker blue
fgcolor = (201, 97, 0) #gold

width = 800
height = 450

tuition = 1000 # just a random constant.
eventChance = 50 # number between 1 and 100
savings = 1000 # total savings
recommendedBudget = 1000 # how much you can spend without dipping into your savings
spentAmmount = 0

mainStats = {
    "performance": 0,
    "approval": 0,
    "budget": 0
}


############### FUNCTIONS ###############

def enactEvent(event, choice):
    e = event.choices[choice].effects
    for i in e:
        i[0](i[1]) # I hate how gross this process is. It must be done

def pushEvent(event):
    # I dont know how to do this right now, but we need to send this event to anar
    # maybe just have him check for the current event, but still want the placeholder
    return event
    
def guiChoice():
    return chosenOption

def tick():
    # Chad's code: (best code)
    # calculate balance for next month
    balance = calcIncome() - costs.total()

    # Update FOCUS_GROUPS
    #Donor approval target is equal to average of the academic level and budget balance
    avgCampusPerformance = (FOCUS_GROUPS["students"].performance + FOCUS_GROUPS["faculty"].performance) / 2
    targetHappiness = (avgCampusPerformance + 0.5 * balance / 20) / 2
    FOCUS_GROUPS["donors"].modApprovalTarget(targetHappiness - FOCUS_GROUPS["donors"].approvalTarget) 
    FOCUS_GROUPS["donors"].updateApproval()

    #fan approval target is equal to campus happiness
    avgCampusHappiness = (FOCUS_GROUPS["students"].approval + FOCUS_GROUPS["faculty"].approval) / 2
    FOCUS_GROUPS["fans"].modApprovalTarget(avgCampusHappiness - FOCUS_GROUPS["fans"].approvalTarget)
    FOCUS_GROUPS["fans"].updateApproval()

    #student and faculty performance wanna go to student and faculty approval
    #update student and faculty approval then set student and faculty performance target equal to new approval then update performance
    FOCUS_GROUPS["students"].updateApproval()
    FOCUS_GROUPS["faculty"].updateApproval()

    FOCUS_GROUPS["students"].modPerformanceTarget(FOCUS_GROUPS["students"].approval - FOCUS_GROUPS["students"].performanceTarget)
    FOCUS_GROUPS["faculty"].modPerformanceTarget(FOCUS_GROUPS["faculty"].approval - FOCUS_GROUPS["faculty"].performanceTarget)

    FOCUS_GROUPS["students"].updatePerformance()
    FOCUS_GROUPS["faculty"].updatePerformance()

    for c in FOCUS_GROUPS:
        FOCUS_GROUPS[c].update()


    
    # check for events
    chanceOfEvent = random.randint(1, 100)
    event = None
    if chanceOfEvent >= eventChance:
        e = random.randint(0, len(randomEvents)-1)
        event = randomEvents[e] # pass this event to anar's front-end
        chosenEvent = pushEvent(event) # placeholder function for passing the event to anar
    choice = guiChoice() # this is a placeholder for the choice passed back by anar's gui
    enactEvent(chosenEvent, choice) # this is a placeholder function for however we want to do this

    # update savings
    vars["savings"] = vars["savings"] - spentAmmount + calcIncome()

def calcIncome():
    #calculates monthly income
    tuition = 60 * FOCUS_GROUPS["students"].performance        #30/month at start on medium
    grants = 40 * FOCUS_GROUPS["faculty"].performance          #20/month at start on medium
    donations = 120 * FOCUS_GROUPS["donors"].performance * FOCUS_GROUPS["donors"].approval     #30/month at start on medium
    endowment = 0.1 * savings                                  #20/month at start on medium
    events = 40 * FOCUS_GROUPS["fans"].approval                #20/month at start on medium

    return tuition + grants + donations + endowment + events

def playButton():
    gameState = 3

def optionsButton():
    if fullscreen:
        window = pygame.display.set_mode((width, height))
        fullscreen = 0
    else:
        window = pygame.display.set_mode(window.get_size(), FULLSCREEN)
        fullscreen = 1

def exitButton():
    gameState = 0








#################### GAME ######################
if __name__ == "__main__":

    window = pygame.display.set_mode((width, height))
    fullscreen = 0
    # get the size of the fullscreen display

    pygame.display.set_caption("Our Dame")
    gameIcon = pygame.image.load("resources/globe.jpg")
    pygame.display.set_icon(gameIcon)

    keyPress = pygame.mixer.Sound("resources/keypress.wav")
    intro = pygame.mixer.Sound("resources/NDvictor.wav")
    intro.play()
    clock = pygame.time.Clock()


    #We should define a sprite class and all the types of stuff we have on the screen are subclasses of sprite
    officeImg =  pygame.image.load("resources/johnjonkinsathisdest.jpg")
    officeImg =  pygame.transform.scale(officeImg, (width, height))
    menuImg =    pygame.image.load("resources/menu.png")
    menuImg =    pygame.transform.scale(menuImg, (int(width/12), int(width/12)))
    
    grampyImg =  pygame.image.load("resources/clocky.jpg")
    grampyImg =  pygame.transform.scale(grampyImg, (width*grampyImg.get_width()//1600, height*grampyImg.get_height()//900))
    cabinetImg = pygame.image.load("resources/cabinot.jpg")
    cabinetImg = pygame.transform.scale(cabinetImg, (width*cabinetImg.get_width()//1600, height*cabinetImg.get_height()//900))
    globeImg = pygame.image.load("resources/globe.jpg")
    globeImg = pygame.transform.scale(globeImg, (width*globeImg.get_width()//1600, height*globeImg.get_height()//900))


    mainGameSprites =  [guiClasses.sprite(officeImg, (0, 0),                             (width, height),                                                     "officeImg"),
                        guiClasses.sprite(menuImg,   (0, 0),                             (int(width/12), int(width/12)),                                      "menuImg"),
                        #Top bar info
                        #Desk junk
                        guiClasses.sprite(grampyImg, (width*1270//1600,height*160//900), (width*grampyImg.get_width()//1600, height*grampyImg.get_height()//900), "grampyImg", show = True),
                        guiClasses.sprite(cabinetImg, (width*160//1600, height*180//900), (width*cabinetImg.get_width()//1600, height*cabinetImg.get_height()//900), "cabinetImg", show = True),
                        guiClasses.sprite(globeImg,   (width*1240//1600, height*500//900), (width*globeImg.get_width()//1600, height*globeImg.get_height()//900), "globeImg", show = True)
                        #guiClasses.sprite()
                        #Proposals
                        #Focus Groups
                        ]
    # Menu images
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
                    guiClasses.sprite(playImg,    (1*width/2, 2*height/12), (int(height/6*playImg.get_width()/playImg.get_height()), int(height/6)),       "playImg", playButton),
                    guiClasses.sprite(optionsImg, (1*width/2, 5*height/12), (int(height/6*optionsImg.get_width()/optionsImg.get_height()), int(height/6)), "optionsImg", optionsButton),
                    guiClasses.sprite(exitImg,    (1*width/2, 8*height/12), (int(height/6*exitImg.get_width()/exitImg.get_height()), int(height/6)),       "exitImg", exitButton)]

    # game over sprites and images
    gameOverImg = pygame.image.load("resources/gameOver.jpeg")
    gameOverImg = pygame.transform.scale(gameOverImg, (width, height))
    gameOverSprites = [guiClasses.sprite(gameOverImg, (0, 0), (width, height), "gameOverImg", exitButton), guiClasses.text("Game Over", (int(width / 2), int(9 * height / 10)), (int(width / 10), int(height / 10)), fgcolor=(255, 0, 0), name = "gameOverText")]

    # choice page images (aka. Blake is sick and tired of this)
    focusGroupNames = [i for i in FOCUS_GROUPS]
    choiceImgNames = [["jack_images/menu bar.jpg", "menu bar"]]
    choiceImgDimensions = [
        [(0, 0), (width, int(height * .1))]
    ]
    choiceImages = []
    for i in range(len(choiceImgNames)):
        tempImg = pygame.image.load(choiceImgNames[i][0])
        tempImg = pygame.transform.scale(tempImg, choiceImgDimensions[i][1])
        choiceImages.append(tempImg)
    

    choiceSprites = []
    for i in range(len(choiceImages)):
        choiceSprites.append(guiClasses.sprite(choiceImages[i], choiceImgDimensions[i][0], choiceImgDimensions[i][1], choiceImgNames[i][1]))

    clickedSprites = []
    hoveredSprites = []
    
    ### Pygame is stupid and my head hurt #don't be mean to pygame

    font = pygame.font.Font("resources/pressStart2P.ttf", fontSize)
    
    # colors
    # r, g, b
    textColor = (230, 230, 230) # change this #no
    GREEN = (50, 250, 50) # change this #no
    DARK = (40, 40, 50)
    OUTLINE = (20, 20, 40)

    #Alright, boys pay attention
    #Game state is teeling what scene to load and how the gui will interact with the user.
        #0 is when the game is gonna be closed
        #1 is when the game is game over screen
        #2 is menu/start screen
        #3 is main game screen
        #4 is map scene

    gameState = 4 #Technicaly should start with 2
    gameVisuals = [None, gameOverSprites, menuSprites, mainGameSprites, choiceSprites, None]
    requestGroups = [studentRequests, facultyRequests, donorRequests, fanRequests]



    descriptionText = {
        "officeImg" : "s",
        "menuImg" : "a",
        "grampyImg" : "b",
        "cabinetImg" : "h",
        "globeImg" : "j",
        "menuBgImg" : "w",
        "playImg" : "t",
        "optionsImg" : "p",
        "exitImg" : "o",
        None : ""
    }






    while gameState:
        window.fill(bgcolor)
        pos = pygame.mouse.get_pos()
        
        
        guiClasses.text(descriptionText[hoveredSprites[-1]], (pos[0] + 5, pos[1] + 5), "hoverText")
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                #pos = pygame.mouse.get_pos()
                clickedSprites = []
                for theSprite in gameVisuals[gameState]:
                    if theSprite.detectCollision(pos):
                        theSprite.function() #call the appropriate function
                        keyPress.play()
                #Do something with the clicked sprites

        for theSprite in gameVisuals[gameState]:
            if theSprite.detectCollision(pos):
                hoveredSprites.append(theSprite.name)


        for surface in gameVisuals[gameState]:
            if str(type(surface)) == "<class 'guiClasses.sprite'>":
                if surface.show:
                    window.blit(surface.image, surface.position)
            elif str(type(surface)) == "<class 'guiClasses.text'>":
                window.blit(surface.text, surface.textRect)
        

        print("hovered sprites" + str(hoveredSprites))

        if gameState == 1: #Game over screen
            pass
        elif gameState == 2: #Start screen/menu screen
            for item in clickedSprites:
                if item == "playImg":
                    gameState = 3
                elif item == "optionsImg":
                    if fullscreen:
                        window = pygame.display.set_mode((width, height))
                        fullscreen = 0
                    else:
                        window = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), FULLSCREEN)
                        fullscreen = 1
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
                elif item == "grampyImg":
                    print("ticking")
                    tick()
                elif item == "cabinetImg":
                    gameState = 4
                    print("cabinet")
                elif item == "globeImg":
                    print("globe")
                    #Chad function
        elif gameState == 4: # playing the game
            
            """
                Things I need to do
                    - make images to replace the temp rectangles
                    - link all the shit so approval and performance actually update
                    - make it look good
                    - should I leave the buttons to anar?
                        - or should I do it myself
                    - fix the top menu
                    - make the art style more closely match the cursed 8-bit theme
            
            
            """
        
            # constants
            border = .005

            # top banner
            bannerCoords = (
                0, 0, 
                width, height/10
            )
            #   pygame.draw.rect(window, DARK, bannerCoords)

            #t = "$" + str(mainStats['budget']) # useless
            #headerText = font.render(t, True, textColor)   
            sustainScore = .5 # between zero and one
            sustainCoords = ( # x, y, width, height
                0 + width * .62, height * .02,
                ((width*sustainScore) * .2), height * .06 
            )
            pygame.draw.rect(window, GREEN, sustainCoords)
            pygame.draw.rect(window, OUTLINE, (sustainCoords[0], sustainCoords[1], int(sustainCoords[2]/sustainScore), sustainCoords[3]), 5)       
            

            ### Middle boxes for choices

            midBoxes = [
                (width * (1-(border*2))) / len(requestGroups),
                height * .5
            ]
            for i in range(len(requestGroups)):
                tempCoords = (
                    (width * border * (i)) + (midBoxes[0] * i), height * .15,
                    midBoxes[0], midBoxes[1]
                )
                pygame.draw.rect(window, DARK, tempCoords)
                
                # its all text
                # display the text here, but I dont wanna right now

            ### Bottom info bar with each focus group

            """
            (.05 * )


            """
            sectionSize = (width*(1-(border*2)))/len(FOCUS_GROUPS) # side buffer not included
            sectionHeight = height * .30
            for i in range(len(FOCUS_GROUPS)): # the background box
                tempCoords = (
                    (width * border * (i)) + (sectionSize * i), height * .7, 
                    sectionSize, sectionHeight
                )
                pygame.draw.rect(window, DARK, tempCoords) # draw the background box

                # draw the status bars
                performCoords = (
                    tempCoords[0] + (sectionSize * .85), 
                    tempCoords[1] + (sectionHeight * .2),
                    sectionSize * .1,
                    sectionHeight * .6
                )
                approveCoords = (
                    tempCoords[0] + (sectionSize * .7), 
                    tempCoords[1] + (sectionHeight * .2),
                    sectionSize * .1,
                    sectionHeight * .6
                )
                #tempPerform = FOCUS_GROUPS[focusGroupNames[i]].performance
                tempPerform = 20
                tempApprove = FOCUS_GROUPS[focusGroupNames[i]].approval
                pygame.draw.rect(window, GREEN, (performCoords[0], performCoords[1] + tempPerform, performCoords[2], performCoords[3] - tempPerform))
                pygame.draw.rect(window, OUTLINE, performCoords, 5)

                pygame.draw.rect(window, GREEN, (approveCoords[0], approveCoords[1] + tempApprove, approveCoords[2], approveCoords[3] - tempApprove))
                pygame.draw.rect(window, OUTLINE, approveCoords, 5)



            """
            for group in FOCUS_GROUPS:
                FOCUS_GROUPS[group]
            """

            pass
        elif gameState == 5: #Options scene
            pass

        clickedSprites = []
        hoveredSprites = []
        pygame.display.update()
        clock.tick(fps) #Set FPS
    pygame.quit()
