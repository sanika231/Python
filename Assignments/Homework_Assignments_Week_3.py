##Homework Question1
import random
num1=int(input("enter a number for start range "))
num2=int(input("enter a second number for end range "))
for n in range(1,31,1):
    numbers=random.randrange(num1,num2,1)
    if numbers%2==0:
        print(n,numbers, "even")
    if numbers%2!=0:
        print(n,numbers, "odd")
        

##Homework Question2
import random
first=input("enter your first name ")
last=input("enter your last name ")
if len(first)==len(last):
    number=random.randint(1,10)
    print(first,last,number, sep='')
if len(first)!=len(last):
    number=random.randint(20,200)
    print(first,last,number, sep='')

##Homework Question3
import random
num1=random.randint(1,100)
num2=random.randint(1,100)
num3=random.randint(1,100)
print(num1)
print(num2)
print(num3)
if num1>num2 and num1>num3:
    print("the first number is the greatest")
if num2>num1 and num2>num3:
    print("the second number is the greatest")
if num3>num1 and num3>num2:
    print("the third number is the greatest")

##Homework Question4
import random
for n in range(1,26,1):
    numbers=random.randrange(50,150,1)
    if numbers%2==0 and numbers%3==0:
        print(numbers, "is also divisible by 6")
    if numbers%2!=0 or numbers%3!=0:
        print(numbers, "is not divisible by 6")

##Homework Question5
import random
num1=random.randint(1,10)
num2=random.randint(1,10)
num3=random.randint(1,10)
print(num1, num2, num3)
if num2>num1 and num2>num3:
    print("Yay!")
