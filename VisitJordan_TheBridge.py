from urllib.request import urlopen
from bs4 import BeautifulSoup
import winsound
import time

frequency = 3000  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

minutes = int(input("Please enter the checking time(in minutes) : "))

html = 'https://www.gateway2jordan.gov.jo/landplatform/'

while True:
    uRL = urlopen(html).read()
    soup = BeautifulSoup(uRL, features="lxml")
    soupText = str(soup)
    # getting the start index of the string to be checked
    startIndex = soupText.find("GetCrossingpoint(this.value)")
    # startString is the whole page from the start string
    startString = soupText[startIndex:-1]
    # The endIndex is from startIndex untill the index of first "select" (end of the div)
    endIndex = startIndex + startString.find("select")

    # check if the bridge string is added, meaning the King Hussein Bridge is added to the form
    if soupText[startIndex:endIndex].lower().find("bridge") > 0:
        while True:
            time.sleep(0.25)
            winsound.Beep(frequency, duration)
            print("VisitJordan application has changed, King Hussein Bridge has been added!")

    print("Nothing changed")
    if minutes == 1:
        print("Sleeping for: %s minute" % str(minutes))
    else:
        print("Sleeping for: %s minutes" % str(minutes))

    # sleeping time is 60(seconds)* number of minutes specified
    time.sleep(minutes * 60)
