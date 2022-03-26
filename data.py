
from classes import FocusGroup, Choice, Event, Request, Costs

####Helper Functions####
def modSustainability(var):
    vars["sustainability"] += var

FOCUS_GROUPS = {
    "students": FocusGroup("exit.png", 0.5, 0.5),
    "faculty": FocusGroup("exit.png", 0.5, 0.5),
    "donors": FocusGroup("exit.png", 0.5, 0.5),
    "fans": FocusGroup("exit.png", 0.5, 0.5),
}

variables = {
    "sustainability": 0,
    "savings": 200
}

costs = Costs(25, 30, 10, 15, 20) #monthly costs not yearly. Based off yearly cost data Jack found online

####lists####
studentRequests = [
    Request(
        title = "Increased Club Support",
        body = "The student body wants Nuestro Madre to increase its club support and spending.\nCost: 5M\nEffects:\n  - Increase student happiness target by 10%.\n  - Decrease faculty happiness target by 5%\n  - Increase monthly spending on student groups by 2M",
        effects = [[FOCUS_GROUPS["students"].modApprovalTarget, 0.1], [FOCUS_GROUPS["faculty"].modApprovalTarget, -0.05], [costs.modStudentGroups, 2]],
        cost = 5
    )
]

facultyRequests = [
    Request(
        title = "More Research Grants",
        body = "The faculty want Nuestro Madre to increase the amount of research grants that it gives.\nCost: 10M\nEffects:\n - Increase facultry happiness target by 10%\n  - Increase student happiness target by 5%\n  - Increase monthly spending on research by 5M",
        effects = [[FOCUS_GROUPS["faculty"].modApprovalTarget, 0.1], [FOCUS_GROUPS["students"].modApprovalTarget, 0.05], costs.modResearch, 5],
        cost = 10
    )
]

donorRequests = [
    Request(
        title = "Donor Celebration Feast",
        body = "Many Nuestro Madre donors have been requesting that the university holds a feast.\nCost: 2M\nEffects:\n  - Increase donor happiness by 10%",
        effects = [[FOCUS_GROUPS["donors"].modApproval, 0.1]],
        cost = 2
    )
]

fanRequests = [
    Request(
        title = "Year-Round Campus Tours",
        body = "Many Nuestro Madre enthusiasts are requesting year-round, guided tours of the campus. This would cost very little for the university to do, but the student body might not appreciate the year-round tours.\nCost: 4M\nEffects:\n  - Increase fan happiness target by 10%\n  - Decrease student happiness target by 5%",
        effects = [[FOCUS_GROUPS["fans"].modApprovalTarget, 10], [FOCUS_GROUPS["students"].modApprovalTarget, -5]],
        cost = 4
    )
]

sustainabilityProposals = [
    Request(
        title = "On-Campus Farming",
        body = "Nuestro Madre can establish student-run, organic farms on campus. This would allow students to become directly involved in making the campus a more sustainable place and it would make the campus a more sustainable place.\nCost: 8M\nEffects:\n  - Increase student happiness target by 10%\n  - Increase sustainability by 5%\n  - Increase monthly cost of administration by 3M",
        effects = [[FOCUS_GROUPS["students"].modApprovalTarget, 10], [modSustainability, 0.05], [costs.modAdmin, 3]],
        cost = 8
    ),
    Request(
        title = "Greener Construction Initiative",
        body = "Up to 32% of landfill waste comes from construction sites, and 13% of  material sent to construction sites goes unnused. Putting more resources into construction planning could help reduce unnecessary waste.\nCost: 6M\nEffects: \n  - Increase sustainability by 10%\n  - Increase monthly cost of administration by 2M",
        effects = [[modSustainability, 0.1], [costs.modAdmin, 2]],
        cost = 6
    ),
    Request(
        title = "Solar Panel Initiative",
        body = "Placing ",
        effects = [],
        cost = 0
    )
]

randomEvents = [
    Event(
        title = "Students Ask for Spring CLub Fair",
        image = "deskJonkers.jpg",
        body = "Many students have requested an additional club fair be held at the beginning of the spring semester. Student body president Pat Li has brought a petition to hold the event to Father Jonkins. After much deliberation, Father Jonkins decided to . . .",
        choices = [
            Choice(
                title = "Hold the Event",
                body = "Increase cost of club spending by 2M\nIncrease student happiness target by 5%.",
                effects = [[costs.modStudentGroups, 2], [FOCUS_GROUPS["students"].modApprovalTarget, 0.05]]
            ),
            Choice(
                title = "Reject the Proposal",
                body = "Decrease student happiness by 5%",
                effects = [[FOCUS_GROUPS['students'].modApproval, -0.05]]
            )
        ]
    ),
    Event(
        title = "Bond Hall Toilet Explosion",
        image = "deskJonkers.jpg",
        body = "Late last night a loud bang was heard in one of the Bond Hall bathrooms. Upon investigation, the janitor found that a student had set off fireworks in one of the men's room stalls. Father Jonkins has decided to . . .",
        choices = [
            Choice(
                title = "Prioritize Sustainability",
                body = "Replace the destroyed toilets and plumbing with more environmentally friendly alternatives.\nIncrease cost of administration spending by 2M\nIncrease sustainability by 5%.",
                effects = [[costs.modStudentGroups, 2], [modSustainability, 0.05]]
            ),
            Choice(
                title = "Prioritize a Quick Repair",
                body = "Replace the destroyed toilets and plumbing with the most easily attainable models.\nNo effect.",
                effects = []
            )
        ]
    )
]


# maybe need to import the classes here
# RANDOM_EVENTS = [
#     {
#         "title": "Example",
#         "image": "desk.jpg",
#         "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
#         "choices": [
#             {
#                 "title": "Example",
#                 "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
#                 "effects": [
#                     {
#                         "function": students.addApproval,
#                         "value": 0.1
#                     }
#                 ]
#             }
#         ]

#     },
#     {
#         "title": "Students Ask for Increased Club Spending",
#         "image": "deskJonkers.jpg",
#         "body": "Many students have requested an increase to Nuestro Madre's club funding budget. Student body president Pat Li has brought a petition for increased club spending to Father Jonkins. After much deliberation, Father Jonkins decided to . . .",
#         "choices": [
#             {
#                 "title": "Raise Club Spending",
#                 "body": "Increase cost of club spending by 10M\nIncrease Student approval by 3%",
#                 "effects": [
#                     {
#                         "function": clubs.modFunding,
#                         "value": 10
#                     }
#                 ]
#             },
            
#         ]
#     }
# ]