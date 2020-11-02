import time


def tempsEnSeconde(temps):
    """ Accepte tuple (jour, heures, minutes, secondes) -->
        renvois un tuple de type (secondes). """
    if len(temps) == 9:
        annee_bisextiles = bisextile(temps)
        jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # annee = (temps[0] - 1970) * 31536000
        mois = 0
        nbr_mois = (temps[1] + (temps[0] - 1970) * 12)
        for i in range(1, nbr_mois+1):
            mois += (jours_par_mois[i % 12] * 86400)
        jours = (temps[2] + annee_bisextiles) * 86400
        heures = temps[3] * 3600
        minutes = temps[4] * 60
        secondes = temps[5]
        return (mois + jours + heures + minutes + secondes)

    else:
        jours = temps[0] * 86400
        heures = temps[1] * 3600
        minutes = temps[2] * 60
        secondes = temps[3]
        return jours + heures + minutes + secondes
# PREND LE TEMPS EN (JOUR, HEURES, MINUTES, SECONDES)
# PREND LE TEMPS EN SECONDE


def secondeEnTemps(seconde):
    """ Accepte un tuple de type (secondes) -->
        renvois un tuple de type (jours, heures, minutes, secondes). """

    jours = seconde // 86400
    heures = seconde // 3600 % 24
    minutes = seconde // 60 % 60
    return jours, heures, minutes, seconde % 60
# PREND LE TEMPS EN SECONDE
# RENVOIS LE TEMPS (JOUR, HEURES, MINUTES, SECONDES)


def afficheTemps(temps):
    mot = ["jour", "heure", "minute", "seconde"]
    for i in range(0, 4):
        if temps[i] > 1:
            mot[i] += "s"
            print(temps[i], mot[i])
# PREND LE TEMPS EN (JOUR, HEURES, MINUTES, SECONDES)
# L'AFFICHE (PLURIEL COMPRIS)


def demandeTemps():
    """ Première fonction d'interaction, demande a l'utilisateur
        de saisir le nombre de (jours, heures, minutes, secondes) -->
        renvois un tuple (jours, ). """

    jours = int(input("veuillez entrer le nombre de jours"))
    heures = int(input("veuillez entrer le nombre d'heures"))
    minutes = int(input("veuillez entrer le nombre de minutes"))
    secondes = int(input("veuillez entrer le nombre de minutes"))

    while jours < 0:
        jours = int(input("veuillez entrer un nombre de jour correct"))

    while heures >= 24 or heures < 0:
        heures = int(input("veuillez entrer un nombre d'heures correct"))

    while minutes >= 60 or minutes < 0:
        minutes = int(input("veuillez entrer un nombre de minutes correct"))

    while secondes >= 60 or secondes < 0:
        secondes = int(input("veuillez entrer un nombre de secondes correct"))

    return (jours, heures, minutes, secondes)
# DEMANDE LE TEMPS A L'UTILISATEUR
# SOUS FORME (JOUR, HEURES, MINUTES, SECONDES)


def sommeTemps(temps1, temps2):
    """ Additionne deux tuples 'temps' tels que
        temps : (jours, heures, minutes, secondes) -->
        retourne un tuple sous la même forme. """

    result = [0, 0, 0, 0]
    for i in range(0, 4):
        result[i] = temps1[i] + temps2[i]

    if result[3] >= 60:
        result[2] += result[3] // 60
        result[3] %= 60
    if result[2] >= 60:
        result[1] += result[2] // 60
        result[2] %= 60
    if result[1] >= 24:
        result[0] += result[1] // 24
        result[1] %= 24
    return result
# ADDITIONNE DEUX TUPLES DE FORMES (JOUR, HEURES, MINUTES, SECONDES)
# SOUS LA FORME D'UN TUPLE (JOUR, HEURES, MINUTES, SECONDES)


def proportionTemps(temps, proportion):
    """ accepte un temps (jours, heures, minutes, secondes) -->
        renvois un tuple du même genre correspondant au pourcentage
        (proportion) de ce temps """

    secondes = tempsEnSeconde(temps)
    secondes = secondes * proportion / 100
    return secondeEnTemps(secondes)
# PREND UN TUPLE (JOUR, HEURES, MINUTES, SECONDES)
# DONNE UN POURCENTAGE (PROPORTION) DU TUPLE


def tempsEnDate(temps):
    """ Accepte un temps en (jours, heures, minutes, secondes) -->
        renvois un temps en (annee, mois, jours, heures, minutes, secondes) """
    return (1970 + temps[0] // 365,
            temps[0] % 365 // 30,
            temps[0] % 30,
            temps[1],
            temps[2],
            temps[3])
# PREND UN TUPLE (JOUR, HEURES, MINUTES, SECONDES)
# RENVOIS UN TUPLE SOUS FORME (ANNEE, MOIS, JOURS, HEURES, MINUTES, SECONDES)


def afficheDate(date=-1):
    if date == -1:
        pass
        return

    def afficheAnnee(date):
        return "l'année est " + str(date[0])

    def afficheMois(date):
        return " et le mois est " + str(date[1])

    print(afficheAnnee(date) + afficheMois(date))
    afficheTemps((date[2], date[3], date[4], date[5]))
#  PREND UN TUPLE (ANNEE, MOIS, JOURS, HEURES, MINUTES, SECONDES)
# L'AFFICHE


def bisextile(jour):
    nombre_bisextile = 0
    annee = temps[0]
    bisextile = 0
    for i in range(1970, annee, 1):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            bisextile += 1
    print(bisextile)
    return nombre_bisextile
# PREND UN NOMBRE DE JOUR ET DETERMINE TOUTES LES ANNEES
# BISEXTILES ENTRE 1970 ET 1970 + NOMBRE DE JOURS
# ON CONSIDERE ICI LE PREMIER JANVIER 2020 A 00:00


def nombreBisextile(jour):
    """ accepte un nombre de jour -->
        renvois un nombre d'annéee bisextiles depuis 1970, 00/00 00:00 """
    seconde = jour * 86400
    annee = tempsEnDate(secondeEnTemps(seconde))[0]
    bisextile = 0
    for i in range(1970, annee, 1):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            bisextile += 1
    return bisextile
# PREND UN NOMBRE DE JOUR ET RENVOIS
# LE NOMBRE D'ANNEE BISEXTILES DEPUIS JANVIER 1970 00/00 00:00


def tempsEnDateBisextile(temps):
    bisextile = nombreBisextile(temps[0])
    jours = temps[0] - bisextile

    return (1970 + jours // 365,
            jours % 365 // 30,
            jours % 30,
            temps[1],
            temps[2],
            temps[3])
# MEME FONCTION QUE TEMPSENDATE
# MAIS AVEC LA CORRECTION DES ANNEES BISEXTILES


temps = (time.gmtime())
print(tempsEnSeconde(temps))
print(time.gmtime())
