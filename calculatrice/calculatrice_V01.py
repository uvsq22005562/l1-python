import tkinter as tk

racine = tk.Tk()
contenu = []


def input(texte):
    global contenu
    if len(contenu) == 0 and texte == ' + ' or \
       len(contenu) == 0 and texte == ' - ' or \
       len(contenu) == 0 and texte == ' x ' or \
       len(contenu) == 0 and texte == ' / ':
        erreur()
    elif ' + ' in contenu and texte == ' + ' or \
         ' + ' in contenu and texte == ' - ' or \
         ' + ' in contenu and texte == ' x ' or \
         ' + ' in contenu and texte == ' / ':
        erreur()
    elif ' - ' in contenu and texte == ' + ' or \
         ' - ' in contenu and texte == ' - ' or \
         ' - ' in contenu and texte == ' x ' or \
         ' - ' in contenu and texte == ' / ':
        erreur()
    elif ' x ' in contenu and texte == ' + ' or \
         ' x ' in contenu and texte == ' - ' or \
         ' x ' in contenu and texte == ' x ' or \
         ' x ' in contenu and texte == ' / ':
        erreur()
    elif ' / ' in contenu and texte == ' + ' or \
         ' / ' in contenu and texte == ' - ' or \
         ' / ' in contenu and texte == ' x ' or \
         ' / ' in contenu and texte == ' / ':
        erreur()
    else:
        contenu.append(texte)
        affiche(contenu)


def affiche(texte):
    temp = ''
    if len(contenu) == 0:
        affichage.config(text='')
    else:
        for i in texte:
            temp += str(i)
            affichage.config(text=temp)


def resultat():
    global contenu
    if ' + ' in contenu:
        temp4 = ''
        temp5 = ''
        temp1 = contenu.index(' + ')
        temp2 = contenu[temp1+1:]
        temp3 = contenu[:temp1]
        for i in temp2:
            temp4 += str(i)
        for i in temp3:
            temp5 += str(i)
        temp6 = int(temp4) + int(temp5)
        contenu = []
        contenu.append(temp6)
        affiche(contenu)
    if ' x ' in contenu:
        temp4 = ''
        temp5 = ''
        temp1 = contenu.index(' x ')
        temp2 = contenu[temp1+1:]
        temp3 = contenu[:temp1]
        for i in temp2:
            temp4 += str(i)
        for i in temp3:
            temp5 += str(i)
        temp6 = int(temp4) * int(temp5)
        contenu = []
        contenu.append(temp6)
        affiche(contenu)
    if ' / ' in contenu:
        temp4 = ''
        temp5 = ''
        temp1 = contenu.index(' / ')
        temp2 = contenu[temp1+1:]
        temp3 = contenu[:temp1]
        for i in temp2:
            temp4 += str(i)
        for i in temp3:
            temp5 += str(i)
        temp6 = int(temp5) // int(temp4)
        contenu = []
        contenu.append(temp6)
        affiche(contenu)
    if ' - ' in contenu:
        temp4 = ''
        temp5 = ''
        temp1 = contenu.index(' - ')
        temp2 = contenu[temp1+1:]
        temp3 = contenu[:temp1]
        for i in temp2:
            temp4 += str(i)
        for i in temp3:
            temp5 += str(i)
        temp6 = int(temp5) - int(temp4)
        contenu = []
        contenu.append(temp6)
        affiche(contenu)


def clear_all():
    global contenu
    contenu = []
    affiche(contenu)


def erreur():
    global contenu
    contenu = []
    contenu.append('erreur')
    affiche(contenu)


affichage = tk.Label(racine, text='')
boutton_0 = tk.Button(racine, text='0', command=lambda: input(0))
boutton_1 = tk.Button(racine, text='1', command=lambda: input(1))
boutton_2 = tk.Button(racine, text='2', command=lambda: input(2))
boutton_3 = tk.Button(racine, text='3', command=lambda: input(3))
boutton_4 = tk.Button(racine, text='4', command=lambda: input(4))
boutton_5 = tk.Button(racine, text='5', command=lambda: input(5))
boutton_6 = tk.Button(racine, text='6', command=lambda: input(6))
boutton_7 = tk.Button(racine, text='7', command=lambda: input(7))
boutton_8 = tk.Button(racine, text='8', command=lambda: input(8))
boutton_9 = tk.Button(racine, text='9', command=lambda: input(9))
boutton_C = tk.Button(racine, text='C', command=clear_all)
boutton_addition = tk.Button(racine, text='+', command=lambda: input(' + '))
boutton_soustraction = tk.Button(racine, text='-',
                                 command=lambda: input(' - '))
boutton_multiplication = tk.Button(racine, text='x',
                                   command=lambda: input(' x '))
boutton_division = tk.Button(racine, text='/', command=lambda: input(' / '))
boutton_calcul = tk.Button(racine, text='=', command=resultat)
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
boutton_soustraction.grid(column=0, row=4)
boutton_multiplication.grid(column=1, row=4)
boutton_division.grid(column=2, row=4)
boutton_calcul.grid(column=1, row=5)
affichage.grid(column=3, row=0)


racine.mainloop()
