from ctypes import sizeof
import pygame
class sprite:
    def __init__(self, image, position, size, name = None, show = True):
        self.image = image
        self.position = position
        self.size = size
        self.name = name
        self.show = show


        
        
        self.approval = False




    def detectCollision(self, pos):
        if pos[0] >= self.position[0] and pos[0] <= self.position[0] + self.size[0]:
            if pos[1] >= self.position[1] and pos[1] <= self.position[1] + self.size[1]:
                return True
        return False
class text(sprite):
    def __init__(self, text, position, size, name = None, fgcolor = (201, 97, 0), bgcolor = (12, 23, 40)):
        self.font = pygame.font.Font("resources/pressStart2P.ttf", 32)
        self.text = self.font.render(text, fgcolor, bgcolor)
        self.textRect = self.text.get_rect()
        self.textRect.center = (position[0] - size[0]//2, position[1] - size[1]//2)
        self.position = position
        self.size = size
        self.name = name