#classe de khadija: Data(), Fishing(), savingSystem(), csv files + folder for assetz, stats()
import pandas as pd
import customtkinter as ctk
from PIL import Image  # cest une librairie qui manipule les images png, jpg etc
from tkinter import PhotoImage

class Data():
    def __init__(self,file):
        self.file = str(file) #file lien/nom
        self.dataFrame = self.readFile() # cest le dataframe soit le tableau en version pandas

        if self.dataFrame is not None:
            self.fishEncyclopedia = self.initFishDict() # executer direct apres init + cest un dictionnaire
            self.trash = self.initTrashList() #cest un dictionnaire
            
        
    def readFile(self): #transporter le csv à un dataFrame
        try:
            df = pd.read_csv(self.file, delimiter = ';')
            df = pd.DataFrame(df) #conversion au dataframe/ tableau plus beau
        except Exception as e:
            print(e)
            return None
                    
        return df
    
    def initFishDict(self): # initialiser la liste du poisson item
        fishDict = {}
        for i in range(len(self.dataFrame)):
            if self.dataFrame.at[i,"isFish"] == True: #seulement les poissons
                name = self.dataFrame.iloc[i, 0]
                value = self.dataFrame.iloc[i, 1:].to_dict() # dict dans un dict
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
                value = self.dataFrame.iloc[i, 1:].to_dict() # dict dans un dict
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
    def getTrashNameList(self):
        trashNames = [name for name in self.trash.keys()]
        return trashNames #retourne la liste de tous les noms des déchets
    def getAllNamesList(self):
            all = []
            all.extend(self.getTrashNameList, self.getFishNameList)
            return all # retourne tous les noms des objets
    def getFishAllStatsList(self): #tres specifique:elle prend les stats du dict et les met dans une list exemple de l'affichage list(1,23,hello,1212)
        fishStats = [value for dictio in self.fishEncyclopedia.values() for value in dictio.values()] # rentre dans le premier dict, et puis dans le deuxiemeet extrait les stats du dict 2
        return fishStats # retourne TOUS les valeurs et les mets dans une liste
    def getFishSpecificStatsList(self, name): #tres specifique: au lieu de retourner les valeurs du poisson dans un dict, elle le fait liste style
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
                
class statsPlot():
    def __init__(self):
        pass
    '''
    cette classe va stocker les stats et en tirer de lobjet user. ainsi, elle gère la création du graphique
    '''

class GifImage(): #OPTIONELLE A REVOIR ET TESTER SI CA FONCTIONNE
    def __init__(self, file, root, x, y, width, height, wait):
        if self.checkFile(file) != None:
            self.file = file # cest comme si jai fait au fond self.file= file
            self.root = root
            self.x = x
            self.y = y 
            self.width = width
            self.height = height
            self.wait = wait
            self.showAnimation()
        

    def checkFile(self,file): #avant meme de commencer on check si l'image n'a pas de probleme
        try:
            Image.open(file)
        except Exception as e:
            print(e)
            return None
        return file
    
    def showAnimation(self):
        openImg = Image.open(self.file)
        self.showAnim = None
        frames = openImg.n_frames #n_frames indique le nb d'image qui se trouve dans ce gif
        img = [PhotoImage(file = self.file, format = f"gif -index {i}",master = self.root) for i in range(frames)]# par comprehension a chaque frame on call la fct et on le stock dans une liste + master cest ou il va dessiner

        gifLabel = ctk.CTkLabel(self.root, text = "",width = self.width, height = self.height) # on revient avec ctk pour que ca soit compatible
        gifLabel.place(x = self.x, y = self.y) # ou le placer
                 
        def animation(count):
            newImg = img[count] # on commence avec ce frame precis
            gifLabel.configure(image = newImg) # on prend le label et on le transforme en img
            count += 1 # prochaine img

            if count == frames: # si on arrive a la fin
                count = 0 # on reset le compte pour qu'on puisse loop apres
            self.showAnim = self.root.after(self.wait, lambda: animation(count) ) # on attend self.wait de seconde avant de refaire la fonction: de plus lambda fais que la fct ne s'eexecute pas immediatement, et d'attendre jusqu'a ce que la condition soit satisfaite
        animation(0) # on fait demarer lanimation le zero cest le debut soit le count 0

app = ctk.CTk()
app.geometry("800x400")

fishimg = GifImage("assets/fish.gif", app,50, 50, 100, 100, 1) # to fix the sizing
app.mainloop()





data1 = Data("assets/fishEncylopedia(Sheet1).csv") #jsp honestly
#le lien du fichier ne fonctionne pas correctement, faut voir cest quoi le probleme avec le fichier
#wshhh