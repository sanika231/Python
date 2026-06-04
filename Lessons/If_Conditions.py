##answer=input("do you play roblox? ")
##if answer=="yes":
##    print("its a great game!")
##else:
##    print("you should try it!")

##age=int(input("what is ur age?"))
##wait=16-age
##if age>16:
##    print("u are eligible to drive")
##else:
##    print("u must wait", wait, "more years")
##

##num=int(input("give a random number"))
##if num%2==0:
##    print("the number is even")
##else:
##    print("the number is odd")
##    
##age=int(input("what is ur age?"))
##grade=int(input("what grade r u in"))
##if age>=8 and grade>=3:
##    print("you are eligible to play the game")
##else:
##    print("you are not eligible to play the game")

##state=input("what state do you live in?")
##if state=="california" or state=="California" or state=="oregon" or state=="Oregon" or state=="washington" or state=="Washington":
##    print("we suggest you go for a coastal drive")
##else:
##    print("you may be better of skiing")

##price=int(input("what is the price of your item?"))
##discount=(10*price)/100
##discount2=(20*price)/100
##ap=price-discount
##ap2=price-discount2
##if price<=10:
##    print("the discount would be 10%, and the price would be", ap)
##else:
##    print("the discount would be 20%, and the price would be",ap2)
    
##speed=int(input("what is the speed at which a football is kicked?"))
##if speed<=40:
##    print("saved")
##elif speed>40 and speed<=50:
##    print("good try")
##else:
##    print("goal!")
##

##score=int(input("what score did u get?"))
##if 90<=score<=100:
##    print("good job! you got an A!")
##elif 80<=score<=89:
##    print("you got a B!")
##elif 70<=score<=79:
##    print("you got a C.")
##elif 60<=score<=69:
##    print("you got a D..")
##elif 0<=score<=59:
##    print("you got an F")
##else:
##    print("invalid score")
##

##vacay=input("do u have an upcoming vacation?")
##if vacay=="yes":
##    print("cool! what grade r u in?")
##    grade=input()
##    if grade== "12":
##            print("have a great time studying for SATs")
##    elif grade!= "12":
##            print("have an adventurous vacation!!")
##
##else:
##    print("study hard at school!")
##

##year=int(input("enter any year "))
##if year%4!=0:
##    print("it's not a leap year")
##elif year%100!=0:
##    print("it's a leap year")
##elif year%400!=0:
##    print("it's not a leap year")
##else:
##    print("it's a leap year")
    
##num1=int(input("enter any random number "))
##    
##num2=int(input("enter the second number "))
##
##operation=input("enter the operation you would like to perform (+,-,*,/) ")
##if operation=="+":
##    print("the result is", num1+num2)
##elif operation=="-":
##    print("the result is", num1-num2)
##elif operation=="*":
##    print("the result is", num1*num2)
##elif operation=="/":
##    float_or_int=input("do you want the result as integer or float value? (enter integer or float) ")
##    if float_or_int=="integer":
##        print("the result is", num1//num2)
##    elif float_or_int=="float":
##        print("the result is", num1/num2)
##    else:
##        print("error use the given choices")
##else:
##    print("ERROR enter valid operators")


##num1=int(input("enter any random number "))
##
##num2=int(input("enter the second number "))
##
##num3=int(input("enter the third number "))
##
##if num1 > num2:
##    greatest_num=num1
##    if num1 > num3:
##        greatest_num=num1
##    else:
##        greatest_num=num3
##else:
##    greatest_num=num2
##    if num2 > num3:
##        greatest_num=num2
##    else:
##        greatest_num=num3
##
##print("the greatest number of the three numbers is", greatest_num)

##password=input("enter password ")
##if len(password)< 8:
##    print("password is too short, please try again")
##    password=input("enter password ")
##else:
##    print("password successfully created")

string=input("enter a string ")
if "a" in string:
    print("a is present in string")
if "e" in string:
    print("e is present in string")
if "i" in string:
    print("i is present in string")
if "o" in string:
    print("o is present in string")
if "u" in string:
    print("u is present in string")
else:
    print("there are no vowels present")
