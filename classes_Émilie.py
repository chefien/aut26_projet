'''Classes par Émilie'''

class User():
    '''Joueur et ses informations'''
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.inventory = dict()


class Catch():
    '''Poisson ou déchet possible de pêcher'''
    def __init__(self):
        pass