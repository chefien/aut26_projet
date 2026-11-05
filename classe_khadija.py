#classe de khadija: Data(), Fishing(), savingSystem(), csv files + folder for assetz, stats()
import pandas as pd
import random
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image  # cest une librairie qui manipule les images png, jpg etc




class Data():
    def __init__(self,file):
        self.file = str(file) #file lien/nom
        self.dataFrame = self.readFile() # cest le dataframe soit le tableau en version pandas

        if self.dataFrame is not None:
            #print(self.dataFrame)
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
            all.extend(self.getTrashNameList())
            all.extend(self.getFishNameList())
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
        
class SavingSystem():
    def __init__(self, user,file,data):
        
     # à revoir faut mettre tous les attributs to save! (for loading/ pour chaque partie)
        #on save ca pour la premiere fois
        self.inventory = user.getUserInventory()
        self.username = user.getUserName()
        self.level = user.getUserLevel()
        self.playedBefore = False
        self.file = file
        
        
        #on a besoin de getters et setters:
        # getters so we can be able to read the info after
    def getInv(self):
        return self.inventory
    def getUsername(self):
        return self.username
    def getLevel(self):
        return self.level
    def getPlayedBefore(self):
        return self.playedBefore
    
        # setters so we can be able to save stuff
    
    def setInv(self,newInventory):
        self.inventory = newInventory
        self.user.setInventory = self.inventory
    def setUsername(self, newUsername):
        self.username = newUsername
        self.user.setUsername = self.username
    def setLevel(self, newLevel):
        self.level = newLevel
        self.user.setLevel = self.Level
    def setPlayedBefore(self,status):
        self.playedBefore = status

    def loadingFromCsv(self,file):
        from classes_Émilie import Catch
        try:
            data = pd.read_csv(file)
        except Exception as e:
            print(e)
            return
        tempInv = []
        for i in data:
            catchTemp = Catch(self.data)
            catchTemp.setName(data.loc[0,"Name"])
            catchTemp.setWeight(data.loc[0,"Weight"])
            catchTemp.setSize(data.loc[0,"Size"])
            catchTemp.setIsFish(data.loc[0,"IsFish"])
            catchTemp.setDescription(data.loc[0,"Description"])
            catchTemp.setRarity(data.loc[0,"Rarity"])
            catchTemp.setTimeFishing(data.loc[0,"TimeFishing"])
            tempInv.append(catchTemp)
                    
        
        self.username = data.loc[0,"Username"]
        self.level = data.loc[0,"Level"]
        self.playedBefore = data.loc[0,"Status"]
        return f'chargement du fichier'
    def savingToFile(self):
    # tu vas devoir set avant de sauvegarder un fichier
        data = {
            "Name" : [i.getName() for i in self.getInv()],# catch name
            "Weight" : [i.getWeight() for i in self.getInv()],
            "Size" : [i.getSize() for i in self.getInv()],
            "IsFish" : [i.getIsFish() for i in self.getInv()],
            "Description" : [i.getDescription() for i in self.getInv()],
            "Rarity" : [i.getRarity() for i in self.getInv()],
            "TimeFishing" : [i.getTimeFishing() for i in self.getInv()],
            "Username" : self.getUsername(),
            "Level" : self.getLevel(),
            "Status" : self.getPlayedBefore() }
        df = pd.DataFrame(data)
        df.to_csv(self.file, index = False)

        return f'sauvegardement du fichier'

        ''' 
        what to save?
        inventory, user object, discovered fish, and statistics(for the matplot)
        
        i need to add saving from csv and loading from csv, so the load one will create a csv and store everything i just got and then the save will take the old csv and either overwrite (which i think is not that possible ) or it takes old,deletes it and put a new folder in its place (which is literally overwriting i just realised lmao)
        '''

                
class StatsPlot(ctk.CTkFrame):
    
    def __init__(self,master,user,x,y):
        super().__init__(master)
        self.fishCollected, self.trashCollected = self.filtrate(user)
        self.all = len(user.getUserInventory())
        self.canvas = self.ploting(x,y)

    def filtrate(self,user):
        inventory = user.getUserInventory()
        trash = 0 
        fish = 0
        for item in inventory:
            if item.getIsFish(): #redo the getters
                fish += 1
            else:
                trash += 1 
        return fish, trash

    def ploting(self,x,y):
        fishPercentage = (self.fishCollected / self.all) * 100
        trashPercentage = (self.trashCollected / self.all) * 100
        values = [fishPercentage,trashPercentage]
        names = ["Nombre de poissons déja péché", "Nombre d'ordures déja péché"]

        figure = Figure(figsize = (x,y), dpi = 100) #dpi cest la resolution et figsize cest la taille, figure is the blank space where the graph will be drawn
        subplot = figure.add_subplot(111) #notre graph, add tells it to add space in the canvas for the plot, 111 its to say take the whole space
    
        subplot.pie(values, labels=names, autopct = "%1.0f%%")
        subplot.set_title("Progrès de l'utilisateur")
        canvas = FigureCanvasTkAgg(figure, master = self)
        canvas.draw() #connects the empty space with the graph
        return canvas
        
    def getGraph(self):
        return self.canvas
    def placeGraph(self,x,y):
        self.canvas.get_tk_widget().pack(padx= x, pady= y)
        
    '''
    cette classe va stocker les stats et en tirer de lobjet user. ainsi, elle gère la création du graphique
    nb of fish collected
    graph: circle to compare nb of fish and trash collected
    
    '''
