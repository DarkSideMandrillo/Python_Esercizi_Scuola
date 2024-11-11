import sqlite3

# Connessione al database
conn = sqlite3.connect("siti.db")
cursor = conn.cursor()

# Creazione della tabella
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS siti_web (
    ip TEXT PRIMARY KEY,
    nome_sito TEXT NOT NULL,
    porte_aperte TEXT
)
"""
)


# Dati da inserire (15 indirizzi IP con nomi di siti)
dati = [
    ("127.0.0.1", "example1.com"),
    ("192.168.1.2", "example2.com"),
    ("192.168.1.3", "example3.com"),
    ("192.168.1.4", "example4.com"),
    ("192.168.1.5", "example5.com"),
    ("192.168.1.6", "example6.com"),
    ("192.168.1.7", "example7.com"),
    ("192.168.1.8", "example8.com"),
    ("192.168.1.9", "example9.com"),
    ("192.168.1.10", "example10.com"),
    ("192.168.1.11", "example11.com"),
    ("192.168.1.12", "example12.com"),
    ("192.168.1.13", "example13.com"),
    ("192.168.1.14", "example14.com"),
    ("192.168.1.15", "example15.com"),
]

# Inserimento dei dati
cursor.executemany(
    """
INSERT OR IGNORE INTO siti_web (ip, nome_sito) VALUES (?, ?)
""",
    dati,
)

# Salvataggio delle modifiche
conn.commit()

# Chiusura della connessione
conn.close()

print("Tabella 'siti_web' creata e popolata con successo.")
