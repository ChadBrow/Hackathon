import pygame
width = 540

class FocusGroup: # are we just calling this the money too (where "performance" is "willingness to donate")
    def __init__(self, image, startApproval = 0, startPerformance = 0):
        self.approval = startApproval
        self.performance = startPerformance
        self.approvalTarget = startApproval
        self.performanceTarget = startPerformance
        self.image = pygame.image.load("resources/" + image)
        self.image = pygame.transform.scale(self.image, (width//5, width//5))
    
    
    def modApproval(self, var):
        self.approval += var

    def modPerformance(self, var):
        self.performance += var
    
    def modApprovalTarget(self, var):
        self.approvalTarget += var
    
    def modPerformanceTarget(self, var):
        self.performanceTarget += var
    
    def updateApproval(self):
        self.approval += 0.5 * (self.approvalTarget - self.approval)
    
    def updatePerformance(self):
        self.performance += 0.5 * (self.performanceTarget - self.performance)

    def returnDict(self):
        return {"approval" : self.approval, "performance" : self.approval}

class Choice:
    def __init__(self, title, body, effects, cost = 0):
        self.title = title
        self.body = body
        self.effects = effects
        self.cost = cost
    
    

class Event:
    def __init__(self, title, image, body, choices):
        self.title = title
        self.image = pygame.image.load("resources/" + image)
        self.image = pygame.transform.scale(self.image, (width//5, width//5))
        self.body = body
        self.choices = choices

class Request:
    def __init__(self, title, body, effects, cost = 0):
        self.title = title
        self.body = body
        self.effects = effects
        self.cost = cost

# class MoneySink:
#     def __init__(self, effects): 
#         self.effects = effects #list containing lists. These contained lists contain effect function and multiplier
    
#     def modFunding(self, var):
#         for effect in self.effects:
#             effect[0](effect[1] * var)

class Costs:
    def __init__(self, admin = 0, academics = 0, studentGroups = 0, research = 0, events = 0):
        self.admin = admin
        self.academics = academics
        self.studentGroups = studentGroups
        self.research = research
        self.events = events
    
    def modAdmin(self, var):
        self.admin += var
    
    def modAcademics(self, var):
        self.academics += var
    
    def modStudentGroups(self, var):
        self.studentGroups += var
    
    def modResearch(self, var):
        self.research += var
    
    def modEvents(self, var):
        self.events += var
    
    def total(self):
        return self.admin + self.academics + self.studentGroups + self.research + self.events