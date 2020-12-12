import tkinter as tk

racine = tk.Tk()


def draw(event):
    X = event.x
    Y = event.y
    if X < 250:
        fenetre.create_oval((X-25, Y-25), (X+25, Y+25), fill='red')
    else:
        fenetre.create_oval((X-25, Y-25), (X+25, Y+25), fill='blue')


fenetre = tk.Canvas(width='500', height='500', bg='black')
fenetre.grid(column=0, row=0)
fenetre.create_line((250, 0), (250, 500), fill='white')
racine.bind('<Button-1>', draw)

racine.mainloop()
