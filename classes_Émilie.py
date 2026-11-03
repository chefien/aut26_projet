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

    '''update level avec condition, si rempli change level et return vrai, sinon return faux
    level + (level-1) +2
    '''
    def isLeveledUp(self):
        if (self.level + (self.level-1) + 2) >= self.nbFish:
            self.level += 1
            return True
        return False

    def getUserInventory(self):
        return self.inventory

    def updateInventory(self, catch):
        self.inventory.append(catch)
        self.nbCatch += 1

        if catch.isFish:
            self.nbFish += 1
        else:
            self.nbTrash += 1

    def getUserNbFish(self):
        return self.nbFish

    def getUserNbTrash(self):
        return self.nbTrash

    def getUserNbCatch(self):
        return self.nbCatch








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

        self.print()

    def print(self): #affiche les attributs
        print(self.name)
        print(self.weight)
        print(self.size)
        print(self.isFish)
        print(self.description)
        print(self.rarity)








class Timer(): # fonctionne mais en perfectionnement
    def __init__(self, seconds, positionX=None, positionY=None):
        self.seconds = seconds
        self.lastSecondCounted = -1
        self.isFinished = False
        self.label = None

        if positionX is not None and positionY is not None:
            self.label = ctk.CTkLabel(app, text=f"{self.seconds:02d} sec", font=("Arial", 24))
            self.label.place(x=positionX, y=positionY)
        
        self.end = time.time() + self.seconds

    def updateTimerWithPrint(self):
            
        currentTime = time.time()
            
        if currentTime < self.end:
            timeLeft = int(self.end - currentTime)
            
            if timeLeft != self.lastSecondCounted:
                self.label.configure(text=f"{(timeLeft+1):02d} sec")
                self.lastSecondCounted = timeLeft
                    
            app.after(50, self.updateTimerWithPrint)

        else:
            self.label.configure(text="C'est fini !")
            self.isFinished = True


    def timingWithoutPrint(self):

        currentTime = time.time()

        #si on n'est pas encore rendu à la fin, on demande juste de rappeler la fonction
        if currentTime < self.end:           
            app.after(50, self.updateTimerWithPrint)
        
        else:
            self.isFinished = True

    def getIsFinished(self):
        return self.isFinished



app = ctk.CTk()
app.geometry("800x400")

timer = Timer(10, 550, 50)

app.after(500, timer.updateTimerWithPrint)

app.mainloop()
