# espressione, iterabile, condizione = 0

# List Comprehension
# [espressione for elemento in iterabile if condizione]

numeri = [1, 2, 3, 4, 5]
quadrati = [x**2 for x in numeri]
print(quadrati)

# -------------------------------------- #

numeri_pari = [x for x in range(10) if x % 2 == 0]
print(numeri_pari)

# -------------------------------------- #


def cubo(x):
    return x**3


cubi = [cubo(x) for x in range(5)]
print(cubi)

# -------------------------------------- #

parole = ["ciao", "a", "Python", "cigliegina"]
parole_lunghe = [parola for parola in parole if len(parola) > 3]
print(parole_lunghe)

# -------------------------------------- #

frutti = ["mela", "banana", "ciliegia"]
maiuscole = [frutto.upper() for frutto in frutti]
print(maiuscole)

# -------------------------------------- #
# Enumerate ritorna indice e valore. Funziona su iterable
valori = ["a", "b", "c"]
tuples = [(i, valore) for i, valore in enumerate(valori)]
print(tuples)

# -------------------------------------- #

matrice = [[i * j for j in range(3)] for i in range(3)]
print(matrice)

# -------------------------------------- #

numeri = [1, 2, 3, 4, 5]
# somma dei numeri dispari
numeri_sommati = sum([x for x in numeri if x % 2 == 0])
print(numeri_sommati)
