from tkinter import *
import cartePM

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

"""L E S  F O N C T I O N S"""

#Fonction de déplacement gérant les collisions avec murs + celles avec les pastilles, ainsi que les déplacements du pacman
def depl(event, pacman, carteJeu):
    
    touche = event.keysym
    global posX, posY, Points, dx, dy
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
    elif carteJeu[posY+2*dy][posX+2*dx] == 8: # changement de coté
        if dx == 1:
            posX = 3
        elif dx == -1:
            posX = 55
    elif carteJeu[posY+2*dy][posX+2*dx] == 9: # La case est occupée par une pastille
        carteJeu[posY+2*dy][posX+2*dx] = 0 # On mange la pastille, la case devient vide
        
        canvasJ.addtag_closest('miam', (posX+2*dx)*10+5,(posY+2*dy)*10+5, halo=5) # On tag l'objet 'pastille' sur le canvas -> il s'appelle 'miam'
        canvasJ.delete('miam') # On supprime la pastille du canvas
        posY += dy
        posX += dx

    canvasJ.create_arc(posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19, fill = "yellow", start = (dy*90+abs(dy)*225)+(dx*90-abs(dx)*45), extent = 270) # on re affiche le pacman

   
"""        
def deplacement(event, canvas, pacman):
    global posX, posY
    touche = event.keysym
    print(touche)
    
    if touche == "Up":
        posY -=1
        canvas.itemconfig(pacman, start = 135, extent = 270)
    elif touche == "Down":
        posY += 1
        canvas.itemconfig(pacman, start = -45, extent = 270)
    elif touche == "Right":
        posX +=1
        canvas.itemconfig(pacman, start = 45, extent = 270)
    elif touche == "Left":
        posX -=1
        canvas.itemconfig(pacman, start = 225, extent = 270)

    canvas.coords(pacman,posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19)
"""

    
def makeMap(carteJeu):

    
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
    menu_frame.grid_forget()
    rules_frame.grid()
 
def show_menu():
    global posX, posY, posX1, posY1, posX2, posY2
    posX2 = 34
    posY2 = 32
    posX1 = 24
    posY1 = 32
    posX = 29
    posY = 48
    canvasJ.coords(pacman,posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19)
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
gameMenu_frame = Frame(app, bg = "#172457")
return_btn = Button(gameMenu_frame, text='Retour au menu', command=show_menu)
return_btn.grid(row = 1, column = 3, ipady = 10)

bouCarte1 = Button(gameMenu_frame, text = "Carte 1", bd = 4, bg = "#BEBE15",  command = lambda carte1=cartePM.carte1: makeMap(cartePM.carte1))
bouCarte1.grid(pady = 10,ipady = 5, padx = 5,  row = 1, column = 1)
      
bouCarte2 = Button(gameMenu_frame, text = "Carte 2",bd = 4, bg = "#BEBE15",  command = lambda carte1=cartePM.carte2: makeMap(cartePM.carte2))
bouCarte2.grid(pady = 10, ipady = 5, padx = 5, row = 1, column = 2)


"""L E J E U"""
game_frame = Frame(app)
canvasJ = Canvas(game_frame, bg = "dark blue", width = 600, height = 650)
canvasJ.pack(side = LEFT)
canvasJ.focus_set()
canvasJ.bind("<Key>", lambda event: depl(event, pacman, cartePM.carte2))
return_btn = Button(game_frame, text='Retour au menu', command=show_menu, relief = "ridge")
return_btn.pack(ipady = 10, padx = 5)
#Création du pac man
pacman = canvasJ.create_arc(posX*10-9, posY*10-9 ,posX*10+19 ,posY*10+19, fill = "#BEBE15", start = 225, extent = 270)
    

#Création des fantomes
blinky = canvasJ.create_oval(posX1*10-9, posY1*10-9,posX1*10+19,posY1*10+19, fill = "red")

pinky = canvasJ.create_oval(posX2*10-9, posY2*10-9, posX2*10+19, posY2*10+19, fill = "pink")





"""R E G L E S"""
rules_frame = Frame(app)
rules = Label(rules_frame, text="Blablabla regles blablabla")
rules.grid()
return_btn = Button(rules_frame, text='Retour au menu', command=show_menu)
return_btn.grid()

 
# Au début on commence par montrer le menu
menu_frame.grid()
app.mainloop()
