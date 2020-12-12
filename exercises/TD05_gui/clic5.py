import tkinter as tk

racine = tk.Tk()
ctrl = 1
laliste = []


def draw(event):
    global ctrl
    global laliste
    X = event.x
    Y = event.y
    if ctrl <= 8:
        ronron = fenetre.create_oval((X-25, Y-25), (X+25, Y+25), fill='red')
        laliste.append(fenetre.coords(ronron))
        ctrl += 1
    elif ctrl == 9:
        for i in range(0, 8):
            X = laliste[i][0]
            Y = laliste[i][1]
            fenetre.create_oval((X, Y), (X+50, Y+50), fill='yellow')
        ctrl += 1
    elif ctrl == 10:
        laliste = []
        fenetre.delete('all')
        ctrl = 1


fenetre = tk.Canvas(width='500', height='500', bg='black')
fenetre.grid(column=0, row=0)
racine.bind('<Button-1>', draw)

racine.mainloop()
