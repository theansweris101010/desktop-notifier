import notify2
import time
import requests
import xml.etree.ElementTree as ET
from time import sleep, strftime
import sys
import datetime
import functions
import schedule


inputUser = functions.getWorkHours()

startDay = inputUser[0]
endDay = inputUser[1]
lastMinute = 59
maxMinute = 45
waterreminder = True
stepReminder = True
lunchReminder = True
lunchTime = 12

notify2.init("Desktop Notifier")
notificationstep = notify2.Notification("Stand up", "Sitting kills, moving heals")
notificationwater = notify2.Notification("Water", "Keep calm and drink water")
notificationlunch = notify2.Notification("Lunch time")
notificationend = notify2.Notification("Bye bye! See you tomorrow!")


# Start to print
functions.greetUser(startDay, endDay)
functions.printQuote()
functions.printCoffee()
schedule.every().hour.at(":00").do(functions.hourBeep)
while True:
    schedule.run_pending()
    time.sleep(1)


while int(time.strftime("%H")) < endDay and int(time.strftime("%H")) > startDay:
	if int(time.strftime("%M")) < maxMinute:
		if not stepReminder:
			stepReminder = True
		if not waterreminder and int(time.strftime("%H"))%2 == 0:
			waterreminder = True
		sleep(300)
	else:
		if int(time.strftime("%M")) == lastMinute:
			if stepReminder:
				notificationstep.show()
				stepReminder = False
			if waterreminder:
				notificationwater.show()
				waterreminder = False
	if int(time.strftime("%H")) == lunchTime and 00 <= int(time.strftime("%M")) <= 59 and lunchReminder:
		notificationlunch.show()
		lunchReminder = False