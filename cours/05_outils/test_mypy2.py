# on peut préciser le type d'une fonction avec une flèche
def sommeVersString(a: int, b: int) -> str:
    return str(a+b)


a: int = sommeVersString(3, 2)
sommeVersString(3, 2) + sommeVersString(1, 4)
sommeVersString(3, 2)//sommeVersString(1, 4)
