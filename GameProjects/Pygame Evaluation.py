##import pygame
##from pygame import *
##
##pygame.init()
##
##screen = pygame.display.set_mode((640,480))
##
##pygame.display.set_caption("Shapes!!")
##
##yellow=(235,225,0)
##pure_red=(255,0,0)
##pure_blue=(0, 0, 255)
##pure_green=(0, 255, 0)
##pink=(175, 0, 175)
##orange=(240, 100, 0)
##black=(0,0,0)
##purple=(160,32,240)
##white=(255,255,255)
##
##def show_text(msg, x, y, color, size):
##    fontobj = pygame.font.SysFont("Comic Sans", 32, bold=True, italic=False)
##    msgobj = fontobj.render(msg,False,color)
##    screen.blit(msgobj,(x, y))
##
##color=pure_blue
##x=320
##y=240
##radius=20
##thickness=0
##
##while True:
##    screen.fill(black)
##    pygame.draw.circle(screen, color, (x, y), radius, thickness)
##    if x<320:
##        radius=radius+1
##    if x>320:
##        radius=radius-1
##    for event in pygame.event.get():
##        if event.type==MOUSEMOTION:
##            (x,y)=event.pos
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##
##    pygame.display.update()

##Problem2

import pygame
from pygame import *

pygame.init()

screen = pygame.display.set_mode((640,480))

pygame.display.set_caption("Shapes!!")

yellow=(235,225,0)
pure_red=(255,0,0)
pure_blue=(0, 0, 255)
pure_green=(0, 255, 0)
pink=(175, 0, 175)
orange=(240, 100, 0)
black=(0,0,0)
purple=(160,32,240)
white=(255,255,255)

a=40

b=pygame.image.load("bird.png")
b=pygame.transform.scale(b,(40,40))

def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("Comic Sans", 32, bold=True, italic=False)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

while True:
    b=screen.blit(b,(320,240))
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_UP:
                a=a+1
                b=pygame.transform.scale(b,(a,a))
            if event.key==K_DOWN:
                a=a-1
                b=pygame.transform.scale(b,(a,a))
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()


