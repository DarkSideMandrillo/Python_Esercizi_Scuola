import socket
import sqlite3
from threading import Thread

SERVER_IP = 'localhost'  # IP del server
SERVER_PORT = 22222  # porta usata per la connessione
BUFFER_SIZE = 4096  # dimensione del buffer per i dati

NOME_DB = 'operations.db'

# funzione per gestire i client connessi (gestisce la connessione con un client specifico, inviando operazioni 
# e ricevendo i risultati)
def gestione_client(client_socket, client_address):
    try:
        # richiesta per ricevere l'id del client
        client_id = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        
        if client_id not in ['1', '2']: # se l'id ricevuto non è valido chiudo la connessione
            client_socket.sendall("Id non valido".encode('utf-8'))
            client_socket.close()
            return

        # connessione al database per leggere le operazioni matematiche
        conn = sqlite3.connect(NOME_DB, check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT operation 
                       FROM operations 
                       WHERE client = ?                        
                    ''', (client_id,))
        operazioni_client = cursor.fetchall()
        conn.close()

        # controllo se ci sono delle operazioni per il client
        if not operazioni_client:
            client_socket.sendall("Nessuna operazione disponibile per questo client".encode('utf-8'))
            client_socket.close()
            return
        
        # per ogni client eseguo tutte le sue operazioni
        for operazione in operazioni_client:
            operazione = operazione[0]  # operazione è una tupla 
            client_socket.sendall(operazione.encode('utf-8'))  
            risultato = client_socket.recv(BUFFER_SIZE).decode('utf-8')  # ricevo il risultato
            print(f"{operazione} = {risultato} from {client_address[0]} - {client_address[1]}")

        # alla fine invio messaggio exit per far chiudere il client (quando non ci sono più operazioni)
        client_socket.sendall("exit".encode('utf-8'))
    except Exception as e:
        print(f"Errore nel thread per {client_address}: {e}")
    finally:
        client_socket.close()

# funzione principale del server (avvia il server e accetta connessioni dai client)
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)  # numero massimo di connessioni in coda

    try:
        while True:
            # accetta una connessione dal client  
            client_socket, client_address = server_socket.accept()

            # thread per gestire il client
            thread = Thread(target=gestione_client, args=(client_socket, client_address))
            thread.start()
    except KeyboardInterrupt:
        print("Chiusura del server...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
