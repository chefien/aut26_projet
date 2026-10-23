'''Classes par Émilie''' #allo
from classe_khadija import Data
import random

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


data = Data("assets/fishEncylopedia3.csv")
catch = Catch(data)