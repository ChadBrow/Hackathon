
############## OBSOLETE ##############



import json, random

# import the data
from data import * # import all the variables from data.py
# from classes import *
from main import chosenOption

# global variables
tuition = 1000 # just a random constant.
eventChance = 50 # number between 1 and 100
savings = 1000 # total savings
recommendedBudget = 1000 # how much you can spend without dipping into your savings
spentAmmount = 0
chosenEvent = None

mainStats = {
    "performance": 0,
    "approval": 0,
    "budget": 0
}
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
    # Update FOCUS_GROUPS
    #Donor approval target is equal to the academic level
    avgCampusPerformance = (FOCUS_GROUPS["students"].performance + FOCUS_GROUPS["faculty"].performance) / 2
    FOCUS_GROUPS["donors"].modApprovalTarget(avgCampusPerformance - FOCUS_GROUPS["donors"].approvalTarget) 
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
        e = random.randint(0, len(RANDOM_EVENTS)-1)
        event = RANDOM_EVENTS[e] # pass this event to anar's front-end
        chosenEvent = pushEvent(event) # placeholder function for passing the event to anar
    choice = guiChoice() # this is a placeholder for the choice passed back by anar's gui
    enactEvent(chosenEvent, choice) # this is a placeholder function for however we want to do this

    # update budget
    
    savings = savings - spentAmmount + revenue()

def calcIncome():
    #calculates monthly income
    tuition = 60 * FOCUS_GROUPS["students"].performance        #30/month at start on medium
    grants = 40 * FOCUS_GROUPS["faculty"].performance          #20/month at start on medium
    donations = 120 * FOCUS_GROUPS["donors"].performance * FOCUS_GROUPS["donors"].approval     #30/month at start on medium
    endowment = 0.1 * savings                                  #20/month at start on medium
    events = 40 * FOCUS_GROUPS["fans"].approval                #20/month at start on medium