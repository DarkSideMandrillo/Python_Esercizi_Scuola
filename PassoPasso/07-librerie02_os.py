import os
print(os.getcwd())  # Output: percorso della directory corrente

os.chdir('./zDirProvas')
print(os.getcwd())  # Output: nuova directory corrente

files = os.listdir('.')
print(files)  # Output: lista dei file e directory nella directory corrente

# Creare un file di esempio
with open('file_da_eliminare.txt', 'w') as f:
    f.write('Contenuto del file.')

# Eliminare il file
os.remove('file_da_eliminare.txt')
print('File eliminato.')

# Scrivere su un file (modalità 'w' - sovrascrive il file se esiste)
with open('esempio.txt', 'w') as file:
    file.write('Questo è un esempio di scrittura su file.\n')
    file.write('Questa è una nuova riga.')

# Aggiungere dati a un file esistente (modalità 'a')
with open('esempio.txt', 'a') as file:
    file.write('\nAggiungo questa riga alla fine del file.')

# Leggere tutto il contenuto del file
with open('esempio.txt', 'r') as file:
    contenuto = file.read()
    print(contenuto)

# Leggere il file riga per riga
with open('esempio.txt', 'r') as file:
    for riga in file:
        print(riga.strip())  # `strip()` rimuove eventuali spazi bianchi o newline

# Leggere tutte le righe come una lista
with open('esempio.txt', 'r') as file:
    righe = file.readlines()
    print(righe)  # Output: lista di righe


# Aprire un file in modalità lettura e scrittura ('r+'): Il file deve esistere
with open('esempio.txt', 'r+') as file:
    contenuto = file.read()  # Legge il contenuto attuale
    file.write('\nNuova riga aggiunta in modalità r+.')

# Aprire un file in modalità scrittura e lettura ('w+'): il file viene creato se non esiste
with open('nuovo_file.txt', 'w+') as file:
    file.write('Questo sovrascrive il file.\n')
    file.seek(0)  # Torna all'inizio del file per leggere ciò che è stato scritto
    contenuto = file.read()
    print(contenuto)

