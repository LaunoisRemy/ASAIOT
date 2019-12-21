import time
import utils.grovepi as grovepi

# Connect the Grove Button to digital port D3

class Button :
        #button = 0

	def __init__(self,pin):
                self.button=pin
                grovepi.pinMode(self.button,"INPUT")
                
	def read(self):
                return grovepi.digitalRead(self.button)

	def verifRead(self,pin):
                return grovepi.digitalRead(pin) == 1


