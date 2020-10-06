import notify2
import time
import requests
import xml.etree.ElementTree as ET
from time import sleep
import sys
from functions import getWorkHours

# Init variables...
RSS_FEED = "http://feeds.feedburner.com/azquotes/quoteoftheday"

resp = requests.get(RSS_FEED)
root = ET.fromstring(resp.content)
quote = root.find('channel/item/description').text

inputUser = getWorkHours();

startDay = inputUser[0]
endDay = inputUser[1]
lastMinute = 59
maxMinute = 45
waterreminder = True;
stepReminder = True

notify2.init("Desktop Notifier")
notificationstep = notify2.Notification("Stand up", "Sitting kills, moving heals")
notificationwater = notify2.Notification("Water", "Keep calm and drink water")



# Start to print
if int(time.strftime("%H")) >= endDay:
	print("See you tomorrow!")
	sys.exit()
if int(time.strftime("%H")) < startDay:
	print("Your day starts at ", startDay, ", go back to bed ;)")
	sys.exit()
print("Hi!")
sleep(0.5)
print("Welcome to your desktop notifier!")
sleep(2)
print("Let's start our day by a quote")
sleep(2)
print(quote)
sleep(0.5)
print(".")
sleep(0.5)
print(".")
sleep(0.5)
print(".")
sleep(0.5)
print(".")
sleep(2)

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


