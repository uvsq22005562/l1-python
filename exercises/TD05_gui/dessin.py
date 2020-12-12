import tkinter as tk
from random import randint

racine = tk.Tk()
laliste = []

# Variables
main_color = 'blue'


# fonctions associés aux boutons
def dessinCercle():
    global laliste
    A = randint(0, 300)
    B = randint(0, 300)
    cercle = canvas.create_oval((A, B), (A+100, B+100), fill=main_color)
    laliste.append(cercle)


def dessinCarre():
    global laliste
    A = randint(0, 300)
    B = randint(0, 300)
    carre = canvas.create_rectangle((A, B), (A+100, B+100), fill=main_color)
    laliste.append(carre)


def croix():
    global laliste
    A = randint(0, 300)
    B = randint(0, 300)
    croix1 = canvas.create_line((A, B), (A+100, B+100),
                                fill=main_color, width=20)
    croix2 = canvas.create_line((A+100, B), (A, B+100),
                                fill=main_color, width=20)
    laliste.append([croix1, croix2])


def clearBoard():
    canvas.delete('all')


def color_change():
    global main_color
    main_color = input("choisissez une couleur")


def ctrlZ():
    global laliste
    if len(laliste) > 0:
        if type(laliste[len(laliste)-1]) == list:
            canvas.delete(laliste[len(laliste)-1][1])
            canvas.delete(laliste[len(laliste)-1][0])
            del laliste[len(laliste)-1]
        else:
            canvas.delete(laliste[len(laliste)-1])
            del laliste[len(laliste)-1]


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
bouton6 = tk.Button(racine, text="undo", font=("calibri", "14"),
                    command=ctrlZ)

#       canvas
canvas = tk.Canvas(racine, width="400", height="400",
                   bg="black", relief='ridge', borderwidth=12)

# positionnement des widgets
canvas.grid(column=1, row=1, rowspan=5)
bouton1.grid(column=1, row=0)
bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)
bouton4.grid(column=0, row=3)
bouton5.grid(column=0, row=4)
bouton6.grid(column=0, row=5)

racine.mainloop()
