import tkinter as tk

racine = tk.Tk()
laliste = []


def relie():
    global laliste
    if len(laliste) >= 2:
        if laliste[0][0] > 250 and laliste[1][0] > 250:
            fenetre.create_line((laliste[0][0], laliste[0][1]),
                                (laliste[1][0], laliste[1][1]), fill='blue')
        if laliste[0][0] < 250 and laliste[1][0] < 250:
            fenetre.create_line((laliste[0][0], laliste[0][1]),
                                (laliste[1][0], laliste[1][1]), fill='red')
        del laliste[0]


def draw(event):
    global laliste
    X = event.x
    Y = event.y
    if X < 250:
        pts1 = fenetre.create_rectangle((X, Y), (X+1, Y+1), outline='red')
        laliste.append(fenetre.coords(pts1))
    else:
        pts2 = fenetre.create_rectangle((X, Y), (X+1, Y+1), outline='blue')
        laliste.append(fenetre.coords(pts2))
    relie()


fenetre = tk.Canvas(width='500', height='500', bg='black')
fenetre.grid(column=0, row=0)
fenetre.create_line((250, 0), (250, 500), fill='white')
racine.bind('<Button-1>', draw)

racine.mainloop()
