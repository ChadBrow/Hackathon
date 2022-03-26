

class sprite:
    def __init__(self, image, position, size, name = None):
        self.image = image
        self.position = position
        self.size = size
        self.name = name



        
        
        self.approval = False




    def detectCollision(self, pos):
        if pos[0] >= self.position[0] and pos[0] <= self.position[0] + self.size[0]:
            if pos[1] >= self.position[1] and pos[1] <= self.position[1] + self.size[1]:
                return True
        return False