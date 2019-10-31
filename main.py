from utils import grovepi,buzzer,temphumi,ecranlcd,thRfid,thTemp,Button,potentio
import time

buzzer.init(8) #plug on D8
temphumi.init(2) #plug on D2
ecranlcd.init(1) #plug on I2C-1

buttonValidate = Button.Button(3)
buttonDelete = Button.Button(4)

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
                ecranlcd.setText("Choisissez un choix :")
                valPotentio = potentio.readValueChoix()
                if(valPotentio == 0):
                        ecranlcd.setText("Poser un aliment")
                        if(buttonValidate.verifRead()):
                                ecranlcd.setText("Choisissez une catégorie d'aliment")
                                valPot = potentio.readValue()
                                if(valPot == 0):
                                        ecranlcd.setText("Fruits")
                                elif (valPot == 1):
                                        ecranlcd.setText("Légumes")
                                elif (valPor == 2):
                                        ecranlcd.setText("Cuisinés")
                                elif (valPot == 3):
                                        ecranlcd.setText("Boissons")
                                elif (valPot == 4):
                                        ecranlcd.setText("Viandes")
                                elif (valPot == 5):
                                        ecranlcd.setText("Poissons")
                                elif (valPot == 6):
                                        ecranlcd.setText("Fromages")
                                else :
                                        ecranlcd.setText("Autres")


                else :
                        ecranlcd.setText("Prendre un aliment")

                
                
                
        
        


