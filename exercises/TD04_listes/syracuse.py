def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = []
    while n != 1:
        if n % 2 == 0:
            n = n//2
            liste.append(n)
        else:
            n = n*3 + 1
            liste.append(n)
    return liste


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    D = 2
    for i in range(2, n_max):
        C = syracuse(i)
        if C[len(C)-1] == 1:
            D += 1
        else:
            return False
    if D == n_max:
        return True
    else:
        return False


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    bigboy = [tempsVol(i) for i in range(1, n_max)]
    return bigboy


def volMax(n_max):
    """ renvois le nombre avec le temps de vol maximal dans l'interval donné"""
    liste = tempsVolListe(n_max)
    A = max(liste)
    B = liste.index(A) + 1
    return "c'est le nombre", B, "qui a le temps de vol maximal, avec :", A


def altitudeMaxUnite(n):
    liste = syracuse(n)
    return max(liste)


def altitudeMaxGlobal(n_max):
    liste = [altitudeMaxUnite(i) for i in range(2, n_max)]
    A = max(liste)
    B = liste.index(A) + 2
    return "l'altitude max est atteinte par", B, "avec", A


print(altitudeMaxGlobal(10000))
