def max(liste):
<<<<<<< HEAD
    maximum = liste[0]
    for i in range(len(liste)):
=======
    maximum = 0
    for i in range(len(liste) + 1):
>>>>>>> 0e241ebee3e6dd3305bdb5ede220d7c42fe1a4e8
        if maximum < liste[i]:
            maximum = liste[i]
    return maximum

<<<<<<< HEAD

print(max([1, 4, 3, 1, 3, 7]))
print(max([-1, -3, -4, -2, -6]))
=======
max([1,4,3,1,3,7])
max([-1,-3,-4,-2,-6])
>>>>>>> 0e241ebee3e6dd3305bdb5ede220d7c42fe1a4e8
