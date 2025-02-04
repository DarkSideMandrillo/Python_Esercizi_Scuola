import os
import datetime


# Decoratore per loggare le operazioni
def log_operazioni(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as log_file:
            log_file.write(
                f"Funzione '{func.__name__}' eseguita alle {datetime.datetime.now()}\n"
            )
        return func(*args, **kwargs)

    return wrapper


@log_operazioni
def leggi_file_inventario(file_path):
    """Legge i dati da un file di inventario e li restituisce come lista di tuple."""
    inventario = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Il file {file_path} non esiste.")

    with open(file_path, "r") as file:
        for riga in file:
            nome, categoria, quantita, prezzo = riga.strip().split(",")
            inventario.append((nome, categoria, int(quantita), float(prezzo)))
    return inventario


@log_operazioni
def calcola_valori_totali(inventario):
    """Calcola il valore totale per ogni articolo."""
    return [(nome, quantita * prezzo) for nome, _, quantita, prezzo in inventario]


@log_operazioni
def scrivi_valori_totali(file_path, valori_totali):
    """Scrive i valori totali in un file."""
    with open(file_path, "w") as file:
        for nome, valore in valori_totali:
            file.write(f"{nome},{valore:.2f}\n")


@log_operazioni
def stampa_contenuto_file(file_path):
    """Stampa il contenuto di un file."""
    with open(file_path, "r") as file:
        print(file.read())


# Percorsi dei file
file_inventario = "inventario.txt"
file_valori_totali = "valori_totali.txt"

# Esecuzione del programma
try:
    inventario = leggi_file_inventario(file_inventario)
    valori_totali = calcola_valori_totali(inventario)
    scrivi_valori_totali(file_valori_totali, valori_totali)
    stampa_contenuto_file(file_valori_totali)
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(f"Errore inaspettato: {e}")
