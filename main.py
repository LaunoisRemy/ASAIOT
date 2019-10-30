from utils import buzzer,temphumi,ecranlcd
import time
buzzer.init(8) #plug on D8
temphumi.init(2) #plug on D2
ecranlcd.init(0) #plug on I2C-0
#grovepi.pinMode(buzzer, "OUTPUT")

while True:
	#temphumi.readTemp(5) # read temperature each 2 minutes
	#buzzer.turnOn()
	#time.sleep(2)
	#buzzer.turnOff()	
#OR
    	temp =  temphumi.showTemp()
	print(temp)
	if (temp > 22):
		print(temp)
		buzzer.turnOn()
		
		time.sleep(2) # 10sec of buzzer
		buzzer.turnOff()

	showTemp = "temp = %.02f C"%temp
	ecranlcd.setText(showTemp)
	time.sleep(2)
	


