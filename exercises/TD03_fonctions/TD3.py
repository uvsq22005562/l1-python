# FONCTION N°1 :
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde d'un temps donné comme :
        jour, heure, minute, seconde."""

    jours = temps[0] * 86400
    heures = temps[1] * 3600
    minutes = temps[2] * 60
    secondes = temps[3]
    return jours + heures + minutes + secondes


# FONCTION N°2 :
def secondeEnTemps(seconde):
    """Renvoie le temps comme : (jour, heure, minute, seconde) 
        correspondant au nombre de secondes donnés"""

    jours = seconde // 86400
    heures = seconde // 3600 % 24
    minutes = seconde // 60 % 60
    return jours, heures, minutes, seconde % 60


# FONCTION N°3 :
def pluriel(mot, nombre_mot):
    if nombre_mot > 1:
        mot += "s"
    return mot


# FONCTION N°4 :
def afficheTemps(temps):
    print(temps[0], pluriel("jour", temps[0]), end=" ")
    print(temps[1], pluriel("heure", temps[1]), end=" ")
    print(temps[2], pluriel("minute", temps[2]), end=" ")
    print(temps[3], pluriel("seconde", temps[3]), end=" ")


# FONCTION N°5-6-7 :
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


# FONCTION N°8 :
def tempsEnDate(temps):
    """temps en (année, mois, jours, heures, minutes, secondes)"""
    return (1970 + temps[0] // 365,
            temps[0] % 365 // 30,
            temps[0] % 30,
            temps[1],
            temps[2],
            temps[3])


# FONCTION N°9 :
def nombreBisextile(jour):
    seconde = jour * 86400
    annee = tempsEnDate(secondeEnTemps(seconde))[0]
    bisextile = 0
    for i in range(1970, annee, 1):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            bisextile += 1
    return bisextile


# FONCTION N°10 :
def tempsEnDateBisextile(temps):
    bisextile = nombreBisextile(temps[0])
    jours = temps[0] - bisextile

    return (1970 + jours // 365,
            jours % 365 // 30,
            jours % 30,
            temps[1],
            temps[2],
            temps[3])


print("bonjour")
