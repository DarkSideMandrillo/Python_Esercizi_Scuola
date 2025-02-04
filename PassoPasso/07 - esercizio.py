"""
Scrivi un programma in Python che esegua le seguenti operazioni:

Lettura del file: Leggi il file vendite.csv e crea una lista di dizionari 
in cui ogni dizionario rappresenta una vendita. Gestisci eventuali eccezioni 
legate alla lettura del file (es. file non trovato, errori di formattazione).

Calcolo del valore totale delle vendite:
Usa una list comprehension per calcolare il valore totale (quantità venduta × 
prezzo unitario) per ogni riga del file.
Salva i risultati in una lista di tuple nel formato (nome_prodotto, valore_totale).

Raggruppamento per categoria:
Crea un dizionario in cui le chiavi sono le categorie e i valori sono liste di prodotti 
(come tuple) con il valore totale delle vendite.

Gestione delle eccezioni:
Se il file contiene dati non validi (ad esempio, valori mancanti o non numerici), 
gestisci l'errore mostrando un messaggio e ignorando le righe problematiche.

Scrittura dei risultati:
Salva i risultati in un nuovo file analisi_vendite.txt

"""

import csv

# Percorso del file di input e output
file_input = "vendite.csv"
file_output = "analisi_vendite.txt"


# Funzione per leggere il file e gestire eventuali eccezioni
def leggi_file_vendite(file_path):
    try:
        with open(file_path, "r") as file:
            file_reader = csv.reader(file)
            header = next(file_reader)  # Legge l'intestazione
            vendite = []
            for riga in file_reader:
                try:
                    print(riga)
                    nome_prodotto, categoria, quantita_venduta, prezzo_unitario = riga
                    vendite.append(
                        {
                            "nome_prodotto": nome_prodotto,
                            "categoria": categoria,
                            "quantita_venduta": int(quantita_venduta),
                            "prezzo_unitario": float(prezzo_unitario),
                        }
                    )
                except ValueError:
                    print(f"Errore di formato nella riga: {riga}. Ignorata.")
            return vendite
    except FileNotFoundError:
        print(f"Il file '{file_path}' non è stato trovato.")
        return []


# Funzione per calcolare il valore totale delle vendite
def calcola_valori_totali(vendite):
    return [
        (
            vendita["nome_prodotto"],
            vendita["quantita_venduta"] * vendita["prezzo_unitario"],
        )
        for vendita in vendite
    ]


# Funzione per raggruppare i prodotti per categoria
def raggruppa_per_categoria(vendite):
    cat_valore_prodotto = {}
    for vendita in vendite:
        valore_totale = vendita["quantita_venduta"] * vendita["prezzo_unitario"]
        categoria = vendita["categoria"]
        if categoria not in cat_valore_prodotto:
            cat_valore_prodotto[categoria] = []
        cat_valore_prodotto[categoria].append((vendita["nome_prodotto"], valore_totale))
    return cat_valore_prodotto


# Funzione per scrivere i risultati in un file
def scrivi_risultati(file_path, cat_valore_prodotto):
    try:
        with open(file_path, "w") as file:
            for categoria, prodotti in cat_valore_prodotto.items():
                file.write(f"Categoria: {categoria}\n")
                for nome_prodotto, valore_totale in prodotti:
                    file.write(f"- {nome_prodotto}: {valore_totale:.2f}\n")
                file.write("\n")
        print(f"Risultati salvati in '{file_path}'")
    except Exception as e:
        print(f"Errore durante la scrittura del file: {e}")


def main():
    # Esecuzione del programma
    vendite = leggi_file_vendite(file_input)
    if vendite:
        # valori_totali = calcola_valori_totali(vendite)
        cat_valore_prodotto = raggruppa_per_categoria(vendite)
        scrivi_risultati(file_output, cat_valore_prodotto)


if __name__ == "__main__":
    main()
