##Homework Week 9 Dictionaries
##Question1
fruits={"grape":"" ,"mango":"" ,"orange":"" ,"banana":"" ,"apple":""}
import random
for n in fruits:
    num=random.randint(1,100)
    fruits[n]=num
print(fruits)
name=input("enter a fruit name(apple,banana,orange,mango,grape) ")
print("the price of ", name, "is ",fruits[name])

##Question2
import string
w=input("enter 5 words ")
wl=w.split(" ")
print(wl)
words={}
for n in range(0,5,1):
    k=len(wl[n])
    print(k)
    words[wl[n]]=k
print(words)
    
##Question3
d={"team1":"","team2":""}
import random
n=0
while True:
    score1=random.randint(1,10)
    score2=random.randint(1,10)
    d["team1"]=score1
    d["team2"]=score2
    if d["team1"]==d["team2"]:
        print(d)
        print(n)
        break
    elif d["team1"]!=d["team2"]:
        n=n+1
    else:
        break
        
##Question4
friends={"rania":9,"sahej":8,"namrata":7,"ava":8,"arushi":6}
for n in friends:
    if friends[n]==8:
        print(n,friends[n])

##Question5
D={1:"",2:"",3:"",4:"",5:"", 6:"", 7: "", 8:""}
for n in range(1,9,2):
    c=str(n)
    b=n+1
    d=str(b)
    print(c+d)

##Question6
d={"lonobal":"balloon","ayncd":"candy","naabna":"banana","rotes":"store","lperup":"purple","lapep":"apple","kecpcua":"cupcake","torarc":"carrot","genroa":"orange","perga":"grape",}
for n in d:
    print(n)
    guess=input("guess the word ")
    if guess==d[n]:
        print("correct")
    else:
        print("incorrect, the word was", d[n])









