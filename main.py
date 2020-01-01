from utils import grovepi,buzzer,temphumi,ecranlcd,thRfid,thTemp,thChoix,Button,potentio
import time
import sys
import os
from utils import dweepy

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

choix = thChoix.Choix()
choix.start()
#choix.buttonV = buttonValidate
#choix.buttonD = buttonDelete

#creation de l alerte dweep si la temp depasse le seuil
lock = os.environ.get('DWEET_LOCK')
key = os.environ.get('DWEET_KEY')
condtion_alert="if(dweet.temp > 24) return 'TEST: Greater than 24';"
dweepy.lock('data_temp',lock,key)
dweepy.set_alert('data_temp','alert_frigo@yopmail.com',condition_alert,key)


while True:
        
        #showTemp = "temp = %.02f C"%temp
        #ecranlcd.setText(showTemp)

        #id = ser.readLine()
        #print(id)
        try :
                time.sleep(2)
                if(thread.userId == 1 ) :
                        #print(thread.userId)
                        choix.identif = 1
                        
                 #       print(thread.userId)
                  #      ecranlcd.setText("Faites un choix :")
                   #     valPotentio = potentio.readValueChoix()
                    #    if(valPotentio == 0):
                     #           ecranlcd.setText("Poser un aliment")
                      #          if(buttonValidate.verifRead()):
                       #                 ecranlcd.setText("Choisissez une categorie d'aliment")
                        #                valPot = potentio.readValue()
                         #               if(valPot == 0):
                          #                      ecranlcd.setText("Fruits")
                           #             elif (valPot == 1):
                            #                    ecranlcd.setText("Legumes")
                             #           elif (valPor == 2):
                             #                   ecranlcd.setText("Cuisines")
                              #          elif (valPot == 3):
                               #                 ecranlcd.setText("Boissons")
                                #        elif (valPot == 4):
                                 #               ecranlcd.setText("Viandes")
                                  #      elif (valPot == 5):
                                   #             ecranlcd.setText("Poissons")
                                    #    elif (valPot == 6):
                                     #           ecranlcd.setText("Fromages")
                                      #  else :
                                       #         ecranlcd.setText("Autres")
                                                
                                                
                        #else :
                         #       ecranlcd.setText("Prendre un aliment")


                                
        except KeyboardInterrupt:
                sys.exit(0)

        except IOError :
                print ("Error")
                
        
        


