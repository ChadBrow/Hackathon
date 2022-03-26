import json, random
import classes as c

"""
events
    - text
    - dictionary of their stat changes
    {
        "name" : "whatever the name of the event is"
        "sustain" : +2,
        "approval" : -1,

    }

all the big stats:
    {
        "overall approval" : 
    }


"""
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
scriptedEvents = [] # array of c.Event() objects
randomEvents = [[], [], []] # array of c.Event() -> impacts the university
econEvents = [[], [], []] # array of events that happen to the economy (impacting the fans and donors)

# constants
tuition = 1000 # just a random constant.
eventChance = 50 # number between 1 and 100

mainStats = {
    "performance": 0,
    "approval": 0,
    "budget": 0
}
def startup(dificulty):
    if dificulty == "medium":
        # university people
        students = c.FocusGroup(0.5, 0.04, 0.5, 0.04)
        faculty = c.FocusGroup(0.5, 0.04, 0.5, 0.04)

        # da money (donors, games, tuition)
        donors = c.FocusGroup(0.5, 0.04, 0.5, 0.04) # approval changes % money, performance changes total amount of money
        fans = c.FocusGroup(0.5, 0.04, 0.5, 0.04) # approval changes how many fans come out, performance changes how hype they are

def getEvents(fileName):
    text = ""
    with open(fileName, 'r') as f:
        text += "".join(f.readlines)
    print(text)    
    jsonData = json.loads(text)
    

def tick():

    # check for events
    changeOfEvent = random.randint(1, 100)


    # update the people
    students.update()
    faculty.update()
    donors.update()
    fans.update()
