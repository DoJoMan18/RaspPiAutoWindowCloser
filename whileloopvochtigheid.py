# import modulus
from sense_hat import SenseHat
from time import sleep

# Setting up variables
sh = SenseHat()

# delay between calls
delay = 5
try:
    while True:
        humi = round(sh.get_humidity(), 1)
        print("Vochtigheid:", humi)
        sleep(delay)
except KeyboardInterrupt:
    pass
print("Einde script")