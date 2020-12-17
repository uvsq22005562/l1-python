import tkinter as tk
from math import sqrt

racine = tk.Tk()
contenu = []


def input(texte):
    """ fonction qui ajoute les caractères spéciaux / les chiffres a
        la variables mémoire - est chargé de la gestion des erreurs. """
    global contenu
    if len(contenu) == 0 and texte == ' + ' or \
       len(contenu) == 0 and texte == ' - ' or \
       len(contenu) == 0 and texte == ' x ' or \
       len(contenu) == 0 and texte == ' ² ' or \
       len(contenu) == 0 and texte == ' ^(1/2) ' or\
       len(contenu) == 0 and texte == ' / ':
        pass
    elif ' + ' in contenu and texte == ' + ' or \
         ' + ' in contenu and texte == ' - ' or \
         ' + ' in contenu and texte == ' x ' or \
         ' + ' in contenu and texte == ' ² ' or \
         ' + ' in contenu and texte == ' ^(1/2) ' or \
         ' + ' in contenu and texte == ' / ':
        pass
    elif ' - ' in contenu and texte == ' + ' or \
         ' - ' in contenu and texte == ' - ' or \
         ' - ' in contenu and texte == ' x ' or \
         ' - ' in contenu and texte == ' ² ' or \
         ' - ' in contenu and texte == ' ^(1/2) ' or \
         ' - ' in contenu and texte == ' / ':
        pass
    elif ' x ' in contenu and texte == ' + ' or \
         ' x ' in contenu and texte == ' - ' or \
         ' x ' in contenu and texte == ' x ' or \
         ' x ' in contenu and texte == ' ² ' or \
         ' x ' in contenu and texte == ' ^(1/2) ' or \
         ' x ' in contenu and texte == ' / ':
        pass
    elif ' / ' in contenu and texte == ' + ' or \
         ' / ' in contenu and texte == ' - ' or \
         ' / ' in contenu and texte == ' x ' or \
         ' / ' in contenu and texte == ' ² ' or \
         ' / ' in contenu and texte == ' ^(1/2) ' or \
         ' / ' in contenu and texte == ' / ':
        pass
    elif ' ² ' in contenu and texte == ' + ' or \
         ' ² ' in contenu and texte == ' - ' or \
         ' ² ' in contenu and texte == ' x ' or \
         ' ² ' in contenu and texte == ' ^(1/2) ' or \
         ' ² ' in contenu and texte == ' ² ' or \
         ' ² ' in contenu or \
         ' ² ' in contenu and texte == ' / ':
        pass
    elif ' ^(1/2) ' in contenu and texte == ' + ' or \
         ' ^(1/2) ' in contenu and texte == ' - ' or \
         ' ^(1/2) ' in contenu and texte == ' x ' or \
         ' ^(1/2) ' in contenu and texte == ' ² ' or \
         ' ^(1/2) ' in contenu and texte == ' ^(1/2) ' or \
         ' ^(1/2) ' in contenu or \
         ' ^(1/2) ' in contenu and texte == ' / ':
        pass
    else:
        contenu.append(texte)
        affiche(contenu)


def affiche(texte):
    """ fonction qui affiche sur la partie 'label' de tkinter
        ce que l'on souhaite. """
    temp1 = ''
    if len(contenu) == 0:
        affichage.config(text='')
    else:
        for i in texte:
            temp1 += str(i)
        if len(temp1) >= 3:
            if temp1[len(temp1)-1] == '0' and temp1[len(temp1)-2] == '.':
                temp2 = temp1[:(len(temp1)-2)]
                affichage.config(text=temp2)
            else:
                affichage.config(text=temp1)
        else:
            affichage.config(text=temp1)


def resultat():
    """ fonction qui correspond a la touche = ; effectue les calculs, vide
        la variable mémoire, puis affiche le résultat. """
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
        temp6 = float(temp4) + float(temp5)
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
        temp6 = float(temp4) * float(temp5)
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
        temp6 = float(temp5) / float(temp4)
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
        temp6 = float(temp5) - float(temp4)
        contenu = []
        contenu.append(temp6)
        affiche(contenu)
    if ' ² ' in contenu:
        temp5 = ''
        temp1 = contenu.index(' ² ')
        temp3 = contenu[:temp1]
        for i in temp3:
            temp5 += str(i)
        temp6 = float(temp5) * float(temp5)
        contenu = []
        contenu.append(temp6)
        affiche(contenu)
    if ' ^(1/2) ' in contenu:
        temp5 = ''
        temp1 = contenu.index(' ^(1/2) ')
        temp3 = contenu[:temp1]
        for i in temp3:
            temp5 += str(i)
        temp6 = sqrt(float(temp5))
        contenu = []
        contenu.append(temp6)
        affiche(contenu)


