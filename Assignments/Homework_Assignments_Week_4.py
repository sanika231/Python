##Homework 4a: For Loops
for n in range(1,23,1):
    print("sanika")

for n in range(10,41,1):
    print(n)

for n in range(1,51,1):
    if n%2==0:
        print(n)

for n in range(1,51,1):
    if n%2!=0:
        print(n)

for n in range(1,31,1):
    if n%3==0:
        print(n)

num=int(input("enter a number "))
for n in range(1,num,1):
    if n%2==0:
        print(n)

for n in range(1,11):
    name=input("what is your name? ")
    print("hello", name)

for n in range(50,0,-1):
    print(n)

##Answer to Question 9
## a)5
## b)n
## c)to allow you to execute steps a certain number of times in a looping manner without having to repeat code
## d)start=1, stop=10, step=2

name=input("enter your name ")
for n in range(0,len(name),1):
    print(name[n])

import time
string=input("enter a string ")
for n in range(0,len(string),1):
    print(string[n])
    time.sleep(2)

import random
print(random.uniform(1,100)) ##random.uniform prints random decimal

import random
for n in range(1,16,1):
    print(random.uniform(1,100))

import random
for n in range(1,21,1):
    print(random.uniform(1,100))

import random
num=random.randint(15,20)+random.random()
print(num)

import random
print(random.randint(1,100))

import random
for n in range(1,6,1):
    print(random.randint(100,500))

import time
import random
time.sleep(3)
for n in range(1,16,1):
    print(random.randint(1,100))

import time
import random
for n in range(1,11,1):
    print(random.randint(1,100))
    time.sleep(3)

import random
import time
num=random.randint(1,100)
print("the random number is ",num)
time.sleep(2)
for n in range(1,num,1):
    print(n)
