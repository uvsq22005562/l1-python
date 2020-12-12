import tkinter as tk

racine = tk.Tk()


def draw(event):
    X = event.x
    Y = event.y
    fenetre.create_rectangle((X, Y), (X+1, Y+1), outline='red')


fenetre = tk.Canvas(width='500', height='500', bg='black')
fenetre.grid(column=0, row=0)
racine.bind('<Button-1>', draw)

racine.mainloop()
