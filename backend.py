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
def revenue():
    return 0 # make this something useful
def tick():

    # Update FOCUS_GROUPS
    for c in FOCUS_GROUPS:
        FOCUS_GROUPS[c].update()
    
    # update budget
    
    savings = savings - spentAmmount + revenue()



    # check for events
    changeOfEvent = random.randint(1, 100)



