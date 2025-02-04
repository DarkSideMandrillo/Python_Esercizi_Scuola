import csv
from functools import wraps

try:
    with open(nome_file, "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Legge l'intestazione

        for riga in reader:
            a, b, c, d = riga
except FileNotFoundError:
    a = "errore"

file.write(f"Categoria: {categoria}\n")

file_input = "vendite.csv"
file_output = "analisi_vendite.txt"

ValueError
FileNotFoundError
Exception  # errore per la scrittura del file


def funzione_decoratore(funzione_parametro):
    @wraps(funzione_parametro)
    def wrapper():
        # """ nome convenzionale - wrapper significa 'incarto, confezione' """
        print("... codice da eseguire prima di 'funzione_parametro' ...")
        funzione_parametro()
        print("... codice da eseguire dopo di 'funzione_parametro' ...")

    return wrapper


@funzione_decoratore
def mia_funzione():
    print("Hello World!")


mia_funzione()
