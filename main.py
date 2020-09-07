# Importing modules -------------------
from sense_hat import SenseHat
from time import sleep
import json 
import urllib3

# Setting up variables
sh = SenseHat()
http = urllib3.PoolManager()

# API request for location
data = http.request('GET', 'extreme-ip-lookup.com/json/')
ipgeo = json.loads(data.data.decode('UTF-8'))
location = ipgeo['city']

# API request for weather
data = http.request('GET', 'weerlive.nl/api/json-data-10min.php?key=907e914202&locatie={}'.format(location))
weather = json.loads(data.data.decode('UTF-8'))
weather_humidity = weather['liveweer'][0]['lv']  # Getting humidity from weerlive


# Print stuff
print('De luchtvochtigheid in', location, 'is', weather_humidity)
