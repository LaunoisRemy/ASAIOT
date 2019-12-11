import time
import grovepi

# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
class Button :
	#button = 0

	def __init__(pin):
	    self.button=pin
		grovepi.pinMode(self.button,"INPUT")
			
	def read():
		return grovepi.digitalRead(self.button)

	def verifRead(): #renvoi true quand le bouton est appuyé
		return grovepi.digitalRead(self.button) == 1


