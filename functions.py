import datetime
import requests
import xml.etree.ElementTree as ET
import sys
from time import sleep, strftime
import time
from playsound import playsound

# By default day starts at 9am and ends at 6pm
def getWorkHours():
    while True:
        try:
            startDay = input("From 1 to 23, What time do you start your day?" )
            endDay = input("From 1 to 23, What time do you end your day?" )
            if not startDay:
                startDay = 9
            if not endDay:
                endDay = 23
            if int(startDay) > 23 or int(endDay) > 23:
                raise Exception("Error! This is not a valid hour. Try again")

        # If something else that is not the string
        # version of a number is introduced, the
        # ValueError exception will be called.
        except ValueError:
            # The cycle will go on until validation
            print("Error! This is not a number. Try again.")

        # When successfully converted to an integer,
        # the loop will end.
        else:
            break
    return int(startDay), int(endDay)

# Greet user depending on the time of the day
def greetUser(startDay, endDay):
    if int(time.strftime("%H")) >= endDay:
        print("See you tomorrow!")
        sys.exit()
    if int(time.strftime("%H")) < startDay:
        print("Your day starts at ", startDay, ", go back to bed ;)")
        sys.exit()
    print("It's " + strftime("%H:%M"))
    currentTime = datetime.datetime.now()
    print('-----------------------------------------------------------------------')
    if currentTime.hour < 12 :
        print('Good morning')
    elif currentTime.hour < 18:
        print('Good afternoon')
    elif currentTime.hour < 23:
        print('Good evening')
    else:
        print('Good night')
    sleep(0.5)
    print("Welcome to your desktop notifier!")
    sleep(2)
    print("Let's start our day by a quote")
    sleep(2)

# Print random quote from RSS_FEED
def printQuote():
    RSS_FEED = "http://feeds.feedburner.com/azquotes/quoteoftheday"
    resp = requests.get(RSS_FEED)
    root = ET.fromstring(resp.content)
    quote = root.find('channel/item/description').text
    print(quote)

def printCoffee():
    print("""_________________¶¶¶1___¶¶¶____¶¶¶1_______________
    __________________¶¶¶____¶¶¶____1¶¶1______________
    ___________________¶¶¶____¶¶¶____¶¶¶______________
    ___________________¶¶¶____¶¶¶____¶¶¶______________
    __________________¶¶¶____1¶¶1___1¶¶1______________
    ________________1¶¶¶____¶¶¶____¶¶¶1_______________
    ______________1¶¶¶____¶¶¶1___¶¶¶1_________________
    _____________¶¶¶1___1¶¶1___1¶¶1___________________
    ____________1¶¶1___1¶¶1___1¶¶1____________________
    ____________1¶¶1___1¶¶1___1¶¶¶____________________
    _____________¶¶¶____¶¶¶1___¶¶¶1___________________
    ______________¶¶¶¶___1¶¶¶___1¶¶¶__________________
    _______________1¶¶¶1___¶¶¶1___¶¶¶¶________________
    _________________1¶¶1____¶¶¶____¶¶¶_______________
    ___________________¶¶1____¶¶1____¶¶1______________
    ___________________¶¶¶____¶¶¶____¶¶¶______________
    __________________1¶¶1___1¶¶1____¶¶1______________
    _________________¶¶¶____¶¶¶1___1¶¶1_______________
    ________________11_____111_____11_________________
    __________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
    1¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
    1¶¶¶¶¶¶¶¶¶¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
    1¶¶_______¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
    1¶¶_______¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
    1¶¶_______¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
    1¶¶_______¶¶__1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
    _¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
    _¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________
    __________¶¶___1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1________
    __________1¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________
    ____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11__________
    11_____________________________________________111
    1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1
    __¶¶111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111¶__
    """)

def hourBeep():
    playsound('beep.mp3')