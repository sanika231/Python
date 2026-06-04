import pygame
import random
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

foodx=(random.randint(0,630)//10)*10
foody=(random.randint(0,470)//10)*10

color=pure_red
x=foodx
y=foody
width=10
length=10
thickness=0

snakex=(random.randint(1,640)//10)*10
snakey=(random.randint(1,480)//10)*10

c=pure_green
x1=snakex
y1=snakey
w=10
l=10

down=0
up=0
right=0
left=0

L=[0]
T=[0]
for n in range(0,470):
    n=n+10
    L.append(n)

for j in range(0,630):
    j=j+10
    T.append(j)

snakelist=[[x1,y1]]

a=10

def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("Comic Sans", 32, bold=True, italic=False)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

bg=pygame.image.load("snakebackground.png")
bg=pygame.transform.scale(bg,(640,480))

f=pygame.image.load("food.png")
f=pygame.transform.scale(f,(20,20))

##s=pygame.image.load("snake.png")
##s=pygame.transform.scale(s,(20,20))

while True:
    #adding blits
    screen.blit(bg,(0,0))
    food=screen.blit(f,(x-5,y-5))
    #snake=screen.blit(s,(x1,y1))
    time.delay(100)
    #screen.fill(black)
    
    #food
    ##pygame.draw.rect(screen, color, (x, y, width, length), thickness)

    #snake
##    for segment in snakelist:
##        pygame.draw.rect(screen, c, segment+[10,10])
    for n in snakelist:
        pygame.draw.rect(screen, c, (n[0], n[1], w+a, l+a), thickness)
    if x1<=x+a/2<=x1+a and y1<=y+a/2<=y1+a: # x<=x1<=x+10 and y<=y1<=y+10:
        print(x," ",y)
        x=(random.randint(0,630)//a)*a
        y=(random.randint(0,470)//a)*a
##        x=random.choice(T)
##        y=random.choice(L)
        snakelist.append([x1,y1])
    snakelist.insert(0,[x1,y1])
    snakelist.pop()
    if snakelist[0] in snakelist[1:len(snakelist)]:
        screen.fill(black)
        show_text("game over!",250,220,pure_red,32)
        pygame.display.update()
        print('you died')
        break
    if len(snakelist)==4:
        print(snakelist)
        snakelist=[[x1,y1]]
        print(snakelist)
        a=a+5
    if x1<0:
        left=1
        x1=640
    if x1>640:
        right=1
        x1=0
    if y1<0:
        up=1
        y1=480
    if y1>480:
        down=1
        y1=0
    #snakelist.append([x1,y1])
    for event in pygame.event.get(): 
        if event.type==KEYDOWN:
            if event.key==K_DOWN and K_UP==0:
                down=1
                up=0
                right=0
                left=0
            if event.key==K_UP and K_DOWN==0:
                up=1
                down=0
                right=0
                left=0
            if event.key==K_RIGHT and K_LEFT==0:
                right=1
                up=0
                down=0
                left=0
            if event.key==K_LEFT and K_RIGHT==0:
                left=1
                up=0
                right=0
                down=0
        if event.type == QUIT:
            pygame.quit()
            exit()
    if down==1:
        y1=y1+a
    if up==1:
        y1=y1-a
    if right==1:
        x1=x1+a
    if left==1:
        x1=x1-a

    pygame.display.update()
