from tkinter import *
from tkinter.messagebox import * #On importe cette bibliothèque pour afficher un message d'avertissement
import cartePM  #On importe un autre fichier python contenant la carte.
import random   #On importe 

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

#Différentes variables permettant d'effectuer une verification des positions sur la carte du pacman et des fantômes.
dx = 0
dy = 0
dx1 = 0
dy1 = 0
dx2 = 0
dy2 = 0



#Variable pour le score
pointsScore = 0


"""L E S  F O N C T I O N S"""

#Cette fonction permet d'initialiser la fonction de déplacement des fantômes.
def fantome_True():
    global marche_fantome
    marche_fantome = True
    canvasJ.after(200, update_fantomes)


    
def update_fantomes():
    global posX1, posY1, posX2, posY2, dy2, dx2

    #Condition qui permet de faire fonctionner notre fonction de déplacement automatique des fantômes lorsqu'on lance une partie
    #et qui s'annule quand on quitte le jeu
    if marche_fantome == True:
        #On génére un nombre entre 1 et 4 pour faire varier posX1 et posY1
        a = random.randint(1,4)
        if a == 1:
            dx1 = 1
            dy1 = 0
        elif a == 2:
            dx1 = -1
            dy1 = 0

        elif a== 3:
            dx1 = 0
            dy1 = 1
            
        else:
            dx1 = 0
            dy1 = -1


        if cartePM.carte2[posY1+2*dy1][posX1+2*dx1] == 0 and cartePM.carte2[posY1+2*dy1+abs(dx1)][posX1+2*dx2+abs(dy1)] == 0 and cartePM.carte2[posY1+2*dy1-abs(dx1)][posX1+2*dx1-abs(dy1)] == 0: # case vide 
            posY1 += dy1
            posX1 += dx1
        #Meme chose pour posX2 et posY2
        b = random.randint(1,4)
        if b == 1:
            dx2 = 1
            dy2 = 0

        elif b ==2:
            dx2 = -1
            dy2 = 0
            
        elif b== 3:
            dx2 = 0
            dy2 = 1
            
        else:
            dx2 = 0
            dy2 = -1
            
        if cartePM.carte2[posY2+2*dy2][posX2+2*dx2] == 0 and cartePM.carte2[posY2+2*dy2+abs(dx2)][posX2+2*dx2+abs(dy2)] == 0 and cartePM.carte2[posY2+2*dy2-abs(dx2)][posX2+2*dx2-abs(dy2)] == 0: # case vide 
            posY2 += dy2
            posX2 += dx2

        elif cartePM.carte2[posY2+2*dy2][posX2+2*dx2] == 0 and cartePM.carte2[posY2+2*dy2+abs(dx2)][posX2+2*dx2+abs(dy2)] == 0 and cartePM.carte2[posY2+2*dy2-abs(dx2)][posX2+2*dx2-abs(dy2)] == 1 and dx2 == 1:
            posY2 += 1
      

        elif cartePM.carte2[posY2+2*dy2][posX2+2*dx2] == 0 and cartePM.carte2[posY2+2*dy2+abs(dx2)][posX2+2*dx2+abs(dy2)] == 0 and cartePM.carte2[posY2+2*dy2-abs(dx2)][posX2+2*dx2-abs(dy2)] == 1 and dx2 == -1:
            posY2 -= 1
     
            
        elif cartePM.carte2[posY2+2*dy2][posX2+2*dx2] == 0 and cartePM.carte2[posY2+2*dy2+abs(dx2)][posX2+2*dx2+abs(dy2)] == 0 and cartePM.carte2[posY2+2*dy2-abs(dx2)][posX2+2*dx2-abs(dy2)] == 1 and dy2 == -1:
            posX2 += 1
         
            
        elif cartePM.carte2[posY2+2*dy2][posX2+2*dx2] == 0 and cartePM.carte2[posY2+2*dy2+abs(dx2)][posX2+2*dx2+abs(dy2)] == 0 and cartePM.carte2[posY2+2*dy2-abs(dx2)][posX2+2*dx2-abs(dy2)] == 1 and dy2 == 1:
            posX2 -= 1
          
            
    
                
        #On actualise les coordonnées des fantômes
        canvasJ.coords(blinky, posX1*10-9, posY1*10-9, posX1*10+19, posY1*10+19)
        canvasJ.coords(pinky, posX2*10-9, posY2*10-9, posX2*10+19, posY2*10+19)

    #On rajoute cette condition pour faire en sorte que si on retourne au menu, cette fonction se réinitialise. De ce fait, à chaque fois qu'on relance le jeu, cette fonction s'execute comme si c'etait la premiere fois qu'on l'a lancé.    
    elif marche_fantome == False:
        return

    
    #Timer de Tkinter : toutes les 200ms on appelle la fonction "update_fantomes" qui fait appel à elle meme en plus des coordonées
    canvasJ.after(200, update_fantomes)
    
