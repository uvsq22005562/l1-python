# import de la bibliothèque appJar -> donne accès a
# tout le code pour les gui

from appJar import gui


# On créer une GUI en lui donnant un nom (ici window)
# Ici, la variable str donné a gui() correspond au nom du programme
#  affiché ( quand on passe la souris dessus par exemple )

window = gui("mon programme")


# On ajoute un label, pour l'instant, c'est là que tout se passe  -->
# il sagit d'un widget  ATTENTION : tout les widgets doivent êtres
#  ajoutés avant de démarer la GUI

# attention : on oublie pas la majuscule a Label

# Label prend deux arguments : ("titre UNIQUE du label", "Ce qui va être
#  affiché")  --> le titre va nous permettre de modifier ou de se servir
#  du widget plus tard

window.addLabel("lb1", "Hello World")
window.addLabel("lb2", "ça va vous ? ")
window.addLabel("lb3", "Bon c'est pas encore le pied tout ça ")


# On peut changer certains paramètres de notre GUI :
# Ca va s'appliquer a tout les widget de la GUI qui correspondent
# background --> ici la couleur
# texte --> ici la taille

window.setBg("grey")
window.setFont(40)


# Lance le GUI correspondant
window.go()
