# Importing modules -------------------
from sense_hat import SenseHat
from time import sleep
import json
import urllib3

# Setting up variables
sh = SenseHat()
http = urllib3.PoolManager()

location = ''
weather_humidity = ''


def getlocation():
    global location
    # API request for location
    data = http.request('GET', 'extreme-ip-lookup.com/json/')
    ipgeo = json.loads(data.data.decode('UTF-8'))
    location = ipgeo['city']


def getweather():
    global location, weather_humidity
    # API request for weather
    data = http.request('GET', 'weerlive.nl/api/json-data-10min.php?key=907e914202&locatie={}'.format(location))
    weather = json.loads(data.data.decode('UTF-8'))
    # Getting humidity from weerlive
    weather_humidity = weather['liveweer'][0]['lv']


# Main program -------------------
while True:
    getlocation()
    getweather()
    # Print stuff
    print('De luchtvochtigheid in', location, 'is', weather_humidity)
    sleep(10)
