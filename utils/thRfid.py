import serial
from threading import Thread
import csv
import thChoix
import utils.ecranlcd as ecranlcd
import utils.grovepi as grovepi
import time 
ser = serial.Serial('/dev/ttyACM0',115200)

class Identif(Thread):
    def __init__(self):
            Thread.__init__(self)
            self.userId = 0
            self.name=""
    def interraction(self):
        msg = "Bonjour " + self.name
        ecranlcd.setText(msg)
        time.sleep(3)
        ecranlcd.setText("Faites un choix :")
        time.sleep(3)
        
        nonFini = True
        choix = thChoix.Choix()
        test = choix.debut()
        print(test)

    def run(self):
            while True :
                
                    ecranlcd.setText("Connectez vous")
                    ecranlcd.setRGB(0,0,255)
                    time.sleep(5)
                    lecture_id = ser.readline()
                    #print(lecture_id)
                    
                    
                    with open('/home/pi/ASAIOT/utils/user.csv','r') as file :
                        lignes=file.read().splitlines()
                        dataColum=lignes[0].split(',')
        
                        lignes.remove(lignes[0])
                        liste_perso=[]
                        for l in lignes :
                            dataLigne=l.split(',')
                            i=0
                            personne={}
                            for c in dataColum:
                                personne[c] = dataLigne[i]
                                i+=1
                            liste_perso.append(personne)
                           # print(personnes)
                    file.closed
                    
                    for p in liste_perso :
                        if(p['userId'] in lecture_id) :
                            self.name = p['nom']
                            self.userId = 1
                    if self.userId == 1 :
                        self.interraction()
                        self.userId = 0
                            