class Fishing():
    def __init__(self,catch):
        '''
        one def for the attendez, one for the click one for the finish
        '''
        from classes_Émilie import Timer
        self.catch = catch # needs to be randomised before so you do fish(random choice of fish)
        self.clicks = None
        self.timerPassed= Timer(random.randint(0,100),0,0)
        self.timer = None
        self.win = False
        #updates the clicks and timer and prepares for stage 2 
        self.waiting()
        #stage 2 and forth will have to be manually done

    def waiting(self):
        newTime = self.timerPassed.timingWithoutPrint() # so the time passes
        if newTime.getIsFinished():
            pass
            #self.clicks = getrarity
            #self.timer = gettimer

    def reducingClicks(self):
        self.clicks = self.clicks - 1
    def checkFinalStatus(self):
        if self.timer.getIsFinished() == False and self.clicks == 0:
            return True
        if self.timer.getIsFinished() == True and self.clicks != 0:
            return False

    #getters
    def getNbClicks(self):
        return self.clicks
    def getTimer(self):
        return self.timer
    def getWinStatus(self):
        return self.win
    def getCatch(self):
        return self.catch
    def getTimePassedFirstStage(self):
        return self.timerPassed

#setter
    def setWinStatus(self, status):
        self.win = status
        
class ImageConfig():
    def __init__(self,fileLight,fileDark,x,y):
        
        temp = self.readFile(fileLight,fileDark)
        if temp is not None:
            self.fileLight,self.fileDark = temp
            self.x = x
            self.y = y
            self.myImg = self.createImage()

    def readFile(self,file1, file2): 
        try:
           Image.open(file1)
           Image.open(file2)
        except Exception as e:
            print(e)
            return None
                        
        return file1,file2
    def createImage(self):
        img = ctk.CTkImage(light_image=Image.open(self.fileLight),dark_image=Image.open(self.fileDark),size=(self.x,self.y))
        return img
    def getImage(self):
        return self.myImg

class GifImage(ctk.CTkFrame): #OPTIONELLE A REVOIR ET TESTER SI CA FONCTIONNE
    def __init__(self,master, file, x, y, width, height, wait):
        super().__init__(master)
        if self.checkFile(file) != None:
            self.file = file # cest comme si jai fait au fond self.file= file
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
        img = []

        for i in range(frames):
            openImg.seek(i)
            img.append(ctk.CTkImage(light_image= openImg.copy(), size=(self.width, self.height)))
        gifLabel = ctk.CTkLabel(self.master, text = "",width = self.width, height = self.height) # on revient avec ctk pour que ca soit compatible
        gifLabel.place(x = self.x, y = self.y) # ou le placer
                 
        def animation(count):
            newImg = img[count] # on commence avec ce frame precis
            gifLabel.configure(image = newImg) # on prend le label et on le transforme en img
            count += 1 # prochaine img

            if count == frames: # si on arrive a la fin
                count = 0 # on reset le compte pour qu'on puisse loop apres
            self.showAnim = self.master.after(self.wait, lambda: animation(count) ) # on attend self.wait de seconde avant de refaire la fonction: de plus lambda fais que la fct ne s'eexecute pas immediatement, et d'attendre jusqu'a ce que la condition soit satisfaite
        animation(0) # on fait demarer lanimation le zero cest le debut soit le count 0

#app = ctk.CTk()
#app.geometry("800x400")
#img1 = ImageConfig("assets/mainMenu.jpeg","assets/mainMenu.jpeg",800,400)
#my_label = ctk.CTkLabel(app, text="", image=img1.getImage())
#my_label.pack(pady=10)
#fishimg = GifImage(app,"assets/ocean.gif",150, 25, 100, 25, 50) # to fix the sizing
#app.mainloop()





#data1 = Data("assets/fishEncylopedia3.csv") #jsp honestly
#print(data1.getFishEncyclopedia())

#le lien du fichier ne fonctionne pas correctement, faut voir cest quoi le probleme avec le fichier
#wshhh