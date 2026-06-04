##for n in range(1,11,1):
##    if n%2!=0:
##        print(n)
##    if n%2==0:
##        print("-",n)

##n=1
##while n<11:
##    if n%2!=0:
##        print(n, end=',')
##    else:
##        print("-",n, end=',')
##    n=n+1


##n=0
##n2=1
##for r in range(0,9,1):
##    n3=n+n2
##    print(n3, end=',')
##    n=n2
##    n2=n3

##n=0
##n2=1
##r=0
##while r<9:
##    n3=n+n2
##    print(n3, end=',')
##    n=n2
##    n2=n3 
##    r=r+1


##n=1
##r=1
##t=0
##while t<10:
##    n=n+r
##    print(n, end=',')
##    r=r+1
##    t=t+1

##Homework Assignment Week 6 Questions
##Question 14
##r=2
##for n in range(1,22,1):
##    if n<11:
##        print(n)
##    elif n>11:
##        n=n-r
##        print(n)
##        r=r+2
##    else:
##        print(" ")

##Question1
n=1
first_if_done=0
while True:
    if n<11 and first_if_done==0:
        print(n)
        n=n+1
        if n==11:
          first_if_done=1
    else:
        print(n-1)
        if n>2: 
          n=n-1
        else:
          n=11
          print (" ")

##Extra   
##n=1
##meow=0
##first_if_done=0
##while meow<30:
##    meow= meow+1
##    if n<11 and first_if_done==0:
##        print(n)
##        n=n+1
##        if n==11:
##          first_if_done=1
##          print (" ")
##    else:
##        print(n-1)
##        if n>2: 
##          n=n-1
##        else:
##          n=1
##          print (" ")
##          first_if_done=0

##Question2
num=1
while num<6:
    print("Hello", end=str(num))
    print("")
    num=num+1

##Question3
n=1
while True:
    print(n)
    n=n+1
    if n==11:
        break

##Question4/5/6/7
for n in range(1,731,1):
    n=n+1
    if n==10:
        print("mooh has produced", n, "bottles of milk in 10 days")
    if n==365:
        print("mooh has produced", n, "bottles of milk in one year")
    if n==281:
        print("mooh has produced", n, "bottles of milk in a year with a week of rest every month")
    if n==562:
        print("mooh and mooh2 have produced", n, "bottles of milk in a year with a week of rest every month")

  
##Question8
for n in range(1,4,1):
    w=10
    for n in range(1,12,1):
        if n%2!=0:
            print(w*" ",n*"*")
            w=w-1
for n in range(1,11,1):
    w=10
    print(w*" ","*")


##Question9
for n in range(1,4,1):
    w=5
    for n in range(12,0,-1):
        if n%2!=0:
            print(w*" ",n*"*")
            w=w+1
for n in range(1,11,1):
    w=10
    print(w*" ","*")










