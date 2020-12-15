import tkinter as tk

racine = tk.Tk()

memoire1 = ''
memoire2 = ''
addition_nbr = []


def affiche(texte):
    affichage.config(text=texte)


def memorise(nombre):
    global memoire1
    global memoire2
    if '+' in memoire1:
        memoire2 += nombre
        affiche(memoire2)
    else:
        memoire1 += nombre
        affiche(memoire1)


def clear_all():
    global memoire1
    memoire1 = ''
    affiche(memoire1)


def addition():
    global memoire1
    addition_nbr.append(int(memoire1))
    memorise('+')


affichage = tk.Label(racine, text='')
boutton_0 = tk.Button(racine, text='0', command=lambda: memorise('0'))
boutton_1 = tk.Button(racine, text='1', command=lambda: memorise('1'))
boutton_2 = tk.Button(racine, text='2', command=lambda: memorise('2'))
boutton_3 = tk.Button(racine, text='3', command=lambda: memorise('3'))
boutton_4 = tk.Button(racine, text='4', command=lambda: memorise('4'))
boutton_5 = tk.Button(racine, text='5', command=lambda: memorise('5'))
boutton_6 = tk.Button(racine, text='6', command=lambda: memorise('6'))
boutton_7 = tk.Button(racine, text='7', command=lambda: memorise('7'))
boutton_8 = tk.Button(racine, text='8', command=lambda: memorise('8'))
boutton_9 = tk.Button(racine, text='9', command=lambda: memorise('9'))
boutton_C = tk.Button(racine, text='C', command=clear_all)
boutton_addition = tk.Button(racine, text='+', command=addition)
boutton_1.grid(column=0, row=0)
boutton_2.grid(column=1, row=0)
boutton_3.grid(column=2, row=0)
boutton_4.grid(column=0, row=1)
boutton_5.grid(column=1, row=1)
boutton_6.grid(column=2, row=1)
boutton_7.grid(column=0, row=2)
boutton_8.grid(column=1, row=2)
boutton_9.grid(column=2, row=2)
boutton_C.grid(column=0, row=3)
boutton_0.grid(column=1, row=3)
boutton_addition.grid(column=2, row=3)
affichage.grid(column=3, row=0)


racine.mainloop()
