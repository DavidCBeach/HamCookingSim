import pygame

    
class Box():
    xone = 0
    yone = 0
    xtwo = 0 
    ytwo = 0
    filled = 0
    def __init__(self,xone,yone,xtwo,ytwo,filled):
        self.xone = xone
        self.yone = yone
        self.xtwo = xtwo
        self.ytwo = ytwo
        self.filled = filled
    def click(self, x, y,pointer):
        if x > self.xone and x < self.xtwo and y > self.yone and y < self.ytwo:
            if self.filled == 1 and pointer == 0:
                self.filled = 0
                return 1
            elif self.filled == 2 and pointer == 0:
                self.filled = 0
                return 2
            elif self.filled == 3 and pointer == 0:
                self.filled = 0
                return 3
            elif self.filled == 0 and pointer > 0:
                self.filled = pointer
                return 0
            else:
                return pointer
        else:
            return pointer
    def disp(self,gameDisplay):
        if self.filled == 1:
            gameDisplay.blit(pygame.image.load('ham.png'),(self.xone,self.yone))
        if self.filled == 2:
            gameDisplay.blit(pygame.image.load('wood.png'),(self.xone,self.yone))
        if self.filled == 3:
            gameDisplay.blit(pygame.image.load('ham1.png'),(self.xone,self.yone))
