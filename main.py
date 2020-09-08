#Importing modules -------------------
from sense_hat import SenseHat
from time import sleep
import json, urllib3


# Setting up variables -------------------
sh = SenseHat()
http = urllib3.PoolManager()

reallocation = location = weather_humidity = ''
windowclosed = False

Green, Red, Blue, Yellow, Orange, Brown, Black = (0,255,0), (255,0,0), (0,0,255), (255,220,0), (255,130,0), (80,30,0), (0,0,0) 

# Defining functions -------------------
def DrawWind(c, b, delay):
    #All frames of animation, c is chosen color b is background

    frames = ([
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, c, c,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, c, b
    ], [
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, c, c, c, c,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, c, c, c, c, b
    ], [
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, c, c, c, c, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, c, c, c, c, b, b
    ], [
        b, b, b, b, b, b, b, b,
        b, c, b, b, b, b, b, b,
        b, c, b, b, b, b, b, b,
        b, b, c, c, c, c, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        c, b, b, b, b, b, b, b,
        b, c, c, c, c, b, b, b
    ], [
        b, b, c, b, b, b, b, b,
        b, c, b, c, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, c, b, b, b, b, b, b,
        c, b, c, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b
    ], [
        b, b, b, b, b, b, b, b,
        b, b, b, c, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, c, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b
    ])

    #Displaying of frames and clearing at the end
    for i in frames:
        sh.set_pixels(i)
        sleep(delay)

    sh.clear()

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
    weather_humidity = int(weather['liveweer'][0]['lv'])

while True:
    try:
        getlocation()
        getweather()
        sh_humidity = round(sh.get_humidity(), 1)
        if sh_humidity >= 95 or weather_humidity >= 95:
            #raam sluiten
            windowclosed = True
        else:
            #raam openen
            windowclosed = False
        # Print stuff
        print('De luchtvochtigheid in', reallocation, 'is', str(round(weather_humidity)) + "%")
        for i in range(3): # Setup your sleep here. Right now its around 10 secondes
            if windowclosed == True:
                DrawWind(Red)
            elif windowclosed == False:
                DrawWind(Green)
            else:
                DrawWind(Blue)
            sleep(2)

    except urllib3.exceptions.MaxRetryError:
        print("Failed to establish a connection to one of the API's, please check your ethernet connection.")
    except KeyboardInterrupt:
        exit()
    finally:
        sh.clear()
