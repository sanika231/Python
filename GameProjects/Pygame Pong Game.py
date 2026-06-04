import random
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

color=pure_red
color1=pure_blue
x=5
y=5
x1=585
y1=5
width=50
length=200
thickness=0
up=False
down=False
w=False
s=False

x2=320
y2=240
color2= purple
a=30
b=5
count1="0"
count2="0"

##give point to other player when ball hits wall
##declare winner

def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("Comic Sans", 32, bold=False, italic=False)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

string1="Player1:" + count1
string2="Player2:" + count2

while True:
    screen.fill(black)
    time.delay(90)
    string1="Player1:" + count1
    string2="Player2:" + count2
    show_text(string1,100,50,pink,32)
    show_text(string2,400,50,pink,32)
    pygame.draw.rect(screen, color, (x, y, width, length), thickness)
    pygame.draw.rect(screen, color1, (x1, y1, width, length), thickness)
    pygame.draw.circle(screen, color2, (x2, y2), 30, thickness)
    x2=x2+a
    y2=y2+b
    if x2>=610 or x2<=30:
        a=-a
    if y2>=450 or y2<=30:
        b=-b
    if (x2+30 >= x1 and y1<=y2<=y1+200):
        a=-30
        b=-5
        print("Collision with Right Paddle Detected")
        count2=int(count2)+1
        count2=str(count2)
        b=random.randint(-30,30)
    elif x2>=610:
        count1=int(count1)+1
        count1=str(count1)
    if (x2-30 <= x and y<=y2<=y+200):
        a=30
        b=5
        print("Collision with Left Paddle Detected")
        count1=int(count1)+1
        count1=str(count1)
        b=random.randint(-30,30)
    elif x2<=30:
        count2=int(count2)+1
        count2=str(count2)

    if count1==20 or count2==20:
        if count1==20:
            show_text("player 1 has won the game!",100,50,pink,32)
            pygame.display.update()
            break
        else:
            show_text("player 2 has won the game!",100,50,pink,32)
            pygame.display.update()
            break
    
    if up==True:
        y1=y1-30
    if down==True:
        y1=y1+30
    if w==True:
        y=y-30
    if s==True:
        y=y+30
    if y1<=0:
        y1=0
    if y1>=280:
        y1=280
    if y<=0:
        y=0
    if y>=280:
        y=280
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_UP:
                up=True
            if event.key==K_DOWN:
                down=True
            if event.key==K_w:
                w=True
            if event.key==K_s:
                s=True
        if event.type==KEYUP:
            up=False
            down=False
            w=False
            s=False
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
