import tkinter as tk
from random import randint
racine = tk.Tk()


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r,
        g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color):
    fenetre.create_rectangle((i, j), (i+2, j+2), outline=color)


def aleatoire():
    fenetre.delete('all')
    for i in range(1, 256):
        for j in range(1, 256):
            r = randint(0, 255)
            v = randint(0, 255)
            b = randint(0, 255)
            draw_pixel(j, i, get_color(r, v, b))


def degradeGris():
    fenetre.delete('all')
    for i in range(1, 256):
        for j in range(1, 256):
            draw_pixel(j, i, get_color(j, j, j))


def degrade2D():
    fenetre.delete('all')
    for i in range(1, 256):
        for j in range(1, 256):
            draw_pixel(j, i, get_color(i, 0, j))


fenetre = tk.Canvas(racine, width="256", height="256", bg="black")
bouton1 = tk.Button(racine, text="aléatoire", command=aleatoire)
bouton2 = tk.Button(racine, text="dégradé gris", command=degradeGris)
bouton3 = tk.Button(racine, text="dégradé 2D", command=degrade2D)

fenetre.grid(column=1, row=0, rowspan=3)
bouton1.grid(column=0, row=0)
bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)


racine.mainloop()
