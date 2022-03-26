from ctypes import sizeof
import pygame
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
class text(sprite):
    def __init__(self, text, position, size, name = None):
        fgcolor = (0, 0, 0)
        bgcolor = (255, 255, 255)
        font = pygame.font.Font("resources/pressStart2P.ttf", 32)
        self.text = font.render(text, fgcolor, bgcolor)
        self.textRect = self.text.get_rect()
        self.textRect.update(position, size)
        self.name = name