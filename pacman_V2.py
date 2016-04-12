from tkinter import *
import cartePM  #on importe un autre fichier python contenant les cartes.
import random

#Variable pour la mise en route du déplacement des fonctions
marche_fantome = False

#Position de Blinky (fantôme rouge)
posX1 = 24
posY1 = 32

#Position de Pinky (fantôme rose)
posX2 = 34
posY2 = 32

#Position de PacMan
posX = 29
posY = 48

dx = 0
dy = 0
dx2 = 0
dy2 = 0
dx3 = 0
dy3 = 0

"""L E S  F O N C T I O N S"""
def fantome_True():
    global marche_fantome
    marche_fantome = True
    canvasJ.after(200, update_fantomes)
    
def update_fantomes():
    global posX1, posY1, posX2, posY2

    #Condition qui permet de faire fonctionner notre fonction de déplacement automatique des fantômes lorsqu'on lance une partie
    #et qui s'annule quand on quitte le jeu
    if marche_fantome == True:
        #On génére un nombre entre 1 et 4 pour faire varier posX1 et posY1
        a = random.randint(1,4)
        if a == 1:
            posX1 += 1

        elif a == 2:
            posX1 -= 1

        elif a== 3:
            posY1 += 1
            
        else:
            posY1 -= 1

        #Meme chose pour posX2 et posY2
        b = random.randint(1,4)
        if b == 1:
            posX2 += 1

        elif b ==2:
            posX2 -= 1
            
        elif b== 3:
            posY2 += 1
            
        else:
            posY2 -= 1

                
                
        #On actualise les coordonnées des fantômes
        canvasJ.coords(blinky, posX1*10-9, posY1*10-9, posX1*10+19, posY1*10+19)
        canvasJ.coords(pinky, posX2*10-9, posY2*10-9, posX2*10+19, posY2*10+19)
    #Timer de Tkinter : toutes les 200ms on appelle la fonction "update_fantomes" qui fait appel à elle meme en plus des coordonées
    canvasJ.after(200, update_fantomes)
#Fonction de déplacement gérant les collisions avec murs + celles avec les pastilles, ainsi que les déplacements du pacman
def depl(event, pacman, carteJeu):

    
    
    touche = event.keysym
    
    global posX, posY, Points, dx, dy
    #les dx/dy sont des variables permettant de faire un test pour savoir si les coordonnées du pacman et celles des murs de la carte
    #se confondent, si ce n'est pas le cas, alors on fait varier les variables de positions du pacman suivant la touche pressée.
    if touche == "Up": #haut
        dx = 0
        dy = -1
        canvasJ.itemconfig(pacman, start = 135, extent = 270)
        
    elif touche == "Down": #bas
        dx = 0
        dy = 1
        canvasJ.itemconfig(pacman, start = -45, extent = 270)
    elif touche == "Left": #gauche
        dx = -1
        dy = 0
        canvasJ.itemconfig(pacman, start = 45, extent = 270)
    elif touche == "Right": # droite
        dx = 1
        dy = 0
        canvasJ.itemconfig(pacman, start = 225, extent = 270)


    canvasJ.addtag_closest('pacman', posX*10,posY*10, halo=5) # On tag l'objet 'pacman' sur le canvas -> il s'appelle 'pacman'
    canvasJ.delete('pacman')
  
    if carteJeu[posY+2*dy][posX+2*dx] == 0 and carteJeu[posY+2*dy+abs(dx)][posX+2*dx+abs(dy)] == 0 and carteJeu[posY+2*dy-abs(dx)][posX+2*dx-abs(dy)] == 0: # case vide 
            posY += dy
            posX += dx
    elif carteJeu[posY+2*dy][posX+2*dx] == 8:  #Changement de coté
        if dx == 1:
            posX = 3
        elif dx == -1:
            posX = 55
    elif carteJeu[posY+2*dy][posX+2*dx] == 9:  #La case est occupée par une pastille
        carteJeu[posY+2*dy][posX+2*dx] = 0  #On mange la pastille, la case devient vide
        
        canvasJ.addtag_closest('miam', (posX+2*dx)*10+5,(posY+2*dy)*10+5, halo=5)  #On tag l'objet 'pastille' sur le canvas -> il s'appelle 'miam'
        canvasJ.delete('miam')  #On supprime la pastille du canvas
        posY += dy
        posX += dx

    canvasJ.create_arc(posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19, fill = "yellow", start = (dy*90+abs(dy)*225)+(dx*90-abs(dx)*45), extent = 270) # on re affiche le pacman


 #Fonction pour créer la carte   
