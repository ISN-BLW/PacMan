from tkinter import *

posX = 300
posY = 300


def p(event, canvas, pacman):
    global posX, posY
    touche = event.keysym
    print(touche)
    
    if touche == "Up":
        posY -=20

    elif touche == "Down":
        posY += 20
       
    elif touche == "Right":
        posX +=20
       
    elif touche == "Left":
        posX -=20
       

    canvas.coords(pacman,posX+20,posY+20,posX-20,posY-20)
def carte(canvas):
    global posX, posY

    #Liste de listes représantant la carte en 2D
    #0 = MURS
    #1 = CHEMIN
    #4 = PACGOMME
    #Carte à refaire pour que les chemins aient une largeur de 3 afin que
    #les pacgommes puissent etre mises au milieu du chemin
    carte =[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
               [0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0],
               [0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0],
               [0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0],
               [0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0],
               [0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0],
               [0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0],
               [0,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,0,0],
               [0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0],
               [0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
               [0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0],
               [0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0],
               [0,0,1,1,1,1,0,0,1,1,0,0,1,4,0,0,4,1,0,0,1,1,0,0,1,1,1,1,0,0],
               [0,0,1,1,1,1,0,0,1,1,0,0,1,4,0,0,4,1,0,0,1,1,0,0,1,1,1,1,0,0],
               [0,0,0,0,1,1,0,0,1,1,0,0,1,4,0,0,4,1,0,0,1,1,0,0,1,1,0,0,0,0],
               [0,0,0,0,1,1,0,0,1,1,0,0,1,4,0,0,4,1,0,0,1,1,0,0,1,1,0,0,0,0],
               [0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0],
               [0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0],
               [0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0],
               [0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


    #Création de la carte à l'aide de 2 boucles "for"
    for y in range(30):
        for x in range(30):
            if carte[y][x]==0:
                canvas.create_rectangle(x*20, y*20, x*20+20, y*20 +20, fill = "black", outline = "")


            elif carte[y][x]==4:
                canvas.create_oval(x*20, y*20, x*20+5, y*20+5, fill = "yellow", outline = "")


    
#Fenetre fill pour les règles
def regles():
    top2 = Toplevel(fen)
    top2.focus_set()
    top2.title("Règles")
    top2.geometry("500x500")
    label = Label(top2, text ="Pacman regles etc etc")
    label.pack()

    quitterB = Button(top2, text = "Quitter", command = top2.destroy)
    quitterB.pack()
    
#Fenetre fille pour jouer
def jouer():
    top1 = Toplevel(fen)
    top1.title("C'est Parti !")
    top1.geometry("700x600")

    canvas = Canvas(top1,bg = "dark blue", width = 600, height = 600)
    canvas.pack(side = LEFT)
    canvas.focus_set()

    #Pour le binding, nous devons mettre plusieurs arguments pour la fonction,
    #on utilise donc "lamba", une fonction qui enveloppe la fonction de déplacement
    canvas.bind("<Key>", lambda event :p(event, canvas, pacman))
    carte(canvas)

    #Création du pac man
    pacman = canvas.create_arc(posX+20,posY+20,posX-20,posY-20, fill = "yellow", start = 225, extent = 270)
    

    quitterB = Button(top1, text = "Quitter", command = top1.destroy)
    quitterB.pack()

#Fenetre Principale
fen = Tk()
fen.title("PAC MAN")
fen.geometry("250x150")
#Bouton appelant la fonction "jouer" qui créer une fenetre fille 
gameB = Button(fen,bg = "light blue", text = "Jouer", command = jouer)
gameB.pack(fill = X,pady = 10)

regleB = Button(fen, bg = "light green", text = "Règles", command = regles)
regleB.pack(fill = X, pady = 10)

quitterB = Button(fen, bg = "#499371", text = "Quitter", command = fen.destroy)
quitterB.pack(fill = X, pady = 10)

fen.mainloop()
