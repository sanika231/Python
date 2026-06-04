##Homework for Week2

name=input("enter your name ")
if "a" in name:
    print("The name contains at least one 'a'")
else:
    print("The name does not contain the letter 'a'")

name=input("enter your name ")
sport=input("do you like soccer or football? ")
if sport=="soccer":
    prefer=input("do you like Lionel Messi? yes/no ")
    print("Name:", name)
    print("Likes:" , sport)
    print("Likes Lionel Messi:", prefer)
if sport=="football":
    prefer=input("do you like Tom Brady? yes/no ")
    print("Name:", name)
    print("Likes:" , sport)
    print("Likes Tom Brady:", prefer)

name=input("enter your name ")
music=input("do you like music? ")
if music=="yes":
    prefer=input("what instrument do you prefer? ")
    print("Name:", name)
    print("Likes Music:" , music)
    print("Instrument Preference:", prefer)
if music=="no":
    prefer=input("then what do you listen to when traveling in a car? ")
    print("Name:", name)
    print("Likes Music:" , music)
    print("Activity During Traveling:", prefer)

credit_req=int(input("how many credits do you have? "))
gpa=float(input("what is your GPA?"))
if credit_req >= 120 and gpa>2.0:
    print("you are eligible to graduate!")
else:
    print("you are not eligible to graduate.")

color=input("what is the color of the traffic light? ")
if color=="red":
    print("you should stop here")
if color=="yellow":
    print("you should slow down here")
if color=="green":
    print("you can continue to go")

state=input("what state do you live in? ")
if state=="california":
    print("california has great weather!")
elif state=="arizona":
    print("arizona must be hot!")
elif state=="washington":
    print("washington gets a lot of rain!")
else:
    weather=input("how's the weather in your state? ")
    print("Thank you for teaching me that" , state, "has", weather , "weather!")

age=int(input("what is your age? "))
if age>=18:
    print("you are eligible to work")
elif age>=14 and age<=17:
    gpa=float(input("what is your GPA? "))
    if gpa>=3.5:
        print("you are eligible to work")
    else:
        print("you are not eligible to work")
else:
    print("you are not eligible to work")

distance=int(input("what is the distance covered by the cab during this trip? "))
if distance<=6:
    print("the cost of the trip is $50")
elif distance>6 and distance<15:
    cost=10*(distance-6) +  50
    print("the cost of the trip is", cost)
else:
    cost=8*(distance-6) + 50
    print("the cost of the trip is", cost)

size=input("which glass size would you like to order, large or regular? ")
if size=="large":
    discount=3-((15*3)/100)
    print("after discount, the price would be", discount)
if size=="regular":
    discount=2.5-((10*2.5)/100)
    print("after discount, the price would be", discount)

speed=int(input("what is the speed at which the football is kicked? "))
if speed<=30:
    print("saved")
elif speed>30 and speed<=40:
    print("good try")
else:
    print("goal!")

size=float(input("what is the size of your screen? "))
if size<3.5 or size>10:
    print("no protector available for this screen size")
elif size>=5.0 or size<=10:
    print("the amount due is $5")
elif size<5.0 or size>=3.5:
    print("the amount due is $2.5")

age=int(input("what is your age? "))
if age>=0 and age<6:
    print("you are not allowed on this ride")
elif age>=6 and age<18:
    student=input("are you a student? ")
    if student=="yes":
        print("you are allowed on this ride and the price is $9")
    else:
        print("you are allowed on this ride and the price is $10")
elif age>=18 and age<30:
    student=input("are you a student? ")
    if student=="yes":
        print("you are allowed on this ride and the price is $13.5")
    else:
        print("you are allowed on this ride and the price is $15")
elif age>=30 and age<45:
    student=input("are you a student? ")
    if student=="yes":
        print("you are allowed on this ride and the price is $18")
    else:
        print("you are allowed on this ride and the price is $20")
elif age>=45 and age<60:
    student=input("are you a student? ")
    if student=="yes":
        print("you are allowed on this ride and the price is $22.5")
    else:
        print("you are allowed on this ride and the price is $25")
else:
    print("you are not allowed on this ride")

month=int(input("what is your birthday month as a number? "))
if month==1:
    print("January")
if month==2:
    print("February")
if month==3:
    print("March")
if month==4:
    print("April")
if month==5:
    print("May")
if month==6:
    print("June")
if month==7:
    print("July")
if month==8:
    print("August")
if month==9:
    print("September")
if month==10:
    print("October")
if month==11:
    print("November")
if month==12:
    print("December")

hungry=input("are you hungry? (yes/no)")
if hungry=="yes":
    print("take the next right")
    food=input("what do you feel like eating? (italian, mexican, chinese, regular) ")
    if food=="italian" or food=="mexican":
        print("take the next right again")
    elif food=="chinese":
        print("take the next left")
    elif food=="regular":
        print("take the second left")
    else:
        print("continue driving")
elif hungry=="no":
    print("continue driving")
else:
    print("answer invalid")

string=input("enter a string ")
string2=input("enter another string ")
pattern=input("enter what you would like to search for within these strings ")
if " " in string or " " in string2:
    print("space found")
elif pattern in string and pattern in string:
    print("The pattern is found in both strings")
elif string==string2:
    print("the strings are equal")
elif pattern in string:
    print("the pattern is in only one of the strings")
elif pattern in string2:
    print("the pattern is in only one of the strings")
else:
    print("sorry, pattern not found try again later")
    print("")


