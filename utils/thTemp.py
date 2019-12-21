import serial
from threading import Thread
import csv
import utils.grovepi as grovepi
import math
import time
import utils.buzzer as buzzer

class Temp(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.temp = 0

    def run(self):
        while True :
            try: 
                self.temp = 0
                #on branche le sensor sur D2
                [temp,humidity] = grovepi.dht(2,0)
                if math.isnan(temp) == False and math.isnan(humidity) == False:
                    self.temp = temp
                    print(self.temp)
                    time.sleep(2)
                    if(self.temp > 24):
                        #met en route le buzzer
                        buzzer.turnOn()
                        time.sleep(0.06) # 0.06sec of buzzer
                        buzzer.turnOff()

            except KeyboardInterrupt:
                digitalWrite(buzzer,0)
                break

            except IOError :
                print ("Error")
                
		
