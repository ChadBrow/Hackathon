import pygame, random
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

width = 1600
height = 900
fps = 60

bgcolor = (12, 23, 40) #blue
bgcolorHovered = (6, 12, 20) #darker blue
fgcolor = (201, 97, 0) #gold

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
    
def revenue():

    return 0 # make this something useful
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















#################### GAME ######################
if __name__ == "__main__":
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Our Dame")
    gameIcon = pygame.image.load("resources/deskJonkers.gif")
    pygame.display.set_icon(gameIcon)

    keyPress = pygame.mixer.Sound("resources/keypress.wav")

    clock = pygame.time.Clock()


    #We should define a sprite class and all the types of stuff we have on the screen are subclasses of sprite
    officeImg = pygame.image.load("resources/desk.jpg")
    officeImg = pygame.transform.scale(officeImg, (width, height))
    menuImg =   pygame.image.load("resources/menu.png")
    menuImg =   pygame.transform.scale(menuImg, (int(width/12), int(width/12)))
    grampyImg = pygame.image.load("resources/grampyclock.png")
    grampyImg = pygame.transform.scale(grampyImg, (height//2*grampyImg.get_width()//grampyImg.get_height(), height//2))


    #window.blit(text, textRect)

    mainGameSprites =  [guiClasses.sprite(officeImg, (0, 0),                             (width, height),                                                     "officeImg"),
                        guiClasses.sprite(menuImg,   (0, 0),                             (int(width/12), int(width/12)),                                      "menuImg"),
                        #Top bar info
                        guiClasses.sprite(grampyImg, (width - grampyImg.get_width(), 0), (height//2*grampyImg.get_width()//grampyImg.get_height(), height//2, "grampyImg"))
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


    clickedSprites = []
    hoveredSprites = []
    
    ### Pygame is stupid and my head hurts

    font = pygame.font.Font("resources/pressStart2P.ttf", fontSize)
    
    # colors

    textColor = (230, 230, 230) # change this
    GREEN = (50, 250, 50) # change this
    
    

    #Alright, boys pay attention
    #Game state is teeling what scene to load and how the gui will interact with the user.
        #0 is when the game is gonna be closed
        #1 is when the game is game over screen
        #2 is menu/start screen
        #3 is main game screen
        #4 is map scene
    gameState = 2 #Technicaly should start with 2
    gameVisuals = [None, None, menuSprites, mainGameSprites, None, None]


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
                        keyPress.play()
                #Do something with the clicked sprites

        for theSprite in gameVisuals[gameState]:
            if theSprite.detectCollision(pos):
                hoveredSprites.append(theSprite.name)


        for surface in gameVisuals[gameState]:
            if str(type(surface)) == "<class 'guiClasses.sprite'>":
                window.blit(surface.image, surface.position)
            elif str(type(surface)) == "<class 'guiClasses.text'>":
                window.blit(surface.text, surface.textRect)
        print(clickedSprites)
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
                elif item == "grampyImg":
                    print("ticking")
                    tick()
        elif gameState == 4: # playing the game
            t = "$" + str(mainStats['budget'])
            headerText = font.render(t, True, textColor)            
            pygame.draw.rect(window, GREEN, (10, 10, 10, 20))

            pass
        elif gameState == 5: #Options scene
            pass

        clickedSprites = []
        hoveredSprites = []
        pygame.display.update()
        clock.tick(fps) #Set FPS
    pygame.quit()