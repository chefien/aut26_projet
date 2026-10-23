'''Classes par Émilie'''
from classe_khadija import data
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
    
        self.name = random.choice(data.getAllNamesList)
        self.print
        #getPoissonSpecific(name)

    def print(self):
        print(self.name)

data= data("assets/fishEncylopedia(Sheet1).csv")
catch=Catch(data)