def clear_all():
    """ reset le contenu de la mémoire et l'affichage """
    global contenu
    contenu = []
    affiche(contenu)


def clear_once():
    """ reset le contenu de la mémoire et l'affichage """
    global contenu
    del contenu[len(contenu)-1]
    affiche(contenu)


def erreur():
    """ est appelé suite a la condition d'une erreur; fonction
        qui affiche erreur et reset la mémoire et l'affichage """
    global contenu
    contenu = []
    contenu.append('erreur')
    affiche(contenu)
    contenu = []


# ----- création des widgets -----
affichage = tk.Label(racine, text='', height='3',
                     width='22', font=('helvetica', '8'))
boutton_0 = tk.Button(racine, text='0',
                      command=lambda: input(0), height='2', width='4')
boutton_1 = tk.Button(racine, text='1',
                      command=lambda: input(1), height='2', width='4')
boutton_2 = tk.Button(racine, text='2',
                      command=lambda: input(2), height='2', width='4')
boutton_3 = tk.Button(racine, text='3',
                      command=lambda: input(3), height='2', width='4')
boutton_4 = tk.Button(racine, text='4',
                      command=lambda: input(4), height='2', width='4')
boutton_5 = tk.Button(racine, text='5',
                      command=lambda: input(5), height='2', width='4')
boutton_6 = tk.Button(racine, text='6',
                      command=lambda: input(6), height='2', width='4')
boutton_7 = tk.Button(racine, text='7',
                      command=lambda: input(7), height='2', width='4')
boutton_8 = tk.Button(racine, text='8',
                      command=lambda: input(8), height='2', width='4')
boutton_9 = tk.Button(racine, text='9',
                      command=lambda: input(9), height='2', width='4')
boutton_C = tk.Button(racine, text='C',
                      command=clear_all, height='2', width='4')
boutton_addition = tk.Button(racine, text='+',
                             command=lambda: input(' + '),
                             height='2', width='4')
boutton_soustraction = tk.Button(racine, text='-',
                                 command=lambda: input(' - '),
                                 height='2', width='4')
boutton_multiplication = tk.Button(racine, text='x',
                                   command=lambda: input(' x '),
                                   height='2', width='4')
boutton_division = tk.Button(racine, text='/',
                             command=lambda: input(' / '),
                             height='2', width='4')
boutton_calcul = tk.Button(racine, text='=',
                           command=resultat, height='2', width='4')
boutton_point = tk.Button(racine, text='.',
                          command=lambda: input('.'), height='2', width='4')
boutton_carre = tk.Button(racine, text='²',
                          command=lambda: input(' ² '), height='2', width='4')
boutton_sqrt = tk.Button(racine, text='sqrt',
                         command=lambda: input(' ^(1/2) '),
                         height='2', width='4')
boutton_retour = tk.Button(racine, text=' << ', command=clear_once,
                           height='2', width='4')

# ----- placement des widgets -----
affichage.grid(column=0, row=0, columnspan=4)
boutton_1.grid(column=0, row=1)
boutton_2.grid(column=1, row=1)
boutton_3.grid(column=2, row=1)
boutton_4.grid(column=0, row=2)
boutton_5.grid(column=1, row=2)
boutton_6.grid(column=2, row=2)
boutton_7.grid(column=0, row=3)
boutton_8.grid(column=1, row=3)
boutton_9.grid(column=2, row=3)
boutton_C.grid(column=0, row=4)
boutton_0.grid(column=1, row=4)
boutton_calcul.grid(column=2, row=4)
boutton_addition.grid(column=3, row=1)
boutton_soustraction.grid(column=3, row=2)
boutton_multiplication.grid(column=3, row=3)
boutton_division.grid(column=3, row=4)
boutton_point.grid(column=0, row=5)
boutton_carre.grid(column=1, row=5)
boutton_sqrt.grid(column=2, row=5)
boutton_retour.grid(column=3, row=5)


racine.mainloop()
