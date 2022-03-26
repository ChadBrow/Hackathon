class FocusGroup: # are we just calling this the money too (where "performance" is "willingness to donate")
    def __init__(self, startApproval = 0, startPerformance = 0):
        self.approval = startApproval
        self.performance = startPerformance
    
    def modApproval(self, var):
        self.approval += var

    def modPerformance(self, var):
        self.performance += var
    
    def modDApproval(self, var):
        self.dApproval += var
    
    def modDPerformance(self, var):
        self.dPerformance += var
    
    def update(self):
        self.approval += 0.5 * (0.5 - self.approval)
        self.performance += 0.5 * (0.5 - self.performance)

    def returnDict(self):
        return {"approval" : self.approval, "performance" : self.approval}

class Choice:
    def __init__(self, title, body, effects):
        self.title = title
        self.body = body
        self.effects = effects
    
    

class Event:
    def __init__(self, title, image, body, choice):
        self.title = title
        self.image = image
        self.body = body
        self.choice = choice

class MoneySink:
    def __init__(self, effects, funding = 0, maxFunding = 0): 
        self.funding = funding
        self.maxFunding = maxFunding
        self.effects = effects #list containing lists. These contained lists contain effect function and multiplier
    
    def modFunding(self, var):
        self.funding += var
        for effect in self.effects:
            effect[0](effect[1] * var)