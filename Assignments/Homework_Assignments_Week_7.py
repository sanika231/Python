##Question1
L=[]
L.append("apple")
L.append("orange")
L.append("banana")
L.append("mango")
L.append("grape")
print(L)

##Question2
L=[]
for n in range(1,100,1):
    if n%3==0:
        L.append(n)
print(L)

##Question3
##Pop is used to remove the last item in a list.
##Remove is used to remove a specified item from a list.

##Question4
##Append adds to the end of a list.
##When insert is used, a specific position can be specified.

##Question5
L=["2","3","5","7"]
for n in range(1,100,1):
    if n>10:
        if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0:
            L.append(n)

print("Length of the list is ",len(L))

##Question6
##It is always 0

##Question7&8
L=["1","2","3","4","5","6","7","8","9","10"]
for n in range(2,len(L)):
    print(L[n])

k=len(L)-5
for n in range(k,len(L)):
    print(L[n])

##Question9&10
L=["a","b","c","d","e","f","g","h","i","j"]
for n in range(0,10):
    if n%2==0:
        print(L[n])

for n in range(0,10):
    if n%2!=0:
        print(L[n])

##Question11
It will print numbers 1 through 5

##Question12
numbers=[1,2,3,4,5]
numbers[0]=24
print(numbers)

##Question13
sentence = "I am 12 years old"
wordList = sentence.split()
print(wordList)
##sentence.split

##Question14
L=["a","b","c"]
L.sort(reverse=True)
print(L)

##Question15
name=input("enter a full name ")
L=name.split()
fL=L[0]
sL=L[1]
print(L[0]) ##prints first name
for n in range(0,len(sL)): ##prints all letters of last name on diff lines
    print(sL[n])
print(sL, fL) ##prints last name before first
newfL=list(fL) ##separated first name into multiple
print(newfL)
newsL=list(sL)
print(newsL)
v=len(newsL)-3
print(v) ##take out later
for n in range(0,v,1):
    #print("n equal to ", n,"Char is", newsL[n])
    newsL.remove(newsL[0])
print(newsL)
for n in range(0,3,1): ##prints first 3 letters of first name
    print(newfL[n])
for n in range(0,3,1):
    print(newsL[n])

##Question16,17,18,19,20,21,22
fruits=["grape","mango","banana","orange","apple"]
fruits.pop()
print(fruits)

for n in range(0,len(fruits)):
    print(fruits[n])

fruits.append("strawberry")
print(fruits)

fruits.pop(2)
print(fruits)

fruits.pop(2)
print(fruits)

fruits.insert(1,"lychee")
print(fruits)

fruits.append("apple")
print(fruits)

fruits.remove("apple")
print(fruits)

print(fruits[0])
n=len(fruits)-1
print(fruits[n])































