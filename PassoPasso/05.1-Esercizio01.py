# Hai a disposizione un dataset che rappresenta l’inventario di un negozio sotto 
# forma di una lista di dizionari. Ogni dizionario rappresenta un prodotto e contiene le seguenti informazioni:
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
        "quantita": 20,
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
prodotti_economici = []
print(prodotti_economici)

# Valore Totale dell'Inventario:
# Calcola il valore totale sommato dei prodotti
valore_inventario_tot = sum()

# Valore Totale per ogni prodotto:
# Crea una lista di tuple con nome e costo totale
valore_prodotto = []

# Crea un set con l'elenco di categorie
categorie_uniche = {}

# Prodotti da Riordinare: Un prodotto deve essere riordinato se la sua
# quantità è inferiore a 10.
prodotti_riordinare = []

# Crea un dizionario con categorie e liste di tuple (nome prodotto, valore totale)
# Serve usare il set creato in precedenza
cat_valore_prodotto = {}

# DIFFICILE
# Valore Totale dell'Inventario per categoria:
# Crea un dizionario in cui le chiavi sono le categorie e i valori sono
# il totale del valore dei prodotti # appartenenti a quella categoria.
