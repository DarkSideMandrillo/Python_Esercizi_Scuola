import sqlite3

# Riapertura del database
conn = sqlite3.connect("siti.db")
cursor = conn.cursor()

# Selezione e stampa di tutti i dati dalla tabella
cursor.execute("SELECT * FROM siti_web")
righe = cursor.fetchall()

# Stampa dei dati
print("Contenuto della tabella 'siti_web':")
for riga in righe:
    print(f"IP: {riga[0]}, Nome sito: {riga[1]}")

# Chiusura della connessione
conn.close()
