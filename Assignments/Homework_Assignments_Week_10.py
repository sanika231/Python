##Homework Assignments Week 10- Dictionaries Advanced Questions
##Question8
d={}
for n in range(1,11,1):
    print("only 10 registrations taken")
    name=input("enter ur name ")
    age=int(input("enter ur age "))
    if age>=22 and age<25:
        d[name]=age
    else:
        print("sry try again l8r")
print(d)

##Question9
d={"alice":0,"michelle":0}
for n in range(0,101,1):
    d['alice']=n
    d['michelle']=n
print(d)

##Question10
zoo = { "lion" : 3, "tiger" : 5, "bear" : 6 } 
a = {"hello" : zoo}
c=list(a["hello"].values()) ##to convert to list
print(c[2])

##Question11&12&13
characters = { "lion" : ["Simba", 5], "tiger" : ["Tigress", 2], "panda" : ["Po", 8] } 
a = {"hello" : characters}
c=list(a["hello"].values()) ##to convert to list
print(c[2][0])

b=list(a["hello"].values())
d=list(a["hello"].keys())
for n in range(0,3,1):
    print(d[n],b[n][0])

b=list(a["hello"].values())
d=list(a["hello"].keys())
for n in range(0,3,1):
    print(d[n],b[n])

####Question15&16
d={"sanika":13,"sahej":13,"rania":14,"annika":12,"arushi":11}
b=d["sanika"]
for n in d:
    if d[n]>b:
        b=d[n]
        c=n
print(c,b)

