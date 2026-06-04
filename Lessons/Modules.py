##import time
##print(time.time())
##
##from time import time
##print(time())
##
##from time import *
##print(time())

##import time
##word=input("enter a word and wait for three seconds to check length ")
##time.sleep(3)
##if len(word)> 6:
##    print("the word is greater than 6 letters")
##else:
##    print("the word is less than 6 letters")

##import time
##time.sleep(5)
##refresh=input("would you like to refresh the page? ")
##if refresh=="yes":
##    print("Please wait, your page is loading")
##    time.sleep(2)
##    print("There is high traffic. Please try again later.")
##else:
##    print("Thank you for visiting our website.")

##import random
##integer=random.randint(1,30)
##print(integer)
##if integer%2==0 and integer%3==0:
##    print("the number is a multiple of 2 and 3")
##else:
##    print("the number is not a multiple of 2 and 3")

##import random, time
##num=random.uniform(100,1000)
##print(num)
##time.sleep(3)
##print(round(num,2))

##import random
##num=int(input("enter the number of digits between 1 and 6 "))
##random_num=random.randint(10**(num-1),(10**num)-1)
##print(random_num)

##import math
##sqroot=math.sqrt(169)
##print(sqroot)
##sqroot=math.sqrt(81)
##print(sqroot)
##sqroot=math.sqrt(256)
##print(sqroot)
##sqroot=math.sqrt(64)
##print(sqroot)

##import math
##print(math.pi)

##import math
##pi=math.pi
##distance=2*100*pi
##tdistance= round(distance,3)
##print(tdistance)

##import webbrowser
##webbrowser.open_new_tab('https://www.youtube.com/c/YoungWonks')

##import calendar
##year=int(input("what year were you born? "))
##year1=calendar.calendar(year)
##print(year1)

##import calendar
##month=input("what month were you born in? ")
##year=int(input("what year were you born?"))
##if month=="january":
##    month=1
##if month=="february":
##    month=2
##if month=="march":
##    month=3
##if month=="april":
##    month=4
##if month=="may":
##    month=5
##if month=="june":
##    month=6
##if month=="july":
##    month=7
##if month=="august":
##    month=8
##if month=="september":
##    month=9
##if month=="october":
##    month=10
##if month=="november":
##    month=11
##if month=="december":
##    month=12
##
##month1=calendar.month(year,month)
##print(month1)

##import calendar
##year=1998
##month=2
##day=28
##weekday=calendar.weekday(year,month,day)
##if weekday==0:
##    weekday="Monday"
##if weekday==1:
##    weekday="Tuesday"
##if weekday==2:
##    weekday="Wednesday"
##if weekday==3:
##    weekday="Thursday"
##if weekday==4:
##    weekday="Friday"
##if weekday==5:
##    weekday="Saturday"
##if weekday==6:
##    weekday="Sunday"
##print(weekday)

##import wikipedia
####wikipedia.set_lang(“fr”)
##information = wikipedia.summary("Elephants",sentences=2)
##print(information)

##import datetime
##datetime_object=datetime.datetime.now()
##print(datetime_object)

##date_object=datetime.date.today()
##print(date_object)
