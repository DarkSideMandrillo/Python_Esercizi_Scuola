import csv, os

prodotti = []

nome_file = "vendite.csv"

try:
    with open(nome_file, "r") as file:
        reader = csv.DictReader(file)

        for riga in reader:
            try:
                prodotto = {
                    "nome": riga["nome_prodotto"].strip(),
                    "categoria": riga["categoria"].strip(),
                    "quantita": int(riga["quantita_venduta"]),
                    "prezzo": float(riga["prezzo_unitario"]),
                }
                prodotti.append(prodotto)
            except (ValueError, KeyError):
                print(f"Dati non validi nella riga: {riga}")
except FileNotFoundError:
    print("Errore: File non trovato.")

# Visualizza i primi 5 prodotti caricati
for prodotto in prodotti[:5]:
    print(prodotto)
