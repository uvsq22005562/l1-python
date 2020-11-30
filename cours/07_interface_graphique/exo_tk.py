import tkinter as tk
programme = tk.Tk()

# ===================================================================
# Appel des variables
valeur_gauche = 12
valeur_droite = 25


# ===================================================================
# Call back fonctions
def input_gauche():
    """cmd-bouton: demande la valeur de gauche dans le calcul"""
    global valeur_gauche
    valeur_gauche = int(input("entrez un entier"))
    text1.config(text=str(valeur_gauche))


def input_droite():
    """cmd-bouton: demande la valeur de droite dans le calcul"""
    global valeur_droite
    valeur_droite = int(input("entrez un entier"))
    text3.config(text=str(valeur_droite))


def calculer():
    """calcul la somme"""
    calcul = valeur_gauche + valeur_droite
    text5.config(text=str(calcul))


# ===================================================================
# Widget création
text1 = tk.Label(programme, text="12", font=("helvetica", "26"))
text2 = tk.Label(programme, text="+", font=("helvetica", "26"))
text3 = tk.Label(programme, text="25", font=("helvetica", "26"))
text4 = tk.Label(programme, text="=", font=("helvetica", "26"))
text5 = tk.Label(programme, text="37", font=("helvetica", "26"))
bouton1 = tk.Button(programme,
                    text="choisir une valeur pour l'opérant de gauche",
                    font=("helvetica", "26"), command=input_gauche)
bouton2 = tk.Button(programme, text="calculer", font=("helvetica", "26"),
                    command=calculer)
bouton3 = tk.Button(programme,
                    text="choisir une valeur pour l'opérant de droite",
                    font=("helvetica", "26"), command=input_droite)

# ===================================================================
# Widget position
text1.grid(column=1, row=0)
text2.grid(column=2, row=0)
text3.grid(column=3, row=0)
text4.grid(column=4, row=0)
text5.grid(column=5, row=0)
bouton1.grid(column=0, row=1)
bouton2.grid(column=1, row=1, columnspan=5)
# columnspan --> tu peux te déplacer sur les 5 colonnes suivantes
bouton3.grid(column=0, row=2)

programme.mainloop()


# global ne sert que pour modifier une variable non indenté dans la fct ->
# pas besoin pour juste l'appeler
