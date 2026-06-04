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

def show_text(msg, x, y, color, size):
    fontobj = pygame.font.SysFont("Script", 32, bold=True, italic=False)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

#start screen
def menu():
    c=purple
    width=200
    length=100
    thickness=0
    x=70
    x1=370
    y=140
    t=x+width/3
    k=x1+width/2.75
    m=y+length/4
    while True:
        pygame.draw.rect(screen, c, (x, y, width, length), thickness)
        pygame.draw.rect(screen, c, (x1, y, width, length), thickness)
        show_text("Play",t,m,white,32)
        show_text("Quit",k,m,white,32)
        show_text("Tic Tac Toe",width/3,30, white,32)
        show_text("By: Sanika Thatte",width/3, 50, white, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type== MOUSEBUTTONDOWN:
                if x<=event.pos[0]<=x+width and y<=event.pos[1]<=y+length:
                    screen.fill(black)
                    tictactoe()
                if x1<=event.pos[0]<=x1+width and y<=event.pos[1]<=y+length:
                    pygame.quit()
                    exit()
        pygame.display.update()

##tictactoe game function
def tictactoe():
    color=white
    thickness=2
    radius=40

    turn=0

    screen = pygame.display.set_mode((300,300))

    d={1:"",2:"", 3:"", 4:"",5:"",6:"",7:"",8:"",9:"",}

    def mouseplace(cellnum, symbol):
        if d[cellnum]=="":
            if symbol=="x":
                if cellnum==1:
                    x1=0
                    y1=100
                    d[1]="x"
                elif cellnum==2:
                    x1=100
                    y1=100
                    d[2]="x"
                elif cellnum==3:
                    x1=200
                    y1=100
                    d[3]="x"
                elif cellnum==4:
                    x1=0
                    y1=200
                    d[4]="x"
                elif cellnum==5:
                    x1=100
                    y1=200
                    d[5]="x"
                elif cellnum==6:
                    x1=200
                    y1=200
                    d[6]="x"
                elif cellnum==7:
                    x1=0
                    y1=300
                    d[7]="x"
                elif cellnum==8:
                    x1=100
                    y1=300
                    d[8]="x"
                else:
                    x1=200
                    y1=300
                    d[9]="x"
                draw_x(x1,y1)
            else:
                if cellnum==1:
                    x1=50
                    y1=50
                    d[1]="o"
                elif cellnum==2:
                    x1=150
                    y1=50
                    d[2]="o"
                elif cellnum==3:
                    x1=250
                    y1=50
                    d[3]="o"
                elif cellnum==4:
                    x1=50
                    y1=150
                    d[4]="o"
                elif cellnum==5:
                    x1=150
                    y1=150
                    d[5]="o"
                elif cellnum==6:
                    x1=250
                    y1=150
                    d[6]="o"
                elif cellnum==7:
                    x1=50
                    y1=250
                    d[7]="o"
                elif cellnum==8:
                    x1=150
                    y1=250
                    d[8]="o"
                else:
                    x1=250
                    y1=250
                    d[9]="o"
                circle(x1,y1)

        else:
            print("please pick another number")
        

    def draw_x(x1,y1):
        print(event.pos)
        
        x2=x1+100
        y2=y1-100

        x3=x1
        y3=y1-100

        x4=x1+100
        y4=y1
        pygame.draw.line(screen, color, (x1,y1), (x2,y2), thickness)
        pygame.draw.line(screen, color, (x3,y3), (x4, y4), thickness)


    def circle(x1,y1):
        print(event.pos)
        pygame.draw.circle(screen, color, (x1,y1), radius, thickness)

    while True:
        pygame.draw.line(screen, color, (100,0), (100,300), thickness)
        pygame.draw.line(screen, color, (200,0), (200,300), thickness)
        pygame.draw.line(screen, color, (0,100), (300,100), thickness)
        pygame.draw.line(screen, color, (0,200), (300,200), thickness)
        if d[7]==d[8]==d[9]=="x" or d[4]==d[5]==d[6]=="x" or d[1]==d[2]==d[3]=="x" or d[1]==d[4]==d[7]=="x" or d[2]==d[5]==d[8]=="x" or d[3]==d[6]==d[9]=="x" or d[1]==d[5]==d[9]=="x" or d[3]==d[5]==d[7]=="x":
            show_text("player 1 wins!",45,100,pure_blue,20)
            pygame.display.update()
            time.delay(1000)
            screen = pygame.display.set_mode((640,480))
            print("1")
            break
        if d[7]==d[8]==d[9]=="o" or d[4]==d[5]==d[6]=="o" or d[1]==d[2]==d[3]=="o" or d[1]==d[4]==d[7]=="o" or d[2]==d[5]==d[8]=="o" or d[3]==d[6]==d[9]=="o" or d[1]==d[5]==d[9]=="o" or d[3]==d[5]==d[7]=="o":
            show_text("player 2 wins!",45,100,pure_red,20)
            pygame.display.update()
            time.delay(1000)
            screen = pygame.display.set_mode((640,480))
            print("2")
            break
        if d[1]!="" and d[2]!="" and d[3]!="" and d[4]!="" and d[5]!="" and d[6]!="" and d[7]!="" and d[8]!="" and d[9]!="":
            show_text("its a tie!",80,100,pure_red,20)
            pygame.display.update()
            time.delay(1000)
            screen = pygame.display.set_mode((640,480))
            print("its a tie!")
            break
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type==MOUSEBUTTONDOWN:
                if event.pos[0] in range(0,100):
                    if event.pos[1] in range(0,100):
                        cellnum=1
                    if event.pos[1] in range(100,200):
                        cellnum=4
                    if event.pos[1] in range(200,300):
                        cellnum=7
                if event.pos[0] in range(100,200):
                    if event.pos[1] in range(0,100):
                        cellnum=2
                    if event.pos[1] in range(100,200):
                        cellnum=5
                    if event.pos[1] in range(200,300):
                        cellnum=8
                if event.pos[0] in range(200,300):
                    if event.pos[1] in range(0,100):
                        cellnum=3
                    if event.pos[1] in range(100,200):
                        cellnum=6
                    if event.pos[1] in range(200,300):
                        cellnum=9

                if turn==0:
                    symbol="x"
                    turn=1
                else:
                    symbol="o"
                    turn=0
                mouseplace(cellnum, symbol)
                
                        
                    

        pygame.display.update()


#running loop
while True:
    menu()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type== MOUSEBUTTONDOWN:
            if x<=event.pos[0]<=x+width and y<=event.pos[1]<=y+length:
                screen.fill(black)
                tictactoe()
            if x1<=event.pos[0]<=x1+width and y<=event.pos[1]<=y+length:
                pygame.quit()
                exit()

    pygame.display.update()

