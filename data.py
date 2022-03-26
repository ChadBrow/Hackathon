import classes as c

FOCUS_GROUPS = {
    "students": c.FocusGroup(0.5, 0.5),
    "faculty": c.FocusGroup(0.5, 0.5),
    "donors": c.FocusGroup(0.5, 0.5),
    "fans": c.FocusGroup(0.5, 0.5)
}

costs = c.Costs(25, 30, 10, 15, 20) #monthly costs not yearly. Based off yearly cost data Jack found online

# moneySinks = {
#     "clubs" : c.MoneySink(
#         effects = [
#             [FOCUS_GROUPS['students'].modApproval, 0.002], 
#             [FOCUS_GROUPS['faculty'].modApproval, -0.002],
#             ]
#     ) # change these to real data
    
# }

studentRequests = [
    c.Request(
        title = "Increased Club Support",
        body = "The student body wants Notre Dame to increase its club support and spending.\nCost: 5M\nEffects:\n  - Increase student happiness target by 10%%.\n  - Decrease faculty happiness target by 5%%\n  - Increase monthly spending on student groups by 2M",
        effects = [[FOCUS_GROUPS["students"].modApprovalTarget, 0.1], [FOCUS_GROUPS["faculty"].modApprovalTarget, -0.05], [costs.modStudentGroups, 2]],
        cost = 5
    )
]

facultyRequests = [
    c.Request(
        title = "More Research Grants",
        body = "The faculty want Notre Dame to increase the amount of research grants that it gives.\nCost: 10M\nEffects:\n - Increase facultry happiness target by 10%%.\n  - Increase student happiness target by 5%%\n  - Decrease donor happiness target by 5%%\n  - Increase monthly spending on research by 4M",

    )
]

RANDOM_EVENTS = [
    c.Event(
        title = "Students Ask for Increased Club Spending",
        image = "deskJonkers.jpg",
        body = "Many students have requested an increase to Notre Dame's club funding budget. Student body president Pat Li has brought a petition for increased club spending to Father Jonkins. After much deliberation, Father Jonkins decided to . . .",
        choices = [
            c.Choice(
                title = "Raise Club Spending",
                body = "Increase cost of club spending by 2M\nIncrease student happiness target by 5%%.",
                effects = [[costs.modStudentGroups, 20], [FOCUS_GROUPS["students"].modApprovalTarget, 0.05]]
            ),
            c.Choice(
                title = "Reject the Proposal",
                body = "Decrease student happiness by 5%",
                effects = [[FOCUS_GROUPS['students'].modApproval, -0.05]]
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
#         "body": "Many students have requested an increase to Notre Dame's club funding budget. Student body president Pat Li has brought a petition for increased club spending to Father Jonkins. After much deliberation, Father Jonkins decided to . . .",
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