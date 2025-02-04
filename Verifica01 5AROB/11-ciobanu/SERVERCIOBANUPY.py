import socket
import threading
import sqlite3
from datetime import datetime

HOST = "127.1.1.1"  #!! non è localhost
PORT = 8000


def inizializza_database():  #!! non devi creare viste o tabelle
    conn = sqlite3.connect("fiumi.db")
    cur = conn.cursor()
    cur.execute(
        """
        CREATE WIEW AS  livelli (
            id_stazione INTEGER PRIMARY KEY AUTOINCREMENT,
            fiume TEXT NOT NULL,
            localita TEXT NOT NULL ,
            livello_guardia REAL
        )
    """
    )
    conn.commit()


def gestisci_messaggio(addr, data):
    conn = sqlite3.connect("fiumi.db")  #!! connessione gia aperta
    cur = conn.cursor()
    cur.execute(
        """SELECT * FROM livelli WHERE id_stazione = ?", (data["id"],)"""
    )  #!! errore di sintassi
    stazione = cur.fetchone()
    stazione.split("-")
    conn.close()

    if stazione:
        id = stazione[1]
        livello = stazione[2]
        data_ora = stazione[3]
        livello_guardia1 = 30
        livello_guardia2 = 70
        if livello < 0.3 * livello_guardia1:
            risposta = "Ricezione avvenuta"
        elif (
            0.3 * livello_guardia1 <= livello < 0.7 * livello_guardia2
        ):  #!! errore proporzione
            risposta = "Ricezione avvenuta"  #!! devi stampare ogni volta
            print(f"Pericolo su:  {fiume}, {localita} ({data_ora})")
        else:
            risposta = "allarme"
            print(f" Pericolo in corso su {fiume}, {localita} ({data_ora})")
    else:
        risposta = "Stazione non trovata"

    conn.close()
    return risposta


def main():
    inizializza_database()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)  #!! possono esserci piu connessioni
    print(f"Server in ascolto su {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        messaggio = gestisci_messaggio(conn, addr)
        server.sendall(messaggio.decode())


if __name__ == "__main__":
    main()
