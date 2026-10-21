#classe de khadija: Data(), Fishing(), load(), save(), csv files + folder for assetz
import pandas as pd

class data():
    def __init__(self,file):
        self.file = str(file) #file lien/nom
        self.tableau = self.readFile() # cest le dataframe soit le tableau en version pandas
        self.poissonEncylopedia = self.initPoissonDict() # executer direct apres init + cest un dictionnaire
        self.dechets = self.initDechetsList() #cest un dictionnaire

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
    #aussi si vous voulez des setters lmk!!
    def getPoissonEncyclopedia(self):
        return self.poissonEncylopedia # retourne un dictionnaire le gros truc
    def getDechets(self):
        return self.dechets # retourne un dictionnaire le gros truc
    def getPoissonNameList(self):
        poissonNames = [name for name in self.poissonEncyclopedia.keys()]
        return poissonNames #retourne la liste de tous les noms des poisssons
    def getPoissonToutStatsList(self, name): #very specific: itll take the dict of stats and puts then in a list so itll be something like list(1,23,hello,1212)
        poissonsStats = [value for dictio in self.poissonEncyclopedia.values() for value in dictio.values()] # it goes in the first dict, and then goes in the second to extract the values of the second dict
        return poissonsStats # retourne TOUS les valeurs et les mets dans une liste
    def getPoissonSpecificStatsList(self, name): #very specific: au lieu de retourner les valeurs du poisson dans un dict, elle le fait liste style
       valueDict = self.poissonE ncyclopedia[name] #retourne le dictionnaire des stats du poisson
       poissonNameStats = [value for value in valueDict]
       return poissonNameStats
    def getPoissonSpecific(self, name):
        return self.poissonEncylopedia[name] # retourne les stats du poissons (dans un dictionnaire)
    def getDechetSpecific(self,name):
        return self.dechets[name] #retourne les stats du dechets dans un dictionnaire
        

            


#data1 = data("/Users/khadija/Documents/GitHub/aut26_projet/assets/fishEncylopedia(Sheet1).csv") #jsp honestly
#le lien du fichier ne fonctionne pas correctement, faut voir cest quoi le probleme avec le fichier
#wshhh