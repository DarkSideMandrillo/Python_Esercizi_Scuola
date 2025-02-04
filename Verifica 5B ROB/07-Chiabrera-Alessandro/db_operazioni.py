import sqlite3

# connessione al database (crea il file se non esiste)
conn = sqlite3.connect("db_operazioni.db")
cur = conn.cursor()

# creazione della tabella 'db_operazioni'
cur.execute(
    """
CREATE TABLE IF NOT EXISTS db_operazioni (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificatore univoco per ogni operazione
    client INTEGER NOT NULL,  -- ID del client (1, 2, 3, ecc.)
    db_operazioni TEXT NOT NULL  -- L'operazione matematica da eseguire
)
"""
)

# inserimento di dati nella tabella 'db_operazioni'#!! ma così le op le inserisci. Anche se ci sono gia
cur.execute(
    "INSERT INTO db_operazioni (client, db_operazioni) VALUES (1, '5+6*(454483+3447)')"
)
cur.execute(
    "INSERT INTO db_operazioni (client, db_operazioni) VALUES (2, '5*11738829')"
)
cur.execute(
    "INSERT INTO db_operazioni (client, db_operazioni) VALUES (2, '4+5+6+7/(8573*337)+3-23')"
)
cur.execute("INSERT INTO db_operazioni (client, db_operazioni) VALUES (1, '56*43')")
cur.execute(
    "INSERT INTO db_operazioni (client, db_operazioni) VALUES (1, '(4566-336364)/5')"
)


conn.commit()  # salvataggio delle modifiche nel database

# chiusura della connessione
conn.close()

print("Database e tabella 'db_operazioni' creati con successo!")
