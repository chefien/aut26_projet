'''Classes par Émilie''' #allo
from classe_khadija import Data
from classe_khadija import GifImage
import customtkinter as ctk
import random
import time

class User():
    '''Joueur et ses informations'''
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.inventory = []

    def getUserName(self):
        return self.name

    def getUserLevel(self):
        return self.level

    def getUserInventory(self):
        return self.inventory

    def updateInventory(self, catch):
        self.inventory.append(catch)


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


#data = Data("assets/fishEncylopedia3.csv")
#catch = Catch(data)


class Timer(): # fonctionne mais en perfectionnement
    def __init__(self, seconds):
        self.seconds = seconds

    def updateTimerWithPrint(self):

        global lastSecondCounted
            
        current_time = time.time()
            
        if current_time < end_time:
            timeLeft = int(end_time - current_time)
            
            if timeLeft != lastSecondCounted:
                timer_label.configure(text=f"{(timeLeft+1):02d} sec")
                    
                lastSecondCounted = timeLeft
                    
            app.after(50, timer.updateTimerWithPrint)
        else:
            timer_label.configure(text="C'est fini !")


    def timingWithoutPrint(self): # non terminé
        seconds = self.seconds
        while seconds > 0:
            time.sleep(1)
            seconds -= 1

        import time



timer = Timer(10)

app = ctk.CTk()
app.geometry("800x400")

fishimg = GifImage("assets/fish.gif", app,50, 50, 100, 100, 100) # to fix the sizing

end_time = time.time() + timer.seconds
lastSecondCounted = -1

timer_label = ctk.CTkLabel(app, text=f"{timer.seconds:02d} sec", font=("Arial", 24))
timer_label.place(x=550, y=50)

timer.updateTimerWithPrint()

app.mainloop()
