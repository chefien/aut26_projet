# Classes de Amanda

import customtkinter as ctk

class MainApp(ctk.CTk):
    def __init__(self):
        #j'initialise mes attributs et je créer la fenêtre
        super().__init__()
        self.geometry('1024x768')
        self.title("Fish le poisson")
        #self.data
        #self.user
    
    def title_screen(self):
        self.currentFrame = ctk.CTkFrame()
        self.currentFrame.pack(expend = True, fill = 'both')
        

    