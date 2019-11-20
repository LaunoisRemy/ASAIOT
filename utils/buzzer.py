# GrovePi + Grove Buzzer

from grovepi import *

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
buzzer = 0

def init(pin):
    buzzer=pin
    pinMode(pin,"OUTPUT")
    global buzzer

def turnOn():

    while True:
        try:
            # Buzz for 1 second
            grovepi.digitalWrite(buzzer,1)
            print ('start')

        except KeyboardInterrupt:
            grovepi.digitalWrite(buzzer,0)
            break
        except IOError:
            print ("Error")            

def turnOff():

    while True:
        try:
            # Stop buzzing for 1 second and repeat
            grovepi.digitalWrite(buzzer,0)
            print ('stop')

        except KeyboardInterrupt:
            grovepi.digitalWrite(buzzer,0)
            break
        except IOError:
            print ("Error")
            