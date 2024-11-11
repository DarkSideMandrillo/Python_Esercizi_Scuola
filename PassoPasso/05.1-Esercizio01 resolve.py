# Hai a disposizione un dataset che rappresenta l’inventario di un negozio sotto forma di una lista di dizionari. Ogni dizionario rappresenta un prodotto e contiene le seguenti informazioni:
# "nome": il nome del prodotto (stringa)
# "categoria": la categoria a cui appartiene (es. "elettronica", "abbigliamento", "cucina") (stringa)
# "prezzo": il prezzo del prodotto (numero float)
# "quantita": la quantità disponibile in magazzino (intero)


prodotti = [
    {
        "nome": "televisore",
        "categoria": "elettronica",
        "prezzo": 499.99,
        "quantita": 10,
    },
    {
        "nome": "frullatore",
        "categoria": "cucina",
        "prezzo": 79.99,
        "quantita": 7,
    },
    {
        "nome": "maglietta",
        "categoria": "abbigliamento",
        "prezzo": 15.99,
        "quantita": 100,
    },
    {
        "nome": "laptop",
        "categoria": "elettronica",
        "prezzo": 899.99,
        "quantita": 5,
    },
    {
        "nome": "pentola",
        "categoria": "cucina",
        "prezzo": 29.99,
        "quantita": 50,
    },
]

# Prodotti in Offerta:
# Crea una lista di nomi di prodotti il cui prezzo è inferiore a 100 euro.
prodotti_economici = [
    sotto_100["nome"] for sotto_100 in prodotti if sotto_100["prezzo"] < 100
]
print(prodotti_economici)

# Valore Totale dell'Inventario:
# Calcola il valore totale sommato dei prodotti
valore_inventario_tot = sum(
    [prodotto["prezzo"] * prodotto["quantita"] for prodotto in prodotti]
)
print(valore_inventario_tot)

# Valore Totale per ogni prodotto:
# Crea una lista di tuple con nome e costo totale
valore_prodotto = [
    (prodotto["nome"], prodotto["prezzo"] * prodotto["quantita"])
    for prodotto in prodotti
]
print(valore_prodotto)


# Elenco di categorie
categorie_uniche = {prodotto["categoria"] for prodotto in prodotti}
print("\n", categorie_uniche, "\n")

# Crea un dizionario con categorie e liste di tuple (nome prodotto, valore totale) usando
# list comprehension
# {p["categoria"] for p in prodotti} - Crea un set di categorie

cat_valore_prodotto = {
    categoria: [
        (prodotto["nome"], prodotto["prezzo"] * prodotto["quantita"])
        for prodotto in prodotti
        if prodotto["categoria"] == categoria
    ]
    for categoria in {p["categoria"] for p in prodotti}
}
print("\n", cat_valore_prodotto, "\n")


# Valore Totale dell'Inventario per categoria:
# Calcola il valore totale dell’inventario per ciascuna categoria di prodotto.
# Il valore di un prodotto è dato da prezzo * quantita. Crea un dizionario in
# cui le chiavi sono le categorie e i valori sono il totale del valore dei prodotti
# appartenenti a quella categoria. Usa una list comprehension.
valore_inventario_cat = {
    categoria: sum(
        [
            prodotto["prezzo"] * prodotto["quantita"]
            for prodotto in prodotti
            if prodotto["categoria"] == categoria
        ]
    )
    for categoria in {prodotto["categoria"] for prodotto in prodotti}
}
print(valore_inventario_cat)

# Prodotti da Riordinare: Un prodotto deve essere riordinato se la sua
# quantità è inferiore a 10. Crea una lista di dizionari contenenti solo i
# prodotti che devono essere riordinati. Ogni dizionario deve mantenere
# tutte le informazioni originali del prodotto. Usa una list comprehension.
prodotti_riordinare = [prodotto for prodotto in prodotti if prodotto["quantita"] < 10]
print(prodotti_riordinare)

# Sconto sui Prodotti di una Categoria: Applica uno sconto del 10% a tutti
# i prodotti appartenenti alla categoria "elettronica". Aggiorna la lista
# di prodotti in modo che i prezzi siano ridotti del 10% solo per i prodotti
# in questa categoria. Usa una list comprehension per generare la
# lista aggiornata.
prodotti_scontati = []

# Rapporto di Disponibilità: Genera una lista di stringhe che riportano il
# nome del prodotto seguito da "disponibile" o "non disponibile" in base
# alla quantità. Se la quantità è maggiore di 0, il prodotto è considerato
# disponibile. Esempio: "televisore: disponibile", "laptop: non disponibile".
# Usa una list comprehension.
rapporto_disponibilita = []
