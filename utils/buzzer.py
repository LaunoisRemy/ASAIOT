# GrovePi + Grove Buzzer

from utils.grovepi import *
import time
# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND

def init(pin):
    global buzzer 
    buzzer=pin
    pinMode(buzzer,"OUTPUT")
    
def turnOn():
    try:
        # Buzz for 1 second
        digitalWrite(buzzer,1)
        print ('start')
        time.sleep(1)
    except KeyboardInterrupt:
        digitalWrite(buzzer,0)
    except IOError:
        print ("Error")            

def turnOff():
    try:
        # Stop buzzing for 1 second and repeat
        digitalWrite(buzzer,0)
        print ('stop')
        time.sleep(1)
    except KeyboardInterrupt:
        digitalWrite(buzzer,0)
    except IOError:
        print ("Error")
    
