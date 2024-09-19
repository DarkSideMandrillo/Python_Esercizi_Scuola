# [espressione* for elemento in iterabile if condizione*]

# quadrati di tutti i numeri pari tra 1 e 20
quadrati = [x**2 for x in range(1, 21) if x % 2 == 0]
print(quadrati)

# solo le parole con più di 5 lettere
parole = ["elefante", "gatto", "rinoceronte", "cane", "scimmia", "tigre"]
paroleLunghe = [parola for parola in parole if len(parola) > 5]
paroleLunghe = [x for x in parole if len(x) > 5]
print(paroleLunghe)

# stesse stringhe tutte in maiuscolo
stringhe = ["ciao", "mondo", "python", "esercizi"]
stringheMaiuscolo = [stringa.upper() for stringa in stringhe]
print(stringheMaiuscolo)

# somma di ogni sotto-lista.
liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listaSommata = [sum(lista) for lista in liste]
print(listaSommata)

# lista di tuple con tutte le combinazioni possibili di colore e taglia
colori = ["rosso", "verde", "blu"]
taglie = ["S", "M", "L"]
combinazioni = [(colore, taglia) for colore in colori for taglia in taglie]
print(combinazioni)
