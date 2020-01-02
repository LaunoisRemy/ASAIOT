from utils import grovepi,buzzer,temphumi,ecranlcd,thRfid,thTemp,thChoix,Button,potentio
import time
import sys
import os
import dweepy 


buzzer.init(8) #plug on D8
temphumi.init(2) #plug on D2
ecranlcd.init(1) #plug on I2C-1
potentio.init(1) #plug on A1

#buttonValidate = Button.Button(3)
#buttonDelete = Button.Button(4)

thread = thRfid.Identif()
thread.start()

temp = thTemp.Temp()
temp.start()

#choix.buttonV = buttonValidate
#choix.buttonD = buttonDelete

#creation de l alerte dweep si la temp depasse le seuil
lock = os.environ.get('DWEET_LOCK')
key = os.environ.get('DWEET_LOCK')
condition_alert="if(dweet.temp > 24) return 'TEST: Greater than 24';"
#dweepy.lock('data_temp',lock,key)
#dweepy.set_alert('data_temp','alert_frigo@yopmail.com',condition_alert,key)

"""
while True:
       
        #showTemp = "temp = %.02f C"%temp
        #ecranlcd.setText(showTemp)

        #id = ser.readLine()
        #print(id)
        try :
               
                time.sleep(2)
                if(thread.userId == 1 ) :
                        choix.name = thread.name
                        choix.identif = 1
                              
        except KeyboardInterrupt:
                sys.exit(0)

        except IOError :
                print ("Error")
                
        
        """


