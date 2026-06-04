##Homework 1

print(int(13))

print(float(13))

print(str("hi"))

print(bool(10>9))
print(bool(10<9))

print(str(1000))

print(float(100))

print(str(13.5))

print(int("900"))

print(float("1000.0000"))

num1=int(input("enter a number "))
num2=int(input("enter another number "))
print("the addition of the two numbers would be", num1+num2)

num1=int(input("enter a number "))
num2=int(input("enter another number "))
print("when you subtract the two numbers the result is", num1-num2)

num1=int(input("enter a number "))
num2=int(input("enter another number "))
print("when you multiply the two numbers the result is", num1*num2)

num1=int(input("enter a number "))
num2=int(input("enter another number "))
print("when you divide the two numbers the result is", num1/num2)

num1=int(input("enter a number "))
num2=int(input("enter another number "))
print("the floor division of the two numbers would be", num1//num2)

print("when 99 is divided by 2, the quotient would be", 99/2, "and the remainder would be" , 99%2)

print("when 3 is raised to the power of 2, the result is", 3**2)

print("good","evening")

print(7*"sanika")

print("b"<"h") ##true
print("Pizza">"Pasta") ##true
print(5+8>13) ##false
print(19!=10+9) ##false
print("57+5"==62) ##false
print((6+2)*4==6+2*4) ##false
print(3*3+2<=4*3+1) ##true

Bob="cat"
A="dog"
B="mouse"
print("checking for 3==4", 3==4) ##false
print("checking for 3!=2", 3!=2) ##true
print("checking for 3==2", 3==2) ##false
print("checking for 'Bob'=='Bob'", "Bob"=="Bob") ##true
print(Bob=="Bob") ##false
####print(Bob="Bob") ##error
print("checking for 10+2==6+6",10+2==6+6) ##true
####print("checking for A=10", A=10) ##error
####print("checking for B=10",B=10) ##error
print("checking for A==B",A==B) ##false
print("checking for A!=B",A!=B) ##true
print("checking for 15%3",15%3) ##0
print("checking for 17%3",17%3) ##2
print("checking for 1122>1121",1122>1121) ##true
print("checking for 1122>1124",1122>1124) ##false
print("checking for 1122>1122",1122>1122) ##false
print("checking for 1122>=1122",1122>=1122) ##true
print("checking for 1122<1122",1122<1122) ##false
print("checking for 1122<=1122",1122<=1122) ##true
print("checking for 1111==1111",1111==1111) ##true
print("checking for '111222'==111222","111222"==111222) ##false
print(type(111222)) ##<class 'int'>
print(type("111222")) ##<class 'str'>
print(len("111222")) ##6
print(len("Vishal")) ##6

##Homework 2
age=3
print(age) ##valid

_age=3
print(_age) ##valid

##$age=3
##print($age) ##notvalid

age1=3
print(age1) ##valid

age_=3
print(age_) ##valid

##2age=3
##print(2age) ##notvalid

a_g_e=3
print(a_g_e) ##valid

agE2=3
print(agE2) ##valid

age=3
print(age) ##valid

##age$=3
##print(age$) #notvalid

##Age=21
##print("My age is", age) ##'age' not defined

name= input("enter your name: ")

print(len("string")) ##to print length of a string

print("sanika thatte")
print("pleasanton")
print("CA")

fav_place=input("what is your favorite place? ")
print(fav_place, "is a great place! I also want to go to ", fav_place)

name=input("what is your name? ")
age=int(input("what is your age? "))
phone_num=int(input("what is your phone number? "))
print("Great to know you, ", name, ". You seem to be very smart for a ", age, "-year-old. Thanks for sharing your phone number, ", phone_num, ". Will stay in touch.")

students=int(input("how many students are there in each grade? "))
grades=int(input("how many grades are going on the trip? "))
max_capacity=int(input("what is the max capacity for each bus? "))
tstudents=students*grades
buses=tstudents//max_capacity
print("A total of", tstudents, " students will be going for the field trip.", buses, "buses will be needed.")

rpeople=17%(3*5)
print(rpeople,"people will need to take the bus")

