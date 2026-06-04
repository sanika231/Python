import pygame
import random
from pygame import *

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake Game!!")

foodx = (random.randint(0, 630)//10)*10
foody = (random.randint(0, 470)//10)*10
fcolor = (255, 0, 0)
width = 10
length = 10
thickness = 0

snakex = (random.randint(1, 640)//10)*10
snakey = (random.randint(1, 480)//10)*10
scolor = (255, 255, 0)
w = 10
l = 10

down = 0
up = 0
right = 0
left = 0

a = 10

L = [0]
T = [0]

for n in range(0, 470):
    n = n + 10
    L.append(n)

for j in range(0, 630):
    j = j + 10
    T.append(j)

snakelist = [[snakex, snakey]]

def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("Comic Sans", 32, bold = True, italic = False)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))

bg = pygame.image.load("snakebackground.png")
bg = pygame.transform.scale(bg, (640, 480))

f = pygame.image.load("food.png")
f = pygame.transform.scale(f, (20, 20))

##s=pygame.image.load("snake.png")
##s=pygame.transform.scale(s,(20,20))

while True:
    screen.blit(bg,(0, 0))
    pygame.time.delay(100)

    snakelist.insert(0, [snakex, snakey])
    snakelist.pop()

    food = screen.blit(f, (foodx-5, foody-5))
   
    for n in snakelist:
        pygame.draw.rect(screen, scolor, (n[0], n[1], w + 10, l + 10), thickness)

    #if x1<=x+a/2<=x1+a and y1<=y+a/2<=y1+a: # x<=x1<=x+10 and y<=y1<=y+10:
    if snakex in (foodx,foodx+10) and snakey in (foody,foody+10):
        #print(foodx, " ", foody)
        foodx = (random.randint(0, 630)//a)*a
        foody = (random.randint(0, 470)//a)*a
        snakelist.append([foodx, foody])

    if snakelist[0] in snakelist[1: len(snakelist)]:
        screen.fill((0, 0, 0))
        show_text("game over!", 250, 220, c, 32)
        pygame.display.update()
        pygame.time.delay(100)
        pygame.quit()
        exit()

    if len(snakelist) == 4:
        print(snakelist)
        snakelist = [[snakex, snakey]]
        print(snakelist)
        a = a + 5

    if snakex < 0:
        left = 1
        snakex = 640
    if snakex > 640:
        right = 1
        snakex = 0
    if snakey < 0:
        up = 1
        snakey = 480
    if snakey > 480:
        down = 1
        snakey = 0

    #snakelist.append([x1,y1])
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN and up == 0:
                down = 1
                up = 0
                right = 0
                left = 0
            if event.key == K_UP and down == 0:
                up = 1
                down = 0
                right = 0
                left = 0
            if event.key == K_RIGHT and left == 0:
                right = 1
                up = 0
                down = 0
                left = 0
            if event.key == K_LEFT and right == 0:
                left = 1
                up = 0
                right = 0
                down = 0

        if event.type == QUIT:
            pygame.quit()
            exit()

    if down == 1:
        snakey = snakey + a
    if up == 1:
        snakey = snakey - a
    if right == 1:
        snakex = snakex + a
    if left == 1:
        snakex = snakex - a

    pygame.display.update()
