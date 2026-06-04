##friends=["sahej","pranjali","chinmayee","zainab","zoya"]
####printing lists
##print(friends)
##
##for n in range(0,len(friends)):
##    print(friends[n])
##
##for n in friends:
##    print(n)
##
####adding new items to a list
##friends.append("ria")
##print(friends)
##
##friends.insert(3,"morgan")
##print(friends)
##
####removing items from a list
##x=friends.pop()
##print(x)
##
##friends.pop(3)
##print(friends)
##
##friends.remove("chinmayee")
##print(friends)
##
####sorting lists
##friends.sort()
##print(friends)
##
####reverse order
##friends.sort(reverse=True)
##print(friends)
##
####reverses whole list
##friends.reverse()
##print(friends)
##
####indexing
##print(friends[1])
##print(friends[2:4])
##
####replacing values
##friends[2]="ava"
##print(friends)
##
####copying lists
##newfriends=friends[::-1] ##one : to copy list ::-1 to reverse
##
####spliting strings
##string="hello, how are you"
##splitstring=string.split()
##print(splitstring)
##
####splitting with ,s, default delimiter is always a space
##string="hi,how,are,you"
##s=string.split(",")
##print(s)
##
##string="hello, how are you"
##cstring=list(string)
##print(cstring)
##
####merging list values
##today=['09', '07', '2019']
##mtoday="-".join(today)
##print(mtoday)
##
##password="sanika123"
##gpassword=[]
##guess=None
##t=0
##while guess!=password:
##    guess=input("guess the password ")
##    if guess==password:
##        print(gpassword)
##        print("access granted")
##    else:
##        gpassword.append(guess)
##        t=t+1
##        if t>2:
##            print("access denied, only three tries allowed")
##            break

##Practice
##L=[]
##import random
##for n in range(1,21,1):
##    num=random.randint(1,100)
##    L.append(num)
##    
##print(min(L))
##print(max(L))

##L=[]
##import random
##for n in range(1,21,1):
##    num=random.randint(1,100)
##    L.append(num)
##
##L.sort(reverse=1)
##print(L[1])

##import random
##L=[]
##for n in range(1,11,1):
##    num=random.randint(1,100)
##    L.append(num)
##L.sort()
##print(L)
##SL=[]
##for n in range(1,len(L),1):
##    if L[n]>20:
##        SL.append(L[n])
##print(SL[0])

##import random
##characters=["mickeymouse","minneymouse","winniethepooh","tiger","daisyduck"]
##for n in range(1,11,1):
##    random.shuffle(characters)
##print(characters[0])
##var=random.choice(characters)
##print(var)
##
##altcharacters=random.sample(characters,3)
##print(altcharacters)

##L=[]
##for n in range(1,1000,1):
##    if n%5==0 and n%15!=0:
##        L.append(n)
##print(L)

##L=[]
##import random
##for n in range(1,11,1):
##    num=random.randint(1,200)
##    L.append(num)
##
##for n in range(0,len(L),):
##    if L[n]%5==0:
##        print(L[n])

##import random
##fruits=["grape","mango","banana","orange","apple"]
##while True:
##    index=random.randint(0,4)
##    if "p" in fruits[index]:
##        print(fruits[index])
##        print("letter 'p' found")
##        break
##    else:
##        print(fruits[index])
##        print("letter 'p' not found")

##animals = ["lion", "tiger", "panda", "bear", "kangaroo", "leopard", "dog", "cat"]
##animals.sort(reverse=1)
##print(animals)

##words=["sanika","pranjali","ava","sahej","zainab","ria","zoya","bella","ceon","amy"]
####for n in range(0,len(words),1):
####    if len(words[n])>5:
####        print(words[n])
##
##lname=""
##b=-1
##for n in range(0,len(words),1):
##    if len(words[n])>len(words[b]):
##        lname=words[n]
##        b=b+1
##    else:
##        lname=words[b]
##print(lname)
    
      




