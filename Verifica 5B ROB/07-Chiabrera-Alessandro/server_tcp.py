import socket
import threading
import sqlite3

HOST = '127.0.0.1'  # indirizzo ip del server (host locale)
PORTA = 65000       # porta del server

# funzione per recuperare le operazioni dal database
def carica_operazioni():
    """
    Connette al database, recupera le operazioni dalla tabella 'operazioni',
    e restituisce una lista di tuple (client_id, db_operazioni).
    """
    conn = sqlite3.connect("db_operazioni.db", check_same_thread=False)
    cur = conn.cursor()
    cur.execute("SELECT client, db_operazioni FROM db_operazioni")
    operazioni = cur.fetchall()  # ottiene tutte le operazioni
    conn.close()  # chiude la connessione al database
    return operazioni

# funzione che gestisce la connessione con un singolo client
def gestisci_client(connessione, indirizzo, operazioni):
    """
    Gestisce la comunicazione con un client.
    Invia operazioni al client, riceve i risultati e stampa l'output.
    """
    for operazione in operazioni:
        connessione.sendall(operazione[1].encode())  # invio dell'operazione
        risultato = connessione.recv(4096).decode()  # riceve il risultato
        print(f"Operazione: {operazione[1]} = {risultato} da {indirizzo[0]}:{indirizzo[1]}\n")#stampa l'operazone ed il risultato

    connessione.sendall('exit'.encode())  # comando per terminare il client
    connessione.close()# chiude il client

def main():
    """
    avvia il server, carica le operazioni dal database,
    e gestisce le connessioni dei client in modo multi-thread.
    """
    operazioni = carica_operazioni()  # carica le operazioni dal database

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # configurazione del socket del server
    server.bind((HOST, PORTA))  # associazione tra l'indirizzo e la porta al server
    server.listen()  # mette il server in ascolto
    print(f"Server in ascolto su {HOST}:{PORTA}...")

    while True:  # ciclo per accettare connessioni
        connessione, indirizzo = server.accept()  # accetta la connessione da un client
        print(f"Connessione accettata da {indirizzo}") #stampa a video che la connessione è stata accettata
        thread = threading.Thread(target=gestisci_client, args=(connessione, indirizzo, operazioni))  # avvia un thread per gestire il client
        thread.start()

if __name__ == "__main__":
    main()
