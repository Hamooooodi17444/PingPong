import pygame
import sys
svart=(0,0,0)
vitt=(255,255,255)
röd=(255,0,0)
grön=(0,255,0)
blå=(0,0,255)

pygame.init()

storlek = (800,600)
screen=pygame.display.set_mode(storlek)
rectx=400
recty=580

bollx=50
bolly=50

boll_justering_x=0
bolll_justering_y=0

score = 0
def drawrect(skärm,x,y):
    if x <= 0:
        x = 0
    if x >= 700:
        x=700
    pygame.draw.rect(skärm,röd,{x,y,100,20})

# göra loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
