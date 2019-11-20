# GrovePi + Grove Ultrasonic Ranger

from grovepi import *

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

ultrasonic_ranger=0

def init(pin):
    ultrasonic_ranger=pin
    pinMode(pin,"OUTPUT")
    global ultrasonic_ranger

def surveille(distance):

    while True :
        try:
           print(ultrasonicRead(ultrasonic_ranger))
            if(ultrasonicRead(ultrasonic_ranger)<=distance):
                 return True
        except TypeError:
            print "Error"
        except IOError:
            print "Error"
