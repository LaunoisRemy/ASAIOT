import time
from utils.grovepi import *

# Connect the Grove Button to digital port D3

class Button :
        #button = 0

	def __init__(self,pin):
                self.button=pin
                pinMode(self.button,"INPUT")
                
	def read():
                return digitalRead(self.button)

	def verifRead():
                return digitalRead(self.button) == 1


