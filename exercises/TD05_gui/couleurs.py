import tkinter as tk
from random import randint

racine = tk.Tk()


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r,
         g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color):
    fenetre.create_rectangle((i, j), (i+2, j+2), fill=color)


def aléatoire():
    for i in range(1, 3):
        for j in range(1, 257):
            r = randint(0, 255)
            v = randint(0, 255)
            b = randint(0, 255)
            draw_pixel(j, i, get_color(r, v, b))


fenetre = tk.Canvas(racine, width="256", height="256", bg="black")
bouton1 = tk.Button(racine, text="aléatoire", command=aléatoire)
bouton2 = tk.Button(racine, text="dégradé gris")
bouton3 = tk.Button(racine, text="dégradé 2D")

fenetre.grid(column=1, row=0, rowspan=3)
bouton1.grid(column=0, row=0)
bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)


racine.mainloop()
