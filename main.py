from grovepi import buzzer,temphumi,ecranlcd
import time

buzzer.init(8) #plug on D8
temphumi.init(2) #plug on D2
ecranlcd.init(0) #plug on I2C-0

while True:
	#readTemp(120) # read temperature each 2 minutes
	#OR
	temp = showTemp()

	if (temp < 8):
		buzzer.turnOn()
		time.sleep(10) # 10sec of buzzer
		buzzer.turnOff()

	showTemp = "temp = %.02f C"%temp
	ecranlcd.setText(showTemp)
	time.sleep(30)


