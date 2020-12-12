import tkinter as tk

racine = tk.Tk()
ctrl = 0


def draw(event):
    global ctrl
    global boum
    if ctrl <= 10:
        if ctrl % 2 == 0:
            fenetre.delete(boum)
            ctrl += 1
        else:
            boum = fenetre.create_rectangle((100, 100),
                                            (400, 400), fill='white')
            ctrl += 1
    else:
        racine.quit()


fenetre = tk.Canvas(width='500', height='500', bg='black')
fenetre.grid(column=0, row=0)
boum = fenetre.create_rectangle((100, 100), (400, 400), fill='white')
racine.bind('<Button-1>', draw)

racine.mainloop()
