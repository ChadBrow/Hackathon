
import json, random

# import the data
from data import * # import all the variables from data.py


# constants
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
    return 0

def tick():

    # Update FOCUS_GROUPS
    for c in FOCUS_GROUPS:
        FOCUS_GROUPS[c].update()

    # check for events
    chanceOfEvent = random.randint(1, 100)
    event = None
    if chanceOfEvent >= eventChance:
        e = random.randint(0, len(RANDOM_EVENTS)-1)
        event = RANDOM_EVENTS[e] # pass this event to anar's front-end
        pushEvent(event) # placeholder function for passing the event to anar
    choice = guiChoice() # this is a placeholder for the choice passed back by anar's gui
    enactEvent(event, choice) # this is a placeholder function for however we want to do this

    # update budget
    
    savings = savings - spentAmmount + revenue()

def calcIncome():
    #calculates monthly income
    tuition = 60 * FOCUS_GROUPS["students"].performance        #30/month at start on medium
    grants = 40 * FOCUS_GROUPS["faculty"].performance          #20/month at start on medium
    donations = 120 * FOCUS_GROUPS["donors"].performance * FOCUS_GROUPS["donors"].approval     #30/month at start on medium
    endowment = 0.1 * savings     #20/month at start on medium
    events = 20         #20/month at start on medium