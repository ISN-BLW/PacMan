from tkinter import *
import threading
import random
a = 0
posX1 = 30
posY1 = 30
def zer(canvas, blinky):
    global posX1, posY1, a
    threading.Timer(0.25,zer,[canvas,blinky]).start()

    
    if a ==0:    
        canvas.coords(blinky, posX1*10-9, posY1*10-9,posX1*10+19,posY1*10+19)
        canvas.itemconfig(blinky, fill="blue", start = 225, extent = 270, outline = "")
        
        a = 1
    elif a == 1:
        canvas.coords(blinky, posX1*10-9, posY1*10-9,posX1*10+19,posY1*10+19)
        canvas.itemconfig(blinky, fill="red", start = 180, extent = 200, outline = "") 
        a = 2

    elif a == 2:
        canvas.coords(blinky, posX1*10-9, posY1*10-9,posX1*10+19,posY1*10+19)
        canvas.itemconfig(blinky, fill="red", start = 180, extent = 359, outline = "") 
        a = 0

fen = Tk()
canvas = Canvas(fen, height = 600, width = 600)
canvas.pack()
blinky = canvas.create_arc(posX1*10-9, posY1*10-9,posX1*10+19,posY1*10+19, fill = "red", start = 225, extent = 270)
zer(canvas, blinky)
fen.mainloop()
