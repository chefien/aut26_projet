'''Classes par Émilie'''


from classe_khadija import Data
from classe_khadija import GifImage
import customtkinter as ctk
import random
import time




class User():
    '''Joueur et ses informations'''
    def __init__(self):
        self.name = None
        self.level = 0
        self.inventory = []
        self.nbFish = 0
        self.nbTrash = 0
        self.nbCatch = 0

    def setUserName(self, name):
        self.name = name

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

    def updateInventory(self, catch):
        self.inventory.append(catch)
        self.nbCatch += 1

        if catch.isFish:
            self.nbFish += 1
        else:
            self.nbTrash += 1

    '''update level avec condition, si rempli change level et return vrai, sinon return faux
    level + (level-1) + 2
    '''
    def isLeveledUp(self):
        if (self.level + (self.level-1) + 2) >= self.nbFish:
            self.level += 1
            return True
        return False




class Catch():
    '''Poisson ou déchet possible de pêcher'''
    def __init__(self, data):
    
        self.name = random.choice(data.getAllNamesList())
        
        if self.name in data.getFishNameList(): #pour les poissons
            
            self.weight = random.uniform(float(data.getFishSpecific(self.name)["startWeight"]), float(data.getFishSpecific(self.name)["finishWeight"]))  #(en kg)
            self.weight = round(self.weight,3)
            self.size = random.uniform(float(data.getFishSpecific(self.name)["startSize"]), float(data.getFishSpecific(self.name)["finishSize"]))  #(en cm)
            self.size = round(self.size,3)
            self.isFish = True
            self.description = data.getFishSpecific(self.name)["description"]
            self.rarity = data.getFishSpecific(self.name)["rarity"]
 
        else : #pour les déchets
            self.weight = random.uniform(float(data.getTrashSpecific(self.name)["startWeight"]), float(data.getTrashSpecific(self.name)["finishWeight"]))  #(en kg)
            self.weight = round(self.weight,3)
            self.size = random.uniform(float(data.getTrashSpecific(self.name)["startSize"]), float(data.getTrashSpecific(self.name)["finishSize"]))  #(en cm)
            self.size = round(self.size,3)
            self.isFish = False
            self.description = data.getTrashSpecific(self.name)["description"]
            self.rarity = data.getTrashSpecific(self.name)["rarity"]


        #les attributs du temps d'attente, du temps pour pêcher et du nombre de clicks nécessaires pour pêcher dépendent de la rareté
        if self.rarity == "commun":
            self.timeWaiting = 30  #(en sec)
            self.timeFishing = 60  #(en sec)
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
        self.seconds = seconds
        self.lastSecondCounted = -1
        self.isFinished = False
        self.label = None
        self.master = master
        
        self.label = ctk.CTkLabel(app, text=f"{self.seconds:02d} sec", font=("Arial", 15, "bold"), text_color="#B10E0E")
        self.label.pack(side="right", padx=10)
        
        self.end = time.time() + self.seconds



    def updateTimerWithPrint(self):
        currentTime = time.time()
            
        if not self.isFinished and currentTime < self.end:
            timeLeft = int(self.end - currentTime)
            
            if timeLeft != self.lastSecondCounted:
                self.label.configure(text=f"{(timeLeft+1):02d} sec")
                self.lastSecondCounted = timeLeft
                    
            self.master.after(50, self.updateTimerWithPrint)

        else:
            self.label.configure(text="C'est fini !")
            self.isFinished = True
            self.master.after(3*1000, self.autoDestruct)



    def timingWithoutPrint(self):
        currentTime = time.time()

        #si on n'est pas encore rendu à la fin, on demande juste de rappeler la fonction
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






app = ctk.CTk()
app.geometry("800x400")

timer = Timer(app, 10)

app.after(500, timer.updateTimerWithPrint)

app.mainloop()
