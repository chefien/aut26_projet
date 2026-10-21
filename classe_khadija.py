#classe de khadija: Data(), Fishing(), load(), save(), csv files + folder for assetz
import pandas as pd

class data():
    def __init__(self,file):
        self.file = str(file) #file lien/nom
        self.dataFrame = self.readFile() # cest le dataframe soit le tableau en version pandas
        self.fishEncyclopedia = self.initFishDict() # executer direct apres init + cest un dictionnaire
        self.trash = self.initTrashList() #cest un dictionnaire

    def readFile(self): #transporter le csv à un dataFrame
        try:
            df = pd.read_csv(self.file, delimiter = ';')
            df = pd.DataFrame(df) #conversion au dataframe/ tableau plus beau
        except Exception as e:
            print(e)
                    
        return df
    
    def initFishDict(self): # initialiser la liste du poisson item
        fishDict = {}
        for i in range(len(self.dataFrame)):
            if self.dataFrame.at[i,"isFish"] == True: #seulement les poissons
                name = self.dataFrame.iloc[i, 0]
                value = self.dataFrame.iloc[i, 1:].to_dict() # dict inside of a dict
                fishDict[name] = value # exemple: poisson rouge : weight: 23 size: 4 etcetc il n ya pas le nom du poisson dans le dict, lmk si cela pose des problemes
                '''
                exemple: poissondict:
                clownfish: 
                {'weight': 23, 'size': 4, 'rarity': 2, 'isFish': True} <- dictionnaire 
                '''
        return fishDict

    def initTrashList(self):
        trashDict = {}
        for i in range(len(self.dataFrame)):
            if self.dataFrame.at[i,"isFish"] == False: #seulement les dechets
                name = self.dataFrame.iloc[i, 0]
                value = self.dataFrame.iloc[i, 1:].to_dict() # dict inside of a dict
                trashDict[name] = value 
        return trashDict



    #les getters si jamais
    #aussi si vous voulez des setters lmk!!
    def getFishEncyclopedia(self):
        return self.fishEncyclopedia # retourne un dictionnaire le gros truc
    def getTrash(self):
        return self.trash # retourne un dictionnaire le gros truc
    def getFishNameList(self):
        fishNames = [name for name in self.fishEncyclopedia.keys()]
        return fishNames #retourne la liste de tous les noms des poisssons
    def getFishAllStatsList(self): #very specific: itll take the dict of stats and puts then in a list so itll be something like list(1,23,hello,1212)
        fishStats = [value for dictio in self.fishEncyclopedia.values() for value in dictio.values()] # it goes in the first dict, and then goes in the second to extract the values of the second dict
        return fishStats # retourne TOUS les valeurs et les mets dans une liste
    def getFishSpecificStatsList(self, name): #very specific: au lieu de retourner les valeurs du poisson dans un dict, elle le fait liste style
       valueDict = self.fishEncyclopedia[name] #retourne le dictionnaire des stats du poisson
       fishNameStats = [value for value in valueDict.values()]
       return fishNameStats
    def getFishSpecific(self, name):
        return self.fishEncyclopedia[name] # retourne les stats du poissons (dans un dictionnaire)
    def getTrashSpecific(self,name):
        return self.trash[name] #retourne les stats du dechets dans un dictionnaire
        
class savingSystem():
    def __init__(self):
     # à revoir faut mettre tous les attributs to save! (for loading/ pour chaque partie)
        pass
        #on a besoin de getters et setters:
        # getters so we can be able to read the info after
        # setters so we can be able to save stuff
        '''
        what to save?
        inventory, user object, discovered fish, and statistics(for the matplot)
        '''
                


data1 = data("assets/fishEncylopedia(Sheet1).csv") #jsp honestly
#le lien du fichier ne fonctionne pas correctement, faut voir cest quoi le probleme avec le fichier
#wshhh