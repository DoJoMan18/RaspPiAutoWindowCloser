# Importing modules -------------------
from sense_hat import SenseHat
from time import sleep
import json 
import urllib3
sh = SenseHat()
http = urllib3.PoolManager()

url = 'extreme-ip-lookup.com/json/'
#headers{'x-api-key': 'fa06f1ed94'}
data = http.request('GET', url)
ipgeo = json.loads(data.data.decode('UTF-8'))

location = ipgeo['city']
url = 'weerlive.nl/api/json-data-10min.php?key=907e914202&locatie={}'.format(location)
#headers{'x-api-key': 'fa06f1ed94'}
data = http.request('GET', url)
weer = json.loads(data.data.decode('UTF-8'))



weeronline_lv = weer['liveweer'][0]['lv']
print('De luchtvochtigheid in', location, 'is', weeronline_lv)
