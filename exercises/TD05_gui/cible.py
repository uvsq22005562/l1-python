import tkinter as tk

taille_fenetre = int(input("entrez la taille de la fenêtre : "))
nbr_paterne = int(input("nombre de paternes ( 6 cercles ) voulus : "))

racine = tk.Tk()

fenetre = tk.Canvas(racine, height=str(taille_fenetre),
                    width=str(taille_fenetre), bg="black")
fenetre.grid(column=0, row=0)

colors = ["blue", "green", "black", "yellow", "magenta", "red"]
C = taille_fenetre/2
A = C/(nbr_paterne*6)
B = C
for i in range(1, nbr_paterne + 1):
    fenetre.create_oval((C-B, C-B), (C+B, C+B), fill=["blue"])
    B -= A
    fenetre.create_oval((C-B, C-B), (C+B, C+B), fill=["green"])
    B -= A
    fenetre.create_oval((C-B, C-B), (C+B, C+B), fill=["black"])
    B -= A
    fenetre.create_oval((C-B, C-B), (C+B, C+B), fill=["yellow"])
    B -= A
    fenetre.create_oval((C-B, C-B), (C+B, C+B), fill=["magenta"])
    B -= A
    fenetre.create_oval((C-B, C-B), (C+B, C+B), fill=["red"])
    B -= A

racine.mainloop()
