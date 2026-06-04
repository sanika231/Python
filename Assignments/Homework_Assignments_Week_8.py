##Lists Advanced Questions Homework

##Question 9
animal_names=["cat","dog","mouse"]
animal_sounds=["meow","ruff","squeak"]
young_ones=["kitty","puppy","babymouse"]
animals=["cat","dog","mouse","meow","ruff","squeak","kitty","puppy","babymouse"]
for n in range(0,3,1):
    b=n+3
    c=n+6
    print(animals[n])
    print(animals[b])
    print(animals[c])

##Question 10
a = [1,2,3,4,5]
for n in range(0,5,1):
    print(a[n])

##Question 11
a = [1,2,3,4,5]
for n in range(1,6,1):
    print(n)
    for t in range(0,5,1):
        print(a[t])

##Question 12
a = [1,2,3,4,5]
for n in range(1,6,1):
    print(n)
    for t in range(0,5,1):
        print(a[t], end="")
    print("")

##Question 13
a = [1,2,3,4,5]
for n in range(0,5,1):
    print(a[n])
    print(a[n])

##Question 14
a = [1,2,3,4,5]
for n in range(0,5,1):
    print(a[n],a[n])

##Question 15
a = [1,2,3,4,5]
b = [6,7,8,9,10]
for n in range(1,6,1):
    print(n)
    for t in range(0,5,1):
        print(b[t])

##Question 16
a = [[[1,2], [3,4]]]
print(a[0][0])
print(a[0][1])

##Question 17
a = [[[1,2], [3,4]]] 
b = [[[5,6], [7,8]]]
print(a[0][0][0]+b[0][0][0],a[0][0][1]+b[0][0][1])
print(a[0][1][0]+b[0][1][0],a[0][1][1]+b[0][1][1])

##Question 18
import random
L=[]
while len(L)<10:
    num=random.randint(1,10)   
    if num not in L:
        L.append(num)
print(L)

##Question 19
import random
eventcount=0
cards=["JoS","KoC","QoH","AoD"]
for n in range(1,6,1):
    random.shuffle(cards)
    if cards.index("AoD")-cards.index("KoC")==1:
        eventcount+=1
print("the probability is",eventcount,"/5")