def makeMap(carteJeu):
    fantome_True()
    #Créer la carte choisie avec 2 boucles for à partir d'une liste de liste
    gameMenu_frame.grid_forget()
    game_frame.grid()
    
    for y in range(65):
        for x in range(59):
            if carteJeu[y][x]==1:
                canvasJ.create_rectangle(x*10, y*10, x*10+9, y*10+9, fill = "black", outline = "")


            elif carteJeu[y][x]==9:
                canvasJ.create_oval(x*10+3, y*10+3, x*10+7, y*10+7, fill = "yellow", outline = "")

   #On remet au premier plan les objets animés (pacman, fantômes)
    canvasJ.tag_raise(pacman)
    canvasJ.tag_raise(blinky)
    canvasJ.tag_raise(pinky)
    
def start_game():
    # app (Tk) contient trois enfants : nos 3 frames.
    # On appelle grid_forget sur les 3, puis on
    # appelle grid sur celle qu'on veut montrer
    menu_frame.grid_forget()
    gameMenu_frame.grid()
 
def show_rules():
    #On oublie la frame de menu pour appeler (grid) la frame du menu
    menu_frame.grid_forget()
    rules_frame.grid()
 
def show_menu():
    #On réinitialise les positions du pacman à chaque fois que cette fonction est appelée
    #Ainsi à chaque fois que l'utilisateur est en jeu et qu'il retourne à la fenêtre principale alors les positions se réinitialisent toutes et un nouvelle partie peut débuter
    global posX, posY, posX1, posY1, posX2, posY2, marche_fantome
    marche_fantome = False
    posX = 29
    posY = 48
    posX1 = 24
    posY1 = 32
    posX2 = 34
    posY2 = 32
    canvasJ.delete("all") #On supprime tous les objets : fantômes et pacman
    
    blinky = canvasJ.create_oval(posX1*10-9, posY1*10-9,posX1*10+19,posY1*10+19, fill = "red")
    pinky = canvasJ.create_oval(posX2*10-9, posY2*10-9, posX2*10+19, posY2*10+19, fill = "pink")
    for child in app.winfo_children():
        child.grid_forget()
    menu_frame.grid()


   

app = Tk()
app.geometry("800x650")
app.title("PAC MAN")




"""M E N U"""
menu_frame = Frame(app)
startB = Button(menu_frame, text='START', command=start_game)
regleB = Button(menu_frame, text='Règles', command=show_rules)
quitterB = Button(menu_frame, text = "Quitter", command = app.destroy)
startB.grid(row = 2, column = 2, ipady = 10)
regleB.grid(row = 4, column = 4, ipady = 10)
quitterB.grid(row = 5, column = 5, ipady = 10)



 
"""C H O I X  D E S  C A R T E S"""
#Frame pour le menu
gameMenu_frame = Frame(app, bg = "#172457")

#Bouton pour retourner au menu
return_btn = Button(gameMenu_frame, text='Retour au menu', command=show_menu)
return_btn.grid(row = 1, column = 3, ipady = 10)

#Bouton pour choisir la carte 1
bouCarte1 = Button(gameMenu_frame, text = "Carte 1", bd = 4, bg = "#BEBE15",  command = lambda carte1=cartePM.carte1: makeMap(cartePM.carte1))
bouCarte1.grid(pady = 10,ipady = 5, padx = 5,  row = 1, column = 1)

#Bouton pour choisir la carte 2
bouCarte2 = Button(gameMenu_frame, text = "Carte 2",bd = 4, bg = "#BEBE15",  command = lambda carte1=cartePM.carte2: makeMap(cartePM.carte2))
bouCarte2.grid(pady = 10, ipady = 5, padx = 5, row = 1, column = 2)



"""L E J E U"""
game_frame = Frame(app)

canvasJ = Canvas(game_frame, bg = "dark blue", width = 600, height = 650)
canvasJ.pack(side = LEFT)
canvasJ.focus_set()
canvasJ.bind("<Key>", lambda event: depl(event, pacman, cartePM.carte2))

#Bouton pour retourner au menu
return_btn = Button(game_frame, text='Retour au menu', command=show_menu, relief = "ridge")
return_btn.pack(ipady = 10, padx = 5)

#Création du pac man
pacman = canvasJ.create_arc(posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19, fill = "#BEBE15", start = 225, extent = 270)
    

#Création des fantomes
blinky = canvasJ.create_oval(posX1*10-9, posY1*10-9,posX1*10+19,posY1*10+19, fill = "red")

pinky = canvasJ.create_oval(posX2*10-9, posY2*10-9, posX2*10+19, posY2*10+19, fill = "pink")



#canvasJ.after(200, update_fantomes)


"""R E G L E S"""
rules_frame = Frame(app)
rules = Label(rules_frame, text="Blablabla regles blablabla")
rules.grid()
return_btn = Button(rules_frame, text='Retour au menu', command=show_menu)
return_btn.grid()

 
# Au début on commence par montrer le menu
menu_frame.grid()
app.mainloop()
