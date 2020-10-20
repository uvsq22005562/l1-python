def max(liste):
    maximum = liste[0]
    for i in range(len(liste)):
        if maximum < liste[i]:
            maximum = liste[i]
    return maximum


print(max([1, 4, 3, 1, 3, 7]))
print(max([-1, -3, -4, -2, -6]))
