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
color=yellow
x=320
y=240
ychange=50
radius=20
thickness=0
c=pure_green
width=30
length=180
length2=480
x1=550
y1=0
y2=320
count="0"

def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("Great Vibes", 32, bold=True, italic=False)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

#upload and resize image
bg=pygame.image.load("background.png")
bg=pygame.transform.scale(bg,(640,480))

b=pygame.image.load("bird.png")
b=pygame.transform.scale(b,(40,40))

pipe=pygame.image.load("toppipe.png")
pipe=pygame.transform.scale(pipe,(width,length))

pipetwo=pygame.image.load("bottompipe.png")
pipetwo=pygame.transform.scale(pipetwo,(width,length2))

while True:
    screen.blit(bg,(0,0))
    bird=screen.blit(b,(x-20,y-20))
    pipe1=screen.blit(pipe,(x1,y1))
    pipe2=screen.blit(pipetwo,(x1,y2))
    time.delay(100)
    string="Score:" + count
    show_text(string,280,50,pure_blue,32)
    #pipe1=pygame.draw.rect(screen, c, (x1, y1, width, length), thickness)
    #pipe2=pygame.draw.rect(screen, c, (x1, y2, width, length2), thickness)
    #bird=pygame.draw.circle(screen, color, (x, y), radius, thickness)
    if bird.colliderect(pipe1) or bird.colliderect(pipe2) or y<0 or y>480:
        screen.fill(black)
        show_text("game over!",250,220,pure_red,32)
        pygame.display.update()
        print('collision')
        break
    y=y+5
    x1=x1-5
    if x1<=0:
        x1=640
        length=random.randint(1,240)
        pipe=pygame.transform.scale(pipe,(width,length))
        y2=length+150
    if x1<251 and x1>249:
        count=int(count)+1
        count=str(count)
        string="Score:" + str(count)
        pygame.display.update
    if int(count)==10:
        show_text(string,280,50,pure_blue,32)
        show_text("you win!!",280,200,purple,32)
        pygame.display.update()
        break
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                 y=y-ychange
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
