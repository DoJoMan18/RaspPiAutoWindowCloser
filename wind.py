from sense_hat import SenseHat
from time import sleep
sh = SenseHat()

Green = (0,255,0)
Red = (255,0,0)
Blue = (0,0,255)
Yellow = (255,220,0)
Orange = (255,130,0)
Brown = (80,30,0)

def DrawWind(c):
    delay = 0.2
    b = (0,0,0)

    frames = ([
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,c,c,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,c,b
    ],[
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,c,c,c,c,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,c,c,c,c,b
    ],[
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,c,c,c,c,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,c,c,c,c,b,b
    ],[
        b,b,b,b,b,b,b,b,
        b,c,b,b,b,b,b,b,
        b,c,b,b,b,b,b,b,
        b,b,c,c,c,c,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        c,b,b,b,b,b,b,b,
        b,c,c,c,c,b,b,b
    ],[
        b,b,c,b,b,b,b,b,
        b,c,b,c,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,c,b,b,b,b,b,b,
        c,b,c,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
    ],[
        b,b,b,b,b,b,b,b,
        b,b,b,c,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,c,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
    ])

    for i in frames:
        sh.set_pixels(i)
        sleep(delay)
    
    sh.clear()

DrawWind(Blue)