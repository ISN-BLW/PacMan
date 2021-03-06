from tkinter import *
from tkinter.messagebox import * #On importe cette bibliothèque pour afficher un message d'avertissement
import cartePM  #On importe un autre fichier python contenant la carte.
import random   #On importe 

#Variable pour la mise en route du déplacement des fonctions
marche_fantome = False

#Position de Blinky (fantôme rouge)
posX1 = 15
posY1 = 42

#Position de Pinky (fantôme rose)
posX2 = 44
posY2 = 11

#Position de Verty (fantome vert)
posX3 = 44
posY3 = 42

#Position de Bleuy (fantome bleu)
posX4 = 14
posY4 = 12
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
dx3 = 0
dy3 = 0
dx4 = 0
dy4 = 0



#Variable pour le score, le temps et les vies
pointsScore = 0
pointsScore_aff = 0
timer = 120
vie_affiche = 3

"""L E S  F O N C T I O N S"""

#Fonction du timer
def timerJeu():
    global timer
    timer -= 1
    lbl_timer.config(text = "Temps Restant :\n" +str(timer))
    canvasJ.after(1000,timerJeu)

    if timer == 0:
        showinfo("ALERTE", "Vous avez perdu !\n")
        show_menu()
    
#Cette fonction permet d'initialiser la fonction de déplacement des fantômes.
def fantome_True():
    global marche_fantome
    marche_fantome = True
    canvasJ.after(100, update_fantomes)
    canvasJ.after(1000,timerJeu)

    
def update_fantomes():
    global posX1, posY1, posX2, posY2, posX3, posY3, posX4, posY4, dy2, dx2, dx3, dy3, dx4, dy4

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


        if cartePM.carte2[posY1+2*dy1][posX1+2*dx1] == 0 and cartePM.carte2[posY1+2*dy1+abs(dx1)][posX1+2*dx2+abs(dy1)] == 0 and cartePM.carte2[posY1+2*dy1-abs(dx1)][posX1+2*dx1-abs(dy1)] == 0 :   # case vide 
            posY1 += dy1
            posX1 += dx1
            
        elif cartePM.carte2[posY1+2*dy1][posX1+2*dx1] == 9:     
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
        
        elif cartePM.carte2[posY2+2*dy2][posX2+2*dx2] == 9:     
            posY2 += dy2
            posX2 += dx2

        #Pour posX3/posY3
        c = random.randint(1,4)
        if c == 1:
            dx3 = 1
            dy3 = 0
            

        elif c == 2:
            dx3 = -1
            dy3 = 0
            
        elif c == 3:
            dx3 = 0
            dy3 = 1
            
        else:
            dx3 = 0
            dy3 = -1
            
        if cartePM.carte2[posY3+2*dy3][posX3+2*dx3] == 0 and cartePM.carte2[posY3+2*dy3+abs(dx3)][posX3+2*dx3+abs(dy3)] == 0 and cartePM.carte2[posY3+2*dy3-abs(dx3)][posX3+2*dx3-abs(dy3)] == 0: # case vide 
            posY3 += dy3
            posX3 += dx3
        
        elif cartePM.carte2[posY3+2*dy3][posX3+2*dx3] == 9:     
            posY3 += dy3
            posX3 += dx3
        #Pour posX4/posY4
        d = random.randint(1,4)
        if d == 1:
            dx4 = 1
            dy4 = 0
            

        elif d == 2:
            dx4 = -1
            dy4 = 0
            
        elif d == 3:
            dx4 = 0
            dy4 = 1
            
        else:
            dx4 = 0
            dy4 = -1
            
        if cartePM.carte2[posY4+2*dy4][posX4+2*dx4] == 0 and cartePM.carte2[posY4+2*dy4+abs(dx4)][posX4+2*dx4+abs(dy4)] == 0 and cartePM.carte2[posY4+2*dy4-abs(dx4)][posX4+2*dx4-abs(dy4)] == 0: # case vide 
            posY4 += dy4
            posX4 += dx4
        
        elif cartePM.carte2[posY4+2*dy4][posX4+2*dx4] == 9:     
            posY4 += dy4
            posX4 += dx4
        #On actualise les coordonnées des fantômes
        canvasJ.coords(blinky, posX1*10-9, posY1*10-9, posX1*10+19, posY1*10+19)
        canvasJ.coords(pinky, posX2*10-9, posY2*10-9, posX2*10+19, posY2*10+19)
        canvasJ.coords(verty, posX3*10-9, posY3*10-9, posX3*10+19, posY3*10+19)
        canvasJ.coords(bleuy, posX4*10-9, posY4*10-9, posX4*10+19, posY4*10+19)

    #On rajoute cette condition pour faire en sorte que si on retourne au menu, cette fonction se réinitialise.
    #De ce fait, à chaque fois qu'on relance le jeu, cette fonction s'execute comme si c'etait la premiere fois qu'on l'a lancé.    
    elif marche_fantome == False:
        return

    
    #Timer de Tkinter : toutes les 200ms on appelle la fonction "update_fantomes" qui fait appel à elle meme en plus des coordonées
    canvasJ.after(100, update_fantomes)
    
