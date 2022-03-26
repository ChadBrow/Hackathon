import json
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
students = c.FocusGroup()
faculty = c.FocusGroup()


mainStats = {
    "performance": 0,
    "approval": 0,
    "budget": 0
}