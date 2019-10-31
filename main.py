from utils import grovepi,buzzer,temphumi,ecranlcd,thRfid,thTemp,Button
import time

buzzer.init(8) #plug on D8
temphumi.init(2) #plug on D2
#ecranlcd.init(0) #plug on I2C-0
#grovepi.pinMode(buzzer, "OUTPUT")

#buttonValidate = Button(3)
#buttonDelete = Button(4)

#Identif(Thread).start()
thread = thRfid.Identif()
thread.start()

temp = thTemp.Temp()
temp.start()
#ser = serial.Serial('/dev/ttyACM0',115200)

while True:
        
        #showTemp = "temp = %.02f C"%temp
        #ecranlcd.setText(showTemp)

        #id = ser.readLine()
        #print(id)
        time.sleep(2)
        if(thread.userId == 1 ) :
                print(thread.userId)
                
        
        


