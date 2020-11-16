# 4 + 14 + 15 + 1 = 34 --> ligne
# 4 + 7 + 10 + 13 = 34 --> diagonale
# 4 + 9 + 5 + 16 = 34 --> colonne
# Il sagit donc bien d'un carré magique

# Appel des variables tel que --> valeurs des carres pour tout l'exercice
carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        for j in i:
            if len(str(j)) == 2:
                print(j, end=' ')
            else:
                print(j, end='. ')
        print('')
    print('')


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si
     toutes les lignes ont la même somme, et -1 sinon """
    A = 0
    for i in range(len(carre)):
        B = 0
        for j in range(len(carre[i])):
            B += carre[i][j]
        A += B
    if A % B == 0:
        return A // 4
    else:
        return -1


print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))
