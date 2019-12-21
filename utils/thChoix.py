import serial
from threading import Thread,Condition,Lock
import csv
import utils.grovepi as grovepi
import utils.potentio as potentio
import utils.Button as Button
import time
import utils.ecranlcd as ecranlcd
import sys

class Choix(Thread):
    def __init__(self):
            Thread.__init__(self)
            self.identif = 0 #false
            self.pause_cond = Condition()
            self.buttonV = Button.Button(3)
            self.buttonD = Button.Button(4)
            self.paused = False
            self.step = 0

    def run(self):
            ecranlcd.setText("Faites un choix :")
            time.sleep(5)
            while True :
                   with self.pause_cond:
                        while self.paused :
                                self.pause_cond.wait()
                        if(self.identif == 1):
                                       
                                self.choix()
                        #print(self.identif)
                        
    def choix(self):
         print(self.step)
         if(self.step == 0) : self.debut()
         elif(self.step == 1) : self.categoriesD()
         #if(self.step == 2) : self.categoriesP()
         #if(self.step == 3) : self.depot()
         #if(self.step == 4) : self.prise()
         else : self.fin()

    def debut(self):
         valPotentio = potentio.readValueChoix()
         print(valPotentio)
         if(valPotentio == 0):
                  ecranlcd.setText("Poser un aliment")
                  time.sleep(3)
                  if(self.buttonV.verifRead(self.buttonV.button)):
                        self.step = 1
                  #print(self.buttonV.verifRead())
                                        
         else :
                  ecranlcd.setText("Prendre un aliment")
                  time.sleep(3)
                  if(self.buttonV.verifRead(self.buttonV.button)):
                        self.step = 2


    def categoriesD(self):
         time.sleep(1)
         valPotentio = potentio.readValue()
         #print(valPotentio)
         if(valPotentio == 0):
                 ecranlcd.setText("Legumes")
                 time.sleep(2)
         elif(valPotentio == 1):
                 ecranlcd.setText("Fruits")
                 time.sleep(2)
         elif(valPotentio == 2):
                 ecranlcd.setText("Viandes")
                 time.sleep(2)
         elif(valPotentio == 3):
                 ecranlcd.setText("Poissons")
                 time.sleep(2)
         elif(valPotentio == 4):
                 ecranlcd.setText("Cuisines")
                 time.sleep(2)
         elif(valPotentio == 5):
                 ecranlcd.setText("Laitages")
                 time.sleep(2)
         elif(valPotentio == 6):
                 ecranlcd.setText("Boissons")
                 time.sleep(2)
         else:
                 ecranlcd.setText("Autres")
                 time.sleep(2)

    def fin(self):
         ecranlcd.setText("Merci au revoir")
         ecranlcd.setText("")
         
    def pause(self):
         self.paused = True
         self.pause_cond.acquire()
                              

    def resume(self):
         self.paused = False
         self.pause_cond.notify()
         self.pause_cond.release()
