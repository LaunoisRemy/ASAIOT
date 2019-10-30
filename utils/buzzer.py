# GrovePi + Grove Buzzer

import grovepi
import time
# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
 
def init(pin):
    global buzzer 
    buzzer=pin
    grovepi.pinMode(buzzer,"OUTPUT")
    
def turnOn():
	try:
            # Buzz for 1 second
            grovepi.digitalWrite(buzzer,1)
            print ('start')
	    time.sleep(1)
        except KeyboardInterrupt:
            grovepi.digitalWrite(buzzer,0)
        except IOError:
            print ("Error")            

def turnOff():
        try:
            # Stop buzzing for 1 second and repeat
            grovepi.digitalWrite(buzzer,0)
            print ('stop')
	    time.sleep(1)
        except KeyboardInterrupt:
            grovepi.digitalWrite(buzzer,0)
        except IOError:
            print ("Error")
            
