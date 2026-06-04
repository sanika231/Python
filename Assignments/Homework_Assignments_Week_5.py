##Homework Assignment: While Loops

##Question 1
import random
n=1
while n<11:
    integers=random.randint(1,100)
    n=n+1
    if integers%5==0:
        print("this number is divisible by 5: ", integers)
    else:
        pass

##Question 2
n=1
while True:
    n=n+1
    if n%2==0:
        print("Hello")
    else:
        print("World")
    
##Question 3
while True:
    email=str(input("enter valid email adress "))
    if "@" in email and ".com" in email:
        break

##Question 4
import random
while True:
    n=random.randint(1,10)
    print(n)
    if n==7:
        break

##Question 5
while True:
    string=input("enter a string ")
    if len(string)>7:
        break
    
