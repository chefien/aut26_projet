#classe de khadija: Data(), Fishing(), load(), save(), csv files + folder for assetz
import pandas as pd

class data():
    def __init__(self,file):
        self.file = str(file) #file lien/nom
        self.readFile() #executer immediatement la fct 

    def readFile(self): #transporter le csv à un dataFrame
        df = pd.read_csv(self.file)
        display(df)


# data1 = data("assets/fishEncyclopedia(Sheet1).csv")
