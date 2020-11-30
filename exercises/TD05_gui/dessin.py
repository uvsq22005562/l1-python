import tkinter as tk
from random import randint

racine = tk.Tk()


# Variables
main_color = 'blue'


# fonctions associés aux boutons
def dessinCercle():
    A = randint(0, 300)
    B = randint(0, 300)
    canvas.create_oval((A, B), (A+100, B+100), fill=main_color)


def dessinCarre():
    A = randint(0, 300)
    B = randint(0, 300)
    canvas.create_rectangle((A, B), (A+100, B+100), fill=main_color)


def croix():
    A = randint(0, 300)
    B = randint(0, 300)
    canvas.create_line((A, B), (A+100, B+100), fill=main_color, width=20)
    canvas.create_line((A+100, B), (A, B+100), fill=main_color, width=20)


def clearBoard():
    canvas.delete('all')


def color_change():
    global main_color
    main_color = input("choisissez une couleur")


# création des widgets
#       boutons
bouton1 = tk.Button(racine, text="choisir une couleur",
                    font=("calibri", "14"), command=color_change)
bouton2 = tk.Button(racine, text="cercle", font=("helvetica", "10"),
                    command=dessinCercle)
bouton3 = tk.Button(racine, text="carré", font=("helvetica", "10"),
                    command=dessinCarre)
bouton4 = tk.Button(racine, text="croix", font=("helvetica", "10"),
                    command=croix)
bouton5 = tk.Button(racine, text="clear the board", font=("helvetica", "10"),
                    command=clearBoard)

#       canvas
canvas = tk.Canvas(racine, width="400", height="400",
                   bg="black", relief='ridge', borderwidth=12)

# positionnement des widgets
canvas.grid(column=1, row=1, rowspan=4)
bouton1.grid(column=1, row=0)
bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)
bouton4.grid(column=0, row=3)
bouton5.grid(column=0, row=4)

racine.mainloop()
