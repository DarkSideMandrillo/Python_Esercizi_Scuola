import tkinter as tk
from tkinter import filedialog


def seleziona_file():
    # Crea una finestra nascosta per la selezione del file
    root = tk.Tk()
    root.withdraw()  # Nasconde la finestra principale

    # Mostra il dialogo per la selezione del file
    file_path = filedialog.askopenfilename(
        title="Seleziona un file",
        filetypes=[("Tutti i file", "*.*"), ("File di testo", "*.txt")],
    )

    if file_path:
        print(f"Hai selezionato il file: {file_path}")
    else:
        print("Nessun file selezionato")

    return file_path


# Esempio di utilizzo
file_selezionato = seleziona_file()

if file_selezionato:
    print(f"Percorso del file selezionato: {file_selezionato}")
