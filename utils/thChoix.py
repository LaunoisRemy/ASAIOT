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
            self.choice = False #permet de savoir si l'utilisateur a choisi de poser (True) ou de prendre (False)
            self.categorie = 0 #numero de categorie
            self.id = 0 #id de l'aliment
            self.qte = 0 #quantite choisie par l'utilisateur

    def run(self):
            ecranlcd.setText("Faites un choix :")
            ecranlcd.setRGB(0,0,255)
            time.sleep(5)
            while True :
                   with self.pause_cond:
                        while self.paused :
                                self.pause_cond.wait()
                        if(self.identif == 1):
                                       
                                self.choix()
                        #print(self.identif)
                        
    def choix(self):
         if(self.step == 0) : self.debut()
         elif(self.step == 1) : self.categories()
         elif(self.step == 2) : self.depot()
         elif(self.step == 3) : self.prise()
         elif(self.step == 4) : self.quantite()
         else : self.fin()

    def debut(self):
         valPotentio = potentio.readValueChoix()
         if(valPotentio == 0):
                  ecranlcd.setText("Poser un aliment")
                  time.sleep(3)
                  if(self.buttonV.verifRead(self.buttonV.button)):
                        self.step = 1
                        self.choice = False
                  #print(self.buttonV.verifRead())
                                        
         else :
                  ecranlcd.setText("Prendre un aliment")
                  time.sleep(3)
                  if(self.buttonV.verifRead(self.buttonV.button)):
                        self.step = 1
                        self.choice = True


    def categories(self):
         time.sleep(1)
         valPotentio = potentio.readValue()
         #print(valPotentio)
         if(valPotentio == 0):
                ecranlcd.setText("Legumes")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        if(self.choice): #prendre un aliment
                            self.step = 3
                            ecranlcd.setText("Choisissez parmi la liste : ")
                            time.sleep(5)
                        else : #poser
                            self.step = 2

                        self.categorie = 0

                if(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        self.step = 0

         elif(valPotentio == 1):
                ecranlcd.setText("Fruits")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        if(self.choice): #prendre un aliment
                            self.step = 3
                            ecranlcd.setText("Choisissez parmi la liste : ")
                            time.sleep(5)
                        else : #poser
                            self.step = 2

                        self.categorie = 1

                if(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        self.step = 0

         elif(valPotentio == 2):
                ecranlcd.setText("Viandes")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        if(self.choice): #prendre un aliment
                            self.step = 3
                            ecranlcd.setText("Choisissez parmi la liste : ")
                            time.sleep(5)
                        else : #poser
                            self.step = 2

                        self.categorie = 2

                if(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        self.step = 0

         elif(valPotentio == 3):
                ecranlcd.setText("Poissons")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        if(self.choice): #prendre un aliment
                            self.step = 3
                            ecranlcd.setText("Choisissez parmi la liste : ")
                            time.sleep(5)
                        else : #poser
                            self.step = 2

                        self.categorie = 3

                if(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        self.step = 0

         elif(valPotentio == 4):
                ecranlcd.setText("Cuisines")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        if(self.choice): #prendre un aliment
                            self.step = 3
                            ecranlcd.setText("Choisissez parmi la liste : ")
                            time.sleep(5)
                        else : #poser
                            self.step = 2

                        self.categorie = 4

                if(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        self.step = 0

         elif(valPotentio == 5):
                ecranlcd.setText("Laitages")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        if(self.choice): #prendre un aliment
                            self.step = 3
                            ecranlcd.setText("Choisissez parmi la liste : ")
                            time.sleep(5)
                        else : #poser
                            self.step = 2 

                        self.categorie = 5

                if(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        self.step = 0

         elif(valPotentio == 6):
                ecranlcd.setText("Boissons")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        if(self.choice): #prendre un aliment
                            self.step = 3
                            ecranlcd.setText("Choisissez parmi la liste : ")
                            time.sleep(5)
                        else : #poser
                            self.step = 2

                        self.categorie = 6

                if(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        self.step = 0

         else:
                ecranlcd.setText("Autres")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        if(self.choice): #prendre un aliment
                            self.step = 3
                            ecranlcd.setText("Choisissez parmi la liste : ")
                            time.sleep(5)
                        else : #poser
                            self.step = 2

                        self.categorie = 7

                if(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        self.step = 0

    def depot(self):
        ecranlcd.setText("Entrez le nom de l'aliment a deposer : ")
        #input de l'utilisateur 
        nom = input()
        ecranlcd.setText("Entrez la date de perremption : ")
        date = input() #peut etre vide 
        ecranlcd.setText("Entrez la quantite : ")
        quantite = input()
        #mettre les infos dans le csv


    def prise(self):
        categorie = self.convertCat(self.categorie)
        liste = self.listAl(categorie)
        taille = len(liste)
        valPotentio = potentio.readFromNb(taille)
        for i in range(1,taille+1):
            #for r in liste:
                if liste[i-1][2] != '0':
                    if(valPotentio == taille - (i)):
                        ecranlcd.setText(""+liste[i-1][1]+"")#nom des produits
                        time.sleep(2)
                        
                        if(self.buttonV.verifRead(self.buttonV.button)):
                            self.id = liste[i-1][0]
                            ecranlcd.setText("Choisissez une quantite : ")
                            time.sleep(2)
                            self.step = 4 #choix quantite

                        if(self.buttonD.verifRead(self.buttonD.button)):
                            ecranlcd.setText("Vous avez annule")
                            time.sleep(5)
                            self.step = 0
                        
                    elif(valPotentio == taille):
                        ecranlcd.setText(""+liste[i-1][1]+"")#nom des produits
                        time.sleep(2)

                        if(self.buttonV.verifRead(self.buttonV.button)):
                            self.id = liste[i-1][0]
                            ecranlcd.setText("Choisissez une quantite : ")
                            time.sleep(2)
                            self.step = 4 #choix quantite

                        if(self.buttonD.verifRead(self.buttonD.button)):
                            ecranlcd.setText("Vous avez annule")
                            time.sleep(5)
                            self.step = 0
            


    def quantite(self):
        liste = self.listeQte(self.id)
        quantite = int(liste[0][2])
        valPotentio = potentio.readFromNb(quantite)
        #print(quantite)
        for i in range(1,quantite+1) :
            if(valPotentio == quantite - (i)):
                stri = str(i)
                ecranlcd.setText(""+stri+"")
                time.sleep(3)
                if(self.buttonV.verifRead(self.buttonV.button)):
                    self.qte = i
                    self.majStock()
                    ecranlcd.setText("Retirez le(s) aliment(s) du frigo")
                    time.sleep(5)
                    self.step = 6 #fin

                if(self.buttonD.verifRead(self.buttonD.button)):
                    ecranlcd.setText("Vous avez annule")
                    time.sleep(5)
                    self.step = 0
                    
            elif(valPotentio == quantite):
                stri = str(quantite)
                ecranlcd.setText(""+stri+"")
                time.sleep(3)
                if(self.buttonV.verifRead(self.buttonV.button)):
                    self.qte = i
                    self.majStock()
                    ecranlcd.setText("Retirez le(s) aliment(s) du frigo")
                    time.sleep(5)
                    self.step = 6 #fin

                if(self.buttonD.verifRead(self.buttonD.button)):
                    ecranlcd.setText("Vous avez annule")
                    time.sleep(5)
                    self.step = 0
                    
        
    def fin(self):
         ecranlcd.setText("Merci au revoir")
         time.sleep(2)
         ecranlcd.setText("")

    def listeQte(self,id):
        liste=[]
        with  open('./utils/stock.csv','r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if id == row[0] :
                    liste.append(row)
            f.close()           
        return liste

    def listAl(self,categorie):
        liste=[]
        with  open('./utils/stock.csv','r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if categorie in row :
                    liste.append(row)
            f.close()
        return liste

    def convertCat(self,cat):
        if self.categorie == 0 :
            return 'LEGUMES'
        elif self.categorie == 1:
            return 'FRUITS'
        elif self.categorie == 2:
            return 'VIANDES'
        elif self.categorie == 3 :
            return 'POISSONS'
        elif self.categorie == 4:
            return 'CUISINES'
        elif self.categorie == 5:
            return 'BOISSONS'
        elif self.categorie == 6 :
            return 'LAITAGES'
        else :
            return 'AUTRES'

                                 
    def majStock(self):
        text = open("./utils/stock.csv", "r")
        txt=csv.reader(text)

        liste=[]
            
        for ligne in txt :
            if(ligne[0]==self.id):
                nv_qte=int(ligne[2]) - int(self.qte) #quantite apres soustraction de la quantite choisie par l utilisateur
		nv_qte=str(nv_qte)
                ligne[2]=ligne[2].replace(ligne[2],nv_qte)
                
            liste.append(ligne)

        out=open("./utils/stock.csv", "w")
        wr=csv.writer(out)  
        wr.writerows(liste)
        out.close()
        text.close()
        print("Mise a jour du stock")


        
    def pause(self):
         self.paused = True
         self.pause_cond.acquire()
                              

    def resume(self):
         self.paused = False
         self.pause_cond.notify()
         self.pause_cond.release()
