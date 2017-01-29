import pygame
from box import Box
from fire import Fireroom
pygame.init()

height = 600
width = 800


gameDisplay = pygame.display.set_mode((width, height))

pygame.display.set_caption("Ham Cooking Sim")

box11 = Box(0,0,60,60,1)
box12 = Box(0,60,60,120,2)
box13 = Box(0,120,60,180,2)
box14 = Box(0,180,60,240,2)
box15 = Box(0,240,60,300,2)
box16 = Box(0,300,60,360,1)
box17 = Box(0,360,60,420,1)
box18 = Box(0,420,60,480,1)
box19 = Box(0,480,60,540,1)
box110 = Box(0,540,60,600,1)
box21 = Box(60,0,120,60,1)
box22 = Box(60,60,120,120,1)
box23 = Box(60,120,120,180,2)
box24 = Box(60,180,120,240,1)
box25 = Box(60,240,120,300,1)
box26 = Box(60,300,120,360,1)
box27 = Box(60,360,120,420,2)
box28 = Box(60,420,120,480,1)
box29 = Box(60,480,120,540,1)
box210 = Box(60,540,120,600,1)
box31 = Box(120,0,180,60,1)
box32 = Box(120,60,180,120,2)
box33 = Box(120,120,180,180,1)
box34 = Box(120,180,180,240,1)
box35 = Box(120,240,180,300,1)
box36 = Box(120,300,180,360,2)
box37 = Box(120,360,180,420,1)
box38 = Box(120,420,180,480,1)
box39 = Box(120,480,180,540,1)
box310 = Box(120,540,180,600,2)
four = Fireroom(420,360)
three = Fireroom(240,360)

one = Fireroom(240,60)

two = Fireroom(420,60)

clock = pygame.time.Clock()
woodImg = pygame.image.load('wood.png')
hamImg = pygame.image.load('ham.png')
ham1Img = pygame.image.load('ham1.png')
bgImg = pygame.image.load('back.png')
def ham(x,y):
    gameDisplay.blit(hamImg,(x,y))
'''
def cook():
    if cooking.filled == 1 and fire.filled == 2:
        cooking.filled = 3
        fire.filled = 0
        '''
def game():
    ended = False  
    pos = []
    x = 0
    y = 0 
    pointer = 0
    while not ended:
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ended = True
            if event.type == pygame.MOUSEBUTTONUP:
                pointer = box11.click(x,y, pointer) 
                pointer = box12.click(x,y, pointer) 
                pointer = box13.click(x,y, pointer) 
                pointer = box14.click(x,y, pointer) 
                pointer = box15.click(x,y, pointer) 
                pointer = box16.click(x,y, pointer) 
                pointer = box17.click(x,y, pointer) 
                pointer = box18.click(x,y, pointer) 
                pointer = box19.click(x,y, pointer) 
                pointer = box110.click(x,y, pointer) 
                pointer = box21.click(x,y, pointer) 
                pointer = box22.click(x,y, pointer) 
                pointer = box23.click(x,y, pointer) 
                pointer = box24.click(x,y, pointer) 
                pointer = box25.click(x,y, pointer) 
                pointer = box26.click(x,y, pointer) 
                pointer = box27.click(x,y, pointer) 
                pointer = box28.click(x,y, pointer) 
                pointer = box29.click(x,y, pointer) 
                pointer = box210.click(x,y, pointer) 
                pointer = box31.click(x,y, pointer) 
                pointer = box32.click(x,y, pointer) 
                pointer = box33.click(x,y, pointer) 
                pointer = box34.click(x,y, pointer) 
                pointer = box35.click(x,y, pointer) 
                pointer = box36.click(x,y, pointer) 
                pointer = box37.click(x,y, pointer) 
                pointer = box38.click(x,y, pointer) 
                pointer = box39.click(x,y, pointer) 
                pointer = box310.click(x,y, pointer) 
                pointer = one.clickk(x,y,pointer)
                pointer = two.clickk(x,y,pointer)
                pointer = three.clickk(x,y,pointer)
                pointer = four.clickk(x,y,pointer)
                '''
                pointer = one.fire.click(x,y, pointer) 
                pointer = one.cooking.click(x,y, pointer) 
                
                pointer = two.fire.click(x,y, pointer) 
                pointer = two.cooking.click(x,y, pointer) 
                
                pointer = three.fire.click(x,y, pointer) 
                pointer = three.cooking.click(x,y, pointer) 
                pointer = four.fire.click(x,y, pointer) 
                pointer = four.cooking.click(x,y, pointer) 
                '''
                print pointer
        gameDisplay.blit(bgImg,(0,0))
        one.cook(gameDisplay)
        two.cook(gameDisplay)
        three.cook(gameDisplay)
        four.cook(gameDisplay)
        box11.disp(gameDisplay)
        box12.disp(gameDisplay)
        box13.disp(gameDisplay)
        box14.disp(gameDisplay)
        box15.disp(gameDisplay)
        box16.disp(gameDisplay)
        box17.disp(gameDisplay)
        box18.disp(gameDisplay)
        box19.disp(gameDisplay)
        box110.disp(gameDisplay)
        box21.disp(gameDisplay)
        box22.disp(gameDisplay)
        box23.disp(gameDisplay)
        box24.disp(gameDisplay)
        box25.disp(gameDisplay)
        box26.disp(gameDisplay)
        box27.disp(gameDisplay)
        box28.disp(gameDisplay)
        box29.disp(gameDisplay)
        box210.disp(gameDisplay)
        box31.disp(gameDisplay)
        box32.disp(gameDisplay)
        box33.disp(gameDisplay)
        box34.disp(gameDisplay)
        box35.disp(gameDisplay)
        box36.disp(gameDisplay)
        box37.disp(gameDisplay)
        box38.disp(gameDisplay)
        box39.disp(gameDisplay)
        box310.disp(gameDisplay)
        two.dispp(gameDisplay)
        one.dispp(gameDisplay)
        three.dispp(gameDisplay)
        four.dispp(gameDisplay)
        '''
        two.fire.disp(gameDisplay)
        two.cooking.disp(gameDisplay)
        
        three.fire.disp(gameDisplay)
        three.cooking.disp(gameDisplay)
        four.fire.disp(gameDisplay)
        four.cooking.disp(gameDisplay)
        '''
        if pointer == 1:
            ham(x,y)
        if pointer == 2:
            gameDisplay.blit(woodImg,(x,y))
        if pointer == 3:
            gameDisplay.blit(ham1Img,(x,y))
        pygame.display.update()
        clock.tick(60)

game()
pygame.quit()

quit()
