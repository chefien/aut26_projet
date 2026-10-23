'''Classes par Émilie'''
from classe_khadija import Data
import random

class User():
    '''Joueur et ses informations'''
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.inventory = dict()


class Catch():
    '''Poisson ou déchet possible de pêcher'''
    def __init__(self, data):
    
        self.name = random.choice(data.getAllNamesList())
        if self.name in data.getFishNameList():
            self.weight = random.randrange(data.getFishSpecific(self.name)["startWeight"], data.getFishSpecific(self.name)["finishWeight"], 0.0001)  #(en kg)
            self.size = random.randrange(data.getFishSpecific(self.name)["startSize"], data.getFishSpecific(self.name)["finishSize"], 0.1)  #(en cm)
        else : #pour les déchets
            self.weight = random.randrange(data.getTrashSpecific(self.name)["startWeight"], data.getTrashSpecific(self.name)["finishWeight"], 0.0001)  #(en kg)
            self.size = random.randrange(data.getTrashSpecific(self.name)["startSize"], data.getTrashSpecific(self.name)["finishSize"], 0.1)  #(en cm)
        
        self.print()

    def print(self):
        print(self.name)


data = Data("assets/fishEncylopedia2(Sheet1).csv")
catch = Catch(data)