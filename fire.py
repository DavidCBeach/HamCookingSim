import pygame

class Fireroom():
    x = 0
    y = 0
    time = 0
    animation = 0
    confirmation = 0
    tago = 0
    endtime = 3000
    cxone = 0
    cyone = 0
    cxtwo = 0 
    cytwo = 0
    cfilled = 0
    fxone = 0
    fyone = 0
    fxtwo = 0 
    fytwo = 0
    ffilled = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.cxone = self.x
        self.cyone = self.y
        self.cxtwo = self.x+60
        self.cytwo = self.y+60
        self.cfilled = 0
        self.fxone = self.x
        self.fyone = self.y+120
        self.fxtwo = self.x+60
        self.fytwo = self.y+180
        self.ffilled = 0
    def clickk(self, x,y,pointer):
        if x > self.cxone and x < self.cxtwo and y > self.cyone and y < self.cytwo:
            if self.cfilled == 1 and pointer == 0:
                self.cfilled = 0
                return 1
            elif self.cfilled == 2 and pointer == 0:
                self.cfilled = 0
                return 2
            elif self.cfilled == 3 and pointer == 0:
                self.cfilled = 0
                return 3
            elif self.cfilled == 0 and pointer > 0:
                self.cfilled = pointer
                return 0
            else:
                return pointer

        elif x > self.fxone and x < self.fxtwo and y > self.fyone and y < self.fytwo:
            if self.ffilled == 1 and pointer == 0:
                self.ffilled = 0
                return 1
            elif self.ffilled == 2 and pointer == 0:
                self.ffilled = 0
                return 2
            elif self.ffilled == 3 and pointer == 0:
                self.ffilled = 0
                return 3
            elif self.ffilled == 0 and pointer > 0:
                self.ffilled = pointer
                return 0
            else:
                return pointer
        else:
            return pointer
        return pointer
    def dispp(self, gameDisplay):
        if self.cfilled == 1:
            gameDisplay.blit(pygame.image.load('ham.png'),(self.cxone,self.cyone))
        if self.cfilled == 2:
            gameDisplay.blit(pygame.image.load('wood.png'),(self.cxone,self.cyone))
        if self.cfilled == 3:
            gameDisplay.blit(pygame.image.load('ham1.png'),(self.cxone,self.cyone))
        if self.ffilled == 1:
            gameDisplay.blit(pygame.image.load('ham.png'),(self.fxone,self.fyone))
        if self.ffilled == 2:
            gameDisplay.blit(pygame.image.load('wood.png'),(self.fxone,self.fyone))
        if self.ffilled == 3:
            gameDisplay.blit(pygame.image.load('ham1.png'),(self.fxone,self.fyone))
    def cook(self,gameDisplay):
        
        if self.cfilled == 1 and self.ffilled == 2:
            self.ffilled = 0
            self.confirmation = 1
        if self.confirmation == 1:
            if self.cfilled == 1 and self.tago == 0:
                self.tago = 1
                self.endtime = self.time+700
                print self.endtime
            if self.time > self.endtime and self.tago == 1:
                self.cfilled = 3
                self.tago = 0
            if self.time > 3000:
                self.confirmation = 0
                self.time = 0
            else:
                self.animation += 0.2
                self.time+=1
                if self.animation > 1 and self.animation <= 2:
                    gameDisplay.blit(pygame.image.load('flame1.png'),(self.x,self.y+60))
                if self.animation > 2 and self.animation <= 3:
                    gameDisplay.blit(pygame.image.load('flame2.png'),(self.x,self.y+60))
                if self.animation > 3 and self.animation <= 4:
                    gameDisplay.blit(pygame.image.load('flame3.png'),(self.x,self.y+60))
                if self.animation > 4 and self.animation <= 5:
                    gameDisplay.blit(pygame.image.load('flame4.png'),(self.x,self.y+60))
                if self.animation > 5 and self.animation <= 6:
                    gameDisplay.blit(pygame.image.load('flame5.png'),(self.x,self.y+60))
                if self.animation > 6 and self.animation <= 7:
                    gameDisplay.blit(pygame.image.load('flame3.png'),(self.x,self.y+60))
                if self.animation > 7 and self.animation <= 8:
                    gameDisplay.blit(pygame.image.load('flame1.png'),(self.x,self.y+60))
                if self.animation > 8 and self.animation <= 9:
                    gameDisplay.blit(pygame.image.load('flame2.png'),(self.x,self.y+60))
                if self.animation > 9 and self.animation <= 10:
                    gameDisplay.blit(pygame.image.load('flame3.png'),(self.x,self.y+60))
                if self.animation > 10 and self.animation <= 11:
                    gameDisplay.blit(pygame.image.load('flame4.png'),(self.x,self.y+60))
                if self.animation > 11 and self.animation <= 12:
                    gameDisplay.blit(pygame.image.load('flame2.png'),(self.x,self.y+60))
                if self.animation > 12 and self.animation <= 13:
                    gameDisplay.blit(pygame.image.load('flame3.png'),(self.x,self.y+60))
                if self.animation >= 13:
                    self.animation = 1
                     
