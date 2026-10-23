# Classes de Amanda
'''
Le fonctionnement des écrans est plutôt simple:
Il y a une classe qui s'occupe de l'écran principale et fait les changements de frame
Chaque frame est une classe, ce qui simplifie la programmation et la rend claire.

'''

import customtkinter as ctk
#from classe_khadija import data, savingSystem
#from classes_Émilie import User, Catch

class TitleScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #Titre du jeu
        self.label = ctk.CTkLabel(self, text = "Fish le poisson", font = ("arial", 28, 'bold'))
        self.label.pack(pady = 40)

        #Bouton Jouer
        #Si le jeu a deja load ou non, va etre pour l'instant juste jouer
        self.play_btn = ctk.CTkButton(self, text = 'Jouer', command = self.on_play)
        self.play_btn.pack(pady = 10)

        #Bouton Charger
        self.load_btn = ctk.CTkButton(self, text = 'Charger', command = self.on_load)
        self.load_btn.pack(pady = 10)

        #Bouton Crédits
        self.credit_btn = ctk.CTkButton(self, text = 'Crédits', command = self.credit_frame)
        self.credit_btn.pack(pady = 10)

        #Bouton Charger
        self.quit_btn = ctk.CTkButton(self, text = 'Quitter', command = self.master.destroy)
        self.quit_btn.pack(pady = 10)

    def on_play(self):
        pass
    #exemple: self.master.show_frame(GameScreen)

    def on_load(self):
        print("Chargement de la sauvegarde")

    def credit_frame(self):
        self.master.show_frame(CreditScreen)
    

class CreditScreen(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text = 'Crédits', font = ('ariel', 24, 'bold'))
        self.label.pack(pady = 30)

        self.names = ctk.CTkLabel(
            self, 
            text="Projet créé par :\n- Amanda\n- Khadija\n- Émilie", 
            font=("arial", 16)
        )
        self.names.pack(pady=20)

        # Bouton pour revenir au menu principal
        self.back_btn = ctk.CTkButton(self, text="Retour", command=self.back)
        self.back_btn.pack(pady=20)

    def back(self):
        self.master.show_frame(TitleScreen)




        


class MainApp(ctk.CTk):
    def __init__(self):
        #j'initialise mes attributs et je créer la fenêtre
        super().__init__()
        self.geometry('900x600')
        self.title("Fish le poisson")
        #self.data = Data()
        #self.user = User()
        self.current_frame = None
        self.show_frame(TitleScreen)

    def show_frame(self, frame_class):
        #Méthode pour changer d'écran facilement

        #si l'écran est toujours existant
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frame_class(master = self)
        self.current_frame.pack(expand = True, fill = 'both')


        

    