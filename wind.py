from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

def DrawWind():
    delay = 0.2

    b = (0,0,0)
    g = (0,255,0)
    r = (255,0,0)

    c = g


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

DrawWind()