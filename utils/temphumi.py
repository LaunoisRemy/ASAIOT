# GrovePi + Grove Temp/Humi Sensor

from utils.grovepi import *
import math
import time

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# SIG,NC,VCC,GND

# temp_humidity_sensor_type
blue = 0    # The Blue colored sensor.

def init(pin):
    global sensor
    sensor=pin
    pinMode(pin,"INPUT")

# Take measurements of the sensor each X seconds
def readTemp(seconds):
    while True:
        try:
            # The first parameter is the port, the second parameter is the type of sensor.
            [temp,humidity] = dht(sensor,blue)  
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
                time.sleep(seconds)

        except IOError:
            print ("Error")

# Read temperature measurement of the sensor, one time
def showTemp():
    try:
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = dht(sensor,blue)  
        if math.isnan(temp) == False:
            return temp

    except IOError:
        print ("Error")