#Fonction de déplacement gérant les collisions avec murs + celles avec les pastilles, ainsi que les déplacements du pacman
def depl(event, pacman, carteJeu):
    global pointsScore
    
    
    touche = event.keysym
    
    global posX, posY, Points, dx, dy
    #les dx/dy sont des variables permettant de faire un test pour savoir si les coordonnées du pacman et celles des murs de la carte
    #se confondent, si ce n'est pas le cas, alors on fait varier les variables de positions du pacman suivant la touche pressée.
    if touche == "Up": #Haut
        dx = 0
        dy = -1
        canvasJ.itemconfig(pacman, start = 135, extent = 270)
        
    elif touche == "Down": #Bas
        dx = 0
        dy = 1
        canvasJ.itemconfig(pacman, start = -45, extent = 270)
    elif touche == "Left": #Gauche
        dx = -1
        dy = 0
        canvasJ.itemconfig(pacman, start = 225, extent = 270)
    elif touche == "Right": #Droite
        dx = 1
        dy = 0
        canvasJ.itemconfig(pacman, start = 45, extent = 270)

    canvasJ.coords(pacman,posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19)
    
    #canvasJ.addtag_closest('pacman', posX*10,posY*10, halo=5) # On tag l'objet 'pacman' sur le canvas -> il s'appelle 'pacman'
    #canvasJ.delete('pacman')
  
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
        pointsScore += 10
        lbl_Score.config(text = "P.O.I.N.T.S\n" + str(pointsScore))
        
        canvasJ.addtag_closest('miam', (posX+2*dx)*10+5,(posY+2*dy)*10+5, halo=5)  #On tag l'objet 'pastille' sur le canvas -> il s'appelle 'miam'
        canvasJ.delete('miam')  #On supprime la pastille du canvas
        posY += dy
        posX += dx

    #canvasJ.create_arc(posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19, fill = "yellow", start = (dy*90+abs(dy)*225)+(dx*90-abs(dx)*45), extent = 270) # on re affiche le pacman

    if posX == posX2 and posY == posY2:
        posY = 48
        posX = 29
        pointsScore -= 200
        canvasJ.coords(pacman,posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19)
    if pointsScore == 2460: #246 points au total
       #on affiche un message pour alerter le joueur de sa victoire et on le fait revenir au menu du jeu
        showinfo("ALERTE", "Vous avez gagné !")
        show_menu()


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
    gameMenu_frame.grid(ipadx = 30, ipady = 150)
 
def show_rules():
    #On oublie la frame de menu pour appeler (grid) la frame du menu
    menu_frame.grid_forget()
    rules_frame.grid(ipady = 150)
 
def show_menu():
    
    #On réinitialise les positions du pacman à chaque fois que cette fonction est appelée
    #Ainsi à chaque fois que l'utilisateur est en jeu et qu'il retourne à la fenêtre principale alors les positions se réinitialisent toutes et un nouvelle partie peut débuter
    #On réinitialise également le score
    global posX, posY, posX1, posY1, posX2, posY2, marche_fantome, pointsScore
    marche_fantome = False
    posX = 29
    posY = 48
    posX1 = 24
    posY1 = 32
    posX2 = 34
    posY2 = 32
    pointsScore = 0

    lbl_Score.config(text = "P.O.I.N.T.S\n" + str(pointsScore))
    
    
    canvasJ.coords(blinky, posX1*10-9, posY1*10-9, posX1*10+19, posY1*10+19)
    canvasJ.coords(pinky, posX2*10-9, posY2*10-9, posX2*10+19, posY2*10+19)
    canvasJ.coords(pacman, posX*10-9, posY*10-9, posX*10+19, posY*10+19)
    #On oublie la frame active pour retourner au menu
    for child in app.winfo_children():
        child.grid_forget()
    menu_frame.grid(ipady = 150)


#Variable des dimensions de notre fenêtre
L = 800
H = 650 

