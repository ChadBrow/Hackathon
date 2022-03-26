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
    