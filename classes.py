class FocusGroup:

    def __innit__(self, startApproval = 0, startPerform = 0):
        self.approval = startApproval
        self.performance = startPerform
    
    def modApproval(self, var):
        self.approval += var

    def modPerformance(self, var):
        self.performance += var
    
    
    def returnDict(self):
        return {"approval" : self.approval, "performance" : self.approval}

class Choice:
    def __init__(self, title, body, effects):
        self.title = title
        self.body = body
        self.effects = effects
    
    

class Event:
    def __innit__(self, title, image, body, choices):
        self.title = title
        self.image = image
        self.body = body
        self.choices = choices
    
    