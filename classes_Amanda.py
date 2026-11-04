# Classes de Amanda
'''
Le fonctionnement des écrans est plutôt simple:
Il y a une classe qui s'occupe de l'écran principale et fait les changements de frame
Chaque frame est une classe, ce qui simplifie la programmation et la rend claire.

'''

import customtkinter as ctk
from classes_Émilie import User, Catch
from classe_khadija import ImageConfig, Data, GifImage

class TitleScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #image pour le background
        bg = ImageConfig(r"assets/mainMenu.jpeg",r"assets/mainMenu.jpeg", self.master.window_width,self.master.window_height)

        self.bg_label = ctk.CTkLabel(self, text = '', image = bg.getImage())
        self.bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        #Titre du jeu
        
        self.label = ctk.CTkLabel(self, text = "Fish le poisson", font = ("arial", 28, 'bold'))
        self.label.pack(pady = 40)

        #Bouton Jouer
        #Si le jeu a deja load ou non, va etre pour l'instant juste jouer
        if self.master.user.getUserName() is not None:
            self.play_btn = ctk.CTkButton(self, text = 'Continuer', command = self.on_play, corner_radius=0)

            self.new_play_btn = ctk.CTkButton(self, text = 'Nouvelle Partie', command = self.on_new_play, corner_radius=0, fg_color="#b12626")
            self.new_play_btn.pack(pady = 10)
        else:
            self.play_btn = ctk.CTkButton(self, text = 'Nouvelle Partie', command = self.on_new_play, corner_radius=0,fg_color="#b12626")

        self.play_btn.pack(pady = 10)

        #Bouton Charger
        self.load_btn = ctk.CTkButton(self, text = 'Charger', command = self.on_load, corner_radius=0)
        self.load_btn.pack(pady = 10)

        #Bouton Crédits
        self.credit_btn = ctk.CTkButton(self, text = 'Crédits', command = self.credit_frame, corner_radius=0)
        self.credit_btn.pack(pady = 10)

        #Bouton Charger
        self.quit_btn = ctk.CTkButton(self, text = 'Quitter', command = self.master.destroy, corner_radius=0)
        self.quit_btn.pack(pady = 10)

    def on_play(self):
        self.master.show_frame(GameScreen)
    def on_new_play(self):
        self.master.show_frame(newGameScreen)

    def on_load(self):
        print("Chargement de la sauvegarde")

    def credit_frame(self):
        self.master.show_frame(CreditScreen)

