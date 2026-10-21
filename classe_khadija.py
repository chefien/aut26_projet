#classe de khadija: Data(), Fishing(), load(), save(), csv files + folder for assetz
import pandas as pd

class data():
    def __init__(self,file):
        self.file = str(file) #file lien/nom
        self.tableau = self.readFile() # cest le dataframe soit le tableau en version pandas
        self.poissonEncylopedia = self.initPoissonDict() # executer direct apres init
        self.dechets = self.initDechetsList()

    def readFile(self): #transporter le csv à un dataFrame
        df = pd.read_csv(self.file, delimiter = ';')
        df = pd.DataFrame(df) #conversion au dataframe/ tableau plus beau
        return df
    
    def initPoissonDict(self): # initialiser la liste du poisson item
        poissonDict = {}
        for i in range(len(self.tableau)):
            if self.tableau.at[i,"isFish"] == True: #seulement les poissons
                name = self.tableau.iloc[i, 0]
                value = self.tableau.iloc[i, 1:].to_dict() # dict inside of a dict
                poissonDict[name] = value # exemple: poisson rouge : weight: 23 size: 4 etcetc il n ya pas le nom du poisson dans le dict, lmk si cela pose des problemes
                '''
                exemple: poissondict:
                clownfish: 
                {'weight': 23, 'size': 4, 'rarity': 2, 'isFish': True} <- dictionnaire 
                '''
        return poissonDict

    def initDechetsList(self):
        dechetsDict = {}
        for i in range(len(self.tableau)):
            if self.tableau.at[i,"isFish"] == False: #seulement les dechets
                name = self.tableau.iloc[i, 0]
                value = self.tableau.iloc[i, 1:].to_dict() # dict inside of a dict
                dechetsDict[name] = value 
        return dechetsDict



    #les getters si jamais
    def getPoissonEncyclopedia(self):
        return self.poissonEncylopedia # retourne un dictionnaire
    def getDechets(self):
        return self.dechets # retourne un dictionnaire
    def getPoissonList(self):
        poissonNames = [name for name in self.poissonEncyclopedia.keys()]
        return poissonNames #retourne la liste de tous les noms des poisssons
    def getPoissonSpecific(self, name):
        

            


data1 = data("/Users/khadija/Documents/GitHub/aut26_projet/assets/fishEncylopedia(Sheet1).csv") #jsp honestly
