import classes as c

FOCUS_GROUPS = {
    "students": c.FocusGroup(0.5, 0.04, 0.5, 0.04),
    "faculty": c.FocusGroup(0.5, 0.04, 0.5, 0.04),
    "donors": c.FocusGroup(0.5, 0.04, 0.5, 0.04),
    "fans": c.FocusGroup(0.5, 0.04, 0.5, 0.04)
}

moneySinks = {
    "clubs" : c.MoneySink(
        effects = [
            [FOCUS_GROUPS['students'].modDApproval(0.001)], 
            [FOCUS_GROUPS['students'].modApproval, 0.002], 
            [FOCUS_GROUPS['faculty'].modDApproval, -0.0005]], 
            funding=100,
            maxFunding = 150
    ) # change these to real data
    
}

RANDOM_EVENTS = [
    c.Event(
        title = "Students Ask for Increased Club Spending",
        image = "deskJonkers.jpg",
        body = "Many students have requested an increase to Notre Dame's club funding budget. Student body president Pat Li has brought a petition for increased club spending to Father Jonkins. After much deliberation, Father Jonkins decided to . . .",
        choice = [
            c.Choice(
                title = "Raise Club Spending",
                body = "Increase cost of club spending by 20M\nIncrease student happiness growth by 2%% and decrease faculty happiness growth by 1%",
                effects = [[moneySinks['clubs'].modFunding, 20], [FOCUS_GROUPS['students'].modApproval, -4]]
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