#Fonction de déplacement gérant les collisions avec murs + celles avec les pastilles, ainsi que les déplacements du pacman
def depl(event, pacman, carteJeu):
    global pointsScore, pointsScore_aff, posX, posY, Points, dx, dy, vie_affiche

    
    touche = event.keysym
    #A chaque déplacement du pacman, on créé un rectangle bleu pour cacher les pacgommes
    canvasJ.create_rectangle(posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19, fill = "dark blue", outline = "")
    #Puis on remet au premier plan le pacman et les fantomes
    canvasJ.tag_raise(pacman)
    canvasJ.tag_raise(pinky)
    canvasJ.tag_raise(blinky)
    canvasJ.tag_raise(bleuy)
    canvasJ.tag_raise(verty)

    #les dx/dy sont des variables permettant de faire un test pour savoir si les coordonnées du pacman et celles des murs de la carte
    #se confondent, si ce n'est pas le cas, alors on fait varier les variables de positions du pacman suivant la touche pressée.
    if touche == "Up": #Haut
        dx = 0
        dy = -1
        #On repositionne le pacman en fonction du mouvement 
        canvasJ.itemconfig(pacman, start = 135, extent = 270)
        
    elif touche == "Down": #Bas
        dx = 0
        dy = 1
         #On repositionne le pacman en fonction du mouvement 
        canvasJ.itemconfig(pacman, start = -45, extent = 270)
    elif touche == "Left": #Gauche
        dx = -1
        dy = 0
        #On repositionne le pacman en fonction du mouvement 
        canvasJ.itemconfig(pacman, start = 225, extent = 270)
    elif touche == "Right": #Droite
        dx = 1
        dy = 0
        #On repositionne le pacman en fonction du mouvement 
        canvasJ.itemconfig(pacman, start = 45, extent = 270)

    

  
    if carteJeu[posY+2*dy][posX+2*dx] == 0 and carteJeu[posY+2*dy+abs(dx)][posX+2*dx+abs(dy)] == 0 and carteJeu[posY+2*dy-abs(dx)][posX+2*dx-abs(dy)] == 0: # case vide 
            posY += dy
            posX += dx
    elif carteJeu[posY+2*dy][posX+2*dx] == 8:  #Changement de coté
        if dx == 1:
            posX = 3
        elif dx == -1:
            posX = 55
    elif carteJeu[posY+2*dy][posX+2*dx] == 9:  #La case est occupée par une pastille
        #On determine cette case comme étant une case vide
        carteJeu[posY+2*dy][posX+2*dx] = 0  
        pointsScore_aff += 10
        pointsScore += 10
        lbl_Score.config(text = "P.O.I.N.T.S\n" + str(pointsScore_aff))

       
        posY += dy
        posX += dx


    
    canvasJ.coords(pacman,posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19)

    #Si les positions du pacman sont les memes que celles d'un fantome alors on enleve 200 points et on remet le pacman à ses coordonnées de base
    if posX == posX2 and posY == posY2 or posX == posX1 and posY == posY1 or posX == posX3 and posY == posY3 or posX == posX4 and posY == posY4:
        posY = 48
        posX = 29
        pointsScore_aff -= 200
        lbl_Score.config(text = "P.O.I.N.T.S\n" + str(pointsScore_aff))
        canvasJ.coords(pacman,posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19)
    #systeme de vie
     
        vie_affiche -= 1
        lbl_vie.config(text = "vie\n" + str(vie_affiche))
        
    if vie_affiche == 0 :
        showinfo("ALERTE", "Vous avez perdue!\n")
        app.destroy()
        


        
    if pointsScore == 24000: #242 pastilles au total

       #on affiche un message pour alerter le joueur de sa victoire et on le fait revenir au menu du jeu
        showinfo("ALERTE", "Vous avez gagné !\n\n     Bien joué !")
        app.destroy()
    
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
    canvasJ.tag_raise(verty)
    canvasJ.tag_raise(bleuy)
    
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
    global posX, posY, posX1, posY1, posX2, posY2, posX3, posY3, posX4, posY4, marche_fantome, pointsScore, pointsScore_aff
    marche_fantome = False
    posX = 29
    posY = 48
    posX1 = 14
    posY1 = 43
    posX2 = 43
    posY2 = 14
    posX3 = 44
    posY3 = 42
    posX4 = 14
    posY4 = 12
    pointsScore = 0
    pointsScore_aff = 0

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
startB = Button(boxM, text='Jouer', command=start_game, relief = GROOVE)
regleB = Button(boxM, text='Règles', command=show_rules, relief = GROOVE)
quitterB = Button(boxM, text = "Quitter", command = app.destroy, relief = GROOVE)
startB.pack(ipady = 15, ipadx = 15, pady = 15, padx = 15)
regleB.pack(ipady = 15, ipadx = 15, pady = 15, padx = 15)
quitterB.pack(ipady = 15, ipadx = 15, pady = 15, padx = 15)



 
"""C H O I X  D E  L A  C A R T E"""
#Frame pour le menu
gameMenu_frame = Frame(app, bg = "#2EA4BA")
boxGM = Frame(gameMenu_frame, bg = "#017F97")
boxGM.pack(padx = 300, pady = 150)

