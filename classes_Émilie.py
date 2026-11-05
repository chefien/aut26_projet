'''Classes par Émilie'''

from classe_khadija import Data
from classe_khadija import GifImage
import customtkinter as ctk
import random
import time


class User():
    '''Joueur et ses informations'''
    def __init__(self):

        #initialement None, on demandera le nom par la suite
        self.name = None

        #augmentera selon le nombre de poissons attrappés
        self.level = 0

        #contiendra tout ce qui sera attrappé
        self.inventory = []

        #seront mis à jour lors de chaque prise
        self.nbFish = 0
        self.nbTrash = 0
        self.nbCatch = 0


    #après avoir demander le nom
    def setUserName(self, name):
        self.name = name

    #getters
    def getUserName(self):
        return self.name

    def getUserLevel(self):
        return self.level

    def getUserInventory(self):
        return self.inventory

    def getUserNbFish(self):
        return self.nbFish

    def getUserNbTrash(self):
        return self.nbTrash

    def getUserNbCatch(self):
        return self.nbCatch

    #met à jour l'inventaire, le total de poissons, de déchets et les deux ensemble
    def updateInventory(self, catch):
        self.inventory.append(catch)
        self.nbCatch += 1

        if catch.isFish:
            self.nbFish += 1
        else:
            self.nbTrash += 1


    #update level avec condition, si rempli change level et return vrai, sinon return faux
    # level + (level-1) + 2 doit être 
    def isLeveledUp(self):
        if self.nbFish >= (self.level + (self.level-1) + 2):
            self.level += 1
            return True
        return False




class Catch():
    '''Poisson ou déchet possible de pêcher'''
    #doit être créé avant la pêche car le temps d'attente, le temps de pêche et le nombre de clics pour la pêche sont fait ici
    def __init__(self, data):

        #on veut un poisson/déchet au hasard
        self.name = random.choice(data.getAllNamesList())

        #pour les poissons
        if self.name in data.getFishNameList():

            #on veut le poids (en kg) au hasard dans la plage associée
            self.weight = random.uniform(float(data.getFishSpecific(self.name)["startWeight"]), float(data.getFishSpecific(self.name)["finishWeight"]))
            #on a seulement besoin de 3 chiffres après la virgule
            self.weight = round(self.weight,3)

            #on veut la longueur (en cm) au hasard dans la plage associée
            self.size = random.uniform(float(data.getFishSpecific(self.name)["startSize"]), float(data.getFishSpecific(self.name)["finishSize"]))
            #on a seulement besoin de 3 chiffres après la virgule
            self.size = round(self.size,3)

            self.isFish = True

            #la description spécifique à la sorte de poisson
            self.description = data.getFishSpecific(self.name)["description"]

            #la rareté va servir pour implémenter le temps d'attente, le temps de pêche et le nombre de clics pour la pêche
            self.rarity = data.getFishSpecific(self.name)["rarity"]

        #pour les déchets
        else : 

            #on veut le poids (en kg) au hasard dans la plage associée
            self.weight = random.uniform(float(data.getTrashSpecific(self.name)["startWeight"]), float(data.getTrashSpecific(self.name)["finishWeight"]))  #(en kg)
            #on a seulement besoin de 3 chiffres après la virgule
            self.weight = round(self.weight,3)

            #on veut la longueur (en cm) au hasard dans la plage associée
            self.size = random.uniform(float(data.getTrashSpecific(self.name)["startSize"]), float(data.getTrashSpecific(self.name)["finishSize"]))  #(en cm)
            #on a seulement besoin de 3 chiffres après la virgule
            self.size = round(self.size,3)

            self.isFish = False

            #la description spécifique à la sorte de déchet
            self.description = data.getTrashSpecific(self.name)["description"]

            #la rareté va servir pour implémenter le temps d'attente, le temps de pêche et le nombre de clics pour la pêche
            self.rarity = data.getTrashSpecific(self.name)["rarity"]


        #les attributs du temps d'attente, du temps pour pêcher et du nombre de clics nécessaires pour pêcher dépendent de la rareté
        if self.rarity == "commun":

            #le temps d'attente avant que la pêche ne commence (en sec)
            self.timeWaiting = 30

            #le temps maximal pour atteindre le nombre clics requis pour obtenir la prise (en sec)
            self.timeFishing = 60

            #le nombre de clics nécessaire d'atteindre pour obtenir la prise
            self.clicks = 150

        elif self.rarity == "uncommun":
            self.timeWaiting = 60  #(en sec)
            self.timeFishing = 50  #(en sec)
            self.clicks = 155

        elif self.rarity == "rare":
            self.timeWaiting = 90  #(en sec)
            self.timeFishing = 40  #(en sec)
            self.clicks = 160

        elif self.rarity == "epic":
            self.timeWaiting = 120  #(en sec)
            self.timeFishing = 30  #(en sec)
            self.clicks = 165

        elif self.rarity == "legendary":
            self.timeWaiting = 150  #(en sec)
            self.timeFishing = 20  #(en sec)
            self.clicks = 170 

        else:
            self.timeWaiting = 0  #(en sec)
            self.timeFishing = 0  #(en sec)
            self.clicks = 0     

        

    def getTimeWaiting(self):
        return self.timeWaiting

    def getTimeFishing(self):
        return self.timeFishing

    def getNbClicks(self):
        return self.clicks







class Timer(): 
    def __init__(self, master, seconds):

        #temps inital du timer
        self.seconds = seconds
        self.milliseconds = 0

        
        self.lastSecondCounted = -1
        self.isFinished = False
        self.label = None
        self.master = master
        
        self.label = ctk.CTkLabel(self.master, text=f"{self.seconds:02d}.{self.milliseconds:02d} sec", font=("Arial", 15, "bold"), text_color="#B10E0E")
        self.label.pack(side="right", padx=10)
        
        self.end = time.time() + self.seconds



    def updateTimerWithPrint(self):
        currentTime = time.time()
            
        if not self.isFinished and currentTime < self.end:
            timeLeft = self.end - currentTime

            #séparer les secondes et les millisecondes
            secondsLeft = int(timeLeft)

            #prendre la partie après la virgule et on la multiplie par 100
            millisecondsLeft = int((timeLeft - secondsLeft) * 100)

            #mettre à jour le label (le 02d c'est pour 2 décimales)
            self.label.configure(text=f"{secondsLeft:02d}.{millisecondsLeft:02d} sec")
                                
            #rafraîchir toutes les 10 ms pour que le défilement soit fluide
            self.master.after(10, self.updateTimerWithPrint)
            

        else:
            self.label.configure(text="C'est fini !")
            self.isFinished = True
            self.master.after(3*1000, self.autoDestruct)

            
            

    def updatetimerWithoutPrint(self):
        currentTime = time.time()

        #si il n'a pas encore été détruit (autoDestruct) et on n'est pas encore rendu à la fin
        if not self.isFinished and currentTime < self.end:           
            self.master.after(50, self.updateTimerWithPrint)
        
        else:
            self.isFinished = True


    def getIsFinished(self):
        return self.isFinished


    def autoDestruct(self):
        self.label.destroy()


    def stop(self):
        self.isFinished = True
        if self.label is not None and self.label.winfo_exists():
            self.label.configure(text="00 sec")






'''app = ctk.CTk()
app.geometry("800x400")

timer = Timer(app, 10)

app.after(500, timer.updateTimerWithPrint)

app.mainloop()'''
