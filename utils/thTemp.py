import serial
from threading import Thread
import csv

class Temp(Thread):
	"""Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self):
        Thread.__init__(self)
        self.temp = 0

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        while True :
        	self.temp = 0

        	[temp,humidity] = dht(sensor,blue)  
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                self.temp = temp
        	
		