class newGameScreen(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        
        # Demande à l'utilisateur l'information requise
        self.label = ctk.CTkLabel(self,text="Veuillez entrer votre nom : ")
        self.label.pack(expand = True, pady = (0,40))
        self.entry = ctk.CTkEntry(self, placeholder_text= 'Écrire ici...')
        self.entry.pack(pady=10, expand = True)

        #Une fois prêt, l'utilisateur va aller à l'écran du jeu à l'aide d'un bouton
        self.button = ctk.CTkButton(self, text = 'Jouer', command=self.on_next)
        self.button.pack(pady = 10, expand = True)

    def on_next(self):
        #Initialise l'user
        self.master.user.setUserName(self.entry.get())
        #Lance l'écran de jeu
        if (self.entry.get() == '') or (self.entry.get() == None):
            self.label.configure(text = 'Veuillez entrer un nom valide')
        else:
            self.master.show_frame(GameScreen)

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
        self.main_container.grid_columnconfigure(1, weight=3) #centre
        self.main_container.grid_columnconfigure(2, weight=2) #droite
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
       self.back_btn.pack(padx = (10,0), side = 'right' )


       
       
    #####################################
    #Colonne gauche, joueur + inventaire#
    #####################################
    def create_left_panel(self):
        #Creation du l'écran de gauche
        self.left_panel = ctk.CTkFrame(self.main_container,fg_color="#9fb498")
        self.left_panel.grid(row = 0, column = 0, sticky = 'nsew', pady = 10, padx = 10)

        #--------------------------------------------
        #création du frame avec les info du joueur (nom, niveau, nmb de poissons)
        self.user_info_frame = ctk.CTkFrame(self.left_panel,fg_color="#dee6ed", height = 50)
        self.user_info_frame.pack(side = 'top', pady = (0,10), fill = 'x')
        #montre le nom du joueur
        self.user_name_label = ctk.CTkLabel(self.user_info_frame, text = self.master.user.getUserName(),font=("arial", 21, 'bold'))
        self.user_name_label.pack(pady = 10, side = 'left', padx = 20)
        #montre le niveau du joueur
        self.user_level_label = ctk.CTkLabel(self.user_info_frame, text = f'Niveau : {self.master.user.getUserLevel()}')
        self.user_level_label.pack(pady = 10,anchor = 'e', padx = 20)
        #montre le nmb de poissons attrape
        self.user_fish_label = ctk.CTkLabel(self.user_info_frame, text = f'Poissons : {self.master.user.getUserNbFish()}')
        self.user_fish_label.pack(pady = 10,anchor = 'e', padx = 20)

        #--------------------------------------------
        ##création du frame avec la ''librairie'' de tous les poissons qui est scrollable
        self.gallery_frame_scroll = ctk.CTkScrollableFrame(self.left_panel,fg_color="#dee6ed")
        self.gallery_frame_scroll.pack(side = 'top', pady = 5, fill = 'both', expand = True)
        self.gallery_frame_scroll.grid_columnconfigure(0,weight = 1)
        self.gallery_frame_scroll.grid_columnconfigure(1,weight = 1)

        
        current_row = 0
        current_column = 0

        self.gallery_dict = dict()
        for i in self.master.data.getFishNameList():
            path = f"assets/{i}.png"
            current_fish_image = ImageConfig(path,path,100,100)
            current_button = ctk.CTkButton(self.gallery_frame_scroll,
                                           image=current_fish_image.getImage(),
                                             command = lambda i=i: self.selected_fish(i),
                                             border_color ="#66ce7f", 
                                             border_width=0,
                                             text = '',
                                             fg_color="#dee6ed",
                                             height=100,width=100,
                                             hover_color="#fcf8f8",
                                             corner_radius=0)
            current_button.grid(pady = 5,padx = 5,
                                row = current_row, 
                                column = current_column)

            self.gallery_dict[i] = current_button

            if current_column == 0:
                current_column = 1
            else:
                current_column = 0
                current_row +=1

    





    ###############################################
    #Colonne milieu, etang, timer, lancer la ligne#
    ###############################################
    def create_center_panel(self):
        self.center_panel = ctk.CTkFrame(self.main_container,fg_color="#9fb498")
        self.center_panel.grid(row = 0, column = 1, sticky = 'nsew', pady = 5, padx = 5)

        ##header avec le nom de l'environnement
        header_label = ctk.CTkLabel(self.center_panel, 
                                    text= "Étang de pêche", 
                                    font=('ariel', 15, 'bold'), 
                                    fg_color= "#dee6ed",
                                    corner_radius=2)
        header_label.pack(fill = 'both',expand = True, pady = 10, padx = 15)

        #NE FONCTIONNE PAS POUR L'INSTANT
        ##le gif de l'environnement
        #environment_gif = GifImage(self.center_panel,"assets/ocean.gif", 100, 100, 5)
        #environment_gif.pack(pady = 5, padx = 5)
        path = r"assets\mainMenu.jpeg"
        environment_img = ImageConfig(path,path,360,360)
        environment_label = ctk.CTkLabel(self.center_panel, image=environment_img.getImage(),text = '')
        environment_label.pack()

        ##bouton de pêche
        self.fish_button = ctk.CTkButton(self.center_panel, 
                                         text = 'Lancer la ligne', 
                                         font = ('ariel',13, 'bold')
                                         )
        self.fish_button.pack(padx = 10, pady = 10,  expand = True, ipadx = 10, ipady = 10)


    #######################################
    #Colonne de droite, détails du poisson#
    #######################################
    def create_right_panel(self):
        self.right_panel = ctk.CTkFrame(self.main_container,fg_color="#dee6ed")
        self.right_panel.grid(row = 0, column = 2, sticky = 'nsew', pady = 10, padx = 10)

        label_selec = ctk.CTkLabel(self.right_panel, text = 'Sélection :')
        label_selec.pack(pady = 5)

        self.label_fish_name =ctk.CTkLabel(self.right_panel, text = "Aucun")
        self.label_fish_name.pack(pady = 5)

        fish_image = ImageConfig(r"assets/NoSelection.jpg",r"assets/NoSelection.jpg", 150,150)
        self.label_fish_image = ctk.CTkLabel(self.right_panel, 
                                             image=fish_image.getImage(), 
                                             height=150, width=150, 
                                             border_color='black', 
                                             border_width=2,
                                             text = '')
        self.label_fish_image.pack(pady = 5)

        self.label_rarity = ctk.CTkLabel(self.right_panel,text = 'N/A')
        self.label_rarity.pack(pady = 5)

        label_desc = ctk.CTkLabel(self.right_panel, text = 'Description')
        label_desc.pack(pady = 5)

        self.label_fish_desc = ctk.CTkLabel(self.right_panel,text = 'Aucun poisson de sélectionné!',wraplength = 180)
        self.label_fish_desc.pack(pady = 5)

        label_inventory = ctk.CTkLabel(self.right_panel,text = 'Inventaire :')
        label_inventory.pack(pady = 5,padx = 10, anchor = 'w')

        self.inventory_frame_scroll = ctk.CTkScrollableFrame(self.right_panel)
        self.inventory_frame_scroll.pack(pady=5, padx = 10, expand = True, fill = 'both')

        


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

    def selected_fish(self,fish_name):
            for i in self.gallery_dict.values():
                i.configure(border_width = 0)
            print(fish_name)
            #ajouter une bordure verte
            self.gallery_dict[fish_name].configure(border_width = 5)
            #modification du right panel
            self.modify_desc_fish(fish_name)
            #modification 
            #contenu inventaire
            self.modify_inventory_list(fish_name)
            
    def modify_desc_fish(self, fish_name):
        self.label_fish_name.configure(text = fish_name)

        list_fish = self.master.data.getFishSpecificStatsList(fish_name).copy()

        self.label_fish_desc.configure(text = list_fish[-2])

        self.label_rarity.configure(text = list_fish[-1])

        path = f"assets/{fish_name}.png"
        fish_image = ImageConfig(path,path, 150,150)
        self.label_fish_image.configure(image = fish_image.getImage())

    def modify_inventory_list(self, fish_name):

        #nettoie toute l'information qu'il y avait avant
        for widget in self.inventory_frame_scroll.winfo_children():
            widget.destroy()
        #on ajoute les bonnes informations (les poissons)
        for x in self.master.user.inventory:
                if x.name == fish_name:
                    label = ctk.CTkLabel(self.inventory_frame_scroll, text = f"• {x.size} cm, {x.weight} kg")
                    label.pack(pady = 5, padx = 10, anchor = 'w')

    def on_fishing(self):
        #Il existe 3 phases de la mécanique du jeu:

        #LANCER LA LIGNE#

        #genere un catch
        self.current_catch = Catch(self.master.data)
        #change le text pour montrer que le joueur est en attente d'un poisson
        self.fish_button.configure(text = "Patientez...", state = 'disabled')
        #on attend un certain moment
        wait_time = self.current_catch.
    
    


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

        self.window_width = 1000
        self.window_height = 600
        self.center_window()

        self.title("Fish le poisson")

        self.user = User()
        self.data = Data(r"assets/fishEncylopedia3.csv")
        
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
