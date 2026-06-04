##Homework Week 13
##Question1&2
string=input("enter a string ")
print(string.title())
print(string.lower())

##Question3
def strings(str1,str2):
    print(str1.upper())
    print(str2.upper())

str1=input("enter a string ")
str2=input("enter another string ")
strings(str1,str2)

##Question4&5
def strings(str1,str2):
    fstr=str1.replace(" ","#")
    fstr2=str2.replace(" ","#")
    print(fstr.swapcase())
    print(fstr2.swapcase())

str1=input("enter a string ")
str2=input("enter another string ")
strings(str1,str2)

##Question6&7&8
friends=["sahej","pranjali","chinmayee","zainab","zoya"]
combo=input("enter a combination of letters ")
print(combo.isupper())
print(combo.islower())
for n in friends:
    if combo in n:
        print(n)

##Question9&10
fruits=["apple","banana","grape","mango","apricot"]
for n in fruits:
    if n.startswith("a")==True:
        print(n)
    if n.endswith("t")==True:
        print(n)

##Question11
string=input("enter string ")
L=[]
for n in string:
    if n not in L:
        L.append(n)
print(L)
    
