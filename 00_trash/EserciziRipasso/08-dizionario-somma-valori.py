dizionari = [
    {"a": 1, "e": 1, "d": 10},
    {"b": 9},
    {"e": 1, "b": 5, "d": 8, "a": 2, "c": 3},
    {"e": 3, "b": 8, "c": 8, "d": 7, "a": 8},
    {"c": 9, "d": 1},
]
sommaDizionari = {}

for dizionario in dizionari:
    for key, value in dizionario.items():
        if key in sommaDizionari:
            sommaDizionari[key] += value
        else:
            sommaDizionari[key] = value

print(sommaDizionari)


dizionari = [
    {"a": 1, "e": 1, "d": 10},
    {"b": 9},
    {"e": 1, "b": 5, "d": 8, "a": 2, "c": 3},
    {"e": 3, "b": 8, "c": 8, "d": 7, "a": 8},
    {"c": 9, "d": 1},
]
sommaDizionari = {}

for dizionario in dizionari:
    for key, value in dizionario.items():
        # sommaDizionari.get(key, 0): Se la chiave key non esiste in sommaDizionari,
        # restituisce 0, così puoi sommare direttamente senza bisogno dell'if.
        sommaDizionari[key] = sommaDizionari.get(key, 0) + value

print(sommaDizionari)