app = Tk()
#On empêche l'utilisateur de redimensionner la fenêtre par soucis
app.resizable(width=FALSE, height=FALSE)
#On ajuste le positionnement de la fenêtre pour qu'elle soit au mileu de l'ecran
app.geometry("%dx%d%+d%+d" % (L,H,(app.winfo_screenwidth()-L)//2,(app.winfo_screenheight()-H)//2))
app.title("PAC MAN")




"""M E N U"""
menu_frame = Frame(app, bg = "#2EA4BA")
boxM = Frame(menu_frame, bg = "#017F97")
boxM.pack(padx = 350, pady = 150)
startB = Button(boxM, text='START', command=start_game, relief = GROOVE)
regleB = Button(boxM, text='Règles', command=show_rules, relief = GROOVE)
quitterB = Button(boxM, text = "Quitter", command = app.destroy, relief = GROOVE)
startB.pack(ipady = 15, ipadx = 15, pady = 15, padx = 15)
regleB.pack(ipady = 15, ipadx = 15, pady = 15, padx = 15)
quitterB.pack(ipady = 15, ipadx = 15, pady = 15, padx = 15)



 
"""C H O I X  D E  L A  C A R T E"""
#Frame pour le menu
gameMenu_frame = Frame(app, bg = "#2EA4BA ")
boxGM = Frame(gameMenu_frame, bg = "#017F97 ")
boxGM.pack(padx = 300, pady = 150)

#Bouton pour choisir la carte 
bouCarte2 = Button(boxGM, text = "Carte",bd = 4, command = lambda carte1=cartePM.carte2: makeMap(cartePM.carte2))
bouCarte2.pack(ipady = 20, ipadx = 20, pady = 50, padx = 50)

#Bouton pour retourner au menu
return_btn = Button(boxGM, text='Retour au menu', command=show_menu, relief = GROOVE)
return_btn.pack(ipady = 10, pady =20)

#Bouton pour choisir la carte 1
#bouCarte1 = Button(gameMenu_frame, text = "Carte 1", bd = 4, bg = "#BEBE15",  command = lambda carte1=cartePM.carte1: makeMap(cartePM.carte1))
#bouCarte1.grid(pady = 10,ipady = 5, padx = 5,  row = 1, column = 1)





"""L E J E U"""
game_frame = Frame(app, bg = "#2EA4BA")

canvasJ = Canvas(game_frame, bg = "dark blue", width = 600, height = 650)
canvasJ.pack(side = LEFT)
canvasJ.focus_set()
canvasJ.bind("<Key>", lambda event: depl(event, pacman, cartePM.carte2))

#Bouton pour retourner au menu
return_btn = Button(game_frame, text='Retour au menu', command=show_menu, relief = "ridge")
return_btn.pack(ipady = 10, ipadx = 10, padx = 5, pady = 20)

#Création du pac man
pacman = canvasJ.create_arc(posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19, fill = "yellow", start = 225, extent = 270)
    

#Création des fantomes
blinky = canvasJ.create_oval(posX1*10-9, posY1*10-9,posX1*10+19,posY1*10+19, fill = "red")

pinky = canvasJ.create_oval(posX2*10-9, posY2*10-9, posX2*10+19, posY2*10+19, fill = "pink")

#Label affichant le score
lbl_Score = Label(game_frame, text = "P.O.I.N.T.S\n" + str(pointsScore), font = "Courier 20 bold", bg = "#017F97", fg = "white")
lbl_Score.pack(pady = 50, padx = 10)                         

if pointsScore == 20:
    print("Wonja va récuperer ces bananes")


"""R E G L E S"""
rules_frame = Frame(app, bg = "#2EA4BA")
boxR = Frame(rules_frame)
boxR.pack(padx = 175, pady = 150)
rules = Label(boxR, text="Le jeu commence en cliquant sur l'ecran de jeu.\n"
              "Le but du jeu est de collecter tous les points dans le niveau.\n"
              "Pendant ce temps on est suivi par plusieurs fantômes qui ne doivent pas nous toucher.\n\n"
              "Pacman est déplacé grâce aux touches flèche.\n"
              "Partout où il passe, il mange les points jaunes.\n"
              "Lorsque tous les points ont été mangés, le niveau est terminé.\n"
              "Une rencontre avec un des fantômes réinitialise la position du pacman. \n", bg = "#017F97", fg = "white")
rules.grid()
return_btn = Button(rules_frame, text='Retour au menu', command=show_menu, relief = GROOVE)
return_btn.pack(ipady = 5, ipadx = 5, pady = 10)

 
# Au début on commence par montrer le menu
menu_frame.grid(ipady = 150)
app.mainloop()
