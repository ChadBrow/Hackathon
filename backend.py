import json, random
import classes as c

# import the data
from data import * # import all the variables from data.py


# university people
students = c.FocusGroup()
faculty = c.FocusGroup()

# da money (donors, games, tuition)
donors = c.FocusGroup() # approval changes % money, performance changes total amount of money
fans = c.FocusGroup() # approval changes how many fans come out, performance changes how hype they are


# misc pain and punishment
"""
Three groups of events:
- minor
- noteworthy
- severe

or should we do
- good
- neutral 
- bad
"""

# constants
tuition = 1000 # just a random constant.
eventChance = 50 # number between 1 and 100

mainStats = {
    "performance": 0,
    "approval": 0,
    "budget": 0
}

def tick():

    # check for events
    changeOfEvent = random.randint(1, 100)


    # update the people
    students.update()
    faculty.update()
    donors.update()
    fans.update()





def parseEvents(events): # this method is probably obsolete
    tempEvents = []
    for event in events: # check to see if this plays with the python list of dictionaries
        tC = [c.Choice(j['title'], j['body'], j['effects']) for j in event['choices']]
        tempEvents.append(c.Event(event['title'], event['image'], event['body'], tC))
    return tempEvents
