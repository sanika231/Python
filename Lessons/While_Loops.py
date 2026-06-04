##n=1
##while n<51:
##    print(n)
##    n=n+1

##n=-120
##while n<121:
##    print(n)
##    n=n+1

##n=20
##d="decrease" 
##while n<36:
##    print(n)
##    if d=="decrease":
##        n=n-1
##    elif d=="increase":
##        n=n+1
##    if n==0:
##        d="increase"
    
##n=-17
##d="increase"
##run=True
##while run==True:
##    print(n)
##    if d=="increase":
##        n=n+1
##    elif d=="decrease":
##        n=n-1
##        if n==7:
##            print("bing!")
##            run=False
##    if n==25:
##        d="decrease"

##n=1
##d="increase"
##while True:
##    print(n)
##    if d=="increase":
##        n=n+1
##    elif d=="decrease":
##        n=n-1
##    if n==10:
##        d="decrease"
##    if n==1:
##        d="increase"

##import time
##import random
##while True:
##    decimal=random.uniform(1,100)
##    num=random.randint(1,100)
##    print(decimal)
##    print(num)
##    time.sleep(3)

##import time
##n=5
##while n>0:
##    print(n)
##    n=n-1
##    time.sleep(1)
##
##print("blast off!")

##n=1
##while True:
##    print(n)
##    n=n+1
##    if n==16:
##        print("hello")
##        break

##import random
##import time
##deposit=int(input("how much money would you like to deposit in your account "))
##while True:
##    dice=input("would you like to roll the dice? yes/no ")
##    if dice=="yes":
##        dice1=random.randint(1,6)
##        dice2=random.randint(1,6)
##        print(dice1)
##        print(dice2)
##        print("waiting for a few secs")
##        time.sleep(2)
##        if dice1==dice2:
##            print("you won")
##            deposit=deposit+5
##        else:
##            print("you lost")
##            deposit=deposit-1
##        if deposit==0:
##            print("thank you for playing")
##            break
##    else:
##        print("thank you for playing")
##        break
    
##password="september"
##while True:
##    pcheck=str(input("enter the password "))
##    if password==pcheck:
##        print("Access Granted")
##        break
##    if password!=pcheck:
##        print("Access Denied")

##import random
##while True:
##    num=random.randint(100,999)
##    print(num)
##    if num%23==0:
##        break

##import random
##count=0
##while True:
##    num=random.randint(20,30)
##    guess=int(input("guess a number between 20 and 30 "))
##    if guess!=num:
##        count=count+1
##    else:
##        print(count)
##        break
    
##while True:
##    string=input("enter a string ")
##    if string=="stop":
##        break
##    else:
##        for n in range(0,len(string),1):
##            print(string[n])






