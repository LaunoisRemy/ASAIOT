import serial
from threading import Thread,Condition,Lock
import csv
import utils.grovepi as grovepi
import utils.potentio as potentio
import utils.Button as Button
import time
import utils.ecranlcd as ecranlcd
import sys

class Choix():
    def __init__(self):
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
            self.stepdate = 1 #etape de la conception de la date de peremption (1 : jour, 2 : date, 3: annee)
            self.j = "1" #jour par defaut
            self.m = "01" #mois par defaut
            self.a = "2020" #annee par defaut

    # def run(self):
    #         ecranlcd.setText("Connectez vous")
    #         ecranlcd.setRGB(0,0,255)
    #         time.sleep(5)
    #         while True :
    #                with self.pause_cond:
    #                     while self.paused :
    #                             self.pause_cond.wait()
    #                     if(self.identif == 1):
    #                             self.choix()
                        
    # def choix(self):
    #      if(self.step == 0) : self.debut()
    #      elif(self.step == 1) : self.categories()
    #      elif(self.step == 2) : self.depot()
    #      elif(self.step == 3) : self.prise()
    #      elif(self.step == 4) : self.quantite()
    #      elif(self.step == 5) : self.quantiteDepot()
    #      elif(self.step == 6) : self.choixDate()
    #      elif(self.step == 7) : self.datePeremption()
    #      else : self.fin()

    #Choix de l utilisateur : prise ou depot d aliments
    def debut(self):
        self.step = 0
        while self.step == 0 :
            valPotentio = potentio.readValueChoix()
            if(valPotentio == 0):
                ecranlcd.setText("Poser un aliment")
                time.sleep(3)
                if(self.buttonV.verifRead(self.buttonV.button)):
                    self.choice = False
                    self.categories()
            else :
                ecranlcd.setText("Prendre un aliment")
                time.sleep(3)
                if(self.buttonV.verifRead(self.buttonV.button)):
                    self.choice = True
                    self.categories()

    #Afficher les differentes categories 
    def categories(self):
        choix = False
        while choix == False :
            time.sleep(1)
            valPotentio = potentio.readValue()
            if(valPotentio == 0):
                ecranlcd.setText("Legumes")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                    ecranlcd.setText("Choisissez parmi la liste : ")
                    time.sleep(5)
                    if(self.choice): #prendre un aliment
                        choix = True
                        self.prise()
                    else : #poser
                        choix = True
                        self.depot()

                    self.categorie = 0
                elif(self.buttonD.verifRead(self.buttonD.button)):
                    ecranlcd.setText("Vous avez annule")
                    time.sleep(5)
                    choix = True
                    self.debut()
                    
            elif(valPotentio == 1):
                ecranlcd.setText("Fruits")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        self.categorie = 1
                        ecranlcd.setText("Choisissez parmi la liste : ")
                        time.sleep(5)
                        if(self.choice): #prendre un aliment
                            choix = True
                            self.prise()
                        else : #poser
                            choix = True
                            self.depot()

                elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()

            elif(valPotentio == 2):
                ecranlcd.setText("Viandes")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        self.categorie = 2
                        ecranlcd.setText("Choisissez parmi la liste : ")
                        time.sleep(5)
                        if(self.choice): #prendre un aliment
                            choix = True
                            self.prise()
                        else : #poser
                            choix = True
                            self.depot()

                elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()

            elif(valPotentio == 3):
                ecranlcd.setText("Poissons")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        self.categorie = 3
                        ecranlcd.setText("Choisissez parmi la liste : ")
                        time.sleep(5)
                        if(self.choice): #prendre un aliment
                            choix = True
                            self.prise()
                        else : #poser
                            choix = True
                            self.depot()

                elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()

            elif(valPotentio == 4):
                ecranlcd.setText("Cuisines")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        self.categorie = 4
                        ecranlcd.setText("Choisissez parmi la liste : ")
                        time.sleep(5)
                        if(self.choice): #prendre un aliment
                            choix = True
                            self.prise()
                        else : #poser
                            choix = True
                            self.depot()

                elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()

            elif(valPotentio == 5):
                ecranlcd.setText("Laitages")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        self.categorie = 5
                        ecranlcd.setText("Choisissez parmi la liste : ")
                        time.sleep(5)
                        if(self.choice): #prendre un aliment
                            choix = True
                            self.prise()
                        else : #poser
                            choix = True
                            self.depot()

                elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()

            elif(valPotentio == 6):
                ecranlcd.setText("Boissons")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        self.categorie = 6
                        ecranlcd.setText("Choisissez parmi la liste : ")
                        time.sleep(5)
                        if(self.choice): #prendre un aliment
                            choix = True
                            self.prise()
                        else : #poser
                            choix = True
                            self.depot()

                elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()

            else:
                ecranlcd.setText("Autres")
                time.sleep(2)
                if(self.buttonV.verifRead(self.buttonV.button)):
                        self.categorie = 7
                        ecranlcd.setText("Choisissez parmi la liste : ")
                        time.sleep(5)
                        if(self.choice): #prendre un aliment
                            choix = True
                            self.prise()
                        else : #poser
                            choix = True
                            self.depot()

                elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()
            
    #Affichage des noms des produits pour la categorie choisie
    def depot(self):
        categorie = self.convertCat(self.categorie)
        liste = self.listAl(categorie)
        taille = len(liste)
        choix = False
        while choix == False :
            valPotentio = potentio.readFromNb(taille)
            for i in range(1,taille+1):
                    if(valPotentio == taille - (i)):
                        ecranlcd.setText(""+liste[i-1][1]+"")#nom des produits
                        time.sleep(2)
                            
                        if(self.buttonV.verifRead(self.buttonV.button)):
                            self.id = liste[i-1][0]
                            ecranlcd.setText("Choisissez une quantite : ")
                            time.sleep(2)
                            choix = True
                            self.quantiteDepot() #choix quantite

                        elif(self.buttonD.verifRead(self.buttonD.button)):
                            ecranlcd.setText("Vous avez annule")
                            time.sleep(5)
                            choix = True
                            self.debut()
                            
                    elif(valPotentio == taille):
                        ecranlcd.setText(""+liste[i-1][1]+"")#nom des produits
                        time.sleep(2)

                        if(self.buttonV.verifRead(self.buttonV.button)):
                            self.id = liste[i-1][0]
                            ecranlcd.setText("Choisissez une quantite : ")
                            time.sleep(2)
                            choix = True
                            self.quantiteDepot() #choix quantite

                        elif(self.buttonD.verifRead(self.buttonD.button)):
                            ecranlcd.setText("Vous avez annule")
                            time.sleep(5)
                            choix = True
                            self.debut()

    #Choix de la quantite a deposer
    def quantiteDepot(self):
        liste = self.listeQte(self.id)
        quantite = 10 #on met une quantite max a 10
        choix = False
        while choix == False :
            valPotentio = potentio.readFromNb(quantite)
            for i in range(1,quantite+1) :
                if(valPotentio == quantite - (i)):
                    stri = str(i)
                    ecranlcd.setText(""+stri+"")
                    time.sleep(3)
                    if(self.buttonV.verifRead(self.buttonV.button)):
                        self.qte = i
                        self.majStock(True)
                        ecranlcd.setText("Date de peremption ?")
                        time.sleep(5)
                        choix = True
                        self.choixDate() #choix date de peremption

                    elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()
                        
                elif(valPotentio == quantite):
                    stri = str(quantite)
                    ecranlcd.setText(""+stri+"")
                    time.sleep(3)
                    if(self.buttonV.verifRead(self.buttonV.button)):
                        self.qte = i
                        self.majStock(True)
                        ecranlcd.setText("Date de peremption ?")
                        time.sleep(5)
                        choix = True
                        self.choixDate() #choix date de peremption

                    elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()

    #Demande a l utilisateur si le(s) aliment(s) possede un edate de peremption
    def choixDate(self):
        choix = False
        while choix == False :
            valPotentio = potentio.readFromNb(2)
            if(valPotentio == 0):
                ecranlcd.setText("Oui")
                time.sleep(3)
                if(self.buttonV.verifRead(self.buttonV.button)):
                    ecranlcd.setText("Entrez la date")
                    time.sleep(5)
                    choix = True
                    self.datePeremption() #date de peremption

                elif(self.buttonD.verifRead(self.buttonD.button)):
                    ecranlcd.setText("Vous avez annule")
                    time.sleep(5)
                    choix = True
                    self.debut()
            else:
                ecranlcd.setText("Non")
                time.sleep(3)
                if(self.buttonV.verifRead(self.buttonV.button)):
                    ecranlcd.setText("Vous pouvez deposer le(s) aliment(s)")
                    time.sleep(5)
                    choix = True
                    self.fin() #fin

                elif(self.buttonD.verifRead(self.buttonD.button)):
                    ecranlcd.setText("Vous avez annule")
                    time.sleep(5)
                    choix = True
                    self.debut()

    #Choix de la date de peremption
    def datePeremption(self):
        jour = 31
        mois = 12
        annee = 2035
        choix = False
        while choix == False:
            if(self.stepdate == 1):
                valPotentio = potentio.readFromNb(jour)
                for i in range(1,jour+1):
                    if(valPotentio == jour - (i)):
                        stri = str(i)
                        ecranlcd.setText(""+stri+"/"+self.m+"/"+self.a+"")
                        time.sleep(3)
                        if(self.buttonV.verifRead(self.buttonV.button)):
                            self.j = str(i)
                            ecranlcd.setText("Choisissez le mois :")
                            time.sleep(5)
                            self.stepdate = 2 #mois

                        elif(self.buttonD.verifRead(self.buttonD.button)):
                            ecranlcd.setText("Vous avez annule")
                            time.sleep(5)
                            choix = True
                            self.debut()
                            
                    elif(valPotentio == jour):
                        stri = str(jour)
                        ecranlcd.setText(""+stri+"/"+self.m+"/"+self.a+"")
                        time.sleep(3)
                        if(self.buttonV.verifRead(self.buttonV.button)):
                            self.j = str(jour)
                            ecranlcd.setText("Choisissez le mois :")
                            time.sleep(5)
                            self.stepdate = 2 #mois

                        elif(self.buttonD.verifRead(self.buttonD.button)):
                            ecranlcd.setText("Vous avez annule")
                            time.sleep(5)
                            choix = True
                            self.debut()


            elif(self.stepdate == 2):
                valPotentio = potentio.readFromNb(mois)
                for i in range(1,mois+1):
                    if(valPotentio == mois - (i)):
                        stri = str(i)
                        ecranlcd.setText(""+self.j+"/"+stri+"/"+self.a+"")
                        time.sleep(3)
                        if(self.buttonV.verifRead(self.buttonV.button)):
                            self.m = str(i)
                            ecranlcd.setText("Choisissez l annee :")
                            time.sleep(5)
                            self.stepdate = 3 #annees

                        elif(self.buttonD.verifRead(self.buttonD.button)):
                            ecranlcd.setText("Vous avez annule, choisissez un jour")
                            time.sleep(5)
                            self.stepdate = 1 #on reviens sur les jours
                            
                    elif(valPotentio == mois):
                        stri = str(mois)
                        ecranlcd.setText(""+self.j+"/"+stri+"/"+self.a+"")
                        time.sleep(3)
                        if(self.buttonV.verifRead(self.buttonV.button)):
                            self.m = str(mois)
                            ecranlcd.setText("Choisissez l annee :")
                            time.sleep(5)
                            self.stepdate = 3 #annees

                        elif(self.buttonD.verifRead(self.buttonD.button)):
                            ecranlcd.setText("Vous avez annule, choisissez un jour")
                            time.sleep(5)
                            self.stepdate = 1 #on reviens sur les jours

            if(self.stepdate == 3):
                taille = annee - 2020
                valPotentio = potentio.readFromNb(taille)
                for i in range(2020,annee+1):
                    if(valPotentio == annee - (i)):
                        stri = str(i)
                        ecranlcd.setText(""+self.j+"/"+self.m+"/"+stri+"")
                        time.sleep(3)
                        if(self.buttonV.verifRead(self.buttonV.button)):
                            self.a = str(i)
                            self.majDate()
                            ecranlcd.setText("Vous pouvez deposer le(s) aliment(s)")
                            time.sleep(5)
                            choix = True
                            self.fin() #fin

                        elif(self.buttonD.verifRead(self.buttonD.button)):
                            ecranlcd.setText("Vous avez annule, choisssez un mois")
                            time.sleep(5)
                            self.stepdate = 2 #on reviens sur les mois
                            
                    elif(valPotentio == annee):
                        stri = str(annee)
                        ecranlcd.setText(""+self.j+"/"+self.m+"/"+stri+"")
                        time.sleep(3)
                        if(self.buttonV.verifRead(self.buttonV.button)):
                            self.a = str(annee)
                            self.majDate()
                            ecranlcd.setText("Vous pouvez deposer le(s) aliment(s)")
                            time.sleep(5)
                            choix = True
                            self.fin() #fin

                        elif(self.buttonD.verifRead(self.buttonD.button)):
                            ecranlcd.setText("Vous avez annule, choisssez un mois")
                            time.sleep(5)
                            self.stepdate = 2 #on reviens sur les mois


    #Affichage des aliments disponibles dans la categorie choisie
    def prise(self):
        categorie = self.convertCat(self.categorie)
        liste = self.listAl(categorie)
        taille = len(liste)

        choix = False
        while choix == False :
            
            #si la categorie ne possede aucuns aliments presents dans le frigo
            if(taille == 0):
                ecranlcd.setText("Aucun aliment n est disponible pour cette categorie")
                time.sleep(5)
                choix = True
                self.categories() #retour aux categories
            
            else:
                valPotentio = potentio.readFromNb(taille)
                for i in range(1,taille+1):
                    #on n affiche pas les aliments qui ne sont pas presents dans le frigo
                    if liste[i-1][2] != '0':
                        if(valPotentio == taille - (i)):
                            ecranlcd.setText(""+liste[i-1][1]+"")#nom des produits
                            time.sleep(2)
                            
                            if(self.buttonV.verifRead(self.buttonV.button)):
                                self.id = liste[i-1][0]
                                ecranlcd.setText("Choisissez une quantite : ")
                                time.sleep(2)
                                choix = True
                                self.quantite() #choix quantite

                            elif(self.buttonD.verifRead(self.buttonD.button)):
                                ecranlcd.setText("Vous avez annule")
                                time.sleep(5)
                                choix = True
                                self.debut()
                            
                        elif(valPotentio == taille):
                            ecranlcd.setText(""+liste[i-1][1]+"")#nom des produits
                            time.sleep(2)

                            if(self.buttonV.verifRead(self.buttonV.button)):
                                self.id = liste[i-1][0]
                                ecranlcd.setText("Choisissez une quantite : ")
                                time.sleep(2)
                                choix = True
                                self.quantite()#choix quantite

                            elif(self.buttonD.verifRead(self.buttonD.button)):
                                ecranlcd.setText("Vous avez annule")
                                time.sleep(5)
                                choix = True
                                self.debut()

    #Choix de la quantite a prendre, selon le stock actuel
    def quantite(self):
        choix = False
        while choix == False:
            
            liste = self.listeQte(self.id)
            quantite = int(liste[0][2])
            valPotentio = potentio.readFromNb(quantite)
            for i in range(1,quantite+1) :
                if(valPotentio == quantite - (i)):
                    stri = str(i)
                    ecranlcd.setText(""+stri+"")
                    time.sleep(3)
                    if(self.buttonV.verifRead(self.buttonV.button)):
                        self.qte = i
                        self.majStock(False)
                        ecranlcd.setText("Retirez le(s) aliment(s) du frigo")
                        time.sleep(5)
                        choix = True
                        self.fin() #fin

                    elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()
                    
                elif(valPotentio == quantite):
                    stri = str(quantite)
                    ecranlcd.setText(""+stri+"")
                    time.sleep(3)
                    if(self.buttonV.verifRead(self.buttonV.button)):
                        self.qte = i
                        self.majStock(False)
                        ecranlcd.setText("Retirez le(s) aliment(s) du frigo")
                        time.sleep(5)
                        choix = True
                        self.fin() #fin

                    elif(self.buttonD.verifRead(self.buttonD.button)):
                        ecranlcd.setText("Vous avez annule")
                        time.sleep(5)
                        choix = True
                        self.debut()
                    
    #Fin du choix pour l utilisateur     
    def fin(self):
         ecranlcd.setText("Merci au revoir")
         time.sleep(2)
         ecranlcd.setText("")
         self.identif = 0
         self.step = 8

    #
    def listeQte(self,id):
        liste=[]
        with  open('/home/pi/ASAIOT/utils/stock.csv','r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if id == row[0] :
                    liste.append(row)
            f.close()           
        return liste

    #Liste des aliments selon la categorie choisie
    def listAl(self,categorie):
        liste=[]
        with  open('/home/pi/ASAIOT/utils/stock.csv','r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if categorie in row :
                    liste.append(row)
            f.close()
        return liste

    #Convertit l id de la categorie afin quelle corresponde au csv
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

    #Met a jour le stock                             
    def majStock(self,ajout): #ajout booleen : true si il faut ajouter au stock false sinon
        text = open("/home/pi/ASAIOT/utils/stock.csv", "r")
        txt=csv.reader(text)

        liste=[]
            
        for ligne in txt :
            if(ligne[0]==self.id):
                if(ajout):
                    anc_qte = int(ligne[2])
                    ch_qte = int(self.qte)
                    nv_qte=anc_qte + ch_qte  #quantite apres soustraction de la quantite choisie par l utilisateur
                else :
                    nv_qte=int(ligne[2]) - int(self.qte) #quantite apres soustraction de la quantite choisie par l utilisateur
                nv_qte=str(nv_qte)
                ligne[2]=ligne[2].replace(ligne[2],nv_qte)
                
            liste.append(ligne)

        out=open("/home/pi/ASAIOT/utils/stock.csv", "w")
        wr=csv.writer(out)  
        wr.writerows(liste)
        out.close()
        text.close()
        print("Mise a jour du stock")

    #Rajoute la date de peremption au csv
    def majDate(self):
        text = open("/home/pi/ASAIOT/utils/stock.csv", "r")
        txt=csv.reader(text)

        liste=[]
        if(int(self.m) < 10):
            date = ""+self.j+"/0"+self.m+"/"+self.a+""
        else :
            date = ""+self.j+"/"+self.m+"/"+self.a+""

        for ligne in txt :
            if(ligne[0]==self.id):
                ligne[4]=ligne[4].replace(ligne[4],date)
                
            liste.append(ligne)

        out=open("/home/pi/ASAIOT/utils/stock.csv", "w")
        wr=csv.writer(out)  
        wr.writerows(liste)
        out.close()
        text.close()
        print("Mise a jour du stock")

