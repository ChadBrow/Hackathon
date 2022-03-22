class InterestGroup:
    """
        name
        size?
        available capital
        interests

    """
    def __init__(self, name, size, availCapital, interests):
        self.name = name # str
        self.size = size # int
        self.availCap = availCapital # monetary
        self.interests = interests # array of strings or ints which correspond to certain topics

class Building:
    # gonna deal with other methods later, this is just for our brainstorming
    def __init__(self, name, size, energyRequirement, energyProduction, energyStorage, capacity, function): # should we deal with energy storage?
        self.name = name # str
        self.size = size # int
        self.eRequirement = energyRequirement # amount it consumes per turn(?)
        self.eProduction = energyProduction # produced by that building
        self.eStorage = energyStorage # stored (or should be not worry about storing excess energy?)
        self.capacity = capacity # people (mainly used for dorms -> most buildings would probably be zero)
        self.function = function # what the building's role is
