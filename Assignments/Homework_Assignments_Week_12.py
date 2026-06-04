##Homework Week 12
##Question1
def tpoints(weeks):
    points=weeks*10*2
    print(points)

weeks=int(input("how many weeks have passed "))
tpoints(weeks)

##Question2
def days(month):
    if month=="jan" or month=="mar" or month=="may" or month=="jul" or month=="aug" or month=="oct" or month=="dec":
        daysinmonth=31
        return daysinmonth
    elif month=="feb":
        daysinmonth=28
        return daysinmonth 
    else:
        daysinmonth=30
        return daysinmonth

month=input("what month is it ")
print("there are",days(month),"days in",month)

##Question3
def factors(num):
    L=[]
    for n in range(1,num+1,1):
        if num%n==0:
            L.append(n)
    return L
    
num=int(input("enter a num "))
print("the factors of",num,"are",factors(num))

##Question4
def palindrome_check(string):
    if string==string[::-1]:
        return "the string is a palindrome"
    else:
        return "the string is not a palindrome"

string=input("enter a string ")
print(palindrome_check(string))

##Question5
import string
def count(string):
    for n in string:
        upper=sum(1 for string in string if string.isupper())
    print(upper, "uppercase letters")
    for t in string:
        lower=sum(1 for string in string if string.islower())
    print(lower, "lowercase letters")
    
string=input("enter a string ")
count(string)








