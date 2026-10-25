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
        self.master.show_frame(GameScreen)
    #exemple: self.master.show_frame(GameScreen)

    def on_load(self):
        print("Chargement de la sauvegarde")

    def credit_frame(self):
        self.master.show_frame(CreditScreen)

class GameScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Création du la barre d'en haut (menu)
        self.create_top_bar()

        # Le frame qui contient les trois colonnes
        self.main_container = ctk.CTkFrame(self, fg_color="#9fb498")
        self.main_container.pack(expand=True, fill="both", padx=10, pady=5)

        # confugaration des colonnes
        self.main_container.grid_columnconfigure(0, weight=2) #gauche
        self.main_container.grid_columnconfigure(1, weight=4) #centre
        self.main_container.grid_columnconfigure(2, weight=1) #droite
        self.main_container.grid_rowconfigure(0, weight=1)

        # création des 3 sections
        self.create_left_panel()
        self.create_center_panel()
        self.create_right_panel()
        

    ############################
    # La barre d'en haut (menu)#
    ############################
    def create_top_bar(self):
       self.top_menu = ctk.CTkFrame(self, bg_color = 'transparent')
       self.top_menu.pack(side="top", fill="x", padx=10, pady=(10, 5))

       ####Boutons#####

        #Bouton sauvegarder
       self.save_btn = ctk.CTkButton(self.top_menu, text = 'Sauvegarder', command = self.on_save)
       self.save_btn.pack(padx = (0,10), side = 'left')

        #Bouton Charger
       self.load_btn = ctk.CTkButton(self.top_menu, text = 'Charger', command = self.on_load)
       self.load_btn.pack(padx = 10, side = 'left')

        #Bouton Stats
       self.stats_btn = ctk.CTkButton(self.top_menu, text = 'Statistiques du jeu', command = self.on_stats)
       self.stats_btn.pack(padx = 10, side = 'left')

       #Bouton retour
       self.back_btn = ctk.CTkButton(self.top_menu, text = 'Retourner au menu principal', command = self.on_return)
       self.back_btn.pack(padx = 10, side = 'left' )

        #Bouton Quitter
       self.quit_btn = ctk.CTkButton(
           self.top_menu, 
           text='✕', 
           width=30,        
           height=30, 
           command = self.master.destroy, 
           fg_color='red'
           )
       self.quit_btn.pack(padx = (10,0), side = 'right')

       
       
    #####################################
    #Colonne gauche, joueur + inventaire#
    #####################################
    def create_left_panel(self):
        pass

    ###############################################
    #Colonne milieu, etang, timer, lancer la ligne#
    ###############################################
    def create_center_panel(self):
        pass

    #######################################
    #Colonne de droite, détails du poisson#
    #######################################
    def create_right_panel(self):
        pass

    #######################
    #Commandes des boutons#
    #######################
    def on_load(self):
        print("Bouton charger cliqué")

    def on_save(self):
        print("Bouton sauvegarder cliqué")

    def on_options(self):
        print("Bouton options cliqué")

    def on_stats(self):
        print("Bouton stats cliqué")

    def on_return(self):
        # Revient à l'écran titre
        self.master.show_frame(TitleScreen)

    def on_cast_line(self):
        print("Lancer la ligne cliqué! (timer d'Émilie)")
    


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

        self.window_width = 900
        self.window_height = 600
        self.center_window()

        self.title("Fish le poisson")
        #Enlever la barre de windows afin d'enelver le x
        self.overrideredirect(True)
        #self.data = Data()
        #self.user = User()
        self.current_frame = None
        self.show_frame(TitleScreen)

    def center_window(self):
        #permet que la fenêtre se trouve exactement au milieu de l'écran

        #taille de l'écran de l'utilisateur
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        #trouver les coordos de la position du centre de l'écran
        x = int((screen_width-self.window_width)/2)
        y = int((screen_height-self.window_height)/2)

        #on créer le fenetre avec les bonnes informations!
        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")


    def show_frame(self, frame_class):
        #Méthode pour changer d'écran facilement

        #si l'écran est toujours existant
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frame_class(master = self)
        self.current_frame.pack(expand = True, fill = 'both')


        

    ##temp
app = MainApp()
if __name__ == "__main__":
    app.mainloop()
