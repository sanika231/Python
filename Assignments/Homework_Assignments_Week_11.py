##Homework Assignments Week 11
##Question1
def books(days):
    booksread=days//6
    return booksread

days=int(input("how many days have passed "))
print("the number of books read is",books(days))


##Question2
import datetime
import time
def greeting(month):
    time=datetime.datetime.now()
    hours = time.hour;
    print(hours)
    if hours<=12:
        print("good morning!")
    if hours<=18 and hours>12:
        print("good afternoon!")
    if hours<=21 and hours>18:
        print("good evening!")
    if hours>21:
        print("good night!")
    if month=="feb" or month=="mar" or month=="apr":
        print("time for some spring cleaning")
    if month=="may" or month=="jun" or month=="jul":
        print("nothing beats swimming in this weather")
    if month=="aug" or month=="sept" or month=="oct":
        print("happy monsoons")
    if month=="nov" or month=="dec" or month=="jan":
        print("its been chilly out there")

month=input("enter what month it is ")
greeting(month)

import datetime
t=datetime.datetime.now()
print(t)

##Question3
import random
from datetime import *
def createlist(L):
    for n in range(1,21,1):
        num=random.randint(1,100)
        L.append(num)
    print(L)
    for n in range(0,5,1):
        print(L[n])

def user_move(L,index,result):
    correct=0
    a=datetime.now()- datetime.now()
    print (a)
    for n in range(1,3,1):
        t1=datetime.now()
        guess=int(input("guess the next number "))
        t2=datetime.now()
        a = a + (t2-t1)
        print (a,n)
        if guess==L[index]:
            print("correct")
            correct=correct+1
            result[0]="success"
            return a
        else:
            if n==2:
                print("Not correct")
                result[0]="fail"
                return a
        print("ur score is",correct)
        

L=[]
result=["status"]
createlist(L)
totalt=datetime.now()- datetime.now()
for k in range(5,20,1):
    totalt=totalt+user_move(L,k,result)
    print ("total_time is", totalt, "K is", L[k])

##Question4
L=["chocolate","cookiesncream","vanilla","mango","mint"]
print(L)
def icecream():
    remove=input("which flavor would u like to remove ")
    L.remove(remove)
    print(L)

icecream()   
        

##Question5
d={"the hunger games":"suzanne collins","divergent":"veronica roth","throne of glass":"sarah j. mass"}
def sort():
    c=sorted(d.items(),reverse=1)
    print(c)
sort()

##Question6
def factorial(n):
    if n==0:
        return 1
    else:
        result=n*factorial(n-1)
        return result

n=int(input("enter a num "))
print("factorial of",n," is",factorial(n))

##Question7
def calculate(time,distance):
    sec=time*3600
    meters=distance*1000
    speed=meters/sec
    print("speed is",speed,"in m/s ")

time=int(input("enter num of hrs "))
distance=int(input("enter distance in kilometers "))
calculate(time,distance)

##Question8
radius=0
base=0
height=0
def circle(radius):
    radius=int(input("enter radius of circle "))
    area=3.14*radius**2
    print("the area is",area)
def triangle(base,height):
    base=int(input("enter base "))
    height=int(input("enter height "))
    area=base*height/2
    print("the area is",area)
def rectangle(base,height):
    base=int(input("enter base "))
    height=int(input("enter height "))
    area=base*height
    print("the area is",area)

shape=input("select circle,triangle or rectangle " )
if shape=="circle":
    circle(radius)
if shape=="triangle":
    triangle(base,height)
if shape=="rectangle":
    rectangle(base,height)

##Question9
def soup():
    d={"vegetable":"3.50","tomato":"4.50"}
    print(d)
def main():
    d={"salad":"10.50","pasta":"7.80","rice":"6.40"}
    print(d)
def dessert():
    d={"cookies":"5.50","cake":"7.80","cupcakes":"3.40","mango lassi":"5.50"}
    print(d)
soup()
main()
dessert()

Question10
def letters(w1,w2,w3):
    L=[]
    W1=list(w1)
    W2=list(w2)
    W3=list(w3)
    for i in W1:
        if i not in L:
            L.append(i)
    for i in W2:
        if i not in L:
            L.append(i)
    for i in W3:
        if i not in L:
            L.append(i)
    print(L)
        

w1=input("enter a word")
w2=input("enter another word")
w3=input("enter another word")
letters(w1,w2,w3)













    