#Bouton pour choisir la carte 
bouCarte = Button(boxGM, text = "Carte",bd = 4, command = lambda carte1=cartePM.carte2: makeMap(cartePM.carte2))
bouCarte.pack(ipady = 20, ipadx = 20, pady = 50, padx = 50)

#Bouton pour retourner au menu
return_btn = Button(boxGM, text='Retour au menu', command=show_menu, relief = GROOVE)
return_btn.pack(ipady = 10, pady =20)







"""L E J E U"""
game_frame = Frame(app, bg = "#2EA4BA")

canvasJ = Canvas(game_frame, bg = "dark blue", width = 600, height = 650)
canvasJ.pack(side = LEFT)
canvasJ.focus_set()
canvasJ.bind("<Key>", lambda event: depl(event, pacman, cartePM.carte2))

#Bouton pour retourner au menu
return_btn = Button(game_frame, text='Quitter', command=app.destroy, relief = "ridge")
return_btn.pack(ipady = 10, ipadx = 10, padx = 5, pady = 20)

#Création du pac man
pacman = canvasJ.create_arc(posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19, fill = "yellow", start = 225, extent = 270)
    

#Création des fantomes
blinky = canvasJ.create_oval(posX1*10-9, posY1*10-9,posX1*10+19,posY1*10+19, fill = "red")

pinky = canvasJ.create_oval(posX2*10-9, posY2*10-9, posX2*10+19, posY2*10+19, fill = "pink")

verty = canvasJ.create_oval(posX3*10-9, posY3*10-9, posX3*10+19, posY3*10+19, fill = "green")

bleuy = canvasJ.create_oval(posX4*10-9, posY4*10-9, posX4*10+19, posY4*10+19, fill = "cyan")
#Label affichant le score
lbl_Score = Label(game_frame, text = "P.O.I.N.T.S\n" + str(pointsScore), font = "Courier 20 bold", bg = "#017F97", fg = "white")
lbl_Score.pack(pady = 50, padx = 10)                         

lbl_timer = Label(game_frame, text = "Temps Restant :\n" +str(timer),  font = "Courier 12 bold", bg = "#017F97", fg = "white")
lbl_timer.pack(pady = 50, padx = 10)


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

#Label affichant les vie
lbl_vie = Label(game_frame, text = "vie\n" + str(vie_affiche), font = "Courier 20 bold", bg = "#017F97", fg = "white")
lbl_vie.pack(pady = 60, padx = 20)

 
# Au début on commence par montrer le menu
menu_frame.grid(ipady = 150)
app.mainloop()
