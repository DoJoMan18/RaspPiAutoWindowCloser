# Importing modules -------------------
from sense_hat import SenseHat
from time import sleep
import json
import urllib3

# Setting up variables
sh = SenseHat()
http = urllib3.PoolManager()

reallocation = ''
location = ''
weather_humidity = ''
Green = (0,255,0)
Red = (255,0,0)
Blue = (0,0,255)
Yellow = (255,220,0)
Orange = (255,130,0)
Brown = (80,30,0)

#Function to draw wind animation
def DrawWind(color):
    delay = 0.2

    b = (0,0,0)

    c = color

    frame1 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,c,c,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,c,b
    ]

    frame2 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,c,c,c,c,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,c,c,c,c,b
    ]

    frame3 = [
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,c,c,c,c,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,c,c,c,c,b,b
    ]

    frame3 = [
        b,b,b,b,b,b,b,b,
        b,c,b,b,b,b,b,b,
        b,c,b,b,b,b,b,b,
        b,b,c,c,c,c,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        c,b,b,b,b,b,b,b,
        b,c,c,c,c,b,b,b
    ]

    frame4 = [
        b,b,c,b,b,b,b,b,
        b,c,b,c,b,b,b,b,
        b,c,b,b,b,b,b,b,
        b,b,c,c,b,b,b,b,
        b,c,b,b,b,b,b,b,
        c,b,c,b,b,b,b,b,
        c,b,b,b,b,b,b,b,
        b,c,c,b,b,b,b,b
    ]

    frame5 = [
        b,b,c,b,b,b,b,b,
        b,c,b,c,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,c,b,b,b,b,b,b,
        c,b,c,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
    ]

    frame6 = [
        b,b,b,b,b,b,b,b,
        b,b,b,c,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,c,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
    ]

    sense.clear()
    sleep(delay)
    sense.set_pixels(frame1)
    sleep(delay)
    sense.set_pixels(frame2)
    sleep(delay)
    sense.set_pixels(frame3)
    sleep(delay)
    sense.set_pixels(frame4)
    sleep(delay)
    sense.set_pixels(frame5)
    sleep(delay)
    sense.set_pixels(frame6)
    sleep(delay)
    sense.clear()
    sleep(delay)

def getlocation():
    global location, reallocation
    # API request for location
    data = http.request('GET', 'extreme-ip-lookup.com/json/')
    ipgeo = json.loads(data.data.decode('UTF-8'))
    location = ipgeo['city'].replace(" ", "")
    reallocation = ipgeo['city']


def getweather():
    global location, weather_humidity
    # API request for weather
    data = http.request('GET', 'weerlive.nl/api/json-data-10min.php?key=907e914202&locatie={}'.format(location))
    weather = json.loads(data.data.decode('UTF-8'))
    # Getting humidity from weerlive
    weather_humidity = weather['liveweer'][0]['lv']


# Main program -------------------
while True:
    try: 
        getlocation()
        getweather()
        # Print stuff
        print('De luchtvochtigheid in', reallocation, 'is', weather_humidity)
        sleep(10)
    except urllib3.exceptions.MaxRetryError:
        print("Failed to establish a connection to one of the API's, please check your ethernet connection.")
    except KeyboardInterrupt:
        exit()
