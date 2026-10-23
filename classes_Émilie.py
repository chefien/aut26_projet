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
        self.weight = random.randrange(data.getPoissonSpecific([self.name])["startWeight"], data.getPoissonSpecific([self.name])["finishWeight"], 0.0001)  #(en kg)
        self.size = random.randrange(data.getPoissonSpecific([self.name])["startSize"], data.getPoissonSpecific([self.name])["finishWeight"], 0.0001)  #(en kg)
        #getPoissonSpecific(name)
        self.print()

    def print(self):
        print(self.name)


data = Data("assets/fishEncylopedia2(Sheet1).csv")
catch = Catch(data)